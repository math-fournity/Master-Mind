# Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity

**arXiv ID**: 2607.25139v1
**Authors**: Katerina Tang, Daniel Kaiser, William Thompson, Jean-Gabriel Young, Laurent Hébert-Dufresne, Nicholas W. Landry
**Published**: 2026-07-27
**Categories**: physics.soc-ph, cs.SI, math.ST
**Comments**: 15 pages, 7 figures
**HTML URL**: https://arxiv.org/html/2607.25139v1

## Abstract

Simple and complex contagions differ mechanistically; multiple exposures act synergistically in the latter but independently in the former. Yet correlated mixtures of simple contagions may appear complex when inferring global contagion rules, a phenomenon we call "emergent complexity." We present a measure of contagion complexity and an inferential framework for estimating mixtures of nonparametric contagion rules from time-series data. Our work reframes past studies on complex contagion by offering heterogeneous mixtures of simple contagions as an alternative explanation.

## Full Text

Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.25139v1 [physics.soc-ph] 27 Jul 2026

## Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneityKaterina TangThese authors contributed equally to this work. Correspondence should be addressed to daniel.kaiser@virginia.edu.Center for Applied Mathematics, Cornell University, Ithaca, New York 14853, USADaniel KaiserThese authors contributed equally to this work. Correspondence should be addressed to daniel.kaiser@virginia.edu.Department of Biology, University of Virginia, Charlottesville, Virginia 22903, USAWilliam ThompsonThese authors contributed equally to this work. Correspondence should be addressed to daniel.kaiser@virginia.edu.Vermont Complex Systems Institute, University of Vermont, Burlington, Vermont 05405, USAJean-Gabriel YoungVermont Complex Systems Institute, University of Vermont, Burlington, Vermont 05405, USADepartment of Mathematics & Statistics, University of Vermont, Burlington, Vermont 05405, USALaurent Hébert-DufresneVermont Complex Systems Institute, University of Vermont, Burlington, Vermont 05405, USADepartment of Computer Science, University of Vermont, Burlington, Vermont 05405, USASanta Fe Institute, Santa Fe, NM 87501, USAComplexity Science Hub Vienna, A-1080 Vienna, AustriaNicholas W. LandryDepartment of Biology, University of Virginia, Charlottesville, Virginia 22903, USAVermont Complex Systems Institute, University of Vermont, Burlington, Vermont 05405, USASchool of Data Science, University of Virginia, Charlottesville, Virginia 22903, USA

## Abstract

Simple and complex contagions differ mechanistically; multiple exposures act synergistically in the latter but independently in the former.
Yet correlated mixtures of simple contagions may appear complex when inferring global contagion rules, a phenomenon we call “emergent complexity.”
We present a measure of contagion complexity and an inferential framework for estimating mixtures of nonparametric contagion rules from time-series data.
Our work reframes past studies on complex contagion by offering heterogeneous mixtures of simple contagions as an alternative explanation.

## 

Introduction—The spread of information, beliefs, and behaviors, together referred to as “social contagion” is often modeled as a complex contagion, in which multiple exposures act synergistically to promote adoption[27,5].
This mechanism is often presented in contrast to simple contagion mechanisms, where one exposure is sufficient for infection and successive exposures independently contribute to the probability of a node becoming infected.
Complex contagions can exhibit qualitatively different dynamics from simple contagions, such as discontinuous transitions[6], superexponential spread[12], different responses to modular network structure[21,23], and distinct optimal intervention strategies[7].

These differences have motivated a growing literature on inferring the contagion rules underlying observed dynamics.
Existing statistical methods, however, often either assumea priorithat the transmission mechanism is known[24]or simply seek to explain whether complex or simple contagion rules better explain infection data in synthetic[4,2]and empirical[20,29]settings.
The simple and complex contagion paradigms can be unified by specifying infection probabilities through acontagion kernelmapping the number of infected neighbors to an infection probability, i.e., a dose-response curve[6].
Recent work introduced a Bayesian inferential method for estimating nonparametric contagion kernels from time-series data[17]; however, this study assumed every individual was characterized by the same contagion kernel.

This kernel-based view is useful, but contagion kernel inference is not the same as mechanism selection.
Several models have been shown to map to complex contagion dynamics despite having simple contagion rules: contagions with heterogeneous parameters across space[25], contagions with memory effects[3,26], or synergistic contagions[12,10].
In the first example, the transmission rate of a simple contagion varies across settings, and ignoring this variation leads to inference of a nonlinear contagion kernel[25]because a local increase in incidence not only means more infectious cases but also suggests a higher local transmission rate[11].
Interacting contagions provide another example: if one infection changes the susceptibility to or transmissibility of another, then unobserved co-infection states make the transmission rate of the observed contagion appear to vary with prevalence, even when the underlying mechanisms are simple[12].
Across these studies, the existence of heterogeneous kernels and uncertainty in parameters is the source of what we callemergent contagion complexity, reflecting that contagion dynamics can appear governed by a complex kernel when, in reality, they are generated by a mixture of simple (or simpler) contagion kernels.

In this Letter, we distinguish two sources of apparent contagion complexity.
First, a contagion kernel may depart from the independent-exposure form of simple contagions, indicatingmechanistic complexityin the underlying transmission rule.
Second, a kernel may appear non-simple because it aggregates over heterogeneous subpopulations with different kernels and structured mixing across the network; we refer to this asemergent complexity.
We introduce a score for apparent kernel complexity, use it to characterize sufficient conditions under which correlated heterogeneity makes a global kernel appear complex, and then detail a method by which a complex contagion kernel may be disambiguated from a mixture of simple contagion kernels.
That is, we aim to distinguish mechanistic complexity from emergent complexity.
Our findings suggest that complexity may be thought of as an emergent property of contagions and help reframe past empirical work on complex contagions.

## 

Heterogeneous contagion kernel model and inference—We generalize the susceptible-infected-susceptible (SIS) contagion process described in Ref.[17]to model heterogeneous contagion kernels.
At each timet,t,a susceptible nodeiiis infected with probabilityci​(ν),c_{i}(\nu),whereν\nuis the number of infected neighbors of nodeii.
An infected node recovers with probabilityγ.\gamma.Each node’s contagion kernelci:ℕ→[0,1]c_{i}:\mathbb{N}\to[0,1]can be represented in nonparametric form as a vector𝒄i=[ci,1,…,ci,N−1]T,\bm{c}_{i}={[c_{i,1},\dots,c_{i,N-1}]}^{\mathrm{T}},whereci,νc_{i,\nu}denotes nodeii’s probability of infection byν\nuinfected neighbors andNNis the number of nodes in the network.
This flexible representation allows us to consider simple and complex contagion kernels as special cases.
For simple contagions, in which exposures are independent and infect a node with probabilityβ\beta,c​(ν)=1−(1−β)νc(\nu)=1-(1-\beta)^{\nu}.
For threshold contagion, in which a node adopts deterministically ifτ\tauneighbors have adopted,c​(ν)=𝟙ν≥τc(\nu)=\mathbbm{1}_{\nu\geq\tau}, where𝟙\mathbbm{1}is the indicator function.

To describe the time evolution of this contagion process mathematically, we track the states of all nodes in vector𝒙​(t)=[x1​(t),…,xN​(t)]T,\bm{x}(t)={[x_{1}(t),\dots,x_{N}(t)]}^{\mathrm{T}},wherexi​(t)x_{i}(t)is the infection status of individualiiat timet,t,withxi​(t)=0x_{i}(t)=0andxi​(t)=1x_{i}(t)=1representing susceptible and infected states, respectively.
The collection of state vectors at timest=0,1,…,Tt=0,1,\dots,Tis matrix𝑿=[𝒙​(0),𝒙​(1),…,𝒙​(T)].\bm{X}=[\bm{x}(0),\bm{x}(1),\dots,\bm{x}(T)].

From previous work[17], the likelihood of a series of states𝑿\bm{X}given network adjacency matrix𝑨\bm{A}(assumed to be known) isP​(𝑿∣𝑨,γ,{𝒄i})∝∏i=1N∏ν=1N−1ci​(ν)Mi,ν​(1−ci​(ν))Ni,ν,P(\bm{X}\mid\bm{A},\gamma,\{\bm{c}_{i}\})\propto\prod_{i=1}^{N}\prod_{\nu=1}^{N-1}c_{i}(\nu)^{M_{i,\nu}}(1-c_{i}(\nu))^{N_{i,\nu}},(1)

whereγ\gammais the recovery rate,𝒄i\bm{c}_{i}is the nonparametric contagion vector associated with nodeii, andMi,νM_{i,\nu}andNi,νN_{i,\nu}are the number of infection and non-infection events, respectively, for nodeiiwhen it hasν\nuinfected neighbors.
The associated matrices,𝑴\bm{M}and𝑵\bm{N}, fully summarize the dynamics and are the only inputs required for inference.

We model node-specific contagion vectors𝒄i\bm{c}_{i}as draws from a finite mixture of nonparametric kernel modes.
That is, each nodeiibelongs to a single latent kernel classzi∈{1,…,K}z_{i}\in\{1,\dots,K\}and its logit-scale kernelc~i​(ν)=logit⁡ci​(ν)∈ℝ\tilde{c}_{i}(\nu)=\operatorname{logit}c_{i}(\nu)\in\mathbb{R}varies around a class-level logit-scale modeμ~zi​(ν)\tilde{\mu}_{z_{i}}(\nu),c~i​(ν)∼Normal​(μ~zi​(ν),σ).\tilde{c}_{i}(\nu)\sim\mathrm{Normal}\,\left(\tilde{\mu}_{z_{i}}(\nu),\sigma\right).

We constrain eachμk\mu_{k}to be monotonic inν\nu, but our results hold without this assumption for sufficient data.
Details on this constraint and an expanded discussion of the mixture model are in Appendix A.

## 

Emergent complexity in networks with community structure—We examine conditions under which emergent contagion complexity may arise by first considering networks generated from a two-block stochastic block model (SBM)[14,15,16].
This model hasNNnodes split evenly between blocks, an expected mean degree⟨k⟩\langle k\rangle, and within- and between-block edge probabilities ofpin=(1+ε)​⟨k⟩/(N−1),p_{\mathrm{in}}=(1+\varepsilon)\langle k\rangle/(N-1),andpout=(1−ε)​⟨k⟩/(N−1)p_{\mathrm{out}}=(1-\varepsilon)\langle k\rangle/(N-1), respectively[16].
In this model,ε\varepsiloncontrols community separation; whenε=0\varepsilon=0, we obtain an Erdős-Rényi network and whenε=1\varepsilon=1, we obtain a network with two disconnected communities.
A network generated from this model withN=256N=256,⟨k⟩=18\langle k\rangle=18, and a separation ofε=0.9\varepsilon=0.9is shown inFigure1(a).

Each node is assigned simple kernelc(g)​(ν)=1−(1−βg)ν,c^{(g)}(\nu)=1-(1-\beta_{g})^{\nu},(2)

whereg∈{1,2}g\in\{1,2\}is the node’s community label.
We letβ1≤β2\beta_{1}\leq\beta_{2}so that the only mechanistic difference between communities is their per-contact infectivity.
InFigure1,γ=0.1\gamma=0.1,β1=0.01\beta_{1}=0.01, andβ2=0.04\beta_{2}=0.04.
When this community-level heterogeneity is ignored, and a global (i.e., single-component,K=1K=1) nonparametric kernel mode is inferred, the estimate appears sigmoidal, as seen inFigure1(b), which is often associated with complex contagion[6,1].
In this case, however, both ground-truth kernels are simple.Figure 1:Mixtures of simple contagions appear complex when heterogeneous infection probabilities are correlated.(a) A two-community stochastic block model withN=256N=256,⟨k⟩=18,\langle k\rangle=18,andε=0.9\varepsilon=0.9. Node colors indicate each individual’s (unknown) underlying simple infection kernel—one ofc(1)​(ν)c^{(1)}(\nu)orc(2)​(ν)c^{(2)}(\nu), shown in panel b.
(b) Infection probabilityc​(ν)c(\nu)given thatν\nuneighbors are infected. The true underlying simple contagion kernels,c(1)​(ν)c^{(1)}(\nu)andc(2)​(ν)c^{(2)}(\nu), are of the form1−(1−βg)ν1-(1-\beta_{g})^{\nu}withβ1=0.01\beta_{1}=0.01andβ2=0.04\beta_{2}=0.04. Inferring a global kernel mode yields the solid black curve, which exhibits a sigmoidal shape commonly associated with complex contagion kernels.

The apparent complexity of this global kernel arises from a correlation between the exposure level,ν\nu, and the latent community-specific infectivity.
Infections at lowν\nu-values come predominantly fromβ1\beta_{1}nodes, which sustain fewer infections within their community, while infections at highν\nuare dominated byβ2\beta_{2}nodes, which sustain more infections within their community.
Therefore, fitting a single kernel mode to these data averages over the underlying simple kernels in an exposure-dependent way, and we recover a sigmoidal kernel.
This is a network-structured analogue of the nonlinear bias identified in Ref.[25], where apparent complexity emerges because exposure becomes a proxy for unobserved transmission heterogeneity.

In our model, the correlation between individual kernels and community structure is tunable, allowing us to explore how aligned kernel and community assignments must be for the global kernel to exhibit emergent complexity.
We measure the complexity of an inferred contagion kernel by quantifying its departure from a simple contagion form [Eq. (2)], adjusted to account for posterior uncertainty.
Specifically, we compute the Mahalanobis distance from a simple reference kernel parameterized by the posterior mean infectivityβ¯sc\bar{\beta}_{\mathrm{sc}}of a simple model inferred from the same data.
We subtract the contribution expected from posterior spread alone and divide by that posterior-uncertainty baseline.
The resultingcomplexity score,DD, measures the excess squared distance from the simple contagion reference as a fraction of the posterior-uncertainty baseline.
That is,D=0D=0indicates no departure beyond posterior spread, whileD≥1D\geq 1indicates that the systematic departure is at least as large as the posterior-uncertainty baseline.
For more details, see Appendix B.

The complexity score allows us to find sufficient structural and dynamical conditions under which exposure becomes informative about latent infectivity in this two-block SBM.
We first explore the influence of community separation and kernel-community alignment.
Here,ω∈[0,0.5]\omega\in[0,0.5]represents the probability that a node’s kernel assignment is “flipped” relative to its community label.
Kernels are perfectly aligned with communities whenω=0\omega=0[as inFigure1(a)]; kernels are assigned independent of community labels whenω=0.5\omega=0.5.Figure2(a) shows that emergent complexity requires both ingredients.
When communities are weakly separated, or when kernels are assigned sufficiently at random across communities, the global kernel mode remains close to a simple contagion.
Asε\varepsilonincreases andω\omegadecreases, the exposure level,ν\nu, becomes increasingly predictive of the latent kernel, and the inferred global kernel no longer appears simple.

At fixedε=0.9\varepsilon=0.9, the inferred kernel modes demonstrate this transition asω\omegadecreases [Figure2(b)].
When kernel assignments are randomized across communities (ω=0.5\omega=0.5), the global mode is close to a pointwise average of the two underlying kernels.
As kernel assignments become increasingly aligned with the underlying communities, this average becomes exposure-dependent, forcing a transition between theβ1\beta_{1}andβ2\beta_{2}kernels;
the result is a sigmoidal kernel.Figure 2:Emergent complexity in the two-block(ε,δ)(\varepsilon,\delta)-stochastic block model withN=256N=256,⟨k⟩=18\langle k\rangle=18.Each heatmap cell averages 10 simulations. (a) The complexity score,DD, of inferred global kernel mode with respect to community separation (ε\varepsilon) and block-flip probability (ω\omega). We fixβ1=0.01\beta_{1}=0.01andβ2=0.04.\beta_{2}=0.04.(b) The posterior mean global kernel modes at fixedε=0.9\varepsilon=0.9for varyingω\omega, with 90% highest density interval (HDI) shading. Dashed curves show the ground-truth simple kernels. Kernels correspond to(ε,ω)(\varepsilon,\omega)combinations marked in panel (a). (c) The complexity score,DD, of the inferred global kernel mode with respect to density imbalanceδ\deltaand kernel contrastrβ≡β2/β1r_{\beta}\equiv\beta_{2}/\beta_{1}with fixedε=0.9\varepsilon=0.9andω=0.1\omega=0.1. The(δ,rβ)(\delta,r_{\beta})combination used in (a) is marked. (d) The posterior mean global kernel modes at fixedrβ=5r_{\beta}=5and two values ofδ\delta, with 90% HDI shading. Kernels correspond to(rβ,δ)(r_{\beta},\delta)combinations marked in panel (c).

This experiment assumes that the two communities have equal expected degrees, which is rarely the case in empirical networks[19].
To test whether the same mechanism persists when the communities have unequal densities, we introduce density imbalance parameterδ∈[−1,1]\delta\in[-1,1].
Keeping the between-block probabilitypoutp_{\mathrm{out}}fixed, we multiply the within-block probabilitypinp_{\mathrm{in}}by(1+δ)(1+\delta)in block 1 and by(1−δ)(1-\delta)in block 2 so thatδ>0\delta>0makes block 1 denser than block 2, and the opposite is true forδ<0\delta<0.
We fixε=0.9\varepsilon=0.9andω=0.1\omega=0.1, values for whichFigure2(a) predicts emergent complexity, and vary bothδ\deltaand the kernel contrastrβ≡β2/β1.r_{\beta}\equiv\beta_{2}/\beta_{1}.Figure2(c) shows that—unsurprisingly—a sufficiently large contrast between the two simple kernels is necessary.
Whenrβr_{\beta}is close to 1, the population is effectively homogeneous, and the global kernel remains simple.
For largerrβr_{\beta}, density imbalance can greatly amplify emergent complexity by separating the exposure distributions of the two latent kernel classes, makingν\numore informative about community-specific infectivity.

The two high-complexity regions inFigure2(c) correspond to distinct non-simple kernel shapes.
Forδ<0,\delta<0,the density imbalance reinforces the mechanism described above: high-exposure observations are concentrated amongβ2\beta_{2}nodes, producing the same sigmoidal aggregate kernel [Figure2(d)].
Forδ>0,\delta>0,theβ1\beta_{1}community is denser than theβ2\beta_{2}community.
Consequently, the inferred kernel grows quickly at low exposure, flattens, and rises again—more slowly—at largerν\nu.
Between these two regimes, we see a low-complexity region whose location shifts to largerδ\deltaasrβr_{\beta}increases.
Increasingβ2\beta_{2}increases the typical exposure level in theβ2\beta_{2}block, so a larger (positive)δ\deltais needed to densify theβ1\beta_{1}block and restore overlap between the two exposure distributions.
See the Supplemental Material for more details.

Notably, emergent complexity is not limited to the canonical, threshold-like signal of peer reinforcement [Figure2(d)]: correlated heterogeneity generates a broader class of global kernels whose shape depends on how network structure maps latent contagion types onto exposure levels.
The same mechanism also arises beyond idealized block models: in the Supplemental Material, we observe emergent complexity on an empirical network.

## 

Disentangling mechanistic and emergent complexity—The complexity score identifies when an inferred kernel mode departs from the simple contagion family, but it does not distinguish emergent complexity from mechanistic complexity.
A non-simple global kernel mode could reflect a genuinely complex contagion rule shared by all nodes, or it could arise from aggregating over heterogeneous subpopulations with simpler rules.
To distinguish these possibilities, we use node-level cross-validation (CV) to select the number of mixture componentsKK.Figure 3:Cross-validation distinguishes a single complex kernel from a heterogeneous mixture of simple kernels in a two-block SBM withε=0.9\varepsilon=0.9.(a) Mean held-out log pointwise predictive density (LPPD) per node under 5-fold cross-validation with respect to number of mixture components,KK. For data generated by one complex kernel, the 1-SE rule selectsK=1K=1; for data generated by two simple kernels, the 1-SE rule selectsK=2K=2. (b,c) Inferred kernel mode(s) with 90% HDI shading for data generated by one complex kernel, shown in gray. (d,e) Inferred kernel mode(s) with 90% HDI shading for data generated by two simple kernels, shown in gray.

For each candidateK=1,…,KmaxK=1,\dots,K_{\max}, we performkk-fold cross-validation over nodes.
We compute the exposure-count matrices𝑴\bm{M}and𝑵\bm{N}from the full observed time series on the complete network, then hold out rows of these matrices from the likelihood.
Thus, held-out nodes’ transition counts are excluded from training, but their observed states still contribute to neighboring nodes’ exposure counts.
We score each model by the mean held-out log pointwise predictive density[28]per node across folds, marginalizing over each held-out node’s latent component assignmentziz_{i}.
Because unsupported components typically receive negligible weight or duplicate existing modes, CV scores tend to plateau.
We therefore select the smallestKKwhose CV score lies within one standard error of the maximum[9]; see Appendix C for more information.

Figure3demonstrates that node-level CV can distinguish a shared non-simple kernel from a heterogeneous mixture of simpler kernels in two-block SBMs with strong community separation(ε=0.9)(\varepsilon=0.9)and strongly aligned kernel assignments(ω=0.1)(\omega=0.1).
When the data are generated by a single complex kernel, additional mixture components do not improve held-out predictive performance, and the 1-SE rule consistently selectsK=1K=1[Figure3(a)].
The selected model therefore recovers a single population-level non-simple contagion rule [Figure3(b)].
In the over-specifiedK=2K=2model, one component recovers the same kernel, while the extra component is only weakly identified: its posterior is diffuse, and its mixture weight is negligible [Figure3(c)].

In contrast, when the data are generated by two simple kernels, the CV score increases sharply fromK=1K=1toK=2K=2and then plateaus [Figure3(a)].
TheK=1K=1model aggregates the two subpopulations into an exposure-dependent average, producing a complex global kernel [Figure3(d)].
TheK=2K=2model instead recovers the underlying simple component modes [Figure3(e)].
These simulations demonstrate that cross-validation can disentangle mechanistic and emergent complexity: mechanistic complexity is supported when a single non-simple kernel is sufficient for held-out prediction, whereas emergent complexity is supported when multiple simpler components are required.

## 

Discussion—In this Letter, we have demonstrated that inferential frameworks can recover contagion rules that suggest peer reinforcement is at play—the classical “complex contagion” paradigm—when, in reality, the underlying mechanism is heterogeneous simple contagion.
This suggests that the current understanding of complex contagion should be expanded to encompass not only mechanistic complexity, often characterized by sigmoidal contagion kernels, but also emergent complexity, characterized by correlated heterogeneity.
This work introduces acomplexity score, a measure of complexity quantifying the amount by which a contagion kernel deviates from the simple contagion family.
We use this measure to explore network structures and dynamics that exhibit emergent complexity.
This measure, however, cannot capture the full spectrum of complexity; as illustrated inFigure2(d), two qualitatively different kernels with large complexity scores arise.
Emergent complexity arises when community structure and kernel assignments are sufficiently aligned; density differences between communities can then amplify the effect or reshape the inferred global kernel.
Finally, we have shown that it is possible to distinguish mechanistic from emergent complexity using a Bayesian inferential approach coupled with cross-validation.

While we have demonstrated that emergent complexity can, in principle, occur, here we have focused on the simplest case: two communities and two simple contagion kernels.
These results raise several questions about the generality, detectability, and empirical relevance of emergent complexity.
First, we must extend our framework to an arbitrary number of communities and kernels.
What does the resulting kernel look like?
Are we still able to disentangle the underlying kernels?
Second, while we have suggested that emergent complexity may plausibly explain contagions that look complex, this phenomenon has not yet been identified in systems with empirical dynamics.
Nonetheless, this study is a meaningful step forward in measuring and inferring complex and heterogeneous contagion kernels.

## 

Data availability—The data and code that support the findings of this study are archived on Zenodo athttps://doi.org/10.5281/zenodo.21632561. Any current unreleased code is available on GitHub athttps://github.com/kaiser-dan/heterogeneous-infection-kernels.

## Acknowledgements.The authors acknowledge support from the National Institutes of Health (1P20 GM125498-01 Centers of Biomedical Research Excellence Award, J.-G.Y., N.W.L., & L.H.-D.), from The National Science Foundation (award #2419733, J.-G.Y. & L.H.-D.) and from the University of Virginia Prominence-to-Preeminence (P2PE) STEM Targeted Initiatives Fund, SIF176A Contagion Science (N.W.L. and D.K.).
The authors acknowledge Research Computing (rc.virginia.edu) at The University of Virginia for providing computational resources and technical support that contributed to the results reported in this publication.
The authors would like to thank Sichen Jin and Clio Andris for providing data.

## References
- [1]R. Aiyappa, A. Flammini, and Y. Ahn(2024-04)Emergence of simple and complex contagion dynamics from weighted belief networks.Science Advances10(15),pp. eadh4439.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [2]E. Andres, G. Ódor, I. Iacopini, and M. Karsai(2025-03)Distinguishing mechanisms of social contagion from local network view.npj Complexity2(1),pp. 8.External Links:ISSN 2731-8753,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [3]J. Anttila, L. Mikonranta, T. Ketola, V. Kaitala, J. Laakso, and L. Ruokolainen(2017)A mechanistic underpinning for sigmoid dose-dependent infection.Oikos126(6),pp. 910–916.External Links:ISSN 1600-0706,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [4]G. Cencetti, D. A. Contreras, M. Mancastroppa, and A. Barrat(2023-06)Distinguishing Simple and Complex Contagion Processes on Networks.Physical Review Letters130(24),pp. 247401.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [5]D. Centola(2010-09)The Spread of Behavior in an Online Social Network Experiment.Science329(5996),pp. 1194–1197.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [6]P. S. Dodds and D. J. Watts(2004-05)Universal Behavior in a Generalized Model of Contagion.Physical Review Letters92(21),pp. 218701.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [7]D. Guilbeault and D. Centola(2021-07)Topological measures for identifying and predicting the spread of complex contagions.Nature Communications12(1),pp. 4430.External Links:ISSN 2041-1723,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [8]A. Gupta and N. W. Landry(2026-05)The interplay of network structure and correlated infectious traits in epidemic models.arXiv.External Links:2605.12773,Document,LinkCited by:Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [9]T. Hastie, R. Tibshirani, and J. Friedman(2009)Model Assessment and Selection.InThe Elements of Statistical Learning: Data Mining, Inference, and Prediction,T. Hastie, R. Tibshirani, and J. Friedman (Eds.),pp. 219–259.External Links:Document,Link,ISBN 978-0-387-84858-7Cited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [10]L. Hébert-Dufresne, Y. Ahn, A. Allard, V. Colizza, J. W. Crothers, P. S. Dodds, M. Galesic, F. Ghanbarnejad, D. Gravel, R. A. Hammond, K. Lerman, J. Lovato, J. J. Openshaw, S. Redner, S. V. Scarpino, G. St-Onge, T. R. Tangherlini, and J. Young(2025-09)One pathogen does not an epidemic make: a review of interacting contagions, diseases, beliefs, and stories.npj Complexity2(1),pp. 26.External Links:ISSN 2731-8753,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [11]L. Hébert-Dufresne, A. Allard, J. Young, W. H. W. Thompson, and G. St-Onge(2026-05)Simpson’s paradox explains the ubiquity of nonlinear, threshold, and complex contagions.arXiv.External Links:2605.00791,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [12]L. Hébert-Dufresne, S. V. Scarpino, and J. Young(2020-04)Macroscopic patterns of interacting contagions are indistinguishable from social reinforcement.Nature Physics16(4),pp. 426–431.External Links:ISSN 1745-2481,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [13]Https://data.gov/.External Links:LinkCited by:Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [14]M. Jerrum and G. B. Sorkin(1998-03)The Metropolis algorithm for graph bisection.Discrete Applied Mathematics82(1),pp. 155–175.External Links:ISSN 0166-218X,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [15]B. Karrer and M. E. J. Newman(2011-01)Stochastic blockmodels and community structure in networks.Physical Review E83(1),pp. 016107.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [16]N. W. Landry and J. G. Restrepo(2023-09)Opinion disparity in hypergraphs with community structure.Physical Review E108(3),pp. 034311.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [17]N. W. Landry, W. Thompson, L. Hébert-Dufresne, and J. Young(2024-10)Reconstructing networks from simple and complex contagions.Physical Review E110(4),pp. L042301.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [18]O. Ledoit and M. Wolf(2004)A well-conditioned estimator for large-dimensional covariance matrices.Journal of multivariate analysis88(2),pp. 365–411.Cited by:Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [19]J. Leskovec, K. J. Lang, A. Dasgupta, and M. W. Mahoney(2008-04)Statistical properties of community structure in large social and information networks.InProceedings of the 17th International Conference on World Wide Web,WWW ’08,New York, NY, USA,pp. 695–704.External Links:Document,Link,ISBN 978-1-60558-085-2Cited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [20]B. Mønsted, P. Sapieżyński, E. Ferrara, and S. Lehmann(2017-09)Evidence of complex contagion of information in social media: An experiment using Twitter bots.PLOS ONE12(9),pp. e0184148.External Links:ISSN 1932-6203,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [21]A. Nematzadeh, E. Ferrara, A. Flammini, and Y. Ahn(2014-08)Optimal Network Modularity for Information Diffusion.Physical Review Letters113(8),pp. 088701.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [22]M. E. J. Newman(2006-06)Modularity and community structure in networks.Proceedings of the National Academy of Sciences103(23),pp. 8577–8582.External Links:Document,LinkCited by:Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [23]D. J. P. O’Sullivan, G. J. O’Keeffe, P. G. Fennell, and J. P. Gleeson(2015)Mathematical modeling of complex contagion on clustered networks.Frontiers in Physics3.External Links:ISSN 2296-424X,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [24]T. P. Peixoto(2019-09)Network Reconstruction and Community Detection from Dynamics.Physical Review Letters123(12),pp. 128301.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [25]G. St-Onge, L. Hébert-Dufresne, and A. Allard(2024-01)Nonlinear bias toward complex contagion in uncertain transmission settings.Proceedings of the National Academy of Sciences121(1),pp. e2312202121.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [26]G. St-Onge, H. Sun, A. Allard, L. Hébert-Dufresne, and G. Bianconi(2021-10)Universal Nonlinear Infection Kernel from Heterogeneous Exposure on Higher-Order Networks.Physical Review Letters127(15),pp. 158301.External Links:Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [27]T. W. Valente(1996)Network models of the diffusion of innovations.Computational and Mathematical Organization Theory2(2).External Links:ISSN 1572-9346,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [28]A. Vehtari, A. Gelman, and J. Gabry(2017-09)Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC.Statistics and Computing27(5),pp. 1413–1432.External Links:ISSN 1573-1375,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity,Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.
- [29]L. Weng, F. Menczer, and Y. Ahn(2013-08)Virality Prediction and Community Structure in Social Networks.Scientific Reports3(1),pp. 2522.External Links:ISSN 2045-2322,Document,LinkCited by:‣Emergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity.

End Matter


Appendix A: Mixture model.To pool information across nodes while accommodating population heterogeneity, we model nodeii’s contagion kernel𝒄i\bm{c}_{i}as drawn from a finite mixture ofKKlatent components.
To allow for more flexible modeling, we work throughout on the logit scale, definingc~i​(ν)≡logit​ci​(ν)∈ℝ.\tilde{c}_{i}(\nu)\equiv\mathrm{logit}\ c_{i}(\nu)\in\mathbb{R}.

Nodeiiis assigned to componentzi∈{1,…,K}z_{i}\in\{1,\dots,K\}with probabilityπk=P​(zi=k),\pi_{k}=P(z_{i}=k),where𝝅∼Dirichlet​(𝟏K).\bm{\pi}\sim\mathrm{Dirichlet}(\bm{1}_{K}).Nodes assigned to the same mixture component share a commonkernel mode𝝁k\bm{\mu}_{k}—a subpopulation-level contagion kernel reflecting characteristic behavior for that group—around which individual node kernels vary on the logit scale:c~i​(ν)∼Normal​(μ~zi​(ν),σ),\tilde{c}_{i}(\nu)\sim\mathrm{Normal}\,\left(\tilde{\mu}_{z_{i}}(\nu),\sigma\right),

whereσ\sigmais a global scale parameter controlling the degree of node-level heterogeneity within each component.

We construct each componentkk’s kernel mode to be non-decreasing inν,\nu,reflecting our assumption that additional infectious contacts cannot reduce infection risk.
Specifically, we form the cumulative sum of a Dirichlet-distributed increment vector𝚫k∼Dirichlet​(κ​𝟏kmax)\bm{\Delta}_{k}\sim\mathrm{Dirichlet}(\kappa\bm{1}_{k_{\max}})scaled by a component-specific ceiling probabilitypk∈[0,1]:p_{k}\in[0,1]:μk​(ν)=pk​∑j=1νΔk,j\mu_{k}(\nu)=p_{k}\sum_{j=1}^{\nu}\Delta_{k,j}

The concentration parameterκ\kappa—fixed at 1.0 throughout our experiments—controls the smoothness of kernel modes: small values ofκ\kappaallow highly non-uniform kernels where infection probability increases rapidly over a narrow range ofν,\nu,while large values favor smoother, more gradual kernels.
Note that we truncate the kernel domain atkmax≤N−1k_{\max}\leq N-1for simplicity.

The ceilingpkp_{k}directly controls the maximum infection probability attained under componentk,k,encoding the assumption that infection risk saturates below certainty even at high exposure.
We place a normal prior on the logit-scale ceilingℓk≡logit​pk\ell_{k}\equiv\mathrm{logit}\ p_{k}centered at the empirical log-odds of infection in the data.
This places prior mass in a region consistent with the scale of the data and prevents the prior from dominating the likelihood when infection rates are close to zero or one.

Appendix B: Complexity score.We quantify the apparent complexity of an inferred contagion kernel mode by measuring its departure—adjusted for posterior uncertainty—from a reference kernel.
In this work, the reference kernel is a simple contagion kernel, but the same construction can be applied to any hypothesized kernel shape.

Let𝝁~(s)∈ℝkmax\tilde{\bm{\mu}}^{(s)}\in\mathbb{R}^{k_{\max}}denote posterior drawss,s=1,…,Ss=1,\dots,S, of the logit-scale kernel mode, and let𝝁~sc\tilde{\bm{\mu}}_{\mathrm{sc}}denote the logit-scale simple contagion reference,𝝁~sc​(ν)=logit​[1−(1−β¯sc)ν],\tilde{\bm{\mu}}_{\mathrm{sc}}(\nu)=\mathrm{logit}\,\left[1-(1-\bar{\beta}_{\mathrm{sc}})^{\nu}\right],

whereβ¯sc\bar{\beta}_{\mathrm{sc}}is the posterior mean infectivity under the simple contagion model fit to the same data.
All distances are computed on the logit scale.

For each posterior draw, define the regularized Mahalanobis distanceQ(s)≡(𝝁~(s)−𝝁~sc)T​𝑷​(𝝁~(s)−𝝁~sc),Q^{(s)}\equiv{\left(\tilde{\bm{\mu}}^{(s)}-\tilde{\bm{\mu}}_{\text{sc}}\right)}^{\mathrm{T}}\bm{P}\left(\tilde{\bm{\mu}}^{(s)}-\tilde{\bm{\mu}}_{\text{sc}}\right),

where𝑷=(𝚺^+λ​tr​(𝚺^)kmax​𝑰)−1.\bm{P}=\left(\hat{\bm{\Sigma}}+\lambda\frac{\mathrm{tr}(\hat{\bm{\Sigma}})}{k_{\max}}\bm{I}\right)^{-1}.

Here,𝚺^\hat{\bm{\Sigma}}is the posterior sample covariance of𝝁~\tilde{\bm{\mu}}and𝑷\bm{P}is a regularized inverse covariance.
We setλ≡αLW/(1−αLW),\lambda\equiv\alpha_{\mathrm{LW}}/(1-\alpha_{\mathrm{LW}}),whereαLW\alpha_{\mathrm{LW}}is the Ledoit-Wolf shrinkage estimate[18], to preserve the posterior covariance geometry while preventing poorly estimated near-zero covariance eigenvalues from receiving unbounded weight.

To interpretQ(s)Q^{(s)}, write a posterior draw as𝝁~=𝝁¯+𝜺,𝝁¯=𝔼​[𝝁~],𝔼​[𝜺]=𝟎,Cov​(𝜺)=𝚺.\tilde{\bm{\mu}}=\bar{\bm{\mu}}+\bm{\varepsilon},\quad\bar{\bm{\mu}}=\mathbb{E}[\tilde{\bm{\mu}}],\quad\mathbb{E}[\bm{\varepsilon}]=\bm{0},\quad\mathrm{Cov}(\bm{\varepsilon})=\bm{\Sigma}.

Then𝔼​[(𝝁~−𝝁~sc)T​𝑷​(𝝁~−𝝁~sc)]=\displaystyle\mathbb{E}\left[{\left(\tilde{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)}^{\mathrm{T}}\bm{P}\left(\tilde{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)\right]=(𝝁¯−𝝁~sc)T​𝑷​(𝝁¯−𝝁~sc)\displaystyle\;{\left(\bar{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)}^{\mathrm{T}}\bm{P}\left(\bar{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)+tr​(𝑷​𝚺).\displaystyle+\mathrm{tr}(\bm{P}\bm{\Sigma}).

The first term measures displacement of the posterior mean from the reference, while the trace term is the distance expected from posterior spread alone under the regularized Mahalanobis metric.
We therefore define our complexity score asD≡⟨Q⟩s−tr​(𝑷​𝚺^)tr​(𝑷​𝚺^),⟨Q⟩s=S−1​∑s=1SQ(s).D\equiv\frac{\langle Q\rangle_{s}-\mathrm{tr}(\bm{P}\hat{\bm{\Sigma}})}{\mathrm{tr}(\bm{P}\hat{\bm{\Sigma}})},\qquad\langle Q\rangle_{s}=S^{-1}\sum_{s=1}^{S}Q^{(s)}.

Thus,DDis a dimensionless signal-to-uncertainty ratio on the squared Mahalanobis scale.
The valueD=0D=0indicates no systematic departure from the reference kernel beyond posterior spread, whileD=1D=1indicates that the excess (squared) departure is equal to the uncertainty baseline.
Equivalently, the posterior mean squared Mahalanobis distance from the reference is1+D1+Dtimes the distance expected from posterior uncertainty alone.

As a limiting case, suppose the logit-scale kernel mode𝝁~\tilde{\bm{\mu}}were known exactly, i.e.,𝚺=𝟎.\bm{\Sigma}=\bm{0}.Apparent complexity relative to the simple contagion reference could be measured in a straightforward manner as the mean squared logit-scale deviation:D0=1kmax​(𝝁~−𝝁~sc)T​(𝝁~−𝝁~sc)D_{0}=\frac{1}{k_{\max}}{\left(\tilde{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)}^{\mathrm{T}}\left(\tilde{\bm{\mu}}-\tilde{\bm{\mu}}_{\text{sc}}\right)

The scoreDDis the uncertainty-adjusted analogue: it replaces the identity geometry with a posterior-uncertainty-aware geometry, subtracts the distance expected from posterior spread alone, and normalizes the remaining systematic departure by that uncertainty baseline.

Finally,DDcan be calibrated by posterior predictive simulation under a fitted simple contagion null, as described in the Supplemental Material.
This calibration is useful because even a truly simple contagion can yield a positive estimated complexity score when the time series is short and the kernel is inferred rather than observed.

Appendix C: Node-level cross-validation.We use node-level cross-validation (CV) to select the number of mixture components,KK.
For each fold, the exposure-count matrices𝑴\bm{M}and𝑵\bm{N}are formed once on the full network, and held-out nodes are excluded only by dropping their rows from the training likelihood. Thus, held-out nodes are not removed from the dynamical process: their observed states still contribute to the exposure counts of the training nodes.

Recall thatMi,νM_{i,\nu}andNi,νN_{i,\nu}count, respectively, the infection and non-infection events at nodeiiwhile it hadν\nuinfected neighbors.
After fitting on the training set, we score the held-out fold by its log pointwise predictive density (LPPD)[28]:LPPDj=∑i∈ℱjlog⁡p^​(Mi,Ni∣{Mℓ,Nℓ:ℓ∈ℱ−j}),\text{LPPD}_{j}=\sum_{i\in\mathcal{F}_{j}}\log\hat{p}(M_{i},N_{i}\mid\{M_{\ell},N_{\ell}:\ell\in\mathcal{F}_{-j}\}),

wherep^​(Mi,Ni)=\displaystyle\hat{p}(M_{i},N_{i})=1S∑s=1S∑k=1K[πk(s)\displaystyle\;\frac{1}{S}\sum_{s=1}^{S}\sum_{k=1}^{K}\bigg[\pi_{k}^{(s)}×∏ν=1kmaxμk(s)(ν)Mi,ν(1−μk(s)(ν))Ni,ν],\displaystyle\times\prod_{\nu=1}^{k_{\max}}\mu_{k}^{(s)}(\nu)^{M_{i,\nu}}\bigl(1-\mu_{k}^{(s)}(\nu)\bigr)^{N_{i,\nu}}\bigg],

with{𝝅(s),𝝁(s)}s=1S\{\bm{\pi}^{(s)},\bm{\mu}^{(s)}\}_{s=1}^{S}drawn from the posterior given{Mℓ,Nℓ:ℓ∈ℱ−j}.\{M_{\ell},N_{\ell}:\ell\in\mathcal{F}_{-j}\}.The predictive therefore depends only on the population-level kernelsμk\mu_{k}and weightsπk\pi_{k}; no per-node latent quantity enters.

The overall CV score is the mean LPPD per held-out node.
We repeat this procedure forK=1,2,…,KmaxK=1,2,\dots,K_{\max}mixture components and apply the one-standard-error (1-SE) rule: we select the smallestKKwhose mean LPPD lies within one standard error of the maximum[9].
This parsimony criterion is useful here because unsupported extra components cannot be tuned to held-out node-specific fluctuations; the held-out predictive depends only on subpopulation-level kernel modes and mixture weights.
In practice, extra components tend to receive negligible weight or duplicate existing components, so the CV curve plateaus—with at most a slight downward drift from the extra population-level parameters—onceKKcaptures the population heterogeneity.
In our simulations, these plateaus begin at the trueKK, and the 1-SE rule recovers the true number of components across replicates; see the Supplemental Material.

Supplemental Material forEmergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneity

Cross validation for selecting the number of mixture components.As described in Appendix C, we use five-fold node-level cross-validation (CV) and the one-standard-error rule to select the number of mixture componentsKK.
Here, we show that this procedure is stable across simulation replicates (20 for each ground truth data generating process).
Throughout, we consider networks drawn from our(ε,δ)(\varepsilon,\delta)-stochastic block model withN=256,N=256,⟨k⟩\langle k\rangle=18,ε=0.9,\varepsilon=0.9,andδ=0.0.\delta=0.0.

For data generated by a single, complex kernel—the sigmoidal kernel recovered inFigure1—the CV score curves consistently plateau atK=1K=1, indicating that additional components do not improve predictive performance [FigureS1(a)].
For data generated by a mixture of two simple kernels withβ1=0.01\beta_{1}=0.01andβ2=0.04\beta_{2}=0.04—assigned to communities 1 and 2, respectively, with block-flip probabilityω=0.1\omega=0.1—the CV score curves consistently increase fromK=1K=1toK=2K=2and then plateau [FigureS1(b)].
Applying the one-standard-error rule recovers the true number of kernel components across all simulations [FigureS1(c)].Figure S1:Cross-validation recovers the true number of kernel components.(a) Mean held-out LPPD per node versus number of mixture components,KK, for data generated by one complex kernel. (b) Corresponding CV curves for data generated by two simple kernels with block-flip probabilityω=0.1\omega=0.1. Gray curves show individual simulation replicates; colored points and error bars show the mean±1\pm 1SE for one highlighted simulation. Dashed horizontal lines indicate the 1-SE selection threshold. (c) Confusion matrix comparing the true and selected number of components.

Empirical results.To complement the experiments on synthetic contact structures presented inFigure2, we next show that emergent complexity can arise with synthetic SIS dynamics on an empirical network.
We use a network of United States representatives in the 118th Congress, connecting two representatives if they agreed on at least 980 roll-call votes.
The data is gathered from publicly available records[13].
The resulting network is undirected, unweighted, and without multi-edges or self-loops.
We restrict our analysis to the 107 representatives in the largest connected component of this network.
We find two communities of representatives using a spectral method, bisecting the network according to the sign of the entries of the second-largest eigenvalue of the modularity matrix[22].
Nodes in the denser of the two communities are assigned with probability1−ω1-\omegaan underlying simple kernel withβ2=0.05\beta_{2}=0.05; nodes in the sparser community are similarly assigned a simple kernel withβ1=0.01\beta_{1}=0.01.
We assume a constant healing rate ofγ=0.1\gamma=0.1.Figure S2:Emergent complexity on an empirical network.(a) The congressional network with node color and shape indicating its community label.
(b) The complexity score,DD, with respect to the block-flip probability.
We plot the average of 10 repetitions and±\pm1 standard deviation.
(c) Representative samples from the posterior kernel with underlying ground-truth kernels plotted in gray.

With sufficiently smallω\omega—that is, sufficiently high kernel-community alignment—the inferred global kernel has significant complexity [FigureS2,TableS1].
We assess significance with a posterior predictive null for global simple contagion with shared .
We construct a null distribution by posterior predictive simulation: for each replicater=1,…,R,r=1,\dots,R,we drawβ(r)\beta^{(r)}from the posterior of the simple contagion model fit to the observed data and simulate a new dataset on the same network with the same observation window and recovery probabilityγ\gammaused in the observed analysis.
We then fit the nonparametric kernel model to the replicate dataset and compute the corresponding complexity scoreDrep(r)D_{\mathrm{rep}}^{(r)}with the simple contagion reference kernel parameterized byβ(r).\beta^{(r)}.The dimensionless ridge parameterλ\lambdaused in computingDrep(r)D_{\mathrm{rep}}^{(r)}is chosen once—from the observed data—and then held fixed across replicate analyses.

The posterior predictivepp-value is thenpppc=1+∑r=1R𝟙​[Drep(r)≥Dobs]R+1,p_{\mathrm{ppc}}=\frac{1+\sum_{r=1}^{R}\mathbbm{1}\left[D_{\mathrm{rep}}^{(r)}\geq D_{\mathrm{obs}}\right]}{R+1},

the fraction of null replicates whose complexity is at least as large as that observed in the original dataset (with a finite-replicate correction).
Such calibration is necessary because finite time series, stochastic simulation noise, posterior uncertainty, and covariance estimation can all produce nonzero complexity even when the data-generating kernel is simple.
Thus,pppcp_{\mathrm{ppc}}measures whether the observed departure from the simple contagion family is larger than expected under a fitted simple contagion null model.

The observed complexity score is significant for smallω\omega(p<0.05p<0.05;TableS1), indicating more apparent complexity than expected under a homogeneous simple contagion process on the same network.ω\omegaPosterior predictivepp-value0.00.0198∗0.0198^{*}0.10.0099∗∗0.0099^{**}0.20.0099∗∗0.0099^{**}0.31.00000.40.92080.50.9909Table S1:Posterior predictivepp-values for kernels inferred from the Congress agreement dataset.p∗≤0.05{}^{*}p\leq 0.05,p∗∗≤0.01{}^{**}p\leq 0.01

This result is consistent with the SBM results above but shows that emergent complexity is not specific to idealized block models: the same exposure-dependent aggregation can arise on an empirical network with naturally occurring community structure.
Moreover, the inferred global kernel is not strongly sigmoidal, reinforcing that emergent complexity can produce nonstandard departures from the simple contagion family.

The basic reproduction number for two simple kernels and the(ε,δ)(\varepsilon,\delta)-stochastic block model.To derive the basic reproduction number for the model used in generating the results in Fig.2, we employ a mean-field approach.
For a network of sizeNNand a fixed mean degree⟨k⟩\langle k\rangle, the(ε,δ)(\varepsilon,\delta)-stochastic block model (SBM) is a 2-parameter model, where the community separation parameter,ε\varepsilon, controls the number of links between the two blocks[14], each of sizeN/2N/2, and the density imbalance parameter,δ\delta, controls the relative densities between the two blocks.
Whenδ=0\delta=0, we recover the standard planted partition model; in this case, whenε=0\varepsilon=0, we recover an Erdős-Rényi network.
Whenε=1\varepsilon=1, we obtain two isolated communities.
Whenδ>0\delta>0, block 1 is denser than block 2, and whenδ<0\delta<0, the opposite is true.
Conditioned on node labels, between-block edges occur with probabilityp12=p21=(1−ε)​⟨k⟩/(N−1)p_{12}=p_{21}=(1-\varepsilon)\langle k\rangle/(N-1), while within-block edges occur with probabilitiesp11=(1+δ)​(1+ε)​⟨k⟩/(N−1)p_{11}=(1+\delta)(1+\varepsilon)\langle k\rangle/(N-1)andp22=(1−δ)​(1+ε)​⟨k⟩/(N−1)p_{22}=(1-\delta)(1+\varepsilon)\langle k\rangle/(N-1)in blocks 1 and 2, respectively.

We definex1x_{1}andx2x_{2}as the fraction of infected nodes in communities 1 and 2, respectively, and, following the same steps as in Ref.[16], we obtain the following system of equations:d​x1d​t\displaystyle\frac{dx_{1}}{dt}=−γ​x1+β¯1​⟨k⟩2​(1−x1)​[(1+ε)​(1+δ)​x1+(1−ε)​x2],\displaystyle=-\gamma x_{1}+\bar{\beta}_{1}\frac{\langle k\rangle}{2}(1-x_{1})\left[(1+\varepsilon)(1+\delta)x_{1}+(1-\varepsilon)x_{2}\right],(S1)d​x2d​t\displaystyle\frac{dx_{2}}{dt}=−γ​x2+β¯2​⟨k⟩2​(1−x2)​[(1−ε)​x1+(1+ε)​(1−δ)​x2],\displaystyle=-\gamma x_{2}+\bar{\beta}_{2}\frac{\langle k\rangle}{2}(1-x_{2})\left[(1-\varepsilon)x_{1}+(1+\varepsilon)(1-\delta)x_{2}\right],(S2)

whereβ¯1=(1−ω)​β1+ω​β2\bar{\beta}_{1}=(1-\omega)\beta_{1}+\omega\beta_{2}andβ¯2=ω​β1+(1−ω)​β2\bar{\beta}_{2}=\omega\beta_{1}+(1-\omega)\beta_{2}denote the average infectivity in blocks 1 and 2, respectively.

Linearizing this system about the𝟎\mathbf{0}equilibrium, we obtain the linear equation for the perturbations about this equilibrium,dd​t​[x1x2]\displaystyle\frac{d}{dt}\begin{bmatrix}x_{1}\\
x_{2}\end{bmatrix}=(−γ​I+⟨k⟩2​[β¯1​(1+ε)​(1+δ)β¯1​(1−ε)β¯2​(1−ε)β¯2​(1+ε)​(1−δ)])​[x1x2].\displaystyle=\left(-\gamma I+\frac{\langle k\rangle}{2}\begin{bmatrix}\bar{\beta}_{1}(1+\varepsilon)(1+\delta)&\bar{\beta}_{1}(1-\varepsilon)\\
\bar{\beta}_{2}(1-\varepsilon)&\bar{\beta}_{2}(1+\varepsilon)(1-\delta)\end{bmatrix}\right)\begin{bmatrix}x_{1}\\
x_{2}\end{bmatrix}.

Then, lettingBBdenote the infection matrix above,tr​(B)=\displaystyle\text{tr}(B)=(⟨k⟩2​(1+ε)​(1+δ)​β¯1)+(⟨k⟩2​(1+ε)​(1−δ)​β¯2)\displaystyle\,\left(\frac{\langle k\rangle}{2}(1+\varepsilon)(1+\delta)\bar{\beta}_{1}\right)+\left(\frac{\langle k\rangle}{2}(1+\varepsilon)(1-\delta)\bar{\beta}_{2}\right)=\displaystyle=⟨k⟩2​(1+ε)​[(β¯1+β¯2)+δ​(β¯1−β¯2)]\displaystyle\frac{\langle k\rangle}{2}(1+\varepsilon)\left[\left(\bar{\beta}_{1}+\bar{\beta}_{2}\right)+\delta\left(\bar{\beta}_{1}-\bar{\beta}_{2}\right)\right]det(B)=\displaystyle\det(B)=(⟨k⟩2​(1+ε)​(1+δ)​β¯1)​(⟨k⟩2​(1+ε)​(1−δ)​β¯2)\displaystyle\,\left(\frac{\langle k\rangle}{2}(1+\varepsilon)(1+\delta)\bar{\beta}_{1}\right)\left(\frac{\langle k\rangle}{2}(1+\varepsilon)(1-\delta)\bar{\beta}_{2}\right)−(⟨k⟩2​(1−ε)​β¯1)​(⟨k⟩2​(1−ε)​β¯2)\displaystyle-\left(\frac{\langle k\rangle}{2}(1-\varepsilon)\bar{\beta}_{1}\right)\left(\frac{\langle k\rangle}{2}(1-\varepsilon)\bar{\beta}_{2}\right)=\displaystyle=⟨k⟩24​β¯1​β¯2​[(1+ε)2​(1−δ2)−(1−ε)2].\displaystyle\,\frac{\langle k\rangle^{2}}{4}\bar{\beta}_{1}\bar{\beta}_{2}\left[(1+\varepsilon)^{2}(1-\delta^{2})-(1-\varepsilon)^{2}\right].

Then the eigenvalues of−γ​I+B-\gamma I+Bareλ=\displaystyle\lambda=−γ+⟨k⟩4​(1+ε)​[(β¯1+β¯2)+δ​(β¯1−β¯2)]\displaystyle-\gamma+\frac{\langle k\rangle}{4}(1+\varepsilon)\left[\left(\bar{\beta}_{1}+\bar{\beta}_{2}\right)+\delta\left(\bar{\beta}_{1}-\bar{\beta}_{2}\right)\right]±⟨k⟩4​(1+ε)2​[(β¯1−β¯2)+δ​(β¯1+β¯2)]2+4​(1−ε)2​β¯1​β¯2,\displaystyle\pm\frac{\langle k\rangle}{4}\sqrt{(1+\varepsilon)^{2}\left[\left(\bar{\beta}_{1}-\bar{\beta}_{2}\right)+\delta\left(\bar{\beta}_{1}+\bar{\beta}_{2}\right)\right]^{2}+4(1-\varepsilon)^{2}\bar{\beta}_{1}\bar{\beta}_{2}},=\displaystyle=−γ+⟨k⟩4(1+ε)[(β1+β2)+δ(1−2ω)(β1−β2)\displaystyle\,-\gamma+\frac{\langle k\rangle}{4}(1+\varepsilon)\Bigg[(\beta_{1}+\beta_{2})+\delta(1-2\omega)(\beta_{1}-\beta_{2})±[(1−2​ω)​(β1−β2)+δ​(β1+β2)]2+(1−ε1+ε)2​[(β1+β2)2−(1−2​ω)2​(β1−β2)2]],\displaystyle\pm\sqrt{[(1-2\omega)(\beta_{1}-\beta_{2})+\delta(\beta_{1}+\beta_{2})]^{2}+\left(\displaystyle\frac{1-\varepsilon}{1+\varepsilon}\right)^{2}[(\beta_{1}+\beta_{2})^{2}-(1-2\omega)^{2}(\beta_{1}-\beta_{2})^{2}]}\;\Bigg],

and the reproduction number isR0=\displaystyle R_{0}=⟨k⟩​(1+ε)4​γ[(β1+β2)+δ(1−2ω)(β1−β2)\displaystyle\frac{\langle k\rangle(1+\varepsilon)}{4\gamma}\bigg[(\beta_{1}+\beta_{2})+\delta(1-2\omega)(\beta_{1}-\beta_{2})+[(1−2​ω)​(β1−β2)+δ​(β1+β2)]2+(1−ε1+ε)2​[(β1+β2)2−(1−2​ω)2​(β1−β2)2]].\displaystyle+\sqrt{[(1-2\omega)(\beta_{1}-\beta_{2})+\delta(\beta_{1}+\beta_{2})]^{2}+\left(\displaystyle\frac{1-\varepsilon}{1+\varepsilon}\right)^{2}[(\beta_{1}+\beta_{2})^{2}-(1-2\omega)^{2}(\beta_{1}-\beta_{2})^{2}]}\bigg].(S3)Figure S3:Analytical estimate ofR0R_{0}fromEmergent contagion complexity: Disentangling mechanistic complexity from correlated heterogeneityderived from our mean-field model. Here, as inFigure2,⟨k⟩=18\langle k\rangle=18. Additional parameter values areβ1≡0.01,β2≡0.04\beta_{1}\equiv 0.01,\beta_{2}\equiv 0.04, andω≡0.1\omega\equiv 0.1.

As seen inFigureS3, the reproduction number is strongly dependent on the relative densities of the two communities.
Notice that negativeδ\deltavalues correspond to a large increase in the reproduction number.
This matches what we would expect fromFigure2(d), where the global inferred kernel follows the more infectious contagion kernel for small values ofν\nu.
For positiveδ\deltavalues, we see a decrease in the reproduction number, and this corresponds to the sigmoidal “complex” kernel inFigure2(d).
As found in Ref.[8], whenω≠1/2\omega\neq 1/2andβ1≠β2\beta_{1}\neq\beta_{2}, the reproduction number depends on the strength of community structure.

Mean-field analysis of the low-complexity region in the(ε,δ)(\varepsilon,\delta)-stochastic block model.Figure2(c) shows a low-complexity region whose location shifts to largerδ\deltaas the kernel contrast,rβr_{\beta}, increases.
Here we derive a mean-field predictor for the location of this low-complexity region based on the observation that a global kernel appears complex when exposure levelν\nuis informative about a node’s latent kernel class.

LetLi,ν=Mi,ν+Ni,νL_{i,\nu}=M_{i,\nu}+N_{i,\nu}denote the number of exposure observations for a susceptible nodeiiat exposure levelν\nu.
An empirical estimate of the infection probability at exposureν\nuisc^​(ν)=∑i=1NMi,ν∑i=1NLi,ν.\hat{c}(\nu)=\frac{\sum_{i=1}^{N}M_{i,\nu}}{\sum_{i=1}^{N}L_{i,\nu}}.

For each kernel classℓ∈{1,2}\ell\in\{1,2\}, letMν(ℓ)M_{\nu}^{(\ell)}andLν(ℓ)L_{\nu}^{(\ell)}denote the number of infections and total susceptible exposure observations, respectively, amongβℓ\beta_{\ell}nodes at exposure levelν\nu.
We can rewritec^​(ν)\hat{c}(\nu)asc^​(ν)=Mν(1)Lν(1)+Lν(2)+Mν(2)Lν(1)+Lν(2)=[1−Wβ2​(ν)]​(Mν(1)Lν(1))+Wβ2​(ν)​(Mν(2)Lν(2))\hat{c}(\nu)=\frac{M_{\nu}^{(1)}}{L_{\nu}^{(1)}+L_{\nu}^{(2)}}+\frac{M_{\nu}^{(2)}}{L_{\nu}^{(1)}+L_{\nu}^{(2)}}\\
=[1-W_{\beta_{2}}(\nu)]\left(\frac{M_{\nu}^{(1)}}{L_{\nu}^{(1)}}\right)+W_{\beta_{2}}(\nu)\left(\frac{M_{\nu}^{(2)}}{L_{\nu}^{(2)}}\right)

whereWβ2​(ν)=Lν(2)Lν(1)+Lν(2)W_{\beta_{2}}(\nu)=\frac{L_{\nu}^{(2)}}{L_{\nu}^{(1)}+L_{\nu}^{(2)}}(S4)

is the fraction of susceptible observations at exposure levelν\nucontributed by nodes with the high-infectivity (β2\beta_{2}) kernel.

From the form ofc^​(ν),\hat{c}(\nu),we see that apparent complexity is controlled not only by the kernel contrast betweenβ1\beta_{1}andβ2\beta_{2}but also by howWβ2​(ν)W_{\beta_{2}}(\nu)varies over the observed exposure range.
IfWβ2​(ν)W_{\beta_{2}}(\nu)is approximately constant inν,\nu,the global kernel is close to a fixed convex combination of the two simple kernels and remains comparatively simple.
IfWβ2​(ν)W_{\beta_{2}}(\nu)varies strongly withν,\nu,the global estimate averages the two simple kernels in an exposure-dependent way, producing an apparent departure from the simple contagion family.

We use a block mean-field approximation to estimateWβ2​(ν)W_{\beta_{2}}(\nu)under the(ε,δ)(\varepsilon,\delta)-SBM with network sizeNNand fixed mean degree⟨k⟩.\langle k\rangle.Letρg,ℓ​(t)=P​(a node in blockgwith kernelℓis infected at timet),\rho_{g,\ell}(t)=P(\text{a node in block $g$ with kernel $\ell$ is infected at time $t$}),

whereg,ℓ∈{1,2}.g,\ell\in\{1,2\}.The exposure distribution of a susceptible node depends on its structural block through the aggregate block prevalences:ρ¯1​(t)=(1−ω)​ρ1,1​(t)+ω​ρ1,2​(t),ρ¯2​(t)=ω​ρ2,1​(t)+(1−ω)​ρ2,2​(t),\bar{\rho}_{1}(t)=(1-\omega)\rho_{1,1}(t)+\omega\rho_{1,2}(t),\qquad\bar{\rho}_{2}(t)=\omega\rho_{2,1}(t)+(1-\omega)\rho_{2,2}(t),(S5)

where, recall, a node in block 1 is assigned kernel 1 with probability1−ω1-\omegaand kernel 2 with probabilityω\omegaand vice versa for a node in block 2.
The number of infected neighbors of a susceptible node in blocks 1 and 2, respectively, is approximated as Poisson with meanλ1​(t)=(N2−1)​p11​ρ¯1​(t)+N2​p12​ρ¯2​(t),λ2​(t)=N2​p12​ρ¯1​(t)+(N2−1)​p22​ρ¯2​(t),\lambda_{1}(t)=\left(\frac{N}{2}-1\right)p_{11}\bar{\rho}_{1}(t)+\frac{N}{2}p_{12}\bar{\rho}_{2}(t),\qquad\lambda_{2}(t)=\frac{N}{2}p_{12}\bar{\rho}_{1}(t)+\left(\frac{N}{2}-1\right)p_{22}\bar{\rho}_{2}(t),(S6)

wherep11p_{11}andp22p_{22}are the within-block edge probabilities andp12p_{12}is the between-block edge probability defined in the previous section.
The first term inλ1\lambda_{1}is the expected number of infected neighbors from within block 1 and the second term is the expected number of infected neighbors from block 2; the terms inλ2\lambda_{2}have a similar interpretation.

The mean infection probability for a susceptible node in blockggwith simple kernelc(ℓ)​(ν)=1−(1−βℓ)νc^{(\ell)}(\nu)=1-(1-\beta_{\ell})^{\nu}is then∑ν≥0e−λg​(λg)νν!​c(ℓ)​(ν)=1−exp⁡(−βℓ​λg).\sum_{\nu\geq 0}e^{-\lambda_{g}}\frac{(\lambda_{g})^{\nu}}{\nu!}c^{(\ell)}(\nu)=1-\exp(-\beta_{\ell}\lambda_{g}).

Therefore, the four-class discrete-time mean-field equations areρg,ℓ​(t+1)=(1−γ)​ρg,ℓ​(t)+[1−ρg,ℓ​(t)]​[1−exp⁡(−βℓ​λg)]\rho_{g,\ell}(t+1)=(1-\gamma)\rho_{g,\ell}(t)+[1-\rho_{g,\ell}(t)][1-\exp(-\beta_{\ell}\lambda_{g})]

forg,ℓ∈{1,2}.g,\ell\in\{1,2\}.At a positive fixed point,γ​ρg,ℓ∗=(1−ρg,ℓ∗)​[1−exp⁡(−βℓ​λg∗)].\gamma\rho_{g,\ell}^{*}=(1-\rho_{g,\ell}^{*})[1-\exp(-\beta_{\ell}\lambda_{g}^{*})].

These four equations must be solved self-consistently becauseλ1∗\lambda_{1}^{*}andλ2∗\lambda_{2}^{*}depend on the aggregate block prevalences [see Eqs. (S5) and (S6)].

Near the positive fixed point,Lν(2)\displaystyle L_{\nu}^{(2)}∝ω​(1−ρ1,2∗)​exp⁡(−λ1∗)​(λ1∗)νν!+(1−ω)​(1−ρ2,2∗)​exp⁡(−λ2∗)​(λ2∗)νν!,\displaystyle\propto\omega(1-\rho_{1,2}^{*})\exp(-\lambda_{1}^{*})\frac{(\lambda_{1}^{*})^{\nu}}{\nu!}+(1-\omega)(1-\rho_{2,2}^{*})\exp(-\lambda_{2}^{*})\frac{(\lambda_{2}^{*})^{\nu}}{\nu!},Lν(1)\displaystyle L_{\nu}^{(1)}∝(1−ω)​(1−ρ1,1∗)​exp⁡(−λ1∗)​(λ1∗)νν!+ω​(1−ρ2,1∗)​exp⁡(−λ2∗)​(λ2∗)νν!.\displaystyle\propto(1-\omega)(1-\rho_{1,1}^{*})\exp(-\lambda_{1}^{*})\frac{(\lambda_{1}^{*})^{\nu}}{\nu!}+\omega(1-\rho_{2,1}^{*})\exp(-\lambda_{2}^{*})\frac{(\lambda_{2}^{*})^{\nu}}{\nu!}.

Rather than working directly withWβ2​(ν)W_{\beta_{2}}(\nu)[Eq. (S4)], it is helpful to consider its odds,Wβ2​(ν)1−Wβ2​(ν)=Lν(2)Lν(1)=ω​(1−ρ1,2∗)+(1−ω)​(1−ρ2,2∗)​R​(ν)(1−ω)​(1−ρ1,1∗)+ω​(1−ρ2,1∗)​R​(ν),\frac{W_{\beta_{2}}(\nu)}{1-W_{\beta_{2}}(\nu)}=\frac{L_{\nu}^{(2)}}{L_{\nu}^{(1)}}=\frac{\omega(1-\rho_{1,2}^{*})+(1-\omega)(1-\rho_{2,2}^{*})R(\nu)}{(1-\omega)(1-\rho_{1,1}^{*})+\omega(1-\rho_{2,1}^{*})R(\nu)},(S7)

whereR​(ν)=exp⁡[−(λ2∗−λ1∗)]​(λ2∗λ1∗)νR(\nu)=\exp[-(\lambda_{2}^{*}-\lambda_{1}^{*})]\left(\frac{\lambda_{2}^{*}}{\lambda_{1}^{*}}\right)^{\nu}

is the ratio of the Poisson exposure probabilities for blocks 2 and 1.

We see immediately that the quantityWβ2​(ν)W_{\beta_{2}}(\nu)is nearly constant when the two structural blocks generate similar exposure distributions.
Under the Poisson approximation, this occurs when their mean exposure levels are approximately equal:λ1∗​(δ)≈λ2∗​(δ),\lambda_{1}^{*}(\delta)\approx\lambda_{2}^{*}(\delta),

where the dependence ofλg\lambda_{g}onδ\deltacomes in throughp11p_{11}andp22p_{22}in Eq. (S6).
We therefore defineF​(δ)=λ2∗​(δ)−λ1∗​(δ),F(\delta)=\lambda_{2}^{*}(\delta)-\lambda_{1}^{*}(\delta),

whereλ1∗\lambda_{1}^{*}andλ2∗\lambda_{2}^{*}are the block mean exposures [Eq. (S6)] evaluated at the positive fixed point(ρ1,1∗,ρ1,2∗,ρ2,1∗,ρ2,2∗)(\rho_{1,1}^{*},\rho_{1,2}^{*},\rho_{2,1}^{*},\rho_{2,2}^{*})of the four-class mean-field system.
The predicted low-complexity region is obtained by scanning overδ\delta—for fixedN,⟨k⟩,ε,ω,β1,N,\,\langle k\rangle,\,\varepsilon,\,\omega,\,\beta_{1},andβ2\beta_{2}(equivalently,rβr_{\beta}), andγ\gamma—and identifying whereF​(δ)F(\delta)crosses zero.
Theδ\delta-value at whichF​(δ)F(\delta)crosses zero is shown inFigureS4.Figure S4:The mean-field exposure-balance criterion predicts the location of the low-complexity region.Complexity score,DD, of the inferred global kernel mode with respect to density imbalance,δ\delta, and kernel contrast,rβ≡β2/β1r_{\beta}\equiv\beta_{2}/\beta_{1}for the(ε,δ)(\varepsilon,\delta)-SBM withN=256N=256nodes,⟨k⟩=18,\langle k\rangle=18,ε=0.9\varepsilon=0.9, andω=0.1\omega=0.1.
We fixβ1=0.01\beta_{1}=0.01and varyβ2∈[0.01,0.05].\beta_{2}\in[0.01,0.05].Each cell averages 10 simulations.
The white curve shows the mean-field prediction obtained by solving the four-class mean-field system for its positive fixed point and locating the zero ofF​(δ)=λ2∗​(δ)−λ1∗​(δ),F(\delta)=\lambda_{2}^{*}(\delta)-\lambda_{1}^{*}(\delta),the value ofδ\deltaat which the two structural blocks have equal mean exposure.

This predicted zero is an implicit mean-field criterion for exposure balance: the value ofδ\deltaat which the two structural blocks have approximately equal mean exposure levels.
At this point, the ratioR​(ν)R(\nu)is approximately constant inν\nu, so the quantityWβ2W_{\beta_{2}}is also approximately constant inν.\nu.The calculation should therefore be interpreted as a predictor for where exposure level is least informative about latent kernel class and thus where the global kernel is expected to have reduced apparent complexity.

Reproducing experiments.For convenience, we collect the parameter values used in throughout our experiments.
All networks sampled from our(ε,δ)(\varepsilon,\delta)-SBM model haveN=256N=256\penalty 10000\nodes and a mean degree⟨k⟩=18\langle k\rangle=18\penalty 10000\.
We consider only unweighted, undirected networks without self-loops or multi-edges.
The block strength,ε\varepsilon, varies between experiments and takes values in[0,1][0,1].

When we simulate contagion processes on these networks, we fix the healing rate atγ≡0.1\gamma\equiv 0.1and simulate all processes for 1000 time steps.
While the quality of the inference decreases with too few time steps, 1000 time steps are more than sufficient for the size of networks considered here.
While the infection probabilityβ1=0.01\beta_{1}=0.01is fixed in all experiments, we varyβ2\beta_{2}to modifyrβr_{\beta}.

## 


- 


Major funding support from
