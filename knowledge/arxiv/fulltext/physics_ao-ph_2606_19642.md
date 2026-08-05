# Rigorous uncertainty quantification of probabilistic AI weather forecasts with conformal prediction

**arXiv ID**: 2606.19642v1
**Authors**: Anna Asch, Raphael Rossellini, Pedram Hassanzadeh, Rebecca Willett
**Published**: 2026-06-17
**Categories**: physics.ao-ph, stat.AP, stat.ML
**HTML URL**: https://arxiv.org/html/2606.19642v1

## Abstract

Probabilistic weather forecasting is undergoing rapid transformation with artificial intelligence (AI). In traditional numerical weather prediction, computing power can limit how well ensemble forecasts approximate the unknown statistical distribution of future states. AI models facilitate larger ensembles and are trained with probabilistic considerations, ideally leading to better uncertainty quantification. Forecasts from these state-of-the-art models are often considered well-calibrated. However, here we show that the statistical coverage of such models, the ultimate measure of calibration, can struggle, especially on extreme events. To address this shortcoming, we employ conformal prediction, a class of statistical methods that mathematically guarantees coverage under no distributional assumptions, unlike previous post-processing techniques. We apply online conformal prediction to temperature and precipitation forecasts (including extremes) of three leading global weather models, GenCast, NeuralGCM, and AIFS-ENS, ensuring calibrated uncertainty at no expense to other probabilistic metrics. This post-processing method can be applied to any forecasting model.

## Full Text

Rigorous uncertainty quantification of probabilistic AI weather forecasts with conformal prediction

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.19642v1 [physics.ao-ph] 17 Jun 2026

¡#1¿[#2]#\@BBOP#1\@BAP#3\@BBN#2\@BBCP

## Rigorous uncertainty quantification of probabilistic AI weather forecasts with conformal predictionAnna AschCorresponding author. Email:aasch@uchicago.eduCommittee on Computational and Applied Mathematics, University of ChicagoRaphael RosselliniDepartment of Statistics, University of ChicagoPedram HassanzadehCommittee on Computational and Applied Mathematics, University of ChicagoDepartment of the Geophysical Sciences, University of ChicagoRebecca WillettCommittee on Computational and Applied Mathematics, University of ChicagoDepartment of Statistics, University of ChicagoDepartment of Computer Science, University of Chicago

## Abstract

Probabilistic weather forecasting is undergoing rapid transformation with artificial intelligence (AI). In traditional numerical weather prediction, computing power can limit how well ensemble forecasts approximate the unknown statistical distribution of future states. AI models facilitate larger ensembles and are trained with probabilistic considerations, ideally leading to better uncertainty quantification. Forecasts from these state-of-the-art models are often considered well-calibrated. However, here we show that thestatistical coverageof such models, the ultimate measure of calibration, can struggle, especially on extreme events. To address this shortcoming, we employ conformal prediction, a class of statistical methods that mathematically guarantees coverage under no distributional assumptions, unlike previous post-processing techniques. We apply online conformal prediction to temperature and precipitation forecasts (including extremes) of three leading global weather models, GenCast, NeuralGCM, and AIFS-ENS, ensuring calibrated uncertainty at no expense to other probabilistic metrics. This post-processing method can be applied to any forecasting model.

## 1Introduction

Ensemble weather predictions are an essential product of operational forecasting centers. Errors from imperfect observations, data assimilation, and predictive models are amplified by the inherent chaos and multi-scale nature of the global weather system, necessitating forecasts that specify a distribution over future states(; ?, ?, ?). But at the heart of probabilistic forecasting is the need for correct uncertainty quantification (UQ). In traditional numerical weather prediction (NWP), empirical distributions are constructed by propagating an ensemble with carefully designed initial condition perturbations through a model(?, ?, ?, ?). Recent models also incorporate stochastic physics schemes(?, ?). Still, inevitable initial condition and modeling errors prevent the forecast distribution from matching the true, unknown distribution of future weather states(?, ?).

A new generation of weather forecasting models, based entirely or partially on AI, improves upon NWP skill at a fraction of the real-time computational cost(?, ?, ?, ?, ?). Fast inference enables larger ensembles and probabilistic objectives shape the architecture and training, ideally leading to better UQ. However, ensemble creation approaches are largely ad hoc; methods include sampling from a conditional diffusion model(?, ?, ?), evolving flow-dependent perturbations in a learned latent space(?, ?), and using traditional methods like bred vectors(?, ?). To improve the quality of ensemble generation in AI-based probabilistic forecasting, practitioners have recently begun incorporating the continuous ranked probability score (CRPS) into training objectives(?, ?) (probabilistic metrics are defined in Section S1). The CRPS is strictly proper—it is optimized when the distribution represented by the probabilistic forecaster is the same as the distribution underlying the training data(?, ?). Because of this characterization, CRPS-trained models are generally considered to produce probabilistic forecasts that accurately represent the underlying data distribution, and evaluation studies based on the CRPS, spread-skill ratio (SSR), and rank histogram have supported this interpretation(?, ?, ?).

In this paper, we examine the calibration of probabilistic weather forecasts. A forecast has correct “statistical coverage” if the actual weather falls within its predicted range as often as the model claims it will. For instance, if a model produces90%90\%temperature prediction intervals, the observed temperature should fall within those bounds90%90\%of the time. A calibrated model is defined as one that achieves the correct coverage for all forecast intervals simultaneously, i.e., exhibits the correct reliability diagram(?, ?). Calibration is an important property for socio-economic decision making; for instance, in agricultural applications, falsely confident forecasts of the likelihood of rainfall can cause significant harm(?, ?, ?). Probabilistic models may have good CRPS or SSR values but still fail to be calibrated(?, ?).

To improve calibration, one can post-process forecasts. A classic technique is the ensemble model output statistics (EMOS) method, which quantifies uncertainty via a Gaussian distribution, with parameters depending on the ensemble mean and variance. Variants fit a non-Gaussian distribution(?, ?), or learn a nonlinear relationship between the covariates and Gaussian parameters via a parameterized neural network(?, ?, ?). To avoid parametric assumptions on the true distribution, several nonparametric methods have been proposed(?, ?, ?, ?, ?). Recent work indicates that post-processing methods, such as model blending, can improve the statistical properties of the ensembles produced by AI weather models(?, ?, ?, ?).

None of the aforementioned post-processing methods come with statistical coverage guarantees. Recent advancements in conformal prediction have produced online methods that adapt to distribution shifts and yieldguaranteedcalibration, under no distributional assumptions. To the best of our knowledge, no other study has applied online conformal prediction to ensemble weather forecasts, and, in general, conformal prediction has seen little use in meteorology. Existing work applying conformal prediction to weather forecasts either constructed intervals around point estimates(?, ?) or worked with fixed adjustments that could not adapt to non-stationarity(?, ?). Other use of conformal prediction has thus far been for specific downstream tasks, such as estimating photovoltaic power(?, ?), forecasting tropical cyclones(?, ?, ?), estimating short-term wind speed(?, ?), and sub-grid-scale parameterizations(?, ?).

In this paper, we quantify the statistical coverage of several state-of-the-art probabilistic AI forecasting models on near-surface temperature and precipitation, showing that the outputs are uncalibrated, especially for extremes. We then apply a specific conformal prediction method, adaptive conformal prediction, as an online post-processing correction to forecast intervals, as visualized in Figure1and described in Section2. Our analysis in Section3shows that this method greatly improves forecast calibration with no lost skill in the CRPS and SSR. We discuss limitations and ways to further improve the method in Section4.

## 2Methods

We use online conformal prediction to provide statistical coverage guarantees for probabilistic weather forecasts. At forecast initialization timett, letXt∈ℝdX_{t}\in\mathbb{R}^{d}denote the atmospheric initial conditions, andYt+τ∈ℝY_{t+\tau}\in\mathbb{R}the true scalar quantity to be predicted at lead timeτ\tau, such as22m temperature at a particular grid point. Letα∈(0,1)\alpha\in(0,1)denote a miscoverage rate, so that1−α1-\alphais the desired coverage rate. From an ensemble forecast, we extract lower and upper ensemble quantiles, denotedq^lo​(Xt)\hat{q}_{\rm lo}(X_{t})andq^hi​(Xt)\hat{q}_{\rm hi}(X_{t}). For a target coverage level of90%90\%(α=0.1\alpha=0.1), these correspond to the empirical 5th and 95th percentiles of the ensemble. Our goal is to modify these raw quantiles so that, over a sequence of forecasts at timest=1,…,Tt=1,\ldots,T,1T​∑t=1T𝟏​{Yt+τ∈C^t​(Xt)}≈1−α,\frac{1}{T}\sum_{t=1}^{T}\mathbf{1}\{Y_{t+\tau}\in\hat{C}_{t}(X_{t})\}\approx 1-\alpha,(1)

whereC^t​(Xt)=[q^lo​(Xt),q^hi​(Xt)]\hat{C}_{t}(X_{t})=[\hat{q}_{\rm lo}(X_{t}),\hat{q}_{\rm hi}(X_{t})]is a prediction interval using information available at timett, and𝟏\mathbf{1}is the indicator function. In words, the fraction of forecasts whose prediction intervals contain the truth should approach the desired coverage level.Figure 1:Schematic of the online adaptive conformal prediction framework for ensemble weather forecasts. We show55-day probabilistic prediction of22m temperature at a target coverage level of90%90\%(α=0.1\alpha=0.1). a) We produce an ensemble55-day forecast of the global atmospheric state. b) From this global forecast, we extract the ensemble forecast at one location and for one variable (“Histogram ofMMraw ensemble forecasts”). The ensemble members are samples from a distribution that approximates the unknown “true conditional distribution” of the weather. Typically, there is a difference between the true and forecast55th percentiles (same for the9595th percentiles); our goal is to correct the forecast percentiles over time using observations. We make a conformalized forecast by subtractingctc_{t}from the forecast55th percentile and addingctc_{t}to the forecast9595th percentile. c) After55days, we observe whether the truth lies inside or outside of the conformalized interval. We updatect+5c_{t+5}, which is the size of the conformal adjustment for the forecast to be issued at timet+5t+5. d) Example time series showing the raw ensemble forecast quantiles, the conformalized forecast quantiles, and ground truth over several weeks of20232023near Chicago (including a heat wave). The size of the conformal adjustment changes over time. The adjoining histogram shows how the ensemble forecasts from panels (b) and (c) are integrated in the online framework.

## 2.1Online Conformal Prediction

We explain an online conformal prediction procedure from? (?) that tracks how much to expand or contract the raw ensemble intervals over time. Figure1visualizes the method. At each forecast timett, we form the conformalized prediction intervalC^t​(Xt)=[q^lo​(Xt)−ct,q^hi​(Xt)+ct].\hat{C}_{t}(X_{t})=\left[\hat{q}_{\rm lo}(X_{t})-c_{t},\,\hat{q}_{\rm hi}(X_{t})+c_{t}\right].(2)

Herectc_{t}is a time-varying padding term in the same physical units as the predicted variable,Yt+τY_{t+\tau}. Ifct>0c_{t}>0, the interval is widened relative to the raw ensemble interval; ifct<0c_{t}<0, it is narrowed. Thus, rather than assuming that the raw ensemble quantiles yield perfect coverage, we learn a correction that adapts as forecast errors are observed.

After the lead time has elapsed, we observe whether the true value fell inside the interval. We defineerrt=𝟏​{Yt+τ∉C^t​(Xt)},\mathrm{err}_{t}=\mathbf{1}\{Y_{t+\tau}\notin\hat{C}_{t}(X_{t})\},(3)

so thaterrt=1\mathrm{err}_{t}=1when the interval misses the truth anderrt=0\mathrm{err}_{t}=0when it contains the truth. The padding is then updated according toct+τ=ct+τ−1+η​(errt−α),c_{t+\tau}=c_{t+\tau-1}+\eta(\mathrm{err}_{t}-\alpha),(4)

where the step size parameterη>0\eta>0controls how quickly the conformal correction responds to recent forecast performance. For the55-day forecasts shown schematically in Figure1, this update isct+5=ct+4+η​(errt−α).c_{t+5}=c_{t+4}+\eta(\mathrm{err}_{t}-\alpha).This update differs from? (?) in that it reflects the operational timing of the forecast: the outcome for the forecast issued on dayttis not known until dayt+5t+5, so the update can only affect forecasts issued after that verification time. The update usesct+4c_{t+4}, the most recent padding value available, before incorporating the newly verified forecast. We prove convergence in Section S2.2.

This rule has an intuitive interpretation. If the interval misses the truth, thenerrt=1\mathrm{err}_{t}=1, and the padding increases byη​(1−α)\eta(1-\alpha), making future intervals more conservative. If the interval contains the truth, thenerrt=0\mathrm{err}_{t}=0, and the padding decreases byη​α\eta\alpha, making future intervals less conservative. For a90%90\%interval,α=0.1\alpha=0.1: a miss increasesctc_{t}by0.9​η0.9\eta, while a successful coverage event decreases it by0.1​η0.1\eta. Thus one miss is balanced by nine successful coverage events, matching the desired10%10\%miscoverage rate.

The coverage guarantee follows directly from this adaptive update. Summing the update overTTverified forecasts gives1T​∑t=1Terrt=α+cT+τ−cτη​T.\frac{1}{T}\sum_{t=1}^{T}\mathrm{err}_{t}=\alpha+\frac{c_{T+\tau}-c_{\tau}}{\eta T}.(5)

The second term describes how the empirical miscoverage rate differs from the intended rateα\alpha. It approaches0asT→∞T\rightarrow\infty, provided thesectc_{t}terms are bounded, which is true ifYYis bounded. In such cases, the empirical miscoverage rate converges toα\alpha. This is the adaptive conformal guarantee: if the original ensemble intervals are too narrow or too wide, the conformalized intervals adjust online toward the target coverage level(?, ?). In practice, the step sizeη\etacontrols a tradeoff between stability and responsiveness. Smaller values produce gradual changes in intervals, while larger values allow quicker reaction to changing forecast skill and faster convergence, but possibly at the expense of stability. We discuss the role ofTTin the Results, but note that empirical convergence to the target miscoverage rate occurs within days or weeks.

We employ the procedure separately for each lead time, variable, and grid point. In Section S2, we detail how we apply online conformal in our setting. We mirror the approach of? (?), which does the adaptation in quantile space instead of variable space. This framework is more easily deployed across many locations in parallel, because the step size is dimensionless; updates become neutral to the climatology of the region.

## 2.2Ensemble Model Output Statistics

We also implement a post-processing baseline, the ensemble model output statistics (EMOS) method of? (?). For temperature, we fit Gaussian distributions; for precipitation, we implement the left-censored generalized extreme value distribution and other modifications discussed in? (?) to account for non-Gaussianity and the possibility of a point mass at0. Implementation details are in Section S2.3.

## 2.3Models and Data

Conformal prediction is agnostic to the model that produces the original quantilesq^lo\hat{q}_{\rm lo}andq^hi\hat{q}_{\rm hi}: NWP, AI, or any other forecasting method could be used. Here, we evaluate our method on three state-of-the-art probabilistic weather forecasting models, two AI-based (GenCast and AIFS-ENS) and one hybrid (NeuralGCM), each of which produce ensemble forecasts(?, ?, ?, ?).

GenCast is a conditional diffusion model that transforms Gaussian noise into a forecast. Depending on the year, we have5252or5656ensemble members. AIFS-CRPS is a transformer-based model, trained with a CRPS-based loss. We use AIFS-ENS, a version fine-tuned on operational Integrated Forecasting System data, and generate 25 ensemble members. NeuralGCM, which has a dynamical core and machine-learned closures, has a stochastic version(?, ?) fine-tuned to match satellite-based precipitation observations from the Integrated Multi-satellitE Retrievals for GPM (IMERG) dataset(?, ?). We generate5151ensemble members. For each model, we estimate quantiles by linearly interpolating between ensemble members. As ground truth, we take the ERA5 reanalysis dataset on which these models were trained(?, ?). The only exception is NeuralGCM precipitation, for which we use IMERG. See Section S3 for further details.

In the Results, we also evaluate the performance on extremes. To define extremes, we select as a threshold the 95th percentile of climatology, calculated for each spatial location and calendar date from ERA5 reanalysis data spanning 1979–2018 (except for NeuralGCM precipitation, for which we use IMERG data from 2000–2018). The coverage on extremes is a type of conditional coverage, and the theoretical guarantee doesnothold in this setting(?, ?).

## 3Results

For each AI model, we evaluate globally on1212-hour total precipitation and near-surface temperature (two-meter temperature for GenCast and AIFS-ENS, and temperature at10001000hPa for NeuralGCM). We calibrate each model at many differentα\alphalevels to improve the entire forecast distribution.

We first consider a lead time ofτ=5\tau=5days andα=0.1\alpha=0.1(90%90\%coverage). For each variable and grid point (indexed byii), we report the fraction of verification times without a miss as the empirical coverage:coveragei=1T​∑t=1T(1−erri,t),{\rm coverage}_{i}=\frac{1}{T}\sum_{t=1}^{T}(1-{\rm err}_{i,t}),(6)

wherettindexes the forecast dates available over the test period from20222022to20242024. Here, a perfectly calibrated forecast would have empirical coverage of90%90\%.

We calculate the empirical coverage for the original ensemble and the conformalized forecast intervals, and then quantify the coverage gain resulting from conformal prediction with the following value, which we call percentage point improvement (ppi):ppii:=|raw​ensemble​coveragei−0.9|−|conformalized​coveragei−0.9|.{\rm ppi}_{i}:=\left|{\rm raw\ ensemble\ coverage}_{i}-0.9\right|-\left|{\rm conformalized\ coverage}_{i}-0.9\right|.(7)

Starting with near-surface temperature, the left of Figure2a shows the global spatial distribution of these values over the test period. The right is the same, but only for days for which the truth exceeded the 95th percentile of climatology, as defined above.
Figure3a is the same, but for total precipitation.Figure 2:a) Left: Spatial map of coverage improvement on near-surface temperature at a target level of90%90\%, averaged over the test period from20222022–20242024. Values are reported in percentage point improvement (ppi), as defined in Equation (7). We track independentctc_{t}values for each grid point. Blue indicates regions where the conformal adjustment improves coverage. The number in the lower left-hand corner is the area-weighted global average ppi. In parentheses is how the area-weighted global average empirical coverage changed between the original and conformalized models. (Their difference may not equal the average ppi because the global average does not commute with the absolute values in Equation (7).) Right: The same, but conditioned on the ground truth being extreme—above the 95th percentile of climatology for the given location and calendar date. Gray hatching indicates locations where 10 or fewer days exceeded the threshold over the test period. Hatching differences across models are due to differences in spatial or temporal resolution. b) Left: Spatial map of the empirical coverage of the original ensemble forecasts. The number in the lower left-hand corner is the area-weighted global average coverage. Right: The same, but conditioned on the ground truth being extreme.Figure 3:The same as Figure2, but for total precipitation.

Conformal prediction improves coverage in almost all cases, as the vast majority of grid points are blue. To understand the spatial variability, we turn to Figures2b and3b, which plot the empirical coverage values (Equation (6)) of the raw forecasting models. Grid points for which there is little gain due to conformalization correspond well with those for which the original forecast already achieved good coverage. Then Figures S1 and S2 show that, on average, the conformalized forecasts achieve the desired marginal coverage almost exactly, as expected due to the convergence guarantee in Section2.1. In practice, convergence to within0.010.01of the target coverage rate occurs within days, and to within0.0010.001after about a month.
There are grid points for which there remains over-coverage in Figure S2, e.g., NeuralGCM over Antarctica. The original55th and9595th percentiles and ground truth are often all0, so we cannot decrease coverage without sometimes outputting empty prediction intervals (i.e.,C^t​(Xt)=∅\hat{C}_{t}(X_{t})=\emptyset), which we decide not to do.

Next we discuss the spatial variability of coverage. As examples seen in Figures2and3, forecasts are improved greatly for NeuralGCM total precipitation over the Sahara, GenCast 2m temperature over the Andes and India, and AIFS-ENS 2m temperature over central Africa. Also, the original coverage on near-surface temperature is better over the ocean than the land for GenCast, the opposite is true for NeuralGCM, and the coverage is similar over land and ocean for AIFS-ENS. It is worthwhile to further explore the regional deficiencies of different models, as globally averaged metrics fail to capture spatial heterogeneity in model skill or calibration. Any relationship between forecast physics and coverage remains to be explored.

Turning to the results for extremes (above the 95th percentile; Section2.3), we note that the raw forecast coverage is uniformly worse on extremes than overall (compare the left and right columns in Figures2b and3b). The spatial distribution of forecast coverage also differs. The reduced quality of the raw ensemble quantiles on extremes can allow conformalization to lend greater improvement on extremes than typical weather, especially noticeable in, for example, NeuralGCM’s near-surface temperature. While in all examples the globally averaged coverage on extremes improves after conformalization, there is room for further improvement, as seen on the right-hand side of Figures S1 and S2, especially for precipitation extremes.

The results thus far focus onα=0.1\alpha=0.1andτ=5\tau=5days, but, as shown in the reliability diagram in Figure4, we also achieve the desired coverage across different target levels and lead times. In most cases the original ensembles undercover, but sometimes they overcover (e.g., NeuralGCM’s total precipitation at target coverage below90%90\%); conformal prediction corrects both. In Figure4, we also compare against a baseline, EMOS, which generally improves calibration. But as conformal prediction comes with a statistical coverage guarantee, it produces near-perfect reliability diagrams. Additionally, the insets show that the method works across lead times from11to1515days.Figure 4:Reliability diagram showing coverage across different target levels at a lead time ofτ=5\tau=5days, including a comparison against the EMOS baseline (see Section2.2). Each point plots a specified target coverage level against the area-weighted globally averaged coverage over the test period,20222022–20242024. The black dashed line indicates a perfect model, red the original model, gold the EMOS-adjusted intervals, and blue the conformalized intervals. The conformalized predictions have reliability lines closely aligned with that of the perfect model. The inset panels show coverage across various lead timesτ\tauat the90%90\%target coverage level.

Better coverage might be achieved at the cost of unreasonable increases to the interval width. However, we demonstrate that this is not the case: the CRPS and SSR are improved or barely affected. See Section S1 for definitions of these metrics and how we adapt them to quantile-based forecasts(?, ?). Figure S3 shows that the SSR generally improves after conformalization, and Figure S4 shows that the CRPS remains almost unchanged. So, when conformal prediction increases the widths of prediction intervals, it is in a principled way—if the interval was not wide enough before.

## 4Summary and Conclusions

In this work, we demonstrate that online conformal prediction is an effective calibration step for global weather forecasting. The raw ensemble forecasts of several AI weather models lack calibration—generally producing overly narrow ranges of forecast values, which manifests in lower statistical coverage than desired. We correct the coverage deficiency at all target coverage levels with online conformal prediction, endowing outputs with a statistical guarantee without sacrificing skill on CRPS or SSR. The online framework adds value over traditional conformal prediction because the adjustments,ctc_{t}, can react to distributional changes, like seasonal differences or long-term trends(?, ?).

We also evaluate forecast coverage on rare extreme events. AI models have been shown to struggle to predict extreme events, especially gray swans, for which UQ becomes particularly important(?, ?, ?, ?). Indeed, the models we evaluate do not correctly represent the likelihood of extremes. The conformalized forecasts improve, but do not perfect, coverage of extreme temperature; for extreme precipitation, improvement is marginal. Tracking separate upper and lower conformal corrections(?, ?) would likely help, but is left for future work. More broadly, developing conformal prediction methods tailored for extremes remains an important challenge. A natural first step is to build upon the uncertainty-aware framework developed by? (?).

We use conformal prediction as a post-processing method, and, as a baseline, we take a classic method, EMOS. Newer techniques exist, but operational state-of-the-art post-processing methods in NWP have become highly specialized(?, ?, ?). Methods like these, or EMOS executed after a more robust parameter search, might provide a stronger baseline (though they will still lack statistical guarantees). However, conformal prediction works out-of-the-box and requires little to no parameter tuning. Our experimental verification that it achieves target coverage demonstrates its utility.

Next, we discuss some relevant aspects of the algorithm. Equation (5) guarantees convergence to the desired miscoverage rateα\alphaasT→∞T\rightarrow\infty. Empirically, online conformal improves coverage even for modest values ofTT, corresponding to less than a month. Another important factor is the number of ensemble members present in the original forecast,MM. AsMMincreases, the raw forecast coverage may improve, but even asM→∞M\rightarrow\infty, the empirical forecast distribution still differs from the unknown, ground truth distribution due to structural errors, so we cannot produce well-calibrated forecasts by simply sampling massive ensembles from AI models. Even if the original model is poor, some amount of interval inflation can always recover good coverage, but the intervals will be large. Conformal prediction learns a data-driven correction directly from observed forecast errors, achieving good coverage without naive inflation.

Our implementation of conformal prediction comes with natural limitations. It only corrects the variance; correcting the bias in tandem could further improve performance. Another drawback is that we must fit a different conformal adjustment for each location, lead time, variable, and quantile. On the positive side, this means the computational cost of the real-time update is easily parallelizable and minimal for each—simply computing a quantile and adding and removing a scalar from a small list. However, this breaks spatial covariance and cross-variable interactions. A good avenue of future work could be reintroducing dependence structure; methods in the literature address this(?, ?, ?), but the distribution-free guarantee would be lost.

## Open Research Section

We obtain GenCast forecasts from Google DeepMind’s WeatherNext Gen, which produces forecasts with an operational version of GenCast (seehttps://developers.google.com/earth-engine/datasets/catalog/projects_gcp-public-data-weathernext_assets_126478713_1_0). We generated the forecasts for Google Research’s NeuralGCM (2.8° stochastic precipitation version) and ECMWF’s AIFS-ENS; the model weights are freely available fromhttps://neuralgcm.readthedocs.io/en/latest/checkpoints.htmlandhttps://huggingface.co/ecmwf/aifs-ens-1.0.
ERA5 reanalysis is freely available from the Copernicus Climate Data Store(?, ?, ?).
IMERG data can be accessed fromhttps://doi.org/10.5067/GPM/IMERG/3B-HH/07(?, ?). Code that produces the results in this paper will be provided upon acceptance.

## Conflict of Interest declaration

The authors declare there are no conflicts of interest for this manuscript.

## Acknowledgments

We thank Adam Marchakitus and Bing Gong for helping produce the original forecasts. A.A. is supported by NSF GRFP-2140001. P.H. and R.W. are grateful for support from NSF AGS-2531264 and AFSOR FA9550-24-1-0327, respectively. This work also received support from the University of Chicago’s Data Science Institute, the Institute of Climate and Sustainable Growth, and the Laude Foundation. Computational resources were provided by NSF ACCESS (ATM170020), NCAR’s CISL (UCHI0014), and the University of Chicago Research Computing Center.

## References

Supporting Information


## Contents of this file
- 1.

Texts S1 to S3
- 2.

Figures S1 to S4

## Introduction

Text S1 contains precise definitions of the probabilistic metrics used for evaluation. Text S2 provides algorithmic implementation details for online conformal prediction and the ensemble model output statistics method, as well as a proof that online conformal prediction converges with delayed updating. Text S3 explains technical details of the data used.

## Appendix S1Probabilistic Metrics

First, we spell out notation, following? (?) closely. All notation is for a particular variable and lead time. Letxi,tmx_{i,t}^{m}be the value of themmth ofMMensemble members from initialization timet=1,…,Tt=1,\ldots,Tat grid pointi∈Gi\in G. Letyi,ty_{i,t}be the verifying observation. Letaia_{i}denote the area of theiith grid cell. Two useful derived quantities in the following exposition are the ensemble mean,x¯i,t\overline{x}_{i,t}, and the unbiased sample variance of the ensemble members,si,t2=1M−1​∑m=1M(x¯i,t−xi,tm)2.s_{i,t}^{2}=\frac{1}{M-1}\sum_{m=1}^{M}\left(\overline{x}_{i,t}-x_{i,t}^{m}\right)^{2}.

Standard implementations of probabilistic metrics in weather forecasting rely on an ensemble to characterize the predictive distribution. However, conformal prediction inherently outputs prediction intervals instead of ensemble members. In the following subsections, we also explain how we calculate metrics in this case, which requires running the algorithm at many target miscoverage levelsα\alpha.

## S1.1Continuous-Ranked Probability Score

Fix locationiiand initialization timettand letF​(x)F(x)be the empirical cumulative distribution function (CDF) of the ensemblexi,tmx_{i,t}^{m},m=1,…,Mm=1,\ldots,M. The continuous ranked probability score (CRPS), in the negative orientation(?, ?), is defined asCRPS​(F,yi,t)=∫−∞∞(F​(z)−𝟏​{z≥yi,t})2​𝑑z.\mathrm{CRPS}(F,y_{i,t})=\int_{-\infty}^{\infty}\left(F(z)-\mathbf{1}\{z\geq y_{i,t}\}\right)^{2}\,dz.

This is the squaredL2L^{2}distance between the empirical and actual CDFs, where the actual CDF is a Heaviside function at the value of the verifying observation,yi,ty_{i,t}. We then average this value over all initialization times and grid points under consideration, obtaining the CRPS:CRPS=1T​∑t=1T1|G|​∑iai​CRPS​(F,yi,t).\mathrm{CRPS}=\frac{1}{T}\sum_{t=1}^{T}\frac{1}{|G|}\sum_{i}a_{i}\mathrm{CRPS}(F,y_{i,t}).

When working with quantile forecasts instead of ensemble members, we approximate the integral with a different formula. Following the presentation in? (?), letFFbe the CDF of the forecast andF−1​(α)F^{-1}(\alpha)the quantile forecast at levelα\alpha. Then, with the quantile scoreQSα​(F−1​(α),y)=2​(𝟏​{y≤F−1​(α)}−α)​(F−1​(α)−y)\mathrm{QS}_{\alpha}(F^{-1}(\alpha),y)=2(\mathbf{1}\{y\leq F^{-1}(\alpha)\}-\alpha)(F^{-1}(\alpha)-y),CRPS​(F,yi,t)=∫01QSα​(F−1​(α),yi,t)​𝑑α.\mathrm{CRPS}(F,y_{i,t})=\int_{0}^{1}\mathrm{QS}_{\alpha}(F^{-1}(\alpha),y_{i,t})\,d\alpha.

We discretize this integral with the availableα\alphavalues.

## S1.2Spread-Skill Ratio

The spread-skill ratio compares, roughly, the ensemble spread to average ensemble mean error. The first term to consider is the average ensemble variance,AvgEnsVar=1T​∑t=1T1|G|​∑iai​si,t2,\mathrm{AvgEnsVar}=\frac{1}{T}\sum_{t=1}^{T}\frac{1}{\left|G\right|}\sum_{i}a_{i}s_{i,t}^{2},

and the mean squared error (MSE) of the ensemble mean isEnsMeanMSE=1T​∑t=1T1|G|​∑iai​(x¯i,t−yi,t)2\mathrm{EnsMeanMSE}=\frac{1}{T}\sum_{t=1}^{T}\frac{1}{\left|G\right|}\sum_{i}a_{i}\left(\overline{x}_{i,t}-y_{i,t}\right)^{2}

Some authors bias-correct this term to obtain a fair estimate(?, ?), and we also do this. This bias-corrected value isEnsMeanMSEfair=EnsMeanMSE−AvgEnsVarM.\mathrm{EnsMeanMSE}_{\textrm{fair}}=\mathrm{EnsMeanMSE}-\frac{\mathrm{AvgEnsVar}}{M}.

Then the SSR isSSR=AvgEnsVarEnsMeanMSEfair.{\mathrm{SSR}}=\sqrt{\frac{\mathrm{AvgEnsVar}}{\mathrm{EnsMeanMSE}_{\textrm{fair}}}}.

If the verifying observation is second-order exchangeable with the ensemble members, the SSR equals11in expectation(?, ?). Assuming little bias in the forecast, a forecast that is underdispersive (overdispersive) on average will haveSSR<\mathrm{SSR}<(>>)11.

When working with quantiles instead of ensemble members, we cannot directly estimate the ensemble mean and variance. Instead, we estimate the mean as𝔼​[X]=∫01F−1​(α)​𝑑α\mathbb{E}[X]=\int_{0}^{1}F^{-1}(\alpha)\,d\alphaand the variance asVar​[X]=∫01(F−1​(α)−𝔼​[X])2​𝑑α\mathrm{Var}[X]=\int_{0}^{1}(F^{-1}(\alpha)-\mathbb{E}[X])^{2}\,d\alpha(assuming finite variance).

## Appendix S2Algorithmic Details

## S2.1Online Conformal Prediction

For each model, we use data from20212021–20242024. Forecasts initialized in20212021serve as pure calibration data. Then we step through all forecast initialization dates in20222022–20242024, using the most recent year’s worth of nonconformity scores as the calibration data with which to calculate the conformal adjustment. We set the step sizeη=0.01\eta=0.01, following? (?).

## S2.2Online Conformal Prediction Delayed Updating Proof

Proposition S1.Fixα∈[0,1]\alpha\in[0,1],η>0\eta>0, andτ∈ℕ>0\tau\in\mathbb{N}_{>0}. SupposeYt∈[−b/2,b/2]​∀t≥1Y_{t}\in[-b/2,b/2]\;\;\forall t\geq 1. Suppose we use theτ\tau-step delayed update rulect+τ=ct+τ−1+η​(errt−α),c_{t+\tau}=c_{t+\tau-1}+\eta(\mathrm{err}_{t}-\alpha),

whereerrt=𝟏​{Yt+τ∉[q^lo​(Xt)−ct,q^hi​(Xt)+ct]}\mathrm{err}_{t}=\mathbf{1}\{Y_{t+\tau}\notin[\hat{q}_{\rm lo}(X_{t})-c_{t},\hat{q}_{\rm hi}(X_{t})+c_{t}]\}. Assumeq^lo​(⋅),q^hi​(⋅)∈[−b/2,b/2]\hat{q}_{\rm lo}(\cdot),\hat{q}_{\rm hi}(\cdot)\in[-b/2,b/2]. In the case thatq^lo​(Xt)−ct>q^hi​(Xt)+ct\hat{q}_{\rm lo}(X_{t})-c_{t}>\hat{q}_{\rm hi}(X_{t})+c_{t}, we adopt the convention thaterrt=1\mathrm{err}_{t}=1.

If we initializec1,…,cτ=0c_{1},\dots,c_{\tau}=0, then|1T​∑t=1T(errt−α)|≤b+τ​ηη​T.\left|\frac{1}{T}\sum_{t=1}^{T}(\mathrm{err}_{t}-\alpha)\right|\leq\frac{b+\tau\eta}{\eta T}.

This recovers the guarantee of? (?, Proposition 1), who study the case ofτ=1\tau=1.

Proof.

Observe that1T​∑t=1Tct+τ=1T​∑t=1Tct+τ−1+1T​∑t=1Tη​(errt−α).\frac{1}{T}\sum_{t=1}^{T}c_{t+\tau}=\frac{1}{T}\sum_{t=1}^{T}c_{t+\tau-1}+\frac{1}{T}\sum_{t=1}^{T}\eta(\mathrm{err}_{t}-\alpha).

By cancellation, we get1η​T​(cT+τ−cτ)=1T​∑t=1T(errt−α).\frac{1}{\eta T}(c_{T+\tau}-c_{\tau})=\frac{1}{T}\sum_{t=1}^{T}(\mathrm{err}_{t}-\alpha).

We know thaterrt=0\mathrm{err}_{t}=0ifct≥bc_{t}\geq b, and, similarly,errt=1\mathrm{err}_{t}=1ifct≤−bc_{t}\leq-b, by the boundedness assumption onYY.

We assert that−b−τ​η​α≤ct≤b+τ​η​(1−α)-b-\tau\eta\alpha\leq c_{t}\leq b+\tau\eta(1-\alpha).

The upper bound holds trivially ifct≤bc_{t}\leq b. So we supposect>bc_{t}>b. Letu≤tu\leq trefer to the last time index for whichcu≤bc_{u}\leq b. We know such an index must exist sincec1,…,cτ=0c_{1},\dots,c_{\tau}=0by assumption. For all indicessssuch thatu+τ<s≤tu+\tau<s\leq t, we must havecs−τ>bc_{s-\tau}>b, by the definition ofuu. Therefore,errs−τ=0\mathrm{err}_{s-\tau}=0andcs−cs−1=η​(errs−τ−α)≤0.c_{s}-c_{s-1}=\eta(\mathrm{err}_{s-\tau}-\alpha)\leq 0.

Thus, after timeuu, only the firstτ\tauupdates yield increases. Each such increase is at mostη​(1−α)\eta(1-\alpha). Thereforect≤cu+τ​η​(1−α)≤b+τ​η​(1−α).c_{t}\leq c_{u}+\tau\eta(1-\alpha)\leq b+\tau\eta(1-\alpha).

This proves the upper bound. The lower bound proof follows from an analogous argument.

Using these bounds and the fact thatcτ=0c_{\tau}=0by assumption, we have|1T​∑t=1T(errt−α)|=|1η​T​(cT+τ−cτ)|≤b+τ​ηη​T.\left|\frac{1}{T}\sum_{t=1}^{T}(\mathrm{err}_{t}-\alpha)\right|=\left|\frac{1}{\eta T}(c_{T+\tau}-c_{\tau})\right|\leq\frac{b+\tau\eta}{\eta T}.

## S2.3Ensemble Model Output Statistics

As in the original? (?) paper, we fit the following Gaussian predictive distribution at each grid point:𝒩​(a+b​X¯,c+d​S2),\mathcal{N}\left(a+b\overline{X},c+dS^{2}\right),

whereaa,bb,cc, andddare learned coefficients,X¯\overline{X}is the forecast mean, andS2S^{2}is the forecast variance. We use a single coefficientbbfor the ensemble meanX¯\overline{X}, rather than fitting separate coefficients for each ensemble member, because we work with a single forecasting system with exchangeable ensemble members.

We also implement a precipitation-specific version, the left-censored generalized extreme value (GEV) distribution proposed by? (?). This model characterizes precipitation with a CDF of the formG~​(y)={G​(y),y≥00,y<0,\widetilde{G}(y)=\begin{cases}G(y),&y\geq 0\\
0,&y<0,\end{cases}

whereG​(y)G(y)is the CDF of the GEV distribution,G​(y)={exp⁡[−{1+ξ​(y−μσ)}−1/ξ],ξ≠0exp⁡[−exp⁡{(−y−μσ)}],ξ=0,G(y)=\begin{cases}\exp{\left[-\left\{1+\xi\left(\frac{y-\mu}{\sigma}\right)\right\}^{-1/\xi}\right]},&\xi\neq 0\\
\exp{\left[-\exp\left\{\left(-\frac{y-\mu}{\sigma}\right)\right\}\right]},&\xi=0,\end{cases}

withG​(y):=1G(y):=1forξ<0\xi<0andy>μ−σ/ξy>\mu-\sigma/\xi, andG​(y):=0G(y):=0forξ>0\xi>0andy<μ−σ/ξy<\mu-\sigma/\xi.? (?) restrictsξ∈(−0.278,1)\xi\in(-0.278,1), and over this range, the mean of the GEV distribution ism={μ+σ​Γ​(1−ξ)−1ξ,ξ≠0μ+σ​γ,ξ=0,m=\begin{cases}\mu+\sigma\frac{\Gamma(1-\xi)-1}{\xi},&\xi\neq 0\\
\mu+\sigma\gamma,&\xi=0\end{cases},

whereΓ\Gammais the gamma function andγ\gammais the Euler–Mascheroni constant.

At each grid pointii, letX¯\overline{X}be the forecast mean as before,𝟏X=0¯\overline{\mathbf{1}_{X=0}}be the fraction of ensemble members predicting zero precipitation, andMD​(X)=1M2​∑m,m′|xi,tm−xi,tm′|\mathrm{MD}(X)=\frac{1}{M^{2}}\sum_{m,m^{\prime}}\left|x_{i,t}^{m}-x_{i,t}^{m^{\prime}}\right|be the ensemble mean difference. Then, we connect parametersmim_{i}andσi\sigma_{i}to the ensemble output viami\displaystyle m_{i}=α0+α1⋅X¯+α2⋅𝟏X=0¯\displaystyle=\alpha_{0}+\alpha_{1}\cdot\overline{X}+\alpha_{2}\cdot\overline{\mathbf{1}_{X=0}}(S1)σi\displaystyle\sigma_{i}=β0+β1⋅MD​(X).\displaystyle=\beta_{0}+\beta_{1}\cdot\mathrm{MD}(X).(S2)

The coefficientsα0\alpha_{0},α1\alpha_{1},α2\alpha_{2},β0\beta_{0},β1\beta_{1}, andξ\ximust be estimated at each spatial location. To make the parameter estimation more robust, we implement spatial pooling, at each spatial location expanding the training data to include observations from the surrounding3×33\times 3block of grid points.

In both cases, we estimate the parameters by minimizing the CRPS over the most recent3030days of verified observations.

## Appendix S3Data

GenCast forecasts are initialized daily at 0Z, and we subsample from the native0.25∘0.25^{\circ}grid to a1∘1^{\circ}grid. There are5656ensemble members available for the years20212021,20222022, and20232023, and5252ensemble members for20242024. NeuralGCM forecasts have5151ensemble members at2.8∘2.8^{\circ}resolution. We run the model from initial conditions at 0Z every33days. We generate AIFS-ENS forecasts with2525ensemble members twice weekly, initialized at 0Z, and subsample from the native0.25∘0.25^{\circ}grid to a1∘1^{\circ}grid.

For all models, we use data from20212021–20242024. This time period is completely out of sample for GenCast and NeuralGCM. AIFS-ENS, however, was fine-tuned on operational Integrated Forecasting System analysis data that includes20212021–20232023, so these results are not strictly out of sample.

When we evaluate on “near-surface temperature”, this is22m temperature for GenCast and AIFS-ENS, and temperature at10001000hPa for NeuralGCM (since this model does not have22m temperature). For “precipitation”, we evaluate on total1212-hour accumulated precipitation, for all models.Figure S1:The same as Figure 2b, but for the conformalized forecasts of near-surface temperature.Figure S2:The same as Figure 3b, but for the conformalized forecasts of total precipitation.Figure S3:The SSR as a function of lead time. The conformalized model (solid lines) generally performs better (i.e., has values closer to 1) than the raw ensembles (dashed lines).Figure S4:The CRPS as a function of lead time, in units of the variable (C∘{}^{\circ}\textrm{C}for temperature, andmmfor precipitation). The performance of the raw model (dashed lines) is comparable to that of the conformalized model (solid lines).

## 


- 


Major funding support from
