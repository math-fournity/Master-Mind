# Forecasting threshold exceedance of atmospheric variables at a specific location

**arXiv ID**: 2605.31079v1
**Authors**: Roberta Baggio, Jean-François Muzy
**Published**: 2026-05-29
**Categories**: physics.ao-ph, physics.data-an, stat.ML
**Comments**: 24 pages, 8 Figures, 4 tables
**HTML URL**: https://arxiv.org/html/2605.31079v1

## Abstract

This study compares two methodological approaches for predicting, at a given site, threshold exceedances of atmospheric variables such as temperature and wind speed: (i) direct probabilistic methods, which treat exceedance as a binary classification problem, and (ii) full distribution probabilistic methods, which model the complete conditional probability law of the target variable. Using theoretical analysis and numerical simulations on a toy model, alongside real-world data from the MeteoNet dataset (2016--2018) for southeastern France, we demonstrate that the full distribution approach consistently outperforms the direct method for rare, extreme events. This advantage arises because the full distribution approach effectively learns the parameters of the conditional distribution from moderate and mild intensity events, thereby achieving better calibration and discrimination in the tails. We find that the specific parametric shape of the chosen distribution plays a secondary role compared to accurately capturing predictable shifts in its bulk properties (i.e., mean and variance). This empirical indistinguishability is also informative about the physical mechanics driving atmospheric extremes, suggesting that extreme exceedances are primarily driven by significant conditional displacements of the entire distribution rather than by unpredictable, fat-tailed anomalies within a static climatology. Our results are validated for both strong surface wind speeds and intense hourly rainfall, with performance evaluated using proper scoring rules (Brier score, logarithmic score) and deterministic skill scores (Peirce Skill Score, CSI, HSS). These findings highlight the critical importance of modeling the full probability distribution for rare-event forecasting and provide practical guidance for improving extreme weather prediction in operational meteorology.

## Full Text

Forecasting threshold exceedance of atmospheric variables at a specific location

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.31079v1 [physics.ao-ph] 29 May 2026\Author

[a][baggio_r@univ-corse.fr]RobertaBaggio\Author[a]Jean-FrançoisMuzy

a]Laboratoire Sciences Pour L’Environnement, UMR 6134, CNRS Université de Corse, Avenue du 9 Septembre, Corte, France\pubdiscuss\published

## Forecasting threshold exceedance of atmospheric variables at a specific location

## Abstract

Accurate short-term forecasting of extreme weather events is essential for early warning systems and disaster mitigation. This study compares two methodological approaches for predicting, at some given site, threshold exceedances of atmospheric variables such as temperature and wind speed: (i) direct probabilistic methods, which treat exceedance as a binary classification problem and (ii) full distribution probabilistic methods, which model the complete conditional probability law of the target variable. Using theoretical analysis and numerical simulations on a toy model, alongside real-world data from the MeteoNet dataset (2016–2018) for southeastern France, we demonstrate that the full distribution approach consistently outperforms the direct method for rare, extreme events.
This advantage arises because the full distribution approach can effectively learn the parameters of the conditional distribution even from moderate and mild intensity events, thus achieving better calibration and discrimination in the tails. We find that the specific parametric shape of the chosen distribution plays a secondary role compared to accurately capturing predictable shifts in its bulk properties (i.e., mean and variance). This suggests that extreme exceedances are primarily driven by significant conditional
displacements of the entire distribution, rather than by unpredictable, fat-tailed anomalies within a static climatology. Our results are validated for both strong surface wind speeds and intense hourly rainfall, with performance evaluated using proper scoring rules (Brier Score, logarithmic score) and deterministic skill scores (Peirce Skill Score, Critical Success Index, Heidke Skill Score).
These findings highlight the critical importance of modeling the full probability distribution for rare-event forecasting and provide practical guidance for improving extreme weather prediction in operational meteorology.\copyrightstatement

TEXT\introduction

The accurate and timely prediction of extreme weather events is an important and difficult problem in operational meteorology(Seneviratne et al.,2023). Driven by climate change, the frequency and intensity of localized, high-impact phenomena are clearly increasing, posing severe risks to public safety, civil infrastructure and the stability of renewable energy grids. Despite remarkable progress in numerical weather prediction (NWP)(Bauer et al.,2015), including convection-permitting systems such as AROME from Météo-France, specifically designed to improve predictions at regional scale(Seity et al.,2011), predicting the precise timing and magnitude of localized extremes at the site level remains very challenging. This difficulty mainly stems from the highly non-linear and chaotic nature of atmospheric dynamics(Lorenz,1963), compounded by the smoothing effects of grid-scale parameterizations, unresolved complex topography and sub-grid microphysical processes. Furthermore, for short-term forecasting purposes, the high computational cost of NWP models inherently limits their rapid-update capabilities. Consequently, at very short time scales, such as those required for nowcasting, prediction methods traditionally relied on statistical inference approaches that use historical data and past observed patterns to project future states. Early techniques range from the development of specific stochastic time-series models designed to account for observed localized fluctuations (see, e.g.,Baïle et al. (2011); Tascikaraoglu and Uzunoglu (2014); Kaur et al. (2023)) to optical flow methods for radar tracking(Beauchemin and Barron,1995; Ayzel et al.,2019). Building directly upon this foundation, modern machine learning (ML) leverages massive meteorological datasets to extract complex, nonlinear spatiotemporal patterns and enable hybrid approaches that combine in-situ observations with NWP outputs.
The field of short-term weather prediction has been significantly transformed by deep learning approaches.
For high-resolution prediction, architectures such as Deep Generative Models of Radar (DGMR) produce highly realistic probabilistic 90-minute rainfall forecasts(Ravuri et al.,2021), while attention-based models like MetNet and MetNet-2 deliver skillful, 1-km resolution predictions up to 12 hours ahead over continental domains(Sønderby et al.,2020; Espeholt et al.,2022). Concurrently, at the global scale, data-driven surrogates like GraphCast(Lam et al.,2023)and FourCastNet(Pathak et al.,2024)rapidly generate multi-day fields that can serve as boundary conditions for finer-scale models. A comprehensive review of these architectures falls beyond the scope of this paper and we refer to, e.g.,Schultz et al. (2021); Bouallègue et al. (2024)for further details.

The current work specifically focuses on the application of ML and hybrid approaches to threshold exceedance predictions. Indeed, for early warning systems, disaster management or sectoral planning, predicting severe weather events is often formulated as forecasting threshold exceedances such as temperatures surpassing30∘​C30^{\circ}\mathrm{C}, hourly rainfall exceeding3030mm, or wind speeds over9090km/h. In this study, we address the site-specific nowcasting of such exceedance events within a 0–6 h time window. Concretely, for a fixed location and atmospheric variable, our goal is to estimate the probability of exceedance in a form that can be rapidly updated and remains statistically well-calibrated(Bojinski et al.,2023). To achieve this task, existing methodologies can be split into two main categories. The first isdirect exceedance modeling, which treats the exceedance (or non-exceedance) of a specific threshold as a Bernoulli outcome. This approach learns directly the probabilityp∈[0,1]p\in[0,1]of such Bernoulli event, framing the task as a standard binary classification problem optimized via Binary Cross-Entropy (BCE). The second category comprisesfull-distribution(or distributional) approaches. Instead of directly predicting the binary outcome, these methods estimate the complete conditional probability law of the target variable. The exceedance probability can then be computed directly from the cumulative distribution function (CDF) associated with the forecasted distribution.

Direct probabilistic forecasting for binary events is a well-established practice in the nowcasting of extreme meteorological conditions(Glahn and Lowry,1972; Jolliffe,2004; Wilks,2009). This classification approach has been successfully applied to a wide variety of phenomena, including severe convective episodes(Pang et al.,2019), intense rainfall(Schaumann et al.,2021; Bouttier and Marchal,2024; Pujol et al.,2025), and pollution peaks(Dutot et al.,2007). To generate these probabilistic forecasts, operational systems employ distinct methodological pathways. The first relies entirely on numerical weather prediction (NWP) ensembles, estimating the probability of exceedance from the fraction of physical members that surpass a target threshold(Leutbecher and Palmer,2008). A second class of methods is purely data-driven, treating threshold exceedance as a standard binary classification problem. ML classifiers, such as random forests or deep neural networks optimized via Binary Cross-Entropy, excel in this space by learning exceedance probabilities directly from large, labeled datasets of historical observations, radar imagery, or reanalysis(McGovern et al.,2017; Lagerquist et al.,2017; Agrawal et al.,2019). A third pathway consists of hybrid techniques that synthesize these two paradigms by post-processing and calibrating NWP forecasts to improve local accuracy and reliability. This includes statistical approaches such as logistic regression(Hess,2020), as well as machine learning approaches such as neural networks combining NWP forecasts and observations(Pujol et al.,2025)or classifiers trained on NWP-derived predictors to directly estimate exceedance probabilities(McGovern et al.,2017).

Techniques designed to predict the full probability distribution provide a comprehensive characterization of predictive uncertainty and span a large range of statistical paradigms. Traditional parametric approaches, such as Ensemble Model Output Statistics and Generalized Additive Models for Location, Scale, and Shape, assume that the target atmospheric variable follows a pre-defined probability law(Gneiting et al.,2005; Schlosser et al.,2019). These models establish a mapping between atmospheric predictors and the distribution’s parameters, typically optimizing a proper scoring rule such as the logarithmic score or the Continuous Ranked Probability Score (CRPS)(Jolliffe,2004). In recent years, these parametric frameworks have been heavily augmented by deep learning(Salinas et al.,2020). The advent of "neural distributional regression" allows neural networks to non-linearly learn the predictor-to-parameter mapping, yielding significant improvements in forecast calibration and skill(Rasp and Lerch,2018; Baggio and Muzy,2024; Baggio et al.,2025). This concept has also been successfully extended to spatial domains through the use of gridded distributional U-Nets, particularly for the post-processing of precipitation fields(Pic et al.,2025).

Nonparametric and semiparametric alternatives, such as standard Quantile Regression Forests (QRF), circumvent rigid distributional assumptions for the bulk of the data by estimating conditional quantiles directly from the empirical distribution of decision tree leaves(Meinshausen and Ridgeway,2006; Taillardat et al.,2016; Park et al.,2022). However, standard QRF exhibits a critical limitation for tail events: it cannot extrapolate beyond the maximum values observed in the training set. This extrapolation barrier is a fundamental challenge shared across the broader spectrum of statistical and deep learning architectures. To surmount this limitation, many extreme weather nowcasting approaches integrate Extreme Value Theory (EVT)(Coles et al.,2001)directly into modeling(Friederichs and Thorarinsdottir,2012). This can typically be operationalized via thePeaks Over Threshold(POT) approach, which explicitly models excesses above a high threshold using the Generalized Pareto Distribution (GPD). While EVT-based methodologies are highly effective for calibrating early warnings of localized, severe events like flash floods, they introduce a notoriously difficult bias-variance trade-off: setting the POT threshold too low violates the asymptotic assumptions of the GPD, whereas setting it too high severely restricts the sample size available to robustly estimate the tail parameters(see, e.g., Bader et al.,2018)

The primary purpose of this paper is to systematically compare direct binary classification versus full-distribution parametric modeling for predicting the likelihood of extreme events. For both paradigms, this study relies upon a hybrid neural network architecture(Baggio et al.,2025; Pujol et al.,2025)that leverages high-resolution NWP predictions alongside local time-series observations at the target site and its surrounding stations. We aim to investigate the intuitive idea that when exceedances are rare, direct binary classification suffers from extreme class imbalance, a scarcity of positive samples and a high sensitivity to threshold definitions. By contrast, distributional models can leverage abundant "non-extreme" outcomes to learn conditional scale and shape parameters. This allows them to produce better-calibrated exceedance probabilities, provided that the chosen family of probability distributions appropriately captures the conditional bulk-tail dependence.
We first formalize this intuition within a simple theoretical framework, supported by both analytical and numerical evidence. We then validate these findings through two site-specific case studies: the exceedance of (i) strong near-surface winds and (ii) intense hourly rainfall in the Mediterranean region of southeastern France. For reproducibility and operational relevance, we useMeteoNet(2016–2018), an open Météo-France dataset aggregating co-registered ground-station and AROME/ARPEGE model outputs over two550×550550\times 550, km domains that encompass our study area(Larvor and Berthomier,2021). Our verification methods follow established best practices, utilizing the Brier Score, Logarithmic Score, reliability diagrams, and ROC/AUC for probabilistic evaluation, alongside the Peirce Skill Score, Critical Success Index, and Heidke Skill Score for the deterministic prediction of binary outcomes. Finally, we discuss potential misspecification issues related to the specific choice of the parametric distribution.

The paper is organized as follows. Section1introduces the forecasting problem, formalizing the definitions and describing the two modeling approaches, direct probabilistic classification and full-distribution probabilistic modeling, along with the verification metrics used for evaluation. Section2provides a theoretical framework and illustrative experiments using a simplified generative model to compare the asymptotic behavior of both methods for extreme quantiles. Section3applies these approaches to real-world data from the MeteoNet dataset, detailing the dataset’s characteristics, the neural network architecture used for predictions and presenting empirical results for wind speed and hourly cumulated rainfall forecasting. Section3.5.2concludes with a synthesis of the findings outlining questions for future research. Finally, the Appendix contains the technical material and detailed analytical computations notably for the toy model.

## 1Statement of the problem

## 1.1Extreme events as binary events

In this section, we set the main notations we use all along the paper and formally define the addressed problem.Y​(t)Y(t)will stand for the value at timettof some atmospheric variable (i.e.Y​(t)=V​(t)Y(t)=V(t)the wind speed,Y​(t)=T​(t)Y(t)=T(t)the temperature,Y​(t)=R​(t)Y(t)=R(t)the amount of precipitation during last hour, etc) at some given location.Y​(t)Y(t)is considered as a stationary stochastic process taking value inℝ\mathbb{R}.

At any timett, given a thresholdY0Y_{0}and a time horizonh>0h>0, our objective is to predict exceedance events ofY​(t+h)Y(t+h). We formalize such events using a binary indicator:It+h​(Y0)=ℋ​(Y​(t+h)−Y0)={1if​Y​(t+h)≥Y0,0otherwise,I_{t+h}(Y_{0})=\mathcal{H}\left(Y(t+h)-Y_{0}\right)=\begin{cases}1&\text{if }Y(t+h)\geq Y_{0},\\
0&\text{otherwise},\end{cases}(1)

whereℋ\mathcal{H}denotes the Heaviside step function. Predicting extreme events thus reduces to forecastingIt+h​(Y0)I_{t+h}(Y_{0})for largeY0Y_{0}values, particularly those corresponding to high percentiles of the site’s climatological distribution. For a probability level1−p1-p(withp≪1p\ll 1), we define the associated quantileQpQ_{p}as:FC​(Qp)=1−p,F_{C}(Q_{p})=1-p,(2)

whereFC​(z)=∫−∞zfC​(u)​𝑑uF_{C}(z)=\int_{-\infty}^{z}f_{C}(u)\,duis the cumulative distribution function (CDF) derived from the climatological probability density functionfC​(u)f_{C}(u). Whenp≪1p\ll 1,It+h​(Qp)I_{t+h}(Q_{p})indicates whetherY​(t+h)Y(t+h)exceeds a threshold chosen in the distribution’s upper tail. In the remainder of this paper, we drop the explicit threshold dependency and implicitly letIt+hI_{t+h}denoteIt+h​(Qp)I_{t+h}(Q_{p})unless stated otherwise.

The previous prediction task constitutes a binary classification problem where the target is:pt​=def​Prob​(It+h=1∣ℱt),p_{t}\underset{\mathrm{def}}{=}\mathrm{Prob}\left(I_{t+h}=1\mid\mathcal{F}_{t}\right),(3)

withℱt\mathcal{F}_{t}representing all information available at timett. Aprobabilistic prediction, namely an estimate ofptp_{t}, denoted asp^t{\widehat{p}}_{t}, can then be converted to adeterministic predictionby thresholding atp⋆p^{\star}:I^t+h={1if​p^t>p⋆.0otherwise,\widehat{I}_{t+h}=\begin{cases}1&\text{if }{\widehat{p}}_{t}>p^{\star}\;.\\
0&\text{otherwise},\end{cases}(4)

In the following sections, we introduce two distinct methodologies to estimate the conditional probabilityptp_{t}and review the probabilistic and deterministic verification metrics used to assess and compare the quality of these threshold exceedance forecasts.

## 1.2Modeling approaches

Our objective is to compare two distinct model classes for estimating the conditional exceedance probabilityptp_{t}defined in Equation (3). Both approaches utilize observable covariatesXtX_{t}as input features representing all available information at timett. However, they fundamentally differ in how they process the target variable during training.

## Classℳ1\mathcal{M}_{1}: Direct probability estimation

The first approach (ℳ1\mathcal{M}_{1}) treats the task strictly as a binary classification problem. A modelM1∈ℳ1M_{1}\in\mathcal{M}_{1}maps the covariates directly to the estimated exceedance probability:M1​(Xt;𝜽^)=p^t(1),M_{1}(X_{t};\widehat{{\boldsymbol{\theta}}})=\widehat{p}_{t}^{(1)},(5)

where𝜽^\widehat{{\boldsymbol{\theta}}}represents the learned model parameters.
This formulation corresponds to standard probabilistic classification, where parameters are typically optimized using the Binary Cross-Entropy (BCE) loss:ℒBCE=−1N​∑i=1N[Iti+h​ln⁡(p^ti(1))​(1−Iti+h)​ln⁡(1−p^ti(1))].\mathcal{L}_{\text{BCE}}=-\frac{1}{N}\sum_{i=1}^{N}\left[I_{t_{i}+h}\ln\left(\widehat{p}_{t_{i}}^{(1)}\right)\left(1-I_{t_{i}+h}\right)\ln\left(1-\widehat{p}_{t_{i}}^{(1)}\right)\right].(6)

The BCE loss is particularly suitable for this task as it directly optimizes for probability calibration.
However, it depends exclusively on the binary indicatorsIti+hI_{t_{i}+h}and consequently, during training, the model discards all continuous magnitude information of the underlying atmospheric variable, reacting only to whether the threshold was breached.

## Classℳ2\mathcal{M}_{2}: Distribution-based probability estimation

The second approach (ℳ2\mathcal{M}_{2}) adopts a two-stage procedure: (i) it estimates the full continuous conditional distribution ofY​(t+h)Y(t+h)givenXtX_{t}, and (ii) it derives the exceedance probability from this distribution. Following parametric deep learning frameworks(e.g., Salinas et al.,2020), the model outputs the time-dependent parametersΠt\Pi_{t}of a chosen parametric family at each time step:M2​(Xt;𝜽^)=Π^t.M_{2}\left(X_{t};\widehat{{\boldsymbol{\theta}}}\right)=\widehat{\Pi}_{t}.(7)

Letf​(y;Πt):=dd​y​Prob​(Y​(t+h)≤y∣ℱt)f(y;\Pi_{t}):=\frac{d}{dy}\text{Prob}\left(Y(t+h)\leq y\mid\mathcal{F}_{t}\right)denote the conditional probability density function (PDF) ofY​(t+h)Y(t+h). The optimal parameters𝜽^\widehat{{\boldsymbol{\theta}}}are learned by minimizing the negative log-likelihood over the continuous observations:ℒLL=−1N​∑k=1Nln⁡f​(Y​(tk+h);Π^tk).\mathcal{L}_{\text{LL}}=-\frac{1}{N}\sum_{k=1}^{N}\ln f\left(Y(t_{k}+h);\widehat{\Pi}_{t_{k}}\right).(8)

In contrast toℳ1\mathcal{M}_{1}, the training loss forℳ2\mathcal{M}_{2}utilizes the exact continuous values ofY​(t+h)Y(t+h), leveraging the entire dataset regardless of how extreme the threshold is. OnceΠ^t\widehat{\Pi}_{t}is inferred, the exceedance probability is computed analytically or numerically as the tail probability:p^t(2)=∫Qp∞f​(y;Π^t)​𝑑y.\widehat{p}_{t}^{(2)}=\int_{Q_{p}}^{\infty}f(y;\widehat{\Pi}_{t})\,dy.(9)

This approach implicitly accounts for the full predictive distribution rather than focusing solely on the probability threshold, potentially stabilizing predictions whenp→0p\to 0.

## 1.3Forecast verification of binary events

Evaluating threshold exceedance forecasts requires both deterministic metrics to assess binary decision-making and probabilistic scores to quantify calibration and resolution under heavy class imbalance(Jolliffe,2004; Wilks,2011).

## Deterministic predictions

Binary forecastsI^t​(Y0)\widehat{I}_{t}(Y_{0})are evaluated using standard metrics derived from the contingency table (TP, TN, FP, FN). We focus on three metrics suited to rare events (p≪1p\ll 1): the Peirce Skill Score (PSS), the Heidke Skill Score (HSS), and the Critical Success Index (CSI).

The PSS measures discrimination independently of class imbalance(Wilks,2011):PSS=HR−FA=TPTP+FN−FPTN+FP.\text{PSS}=\text{HR}-\text{FA}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}-\frac{\mathrm{FP}}{\mathrm{TN}+\mathrm{FP}}.(10)

Conversely, the HSS measures accuracy relative to chance and remains sensitive to the base rate(Jolliffe,2004):HSS=2​(TP⋅TN−FP⋅FN)(TP+FN)​(FN+TN)+(TP+FP)​(TN+FP).\text{HSS}=\frac{2(\mathrm{TP}\cdot\mathrm{TN}-\mathrm{FP}\cdot\mathrm{FN})}{(\mathrm{TP}+\mathrm{FN})(\mathrm{FN}+\mathrm{TN})+(\mathrm{TP}+\mathrm{FP})(\mathrm{TN}+\mathrm{FP})}.(11)

The CSI isolates event detection by omitting true negatives(Wilks,2011):CSI=TPTP+FP+FN.\text{CSI}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}+\mathrm{FN}}.(12)

Binary decisions are obtained by thresholding probabilities atp⋆p^{\star}. Optimal thresholds depend strictly on the target metric(Mason,1979; Jolliffe,2004); analytically,p⋆=pp^{\star}=pmaximizes the PSS, whereas optimal thresholds for the CSI and HSS depend on the score values themselves and are computed numerically (Section3). Further mathematical properties of these scores are detailed inJolliffe (2004)andWilks (2011).

## Probabilistic predictions

Probabilistic forecasts are assessed using proper scoring rules and discrimination metrics to verify calibration, resolution, and sharpness(Wilks,2011; Gneiting and Katzfuss,2014). The Brier Score (BS) measures the mean squared error of the probabilities:BS=1N​∑i=1N(p^ti−Iti+h)2.\text{BS}=\frac{1}{N}\sum_{i=1}^{N}\left(\widehat{p}_{t_{i}}-I_{t_{i}+h}\right)^{2}.(13)

The Brier Skill Score corresponds to the comparison top​(1−p)p(1-p), the expected BS obtained with “climatology” prediction:BSS=1−BSp​(1−p)=Res−RelU,\text{BSS}=1-\frac{\text{BS}}{p(1-p)}=\frac{\mathrm{Res}-\mathrm{Rel}}{U},(14)

whereRel\mathrm{Rel}andRes\mathrm{Res}denote the reliability and resolution components, andU=p​(1−p)U=p(1-p)represents the climatological uncertainty(see Murphy,1973; Jolliffe,2004; Wilks,2011, for full algebraic decompositions). We also consider the logarithmic score (LS), which corresponds to the negative log-likelihood and perfectly matches the binary cross-entropy loss function used during training:LS=−1N​∑i=1N[Iti+h​ln⁡p^ti+(1−Iti+h)​ln⁡(1−p^ti)].\text{LS}=-\frac{1}{N}\sum_{i=1}^{N}\left[I_{t_{i}+h}\ln\widehat{p}_{t_{i}}+(1-I_{t_{i}+h})\ln(1-\widehat{p}_{t_{i}})\right].(15)

Both BS and LS are strictly proper scoring rules(Gneiting et al.,2006). Here they are complemented by the Area Under the ROC Curve (AUC) to assess threshold-independent ranking performance under severe class imbalance(Jolliffe,2004).

## 2Theoretical analysis and numerical experiments with a toy generative model

This section examines a simplified theoretical framework where the observableY​(t+h)Y(t+h)is generated from a covariate vectorXtX_{t}through an underlying data-generating process.
Our objective is to analytically compare the estimation errors of the two approaches (ℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}) introduced previously, focusing on their relative performance in predicting rare extreme events.
Rather than aiming for a fully exhaustive and rigorous treatment, we provide analytical arguments that support the intuitive claim: for high thresholds where exceedances become increasingly rare, the distribution-based approach (ℳ2\mathcal{M}_{2}) demonstrates superior sample efficiency compared to direct probability estimation (ℳ1\mathcal{M}_{1}). This advantage stems from a critical distinction in information utilization: A modelM2∈ℳ2M_{2}\in\mathcal{M}_{2}leverages the complete continuous-valued observations, while modelM1∈ℳ1M_{1}\in\mathcal{M}_{1}effectively relies only on the sparse positive exceedance events, resulting in an effective sample size of approximatelyp​NpNwhereppis the exceedance probability.
Consequently, asp→0p\to 0(i.e., as events become increasingly rare), the performance advantage ofM2M_{2}overM1M_{1}is expected to widen.

We begin by introducing our simplified modeling framework and derive analytical comparisons ofM1M_{1}andM2M_{2}performance using three key metrics: the Brier Score (measuringL2L^{2}error), the relative logarithmic score and the Peirce Skill Score. These theoretical findings are then validated through numerical experiments using an explicit generative model, with implementations of both estimation strategies (ℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}).

## 2.1Estimation of the asymptotic errors for each model and their effects on performance scores.

We consider the following problem setup that is directly inspired from the simple example considered inLerch et al. (2017). Let(Xt)t∈𝒯(X_{t})_{t\in\mathcal{T}}be add-dimensional stationary random process of observable covariates. An unknown mappingF:ℝd→ℝF:\mathbb{R}^{d}\to\mathbb{R}generates a latent mean signal:μt=F​(Xt).\mu_{t}=F(X_{t})\;.(16)

By stationarity ofXtX_{t}, the processμt\mu_{t}is also stationary and we assume its marginal distribution is Gaussian with mean zero and variances2s^{2}. At timet+ht+h, we observe:Y​(t+h)=μt+νt+h,Y(t+h)=\mu_{t}+\nu_{t+h},(17)

whereνt\nu_{t}is a white noise process of varianceσ2\sigma^{2}that is also assumed to be Gaussian. In that respect, the law ofY​(t)Y(t)is Gaussian of varianceσY2=s2+σ2\sigma^{2}_{Y}=s^{2}+\sigma^{2}.
Throughout this paper, we will denote byϕ​(z)\phi(z)the standard normal density andΦ​(z)\Phi(z)the associated cumulative distribution function (CDF) andΦ−1​(q)\Phi^{-1}(q)the inverse cumulative distribution, namely, the reciprocal function ofΦ​(z)\Phi(z). IfZ=(Z1,…,Zn)Z=(Z_{1},\ldots,Z_{n})is a random vector of lawfZ​(z1,…,zn)f_{Z}(z_{1},\ldots,z_{n}), the expectation of any functionG​(z)=G​(z1,…,zn)G(z)=G(z_{1},\ldots,z_{n})with respect toZZ, is denoted as𝔼Z​[G​(z)]=∫𝑑z1​…​𝑑zn​G​(z1,…,zn)​fZ​(z1,…,zn)\mathbb{E}_{Z}\left[G(z)\right]=\int dz_{1}\ldots dz_{n}\;G(z_{1},\ldots,z_{n})\;f_{Z}(z_{1},\ldots,z_{n})(18)

For a fixed thresholdY0∈ℝY_{0}\in\mathbb{R}, the quantity of interest is the conditional exceedance probability:P​(Xt)​=def​pt=Φ​(μt−Qpσ).P(X_{t})\underset{\mathrm{def}}{=}p_{t}=\Phi\left(\frac{\mu_{t}-Q_{p}}{\sigma}\right)\;.(19)

where we noticed thatProb​(ν>z)=1−Prob​(ν≤z)=1−Φ​(zσ)=Φ​(−zσ)\mathrm{Prob}\left(\nu>z\right)=1-\mathrm{Prob}\left(\nu\leq z\right)=1-\Phi(\frac{z}{\sigma})=\Phi(-\frac{z}{\sigma}). We focus on small probability regime, namelyp≪1p\ll 1and we notice that for our model, the quantileQpQ_{p}reads:Qp=−s2+σ2⋅Φ−1​(p).Q_{p}=-\sqrt{s^{2}+\sigma^{2}}\cdot\Phi^{-1}(p).(20)

A key parameter of the model is the noise-to-signal ratio:ρ2=σ2s2,\rho^{2}=\frac{\sigma^{2}}{s^{2}},(21)

representing the relative magnitude of the idiosyncratic noise fluctuationsνt+h\nu_{t+h}inY​(t+h)Y(t+h)compared to its conditional mean signalμt\mu_{t}. Whenρ2\rho^{2}is small, the predictability ofIt+hI_{t+h}is high becauseptp_{t}varies between values close to eitherpt=0p_{t}=0orpt=1p_{t}=1whereas whenρ2→∞\rho^{2}\to\infty, the predictability is small sinceptp_{t}variation around its mean valueppare small.
In this context, it is natural to modelρ2\rho^{2}as an increasing function of the forecasting horizonhh, reflecting the fact that predictability inherently decreases over longer horizons. Consequently, when comparing model output to empirical results, a larger horizon must correspond to a higher effective value ofρ2\rho^{2}. Let us remark that, , with little algebra, one can easily compute the two first moments ofptp_{t}:𝔼Xt​[pt]=𝔼Xt​[Φ​(μt−Qpσ)]=p.\mathbb{E}_{X_{t}}[p_{t}]=\mathbb{E}_{X_{t}}\left[\Phi\left(\frac{\mu_{t}-Q_{p}}{\sigma}\right)\right]=p.(22)

and𝔼Xt​[pt2]=𝔼Xt​[Φ​(μt−Qpσ)2]=Φ2​(Φ−1​(p),Φ−1​(p);r)\mathbb{E}_{X_{t}}[p_{t}^{2}]=\mathbb{E}_{X_{t}}\left[\Phi\left(\frac{\mu_{t}-Q_{p}}{\sigma}\right)^{2}\right]=\Phi_{2}\left(\Phi^{-1}(p),\Phi^{-1}(p);r\right)(23)

wherer=11+ρ2r=\frac{1}{1+\rho^{2}}andΦ2​(x,y;r)\Phi_{2}(x,y;r)stands for the cumulative distribution function of the standard bivariate normal distribution with correlationrr.
Notice that, whenρ2→∞\rho^{2}\to\infty,r→0r\to 0. SinceΦ2​(q,q,0)=Φ2​(q)\Phi_{2}(q,q,0)=\Phi^{2}(q), we thus have, whenρ2→∞\rho^{2}\to\infty,Var​(pt)=𝔼​(pt2)−𝔼​(pt)2→p2−p2=0\mathrm{Var}(p_{t})={\mathbb{E}}(p_{t}^{2})-{\mathbb{E}}(p_{t})^{2}\to p^{2}-p^{2}=0. Indeed, as mentioned above, whenρ→∞\rho\to\infty,Y​(t)Y(t), is a pure, unpredictable, Gaussian white noise of varianceσ2\sigma^{2}and thereforeptp_{t}is constant,pt=pp_{t}=pindependently oftt. On the other hand, whenρ2→0\rho^{2}\to 0,r→1r\to 1and sinceΦ2​(q,q,1)=Φ​(q)\Phi_{2}(q,q,1)=\Phi(q),
one hasVar​(pt)=𝔼​(pt2)−𝔼​(pt)2→p−p2=p​(1−p)\mathrm{Var}(p_{t})={\mathbb{E}}(p_{t}^{2})-{\mathbb{E}}(p_{t})^{2}\to p-p^{2}=p(1-p)which is the variance of a Bernoulli process. This is simple to understand since, in that case,Y​(t+h)Y(t+h)reduces to its predictable componentμt\mu_{t}andptp_{t}becomes itself a Bernoulli process sincept=1p_{t}=1with probabilitypp(ifμt≥Qp\mu_{t}\geq Q_{p}) andpt=0p_{t}=0otherwise.

Our goal is to estimate the functionP​(⋅)P(\cdot)in Eq. (19) which mapsXtX_{t}to the conditional probabilityptp_{t}. This can be done using a modelM(.,𝜽)M(.,{\boldsymbol{\theta}}), which parameters are learned over a training set{[Xt,Y​(t+h)]}t=1N\{[X_{t},Y(t+h)]\}_{t=1}^{N}. We first consider a modelM1(.,𝜽)M_{1}(.,{\boldsymbol{\theta}})that, followingℳ1\mathcal{M}_{1}approach, directly outputs an estimatep^t(1)\widehat{p}_{t}^{(1)}ofptp_{t}. Its best parameters are obtained by minimizing the binary cross-entropy (BCE) loss associated with observed exceedancesIt+h​(Qp)I_{t+h}(Q_{p}). We also consider a modelM2(.,𝜽)M_{2}(.,{\boldsymbol{\theta}})in the classℳ2\mathcal{M}_{2}which provides an estimation ofμt\mu_{t}allowing
one to compute the conditional probability estimatep^t(2)\widehat{p}_{t}^{(2)}using Equation (19).M2M_{2}model’s parameters are obtained by maximizing the log-likelihood which reduces, asσ2\sigma^{2}is known, to the Mean Squared Error.

In AppendixA, we show that, within this framework, in the regimep≪1p\ll 1and when the number of observationsNNis large, under standard asymptotic regularity conditions(see, e.g., Vaart,1998), one has
the following estimation errors onpt(k)p^{(k)}_{t}of modelMkM_{k},k=1,2k=1,2:ℰ1=𝔼​[(p^t(1)−pt)2]​∼p→0​K1​(ρ)N​pρ22+ρ2​[ln⁡(1/p)]−12+ρ2,\displaystyle\mskip-18.0mu{\cal E}_{1}={\mathbb{E}}\left[({\widehat{p}}^{(1)}_{t}-p_{t})^{2}\right]\underset{p\to 0}{\sim}\frac{K_{1}(\rho)}{N}p^{\frac{\rho^{2}}{2+\rho^{2}}}\,\bigl[\ln(1/p)\bigr]^{-\frac{1}{2+\rho^{2}}},(24)ℰ2=𝔼​[(p^t(2)−pt)2]​∼p→0​K2​(ρ)N​p2+2​ρ22+ρ2​[ln⁡(1p)]1+ρ22+ρ2,\displaystyle\mskip-6.0mu{\cal E}_{2}={\mathbb{E}}\left[({\widehat{p}}^{(2)}_{t}-p_{t})^{2}\right]\underset{p\to 0}{\sim}\frac{K_{2}(\rho)}{N}\;p^{\frac{2+2\rho^{2}}{2+\rho^{2}}}\bigl[\ln(\frac{1}{p})\bigr]^{\frac{1+\rho^{2}}{2+\rho^{2}}},(25)

where the averages𝔼{\mathbb{E}}are defined over all learned model’s parameters (and over timett) and where the “noise-to-signal” ratioρ2\rho^{2}is defined in Eq. (21). This result first indicates that,
at fixedpp(small enough), as the noise-to-signal ratio increases, estimation error decreases.
This counterintuitive result can be explained by the fact that the intrinsic predictability of the conditional probabilityptp_{t}is limited by its variance, which can be computed from Eqs (22) and (23):Var​(pt)=𝔼​[pt2]−p2=Φ2​(Φ−1​(p),Φ−1​(p);r)−p2,\text{Var}(p_{t})=\mathbb{E}[p_{t}^{2}]-p^{2}=\Phi_{2}(\Phi^{-1}(p),\Phi^{-1}(p);r)-p^{2}\;,

We have seen that as the ratioρ2\rho^{2}increases, the latent correlationrrtends toward zero, physically implying that idiosyncratic noise dominates the systemic factorμt\mu_{t}. Mathematically, this causes the bivariate distributionΦ2\Phi_{2}to factorize into the product of marginalsp2p^{2}, drivingVar​(pt)\text{Var}(p_{t})to zero and effectively turningptp_{t}into a deterministic constantpp, which is trivially predictable with zero error.
From Eqs. (24) and (25) one can also see that, up to logarithmic corrections, we haveℰ2ℰ1=𝒪​(p)\frac{{\cal E}_{2}}{{\cal E}_{1}}=\mathcal{O}\left(p\right)

showing that, assuming that bothM1M_{1}andM2M_{2}estimation methods are efficient and parameter estimation are asymptotically normal (see AppendixA), in the regime of large thresholdQpQ_{p}(orp→0p\to 0), one expects an error with approachℳ2\mathcal{M}_{2}that is very small compared to the error using approachℳ1\mathcal{M}_{1}. This results originates from the fact that the effective amount of “information” used to calibrateM1M_{1}parameters isp​NpNinstead ofNNresulting in a factorppin the asymptotic variance ratio of the two approaches.

These findings are confirmed when measuring the estimation performance in terms of skill scores, namely with PSS for deterministic predictions and Brier or logarithmic scores for probabilistic predictions. In AppendicesBandC, we analyze the impact of parameter prediction errors on the performance as measured by BSS, LS and PSS for
modelsM1M_{1}andM2M_{2}.
We notably show that BSS behavior is directly related to the behavior of errorsℰ2\mathcal{E}_{2}andℰ1\mathcal{E}_{1}(see Eqs (59)).
Whenp≪1p\ll 1we have:B​S​Sk≈pρ​22+ρ2−ℰkp.BSS_{k}\approx p^{\frac{\rho 2}{2+\rho^{2}}}-\frac{\mathcal{E}_{k}}{p}\;.(26)

Since, whenp≪1p\ll 1,ℰ2≪ℰ1\mathcal{E}_{2}\ll\mathcal{E}_{1}, this confirms that, in this regime, methodM2M_{2}provides better results than methodM1M_{1}sinceB​S​S2>B​S​S1BSS_{2}>BSS_{1}.

We can also compare the two methods in terms of LS. We demonstrate in AppendixBthat LS difference reads whenp↓0p\downarrow 0:Δ​LS1,2​=def​LS1−LS2​∼p→0​Cρ2​N​(Kρ−p​ln⁡(p−1))\Delta\mathrm{LS}_{1,2}\underset{\text{def}}{=}\mathrm{LS}_{1}-\mathrm{LS}_{2}\underset{p\to 0}{\sim}\frac{C_{\rho}}{2N}\left(K_{\rho}-p\ln\left(p^{-1}\right)\right)(27)

whereCρC_{\rho}andKρK_{\rho}are two positive constants defined in AppendixB. We see that, providedp≪1p\ll 1,Δ​LS1,2\Delta\mathrm{LS}_{1,2}is clearly positive meaning thatM2M_{2}approach outperformsM1M_{1}.

For PSS, we establish in Eqs. (66) and (67) of AppendixCexplicit expressions in terms ofptp_{t}-averaged values for methodsM1M_{1}andM2M_{2}. Such integrals that can be evaluated numerically. In the regimeN→∞N\to\infty, we obtains the the following asymptotic behavior forp→0p\to 0:PSS1\displaystyle\text{PSS}_{1}∼\displaystyle\sim1−Kρ​pκ2−C1N​p−γ\displaystyle 1-K_{\rho}p^{\kappa^{2}}-\frac{C_{1}}{N}p^{-\gamma}(28)PSS2\displaystyle\text{PSS}_{2}∼\displaystyle\sim1−Kρ​pκ2−C2N​p1−γ\displaystyle 1-K_{\rho}p^{\kappa^{2}}-\frac{C_{2}}{N}p^{1-\gamma}(29)

whereγ=2​ρ1+ρ2+ρ∈(0,1)​and​κ=1+ρ2−ρ\gamma=\frac{2\rho}{\sqrt{1+\rho^{2}}+\rho}\in(0,1)\;\;\text{and}\;\;\kappa=\sqrt{1+\rho^{2}}-\rho

andKρK_{\rho}is a constant depending onρ\rhosuch that1−Kρ​pκ2→11-K_{\rho}p^{\kappa^{2}}\to 1whenρ→0\rho\to 0and1−Kρ​pκ2→01-K_{\rho}p^{\kappa^{2}}\to 0whenρ→∞\rho\to\infty. It results, as expected, that the maximum expected PSS cannot be positive in pure noise regime while can approach a maximum score (PSS=1=1) in the perfectly predictable situation.
According to Eq. (29), one expects the PSS to increase asp→0p\to 0. This can be intuitively explained by the fact that, asp→0p\to 0, the thresholdQpQ_{p}becomes very large and the eventsIt+h=1I_{t+h}=1become "more predictable" since the idiosyncratic component plays a diminishing role. Indeed, exceedance for large thresholds can occur only whenμt\mu_{t}is very large and thus whenY​(t+h)Y(t+h)is less dependent onνt+h\nu_{t+h}in definition (17). Sinceμt\mu_{t}represents the predictable part of the process, the predictability ofIt+h=1I_{t+h}=1naturally improves in the smallppregime. In contrast, this behavior is not observed forPSS1\text{PSS}_{1}in Eq. (28). Although the intrinsic predictability ofIt+h=1I_{t+h}=1increases asp→0p\to 0, this benefit is entirely canceled by the estimation error of methodM1M_{1}. Indeed, as the probability approaches zero, the effective number of positive casesp​NpNdrops, causing the variance of the estimator to explode and dominate the signal.

ForNNlarge enough, the PSS ratio is therefore expected to behave as:PSS1PSS2∼1−KpN+𝒪​(1N2)​with​Kp∼K​p−γ​(1−C​p).\frac{\text{PSS}_{1}}{\text{PSS}_{2}}\sim 1-\frac{K_{p}}{N}+\mathcal{O}(\frac{1}{N^{2}})\;\mathrm{with}\;K_{p}\sim Kp^{-\gamma}(1-Cp)\;.

We thus recover that fact theM2M_{2}has a better PSS thanM1M_{1}but both methods lead to the same PSS value asN→∞N\to\infty. We can also see that, at fixedNN, the PSS ratio decreases asppbecomes smaller,
so that the smallerpp, the betterM2M_{2}is with respect toM1M_{1}.

## 2.2Numerical validation using a toy generative model

To empirically validate our analytical findings and provide illustrative examples, we implement the simple model described in AppendixD. Specifically, according to Eq. (75), the latent processμt\mu_{t}(Equation (16)) is constructed as a weighted sum of harmonic functions applied to the components of add-dimensional Gaussian white noise inputXtX_{t}.
The so-obtained processμt\mu_{t}is zero mean, approximately normal and the weights chosen such that its variance iss2s^{2}.

Both estimation modelsM1​(Xt,𝜽)M_{1}(X_{t},{{\boldsymbol{\theta}}})andM2​(Xt,𝜽)M_{2}(X_{t},{{\boldsymbol{\theta}}})employ identical multi-layer perceptron (MLP) architectures, each with 3 layers featuring:
- -

Input dimension matching thedd-dimensional covariatesXtX_{t}
- -

Two hidden layers with 32 ReLU-activated units
- -

Linear output layers representing logits forM1M_{1}and regression forM2M_{2}

Theℳ1\mathcal{M}_{1}-type modelM1M_{1}directly estimates exceedance probabilitiesProb​(Y​(t+h)>Y0∣Xt)\mathrm{Prob}(Y(t+h)>Y_{0}\mid X_{t})using binary cross-entropy with logits loss to optimize𝜽{\boldsymbol{\theta}}, while theℳ2\mathcal{M}_{2}-type modelM2M_{2}predicts the latent processμt\mu_{t}by minimizing the mean squared error (MSE) between predicted and observedY​(t+h)Y(t+h)values.
Both models are trained using the Adam optimizer with a batch size of212=40962^{12}=4096, learning rate of10−310^{-3}and early stopping based on validation loss with a patience of 20 epochs. The validation set comprises a separate 10% split of the original training data.

Our experimental setup usesd=12d=12input dimensions with training and test sets containingN=215N=2^{15}andN′=214N^{\prime}=2^{14}samples respectively.
All simulations, model training and predictions were implemented in Python using the PyTorch framework, ensuring efficient GPU acceleration and reproducible results. To robustly evaluate estimation errors, we employ a kind of cross-validation with Monte-Carlo resampling approach: While keeping the set of test pairs(Y​(t+h),Xt)(Y(t+h),X_{t})constant, we train both models on 30 independent realizations of the training set. This methodology provides stable estimates of model performance (notably their bias and variance) while accounting for the inherent variability in training process.Figure 1:Comparison of the mean squared error of theM1M_{1}andM2M_{2}model predictions. Empirical estimates ofℰ1\mathcal{E}_{1}defined in Eq. (48) (■\blacksquare) in panel (a)) andℰ2\mathcal{E}_{2}(symbols (∙\bullet) in panel (b)) defined in Eq. (39) are displayed as a function ofppforρ2=1\rho^{2}=1(dark blue) andρ2=10\rho^{2}=10(green). Dashed and continuous lines represent the analytical expressions expected from respectively Eqs. (51) and (41) (see text for details on numerical experiments).

Figure1presents empirical estimates of the prediction errors for modelsM1M_{1}andM2M_{2}across different exceedance probabilitiespp. Panel (a) displaysℰ1\mathcal{E}_{1}(squares,■\blacksquare), as defined in Equation (48), while panel (b) showsℰ2\mathcal{E}_{2}(circles,∙\bullet), defined in Equation (39). The results cover a range of threshold probabilities fromp=10−3p=10^{-3}top=3×10−1p=3\times 10^{-1}, corresponding to rare events. In accordance with our theoretical framework, these empirical estimates focus exclusively on the variance components of the prediction errors. We have verified that squared bias terms are negligible in the regime we consider, thereby validating the variance-dominated error assumption in AppendixAfor the considered range of exceedance probabilities.
We also consider two different noise-to-signal ratio,ρ2=1\rho^{2}=1andρ2=10\rho^{2}=10while keeping the variance ofY​(t+h)Y(t+h),σY2=s2+σ2=2\sigma_{Y}^{2}=s^{2}+\sigma^{2}=2fixed.Figure 2:Comparison of Brier Skill Score (BSS) and Peirce Skill Score (PSS) for modelsM1∈ℳ1M_{1}\in\mathcal{M}_{1}(symbols (■\blacksquare) and dashed lines) andM2∈ℳ2M_{2}\in\mathcal{M}_{2}(symbols (∙\bullet) and solid lines). Dark violet represent data forρ2=1\rho^{2}=1and while green represent data forρ2=10\rho^{2}=10. Panel (a) shows empirically estimated BSS (Eq. (14)) a function of exceedance probabilitypp. Panel (b) presents analogous PSS results and panel (c) illustrates the PSS performance ratiosPSS1/PSS2\mathrm{PSS}_{1}/\mathrm{PSS}_{2}againstpp. Dashed and solid lines in all panels show theoretical predictions from AppendicesBfor BSS (Eq. (59)) andCfor PSS (Eqs. (66) and (67)).

As anticipated by the discussion after Eqs. (24) and (25),
we clearly see that as the noise-to-signal ratio increases the variance ofp^{\widehat{p}}decreases, reflecting
the fact that asρ2\rho^{2}increasesptp_{t}becomes more and more predictable (it converges to the climatology valueppwhenρ2→∞\rho^{2}\to\infty) and therefore the prediction error decreases. The dashed curves in panel (a) and solid curves in panel (b) represent our analytical predictions derived from Equations (51) and (41) respectively. To achieve optimal alignment between theory and empirical results, we calibrated the constant terms in these analytical expressions. It is noteworthy that, for theℰ1\mathcal{E}_{1}case whenρ2=1\rho^{2}=1, incorporating a quadratic correction termV1′​(μ)=V1′+V1′′​μ2V_{1}^{\prime}(\mu)=V_{1}^{\prime}+V_{1}^{\prime\prime}\mu^{2}in Equation (51) provides marginally better agreement than a simple constant adjustment.
The results demonstrate excellent concordance between the estimated data and our analytical expressions, thereby providing empirical validation for theoretical hypotheses of AppendixA.

Figure2compares the performance of modelsM1M_{1}andM2M_{2}using the Brier Skill Score (Equation (14)) and Peirce Skill Score (Equation (10)). Panel (a) shows that, despite the superior predictability ofptp_{t}highlighted in Figure1, the BSS falls asρ2\rho^{2}increases. This behavior stems from the degraded predictability ofItI_{t}, captured by the first term in Equation (26). Indeed, the conditional probability distribution ofptp_{t}is sharper for small noise-to-signal ratio:ptp_{t}is more often closer topt=1p_{t}=1orpt=0p_{t}=0whenρ2\rho^{2}is small than whenρ2\rho^{2}is large (in the limitρ→0\rho\to 0,ptp_{t}is either0or11and its conditional distribution is infinitely sharp).
It also reveals that relative performance improves with increasingpp, despite the increase in absolute error observed in Figure1.
This indicates that model performance relative to climatology deteriorates for rarer events.
For moderatepp, this behavior is mainly due to the termpρ22+ρ2p^{\frac{\rho^{2}}{2+\rho^{2}}}in Eq. (26) that does not depend on the the prediction method (see also Eq. (59) for a more precise behavior). At smallerpp, the contribution of−ℰ2-\mathcal{E}_{2}is negligible for methodM2M_{2}while, sinceℰ1p∼p−22+ρ2\frac{\mathcal{E}_{1}}{p}\sim p^{-\frac{2}{2+\rho^{2}}}, its contribution toB​S​S1BSS_{1}becomes strongly negative.
In Figure2(b), we see that very much like BSS, PSS decreases with the noise-to-signal ratioρ2\rho^{2}. Again, this stems from a better quality ofItI_{t}prediction for smallerρ2\rho^{2}. The figure further demonstrates that as the exceedance probabilityppdecreases, predictions from modelM2M_{2}become increasingly accurate, as evidenced by the monotonic increase inPSS2\mathrm{PSS}_{2}. This trend confirms our theoretical analysis presented in Section2.1following Equations (28) and (29). A similar pattern is observed for modelM1M_{1}, though only for moderateppvalues. For very smallppvalues,PSS1\text{PSS}_{1}reaches a maximum and then declines, in full consistency with our theoretical predictions.
In Figure2(c) which examines the relative PSS ofM1M_{1}andM2M_{2}, one also clearly sees that methodM2M_{2}has larger PSS than methodM1M_{1}and this is all the more true whenppis small. This confirms that the two methods perform comparably for common events (largestppvalues),M2M_{2}progressively outperformsM1M_{1}asp→0p\to 0. This observed advantage ofM2M_{2}for rare events aligns with our theoretical analysis in Section2.1, thereby providing empirical validation of our analytical predictions regarding the superior sample efficiency of the distribution-based approach for extreme event prediction.
Finally, we can notice that in all cases, the analytical curves derived in AppendicesB(Eq. (59) for BSS) andC(Eqs. (66) and (67)) for PSS) provide a quite fair fit to the empirical data.

## 3Application to rainfall and wind speed data

In this section, the problem introduced previously is examined in the context of forecasting the extreme occurrences of surface wind speed and hourly cumulated rainfall, respectively. First, the meteorological data used for this purpose are presented. The forecasting task, in its specific formulation, is then described in detail. This is followed by a description of the the structure of the input data, of the ANN architecture employed, and the main characteristics of the training procedure.

## 3.1The MeteoNet datasetFigure 3:Geographical extent of the MeteoNet Southeast database, with the localization of the 278 ground stations (∙\bullet)

The meteorological data used in this study were sourced from MeteoNet(Larvor and Berthomier,2021), a comprehensive dataset curated and made publicly available by Météo-France to support researchers and data scientists. The dataset covers two regions, south-eastern and north-western France, for the three year period 2016–2018. It includes various type of observations measures and NWP forecasts gridded data. Following what done in previous work(Baggio et al.,2025), we focus on south-eastern France and use a subset of the available data, that is, only NWP forecasts and ground-station observations are considered in this study. The retained weather variables for each of the data type considered, which have been selected differently for wind speed and accumulated rainfall, are reported in Table1. Although the original ground-station observations are available at 6-min resolution, we aggregate them to hourly time series to limit the number of model parameters, as detailed in Subsection3.3.1. Concerning NWP forecasts, we consider two type of data: 2-D surface fields from the high-resolution AROME model (0.025°) and 3-D fields from the lower-resolution ARPEGE model (0.1°). For each day, the 24-h forecasts come from the 00 UTC run; AROME fields are provided hourly, while ARPEGE fields are available at 1-h or 3-h intervals depending on the lead time.

Starting from the raw dataset files, a two-step post-processing procedure is applied to prepare the model inputs. First, data is organized on a per-station basis by creating one file per selected ground station. Each file stores, in NetCDF format, the station’s hourly time series together with those of neighboring sites, and includes a local subgrid of the 2-D and 3-D NWP fields centered on the station, retaining all available forecast times. During this first stage the integrity of data is preserved and no quality check is applied. Then, in a second phase, these station-based files are processed to form model-ready inputs. Samples containing invalid or missing data are discarded. To ensure statistical significance, for every station file it is checked that available keys are above a given threshold and discarded otherwise. When considering the weather variables reported on Table1and by using a threshold of 2000 and 500 for wind and rainfall respectively, 278 and 268 station are retained among the ones available in the original dataset (see Figure3). Features tensors in valid samples of feature-label pairs are normalized before storing, then these samples are exported in an unified format compatible with Pytorch data generators, either as a large binary file or in-memory arrays.Table 1:Summary of the MeteoNet input data used for model training.Input typeSpace and time gridsWind speed targetCumulative rainfall targetStationsSpatial grid: 11 locations(station + 10 neighbours)Time grid: current + 6 past hourly valuesWind componentsuu,vv(m s-1)Temperature (K)Wind componentsuu,vv(m s-1)Temperature (K)Relative humidity (%)Precipitation (mm h-1)AROMESpatial grid:11×1111\times 11Time grid: all 6 h-ahead predictions2 m temperature (K)2 m relative humidity (%)Wind componentsuu,vv(m s-1)MSLP (Pa)Same as wind-speed target,plus 2 m dew-point temperature (K)and total precipitation (mm)ARPEGESpatial grid:7×5×57\times 5\times 5Time grid: all 6 h-ahead predictionsTemperature (K)Wind componentsuu,vv(m s-1)Pressure (Pa)Same as wind-speed target,plus vertical velocity (Pa s-1)

## 3.2Statement of the forecasting problem for wind and cumulative rainfall

Building on the discussion in Section1.1, we now adapt the framework to our specific case study. Returning to the forecasting problem introduced in Equation (1), we focus on threshold exceedance forecasts for a weather variableY​(t)Y(t)across multiple forecast horizonsh=(h1,h2,…,hH)\textbf{h}=(h_{1},h_{2},\ldots,h_{H}). At a given initial timettand recording siteSS, the objective is to predict the vector of future exceedancesId,t+h\textbf{ I}_{d,t+\textbf{ h}}that is, theHH-dimensional vectorId,t+h=(Id,t+h1Id,t+h2⋮Id,t+hH),\textbf{ I}_{d,t+\textbf{ h}}=\begin{pmatrix}I_{d,t+h_{1}}\\
I_{d,t+h_{2}}\\
\vdots\\
I_{d,t+h_{H}}\end{pmatrix},(30)

representing threshold exceedances at siteSSover multiple future lead times. Following(Baggio et al.,2025), we setH=6H=6with an hourly frequency, so thatId,t+h\textbf{I}_{d,t+\textbf{h}}contains six components corresponding to exceedance predictions from 1 up to 6 hours ahead. Prediction vectorI^d,t+h\widehat{\textbf{I}}_{d,t+\textbf{h}}is obtained by minimizing the losses defined in Eqs. (6) and (8) for methodsM1M_{1}andM2M_{2}, respectively. Notice that for each method, the loss function is extended to multiple horizons by summing overh=1,…,6h=1,\ldots,6. This formulation implicitly treats the different forecast horizons as conditionally independent, an assumption adopted for tractability. Assessing and potentially relaxing this independence assumption constitutes a direction for future research.

For the two weather variables we consider, namely hourly wind speed (m/s) and 1-hour accumulated rainfall (mm), thresholdsQpQ_{p}are calculatedstation-wise, that is, the climatological densities are station-specific:fC​(y)=fCS​(y)f_{C}(y)=f_{C}^{S}(y). The quantile selection is done differently for wind speed and for cumulative rainfall. For wind speed, we simply define everyQpQ_{p}using Equation (2). Then results are computed for a list of 8 probabilitiespp, namely more specifically we usepW∈{0.2,0.1,0.08,0.05,0.03,0.01,0.005,0.002}.p_{W}\in\left\{0.2,0.1,0.08,0.05,0.03,0.01,0.005,0.002\right\}\,.(31)

In the case of rainfall, a different definition is adopted in order to ensure that the detected extreme quantiles remain meaningful despite the large number of dry days. LetFC,+SF_{C,+}^{S}denote the station-wise climatological CDF conditional on rainfall occurrenceFC,+S​(y)=P​(Y≤y​∣Y>​0)F_{C,+}^{S}(y)=P(Y\leq y\mid Y>0). The quantilesQpQ_{p}are defined with respect to this conditional distribution, i.e.FC,+S​(Qp)=p+,RF_{C,+}^{S}(Q_{p})=p_{+,R}, wherep+,Rp_{+,R}is such that:p+,R∈{0.5,0.4,0.3,0.25,0.2,0.15,0.1,0.05,0.025}.p_{+,R}\in\left\{0.5,0.4,0.3,0.25,0.2,0.15,0.1,0.05,0.025\right\}\,.(32)

When displaying results, metrics are plotted as a function of the normalizedpp, recovered asp=p¯w​e​t​p+,Rp=\bar{p}_{wet}\,p_{+,R}, wherep¯w​e​t=P​(X>0)\bar{p}_{wet}=P(X>0)is the probability of a rainy episode occurrence. This baseline probability is defined as the average probability of rainfall across all considered stations, yieldingp¯w​e​t≈0.08\bar{p}_{wet}\approx 0.08for the present dataset. Since the rainfall occurrence probability is station-dependent, this formulation introduces a small approximation. However, it allows for a more consistent comparison of the results with theory, as the resulting unconditional probability levelsppare substantially smaller than the corresponding conditional levelsp+,Rp_{+,R}.

## 3.2.1Probabilistic models for surface wind speed and rainfalls

When using a probabilistic model of typeℳ2\mathcal{M}_{2}, different parametric forms for the implied conditional density functionf​(y)f(y)are adopted to model wind speed and accumulated rainfall. It is worth emphasizing that, although these distributions have been selected with care, the differences among alternative parametric families remain limited once fundamental physical constraints of the target variable are properly enforced, as discussed later in Subsection3.5.2.

## Wind speed

For wind speed, we adopt the so-calledMultifractal-Rice(M-Rice) distribution, following previous work inBaggio and Muzy (2024), where it was shown to outperform classical alternatives such as the Weibull and Gamma distributions in forecasting applications. The M-Rice distribution, introduced inBaïle et al. (2011), is motivated by the random cascade framework used to describe fully developed turbulence. It generalizes the classical Rice distribution by allowing its scale parameter to be random, typically modeled as a log-normal variable, thereby incorporating intermittency effects. The resulting distribution is characterized by three parameters(ν,σ2,λ2)(\nu,\sigma^{2},\lambda^{2}). The parameterν\nucontrols the mean level,σ2\sigma^{2}governs dispersion, andλ2\lambda^{2}, often referred to as theintermittency parameter, regulates the tail behavior. In particular, larger values ofλ2\lambda^{2}produce heavier tails, increasing the probability assigned to extreme wind speeds.
The formal definition of the M-Rice distribution, together with a detailed interpretation of its parameters and numerical implementation, is provided in AppendixE.1.

## Accumulated rainfall

For hourly rainfall accumulation, we adopt a mixed lognormal (zero-inflated) distribution in order to account for the mixed discrete-continuous nature of precipitation.
Rainfall data are characterized by a substantial probability mass at zero (dry events), together with a positively skewed continuous distribution for positive amounts.
The mixed lognormal model explicitly captures this structure by combining a point mass at zero with a lognormal distribution for strictly positive values(Cho et al.,2004; Kedem et al.,1990).
Formally, the distribution is governed by three parameters: the probability of rainfall occurrencepw​e​tp_{wet}and the lognormal parameters(μ,σ2)(\mu,\sigma^{2})controlling the mean and dispersion of positive rainfall amounts.
The mathematical formulation of such “zero-inflated” lognormal distribution is provided in AppendixE.2. In addition to the mixed lognormal, other mixed distributions have been tested, without substantial differences in the model results. These distributions are also defined in the AppendixE.2.

## 3.3Hybrid neural network for predicting cumulative precipitation or surface wind speed

In this subsection, the artificial neural network (ANN) used to forecast weather variables is presented. The overall architecture follows that proposed in a previous study(Baggio et al.,2025)and was re-implemented from scratch within the PyTorch framework. The data and the preprocessing steps required to prepare the model input are first described. Subsequently, the network architecture and the training procedure are briefly discussed.

## 3.3.1Input design

The heterogeneous data sources described above are combined into a feature tensor used as input to the ANN, with each data type processed by a dedicated branch (see Subsection3.3.2). More specifically, a feature-label couple(Xk,Yk)(\textbf{{X}}_{\texttt{k}},\textbf{{Y}}_{\texttt{k}})is defined for eachkeyk=(S,d,t)\texttt{k}=(S,d,t)enconding stationSS, daydd, and timett. More specifically,(Xk,Yk)(\textbf{{X}}_{k},\textbf{{Y}}_{\texttt{k}})denotes the input tensor containing all the variables used for training whileYk\textbf{{Y}}_{\texttt{k}}contains the target variables, consisting of the six future values (one for each forecast hour) of either wind speed or accumulated rainfall. The inputXk\textbf{{X}}_{k}is defined asXk=[GSk,ARk,APk,Ck,Dk],\textbf{{X}}_{\texttt{k}}=\Big[\textbf{{GS}}_{\texttt{k}},\textbf{{AR}}_{\texttt{k}},\textbf{{AP}}_{\texttt{k}},\textbf{{C}}_{\texttt{k}},\textbf{{D}}_{\texttt{k}}\Big],whereGSk\textbf{{GS}}_{\texttt{k}},ARk\textbf{{AR}}_{\texttt{k}}, andAPk\textbf{{AP}}_{\texttt{k}}respectively denote features from ground stations, AROME, and ARPEGE, whileCk\textbf{{C}}_{\texttt{k}}andDS\textbf{{D}}_{S}encode temporal and spatial metadata. The ground station tensorGSk\textbf{{GS}}_{\texttt{k}}includes observations at the target siteSSand its 10 nearest neighboring stations. FornSn_{S}variables, this yields vectors of dimension11​nS11\,n_{S}(33 for wind, 55 for rainfall; see Table1). Using the current time and the six preceding hourly time steps, the resulting tensor has dimensions(7×33)(7\times 33)for wind and(7×55)(7\times 55)for rainfall. The AROME tensorARk\textbf{{AR}}_{\texttt{k}}is constructed from a local spatial patch of11×1111\times 11grid points centered on the station, corresponding to a spatial extent of±0.125∘\pm 0.125^{\circ}. Forecasts at horizonst+1t+1tot+6t+6are included, leading to tensors of shape(6×nA​R×11×11)(6\times n_{AR}\times 11\times 11), withnA​R=5n_{AR}=5for wind and77for rainfall. The ARPEGE tensorAPk\textbf{{AP}}_{\texttt{k}}is defined similarly, using a larger spatial extent (±0.2∘\pm 0.2^{\circ}) but a coarser grid (5×55\times 5). Forecast horizons are matched to the closest available times (multiples of 3 hours when needed). The selected variables (nA​P=5n_{AP}=5) are extracted at 7 vertical levels, yielding tensors of shape(6×4×7×5×5)(6\times 4\times 7\times 5\times 5)for wind and(6×5×7×5×5)(6\times 5\times 7\times 5\times 5)for rainfall. Temporal features inCk\textbf{{C}}_{\texttt{k}}include cyclic encodings of hour and day
along with station metadata (latitude, longitude, altitude) as explained inBaggio et al. (2025). The vectorDk\textbf{{D}}_{\texttt{k}}encodes the relative positions of the ten neighboring stations.

## 3.3.2Neural network model architecture

The proposed ANN architecture follows the design introduced inBaggio et al. (2025), with minor adaptations. Each subtensor ofXd,tS\textbf{{X}}^{S}_{d,t}is processed by a dedicated branch tailored to its structure. Station-level time seriesGSd,ts\textbf{{GS}}_{d,t}^{s}are modeled through stacked LSTM layers to capture temporal dependencies, while the spatiotemporal tensorsARd,ts\textbf{{AR}}_{d,t}^{s}andAPd,ts\textbf{{AP}}_{d,t}^{s}are first processed by convolutional layers to extract spatial features and subsequently passed to LSTM layers to encode their temporal evolution.
In all branches, encoding of contextual features by fully connected layers are concatenated to the predictors prior to the recurrent layers. These context representations are produced by shallow fully connected networks (ContextEncoder) consisting of two layers of sizene​n​c=16n_{enc}=16. The hidden dimension of all LSTM layers is controlled by parameteruL​S​T​Mu_{LSTM}, set touL​S​T​M=64u_{LSTM}=64.
Convolutional layers use kernel size 2 and stride equal to 1 (2D branch) or 2 (3D branch), without padding. For full architectural details we refer toBaggio et al. (2025). The outputs of the three branches are concatenated and passed through an additional dense block before the final prediction layers. For the classification modelM1{M}_{1}, a sigmoid activation is applied to the final layer to produce occurrence probabilities. As predictions are issued simultaneously for six lead times, the output lies inℝ6\mathbb{R}^{6}. For the probabilistic modelM2{M}_{2}, the dense representation is mapped to three distributional parameters via separate linear layers with suitable activation functions to enforce parameter constraints. Since each of the six lead times is associated with three parameters, the output lies inℝ6×3\mathbb{R}^{6\times 3}.

## 3.3.3Dataset split

Time-series dataset splitting requires balancing sample independence with representative seasonal coverage to prevent data leakage from autocorrelated samples, while ensuring subsets share similar probability distributions(Schultz et al.,2021). Given our limited three-year data span (2016–2018), we adopted a balanced approach: all forecasting tasks and labels corresponding to the same calendar day, which exhibit the strongest autocorrelation, were strictly assigned to the same subset. This same-day constraint, combined with a data cutoff at 17:00 UTC, provides a natural temporal separation between consecutive days that mitigates leakage while preserving seasonal variability. To implement this, the complete pool of potential calendar days was randomly partitioned into training (85%85\%), validation (10%10\%), and test (5%5\%) subsets, which were then intersected with the effectively available data. As reported in Table1, the final dataset comprises approximately4.1×1064.1\times 10^{6}total keysk, distributed as3.5×1063.5\times 10^{6}keys for training,4×1054\times 10^{5}keys for validation, and2×1052\times 10^{5}keys for testing.

## 3.3.4Hyperparameter selection and model training

The network presented above contains a total of around2.7×1052.7\times 10^{5}trainable parameters, which is relatively small by modern standards. The model was trained using the Adam optimizer. To mitigate potential overfitting, we adopted an early stopping strategy based on the validation loss (with a patience parameter of1010for wind speed,2020for cumulative rainfalls). The remaining hyperparameters were selected based on prior experience and are reported in Table2.Table 2:training hyperparameters used in the ANN.Training hyperparametersLearning rate0.001LSTM dropout level0.02Batch size (training)512Early stopping patience20 (wind), 15 (rainfalls)

With this setup, model training takes about 3 to 4 minutes for epoch on a single Nvidia Tesla V100 GPU. Considering that the very first epoch takes approximately twice this time due to initialization overhead and that models takes between 11 to 25 epochs to converge, training takes less than 2 hours long. It is important to emphasize a fundamental difference between the two approaches: whileM2M_{2}, which models the full predictive distribution, relies on a single model for all considered thresholds (Eqs. (31)–(32)), strategyM1{M}_{1}, based on binary classification, requires training a separate model for each threshold. After training, inference from the ANN is very fast, so that forecasts can be issued in a matter of seconds (seeBaggio et al. (2025)for details). Since we did not perform an extensive optimization of the hyperparameter space, the model parameters were kept fixed at standard baseline values, leading to highly consistent results between the validation and test splits. Accordingly, the scores presented in Subsection3.4are computed over both datasets simultaneously. This choice is motivated by our primary interest in the structural behavior of the curves asp→0p\to 0, rather than in the absolute metric values themselves. In practice, evaluating solely on the test set produces noisier estimates because of its smaller sample size, while the relative ranking of the models remains unchanged across both subsets.

## 3.4Applicaton results

In this Section we discuss the results obtained with the two modeling strategiesℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}and discuss the reported evaluation metrics in light of the model introduced earlier. All the presented deterministic metrics and scores have been evaluated by using their own optimal thresholdp⋆p^{\star}. This is known a priori forPSS, while forHSSandCSIit was obtained by evaluating a regularly spaced set of possible thresholds using a dedicated automated procedure. We report results for two forecast horizons,h=1h=1andh=6h=6; intermediate horizons exhibit similar behaviour and tend to fall between these two cases. As expected, forecast skill progressively degrades as the lead time increases. This is consistent with our hypothesis in Section2presenting the noise-to-signal ratioρ\rhoas an increasing function of forecast horizon. For the sake of clarity, all plots are showcased using a logarithmic scale onpp.

## 3.4.1Hourly wind speed

In Figure4values ofBSS,PSSand thePSSratio are shown. In line with what observed for the toy generative model, metrics associated with modelM2{M}_{2}are consistently better than the ones obtained with the classification approachM1{M}_{1}. Moreover, the overall trend ofBSSandPSSforp→0p\to 0reflects what shown in Figure2.Figure 4:BSS(panel (a)PSS(panel (b)) and its ratioPSS1/PSS2\mathrm{PSS}_{1}/\mathrm{PSS}_{2}(panel (c)) forhourly wind speedforecasts are shown for the two modelsM1{M}_{1}(symbols (■\blacksquare) and dashed lines) andM2{M}_{2}(symbols (∙\bullet) and solid lines). Two different forecast horizons are highlighted:h=1h=1h (in violet) andh=6h=6h (green).

In particularPSS2\text{PSS}_{2}increases steadily with decreasingpp, whilePSS1\text{PSS}_{1}, though behaving similarly for intermediate values ofpp, sharply deteriorates whenp→0p\to 0(Figure4(c)). This behaviour is reflected in the trend displayed by ratioPSS1/PSS2\text{PSS}_{1}/\text{PSS}_{2}, whose value is near to11for intermediate values ofppbut decreases asp→0p\to 0, thus reflecting what predicted by the model curve (Figure2(c)). This means that modelM2{M}_{2}maintains substantially higher discrimination ability in the rare-event regime, whereasM1{M}_{1}exhibits a marked degradation. Similar behaviour is observed at all forecast horizons, though skill degrades with increasinghh.
The trend of Brier Skill ScoreBSSwith decreasingppis in agreement with the model behaviour and shows a faster degradation ofBSS1\text{BSS}_{1}with respect toBSS2\text{BSS}_{2}(Figures4(a) and2(a)). Moreover, when considering theBSSdecomposition (14) (not shown) we observed that modelM2{M}_{2}performs better both in terms of reliability and resolution. Despite the superiority ofM2{M}_{2}, both models present good levels of calibration, as the termR​e​lU\frac{Rel}{U}, even if increasing rapidly withp→0p\to 0, remains relatively well controlled. This is likely due to the use of proper scoring rules during training (binary cross-entropy forM1{M}_{1}and negative log-likelihood forM2{M}_{2}).Figure 5:CSI (panel (a)) and HSS (panel (b)) relative tohourly wind speedforecasts are displayed for modelsM1{M}_{1}(symbols (■\blacksquare) and dashed lines) andM2{M}_{2}(symbols (∙\bullet) and solid lines). Two different forecast horizons are highlighted:h=1h=1h (in violet) andh=6h=6h (green).Figure 6:BSS(panel (a))PSS(panel (b) and ratioPSS1/PSS2\mathrm{PSS}_{1}/\mathrm{PSS}_{2}(panel (c)) forhourly accumulated rainfallare shown for the two modelsM1{M}_{1}(symbols (

■\blacksquare) and dashed lines) andM2{M}_{2}(symbols (∙\bullet) and solid lines). Two different forecast horizons are highlighted:h=1h=1h (in violet) andh=6h=6h (green).Table 3:AUC and LS scores forhourly wind speedforecasts at lead timesh=1h=1and6​h6\,\mathrm{h}, and probabilitiesp=0.05p=0.05and0.0050.005.ModelppAUCLS1​h1\,\mathrm{h}6​h6\,\mathrm{h}1​h1\,\mathrm{h}6​h6\,\mathrm{h}ℳ1\mathcal{M}_{1}0.050.9580.9340.0950.1290.0050.9630.9550.0190.024ℳ2\mathcal{M}_{2}0.050.9650.9430.0850.1110.0050.9820.9690.0100.014

For completeness, we also report the values of the CSI (Eq. (12)) and HSS (Eq. (11)), which confirm that the probabilistic modelM2{M}_{2}outperformsM1{M}_{1}in all considered cases, (Figure5). The evolution of CSI and HSS with respect toppis shown to provide an overall view of their behaviour. However, these metrics are not suitable for objective comparison across different base rates, as changes in event frequency affect the attainable range of these scores independently of the intrinsic discrimination ability of the model. Finally values of the AUC and LS (Eq. (15)) are reported in Table3forp=0.05,0.005p=0.05,\,0.005(mind that values of the logarithmic score are directly comparable only for equal values ofpp). It is possible to notice than for all the metrics considered, modelM2{M}_{2}performs better thanM1{M}_{1}and that this relative advantage tends to become more pronounced for decreasing values ofpp.

## 3.4.2Hourly accumulated rainfall

The analysis presented in the case of hourly wind speed is now extended to accumulated rainfall.

The behaviour ofBSS,PSSand ratioPSS1/PSS2\mathrm{PSS}_{1}/\mathrm{PSS}_{2}withp→0p\to 0are displayed in Figure6.
Looking at thePSS, showcased in6(b), it is possible to note that whilePSS1\text{PSS}_{1}always decreases asp→0p\to 0,PSS2\text{PSS}_{2}remains almost constant. This differs from what observed in the case of wind (Figure4(b)), but is somewhat expected since the considered values ofppspan a smaller range nearp→0p\to 0where the increasing trend ofPSS2\text{PSS}_{2}suggested by the theoretical model becomes less pronounced.The ratioPSS1/PSS2\mathrm{PSS}_{1}/\mathrm{PSS}_{2}(panel (c) in Figure6) confirms thatPSS1\text{PSS}_{1}is always worse thanPSS2\text{PSS}_{2}. Moreover, as suggested by the model and already observed for wind, this gap becomes and more pronounced with decreasingpp.
The overall decreasing behaviour observed for theBSScurves (panel (a) in Figure6) resembles what already seen for wind speed and is in line with model predictions of Section2. That is, the probabilistic modelM2{M}_{2}consistently outperforms the classification approachM1{M}_{1}. Results are in line with what described for wind even in terms of the reliability and resolution component, which we do not show, as modelM2{M}_{2}exhibits superior performance at a givenpp.Figure 7:CSI (panel (a)) and HSS (panel (b)) relative tohourly accumulated rainfallforecasts are displayed for the two modelsM1{M}_{1}(symbols (■\blacksquare) and dashed lines) andM2{M}_{2}(symbols (∙\bullet) and solid lines). Two different forecast horizons are highlighted:h=1h=1h (in violet) andh=6h=6h (green).Table 4:AUC and LS forhourly accumulated rainfallforecasts at lead timesh=1h=1and6​h6\,\mathrm{h}, and probabilitiesp≈0.04p\approx 0.04and0.0040.004.ModelppAUCLS1​h1\,\mathrm{h}6​h6\,\mathrm{h}1​h1\,\mathrm{h}6​h6\,\mathrm{h}ℳ1\mathcal{M}_{1}0.040.9710.9340.0750.1040.0040.9540.8720.0250.031ℳ2\mathcal{M}_{2}0.040.9750.9420.0690.0930.0040.9720.9410.0180.019Figure 8:BSS(panel (a)), andPSS(panel (b)) forhourly accumulated rainfallare shown for different choices of the parametric distribution in modelℳ2\mathcal{M}_{2}. All the three displayed families are mixed distributions of type (78) with three parameters. More specifically, a mixed lognormal (79) (symbols (■\blacksquare) and solid lines ), a mixed inverse Gaussian (80) (∙\bullet) and dashed lines) and a mixed Weibull distribution (81) (▲\blacktriangle) and dotted lines) have been tested. Two different forecast horizons are highlighted:h=1h=1h (in violet) andh=6h=6h (green).

CSI and HSS are displayed in Figure7. It is possible to remark that, at a given probability levelpp,M2{M}_{2}is always better thanM1{M}_{1}, consistently and for all considered thresholds. Moreover the results reported in Table4, consisting in the values of AUC and LS for two forecasting horizons and two probability levels, also support superiority ofM2{M}_{2}overM1{M}_{1}.
Finally, since one can legitimately question the effect of the distribution choice on the presented results for modelM2{M}_{2}, different mixed distributions have been tested. More specifically, the sensitivity ofM2{M}_{2}’s performance to the choice of parametric family has been investigated by replacing the mixed lognormal distribution with two alternative three-parameter families, namely the mixed inverse Gaussian (Eq. (80)) and mixed Weibull (Eq. (81)) distributions (see AppendixE.2for more details). The results, shown in Figure8, indicate that the choice of parametric family does not impact significantly the results, even if the Weibull distribution appears somewhat less suitable.

## 3.5Discussion

## 3.5.1Comparative performance of wind and accumulated rainfall predictions

For both wind speed and hourly cumulative rainfall, the empirical results are broadly consistent with the theoretical model. However, rainfall forecasting appears intrinsically more challenging, yielding systematically lower classification and probabilistic scores. This suggests a higher level of intrinsic noise in the rainfall dataset for the chosen predictors and problem formulation. Consistently, rainfall validation performance saturates after only a few training epochs before deteriorating, indicating rapid exhaustion of the generalizable signal followed by overfitting to non-transferable variability. The dominant role of intrinsic noise is also clearly reflected in the forecast-horizon dependence. In the model of Section2, the noise-to-signal ratioρ\rhoacts as a proxy for the forecasting horizon. We observe that ‘effective”ρ\rhois increasing much more strongly for rainfall than for wind speed. Specifically, for rainfall, the transition fromh=1h=1toh=6h=6roughly corresponds to a jump fromρ=1\rho=1toρ=10\rho=10in the theoretical model, whereas for wind speed the observed difference betweenh=1h=1andh=6h=6is less pronounced than in the numerical experiments reported in Figure2. Notably, for rainfall, the degradation of BSS asp→0p\to 0is slower forh=6h=6than forh=1h=1, which closely agrees with the theoretical model (Figures6(a) and2(a)), an effect not observed for wind. Likewise, the decline of PSS with increasinghhis more pronounced for accumulated rainfall.

## 3.5.2On the choice of the parametric distribution within theℳ2\mathcal{M}_{2}approach

In forecasting extreme weather events, selecting a parametric familyℱ\mathcal{F}(e.g., Weibull) over𝒢\mathcal{G}(e.g., Gamma) presents a fundamental statistical challenge. Because underlying meteorological conditions continuously evolve, we only ever observe a single outcome for any specific atmospheric state. Identifying the "true" data-generating distribution is therefore an ill-posed problem; the actual conditional probability at a given time step is an inaccessible abstraction that can neither be directly observed nor asymptotically approached. Without access to this ground truth, the only operational proxy for reality is the aggregated evaluation of proper scoring rules such as the Negative Log-Likelihood or the Continuous Ranked Probability Score (CRPS), averaged over a heterogeneous test set. Consequently, model selection is characterized by empirical indistinguishability rather than a unique best-fit model.This structural equivalence allows some freedom in parametric family selection that can be based on theoretically desirable properties (like e.g. the range of the target variable or a spectific tail behavior compatible with the unconditional law) without sacrificing empirical accuracy in the bulk of the data. For sample sizes typical of climatological records, distinct parametric families can yield comparable results. In the context of surface wind speeds, for instance,Baggio and Muzy (2024)demonstrated that various predictive distributions (M-Rice, Weibull, and Gamma) display nearly indistinguishable probabilistic and deterministic scores when applied to meteorological series from the Netherlands and Corsica. Similarly, in our evaluation of intense hourly rainfall, Fig.8shows that three distinct statistical laws (Log-Normal, Inverse Gaussian, and Weibull) produce comparable performances across all standard scoring metrics. This empirical indistinguishability also provides valuable insight into the physical mechanics driving atmospheric extremes. Their predictability typically stems from large, resolved shifts in the "bulk" (the conditional mean and variance) of the distribution, rather than from atypical fluctuations drawn from the tail of a static climatology. When the dominant predictive signal is a massive displacement of the core probability mass, the specific parametric shape of the tail becomes a secondary factor. This dominance of bulk-shifting mechanisms naturally explains why the Peirce Skill Score (PSS) increases with the threshold, a structural behavior perfectly in line with our empirical observations for both intense rainfall and strong wind speeds.\conclusions

In this study, we systematically compared two distinct paradigms for short-term probabilistic forecasting of atmospheric threshold exceedances at some location: direct binary classification, which frames exceedance as a Bernoulli outcome and full-distribution modeling, which estimates the conditional probability law of the target variable. On the theoretical ground, we considered a generative toy model inspired by the simple Gaussian model proposed inLerch et al. (2017). By leveraging standard asymptotic theory, we derived analytical expressions for key evaluation metrics, including the Brier Score and the Peirce Skill Score, as functions of the extreme quantile probability levelpp. Our analysis, supported by both theoretical derivations and numerical simulations, reveals a striking contrast in behavior asp→0p\to 0: for the full-distribution approach, predictive skill, as measured by the PSS, is mathematically expected to improve. This is reminiscent of the fact that extreme events are driven by large excursions in the predictable component of the process. Conversely, the direct binary classification approach exhibits a maximum performance before inevitably declining as the threshold becomes more extreme, a limitation arising from the scarcity of positive examples in the training data for very high quantiles.
These theoretically derived asymptotic behaviors were explicitly corroborated by our empirical validation using the MeteoNet dataset for southeastern France. The fundamental advantage of the full-distribution approach lies in its ability to mitigate the severe class imbalance that degrades the efficacy of direct binary classifiers in the deep tails. By modeling the complete conditional distribution, the framework successfully leverages abundant moderate and non-extreme observations to effectively learn the underlying scale and shape parameters. As validated on strong surface wind speeds and intense hourly rainfall, this approach translates to significantly sharper discrimination and better calibration for rare events.

While full-distribution modeling offers a robust framework for extreme weather prediction, several complex challenges remain for future research in statistical learning. One major issue is parametric misspecification and the accurate modeling of heavy tails. As illustrated by former results for wind speed and the specific examples we considered for hourly rainfalls and as also discussed in section3.5.2, it appears that different choices of the probability distribution class provide comparable results. The success of distributional models intrinsically does not relies so much on the suitability of the chosen parametric family. Instead, our findings indicate that predictive skill for extreme exceedances is primarily derived from accurately capturing large, predictable shifts in the bulk properties of the conditional distribution. Because these extreme occurrences are dominantly driven by strong displacements of the core probability mass rather than by atypical, unpredictable anomalies drawn from a “static” climatological tail, the precise parametric shape of the predictive tail does not play a primary role. This question will be considered with more details in a future work where we will notably explore the need for a dynamic integration of Extreme Value Theory into deep distributional frameworks. Another interesting prospect concerns the current site-specific modeling framework that could be extended to continuous spatial domains. Utilizing advanced architectures like distributional U-Nets or Graph Neural Networks could allow for the joint modeling of spatial dependencies and multivariate extremes, yielding physically coherent, high-resolution probabilistic fields rather than isolated point forecasts.
Finally, while hybrid deep learning and distributional architectures significantly improve predictive skill, operational forecasters require interpretable outputs to confidently issue life-saving warnings. Adapting explainable artificial intelligence methods for distributional regression outputs is an appealing next step. Understanding exactly which atmospheric covariates drive structural shifts in the predicted tail behavior will foster greater trust and facilitate the integration of these advanced statistical learning models into operational decision-making pipelines.\codedataavailabilityThe meteorological data used in this study originate from the MeteoNet database(Larvor and Berthomier,2021), originally developed by Météo-France. The reference version of the dataset utilized in this work is hosted on the Harvard Dataverse and can be accessed athttps://doi.org/10.7910/DVN/NCKRZ2. The complete Python source code for data preprocessing, model implementation, and analysis scripts, along with a minimal self-contained example dataset and an interactive Jupyter Notebook illustrating all aspects of code usage (including data preparation, model training and visualization), is publicly available under the MIT License on Zenodo athttps://doi.org/10.5281/zenodo.20327672(Muzy and Baggio,2026).\authorcontributionRoberta Baggio contributed to code development, experiment design, model execution, result analysis and manuscript writing. Jean-François Muzy contributed to the theoretical analysis, model setup, experiment design, code set up and development and manuscript writing.\competinginterestsThe author declare that they have no competing interests.\financialsupportBoth authors were supported in their research by the ANR research grant SAPHIR (ANR-21-CE04-0014).

## Appendix AComputation of prediction error in asymptotic regime

Let us estimate the prediction error associated with each prediction method when the number of observationsNNis large enough and we assume standard asymptotic regularity conditions(see, e.g., Vaart,1998).

Let𝜽{\boldsymbol{\theta}}denote the vector of model parameters
(e.g., the collection of weights and biases in a neural network).
For a given inputXtX_{t}, the model output is written asz^​(Xt;𝜽)∈ℝd.\widehat{z}(X_{t};{\boldsymbol{\theta}})\in\mathbb{R}^{d}.This means that we havez^=p^\widehat{z}=\widehat{p}forM1M_{1}andz^=μ^\widehat{z}=\widehat{\mu}for modelM2M_{2}.
Letℓ​(Y,X;𝜽)\ell(Y,X;{\boldsymbol{\theta}})denote theper-sample loss function(e.g.[Y−μ^​(Z,𝜽)]2[Y-\widehat{\mu}(Z,{\boldsymbol{\theta}})]^{2}in the case of Gaussian log-likelihood or MSE) from which the
(population) loss is computed as empirically as:ℒ​(𝜽)N=1N​∑t=1Nℓ​(Yt,Xt;𝜽).\mathcal{L}({\boldsymbol{\theta}})_{N}=\frac{1}{N}\sum_{t=1}^{N}\ell(Y_{t},X_{t};{\boldsymbol{\theta}})\;.

We assume that there exists a unique (pseudo-)true parameter value𝜽0=arg⁡min𝜽⁡𝔼​(ℒN​(𝜽)){\boldsymbol{\theta}}_{0}=\arg\min_{\boldsymbol{\theta}}{\mathbb{E}}\left(\mathcal{L}_{N}({\boldsymbol{\theta}})\right),
such that,z^​(Xt;𝜽0)\widehat{z}(X_{t};{\boldsymbol{\theta}}_{0})recovers the “true,” i.e. data-generating, functionz0​(Xt)z_{0}(X_{t})(namelyμ​(Xt)\mu(X_{t})orP​(Xt)P(X_{t})according to the model one considers). Even this assumption is unrealistic in practical situation (notably when misspecification induces at non-zero bias) it is an helpful framework to compare approachesM1M_{1}andM2M_{2}.
We suppose that standard regularity conditions are met and the
the estimator𝜽^\widehat{{\boldsymbol{\theta}}}minimizingℒN​(𝜽){\mathcal{L}}_{N}({\boldsymbol{\theta}})satisfies the usual asymptotic
normality propertyN​(𝜽^−𝜽0)→𝑑𝒩​(0,I𝜽​(𝜽0)−1),\sqrt{N}\,\big(\widehat{{\boldsymbol{\theta}}}-{\boldsymbol{\theta}}_{0}\big)\;\xrightarrow{d}\;\mathcal{N}\!\big(0,\,I_{{\boldsymbol{\theta}}}({\boldsymbol{\theta}}_{0})^{-1}\big),(33)

whereI𝜽​(𝜽0)=𝔼​[−∇𝜽2ℓ​(Y,X;𝜽0)]I_{{\boldsymbol{\theta}}}({\boldsymbol{\theta}}_{0})=\mathbb{E}\big[-\nabla_{{\boldsymbol{\theta}}}^{2}\ell(Y,X;{\boldsymbol{\theta}}_{0})\big]is the Fisher information matrix. Applying the Delta method to the smooth mappingz^​(X;𝜽)\widehat{z}(X;{\boldsymbol{\theta}})then yields, for each fixed inputXX,N​(z^​(X)−z0​(X))→𝑑𝒩​(0,G​(X)⊤​I𝜽​(𝜽0)−1​G​(X)),\sqrt{N}\,\big(\widehat{z}(X)-z_{0}(X)\big)\;\xrightarrow{d}\;\mathcal{N}\!\Big(0,\,G(X)^{\top}\,I_{\boldsymbol{\theta}}({\boldsymbol{\theta}}_{0})^{-1}\,G(X)\Big),(34)

whereG​(X)=∇𝜽z^​(X;𝜽0)G(X)=\nabla_{{\boldsymbol{\theta}}}\;\widehat{z}(X;{\boldsymbol{\theta}}_{0})is the Jacobian of the model output with respect to the parameters,
evaluated at𝜽0{\boldsymbol{\theta}}_{0}.
Under these conditions, we can estimate the error associated with each method.

## A.1ModelM2M_{2}inℳ2\mathcal{M}_{2}class

Let us start with modelM2∈ℳ2M_{2}\in\mathcal{M}_{2}and let us writez^​(Xt,𝜽)=μ^​(Xt)=M2​(Xt;𝜽)\widehat{z}(X_{t},{\boldsymbol{\theta}})={\hat{\mu}}(X_{t})=M_{2}(X_{t};{\boldsymbol{\theta}})whereM2​(Z;𝜽)M_{2}(Z;{\boldsymbol{\theta}}), is defined in Eq. (7) and represents the non-linear function of parameter vector𝜽{\boldsymbol{\theta}}used to inferμ^t{\widehat{\mu}}_{t}(the single varying parameter of the Gaussian law) for an observed covariateXtX_{t}. Since the loss function is the Gaussian log-likelihood, the Fisher information matrix simply reads:I𝜽​(𝜽0)=1σ2​J𝜽0I_{\boldsymbol{\theta}}({\boldsymbol{\theta}}_{0})=\frac{1}{\sigma^{2}}J_{{\boldsymbol{\theta}}_{0}}

whereσ2\sigma^{2}is the conditional variance of observations (the variance of the noise termνt\nu_{t}in Eq. (17)) andJ𝜽0=𝔼Xt(∇𝜽M2(Xt,𝜽)|𝜽=𝜽0.∇𝜽M2(Xt,𝜽)⊤|𝜽=𝜽0).J_{{\boldsymbol{\theta}}_{0}}={\mathbb{E}}_{X_{t}}\left(\left.\nabla_{{\boldsymbol{\theta}}}M_{2}(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}.\left.\nabla_{{\boldsymbol{\theta}}}M_{2}(X_{t},{\boldsymbol{\theta}})^{\top}\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\right)\;.(35)

It follows, from Eq. (34), thatV2​(Xt)V_{2}(X_{t}), the asymptotic variance ofμ^​(Xt)=M2​(Xt,𝜽0)\widehat{\mu}(X_{t})=M_{2}(X_{t},{\boldsymbol{\theta}}_{0}), is simply:V2​(Xt)=σ2N​V2′​(Xt)V_{2}(X_{t})=\frac{\sigma^{2}}{N}V^{\prime}_{2}(X_{t})(36)

where we have definedV2′​(Xt)=∇𝜽M2​(Xt,𝜽)⊤|𝜽=𝜽0​J𝜽0−1​∇𝜽M2​(Xt,𝜽)|𝜽=𝜽0.V^{\prime}_{2}(X_{t})=\left.\nabla_{{\boldsymbol{\theta}}}M_{2}(X_{t},{\boldsymbol{\theta}})^{\top}\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\left.J_{{\boldsymbol{\theta}}_{0}}^{-1}\nabla_{{\boldsymbol{\theta}}}M_{2}(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\;.(37)

Let us use again the Delta method for estimating the asymptotic variance ofp^(2)​(Xt)=Φ​(μ^​(Xt)−Qpσ){\widehat{p}}^{(2)}(X_{t})=\Phi(\frac{\widehat{\mu}(X_{t})-Q_{p}}{\sigma}). SinceΦ′​(z)=ϕ​(z)\Phi^{\prime}(z)=\phi(z), we haveVar​(p^(2)​(Xt))≈V2′​(Xt)N​ϕ2​(Qp−μ​(Xt)σ)\mathrm{Var}\!\left({\widehat{p}}^{(2)}(X_{t})\right)\approx\frac{V^{\prime}_{2}(X_{t})}{N}\phi^{2}\left(\frac{Q_{p}-\mu(X_{t})}{\sigma}\right)(38)

It results that the unconditional error onp^(2)​(Xt){\widehat{p}}^{(2)}(X_{t})corresponds to:ℰ2=1N​𝔼Xt​[V2′​(Xt)​ϕ2​(Qp−μ​(Xt)σ)].{\cal E}_{2}=\frac{1}{N}{\mathbb{E}}_{X_{t}}\left[V^{\prime}_{2}(X_{t})\;\phi^{2}\left(\frac{Q_{p}-\mu(X_{t})}{\sigma}\right)\right]\;.(39)

If one denotesV2′​(μt)=𝔼Xt​(V2′​(Xt)|μ​(Xt)=μt)V_{2}^{\prime}(\mu_{t})={\mathbb{E}}_{X_{t}}(V^{\prime}_{2}(X_{t})|\mu(X_{t})=\mu_{t}), previous equation can be rewritten asℰ2=1N​𝔼μt​[V2′​(μt)​ϕ2​(Qp−μtσ)]{\cal E}_{2}=\frac{1}{N}{\mathbb{E}}_{\mu_{t}}\left[V_{2}^{\prime}(\mu_{t})\;\phi^{2}\left(\frac{Q_{p}-\mu_{t}}{\sigma}\right)\right]. Sinceμt\mu_{t}is supposed to be Gaussian random variable of zero mean and variances2s^{2},
considering the definition ofQpQ_{p}provided in Eq. (20), we obtain:ℰ2=1N​(2​π)3/2​∫V2′​(u)​e−u22​e−(−1+ρ2​Φ−1​(p)−u)2ρ2​𝑑u{\cal E}_{2}=\frac{1}{N(2\pi)^{3/2}}\int V_{2}^{\prime}(u)e^{-\frac{u^{2}}{2}}e^{-\frac{\left(-\sqrt{1+\rho^{2}}\Phi^{-1}(p)-u\right)^{2}}{\rho^{2}}}\;du(40)

whereρ2\rho^{2}is the "noise-to-signal" ratio defined in (21).

If one wants a closed-form expression ofℰ2{\cal E}_{2}, one needs to know the functionV2′​(μ)V^{\prime}_{2}(\mu).
The gaussian integral (40) can be exactly computed for a wide variety of
shapesV2′​(μ)V^{\prime}_{2}(\mu), e.g. polynomial, exponential, etc.
The simplest expression is obtained when one neglects correlations and
one assumes that𝔼​(V2′​(μ))≈V2{\mathbb{E}}(V_{2}^{\prime}(\mu))\approx V_{2}.
In that caseℰ2{\cal E}_{2}reads:ℰ2=V2​ρ2​π​N​2+ρ2​exp⁡(−1+ρ22+ρ2​[Φ−1​(p)]2){\cal E}_{2}=\frac{V_{2}\rho}{2\pi N\sqrt{2+\rho^{2}}}\exp\left(-\frac{1+\rho^{2}}{2+\rho^{2}}\left[\Phi^{-1}(p)\right]^{2}\right)(41)

Since, asp↓0.p\downarrow 0.,e−[Φ−1​(p)]2∼4​π​p2​ln⁡(1/p)e^{-[\Phi^{-1}(p)]^{2}}\;\sim\;4\pi p^{2}\ln(1/p),
one has finally:ℰ2​≈p→0​K2​(ρ)N​p2+2​ρ22+ρ2​[ln⁡(1p)]1+ρ22+ρ2,{\cal E}_{2}\underset{p\to 0}{\approx}\frac{K_{2}(\rho)}{N}\;p^{\frac{2+2\rho^{2}}{2+\rho^{2}}}\bigl[\ln(\frac{1}{p})\bigr]^{\frac{1+\rho^{2}}{2+\rho^{2}}}\;,(42)

whereK2​(ρ)K_{2}(\rho)is a constant that depends onρ\rho.
We notably see that, up to logarithmic corrections:ℰ2​∼p→0​{ρ​pN​if​ρ≪1p2N​if​ρ≫1.{\cal E}_{2}\underset{p\to 0}{\sim}\begin{cases}\frac{\rho\;p}{N}\;\;\text{if}\;\;\rho\ll 1\\
\frac{p^{2}}{N}\;\;\text{if}\;\;\rho\gg 1.\end{cases}(43)

## A.2ModelM1M_{1}in classℳ1\mathcal{M}_{1}

In the case of modelM1∈ℳ1M_{1}\in\mathcal{M}_{1}, we havez^​(Xt;𝜽)=p^(1)​(Xt;𝜽)=M1​(Xt,𝜽)\widehat{z}(X_{t};{\boldsymbol{\theta}})={\widehat{p}}^{(1)}(X_{t};{\boldsymbol{\theta}})=M_{1}(X_{t},{\boldsymbol{\theta}})and the loss function is simply given by expression (6).
In order to simply upcoming developments, let us remark thatp^(1)​(Xt;𝜽)=Sig​[L​(Xt,𝜽)]{\widehat{p}}^{(1)}(X_{t};{\boldsymbol{\theta}})={\mbox{Sig}}\left[L(X_{t},{\boldsymbol{\theta}})\right]whereL​(Xt,θ)L(X_{t},\theta)denotes the logit output corresponding to the model output just before entering in the sigmoid function,Sig​(u)=11+e−u{\mbox{Sig}}(u)=\frac{1}{1+e^{-u}}. For example, one can chooseL​(Xt,𝜽)=M2​(Xt,𝜽)L(X_{t},{\boldsymbol{\theta}})=M_{2}(X_{t},{\boldsymbol{\theta}}).
Since the sigmoid function satisfies0≤Sig​(u)≤10\leq{\mbox{Sig}}(u)\leq 1andSig′​(u)=Sig​(u)​(1−Sig​(u)){\mbox{Sig}}^{\prime}(u)={\mbox{Sig}}(u)(1-{\mbox{Sig}}(u)), we have:d​p^(1)d​L=p^(1)​(1−p^(1)).\frac{d{\widehat{p}}^{(1)}}{dL}={\widehat{p}}^{(1)}(1-{\widehat{p}}^{(1)})\;.(44)

One can thus estimate∇𝜽p^(1)​(Xt,𝜽)|𝜽=𝜽0\left.\nabla_{{\boldsymbol{\theta}}}{\widehat{p}}^{(1)}(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}, as:∇𝜽p^(1)​(Xt,𝜽)|𝜽=𝜽0=pt​(1−pt)​∇𝜽L​(Xt,𝜽)|𝜽=𝜽0\left.\nabla_{{\boldsymbol{\theta}}}{\widehat{p}}^{(1)}(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}=p_{t}(1-p_{t})\left.\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}(45)

In order to estimate the Fisher information Matrix behavior, let us remark
that, the case ofM1M_{1}, the per-sample loss function involved with the BCE isℓ​(It+h,Xt,𝜽)=−[It+h​ln⁡(p^t(1))+(1−It+h)​ln⁡(1−p^t(1))]\ell(I_{t+h},X_{t},{\boldsymbol{\theta}})=-\left[I_{t+h}\ln({\widehat{p}}^{(1)}_{t})+(1-I_{t+h})\ln(1-{\widehat{p}}^{(1)}_{t})\right]

wherep^t(1){\widehat{p}}^{(1)}_{t}stands forp^(1)​(Xt;𝜽){\widehat{p}}^{(1)}(X_{t};{\boldsymbol{\theta}})andIt+h=It+h​(Qp)I_{t+h}=I_{t+h}(Q_{p})is defined in Eq. (1).
One thus has, thanks to (44),∇𝜽ℓ​(It+h,Xt,𝜽)=∂ℓ∂p^t(1)⋅∂p^t(1)∂L⋅∇𝜽L​(Xt,𝜽)\displaystyle\nabla_{\boldsymbol{\theta}}\ell(I_{t+h},X_{t},{\boldsymbol{\theta}})=\frac{\partial\ell}{\partial{\widehat{p}}^{(1)}_{t}}\cdot\frac{\partial{\widehat{p}}^{(1)}_{t}}{\partial L}\cdot\nabla_{\boldsymbol{\theta}}L(X_{t},{\boldsymbol{\theta}})=(−It+hp^t(1)+1−It+h1−p^t(1))⋅(p^t(1)​(1−p^t(1)))⋅∇𝜽L\displaystyle=\left(-\frac{I_{t+h}}{{\widehat{p}}^{(1)}_{t}}+\frac{1-I_{t+h}}{1-{\widehat{p}}^{(1)}_{t}}\right)\cdot\left({\widehat{p}}^{(1)}_{t}(1-{\widehat{p}}^{(1)}_{t})\right)\cdot\nabla_{\boldsymbol{\theta}}L=(p^t(1)−It+h)⋅∇𝜽L​(Xt,𝜽)\displaystyle=({\widehat{p}}^{(1)}_{t}-I_{t+h})\cdot\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})

Hence, because when𝜽=𝜽0{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0},p^t(1)=pt{\widehat{p}}^{(1)}_{t}=p_{t},
the Fisher information matrix becomes:I​(𝜽0)=𝔼Xt​(pt​(1−pt)​V​(Xt))I({\boldsymbol{\theta}}_{0})={\mathbb{E}}_{X_{t}}\Big(p_{t}(1-p_{t})V(X_{t})\Big)\\(46)

where, in order handle simple expressions, we define the matrixV​(Xt)=∇𝜽L​(Xt,𝜽)|𝜽=𝜽0.∇𝜽L​(Xt,𝜽)⊤|𝜽=𝜽0.V(X_{t})=\left.\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}.\left.\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})^{\top}\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\;.

From Eq. (34), using Eq. (45), we thus compute
the error associated with the asymptotic variance ofM1M_{1}output:Var​(p^(1)​(Xt))=pt2​(1−pt)2N​V1​(Xt)\mathrm{Var}\!\left({\widehat{p}}^{(1)}(X_{t})\right)=\frac{p_{t}^{2}(1-p_{t})^{2}}{N}V_{1}(X_{t})(47)

with:V1​(Xt)=∇𝜽L​(Xt,𝜽)⊤|𝜽=𝜽0​I𝜽0−1​∇𝜽L​(Xt,𝜽)|𝜽=𝜽0.V_{1}(X_{t})=\left.\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})^{\top}\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\left.\!\!\!\!I_{{\boldsymbol{\theta}}_{0}}^{-1}\;\nabla_{{\boldsymbol{\theta}}}L(X_{t},{\boldsymbol{\theta}})\right|_{{\boldsymbol{\theta}}={\boldsymbol{\theta}}_{0}}\;.

The final expression of the error thus becomes:ℰ1=𝔼Xt​[Var​(p^(3)​(Xt))]=1N​𝔼Xt​[pt2​(1−pt)2​V1​(Xt)].{\cal E}_{1}={\mathbb{E}}_{X_{t}}\left[\mathrm{Var}\!\left({\widehat{p}}^{(3)}(X_{t})\right)\right]=\frac{1}{N}{\mathbb{E}}_{X_{t}}\left[p_{t}^{2}(1-p_{t})^{2}V_{1}(X_{t})\right]\;.(48)

If one neglects correlations betweenpt​(1−pt)p_{t}(1-p_{t})andV​(Xt)V(X_{t})inI​(𝜽0)I({\boldsymbol{\theta}}_{0})as given in Eq. (46), then because𝔼Xt​(pt​(1−pt))≈p{\mathbb{E}}_{X_{t}}(p_{t}(1-p_{t}))\approx pwhenp≪1p\ll 1,
one has:V1​(Xt)≈p−1​V1′​(Xt)V_{1}(X_{t})\approx p^{-1}V^{\prime}_{1}(X_{t})(49)

whereV1′​(Xt)V^{\prime}_{1}(X_{t})is a scalar defined similarly as in (37) that does not depend onpp. We
then have:ℰ1≈1p​N​𝔼Xt​[pt2​(1−pt)2​V1′​(Xt)]{\cal E}_{1}\approx\frac{1}{pN}{\mathbb{E}}_{X_{t}}\left[p_{t}^{2}(1-p_{t})^{2}V^{\prime}_{1}(X_{t})\right](50)

that is the analog of (39).
By definingV1′​(μ)=𝔼​(V1′​(Xt)|μ​(Xt)=μ)V^{\prime}_{1}(\mu)={\mathbb{E}}(V^{\prime}_{1}(X_{t})|\mu(X_{t})=\mu)and
assuming thatμ\muis Gaussian random variable of zero mean and variances2s^{2},
one gets:ℰ1=1p​N​(2​π)1/2​s\displaystyle{\cal E}_{1}=\frac{1}{pN(2\pi)^{1/2}s}∫V1′​(μ)​e−μ22​s2​Φ2​(μ−Qpσ)\displaystyle\int V^{\prime}_{1}(\mu)e^{-\frac{\mu^{2}}{2s^{2}}}\Phi^{2}\left(\frac{\mu-Q_{p}}{\sigma}\right)(51)[1−Φ​(μ−Qpσ)]2​d​μ\displaystyle\left[1-\Phi\left(\frac{\mu-Q_{p}}{\sigma}\right)\right]^{2}\;d\mu

withQp=−s2+σ2​Φ−1​(p)Q_{p}=-\sqrt{s^{2}+\sigma^{2}}\Phi^{-1}(p).
By supposing, as previously, thatV1′​(μ)V^{\prime}_{1}(\mu)independent ofμ\mu(or more specifically ofptp_{t}), by settingV1=𝔼​(V1​(μ))V_{1}={\mathbb{E}}(V_{1}(\mu))and considering that, whenp→0p\to 0(Qp→∞Q_{p}\to\infty),[1−Φ2​(μ−Qpσ)]≃1\left[1-\Phi^{2}\left(\frac{\mu-Q_{p}}{\sigma}\right)\right]\simeq 1one finally gets:ℰ1≈V1p​N​(2​π)1/2​s​∫e−μ22​s2​Φ2​(μ−Qpσ)​𝑑μ.{\cal E}_{1}\approx\frac{V_{1}}{pN(2\pi)^{1/2}s}\int e^{-\frac{\mu^{2}}{2s^{2}}}\Phi^{2}\left(\frac{\mu-Q_{p}}{\sigma}\right)\;d\mu\;.(52)

Such an expression can be exactly computed by Gaussian integration. It reads:ℰ1≈V1p​N​Φ2​(Φ−1​(p),Φ−1​(p);r).{\cal E}_{1}\approx\frac{V_{1}}{pN}\Phi_{2}(\Phi^{-1}(p),\Phi^{-1}(p);r)\;.(53)

whereΦ2​(q,q,r)\Phi_{2}(q,q,r)is the cdf of the bivariate normal standard normal distribution with correlation coefficientrr(0<r<10<r<1):r=s2s2+σ2=11+ρ2,r=\frac{s^{2}}{s^{2}+\sigma^{2}}=\frac{1}{1+\rho^{2}},(54)

ρ2\rho^{2}being the noise-to-signal ratio defined in (21).
From asymptotic behavior whenp→0p\to 0:Φ2​(Φ−1​(p),Φ−1​(p);r)∼(4​π)−r1+r1−r2​p21+r​[ln⁡(1/p)]−r1+r,\Phi_{2}\!\big(\Phi^{-1}(p),\,\Phi^{-1}(p);\,r\big)\;\sim\;\frac{(4\pi)^{-\frac{r}{1+r}}}{\sqrt{1-r^{2}}}\;p^{\frac{2}{1+r}}\,\bigl[\ln(1/p)\bigr]^{-\frac{r}{1+r}}\;,(55)

one obtains the behavior of the error of methodℳ1\mathcal{M}_{1}as a function ofpp:ℰ1​≈p→0​K1​(ρ)N​pρ22+ρ2​[ln⁡(1/p)]−12+ρ2,{\cal E}_{1}\underset{p\to 0}{\approx}\frac{K_{1}(\rho)}{N}p^{\frac{\rho^{2}}{2+\rho^{2}}}\,\bigl[\ln(1/p)\bigr]^{-\frac{1}{2+\rho^{2}}},(56)

whereK1​(ρ)K_{1}(\rho)is the constant that depends onρ\rho. This equation can be directly compared with
Eq. (42).
We notably see that, up to logarithmic corrections:ℰ1​∼p→0​{1N​if​ρ≪1pN​if​ρ≫1.{\cal E}_{1}\underset{p\to 0}{\sim}\begin{cases}\frac{1}{N}\;\;\text{if}\;\;\rho\ll 1\\
\frac{p}{N}\;\;\text{if}\;\;\rho\gg 1.\end{cases}(57)

## Appendix BRelative Brier Score and Log-score performances ofℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}

We can exploit the conditional variance formulas established in AppendixAto derive the asymptotic behavior Brier and logarithmic scores associated with predictions of modelsM1M_{1}andM2M_{2}. As before, we pay particular attention to the rare-event regime (p→0p\to 0).
We denotep^t(k){\widehat{p}}_{t}^{(k)}denote the estimator of the exceedance probabilitypt=Prob​(Yt+h>Qp∣Xt)p_{t}=\mathrm{Prob}(Y_{t+h}>Q_{p}\mid X_{t})with modelMkM_{k}wherek=1k=1or22.
According to Eq. (13), the Brier Skill scoreB​SkBS_{k}ofMkM_{k}, reads (by replacing the average over observations by the mathematical expectation over the joint law of(𝜽^,Xt,νt+h)(\widehat{{\boldsymbol{\theta}}},X_{t},\nu_{t+h})or equivalently of(𝜽^,pt,It+h)(\widehat{{\boldsymbol{\theta}}},p_{t},I_{t+h})B​Sk\displaystyle BS_{k}=\displaystyle=𝔼​(p^t(k)−It+h)2=𝔼​(p^t(k)−pt+pt−It+h)2\displaystyle{\mathbb{E}}\left({\widehat{p}}_{t}^{(k)}-I_{t+h}\right)^{2}={\mathbb{E}}\left({\widehat{p}}_{t}^{(k)}-p_{t}+p_{t}-I_{t+h}\right)^{2}=\displaystyle=𝔼𝜽^​𝔼pt​(p^t(k)−pt)2+𝔼pt​𝔼It+h|pt​(pt−It+h)2\displaystyle{\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}{\mathbb{E}}_{p_{t}}\left({\widehat{p}}_{t}^{(k)}-p_{t}\right)^{2}+{\mathbb{E}}_{p_{t}}{\mathbb{E}}_{I_{t+h}|p_{t}}\left(p_{t}-I_{t+h}\right)^{2}=\displaystyle=ℰk+𝔼pt​(pt​(1−pt))\displaystyle\mathcal{E}_{k}+{\mathbb{E}}_{p_{t}}\left(p_{t}(1-p_{t})\right)

where we have considered zero correlations between errors(p^t(k)−pt)({\widehat{p}}_{t}^{(k)}-p_{t})and(pt−It+h)(p_{t}-I_{t+h})and
used the fact the𝔼It+h|pt​(It+h)=pt{\mathbb{E}}_{I_{t+h}|p_{t}}(I_{t+h})=p_{t}withIt+h2=It+hI_{t+h}^{2}=I_{t+h}.
Thanks to Eqs. (22) and (23) we finally have the exact relationship between the Brier score ofMkM_{k}and the previously computed asymptotic errorℰk\mathcal{E}_{k}that reads:B​Sk=ℰk+p−Φ2​(Φ−1​(p),Φ−1​(p),r)BS_{k}=\mathcal{E}_{k}+p-\Phi_{2}\left(\Phi^{-1}(p),\Phi^{-1}(p),r\right)(58)

withr=11+ρ2r=\frac{1}{1+\rho^{2}}.
It results from (14), that the Brier Skill of each modelMkM_{k}is :B​S​Sk=1−ℰk+p−Φ2​(Φ−1​(p),Φ−1​(p),r)p​(1−p)BSS_{k}=1-\frac{\mathcal{E}_{k}+p-\Phi_{2}\left(\Phi^{-1}(p),\Phi^{-1}(p),r\right)}{p(1-p)}(59)

Given the asymptotic behavior ofΦ2\Phi_{2}whenp↓0p\downarrow 0(Eq. (55), we have:B​S​Sk≈pρ​22+ρ2−ℰkp.BSS_{k}\approx p^{\frac{\rho 2}{2+\rho^{2}}}-\frac{\mathcal{E}_{k}}{p}\;.(60)

The logarithmic score corresponds to the binary cross-entropy defined in Eq. (6) which expectation givesLSk=−𝔼𝜽^​𝔼Xt​𝔼It+h|Xt​[It+h​ln⁡(p^t(k))+(1−It+h)​ln⁡(1−p^t(k))]\mathrm{LS}_{k}=-{\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}{\mathbb{E}}_{X_{t}}{\mathbb{E}}_{I_{t+h}|X_{t}}\left[I_{t+h}\ln\left({\widehat{p}}_{t}^{(k)}\right)+\left(1-I_{t+h}\right)\ln\left(1-{\widehat{p}}_{t}^{(k)}\right)\right]which leads to:LSk=−𝔼𝜽^​𝔼Xt​[pt​ln⁡(p^t(k))+(1−pt)​ln⁡(1−p^t(k))]\mathrm{LS}_{k}=-{\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}{\mathbb{E}}_{X_{t}}\left[p_{t}\ln\left({\widehat{p}}_{t}^{(k)}\right)+\left(1-p_{t}\right)\ln\left(1-{\widehat{p}}_{t}^{(k)}\right)\right]

where, as before,p^t(k)=p^(k)​(Xt;𝜽^){\widehat{p}}^{(k)}_{t}={\widehat{p}}^{(k)}(X_{t};\widehat{{\boldsymbol{\theta}}})andIt+h=It+h​(Qp)I_{t+h}=I_{t+h}(Q_{p})is defined in Eq. (1).
In this context, in order to compare methodsM1M_{1}andM2M_{2}, one can
evaluateΔ​LS1,2=LS1−LS2\Delta\mathrm{LS}_{1,2}=\mathrm{LS}_{1}-\mathrm{LS}_{2}

where a positive value means thatM2M_{2}performs better thanM1M_{1}.Δ​LS1,2\Delta\mathrm{LS}_{1,2}can be conveniently expressed as:Δ​LS1,2=ℛ1−ℛ2\Delta\mathrm{LS}_{1,2}={\mathcal{R}}_{1}-{\mathcal{R}}_{2}where “excess risk”ℛk=DK​L(pt||p^t(k)){\mathcal{R}}_{k}=D_{KL}\Big(p_{t}||{\widehat{p}}_{t}^{(k)}\Big)represents the Kullback-Leibler divergence
with respect to the true probability, namely:ℛk=𝔼𝜽^​𝔼Xt​[pt​ln⁡ptp^t(k)+(1−pt)​ln⁡1−pt1−p^t(k)].{\mathcal{R}}_{k}={\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}{\mathbb{E}}_{X_{t}}\left[p_{t}\ln\frac{p_{t}}{{\widehat{p}}_{t}^{(k)}}+(1-p_{t})\ln\frac{1-p_{t}}{1-{\widehat{p}}_{t}^{(k)}}\right]\;.(61)

Assuming consistency of the estimators, ie., thatp^t(k)=pt+δt{\widehat{p}}^{(k)}_{t}=p_{t}+\delta_{t}withδt≪1\delta_{t}\ll 1, we can perform a second-order Taylor expansion of the KL divergence aroundptp_{t}and then, taking the expectation over the sampling distribution of the parameters𝜽^\widehat{{\boldsymbol{\theta}}}(which governs the variance ofp^t(k){\widehat{p}}_{t}^{(k)}), we obtain:ℛk≈12​𝔼Xt​(Var​(p^t(k))pt​(1−pt)).{\mathcal{R}_{k}}\approx\frac{1}{2}{\mathbb{E}}_{X_{t}}\left(\frac{\mathrm{Var}\!\left({\widehat{p}}_{t}^{(k)}\right)}{p_{t}(1-p_{t})}\right)\;.

Former expressions of the variance (47) and (38), thus entail respectively:ℛ1\displaystyle\mathcal{R}_{1}≈12​N​p​𝔼Xt​(pt​(1−pt)​V1′​(Xt))\displaystyle\approx\frac{1}{2Np}\mathbb{E}_{X_{t}}\left(p_{t}(1-p_{t})V^{\prime}_{1}(X_{t})\right)ℛ2\displaystyle\mathcal{R}_{2}≈12​N​𝔼Xt​(V2′​(Xt)​ϕ2​(Qp−μ​(Xt)σ)Φ​(μ​(Xt)−Qpσ)​[1−Φ​(μ​(Xt)−Qpσ)])\displaystyle\approx\frac{1}{2N}\mathbb{E}_{X_{t}}\left(\frac{V_{2}^{\prime}(X_{t})\phi^{2}\left(\frac{Q_{p}-\mu(X_{t})}{\sigma}\right)}{\Phi\left(\frac{\mu(X_{t})-Q_{p}}{\sigma}\right)\left[1-\Phi\left(\frac{\mu(X_{t})-Q_{p}}{\sigma}\right)\right]}\right)

where we used the the fact thatpt=Φ​(μ​(Xt)−Qpσ)p_{t}=\Phi\left(\frac{\mu(X_{t})-Q_{p}}{\sigma}\right).
If one focuses on rare-event regime wherept≪1p_{t}\ll 1and one supposes thatV1′​(Xt)V_{1}^{\prime}(X_{t})andV2′​(Xt)V_{2}^{\prime}(X_{t})are independent from terms inptp_{t}andϕ2\phi^{2}, we obtain the asymptotic approximations:ℛ1\displaystyle{\mathcal{R}}_{1}≈\displaystyle\approx12​N​p​𝔼Xt​(pt​V1′​(Xt))=V12​N\displaystyle\frac{1}{2Np}{\mathbb{E}}_{X_{t}}\left(p_{t}V^{\prime}_{1}(X_{t})\right)=\frac{V_{1}}{2N}(62)ℛ2\displaystyle{\mathcal{R}}_{2}≈\displaystyle\approxV22​N​𝔼Xt​(ϕ2​(Qp−μ​(Xt)σ)Φ​(μ​(Xt)−Qpσ))\displaystyle\frac{V_{2}}{2N}{\mathbb{E}}_{X_{t}}\left(\frac{\phi^{2}\left(\frac{Q_{p}-\mu(X_{t})}{\sigma}\right)}{\Phi\left(\frac{\mu(X_{t})-Q_{p}}{\sigma}\right)}\right)(63)

where we used the definition ofpp, namely𝔼​(pt)=p{\mathbb{E}}(p_{t})=p.ℛ2{\mathcal{R}}_{2}can be rewritten asℛ2=𝔼μ​[σ2​ϕ2​(z)/Φ​(z)]{\mathcal{R}}_{2}=\mathbb{E}_{\mu}[\sigma^{2}\phi^{2}(z)/\Phi(z)]withz=(μ−Qp)/σz=(\mu-Q_{p})/\sigma. In the rare-event regime (p→0p\to 0),
sinceQp→∞Q_{p}\to\infty, the argumentzztends to−∞-\infty. Using the Mill’s ratio approximationΦ​(z)∼ϕ​(z)/|z|\Phi(z)\sim\phi(z)/|z|, the integrand simplifies to a linear-Gaussian formσ​|z|​ϕ​(z)\sigma|z|\phi(z).
As before, the resulting integral is evaluated using the saddle-point method, dominated by the contribution atμ∗=Qp​s2/(s2+σ2)\mu_{*}=Q_{p}s^{2}/(s^{2}+\sigma^{2}). This leads to a scaling proportional top​[Φ−1​(p)]2p[\Phi^{-1}(p)]^{2}. By incorporating the refined asymptotic expansion of the quantile function and settingρ2=σ2s2\rho^{2}=\frac{\sigma^{2}}{s^{2}}, we obtain the final behaviorℛ2≈V2​ρ2(1+ρ2)​N​p​ln⁡(1p){\mathcal{R}}_{2}\approx\frac{V_{2}\rho^{2}}{(1+\rho^{2})N}\,p\ \ln\left(\frac{1}{p}\right)leading to our final estimation:Δ​LS1,2​≈p→0​Cρ2​N​(Kρ−p​ln⁡(p−1))\Delta\mathrm{LS}_{1,2}\underset{p\to 0}{\approx}\frac{C_{\rho}}{2N}\left(K_{\rho}-p\ln\left(p^{-1}\right)\right)(64)

whereCρ=2​V2​ρ2(1+ρ2)C_{\rho}=\frac{2V_{2}\rho^{2}}{(1+\rho^{2})}andKρ=V1CρK_{\rho}=\frac{V_{1}}{C_{\rho}}.
We see, providedppis small enough,Δ​S1,2\Delta S_{1,2}is clearly positive andM2M_{2}outperformsM1M_{1}.

## Appendix CAsymptotic Analysis of the Peirce Skill Score (PSS)

Let us perform the same kind of analysis for PSS score. We can remark, from the definition of (10), the averagedPSSk\mathrm{PSS}_{k}for methodℳk\mathcal{M}_{k}can be written as:PSSk\displaystyle\text{PSS}_{k}=𝔼𝜽^[Prob(I^t+h(k)=1|It+h=1)\displaystyle={\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}\left[\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=1\right)\right.(65)−Prob(I^t+h(k)=1|It+h=0)]\displaystyle\left.-\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=0\right)\right]

wherek=1,2k=1,2andI^t+h(k){\widehat{I}}_{t+h}^{(k)}is defined as in Eq. (4), namely,I^t+h(k)=1​if​p^t(k)>p​and​I^t(k)=0​otherwise{\widehat{I}}_{t+h}^{(k)}=1\;\mathrm{if}\;{\widehat{p}}_{t}^{(k)}>p\;\mathrm{and}\;{\widehat{I}}_{t}^{(k)}=0\;\mathrm{otherwise}withp^t(k)=p^(k)​(Xt,𝜽^){\widehat{p}}_{t}^{(k)}={\widehat{p}}^{(k)}(X_{t},\widehat{{\boldsymbol{\theta}}}). It results that:Prob​(I^t+h(k)=1|It+h=1)=∫𝑑x​fX​(x|It+h=1)​𝕀{p^(k)​(x,𝜽^)>p}\displaystyle\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=1\right)=\int dxf_{X}(x|I_{t+h}=1)\mathbb{I}_{\{{\widehat{p}}^{(k)}(x,\widehat{{\boldsymbol{\theta}}})>p\}}=∫fX​(x|It+h=1)​𝕀{P​(x)−p^(k)​(x,𝜽^)<P​(x)−p}\displaystyle=\int f_{X}(x|I_{t+h}=1)\mathbb{I}_{\{P(x)-{\widehat{p}}^{(k)}(x,\widehat{{\boldsymbol{\theta}}})<P(x)-p\}}

where we denoted, at fixedtt,fX​(x)f_{X}(x)the pdf ofXtX_{t}andP​(Xt)=ptP(X_{t})=p_{t}is defined in (19).
By Bayes rule, we havefX​(x|It+h=1)\displaystyle f_{X}(x|I_{t+h}=1)=Prob​(It+h=1|Xt=x)​fX​(x)Prob​(It+h=1)\displaystyle=\frac{\mathrm{Prob}(I_{t+h}=1|\;X_{t}=x)f_{X}(x)}{\mathrm{Prob}(I_{t+h}=1)}=P​(x)​fX​(x)p\displaystyle=\frac{P(x)f_{X}(x)}{p}

and in the same way we havefX​(x|It+h=0)=(1−P​(x))​fX​(x)1−p.f_{X}(x|I_{t+h}=0)=\frac{(1-P(x))f_{X}(x)}{1-p}\;.

This thus entails:Prob​(I^t+h(k)=1|It+h=1)=\displaystyle\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=1\right)=p−1​∫P​(z)​fX​(x)​𝕀{P​(x)−p^(k)​(x,𝜽^)<P​(x)−p}\displaystyle p^{-1}\int P(z)f_{X}(x)\mathbb{I}_{\{P(x)-{\widehat{p}}^{(k)}(x,\widehat{{\boldsymbol{\theta}}})<P(x)-p\}}=p−1​𝔼μ​(Φ​(μ−Qpσ2)​𝕀{P​(x)−p^(k)​(x,𝜽^)<Φ​(μ−Qpσ2)−p})\displaystyle=p^{-1}{\mathbb{E}}_{\mu}\left(\Phi\left(\frac{\mu-Q_{p}}{\sigma^{2}}\right)\mathbb{I}_{\{P(x)-{\widehat{p}}^{(k)}(x,\widehat{{\boldsymbol{\theta}}})<\Phi(\frac{\mu-Q_{p}}{\sigma^{2}})-p\}}\right)

where we made the change of variablex→μ​(x)x\rightarrow\mu(x)and used (19) for the relationship betweenP​(x)P(x)andμ​(x)\mu(x),Φ\Phistanding for the standard normal CDF.
Finally, taking the expectation as respect to the law of𝜽^\widehat{{\boldsymbol{\theta}}}that is supposed to be asymptotically normal, we obtain:𝔼𝜽^​[Prob​(I^t+h(k)=1|It+h=1)]=\displaystyle{\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}\left[\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=1\right)\right]=p−1​𝔼μ​[Φ​(μ−Qpσ2)​Φ​(Φ​(μ−Qpσ2)−pVar​(p^(k)​(Xt)))]=\displaystyle p^{-1}{\mathbb{E}}_{\mu}\left[\Phi\left(\frac{\mu-Q_{p}}{\sigma^{2}}\right)\Phi\left(\frac{\Phi(\frac{\mu-Q_{p}}{\sigma^{2}})-p}{\sqrt{\mathrm{Var}\!\left({\widehat{p}}^{(k)}(X_{t})\right)}}\right)\right]=p−1​𝔼pt​[pt​Φ​(pt−pVar​(p^(k)​(Xt)))]\displaystyle p^{-1}{\mathbb{E}}_{p_{t}}\left[p_{t}\Phi\left(\frac{p_{t}-p}{\sqrt{\mathrm{Var}\!\left({\widehat{p}}^{(k)}(X_{t})\right)}}\right)\right]

Along the same line one can establish that𝔼𝜽^​[Prob​(I^t+h(k)=1|It+h=0)]=\displaystyle{\mathbb{E}}_{\widehat{{\boldsymbol{\theta}}}}\left[\mathrm{Prob}\left({\widehat{I}}_{t+h}^{(k)}=1\;|\;I_{t+h}=0\right)\right]=(1−p)−1​𝔼pt​[(1−pt)​Φ​(pt−pVar​(p^(k)​(Xt)))]\displaystyle(1-p)^{-1}{\mathbb{E}}_{p_{t}}\left[(1-p_{t})\Phi\left(\frac{p_{t}-p}{\sqrt{\mathrm{Var}\!\left({\widehat{p}}^{(k)}(X_{t})\right)}}\right)\right]

and therefore, from (65), we obtain the following expression ofPSSk\text{PSS}_{k}:PSSk=1p​(1−p)​𝔼pt​[(pt−p)​Φ​(pt−pVar​(p^(k)​(Xt)))]\text{PSS}_{k}=\frac{1}{p(1-p)}{\mathbb{E}}_{p_{t}}\left[(p_{t}-p)\Phi\left(\frac{p_{t}-p}{\sqrt{\mathrm{Var}\!\left({\widehat{p}}^{(k)}(X_{t})\right)}}\right)\right]

From Eqs. (47) and (38), when1−pt≈11-p_{t}\approx 1, we get:PSS1=1p​(1−p)​𝔼pt​[(pt−p)​Φ​(p​(pt−p)pt​V1′​N−12)]\displaystyle\text{PSS}_{1}=\frac{1}{p(1-p)}{\mathbb{E}}_{p_{t}}\left[(p_{t}-p)\Phi\left(\frac{\sqrt{p}(p_{t}-p)}{p_{t}\sqrt{V_{1}^{\prime}}N^{-\frac{1}{2}}}\right)\right](66)PSS2=1p​(1−p)​𝔼pt​[(pt−p)​Φ​(pt−ppt​2​ln⁡(pt−1)​V2′​N−12)].\displaystyle\!\!\!\!\!\text{PSS}_{2}=\frac{1}{p(1-p)}{\mathbb{E}}_{p_{t}}\left[(p_{t}-p)\Phi\left(\frac{p_{t}-p}{p_{t}\sqrt{2\ln(p_{t}^{-1})V_{2}^{\prime}}N^{-\frac{1}{2}}}\right)\right]\;.(67)

WhenNNis very large,σN(k)→0\sigma^{(k)}_{N}\to 0, so we can use the expansion ofΦ​(xσ)\Phi(\frac{x}{\sigma})asσ→0\sigma\to 0:Φ​(xσ)=ℋ​(x)+σ22​δ′​(x)+𝒪​(σ4),\Phi\Big(\frac{x}{\sigma}\Big)={\mathcal{H}}(x)+\frac{\sigma^{2}}{2}\delta^{\prime}(x)+\mathcal{O}(\sigma^{4}),

whereℋ​(x){\mathcal{H}}(x)is the Heaviside function andδ′​(x)\delta^{\prime}(x)is the derivative of the Dirac distribution.
It results that, at fixedpp, for largeNN, we have:PSS1≈1p​(1−p)​(𝔼pt​(pt−p)+−V1′2​N​p​fpt​(p))\displaystyle\text{PSS}_{1}\approx\frac{1}{p(1-p)}\left({\mathbb{E}}_{p_{t}}(p_{t}-p)^{+}-\frac{V_{1}^{\prime}}{2N}pf_{p_{t}}(p)\right)(68)PSS2≈1p​(1−p)​(𝔼pt​(pt−p)+−V2′​p2N​ln⁡(1p)​fpt​(p))\displaystyle\text{PSS}_{2}\approx\frac{1}{p(1-p)}\left({\mathbb{E}}_{p_{t}}(p_{t}-p)^{+}-\frac{V_{2}^{\prime}p^{2}}{N}\ln(\frac{1}{p})f_{p_{t}}(p)\right)(69)

To evaluate the behavior ofP​S​SkPSS_{k}forp≪1p\ll 1, we thus have to analyze the asymptotic limits of both𝔼pt​[(pt−p)+]\mathbb{E}_{p_{t}}[(p_{t}-p)^{+}]andfpt​(p)f_{p_{t}}(p). Sincept=Φ​((μt−Qp)/σ)p_{t}=\Phi((\mu_{t}-Q_{p})/\sigma)whereμt∼𝒩​(0,s2)\mu_{t}\sim\mathcal{N}(0,s^{2}), a simple change of variable leads to the density:fpt​(y)=σs​ϕ​(σ​Φ−1​(y)+Xps)ϕ​(Φ−1​(y)).f_{p_{t}}(y)=\frac{\sigma}{s}\frac{\phi\left(\frac{\sigma\Phi^{-1}(y)+X_{p}}{s}\right)}{\phi(\Phi^{-1}(y))}\;.(70)

Evaluating this density at the boundaryy=py=pusing the asymptotic relationΦ−1​(p)2∼2​ln⁡(1/p)\Phi^{-1}(p)^{2}\sim 2\ln(1/p)leads a power-law behavior:fpt​(p)∝exp⁡(γ​Φ−1​(p)22)∼p−γ,f_{p_{t}}(p)\propto\exp\left(\gamma\frac{\Phi^{-1}(p)^{2}}{2}\right)\sim p^{-\gamma}\;,(71)

where the scaling exponent is bounded byγ=2​σs2+σ2+σ∈(0,1)\gamma=\frac{2\sigma}{\sqrt{s^{2}+\sigma^{2}}+\sigma}\in(0,1). The expectation𝔼​[(pt−p)+]=∫p1(y−p)​fpt​(y)​𝑑y\mathbb{E}[(p_{t}-p)^{+}]=\int_{p}^{1}(y-p)f_{p_{t}}(y)dycan be mapped to the original distribution ofμt∼𝒩​(0,s2)\mu_{t}\sim\mathcal{N}(0,s^{2}). By determining the positivity threshold of the integrand,L=Φ−1​(p)​(σ−s2+σ2)L=\Phi^{-1}(p)(\sigma-\sqrt{s^{2}+\sigma^{2}}), and applying the bivariate identity∫ϕ​(z)​Φ​(a​z+b)​𝑑z=Φ2​(z,b1+a2;−a1+a2)\int\phi(z)\Phi(az+b)dz=\Phi_{2}(z,\frac{b}{\sqrt{1+a^{2}}};\frac{-a}{\sqrt{1+a^{2}}}), the integral evaluates to:𝔼​[(pt−p)+]=p​Φ​(Ls)−Φ2​(Ls,Φ−1​(p);−ss2+σ2).\mathbb{E}[(p_{t}-p)^{+}]=p\Phi\left(\frac{L}{s}\right)-\Phi_{2}\left(\frac{L}{s},\Phi^{-1}(p);\frac{-s}{\sqrt{s^{2}+\sigma^{2}}}\right)\;.

In the limitp≪1p\ll 1, this yields the leading-order behavior𝔼​[(pt−p)+]≈Pr​p\mathbb{E}[(p_{t}-p)^{+}]\approx P_{r}p, wherePrP_{r}depends on the correlation parameterr=−s/s2+σ2r=-s/\sqrt{s^{2}+\sigma^{2}}. Substituting these asymptotic limits back into Eqs. (68), (69) and dropping minor logarithmic corrections directly yields the final PSS scaling rules:PSS1\displaystyle\text{PSS}_{1}≈\displaystyle\approx1−Kr​pκ2−C1N​p−γ\displaystyle 1-K_{r}p^{\kappa^{2}}-\frac{C_{1}}{N}p^{-\gamma}(72)PSS2\displaystyle\text{PSS}_{2}≈\displaystyle\approx1−Kr​pκ2−C2N​p1−γ\displaystyle 1-K_{r}p^{\kappa_{2}}-\frac{C_{2}}{N}p^{1-\gamma}(73)

Consequently, whenNNis large relative toK​p−γKp^{-\gamma}, the performance ratio simplifies to:PSS​1PSS​2≈1−CpN​p−γ+𝒪​(1N2)\frac{\text{PSS}{1}}{\text{PSS}{2}}\approx 1-\frac{C_{p}}{N}p^{-\gamma}+\mathcal{O}\left(\frac{1}{N^{2}}\right)(74)

withCp∼C1​p−γ​(1−C2​p)C_{p}\sim C_{1}p^{-\gamma}(1-C_{2}p). This formalizes whyM2M_{2}achieves a superior PSS overM1M_{1}at smallpp, while both safely converge to 1 asN→∞N\to\infty.

## Appendix DA toy model: the weighted harmonic model

LetZZbe a vector of random latent factors defined as:Xt∈ℝN×d,Xt∼iid𝒩​(0,Id).X_{t}\in\mathbb{R}^{N\times d},\quad X_{t}\stackrel{{\scriptstyle\text{iid}}}{{\sim}}\mathcal{N}(0,I_{d})\;.

This means that, at each timet∈[0,N−1]t\in[0,N-1],Xt=(Xt,1,…,Xt,d)X_{t}=(X_{t,1},\dots,X_{t,d})is sampled independently from a standard normal distribution𝒩​(0,Id)\mathcal{N}(0,I_{d}). The model generates a scalar signalμt\mu_{t}as a weighted sum of centered harmonic transformations of these factors:μt=∑k=1d[wk(c)​(cos⁡(Xt,k)−e−1/2)+wk(s)​sin⁡(Xt,k)].\mu_{t}=\sum_{k=1}^{d}\left[w_{k}^{(c)}\left(\cos(X_{t,k})-e^{-1/2}\right)+w_{k}^{(s)}\sin(X_{t,k})\right].(75)

Here, the constante−1/2e^{-1/2}ensures that the cosine terms have zero mean. The coefficientswk(c)w_{k}^{(c)}andwk(s)w_{k}^{(s)}are fixed model parameters (frozen randomness). They are initialized by drawing from a standard normal distribution and then rescaled by a global factorλ\lambdato ensure that the theoretical variance ofμt\mu_{t}matches the target parameters2s^{2}.

## Appendix EProbability distributions for rainfall and wind speed

## E.1The M-Rice probability distribution

In(Baïle et al.,2011), the Rice probability distribution (which corresponds to the norm of a two dimensional random vector which components are 2 independent Gaussian random variables of meanμ1\mu_{1}andμ2\mu_{2}and of same varianceσ2\sigma^{2}) has been extended to “Multifractal Rice" (M-Rice) distribution that accounts for the situation when,
as observed in turbulence models, this varianceσ2\sigma^{2}is itself stochastic with a log-normal distribution.
The M-Rice distribution involves 3 parameters, namely the two Rice parameters coming from from Gaussian lawν=ν12+ν22\nu=\sqrt{\nu_{1}^{2}+\nu_{2}^{2}}andσ2\sigma^{2}and a supplementary parameter, denoted asλ2\lambda^{2}associated with the variance of the log-normal law. This parameter is referred to, in the literature on turbulence, as the “intermittency coefficient”(Frisch,1995). The M-Rice probability density function (PDF) is then:fMR​(y)=12​π​λ2​∫e−ω22​λ2​ye2​ω​σ2​e−y2+ν22​e2​ω​σ2​I0​(y​νe2​ω​σ2)​𝑑ω.f_{\text{MR}}(y)=\frac{1}{\sqrt{2\pi\lambda^{2}}}\int e^{-\frac{\omega^{2}}{2\lambda^{2}}}\frac{y}{e^{2\omega}\sigma^{2}}e^{-\frac{y^{2}+\nu^{2}}{2e^{2\omega}\sigma^{2}}}I_{0}(\frac{y\nu}{e^{2\omega}\sigma^{2}})\;d\omega\;.

whereI0​(z)I_{0}(z)is the order zero modified Bessel function of the first kind.
As advocated in(Baggio and Muzy,2024), this last formula can be fastly evaluated using the a simple Gauss-Hermite quadrature. The M-Rice cumulative distribution function (CDF) or the mean value function can also be obtained along the same way. For the latter, since for a Rice law of parameterν\nuandσ2\sigma^{2}, the mean value isμR=σ​π2​L12​(−ν22​σ2)\mu_{\text{R}}={\displaystyle\sigma{\sqrt{\frac{\pi}{2}}}\,\,L_{\frac{1}{2}}\left(-\frac{\nu^{2}}{2\sigma^{2}}\right)},
whereL12L_{\frac{1}{2}}stands for the order12\frac{1}{2}Laguerre polynomial,
the mean value of a M-Rice distribution reads:μMR​(ν,σ,λ2)≃σ2​∑i=1nwi​L12​(−e2​2​λ​yi​ν22​σ2)\mu_{\text{MR}}(\nu,\sigma,\lambda^{2})\simeq\frac{\sigma}{\sqrt{2}}\sum_{i=1}^{n}w_{i}\,L_{\frac{1}{2}}\left(-\frac{e^{2\sqrt{2}\lambda y_{i}}\nu^{2}}{2\sigma^{2}}\right)\;(76)

withwi=2n−1​n!​πn2​[Hn−1​(yi)]2w_{i}={\frac{2^{n-1}n!{\sqrt{\pi}}}{n^{2}[H_{n-1}(y_{i})]^{2}}}for a quadrature ordernn. For the purpose of this paper, we chose,n=11n=11.

## E.2Mixed distributions for rainfall

Mixed distributions, that is, combining a discrete with a continuous part, are common in the statistical modelling of rainfalls(Kedem et al.,1990). Indeed, there is a finite probability mass concentrated inX=0X=0(the probability that does not rain at all). The continuous part, which models distribution of rain event only, is observed to be highly non-symmetrical and skewed towards high intensity events, so that two common choices are the mixed lognormal and the mixed gamma distributions(Cho et al.,2004).
Considering this, we consider mixed distributions of the general formP​(X=0)=1−pw​e​t,P​(X>0)=pw​e​t,P(X=0)=1-p_{wet},\qquad P(X>0)=p_{wet},(77)

where, conditionally onX>0X>0, the rainfall intensity follows a continuous distribution with densityf+​(x;θ)f_{+}(x;\theta).
The resulting mixture distribution can be written asf​(x)=(1−pw​e​t)​δ0​(x)+pw​e​t​f+​(x;θ)​1{x>0},f(x)=(1-p_{wet})\,\delta_{0}(x)+p_{wet}\,f_{+}(x;\theta)\,\mathbf{1}_{\{x>0\}},(78)

whereδ0\delta_{0}denotes the Dirac mass at zero andθ\thetarepresents the parameters of the positive component. Three different distributionsf+​(x;θ)f_{+}(x;\theta)have been tested throughout this work, all characterized by two parameters. Meaning that (78) has 3 parameters in total (the probability of rainfall occurrencepw​e​tp_{wet}and two additional parameters). The tested distributionsf+​(x;θ)f_{+}(x;\theta)are briefly discussed below:

## Mixed lognormal distributionf+​(x)=1x​σ​2​π​exp⁡(−(log⁡x−μ)22​σ2),x>0.f_{+}(x)=\frac{1}{x\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(\log x-\mu)^{2}}{2\sigma^{2}}\right),\;x>0.(79)

whereμ\mucontrols the central tendency of positive rainfall amounts on the logarithmic scale andσ2\sigma^{2}governs dispersion and tail heaviness.

## Mixed inverse Gaussian distributionf+​(x)=(λ2​π​x3)1/2​exp⁡(−λ​(x−μ)22​μ2​x),x>0.f_{+}(x)=\left(\frac{\lambda}{2\pi x^{3}}\right)^{1/2}\exp\!\left(-\frac{\lambda(x-\mu)^{2}}{2\mu^{2}x}\right),\;x>0.(80)

whereμ>0\mu>0is the mean of the positive rainfall component andλ>0\lambda>0the shape parameter controlling dispersion and tail behavior.
The inverse Gaussian distribution class has notably been shown to account very well for monthly cumulated rainfalls inSukrutha et al. (2018).

## Mixed Weibull distributionf+​(x)=kλ​(xλ)k−1​exp⁡[−(xλ)k],x>0,f_{+}(x)=\frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1}\exp\!\left[-\left(\frac{x}{\lambda}\right)^{k}\right],\;x>0,(81)

whereλ\lambdais a scale parameter regulating the magnitude of rainfall andkkcontrols the shape of the distribution and tail behavior. The Weibull distribution has been used to model rainfall accumulation in several research works, such asWilks (1989); Olivera and Heard (2019)and more recentlyMarra et al. (2023).

## References
- Agrawal et al. (2019)Agrawal, S., Barrington, L., Bromberg, C., Burge, J., Gazen, C., and Hickey,
J.: Machine learning for precipitation nowcasting from radar images, arXiv
preprint arXiv:1912.12132,https://arxiv.org/abs/1912.12132,
2019.
- Ayzel et al. (2019)Ayzel, G., Heistermann, M., and Winterrath, T.: Optical flow models as an open
benchmark for radar-based precipitation nowcasting (rainymotion v0. 1),
Geoscientific Model Development, 12, 1387–1402, 2019.
- Bader et al. (2018)Bader, B., Yan, J., and Zhang, X.: Automated threshold selection for extreme
value analysis via ordered goodness-of-fit tests with adjustment for false
discovery rate, 2018.
- Baggio and Muzy (2024)Baggio, R. and Muzy, J.-F.: Improving probabilistic wind speed forecasting
using M-Rice distribution and spatial data integration, Applied Energy, 360,
122 840,10.1016/j.apenergy.2024.122840, 2024.
- Baggio et al. (2025)Baggio, R., Pujol, K., Pantillon, F., Lambert, D., Filippi, J.-B., and Muzy,
J.-F.: Local wind speed forecasting at short time horizons relying on both
Numerical Weather Prediction and observations from surrounding station, arXiv
preprint arXiv:2503.18797, 2025.
- Baïle et al. (2011)Baïle, R., Muzy, J. F., and Poggi, P.: An M-Rice wind speed frequency
distribution, Wind Energy, 14, 735–748,10.1002/we.454, 2011.
- Bauer et al. (2015)Bauer, P., Thorpe, A., and Brunet, G.: The quiet revolution of numerical
weather prediction, Nature, 525, 47–55,10.1038/nature14956, 2015.
- Baïle et al. (2011)Baïle, R., Muzy, J. F., and Poggi, P.: Short-term forecasting of surface layer
wind speed using a continuous random cascade model, Wind Energy, 14,
719–734,10.1002/we.452, 2011.
- Beauchemin and Barron (1995)Beauchemin, S. S. and Barron, J. L.: The computation of optical flow, ACM
computing surveys (CSUR), 27, 433–466, 1995.
- Bojinski et al. (2023)Bojinski, S., Blaauboer, D., Calbet, X., De Coning, E., Debie, F., Montmerle,
T., Nietosvaara, V., Norman, K., Bañón Peregrín, L., Schmid, F.,
et al.: Towards nowcasting in Europe in 2030, Meteorological applications,
30, e2124, 2023.
- Bouallègue et al. (2024)Bouallègue, Z. B., Clare, M. C. A., Magnusson, L., Gascón, E., Maier-Gerber,
M., Janoušek, M., Rodwell, M., Pinault, F., Dramsch, J. S., Lang, S. T. K.,
Raoult, B., Rabier, F., Chevallier, M., Sandu, I., Dueben, P., Chantry, M.,
and Pappenberger, F.: The Rise of Data-Driven Weather Forecasting: A First
Statistical Assessment of Machine Learning–Based Weather Forecasts in an
Operational-Like Context, Bulletin of the American Meteorological Society,
105, E864 – E883,10.1175/BAMS-D-23-0162.1, 2024.
- Bouttier and Marchal (2024)Bouttier, F. and Marchal, H.: Probabilistic short-range forecasts of
high-precipitation events: optimal decision thresholds and predictability
limits, Natural Hazards and Earth System Sciences, 24, 2793–2816,10.5194/nhess-24-2793-2024, 2024.
- Cho et al. (2004)Cho, H.-K., Bowman, K. P., and North, G. R.: A comparison of gamma and
lognormal distributions for characterizing satellite rain rates from the
tropical rainfall measuring mission, Journal of Applied meteorology, 43,
1586–1597, 2004.
- Coles et al. (2001)Coles, S., Bawa, J., Trenner, L., and Dorazio, P.: An introduction to
statistical modeling of extreme values, vol. 208, Springer, 2001.
- Dutot et al. (2007)Dutot, A.-L., Rynkiewicz, J., Steiner, F. E., and Rude, J.: A 24-h forecast of
ozone peaks and exceedance levels using neural classifiers and weather
predictions, Environmental Modelling & Software, 22, 1261–1269, 2007.
- Espeholt et al. (2022)Espeholt, L., Agrawal, S., Sønderby, C., Kumar, M., Heek, J., Bromberg, C.,
Gazen, C., Carver, R., Andrychowicz, M., Hickey, J., et al.: Deep learning
for twelve hour precipitation forecasts, Nature communications, 13, 5145,
2022.
- Friederichs and Thorarinsdottir (2012)Friederichs, P. and Thorarinsdottir, T. L.: Forecast verification for extreme
value distributions with an application to probabilistic peak wind
prediction, Environmetrics, 23, 579–594, 2012.
- Frisch (1995)Frisch, U.: Turbulence. The legacy of AN Kolmogorov, Turbulence. The legacy of
AN Kolmogorov, 1995.
- Glahn and Lowry (1972)Glahn, H. R. and Lowry, D. A.: The use of model output statistics (MOS) in
objective weather forecasting, Journal of Applied Meteorology and
Climatology, 11, 1203–1211, 1972.
- Gneiting and Katzfuss (2014)Gneiting, T. and Katzfuss, M.: Probabilistic forecasting, Annual Review of
Statistics and Its Application, 1, 125–151, 2014.
- Gneiting et al. (2005)Gneiting, T., Raftery, A. E., III, A. H. W., and Goldman, T.: Calibrated
Probabilistic Forecasting Using EMOS and Minimum CRPS Estimation, Monthly
Weather Review, 133, 1098–1118,10.1175/MWR2904.1, 2005.
- Gneiting et al. (2006)Gneiting, T., Larson, K., Westrick, K., Genton, M. G., and Aldrich, E.:
Calibrated probabilistic forecasting at the stateline wind energy center: The
regime-switching space–time method, Journal of the American Statistical
Association, 101, 968–979, 2006.
- Hess (2020)Hess, R.: Statistical postprocessing of ensemble forecasts for severe weather
at Deutscher Wetterdienst, Nonlinear Processes in Geophysics, 27, 473–487,
2020.
- Jolliffe (2004)Jolliffe, I. T., ed.: Forecast verification: a practitioner’s guide in
atmospheric science, Wiley, Chichester, repr edn., ISBN 978-0-471-49759-2,
2004.
- Kaur et al. (2023)Kaur, J., Parmar, K. S., and Singh, S.: Autoregressive models in environmental
forecasting time series: a theoretical and application review, Environmental
Science and Pollution Research, 30, 19 617–19 641, 2023.
- Kedem et al. (1990)Kedem, B., Chiu, L. S., and North, G. R.: Estimation of mean rain rate:
Application to satellite observations, Journal of Geophysical Research:
Atmospheres, 95, 1965–1972, 1990.
- Lagerquist et al. (2017)Lagerquist, R., McGovern, A., and Smith, T.: Machine learning for real-time
prediction of damaging straight-line convective wind, Weather and
Forecasting, 32, 2175–2193, 2017.
- Lam et al. (2023)Lam, R., Sanchez-Gonzalez, A., Willson, M., Wirnsberger, P., Fortunato, M.,
Alet, F., Ravuri, S., Ewalds, T., Eaton-Rosen, Z., Hu, W., Merose, A., Hoyer,
S., Battaglia, P., Vinyals, O., Stott, D., Pritzel, A., Kavukcuoglu, K., and
Brandstetter, J.: GraphCast: Learning skillful medium-range global weather
forecasting, Science, 382, 1416–1421,10.1126/science.adi2336, 2023.
- Larvor and Berthomier (2021)Larvor, G. and Berthomier, L.: Meteonet: An open reference weather dataset for
ai by météo-france, in: American Meteorological Society Meeting
Abstracts, vol. 101, pp. 1–ii, 2021.
- Lerch et al. (2017)Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., and Gneiting, T.:
Forecaster’s dilemma: extreme events and forecast evaluation, Statistical
Science, pp. 106–127, 2017.
- Leutbecher and Palmer (2008)Leutbecher, M. and Palmer, T. N.: Ensemble forecasting, Journal of
Computational Physics, 227, 3515–3539,10.1016/j.jcp.2007.02.014,
2008.
- Lorenz (1963)Lorenz, E. N.: Deterministic Nonperiodic Flow, Journal of the Atmospheric
Sciences, 20, 130–141,10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2,
1963.
- Marra et al. (2023)Marra, F., Amponsah, W., and Papalexiou, S. M.: Non-asymptotic Weibull tails
explain the statistics of extreme daily precipitation, Advances in Water
Resources, 173, 104 388, 2023.
- Mason (1979)Mason, I.: On reducing probability forecasts to yes/no forecasts, Monthly
Weather Review, 107, 207–211, 1979.
- McGovern et al. (2017)McGovern, A., Elmore, K. L., Gagne, D. J., Haupt, S. E., Karstens, C. D.,
Lagerquist, R., Smith, T., and Williams, J. K.: Using artificial intelligence
to improve real-time decision-making for high-impact weather, Bulletin of the
American Meteorological Society, 98, 2073–2090, 2017.
- Meinshausen and Ridgeway (2006)Meinshausen, N. and Ridgeway, G.: Quantile regression forests., Journal of
machine learning research, 7, 2006.
- Murphy (1973)Murphy, A. H.: A new vector partition of the probability score, Journal of
Applied Meteorology, 12, 595–600,10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2, 1973.
- Muzy and Baggio (2026)Muzy, J.-F. and Baggio, R.: saphir_predict,10.5281/zenodo.20327672,
2026.
- Olivera and Heard (2019)Olivera, S. and Heard, C.: Increases in the extreme rainfall events: Using the
Weibull distribution, Environmetrics, 30, e2532, 2019.
- Pang et al. (2019)Pang, G., He, J., Huang, Y., and Zhang, L.: A binary logistic regression model
for severe convective weather with numerical model data, Advances in
Meteorology, 2019, 6127 281, 2019.
- Park et al. (2022)Park, Y., Maddix, D., Aubet, F.-X., Kan, K., Gasthaus, J., and Wang, Y.:
Learning quantile functions without quantile crossing for distribution-free
time series forecasting, in: International conference on artificial
intelligence and statistics, pp. 8127–8150, PMLR, 2022.
- Pathak et al. (2024)Pathak, J., Subramanian, S., Harrington, P., Raja, S., Chattopadhyay, A.,
Mardani, M., Kurth, T., Hall, D., Li, Z., Azizzadenesheli, K., Hassanzadeh,
P., Kashinath, K., and Anand, A.: FourCastNet: Accelerating global
high-resolution weather forecasting using adaptive Fourier neural operators,
npj Climate and Atmospheric Science, 7, 245,10.1038/s41612-024-00834-8, 2024.
- Pic et al. (2025)Pic, R., Dombry, C., Naveau, P., and Taillardat, M.: Distributional regression
u-nets for the postprocessing of precipitation ensemble forecasts, Artificial
Intelligence for the Earth Systems, 4, 240 067, 2025.
- Pujol et al. (2025)Pujol, K., Baggio, R., Lambert, D., Muzy, J.-F., Filippi, J.-B., and Pantillon,
F.: Improving prediction of heavy rainfall in the Mediterranean with Neural
Networks using both observation and Numerical Weather Prediction data, arXiv
preprint arXiv:2503.24216, 2025.
- Rasp and Lerch (2018)Rasp, S. and Lerch, S.: Neural networks for postprocessing ensemble weather
forecasts, Monthly Weather Review, 146, 3885–3900, 2018.
- Ravuri et al. (2021)Ravuri, S., Lenc, K., Willson, M., Kangin, D., Lam, R., Mirowski, P.,
Fitzsimons, M., Athanassiadou, M., Kashem, S., Madge, S., Prudden, R.,
Mandhane, A. S., Clark, A., Brock, A., Simonyan, K., Hadsell, R., Robinson,
N., Clancy, E., Arenas, A., and Pritzel, A.: Skilful precipitation nowcasting
using deep generative models of radar, Nature, 597, 672–677,10.1038/s41586-021-03854-z, 2021.
- Salinas et al. (2020)Salinas, D., Flunkert, V., Gasthaus, J., and Januschowski, T.: DeepAR:
Probabilistic forecasting with autoregressive recurrent networks,
International journal of forecasting, 36, 1181–1191, 2020.
- Schaumann et al. (2021)Schaumann, P., Hess, R., Rempel, M., Blahak, U., and Schmidt, V.: A calibrated
and consistent combination of probabilistic forecasts for the exceedance of
several precipitation thresholds using neural networks, Weather and
Forecasting, 36, 1079–1096, 2021.
- Schlosser et al. (2019)Schlosser, L., Hothorn, T., Stauffer, R., and Zeileis, A.: Distributional
regression forests for probabilistic precipitation forecasting in complex
terrain, The Annals of Applied Statistics, 13, 1564–1589,10.1214/19-AOAS1247, 2019.
- Schultz et al. (2021)Schultz, M. G., Betancourt, C., Gong, B., Kleinert, F., Langguth, M., Leufen,
L. H., Mozaffari, A., and Stadtler, S.: Can deep learning beat numerical
weather prediction?, Philosophical Transactions of the Royal Society A, 379,
20200 097,10.1098/rsta.2020.0097, 2021.
- Seity et al. (2011)Seity, Y., Brousseau, P., Malardel, S., Hello, G., Bénard, P., Bouttier, F.,
Lac, C., and Masson, V.: The AROME-France Convective-Scale Operational Model,
Monthly Weather Review, 139, 976 – 991,10.1175/2010MWR3425.1, 2011.
- Seneviratne et al. (2023)Seneviratne, S. I., Zhang, X., Adnan, M., Badi, W., Dereczynski, C., Di Luca,
A., et al.: Weather and Climate Extreme Events in a Changing Climate, p.
1513–1766, Cambridge University Press, 2023.
- Sønderby et al. (2020)Sønderby, C. K., Espeholt, L., Heek, J., Dehghani, M., Oliver, A., Salimans,
T., Agrawal, S., Hickey, J., and Kalchbrenner, N.: Metnet: A neural weather
model for precipitation forecasting, arXiv preprint arXiv:2003.12140, 2020.
- Sukrutha et al. (2018)Sukrutha, A., Dyuthi, S. R., and Desai, S.: Multimodel response assessment for
monthly rainfall distribution in some selected Indian cities using best-fit
probability as a tool, Applied Water Science, 8,10.1007/s13201-018-0789-4, 2018.
- Taillardat et al. (2016)Taillardat, M., Mestre, O., Zamo, M., and Naveau, P.: Calibrated ensemble
forecasts using quantile regression forests and ensemble model output
statistics, Monthly Weather Review, 144, 2375–2393, 2016.
- Tascikaraoglu and Uzunoglu (2014)Tascikaraoglu, A. and Uzunoglu, M.: A review of combined approaches for
prediction of short-term wind speed and power, Renewable and Sustainable
Energy Reviews, 34, 243–254, 2014.
- Vaart (1998)Vaart, A. W. v. d.: Asymptotic Statistics, Cambridge Series in Statistical and
Probabilistic Mathematics, Cambridge University Press, 1998.
- Wilks (1989)Wilks, D. S.: Rainfall intensity, the Weibull distribution, and estimation of
daily surface runoff, Journal of Applied Meteorology and Climatology, 28,
52–58, 1989.
- Wilks (2009)Wilks, D. S.: Extending logistic regression to provide
full-probability-distribution MOS forecasts, Meteorological Applications: A
journal of forecasting, practical applications, training techniques and
modelling, 16, 361–368, 2009.
- Wilks (2011)Wilks, D. S.: Statistical methods in the atmospheric sciences, vol. 100,
Academic press, 2011.

## 


- 


Major funding support from
