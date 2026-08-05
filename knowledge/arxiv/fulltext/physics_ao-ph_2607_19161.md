# On the sensitivity of machine-learned probabilistic weather forecast models to scale-aware scoring rules

**arXiv ID**: 2607.19161v2
**Authors**: Simon Lang, Martin Leutbecher, Sam Hatfield
**Published**: 2026-07-21
**Categories**: physics.ao-ph, stat.ML
**HTML URL**: https://arxiv.org/html/2607.19161v2

## Abstract

Probabilistic forecast models can be machine-learned from data using loss functions based on scoring rules such as the Continuous Ranked Probability Score (CRPS). This note summarises a preliminary study comparing versions of AIFS-CRPS, a global weather forecast model, trained with different univariate and multivariate scoring rules that aim to explicitly represent scale-awareness in the loss function. In the first part, we compare the (almost) fair CRPS, a fair global energy score, and a graph energy score based on node neighbourhoods. Across standard verification metrics, forecast skill is broadly similar. In the extratropics we find only small differences, while in the tropics the graph energy score setup performs somewhat better and the global energy score shows some degradation. These results suggest that multivariate scores are a viable alternative to CRPS-based training for global machine-learned weather forecasting. In the second part of the study, we analyse how different scoring rules and scale-aware loss constraints shape the spectra of forecast fields. It is apparent that any form of explicit scale-awareness improves realism. Here, the largest differences are likely associated with different effective weights per scale.

## Full Text

On the sensitivity of machine-learned probabilistic weather forecast models to scale-aware scoring rules

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
- License: CC BY-SA 4.0arXiv:2607.19161v2 [physics.ao-ph] 27 Jul 2026

## On the sensitivity of machine-learned probabilistic weather forecast models to scale-aware scoring rulesSimon Lang, Martin Leutbecher, Sam Hatfield

## Abstract

Probabilistic forecast models can be machine-learned from data using loss functions based on scoring rules such as the Continuous Ranked Probability Score (CRPS). This note summarises a preliminary study comparing versions of AIFS-CRPS, a global weather forecast model, trained with different univariate and multivariate scoring rules that aim to explicitly represent scale-awareness in the loss function. In the first part, we compare the (almost) fair CRPS, a fair global energy score, and a graph energy score based on node neighbourhoods. Across standard verification metrics, forecast skill is broadly similar. In the extratropics we find only small differences, while in the tropics the graph energy score setup performs somewhat better and the global energy score shows some degradation. These results suggest that multivariate scores are a viable alternative to CRPS-based training for global machine-learned weather forecasting. In the second part of the study, we analyse how different scoring rules and scale-aware loss constraints shape the spectra of forecast fields. It is apparent that any form of explicit scale-awareness improves realism. Here, the largest differences are likely associated with different effective weights per scale. All scores are implemented in the Anemoi framework.

## 1Introduction

Machine-learned weather forecasting has advanced rapidly in recent years, with probabilistic global models now reaching competitive skill at a fraction of the cost of traditional ensemble prediction systems. A common approach for training ensemble models is to optimize a proper scoring rule as the training loss, for example, the continuous ranked probability score (CRPS) and its fair or almost fair variants[9,16]. AIFS-CRPS[13]proposes end-to-end CRPS-based training for global fully machine-learned probabilistic weather models, an approach that has since also been used in recent global models such as FGN[1], FourCastNet 3[4], Huracan[17], and others[7,8,20]. The approach is also being applied for regional and high-resolution forecasting, including limited-area[15]and stretched-grid modelling[18]. Meanwhile, proper-score training has now also been explored outside machine-learned weather forecasting, for example in climate downscaling[23], for training probabilistic neural operators[5]and learned probabilistic filtering for data assimilation[3]. Graph neural networks and multivariate score-based objectives have also been used for ensemble post-processing[12].

Here, we address the question whether the recent success of state of the art probabilistic machine-learned weather forecasting is tied specifically to pointwise scores such as CRPS, or whether similar results can also be obtained with multivariate scoring rule optimisation, similar to[19]. We compare the forecast skill of models trained with different loss objectives, with the aim to test whether multivariate spatial training objectives can match the large-scale forecast skill obtained with CRPS-based training. Furthermore, we assess the impact of different approaches that inject scale awareness[14]into the loss objective on spectra of forecast fields. Because spectra characterize how variance is distributed across spatial scales, they provide a useful diagnostic of whether forecast fields reproduce the scale-dependent structure of the atmosphere.

## 2Probabilistic Scores

We consider an ensemble of sizeMM, with ensemble membersx(1),…,x(M)x^{(1)},\dots,x^{(M)}and verifying targetyy.
Fair variants correct the finite-ensemble bias of empirical score estimates that arises from using onlyMMensemble members[9].
We usemmandℓ\ellfor ensemble-member indices,ggfor generic grid-point indices,nnfor a destination graph node,jjfor a source graph node,iifor scale indices,κ\kappafor spectral-mode indices, and𝒢\mathcal{G}for the neighbourhood graph.
For scalar scores,x(m)x^{(m)}andyyare single values at one grid point.
For multivariate scores of fields,x(m)x^{(m)}andyyare vectors containing values at the grid points of the field. All scores are defined for a single forecast step and a single output variable. Hence, in the following, the energy score, graph energy score, graph variogram score, and graph edge energy score are multivariate over space or local edge differences for that variable, not across different output variables.
When a score is aggregated over the discrete forecast grid, we use spatial quadrature weightsωg>0\omega_{g}>0, normalized so that∑g=1Gωg=1\sum_{g=1}^{G}\omega_{g}=1.

## CRPS

For scalar quantities, the standard (unfair) CRPS can be written in kernel form[10]asCRPS​(x(1:M),y)=1M​∑m=1M|x(m)−y|−12​M2​∑m=1M∑ℓ=1M|x(m)−x(ℓ)|.\mathrm{CRPS}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left|x^{(m)}-y\right|-\frac{1}{2M^{2}}\sum_{m=1}^{M}\sum_{\ell=1}^{M}\left|x^{(m)}-x^{(\ell)}\right|.

The fair version is then[9,16]:fCRPS​(x(1:M),y)=1M​∑m=1M|x(m)−y|−12​M​(M−1)​∑m=1M∑ℓ=1ℓ≠mM|x(m)−x(ℓ)|.\mathrm{fCRPS}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left|x^{(m)}-y\right|-\frac{1}{2M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left|x^{(m)}-x^{(\ell)}\right|.

However, the fCRPS has a degeneracy: When all but one ensemble member are equal to the observation, the remaining member is unconstrained by the score.
Following[13], an almost fair variant can be defined as a convex combination of the standard and fair scores,afCRPSα​(x(1:M),y)=α​fCRPS​(x(1:M),y)+(1−α)​CRPS​(x(1:M),y),\mathrm{afCRPS}_{\alpha}(x^{(1:M)},y)=\alpha\,\mathrm{fCRPS}(x^{(1:M)},y)+(1-\alpha)\,\mathrm{CRPS}(x^{(1:M)},y),

withα∈[0,1]\alpha\in[0,1].
Using the kernel representation, this becomesafCRPSα​(x(1:M),y)=1M​∑m=1M|x(m)−y|−12​1−ϵM​(M−1)​∑m=1M∑ℓ=1ℓ≠mM|x(m)−x(ℓ)|,ϵ=1−αM.\mathrm{afCRPS}_{\alpha}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left|x^{(m)}-y\right|-\frac{1}{2}\frac{1-\epsilon}{M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left|x^{(m)}-x^{(\ell)}\right|,\qquad\epsilon=\frac{1-\alpha}{M}.

Thusα=1\alpha=1recovers the fair CRPS, whileα=0\alpha=0recovers the standard CRPS.
For a field, the pointwise score is aggregated with the spatial weights,ℒafCRPS,α=∑g=1Gωg​afCRPSα​(xg(1:M),yg).\mathcal{L}_{\mathrm{afCRPS},\alpha}=\sum_{g=1}^{G}\omega_{g}\,\mathrm{afCRPS}_{\alpha}\left(x_{g}^{(1:M)},y_{g}\right).

## Energy Score

The energy score is a multivariate score[10]. Here, we compute it over the whole spatial field of a single output variable.
For a field differenced∈ℝGd\in\mathbb{R}^{G}overGGgrid points, it uses the spatially weighted Euclidean norm‖d‖W=(∑g=1Gωg​dg2)1/2,\|d\|_{W}=\left(\sum_{g=1}^{G}\omega_{g}\,d_{g}^{2}\right)^{1/2},

whereωg\omega_{g}are the spatial grid weights defined above.
The standard (unfair) energy score isES​(x(1:M),y)=1M​∑m=1M‖x(m)−y‖W−12​M2​∑m=1M∑ℓ=1M‖x(m)−x(ℓ)‖W\mathrm{ES}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left\|x^{(m)}-y\right\|_{W}-\frac{1}{2M^{2}}\sum_{m=1}^{M}\sum_{\ell=1}^{M}\left\|x^{(m)}-x^{(\ell)}\right\|_{W}

and the fair energy score[9]is given byfES​(x(1:M),y)=1M​∑m=1M‖x(m)−y‖W−12​M​(M−1)​∑m=1M∑ℓ=1ℓ≠mM‖x(m)−x(ℓ)‖W.\mathrm{fES}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left\|x^{(m)}-y\right\|_{W}-\frac{1}{2M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left\|x^{(m)}-x^{(\ell)}\right\|_{W}.

Compared with the CRPS, this score treats the whole field as one vector, so it measures whether the ensemble reproduces the joint spatial state and not only the marginal distribution at each grid point.

## Graph Energy Score

The graph energy score localizes the energy score by replacing the norm computed over the full spatial field with a weighted neighbourhood norm defined on a graph.
The motivation is similar to the patched energy score of[19], where a multivariate score is evaluated on localized subsets and then aggregated. This kind of localization is intended to make the score more sensitive to local multivariate relationships than a purely global energy score. In the weather forecasting experiments of[19], patched energy scores performed best among the multivariate scoring rules they considered, which motivates exploring a graph-based localization in the present setting. Compared with earlier patch-based localization approaches, we use local graph neighbourhoods on the data grid, which provide a more flexible way to localize multivariate scoring rules. An advantage of the graph-based approach is that it does not rely on fixed rectangular patches on a regular grid. Instead, it only requires a neighbourhood graph and associated weights, so the same score can in principle be applied on irregular grids, sparse spatial meshes, or sparse observation networks.
For a target nodenn, let𝒩​(n)\mathcal{N}(n)be its open incoming neighbourhood, i.e. the source nodes connected tonnexcludingnnitself, and let𝒩​[n]=𝒩​(n)∪{n}\mathcal{N}[n]=\mathcal{N}(n)\cup\{n\}

be the corresponding closed neighbourhood.
For the graph energy score we use the closed neighbourhood𝒩​[n]\mathcal{N}[n], with edge weightsan​ja_{nj}forj∈𝒩​[n]j\in\mathcal{N}[n].
The self-node contribution is included.
We use normalised uniform edge weightsan​j=an=1/|𝒩​[n]|a_{nj}=a_{n}=1/{|\mathcal{N}[n]|}, resulting in a unit sum∑j∈𝒩​[n]an​j=1.\sum_{j\in\mathcal{N}[n]}a_{nj}=1.

At destination nodenn, the weighted neighbourhood norm is‖d‖𝒢,n=(∑j∈𝒩​[n]an​j​dj2)1/2.\|d\|_{\mathcal{G},n}=\left(\sum_{j\in\mathcal{N}[n]}a_{nj}\,d_{j}^{2}\right)^{1/2}.

The fair graph energy score at target nodennis thenfGESn​(x(1:M),y)=1M​∑m=1M‖x(m)−y‖𝒢,n−12​M​(M−1)​∑m=1M∑ℓ=1ℓ≠mM‖x(m)−x(ℓ)‖𝒢,n,\mathrm{fGES}_{n}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left\|x^{(m)}-y\right\|_{\mathcal{G},n}-\frac{1}{2M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left\|x^{(m)}-x^{(\ell)}\right\|_{\mathcal{G},n},

and the corresponding spatially aggregated graph energy score isfGESgraph​(x(1:M),y)=∑n=1Gωn​fGESn​(x(1:M),y).\mathrm{fGES}_{\mathrm{graph}}(x^{(1:M)},y)=\sum_{n=1}^{G}\omega_{n}\,\mathrm{fGES}_{n}(x^{(1:M)},y).

Instead of scoring the full domain at once, the graph energy score scores each node using only the structure in its prescribed neighbourhood, which makes the loss more sensitive to local spatial organization. Across the full domain, we evaluate this local score at every destination nodenn. This is equivalent to a sliding-window score evaluated at every node, with maximal overlap between adjacent windows. Here, however, each local window is defined by the closed graph neighbourhood𝒩​[n]\mathcal{N}[n]and weightsan​ja_{nj}rather than by a fixed rectangular stencil. Figure1(top-left panel) shows the construction at one destination node.

The energy score is strictly proper. The graph energy score, however, may fail to be strictly proper because different distributions can lead to the same local score even though they differ in their long-range dependence. This can be illustrated by simple counterexamples. Strict propriety may be recovered under additional assumptions, but it is not guaranteed in general. We therefore follow[19]and combine the proper graph energy score with a weak global anchor in the form of the fair energy score. This kind of combination of proper scoring rules preserves propriety for non-negative weights and can be used to target complementary features of multivariate forecasts[21]. The global component captures dependencies that are invisible to the local score and makes the combined score strictly proper.Graph energy scoreu1u_{1}u2u_{2}u3u_{3}u4u_{4}nndu1d_{u_{1}}du2d_{u_{2}}du3d_{u_{3}}du4d_{u_{4}}dnd_{n}dj=xj−yjd_{j}=x_{j}-y_{j},j∈𝒩​[n]j\in\mathcal{N}[n]
‖d‖𝒢,n=(∑j∈𝒩​[n]an​j​dj2)1/2\|d\|_{\mathcal{G},n}=\bigl(\sum_{j\in\mathcal{N}[n]}a_{nj}d_{j}^{2}\bigr)^{1/2}Graph variogram scoreu1u_{1}u2u_{2}u3u_{3}u4u_{4}nnvn​u1​(z)v_{nu_{1}}(z)vn​u2​(z)v_{nu_{2}}(z)vn​u3​(z)v_{nu_{3}}(z)vn​u4​(z)v_{nu_{4}}(z)vn​j​(z)=|zj−zn|pv_{nj}(z)=|z_{j}-z_{n}|^{p},v¯n​j=M−1​∑mvn​j​(x(m))\bar{v}_{nj}=M^{-1}\sum_{m}v_{nj}(x^{(m)})
GVSn=∑j∈𝒩​(n)an​j​(v¯n​j−vn​j​(y))2\mathrm{GVS}_{n}=\sum_{j\in\mathcal{N}(n)}a_{nj}(\bar{v}_{nj}-v_{nj}(y))^{2}Graph edge energy / CRPS edge scoreu1u_{1}u2u_{2}u3u_{3}u4u_{4}nnrn​u1​(z)r_{nu_{1}}(z)rn​u2​(z)r_{nu_{2}}(z)rn​u3​(z)r_{nu_{3}}(z)rn​u4​(z)r_{nu_{4}}(z)Edge differences:rn​j​(z)=zj−znr_{nj}(z)=z_{j}-z_{n}
Joint edge-difference score:‖z−z′‖Δ,n\|z-z^{\prime}\|_{\Delta,n}or CRPSFigure 1:Different scores for a single destination nodenn: the graph energy score (top left) evaluates forecast errors on the closed neighbourhood𝒩​[n]\mathcal{N}[n], which includes the destination node itself, and aggregates them through a weighted neighbourhood norm. The graph variogram score (top right) evaluates squared differences between forecast and observed variogram values on the open neighbourhood𝒩​(n)\mathcal{N}(n). The edge-scores (bottom) use edge differences, either as one local vector for the graph edge energy score or as scalar quantities for the CRPS edge score. Final scores are then obtained by spatial aggregation over destination nodes with weightsωn\omega_{n}. In the schematic,u1,…,u4u_{1},\dots,u_{4}denote example source nodes in𝒩​(n)\mathcal{N}(n).

## Graph Variogram Score

The graph variogram score is a variant of the variogram score[22]. It uses the same fully overlapping node neighbourhood formulation as the graph energy score, but replaces node values by per-edge variogram differences. For an edge from source nodejjto destination nodenn, the variogram transform isvn​j​(z)=|zj−zn|p,v_{nj}(z)=\left|z_{j}-z_{n}\right|^{p},

wherep>0p>0is the variogram exponent.
For the graph variogram score, we use the open neighbourhood𝒩​(n)\mathcal{N}(n), so the self-edgej=nj=nis not included. The edge weights are uniform and normalised to unit suman​j=1/|𝒩​(n)|a_{nj}=1/{|\mathcal{N}(n)|}, i.e.∑j∈𝒩​(n)an​j=1\sum_{j\in\mathcal{N}(n)}a_{nj}=1. Figure1(top-right panel) shows the corresponding formulation on the same neighbourhood graph.

For a single nodenn, the standard (unfair) graph variogram score aggregates squared differences between the observed variogram and the ensemble-mean variogram:GVSn​(x(1:M),y)=∑j∈𝒩​(n)an​j​(1M​∑m=1Mvn​j​(x(m))−vn​j​(y))2.\mathrm{GVS}_{n}(x^{(1:M)},y)=\sum_{j\in\mathcal{N}(n)}a_{nj}\left(\frac{1}{M}\sum_{m=1}^{M}v_{nj}(x^{(m)})-v_{nj}(y)\right)^{2}.

To derive the fair score, we define the weighted squared distance between two local variogram vectors asDn2​(x,x′)=∑j∈𝒩​(n)an​j​(vn​j​(x)−vn​j​(x′))2.D_{n}^{2}(x,x^{\prime})=\sum_{j\in\mathcal{N}(n)}a_{nj}\left(v_{nj}(x)-v_{nj}(x^{\prime})\right)^{2}.

Then we obtain the fair graph variogram score:fGVSn​(x(1:M),y)=1M​∑m=1MDn2​(x(m),y)−12​M​(M−1)​∑m=1M∑ℓ=1ℓ≠mMDn2​(x(m),x(ℓ)).\mathrm{fGVS}_{n}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}D_{n}^{2}(x^{(m)},y)-\frac{1}{2M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}D_{n}^{2}(x^{(m)},x^{(\ell)}).

The corresponding spatially aggregated graph variogram score isfGVSgraph​(x(1:M),y)=∑n=1Gωn​fGVSn​(x(1:M),y).\mathrm{fGVS}_{\mathrm{graph}}(x^{(1:M)},y)=\sum_{n=1}^{G}\omega_{n}\,\mathrm{fGVS}_{n}(x^{(1:M)},y).

The score measures whether the ensemble reproduces local spatial variability.

## Graph Edge Energy Score

The graph edge energy score uses the same open neighbourhood as the graph variogram score, but uses the edge differences rather than applying the variogram transform. For an edge from source nodejjto destination nodenn, we definern​j​(z)=zj−zn,j∈𝒩​(n).r_{nj}(z)=z_{j}-z_{n},\qquad j\in\mathcal{N}(n).

Using the uniform normalized edge weights with∑j∈𝒩​(n)an​j=1\sum_{j\in\mathcal{N}(n)}a_{nj}=1, the edge-differences feature vector isrn​(z)=(an​j​rn​j​(z))j∈𝒩​(n).r_{n}(z)=\left(\sqrt{a_{nj}}\,r_{nj}(z)\right)_{j\in\mathcal{N}(n)}.

The edge-difference distance is defined as‖z−z′‖Δ,n=‖rn​(z)−rn​(z′)‖=(∑j∈𝒩​(n)an​j​[(zj−zn)−(zj′−zn′)]2)1/2.\|z-z^{\prime}\|_{\Delta,n}=\|r_{n}(z)-r_{n}(z^{\prime})\|=\left(\sum_{j\in\mathcal{N}(n)}a_{nj}\left[(z_{j}-z_{n})-(z^{\prime}_{j}-z^{\prime}_{n})\right]^{2}\right)^{1/2}.

The fair graph edge energy score at nodennapplies the fair energy score to this vector of edge differences:fGEESn​(x(1:M),y)=1M​∑m=1M‖x(m)−y‖Δ,n−12​M​(M−1)​∑m=1M∑ℓ=1ℓ≠mM‖x(m)−x(ℓ)‖Δ,n.\mathrm{fGEES}_{n}(x^{(1:M)},y)=\frac{1}{M}\sum_{m=1}^{M}\left\|x^{(m)}-y\right\|_{\Delta,n}-\frac{1}{2M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left\|x^{(m)}-x^{(\ell)}\right\|_{\Delta,n}.

The corresponding spatially aggregated graph edge energy score isfGEES​(x(1:M),y)=∑n=1Gωn​fGEESn​(x(1:M),y).\mathrm{fGEES}(x^{(1:M)},y)=\sum_{n=1}^{G}\omega_{n}\,\mathrm{fGEES}_{n}(x^{(1:M)},y).

The score compares the joint vector of edge differences in the local neighbourhood𝒩​(n)\mathcal{N}(n). Compared with the graph variogram score, it preserves the sign of the edge differences.

## CRPS Edge Score

The CRPS edge score uses the same open neighbourhood𝒩​(n)\mathcal{N}(n), normalized weightsan​ja_{nj}, and edge differencesrn​j​(z)r_{nj}(z)as the graph edge energy score, but scores each edge difference as a scalar quantity. For the almost fair edge CRPS, the scalar score on edge(j,n)(j,n)isECRPSα,n​j​(x(1:M),y)\displaystyle\mathrm{ECRPS}_{\alpha,nj}(x^{(1:M)},y)=1M​∑m=1M|rn​j​(x(m))−rn​j​(y)|\displaystyle=\frac{1}{M}\sum_{m=1}^{M}\left|r_{nj}(x^{(m)})-r_{nj}(y)\right|−12​1−ϵM​(M−1)​∑m=1M∑ℓ=1ℓ≠mM|rn​j​(x(m))−rn​j​(x(ℓ))|,ϵ=1−αM.\displaystyle\quad-\frac{1}{2}\frac{1-\epsilon}{M(M-1)}\sum_{m=1}^{M}\sum_{\begin{subarray}{c}\ell=1\\
\ell\neq m\end{subarray}}^{M}\left|r_{nj}(x^{(m)})-r_{nj}(x^{(\ell)})\right|,\qquad\epsilon=\frac{1-\alpha}{M}.

At each destination nodenn, the score is then aggregated over the source nodesjjECRPSα,n​(x(1:M),y)=∑j∈𝒩​(n)an​j​ECRPSα,n​j​(x(1:M),y).\mathrm{ECRPS}_{\alpha,n}(x^{(1:M)},y)=\sum_{j\in\mathcal{N}(n)}a_{nj}\,\mathrm{ECRPS}_{\alpha,nj}(x^{(1:M)},y).

The spatially aggregated edge CRPS is then given byECRPSα​(x(1:M),y)=∑n=1Gωn​ECRPSα,n​(x(1:M),y).\mathrm{ECRPS}_{\alpha}(x^{(1:M)},y)=\sum_{n=1}^{G}\omega_{n}\,\mathrm{ECRPS}_{\alpha,n}(x^{(1:M)},y).

The edge CRPS assesses whether, for each edge, the marginal ensemble distribution of edge differences matches the observed difference.
Figure1(bottom panel) shows how the edge-difference are defined for the graph edge energy score and the edge CRPS.
Because both edge scores, like the graph variogram score, depend only on differences along graph edges, they should be combined with a score that
constrains the absolute node values.

## Multi-Scale Score definition

We use the multi-scale loss formulation of[14]. For scalar fields on a spatial manifoldℳ\mathcal{M}, letx(m):ℳ→ℝ,y:ℳ→ℝ,x^{(m)}:\mathcal{M}\to\mathbb{R},\qquad y:\mathcal{M}\to\mathbb{R},

denote themm-th ensemble member and target field. In the discrete case, the integrals below are replaced by the corresponding weighted sums over grid points.

For a pointwise scalar scoring rule𝒮\mathcal{S}, the scale-unaware loss isℒscale-unaware=c​∫ℳ𝒮​([x(m)​(q)∣m=1,…,M],y​(q))​dμ​(q),\mathcal{L}_{\text{scale-unaware}}=c\int_{\mathcal{M}}\mathcal{S}\!\left(\left[x^{(m)}(q)\mid m=1,\dots,M\right],y(q)\right)\,\mathrm{d}\mu(q),

whereμ\muis a measure onℳ\mathcal{M}andccis a normalization constant. This applies the score at each locationq∈ℳq\in\mathcal{M}, followed by spatial aggregation. It is not scale-aware because the score only sees the marginal ensemble distribution at each location.

The multi-scale loss introduces ordered smoothing operatorsD1,…,DK−1D_{1},\dots,D_{K-1}, whereDiD_{i}smooths more strongly thanDi+1D_{i+1}. These operators partition a field intoKKresidual scale bands:zscale​1=D1​z,z_{\mathrm{scale}\,1}=D_{1}z,zscale​i=Di​z−Di−1​z,i=2,…,K−1,z_{\mathrm{scale}\,i}=D_{i}z-D_{i-1}z,\qquad i=2,\dots,K-1,zscale​K=z−DK−1​z.z_{\mathrm{scale}\,K}=z-D_{K-1}z.

The first band contains the coarsest component, while later bands contain progressively finer residuals. This approach is similar to a Laplacian-pyramid or Laplacian-cascade decomposition[6]: successive low-pass filtered fields define residual bands that are localized in scale. Following[14], we use the same idea as a scale decomposition for scoring. The smoothing operators may be implemented as spatial kernel smoothers with decreasing width, or as spectral filters when a suitable transform is available.

TheKK-scale loss is then the weighted sum of the loss on each scale band:ℒK​-scale=∑i=1Kζi​c​∫ℳ𝒮​([xscale​i(m)​(q)∣m=1,…,M],yscale​i​(q))​dμ​(q),\mathcal{L}_{K\text{-scale}}=\sum_{i=1}^{K}\zeta_{i}\,c\int_{\mathcal{M}}\mathcal{S}\!\left(\left[x^{(m)}_{\mathrm{scale}\,i}(q)\mid m=1,\dots,M\right],y_{\mathrm{scale}\,i}(q)\right)\,\mathrm{d}\mu(q),

with scale weightζi>0\zeta_{i}>0. The approach is score-agnostic: once the fields are decomposed into scale bands, any suitable scoring rule can be applied separately to each band.

## Scores in spectral space

Another approach to introduce scale awareness is via the application of scoring rules in spectral space. This proceeds by
transforming each scalar forecast field to a spectral representation. Let𝒯\mathcal{T}denote a spectral transform and writex^κ(m)=(𝒯​x(m))κ,y^κ=(𝒯​y)κ,\widehat{x}^{(m)}_{\kappa}=(\mathcal{T}x^{(m)})_{\kappa},\qquad\widehat{y}_{\kappa}=(\mathcal{T}y)_{\kappa},

where a hat denotes the (complex) coefficient, or mode, of the spectral representation of the corresponding variable at wavenumberκ\kappa. The score is evaluated mode by mode and then aggregated over modes.

The exact kind of transform𝒯\mathcal{T}used depends on the nature of the grid on which the score is being calculated. For a global grid with Gaussian latitudes, a transform based on spherical harmonics is an obvious choice, for example. This, and other spectral transforms which operate on two-dimensional fields, gives a spectral decomposition with two wavenumber indices (total and zonal wavenumbers for a spherical harmonic decomposition). Here we do not distinguish between the two wavenumber indices and simply iterate over all wavenumber combinations with a single index,κ\kappa.

We test two variants. The spectral energy score treats each complex coefficient as a two-dimensional real vector and scores the 2-dim vectors with the energy score. This score is sensitive to both amplitude and phase. The spectral magnitude CRPS applies the CRPS to the modulus of the spectral coefficients. The spectral magnitude CRPS constrains the distribution of spectral amplitudes, but does not penalize phase errors.

For the spectral energy score, we definezκ(m)=(Re​x^κ(m),Im​x^κ(m)),zκy=(Re​y^κ,Im​y^κ).z_{\kappa}^{(m)}=\left(\mathrm{Re}\,\widehat{x}^{(m)}_{\kappa},\mathrm{Im}\,\widehat{x}^{(m)}_{\kappa}\right),\qquad z_{\kappa}^{y}=\left(\mathrm{Re}\,\widehat{y}_{\kappa},\mathrm{Im}\,\widehat{y}_{\kappa}\right).

The score at modeκ\kappais then an energy score applied to the 2-dim vectorszκ(1:M)z_{\kappa}^{(1:M)}andzκyz_{\kappa}^{y}.
For the spectral magnitude CRPS, the scalar quantities|x^κ(m)||\widehat{x}^{(m)}_{\kappa}|and|y^κ||\widehat{y}_{\kappa}|are scored with the CRPS.
In both cases, we are left with a vector of scores, one per spectral mode. The full spectral score is obtained by aggregating over all spectral modesκ\kappa, optionally with spectral-band weights.

## 3Experiments

We conduct two sets of experiments. The first assesses the sensitivity of forecast skill to the use of different proper scoring rules as training objectives. The second assesses how different ways of introducing scale awareness into the loss objective affect the global spectra of forecast fields. In both sets of experiments, as stated above, all losses are computed separately for each output variable before they are aggregated across variables.
The first set of experiments is described in section3.1. It comprises three experiments based on the CRPS, the fair global energy score, and the fair graph energy score. The second set is described in section3.2. It comprises twelve experiments with different loss configurations, which we compare in terms of how they shape the spectra of the forecast fields.

## 3.1Proper score forecast skill comparison

We follow AIFS-CRPS[13]in terms of architecture and general training configuration, but restrict resolution here to an O96≈1​deg\approx 1\degmodel. We use the Anemoi framework (https://github.com/ecmwf/anemoi-core) for experimentation. AIFS-CRPS has an encoder–processor–decoder architecture. In our experiments, the encoder maps from the data grid to the processor grid using a graph neural network, with each data-grid node connected to its four nearest processor-grid nodes. The decoder maps from the processor grid back to the data grid, with each data-grid node connected to its eight nearest processor-grid nodes. The graph connectivity for the graph-based scores is defined by akk-nearest-neighbour graph withk=16k=16on the O96 reduced Gaussian grid. The training schedule uses 150,000 iterations at rollout 1, 30,000 iterations at rollout 2, and then 1,000 iterations at each rollout step from 3 to 12. For rollout 1 and rollout 2, we use a cosine learning-rate schedule with a warmup of 1,000 steps followed by decay to zero. The learning rate is10−310^{-3}for rollout 1 and10−510^{-5}for rollout 2. For rollout steps 3 to 12, we use a fixed learning rate of10−610^{-6}. In all cases, optimization uses AdamW with weight decay 0.1. For scores computed in spectral space, we use the spherical harmonic transform capability recently added to Anemoi to transform fields. Training uses ERA5 reanalysis data[11]from 1979 to 2020, and inference is performed for 2022. Here we generate 8-member ensembles to compare forecast scores.
We run three experiments. The univariate baseline experiment uses the almost fair CRPS withα=0.95\alpha=0.95. The second uses the fair energy score. Hence, the whole field is scored jointly through a global spatial score. The third experiment uses the fair graph energy score together with a weak global fair energy score anchor,ℒgraph=fGESgraph+0.1​fES\mathcal{L}_{\mathrm{graph}}=\mathrm{fGES}_{\mathrm{graph}}+0.1\,\mathrm{fES}.

To make score computations efficient, we rely ontorch.compile[2]to generate fused Triton kernels[24].ExperimentTraining objectiveCRPSCRPSGlobal energy scoreEnergy score applied per variable to the full forecast fieldGraph energyGraph energy score with a weak global energy score anchorTable 1:Loss objectives used in the experiments described in section3.1. The CRPS experiment uses the almost fair CRPS withα=0.95\alpha=0.95. The global energy and graph energy terms use the
corresponding fair variants described in section2

## 3.2Impact on spectra of forecast fields

The setup follows section3.1, except that we use a smaller model and a shorter training schedule to reduce computational cost. We use an embedding dimension of 256 and 12 processor layers. Training has only two phases. First, the model is trained as a one-step forecast model for up to 150,000 optimization steps. Second, the corresponding one-step model is used to initialize rollout training. In this phase, we train for 1,000 optimization steps at each rollout length, increasing the rollout length one step at a time up to eight forecast steps, which corresponds to 48 hours lead time.

The loss configuration of the twelve different experiments is described in table2. The single-scale CRPS experiment and the global energy score experiment are the same as the corresponding experiments described in Sec.3.1apart from the cheaper configuration and modified training schedule. For multi-scale experiments, we used different weighting for the small scales of geopotential and mean sea-level pressure, to account for the reduced variance associated with small scales of these fields compared to, e.g. wind. We used a similar approach for the spectral losses with per-waveband weighting. These weighting factors are ad hoc and were chosen only to be of the right order of magnitude - estimated from the data - rather than tuned. In the almost fair CRPS experiments we always setα=0.95\alpha=0.95.

All multi-scale experiments used four graph-based Gaussian smoothing operators on the native O96 grid, with kernel widths of approximately100100,200200,400400, and800800km. The spectral losses used a spherical harmonic transform with truncation T191. For the weighted spectral experiments, spectral modes were grouped according to their total wavenumberℓ\ell, using the bandsℓ=0\ell=0–1010,1111–2020,2121–8080,8181–120120, and121121–191191.ExperimentTraining objectiveSingle-scale CRPSCRPSMulti-scale CRPSMulti-scale version of CRPSMulti-scale edge CRPSMulti-scale CRPS combined with edge CRPSGlobal energy scoreEnergy score applied per variable to the full forecast fieldMulti-scale global energy scoreMulti-scale version of the global energy scoreMulti-scale graph energyMulti-scale graph energy score with a weak global energy score anchorMulti-scale graph edge energyMulti-scale graph energy score combined with the graph edge energy score and a weak global energy score anchorMulti-scale variogramMulti-scale CRPS combined with the graph variogram scoreSpectral energy scoreCRPS combined with the spectral energy scoreSpectral magnitude CRPSCRPS combined with CRPS on spectral-coefficient magnitudesSpectral energy score weightedAs spectral energy, but with band and variable weightingSpectral mag. CRPS weightedAs spectral magnitude, but with band and variable weightingTable 2:Loss objectives used in the experiments described in section3.2. CRPS-based terms use the almost fair CRPS withα=0.95\alpha=0.95. Energy score, graph energy, graph edge energy, and graph variogram terms use the corresponding fair variants described in section2, for further details see section3.2.

## 4Results

## 4.1Forecast Skill Comparison

We first assess how sensitive forecast skill is to the choice of the proper scoring rule used as the training objective. We compare three experiments that use the almost fair CRPS, the fair global energy score, and the fair graph energy score, respectively. The architecture, training configuration, and data are otherwise kept the same across the three experiments, as described in section3.1. For scoring, we interpolate the fields to a resolution of1.5​deg1.5\degand evaluate forecast skill using the fair CRPS.

Forecast skill is broadly similar across the experiments (see figure2). In the extratropics, we do not find a noticeable difference between the three training objectives. In the tropics, however, the graph energy score experiment appears to perform best, while the energy score experiment shows some degradation relative to the other two experiments.
The conclusions are also consistent when the fair energy score or fair graph energy score is used for verification instead of the fair CRPS.

Figure 2:Comparison of the CRPS, energy score, and graph energy score experiments. The top row shows wind speed at 850 hPa, the middle row temperature at 850 hPa, and the bottom row geopotential at 500 hPa. Within each row, the left panel corresponds to the Northern Hemisphere, the middle panel to the Southern Hemisphere, and the right panel to the tropics.

## 4.2Spectra of Forecast Fields

We next assess how sensitive the spectra of forecast fields are to the choice of training objective. We compare the twelve experiments described in section3.2. Their loss objectives are based on different combinations of the probabilistic scores introduced in section2. We test how the different loss objectives affect the representation of variability at different spatial scales.

Different loss objectives can constrain different aspects of forecast fields. To assess the impact of the loss objectives on forecast field variability and physical realism, we compute spectra of accumulated forecast tendencies for the experiments described in section3.2. The accumulated tendencies are the differences between the state at a given lead time and the initial state. For ERA5, they are the differences between analyses at the corresponding valid time and initial time. Spectra are computed from 2022 forecasts initialized every four days from 1 January to 1 December at 00 UTC, 84 initialization dates in total. In addition, we compute spectra for ERA5 analyses as a reference. For the forecast fields, we average spectra over all ensemble members and use a spectral truncation of T191. In the following, we show accumulated tendency spectra and ratios of forecasts versus ERA5, for geopotential, meridional wind, and temperature at 500 hPa (figures3–14).

In these experiments, the single-scale CRPS and global energy score poorly constrain small-scale variability. The global energy score does not appear to offer an advantage over CRPS. This is consistent with previous work showing that the energy score can be relatively insensitive to correlation structure, especially in high-dimensional settings[22,19].

Making the forecast scores scale-aware substantially improves small-scale variability and leads to more realistic forecast fields. This is true both for the multi-scale loss formalism and for spectral scores. However, scale awareness alone does not guarantee realistic variability at all scales and for all variables, as shown by the differences between spectral loss experiments with and without scale- and variable-dependent weighting: simply adding a spectral loss term constrains smaller scale variability, but not to the same degree as the multi-scale experiments that include different weighting per scale (see figure3and figure5). However, after introducing waveband weighting factors, the spectra look very similar.

In general, achieving realistic spectra for geopotential appears more challenging than realistic spectra for wind and temperature in these experiments. For all variables, differences between scale-aware loss objectives are comparatively small. The edge-CRPS experiment and the spectral magnitude CRPS experiment seem to be slightly more successful in constraining small scales for most variables than the other experiments. Some experiments show a slight overcompensation for some variables, where the early lead-time tendencies contain less small-scale variability than the ERA5 reference tendency.Figure 3:Accumulated tendency spectra for geopotential at 500 hPa.Figure 4:Accumulated tendency spectra for geopotential at 500 hPa.Figure 5:Accumulated tendency-spectrum ratios for geopotential at 500 hPa.Figure 6:Accumulated tendency-spectrum ratios for geopotential at 500 hPa.Figure 7:Accumulated tendency spectra for meridional wind at 500 hPa.Figure 8:Accumulated tendency spectra for meridional wind at 500 hPa.Figure 9:Accumulated tendency-spectrum ratios for meridional wind at 500 hPa.Figure 10:Accumulated tendency-spectrum ratios for meridional wind at 500 hPa.Figure 11:Accumulated tendency spectra for temperature at 500 hPa.Figure 12:Accumulated tendency spectra for temperature at 500 hPa.Figure 13:Accumulated tendency-spectrum ratios for temperature at 500 hPa.Figure 14:Accumulated tendency-spectrum ratios for temperature at 500 hPa.

## 5Discussion and Conclusion

In our forecast skill experiments, all loss objectives lead to similar large-scale skill, although the tropical results show some separation, with the graph energy score experiment performing best and the energy score experiment showing some degradation. These results suggest that localized multivariate training objectives are a promising alternative to CRPS-based training, whereas the purely global energy score appears less robust in the present setup. The graph-based approach offers a flexible alternative to patch-based localization because it is not tied to fixed rectangular windows on a structured grid and can therefore be applied to irregular grids or sparse observation networks. The same approach could also be extended to local space-time neighbourhoods.

Realistic spectra of forecast fields are one measure of physical realism. Different ways have been proposed to improve spectral representation in machine-learned weather forecast models. For example,[13]injects noise via conditional layer norms and then applies reference field truncation, where the model forecasts a tendency relative to a truncated, low resolution version of the input state. The now operational version of the AIFS ensemble uses the scale aware loss formulation introduced in[14]. Like AIFS-CRPS, FGN[1]injects noise via conditional layer norms, but uses a single noise vector at all locations instead of spatially varying random fields, to encourage coherence in forecast fields. FourCastNet 3 has a spectral loss term like the spectral magnitude CRPS loss. In addition, it makes use of spatially correlated random fields, and instead of using a truncated reference state, uses its lower resolution processor grid representation interpolated to the output resolution to decode the output fields[4]. Spectral fidelity has also been targeted directly through attention at native resolution[25].

Our results show that scale-aware losses improve spectral fidelity. The weighting of different fields, scales, and variables can matter as much as, or more than, the specific mechanism that is used to inject spatial awareness into the loss. By comparison, the choice of multivariate score has a smaller effect.

One limitation of the study is that experiments were conducted with smaller models, relatively low spatial resolution, and a shortened training schedule. Greater model capacity and longer training may improve the performance of losses without scale awareness or reduce the differences between experiments using different weightings. More testing would be needed to understand what role model architecture plays. In addition, experiments at higher resolution may yield different conclusions, as maintaining spatial coherence across forecast fields is particularly challenging at high resolution[18].

Overall, multivariate scoring rules are a promising direction for generative modelling, but further research is needed to better understand how results depend on localization, scale awareness and model architecture.

## Acknowledgements

The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) for funding this project by providing computing time on the GCS Supercomputer JUPITER at Jülich Supercomputing Centre (JSC). We acknowledge the EuroHPC Joint Undertaking for awarding this project access to the EuroHPC supercomputer Jupiter, hosted by JSC in Juelich, Germany through a EuroHPC JU Special Access call. The authors also gratefully acknowledge all contributors to the Anemoi framework; in particular, we thank Sergio Portilla, Sara Hahner, and Helen Theissen for their contributions related to the spectral transform implementation in Anemoi.

## References
- [1]F. Alet, I. Price, A. El-Kadi, D. Masters, S. Markou, T. R. Andersson, J. Stott, R. Lam, M. Willson, A. Sanchez-Gonzalez, and P. W. Battaglia(2025)Skillful joint probabilistic weather forecasting from marginals.External Links:2506.10772,LinkCited by:§1,§5.
- [2]J. Ansel, E. Yang, H. He, N. Gimelshein, A. Jain, M. Voznesensky, B. Bao, P. Bell, D. Berard, E. Burovski,et al.(2024)PyTorch 2: faster machine learning through dynamic python bytecode transformation and graph compilation.InProceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2,pp. 929–947.External Links:DocumentCited by:§3.1.
- [3]E. Bach, R. Baptista, J. Bröcker, B. Chen, and A. Stuart(2026)Learning probabilistic filters with strictly proper scoring rules.External Links:2606.26497,LinkCited by:§1.
- [4]B. Bonev, T. Kurth, A. Mahesh, M. Bisson, J. Kossaifi, K. Kashinath, A. Anandkumar, W. D. Collins, M. S. Pritchard, and A. Keller(2025)FourCastNet 3: a geometric approach to probabilistic machine-learning weather forecasting at scale.External Links:2507.12144,LinkCited by:§1,§5.
- [5]C. Bülte, P. Scholl, and G. Kutyniok(2025)Probabilistic neural operators for functional uncertainty quantification.External Links:2502.12902,LinkCited by:§1.
- [6]P. J. Burt and E. H. Adelson(1983)The laplacian pyramid as a compact image code.IEEE Transactions on Communications31(4),pp. 532–540.External Links:DocumentCited by:Multi-Scale Score definition.
- [7]S. R. Cachay, D. Watson-Parris, and R. Yu(2026)U-Cast: a surprisingly simple and efficient frontier probabilistic AI weather forecaster.External Links:2604.09041,LinkCited by:§1.
- [8]C. Diaconu, J. Scholz, A. Shysheya, S. Markou, P. Mukhopadhyay, M. Cranmer, and R. E. Turner(2026)Otter Weather: skillful and computationally efficient medium-range weather forecasting.External Links:2606.26421,LinkCited by:§1.
- [9]C. A. T. Ferro(2014)Fair scores for ensemble forecasts.Quarterly Journal of the Royal Meteorological Society140(683),pp. 1917–1923.Cited by:§1,§2,CRPS,Energy Score.
- [10]T. Gneiting and A. E. Raftery(2007)Strictly proper scoring rules, prediction, and estimation.Journal of the American Statistical Association102(477),pp. 359–378.External Links:DocumentCited by:CRPS,Energy Score.
- [11]H. Hersbach, B. Bell, P. Berrisford,et al.(2020)The ERA5 global reanalysis.Quarterly Journal of the Royal Meteorological Society146,pp. 1999–2049.External Links:DocumentCited by:§3.1.
- [12]M. Lakatos(2026)A composite-loss graph neural network for the multivariate post-processing of ensemble weather forecasts.Quarterly Journal of the Royal Meteorological Society.External Links:Document,2509.02784,LinkCited by:§1.
- [13]S. Lang, M. Alexe, M. C. A. Clare, C. Roberts, R. Adewoyin, Z. B. Bouallègue, M. Chantry, J. Dramsch, P. D. Dueben, S. Hahner, P. Maciel, A. Prieto-Nemesio, C. O’Brien, F. Pinault, J. Polster, B. Raoult, S. Tietsche, and M. Leutbecher(2024)AIFS-CRPS: ensemble forecasting using a model trained with a loss function based on the continuous ranked probability score.External Links:2412.15832,LinkCited by:§1,§3.1,§5,CRPS.
- [14]S. Lang, M. Leutbecher, and P. Maciel(2025)A multi-scale loss formulation for learning a probabilistic model with proper score optimisation.External Links:2506.10868,Document,LinkCited by:§1,§5,Multi-Scale Score definition,Multi-Scale Score definition.
- [15]E. Larsson, J. Oskarsson, T. Landelius, and F. Lindsten(2025)CRPS-LAM: regional ensemble weather forecasting from matching marginals.External Links:2510.09484,LinkCited by:§1.
- [16]M. Leutbecher(2019)Ensemble size: how suboptimal is less than infinity?.Quarterly Journal of the Royal Meteorological Society145(S1),pp. 107–128.External Links:Document,LinkCited by:§1,CRPS.
- [17]Z. Ni, J. A. Weyn, H. Zhang, Y. Xiang, J. Bian, W. Jin, K. Thambiratnam, Q. Zhang, H. Dong, and H. Sun(2025)Huracan: a skillful end-to-end data-driven system for ensemble data assimilation and weather prediction.External Links:2508.18486,LinkCited by:§1.
- [18]E. M. Nordhagen, H. H. Haugen, A. F. S. Salihi, M. S. Ingstad, T. N. Nipen, I. A. Seierstad, I. Frogner, M. Clare, S. Lang, M. Chantry, P. Dueben, and J. Kristiansen(2025)High-resolution probabilistic data-driven weather modeling with a stretched-grid.External Links:2511.23043,LinkCited by:§1,§5.
- [19]L. Pacchiardi, R. A. Adewoyin, P. Dueben, and R. Dutta(2024)Probabilistic forecasting with generative networks via scoring rule minimization.Journal of Machine Learning Research25,pp. 1–64.Cited by:§1,§4.2,Graph Energy Score,Graph Energy Score.
- [20]W. A. Perkins, A. Kwa, J. McGibbon, T. Arcomano, S. K. Clark, O. Watt-Meyer, C. S. Bretherton, and L. M. Harris(2026)HiRO-ACE: fast and skillful AI emulation and downscaling trained on a 3 km global storm-resolving model.External Links:2512.18224,LinkCited by:§1.
- [21]R. Pic, C. Dombry, P. Naveau, and M. Taillardat(2025)Proper scoring rules for multivariate probabilistic forecasts based on aggregation and transformation.Advances in Statistical Climatology, Meteorology and Oceanography11(1),pp. 23–58.External Links:Document,LinkCited by:Graph Energy Score.
- [22]M. Scheuerer and T. M. Hamill(2015)Variogram-based proper scoring rules for probabilistic forecasts of multivariate quantities.Monthly Weather Review143(4),pp. 1321–1334.External Links:DocumentCited by:§4.2,Graph Variogram Score.
- [23]M. Schillinger, M. Samarin, X. Shen, R. Knutti, and N. Meinshausen(2025)EnScale: temporally-consistent multivariate generative downscaling via proper scoring rules.External Links:2509.26258,LinkCited by:§1.
- [24]P. Tillet, H. Kung, and D. D. Cox(2019)Triton: an intermediate language and compiler for tiled neural network computations.InProceedings of the 3rd ACM SIGPLAN International Workshop on Machine Learning and Programming Languages,pp. 10–19.External Links:DocumentCited by:§3.1.
- [25]M. Zhdanov, A. Lucic, M. Welling, and J. van de Meent(2026)(Sparse) Attention to the Details: preserving spectral fidelity in ML-based weather forecasting models.External Links:2604.16429,LinkCited by:§5.

## 


- 


Major funding support from
