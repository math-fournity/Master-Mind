# Superstatistical Analysis of PDFs and autocorrelation functions for air pollution concentrations in the UK

**arXiv ID**: 2607.12876v1
**Authors**: Nisal Amarakoon, Hankun He, Christian Beck
**Published**: 2026-07-14
**Categories**: physics.ao-ph, math.DS
**HTML URL**: https://arxiv.org/html/2607.12876v1

## Abstract

Conventional statistical models often struggle to fully capture the complex spatio-temporal dynamics, intermittent fluctuations, and heavy-tailed distributions characteristic of real-world air pollution data. Furthermore, existing literature frequently focuses on extreme events, overlooking the persistence of low-pollution states and temporal memory effects. To address these gaps, we apply superstatistical frameworks from non-equilibrium statistical physics to analyse a comprehensive five-year dataset (2020-2025) of hourly air pollutant concentrations across the United Kingdom. Excellent fits of experimentally measured distributions are obtained from our theoretical models. We observe large heterogeneities of the best fitting parameters depending on the locations where the measurements are performed. These parameters form characteristic patterns in the 3-dimensional parameter space and depend on the type of pollutant considered, as well as on the environmental conditions (high traffic, industrial, or rural surroundings). We also investigate autocorrelation functions and provide evidence for differences in day-time and night-time decays of the autocorrelation function. Our investigation mainly focuses onto the dynamics of NO, NO2, PM2.5, PM10, but we also report on some anomalous distributions observed for O3.

## Full Text

Superstatistical Analysis of PDFs and autocorrelation functions for air pollution concentrations in the UK

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
- License: CC BY 4.0arXiv:2607.12876v1 [physics.ao-ph] 14 Jul 2026

## Superstatistical Analysis of PDFs and autocorrelation functions for air pollution concentrations in the UKNisal Amarakoon1, Hankun He23, Christian Beck1(1\,{}^{1}Centre for Complex Systems, Queen Mary University of London, London E1 4NS, UK
2UK Centre for AI in the Public Sector, London, United Kingdom
3Institute for Connected Communities, University of East London, London E15 4LZ, United Kingdom)

## Abstract

Conventional statistical models often struggle to fully capture the complex spatio-temporal dynamics, intermittent fluctuations, and heavy-tailed distributions characteristic of real-world air pollution data. Furthermore, existing literature frequently focuses on extreme events, overlooking the persistence of low-pollution states and temporal memory effects. To address these gaps, we apply superstatistical frameworks from non-equilibrium statistical physics to analyse a comprehensive five-year dataset (2020–2025) of hourly air pollutant concentrations across the United Kingdom. Excellent fits of experimentally measured distributions are obtained from our theoretical models. We observe large heterogeneities of the best fitting parameters depending on the locations where the measurements are performed. These parameters
form characteristic patterns in the 3-dimensional parameter space and depend on the type of pollutant considered, as well as on the environmental conditions (high traffic, industrial, or rural surroundings). We also investigate autocorrelation functions and provide evidence for differences in day-time and night-time decays of the autocorrelation function. Our investigation mainly focuses onto the dynamics ofN​O,N​O2NO,NO_{2},P​M2.5PM_{2.5},P​M10PM_{10}, but we also report on some anomalous distributions observed forO3O_{3}.

## Impact Statement

Our application paper offers a substantial research contribution at the interface of statistical physics, environmental sciences, geography, and data analytics. It addresses the complex dynamics of air pollution in UK,
analyzing, in particular, the tails of the observed PDFs which describe high-pollution events as well as the low pollution data. Our work enables a
better understanding of the time-varying dynamics of air pollution, which is essential for policy formulation and
the construction of suitable stochastic models, as well as for analyzing the medical consequences of exposure to
polluted air.

## 1Introduction

Air pollution represents one of the most pressing environmental challenges of our time, with far-reaching consequences for human health, ecosystems, and climate systems[1]. Hill emphasizes that “Environmental scientists rely heavily on statistical methods to interpret data, discern patterns, and assess the risks associated with pollutant exposure”[2]. Conventional statistical approaches, while useful for basic analysis, often prove inadequate in characterizing the intricate spatio-temporal patterns and complex distributions observed in real-world pollution data. The field has witnessed significant theoretical advancements through the application of generalized statistical physics principles, particularly through frameworks such as superstatistics[3,4,5,6,7]and nonextensive statistical mechanics[8,9,10]. These methodologies provide robust tools for analysing complex pollution dynamics, including heavy-tailed non-Gaussian probability distributions, long-range correlations, intermittent fluctuations, and region-specific variations that defy traditional modelling assumptions. Our paper here discusses the evolution of air pollution statistical descriptions fromqq-exponential distributions[8]toqq-Gamma formulations, which take into account both high pollution and low-pollution asymptotics, highlighting their respective strengths in addressing different aspects of environmental characteristics. Through careful examination of both theoretical foundations and practical applications, our work underscores how physics-inspired statistical techniques offer superior capabilities for understanding the typical behaviour of pollution probability density functions (PDFs),
allowing for pollution statistical predictions, environmental risk assessment, and evidence-based policy formulation. The integration of these advanced methods into air quality research marks a significant step forward in our ability to understand and mitigate the impacts of the fluctuating aspects of atmospheric pollution.

The quantitative analysis of air pollution statistics began with early applications of parametric probability distributions, illustrated by Marani et al.[11]demonstrating that generalized gamma distributions could effectively model air pollutant concentrations. This foundational study established the importance of statistical methods in air quality research and addressed the need for flexible distributions that could accommodate the right-skewed nature of pollution data. While innovative at its time, this approach was ultimately limited by its assumption of stationary conditions and global statistical uniformity - constraints that would later motivate more sophisticated modelling frameworks.

More recently, Williams et al.[6]develop a novel framework for analysing air pollution dynamics through the lens of superstatistics, by now a standard method in nonequilibrium statistical mechanics[3,4,5]. This approach, rooted in statistical physics, addresses the limitations of conventional models by treating pollution fluctuations as arising from a superposition of different statistical regimes. The authors demonstrate how this method can capture the heavy-tailed probability distributions and intermittent behaviour characteristic of real-world pollutant concentration data. By incorporating time-scale separation between rapid fluctuations and slower environmental variations, their model provides improved representation of extreme pollution events that often evade traditional Gaussian or log-normal descriptions. This work establishes a crucial theoretical foundation for understanding the complex temporal patterns in air pollution, particularly in urban settings where multiple emission sources interact with changing meteorological conditions.

Expanding beyond temporal analysis, He et al.[7]examine the geographical dimension of pollution variability, in their case for a large European data set. The research reveals significant regional differences in pollution statistics across Europe, challenging the assumption of spatial uniformity in air quality modelling. Through advanced spatial analysis techniques, the authors identify distinct statistical signatures in pollution data that correlate with factors such as local emission sources, topographic features and climate patterns. This work provides empirical evidence that pollution dynamics cannot be adequately described by universal constant parameter statistical models, but rather require region-specific approaches. Together, these two studies offer a comprehensive perspective on air pollution statistical features, integrating both temporal and spatial complexity through innovative applications of statistical physics principles to environmental science.

Autocorrelation analysis is another core tool in understanding the persistence and predictability of air pollutant concentrations. The authors of[12]investigated PM10concentrations in the Krasnoyarsk Territory using autocorrelation analysis to explore temporal patterns in particulate matter data from atmospheric monitoring systems. Their work highlights the presence of short term and long term dependencies in PM10time series, which can inform forecasting models and pollution control measures. By focusing on a single pollutant within a specific regional monitoring framework, the study provides valuable insights into local air quality dynamics, while also illustrating the broader need to address both the temporal structure and environmental drivers behind pollutant fluctuations.

Expanding beyond a single location and pollutant, Dai and Zhou[13]analysed temporal and spatial correlation patterns across Chinese cities using hourly monitoring data and network-based approaches such as the Planar Maximally Filtered Graph method. Their findings reveal pollutant specific behaviours, such as strong spatial correlations in ozone and more localised dispersion patterns in particulate matter, and show the persistence of pollution events through long term temporal memory. The identification of geographically coherent clusters of cities with synchronised pollutant dynamics provides an important framework for regional pollution control, emphasizing that policy interventions must account for both meteorological influences and industrial activity patterns across space and time.

A key gap in the literature dealing with statistical fluctuations of air pollutant concentrations is the lack of focus on low pollution periods (besides the high-pollution states that are often investigated[14]) and also the discussion of memory effects, i.e. how pollution levels depend on their past values over time, and how correlation functions decay. Most studies concentrate on high pollution events and extreme cases. However, even during low-pollution periods, pollution can show clear persistence due to weather conditions and ongoing background emissions[15]. Ignoring this can lead to incomplete descriptions of the dynamical behaviour. This illustrates the need for models that also capture the PDF behaviour for low pollution situations, which will lead to the more general PDFs studied in this paper, exhibiting power-law behaviour both for high- and low-pollution situations. In addition to this, we will also study correlation functions of measured pollution concentrations, describing the dynamical behaviour.

## 2Methodology

In this paper, we analyse a large amount of data measured between 2020 to 2025 in the UK, and fit the observed non-Gaussian probability density functions (PDFs) of measured air pollution concentrations with functional forms that are motivated by superstatistical models[3,4]and the formalism of non-extensive statistical mechanics[8,10], i.e. in general by methods borrowed from the physics community when describing complex systems in nonequilibrium states. We will provide a systematic investigation how the best-fitting parameters for the observed PDFs vary at different spatial locations and for different types of pollutants, forming characteristic clouds and patterns in the parameter space.Figure 1:Geographical distribution of UK air quality monitoring sites analysed in this paper. The map illustrates the locations of monitoring stations (red markers) across the United Kingdom, as recorded by the Department for Environment, Food and Rural Affairs (DEFRA).

The spatial data utilized in this study was sourced from the UK-AIR database, comprising hourly concentration measurements recorded between January 2020 and January 2025 across all available monitoring sites in the United Kingdom at this length of time[16]. To evaluate spatial heterogeneity, these sites were categorized into distinct environmental classifications, including Urban Traffic, Urban Background, Urban Industrial, Suburban Industrial, Suburban Background, and Rural Background. The statistical analysis primarily focused on characterizing the distributions of four key atmospheric pollutants: particulate matter 2.5 (P​M2.5PM_{2.5}), particulate matter 10 (P​M10PM_{10}), nitric oxide (NO), and nitrogen dioxide (N​O2NO_{2}). While Ozone (O3O_{3}) was also initially investigated, it frequently exhibited anomalous probability density functions and was therefore excluded from the primary modelling. Prior to the full parameter space analysis, the empirical data was filtered to take positive values only (as expected for a concentration); also a few specific sites that yielded atypical distributions and failed to produce a good fit with the theoretical models were discarded, most of these discarded sites lacked a significant amount of data. The remaining observed probability density functions were fitted withqq-Gamma distribution. To determine the specific distribution parameters (α\alpha,qq, andλ\lambda), the Maximum Likelihood Estimation (MLE) parameter estimation technique was employed, which identifies values that maximize the probability of the observed data being produced by the given distribution with those parameters.

The probability density functions (PDFs) that we will use in our novel fitting approach in the following are the so-calledqq-Gamma distributions, defined asf​(x)=1Z​xα−1​[1+(q−1)​λ​x]11−q,f(x)=\frac{1}{Z}\,x^{\alpha-1}\left[1+(q-1)\lambda x\right]^{\frac{1}{1-q}},(1)

where
- •

α\alphacontrols the shape of the probability density at low concentrationsxx(x→0x\to 0),
- •

qqquantifies the non-extensiveness (deviation from classical exponential decay obtained for the special caseq→1q\to 1),
- •

λ\lambdais an inverse scale parameter,
- •

ZZis a normalization constant.

These types of distributions occur in generalized statistical mechanics models of complex systems (see, e.g.[10]for a recent comprehensive review), as well as in superstatistical modelling approaches, where the parameters of a simple dynamical model (such as local stochastic differential equation) are random variables itself, for details, see e.g.[4]. The relevance of superstatistical models for air pollution dynamics has been previously mentioned and applied to the high pollution tail behaviour of observed PDFs, see[7,14]. Here we go a step further, by also incorporating low-pollution events, thus taking into account the entire range of possible pollution states, from very low to very high.

## 3Results

## 3.1Observed PDFs–typical examples

We focus our statistical analysis primarily onto the following air pollutants: particulate matter
2.5 (P​M2.5PM_{2.5}), particulate matter 10 (P​M10PM_{10}), nitric oxide (N​ONO) and nitrogen dioxide (N​O2NO_{2}), investigating their dynamics for all available sites in the United Kingdom as recorded on[16]. We have investigated the Probability density functions (PDFs) of air pollution concentrations at all these locations and checked whether our theoretical model PDFs yield a good fit. The vast majority of sites are fitted well, though with different values of the parameters.

We start with an illustrative example of a typical trajectory of an air pollution concentration over time, as shown in Fig.2.Figure 2:The time series trajectory plot ofN​O2NO_{2}concentration for the Leicester location between 2020 and 2025, measured at 1 hour intervals.

The graph of Fig.2shows howN​O2NO_{2}levels meassured at an example site in Leicester vary over time. Pollution levels fluctuate across multiple temporal scales, with occasional sharp concentration spikes observed. These spikes are likely caused by special short pollution events, such as high traffic or certain weather conditions. There is also a clear long-term oscillating pattern that repeats over the years, suggesting thatN​O2NO_{2}levels are also affected by seasonal patterns.

In the following, we look at the PDFs generated for various types of pollutants. The use of linear-linear, log-linear, and log-log scales in Fig.3allows us to see which regions of the PDFs are particularly well fitted (for example those around the tails or those around the maximum). Linear-linear plots characterise the ”bulk” of typical data, but they often do not yield much information on the behaviour of rare events in the tails. Log-linear (y-log) scales visualise exponential decay as a straight line, allowing for a precise assessment of how quickly concentrations diminish from the mean. Crucially, log-log plots are useful to identify power-law behaviour as straight lines.Figure 3:PDFs of air pollutant concentrations for the example site at Leicester. Each row displays the distributions of a different pollutant:N​ONO,N​O2NO_{2},P​M10PM_{10}andP​M2.5PM_{2.5}. To highlight different characteristics of the tail behaviours, the columns present the same data across three different axis scales: Linear-Linear (left), Log-Linear (middle), and Log-Log (right). The empirical data is represented by light blue histograms. Theoretical curves areqq-Gamma fits using two different estimation methods: Sum of Squared Residuals (SSR, red dashed lines) and Maximum Likelihood Estimation (MLE, green solid lines).

The PDF shown in the 2nd row of Fig.3actually corresponds precisely to the trajectory shown in Fig. 1,

The distribution of Nitric Oxide (N​ONO) (Fig.3a-c) represents the most extreme case of heavy-tailed behaviour among the 4 investigated pollutants. The non-extensiveness parameter is consistently high (q=1.30q=1.30for MLE andq=1.32q=1.32for SSR), indicating a power-law-like decay that persists even at very high concentrations. This suggests that theN​ONOtime series is characterised by frequent high-intensity ”spikes,” likely due to its proximity to primary combustion sources. In contrast, Nitrogen Dioxide (N​O2NO_{2}) (Fig.3d-f) shows a more moderated distribution withqqvalues closer to unity (q=1.12q=1.12for MLE;q=1.14q=1.14for SSR). WhileN​O2NO_{2}still exhibits heavy-tailed characteristics, the decay is markedly faster than that ofN​ONO. Quantitatively, the MLE method proves superior for both cases, achieving an Anderson-Darling (A2A^{2}) statistic of 36.32 forN​ONOand 25.71 forN​O2NO_{2}, significantly outperforming the SSR fits in both instances.

The final two rows of Fig.3(subplots g-l) depict the distributions forP​M10PM_{10}andP​M2.5PM_{2.5}. Both pollutants demonstrate a transition toward near-exponential behaviour, as evidenced byqqparameters approaching 1. ForP​M10PM_{10}, the MLE and SSR fits are nearly identical (q=1.08q=1.08and1.071.07, respectively), whileP​M2.5PM_{2.5}shows slightly higher values (q=1.11q=1.11for MLE and1.101.10for SSR). This difference suggests that while particulate matter concentrations are susceptible to occasional heavy-tailed events, they lack the extreme stochastic volatility observed inN​ONO. Notably, the scaling parameterλ\lambdavaries significantly between the two, withP​M2.5PM_{2.5}showing a much higher MLE value (λ=1.69\lambda=1.69) thanP​M10PM_{10}(λ=0.60\lambda=0.60). Consistent with the two pollutants, the MLE approach remains the more statistically sound methodology for these particulates, yielding lowerA2A^{2}values (27.0627.06forP​M10PM_{10}and35.0335.03forP​M2.5PM_{2.5}) compared to the SSR approach.Figure 4:Same as Fig.3, but for Ozone (O3O_{3}).

While theqq-Gamma distribution captures
quite efficiently the behaviour of theN​OxNO_{x}andP​MxPM_{x}pollutants discussed so far, there are substances with anomalous behaviour. An example is Ozone (O3O_{3}), typically observed to have PDFs that are quite different from those discussed so far. The reason may be the existence of decay modes forO3O_{3}. Fig.4illustrates that theqq-Gamma struggles to accurately model Ozone concentrations at the Leicester site (as well as at other sites as well). Theqq-Gamma does not capture the 2 maxima observed. The Anderson-Darling test also fails to give us a goodness of fit test statistic.
This highlights the need for further methodological development to account for the distinct statistical behaviour of Ozone concentrations in future studies.

## 3.2Parameter space ofqq-Gamma fits

The parameter relationship plots of Fig.5for all pollutants
measured at the sites displayed in Fig. 1 reveal consistent clustering patterns across different site types, reflecting distinct emission and mixing characteristics. Only MLE is used for the fittings, as it has been shown to be the better fitting method in the previous section.

Urban Traffic sites consistently exhibit the highestqq-values (often between1.11.1and1.31.3) across all pollutants, paired with moderateα\alphavalues (typically2​–​62–6). This indicates strongly non-extensive behaviour and heavy-tailed concentration distributions, characteristic of direct, intermittent emission sources such as vehicle exhaust.

Urban Background and Urban Industrial sites form an intermediate cluster, withqq-values ranging from around1.01.0to1.31.3andα\alphavalues spanning a wider range (approximately2​–​82–8). This suggests more varied and mixed emission sources, including traffic, heating, and industrial contributions, leading to less extreme but still heavy-tailed concentration profiles.

Suburban and Rural Background sites display the lowestqq-values (generally1.0​–​1.151.0–1.15) and the highestα\alphavalues (often4​–​104–10or more), particularly evident in the longer-tailed plots (right-hand panels). This reflects smoother, more well-mixed concentration distributions typical of regional background air, with less influence from nearby strong emission sources.

The observed parameter differences between site environments are statistically significant and indicate that air pollutant concentrations, in their dynamical behaviour, are strongly influenced by the location where they are measured. Traffic sites, understandably, have extreme values. Rural background sites have much more moderate values. Urban and industrial sites have values in between.Figure 5:Parameter relationship plot ofqqvsα\alpha,qqvsλ\lambdaandα\alphavsλ\lambdafitted byqq-Gamma forN​O2NO_{2},N​ONO,P​M10PM_{10}andP​M2.5PM_{2.5}time series. Each dot corresponds to a particular location in the data base.

## 3.3Temporal correlation functions

By calculating the autocorrelation, we can distinguish between pollutant concentrations that dissipate rapidly and those that linger for longer. We determined temporal correlation functionsC(t)=(E(x(s)x(s+t)−E(x(s)2))/E(x(s)2)C(t)=(E(x(s)x(s+t)-E(x(s)^{2}))/E(x(s)^{2})from the measured air pollution time seriesx​(s)x(s). The correlation functions tend to decay slower than exponential. We fitted
these decays withqq-exponential functionseq−λ​t=(1+(q−1)​λ​t)−1q−1e_{q}^{-\lambda t}=(1+(q-1)\lambda t)^{\frac{-1}{q-1}}(reducing to exponentials forq=1q=1).
Correlation functions of this type can by produced by superstatistical paramter fluctuations of the parameterλ\lambdain an exponential decaye−λ​te^{-\lambda t}. Some results,
for the example of the site London Marylebone Ropad, are shown in the following.Figure 6:(a) - Daytime autocorrelation function at 5 lags fitted withqq-exponentials forN​ONO,N​O2NO_{2},P​M2.5PM_{2.5}andP​M10PM_{10}time series measured at London Marylebone Road. (b) - Same as in (a) but for nighttime.

Theqq-exponential fits reveal distinct temporal correlation patterns across all pollutants and exhibit different behaviour if conditioned on either day- or night-time. During daytime, all pollutants exhibit strong non-extensive behaviour withqq-values significantly greater than11(q=1.460−2.688q=1.460-2.688), indicating long-range correlations and heavy-tailed decay in autocorrelation.N​O2NO_{2}shows the most extreme non-extensiveness (q=2.688q=2.688), suggesting particularly persistent concentration patterns, while particulate matter demonstrates intermediate effects. At night, the correlation structure undergoes dramatic changes, nitrogen dioxide transitions to near-exponential decay (q=0.958q=0.958), while nitric oxide maintains non-extensiveness (q=1.409q=1.409) and particulate matter increases in correlation strength (P​M2.5PM_{2.5}:q=2.224q=2.224). Theλ\lambdaparameters, representing the initial decay rate for small time lags, show consistent values across pollutants (0.183−0.2830.183-0.283) with nitric oxide displaying the fastest correlation decay at night (λ=0.283\lambda=0.283) and nitrogen dioxide the slowest during day (λ=0.268\lambda=0.268).Figure 7:Best fitting parametersqqandλ\lambdafor measured shape of auto correlation function ofN​ONO,N​O2NO_{2},P​M2.5PM_{2.5}andP​M10PM_{10}time series.

Again we may proceed to the parameter space,
which for the correlation function fits is just
the 2-dimensional(q,λ)(q,\lambda)plane. Our results for the best fitting parameters(q,λ)(q,\lambda)at the various locations displayed in Fig. 1 are shown in Fig.7.
As shown in the four scattering plots for (a)N​ONO, (b)N​O2NO_{2}, (c)P​M2.5PM_{2.5}, and (d)P​M10PM_{10}, the fittedqqandλ\lambdavalues for all pollutants are concentrated in broad, overlapping clusters. There is no clear visible influence of different site types or between daytime and nighttime periods across the plots.

In all plots theqq-values cluster around 1.0, with most data points concentrated between approximately 0.95 and 1.10. This central clustering suggests that, across different locations and times, the underlying concentration dynamics for these pollutants often approximate a system near classical, extensive statistics. Theλ\lambdavalues associated with theseqq-values vary widely, ranging from about 0.1 to 0.8, indicating a broad range in the strength of temporal correlation.

There is no strong functional relationship betweenqqandλ\lambdavisible for (a),(c), and (d). However, plot (b) for nitrogen dioxide (N​O2NO_{2}) provides evidence for a pattern where the fittedλ\lambdavalue appears to decrease as theqq-value increases. This downward trend is most visible for points fitted during the daytime, suggesting that for daytimeN​O2NO_{2}, stronger non-extensive behaviour correlates with weaker decay of the temporal correlation. In contrast, plots (a), (c), and (d) for NO,P​M10PM_{10}, andP​M2.5PM_{2.5}show widely intermixed points for daytime and nighttime, with no pronounced systematic trend in the parameters. Although urban site types may show a slight tendency towards lowerλ\lambdavalues in some of the plots, there is substantial overlap of the corresponding background sites. Note that forN​ONOandN​O2NO_{2}the averageqq-value is roughly equal to 1, whereas forP​M​2.5PM2.5andP​M​10PM10it is bigger than 1.

## 4Conclusion

Based on the analysis presented in this paper, theqq-Gamma distribution has proven to be a powerful tool for modelling PDFs of temporally varying air pollution concentrations, effectively capturing both, low-level and extreme high-concentration events. Unlike traditional models, this accounts for the observed heavy-tailed nature of pollutant concentrations, leading to more accurate descriptions of air pollution PDFs. Our fittings were quite successful forN​O,N​O2,P​M2.5NO,NO_{2},PM_{2.5}andP​M10PM_{10}. However,
there are limits of the applicability of this approach. For example, for Ozone we observe other types of distributions. Thus, the complexity of air pollution PDFs is inherently depending on the type of substance considered, suggesting that future research must explore alternative or multi-modal superstatistical frameworks to capture the dynamics of these anomalous pollutants.

Our analysis also reveals, by analysis of the parameters underlying the the PDF and autocorrelation structure, that different types of monitoring sites, such as urban traffic, industrial and rural backgrounds, exhibit different statistical signatures that reflect their unique emission sources and environmental conditions. Additionally, the autocorrelation analysis shows clear differences between the dynamics of pollution at night and daytime, with pollutants such asN​O2NO_{2}showing strong persistence during the day but near-exponential decay at night. These distinct spatio-temporal signatures show the need of region-specific and time-sensitive approaches to air quality management, demonstrating that policy interventions must account for local environmental drivers rather than relying on global, universally constant assumptions.

To summarize, our systematic spatio-temporal analysis of air pollution data for the UK shows thatqq-Gamma distributions andqq-exponential correlation functions provide an excellent modelling framework for generic air pollution dynamics. These types of distributions arise naturally from superstatistical models, i.e. from stochastic differential equations where the parameters themselves are random variables.
These types of models provide a more subtle understanding of variations in pollution behaviour, supporting better environmental monitoring, risk assessment, and evidence-based policymaking, aimed at mitigating the impacts of extreme atmospheric pollution. As shown in this paper,
our parametrization in terms of the parametersqq,λ\lambdaandα\alphacan help to quantify and comnpare the statistical properties of different pollutants at a variety of different locations.

## 5Appendix

## 5.1Normalization Factor

The normalization constantZZisZ=∫0∞xα−1​[1+(q−1)​λ​x]11−q​𝑑xZ=\int_{0}^{\infty}x^{\alpha-1}\left[1+(q-1)\lambda x\right]^{\frac{1}{1-q}}\,dx

Using the substitutionv=(q−1)​λ​xv=(q-1)\lambda x,Z=1[(q−1)​λ]α​∫0∞vα−1​(1+v)11−q​𝑑vZ=\frac{1}{[(q-1)\lambda]^{\alpha}}\int_{0}^{\infty}v^{\alpha-1}(1+v)^{\frac{1}{1-q}}\,dv

this evaluates toZ=Γ​(α)​Γ​(1q−1−α)[(q−1)​λ]α​Γ​(1q−1)Z=\frac{\Gamma(\alpha)\,\Gamma\left(\frac{1}{q-1}-\alpha\right)}{[(q-1)\lambda]^{\alpha}\,\Gamma\left(\frac{1}{q-1}\right)}

Theqq-Gamma distribution captures atmospheric pollution complexities through:
- •

the power-law term(xαx^{\alpha})→\rightarrowlow-level pollution events,
- •

theqq-exponential term(heavy tails)→\rightarrowextreme high-concentration events.

## 5.2Parameter Insights for Environmental Scienceq<1\displaystyle q<1→Rapid decay (faster than exponential): confined or short-range processes,\displaystyle\rightarrow\text{Rapid decay (faster than exponential): confined or short-range processes},q≈1\displaystyle q\approx 1→Classical exponential decay,\displaystyle\rightarrow\text{Classical exponential decay},q>1\displaystyle q>1→Heavy-tailed decay (slower than exponential),\displaystyle\rightarrow\text{Heavy-tailed decay (slower than exponential)},α>0\displaystyle\alpha>0→Controls asymmetry; useful for skewed environmental data.\displaystyle\rightarrow\text{Controls asymmetry; useful for skewed environmental data}.

## 5.3Better Extreme Event Prediction
- •

Standard models underestimate tail risks[6].
- •

Theqq-Gamma distribution is taken to better capture both rare low- (x→0x\to 0) and high-pollution (x→∞)x\to\infty)events:P​(x)∝xα−1​[1+(q−1)​λ​x]11−qP(x)\propto x^{\alpha-1}\left[1+(q-1)\lambda x\right]^{\frac{1}{1-q}}

## 5.4Moments of the Distribution

## 5.4.1Mean Concentration⟨x⟩=1Z​∫0∞xα​[1+(q−1)​λ​x]11−q​𝑑x,\langle x\rangle=\frac{1}{Z}\int_{0}^{\infty}x^{\alpha}[1+(q-1)\lambda x]^{\frac{1}{1-q}}\,dx,⟨x⟩=[(q−1)​λ]α​Γ​(1q−1)Γ​(α)​Γ​(1q−1−α)​Γ​(α+1)​Γ​(1q−1−α−1)[(q−1)​λ]α+1​Γ​(1q−1)\langle x\rangle=\frac{[(q-1)\lambda]^{\alpha}\,\Gamma\left(\frac{1}{q-1}\right)}{\Gamma(\alpha)\,\Gamma\left(\frac{1}{q-1}-\alpha\right)}\frac{\Gamma(\alpha+1)\,\Gamma\left(\frac{1}{q-1}-\alpha-1\right)}{[(q-1)\lambda]^{\alpha+1}\,\Gamma\left(\frac{1}{q-1}\right)}⟨x⟩=αλ​[1−(α+1)​(q−1)]\langle x\rangle=\frac{\alpha}{\lambda\left[1-(\alpha+1)(q-1)\right]}

## 5.4.2VarianceVar​(x)=1Z​∫0∞xα+2​[1+(q−1)​λ​x]11−q​𝑑x−⟨x⟩2,\mathrm{Var}(x)=\frac{1}{Z}\int_{0}^{\infty}x^{\alpha+2}[1+(q-1)\lambda x]^{\frac{1}{1-q}}\,dx-\langle x\rangle^{2},Var​(x)=[(q−1)​λ]α​Γ​(1q−1)Γ​(α)​Γ​(1q−1−α)​Γ​(α+2)​Γ​(1q−1−α−2)[(q−1)​λ]α+2​Γ​(1q−1)−α2λ2​[1−(α+1)​(q−1)]2\mathrm{Var}(x)=\frac{[(q-1)\lambda]^{\alpha}\,\Gamma\left(\frac{1}{q-1}\right)}{\Gamma(\alpha)\,\Gamma\left(\frac{1}{q-1}-\alpha\right)}\frac{\Gamma(\alpha+2)\,\Gamma\left(\frac{1}{q-1}-\alpha-2\right)}{[(q-1)\lambda]^{\alpha+2}\,\Gamma\left(\frac{1}{q-1}\right)}-\frac{\alpha^{2}}{\lambda^{2}\left[1-(\alpha+1)(q-1)\right]^{2}}Var​(x)=α​(2−q)λ2​[1−(α+1)​(q−1)]2​[1−(α+2)​(q−1)]\mathrm{Var}(x)=\frac{\alpha(2-q)}{\lambda^{2}\left[1-(\alpha+1)(q-1)\right]^{2}\left[1-(\alpha+2)(q-1)\right]}

## 5.5Interpretation

This distribution combines:
- •

Power-law term(xαx^{\alpha}) for low concentrationsxx,
- •

q-exponential termfor heavy-tailed extreme events, leading to asymptotic power lawx−1q−1x^{-\frac{1}{q-1}}forx→∞x\to\infty.

Previous work[7]only fitted the tails of the data byqq-exponentials. We now look at the entire distribution.Table 1:Physical Interpretation of ParametersParameterPhysical Meaningα\alphaShape at low concentrationsqqNon-extensivenessλ\lambdaDecay rate

## 5.6Maximum Likelihood Estimation (MLE)

Maximum Likelihood Estimation (MLE)is a fundamental method for estimating the parameters of a statistical model[21]. The principle is to find the parameter values that maximize thelikelihood functionℒ​(𝜽|𝐱)\mathcal{L}(\boldsymbol{\theta}|\mathbf{x}), which represents the probability of observing the given sample data𝐱=(x1,x2,…,xn)\mathbf{x}=(x_{1},x_{2},\dots,x_{n}).
- 1.

Likelihood Function:Assuming independent and identically distributed (i.i.d.) data, the joint likelihood for theqq-Gamma distribution is the product of the individual probability densities:ℒ​(α,q,λ|𝐱)=∏i=1nf​(xi|α,q,λ)=∏i=1n1Z​xiα−1[1+(q−1)​λ​xi]1q−1\mathcal{L}(\alpha,q,\lambda|\mathbf{x})=\prod_{i=1}^{n}f(x_{i}|\alpha,q,\lambda)=\prod_{i=1}^{n}\frac{1}{Z}\frac{x_{i}^{\alpha-1}}{\left[1+(q-1)\lambda x_{i}\right]^{\frac{1}{q-1}}}

whereZZis the normalization constant.
- 2.

Log-Likelihood:Maximizing the product in the above equation is numerically unstable. We instead maximize thelog-likelihood, which converts the product into a sum:ℓ​(α,q,λ)=log⁡ℒ​(α,q,λ|𝐱)=∑i=1nlog⁡f​(xi|α,q,λ)\ell(\alpha,q,\lambda)=\log\mathcal{L}(\alpha,q,\lambda|\mathbf{x})=\sum_{i=1}^{n}\log f(x_{i}|\alpha,q,\lambda)\\

## 5.7Sum of Squared Residuals (SSR)

TheSum of Squared Residuals (SSR)quantifies the discrepancy between the observed data and the values expected under the fitted model. Minimizing the SSR achieves the best possible fit of a model to the data[22].

Implementation:
- 1.

Binning:The data is grouped intoKKbins (histogram) with observed frequenciesOkO_{k}fork=1,…,Kk=1,\dots,K.
- 2.

Expected Frequencies:Using the fitted PDF with MLE parameters(α^,q^,λ^)(\hat{\alpha},\hat{q},\hat{\lambda}), the expected frequencyEkE_{k}for binkkis:Ek=n​∫lowerkupperkf​(x|α^,q^,λ^)​𝑑xE_{k}=n\int_{\text{lower}_{k}}^{\text{upper}_{k}}f(x|\hat{\alpha},\hat{q},\hat{\lambda})dx

wherennis the total number of observations.
- 3.

Calculation of SSR:The SSR is computed as the sum of squared differences between observed and expected bin counts:SSR=∑k=1K(Ok−Ek)2\text{SSR}=\sum_{k=1}^{K}(O_{k}-E_{k})^{2}

## 5.8Log-Likelihood Goodness-of-Fit

Thelog-likelihoodprovides a direct measure of model fit. A higher value indicates that the fitted distribution provides a better fit to the observed data[23].

Implementation:
- 1.

Model Fit:The maximized log-likelihood isℓ​(α^,q^,λ^)=∑i=1nlog⁡f​(xi|α^,q^,λ^).\ell(\hat{\alpha},\hat{q},\hat{\lambda})=\sum_{i=1}^{n}\log f(x_{i}|\hat{\alpha},\hat{q},\hat{\lambda}).
- 2.

Model Comparison:Between competing models, the one with the higher maximized log-likelihood is preferred.
- 3.

Penalized Criteria:To balance fit and complexity, criteria such asAIC=−2​ℓ+2​k,BIC=−2​ℓ+k​log⁡(n)\text{AIC}=-2\ell+2k,\quad\text{BIC}=-2\ell+k\log(n)

are commonly used, wherekkis the number of parameters.

## 5.9Anderson-Darling Goodness-of-Fit

TheAnderson-Darling (AD) statisticevaluates how well a model’s cumulative distribution function (CDF) fits the observed data, placing greater emphasis on the tails[24].

Implementation:
- 1.

Empirical CDF:LetFn​(x)F_{n}(x)be the empirical CDF of the sample, andF​(x)F(x)the CDF of the fitted model.
- 2.

AD Statistic:ComputeA2=−n−1n​∑i=1n[(2​i−1)​log⁡F​(x(i))+(2​n+1−2​i)​log⁡(1−F​(x(i)))],A^{2}=-n-\frac{1}{n}\sum_{i=1}^{n}\Big[(2i-1)\log F(x_{(i)})+(2n+1-2i)\log(1-F(x_{(i)}))\Big],

wherex(i)x_{(i)}are the ordered sample values.
- 3.

Interpretation:SmallerA2A^{2}indicates a better fit. It can be used to compare different models or check against critical values for hypothesis testing.

## Data Availability

The data used in this study are publicly available athttps://uk-air.defra.gov.uk/data/data_selector_service?=&1=&s=1&o=#mid. The code used for fitting and generating plots are available athttps://github.com/CptMcSalad/Superstatistical-Analysis-of-PDFs.

## Acknowledgements

C.B. acknowledges funding by a QMUL ISPF-ODA Research England grant on air pollution dynamics, as well as funding by STFC grant UKRI467.

## Author contribution

Conceptualization - All authors; Methodology - All authors; Data curation - All authors. Data visualization -
All authors; Writing original draft - All authors. All authors approved the final submitted draft.

## Competing interest.

The authors declare no competing interests.

## References
- [1]C. Seigneur,Air Pollution: Concepts, Theory, and Applications,
Cambridge University Press, 2019.
- [2]M. K. Hill,Understanding Environmental Pollution, 3rd ed., Cambridge University Press, 2010.
- [3]C. Beck, E. G. D. Cohen,Superstatistics, Physica A: Statistical Mechanics and its Applications, 322 (2003), 267-275.
- [4]C. Beck,Superstatistics: Theoretical concepts and physical applications, in Anomalous Transport: Foundations and Applications, G. Radons et al. (eds.), Wiley-VCH, 2007.
- [5]R. Metzler,Superstatistics and non-Gaussian diffusion, Eur. Phys. J. Special Topics229, 711 (2020).
- [6]Williams, G., Schäfer, B., & Beck, C. (2020). Superstatistical approach to air pollution statistics.Physical Review Research,2(1), 013019.
- [7]He, H., Schäfer, B., & Beck, C. (2022). Spatial heterogeneity of air pollution statistics in Europe.Scientific Reports,12(1), Article 12215.
- [8]C. Tsallis,Possible generalization of Boltzmann-Gibbs statistics,
J. Stat.Phys.52, 479 (1988).
- [9]C. Tsallis and E. Brigatti,Nonextensive statistical mechanics: A brief introduction, Continuum Mech. Thermodyn.,16(2004), 223–235.
- [10]C. Tsallis,Introduction to Nonextensive Statistical Mechanics, 2nd edition, Springer, 2023.
- [11]Marani, A., Lavagnini, I., & Buttazzoni, M. (1986). Statistical Study of Air Pollutant Concentrations via Generalized Gamma Distributions.Journal of the Air Pollution Control Association,36(11), 1250–1254.
- [12]A. A. Golubnichiy and E. A. Tuksina,Autocorrelation analysis of time series of PM10 concentrations according to the data from the atmospheric monitoring subsystem of Krasnoyarsk Territory, Naukovedenie, 7(4) (2015).
- [13]Y. H. Dai, W. X. Zhou,Temporal and spatial correlation patterns of air pollutants in Chinese cities, PLOS ONE, 12 (2017), e0182724.
- [14]H. He, B. Schaefer, C. Beck,Spatial analysis of tails of air pollution PDFs in Europe, Environmental Data Science 3:e30 (2024), 1-11.
- [15]P. Yu, X. Zhang, L. Wang, J. Li,Memory Behaviors of Air Pollutions and Their Spatial Patterns in China, Frontiers in Physics, 10 (2022), 875357.
- [16]UK Air Information Resource, Department for Environment, Food & Rural Affairs (Defra),Data Selector Service, https://uk-air.defra.gov.uk/data/data_selector_service, (accessed May 2024)
- [17]G. G. Stokes,On the Effect of the Internal Friction of Fluids on the Motion of Pendulums, Transactions of the Cambridge Philosophical Society, 9 (1851), 8–106.
- [18]C. N. Davies,The Separation of Airborne Dust and Particles, Proceedings of the Institution of Mechanical Engineers, 1B (1945), 185–213.
- [19]W. C. Hinds,Aerosol Technology: Properties, Behavior, and Measurement of Airborne Particles, 2nd ed., Wiley-Interscience, 1999.
- [20]G. E. Uhlenbeck, L. S. Ornstein,On the Theory of the Brownian Motion, Physical Review, 36 (1930), 823–841.
- [21]G. Casella, R. L. Berger,Statistical Inference, 2nd Edition, Duxbury Press, 2002.
- [22]G. A. F. Seber, A. J. Lee,Linear Regression Analysis, 2nd Edition, Wiley, 2003.
- [23]K. P. Burnham, D. R. Anderson,Model Selection and Multimodel Inference: A Practical Information-Theoretic Approach, 2nd Edition, Springer, 2002.
- [24]T. W. Anderson, D. A. Darling,A Test of Goodness of Fit, Journal of the American Statistical Association, 49(268) (1954), 765–769.

## 


- 


Major funding support from
