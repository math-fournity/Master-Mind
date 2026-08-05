# Integrating Bayesian Spectral Deconvolution and Expert Scientific Reasoning for Robust Peak Estimation

**arXiv ID**: 2605.17518v1
**Authors**: Hayato Okubo, Yoshifumi Amamoto, Toshimitsu Aritake, Hiroyuki Kumazoe, Shiryu Nakano, Evan Jamison, Satoshi Tanaka, Yoh-ichi Mototake
**Published**: 2026-05-17
**Categories**: physics.data-an, stat.AP, stat.ML
**Comments**: 55 pages, 26 figures
**HTML URL**: https://arxiv.org/html/2605.17518v1

## Abstract

Spectral deconvolution is essential for extracting peak structures that encode material properties and chemical structures, but conventional automated methods often fail when spectra contain high-intensity noise or unknown background components. In practice, scientists rarely interpret spectra in isolation. Instead, they identify physically meaningful peaks by relating spectral structures to auxiliary information such as physical-property values, chemical structures, and trends across related measurements. Here, we propose a Bayesian framework that integrates spectral deconvolution with a model of expert scientific reasoning. In this work, expert scientific reasoning refers to the practice of evaluating candidate spectral structures by their consistency with independently measured physical-property values, rather than to manual expert intervention during inference. We formalize this reasoning as a physical-property regression layer, implemented using Gaussian process regression, and couple it with Bayesian spectral deconvolution. By averaging the physical-property likelihood over posterior predictive spectra inferred from Bayesian spectral deconvolution, the proposed method selects spectral models according to the consistency between inferred spectral structures and physical-property information. We validate the framework using synthetic spectra with high-intensity noise or unknown backgrounds and infrared spectra of poly(lactic acid). The method recovers physically meaningful peak structures that conventional Bayesian spectral deconvolution misses or misidentifies from spectra alone, including weak peaks in poly(lactic acid) IR spectra related to measured degradation rates. These results demonstrate that integrating expert scientific reasoning with Bayesian spectral deconvolution enables robust peak estimation under conditions where spectrum-only inference is unreliable.

## Full Text

Integrating Bayesian Spectral Deconvolution and Expert Scientific Reasoning for Robust Peak Estimation

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.17518v1 [physics.data-an] 17 May 2026

## Integrating Bayesian Spectral Deconvolution
and Expert Scientific Reasoning for Robust Peak EstimationHayato OkuboGraduate School of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, JapanYoshifumi AmamotoDepartment of Advanced Materials Science, Graduate School of Frontier Sciences, The University of Tokyo, 5-1-5 Kashiwanoha, Kashiwa, Chiba 277-8561, JapanToshimitsu AritakeHitotsubashi Institute for Advanced Study, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, JapanHiroyuki KumazoeGraduate School of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, JapanShiryu NakanoGraduate School of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, JapanEvan JamisonDepartment of Statistics and Applied Probability, University of California, Santa Barbara, Santa Barbara, CA 93106, USASatoshi TanakaGraduate School of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, JapanYoh-ichi Mototakey.mototake@r.hit-u.ac.jpGraduate School of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, Japan(May 17, 2026)

## Abstract

Spectral deconvolution is essential for extracting peak structures that encode material properties and chemical structures, but conventional automated methods often fail when spectra contain high-intensity noise or unknown background components. In practice, scientists rarely interpret spectra in isolation. Instead, they identify physically meaningful peaks by relating spectral structures to auxiliary information such as physical-property values, chemical structures, and trends across related measurements.
Here, we propose a Bayesian framework that integrates spectral deconvolution with a model of expert scientific reasoning. In this work, expert scientific reasoning refers to the practice of evaluating candidate spectral structures by their consistency with independently measured physical-property values, rather than to manual expert intervention during inference. We formalize this reasoning as a physical-property regression layer, implemented using Gaussian process regression, and couple it with Bayesian spectral deconvolution. By averaging the physical-property likelihood over posterior predictive spectra inferred from Bayesian spectral deconvolution, the proposed method selects spectral models according to the consistency between inferred spectral structures and physical-property information.
We validate the framework using synthetic spectra with high-intensity noise or unknown backgrounds and infrared spectra of poly(lactic acid). The method recovers physically meaningful peak structures that conventional Bayesian spectral deconvolution misses or misidentifies from spectra alone, including weak peaks in poly(lactic acid) IR spectra related to measured degradation rates. These results demonstrate that integrating expert scientific reasoning with Bayesian spectral deconvolution enables robust peak estimation under conditions where spectrum-only inference is unreliable.

## IIntroduction

Spectral deconvolution estimates the number, position, and variance of peaks by regressing the spectra obtained by irradiating materials with X-rays or visible light as a sum of basis functions. This method is crucial for evaluating material properties and chemical structures.
Mass spectrometry[12]is used to determine the molecular weight, whereas infrared (IR) spectroscopy[8,4]and Raman spectroscopy[19]are used to investigate the physical properties and chemical structure of synthesized compounds. Spectral deconvolution enables the identification of the molecular weight and partial structures.
Molecular bonding can be evaluated using the nuclear magnetic resonance spectra[5], whereas X-ray diffraction (XRD) determines the lattice constants and atomic arrangements in crystals[14]by obtaining and deconvolving the spectra.
The properties and chemical structures of materials are determined by measuring the spectra and deconvoluting them into their components.
The automation of processes such as material synthesis and spectral measurement has led to an increase in data requiring spectral deconvolution[3]. Despite these advancements, spectral analysis continues to depend to some extent on expert scientific interpretation[1,29]. The significance of spectral deconvolution, which seeks to promote objectivity and automation within an information science framework, is therefore being increasingly acknowledged.

Existing spectral deconvolution methods may struggle to determine spectral models, such as the number of peaks or the basis function model, for spectral data with complex peak shapes and overlapping peaks.
Estimating the number and shape of peaks is a fundamental requirement for achieving spectral deconvolution.
To improve this capability, Bayesian spectral deconvolution, which applies Bayesian inference to the problem, has been proposed.
Bayesian spectral deconvolution constructs a statistical model by applying Bayesian inference to a regression model that represents the spectrum as a sum of basis functions. This approach enables the estimation of spectral deconvolution model parameters, including the optimal number of peaks required to represent the spectral data[17].
Undesirable components such as high-intensity noise or substance-derived background often appear in spectral data owing to instrument errors, signal processing, or the measured sample and are problematic for analysis[9,32].
In fields lacking a well-defined physical model, the background model may not be well defined, complicating the spectral deconvolution analysis in some cases[6].
Model selection for various analyses, such as peak-number estimation, becomes difficult when the spectral data contain high-intensity noise or background[22]in conventional Bayesian spectral deconvolution.
Thus, existing methods have the drawback that spectral deconvolution becomes difficult when noise dominates or when the background component model is unknown.

However, researchers may achieve spectral deconvolution by applying domain-specific knowledge, even in scenarios where noise is prevalent or the background component model is not defined.
Scientists do not rely solely on the spectral data to analyze the spectra. Rather, they analyze the spectra in the context of the physical properties and chemical structure of the material and variations observed in other measurements collected during their analysis.
Correlations between the changes in material properties or chemical structure often result in shifts in the spectral peaks. These shifts help in identifying the key candidate peaks for analysis and highlight the spectral regions warranting further investigation.
Scientists have achieved spectral deconvolution by leveraging the insights gained from such knowledge, enabling them to extract peak structures buried in noise or appearing against unknown backgrounds[10].
Consequently, peak-number estimation and other spectral model selections are achievable even for complex spectral shapes[33].
The analytical approach used by scientists to focus on the important spectral regions based on the physical property values is crucial for analyzing spectra dominated by noise or where background components are not modeled.

We propose a spectral deconvolution framework that models the process followed by scientists, namely, using material properties and structures to identify the key regions, enabling robust peak estimation even in the presence of dominant noise or unknown backgrounds.
Several methods based on such scientific practices have already been developed.
A Bayesian analysis method for X-ray absorption near-edge structure spectra has been proposed, which improves the accuracy by assigning different model structures or prior distributions to each region, based on the knowledge that the peak-shape measurements differ across the energy regions[16].
Other studies have applied regression modeling to the relationship between the physical property values and peak structures derived from spectral deconvolution[11].
However, these approaches merely provide a framework in which spectral data analysis and knowledge extraction from auxiliary measurement data, such as physical properties, are conducted separately.
Integrating these two steps is expected to automate spectral deconvolution while enabling more comprehensive knowledge extraction of the relationship between the physical properties and spectra.
In this context, our proposed framework comprehensively models the analytical process followed by scientists for deconvoluting complex spectra, as follows.
First, we employ the Bayesian spectral deconvolution model mentioned above to model the spectral data.
Next, we model the practice of examining the relationship between peak structures derived from deconvolution and the physical properties or chemical structures as Gaussian process regression.
This approach aims to integrate the previously underutilized physical property information into the spectral deconvolution, enabling accurate model selection and parameter estimation even in complex spectra containing noise and background.
The proposed method was applied to the spectral deconvolution of synthetic spectral data and IR spectra of polylactic acid, a representative biodegradable polymer, to verify its effectiveness.

## IIMethod

## II.1Problem formulation

We address the problem of selecting spectral models, such as the number of peaks, by integrating the spectral data with physical prior knowledge. This knowledge includes the physical property value, as used by scientists.

We define the dataset used in the proposed method.
We consider the spectral data{xi,yi}i=1N\{x_{i},y_{i}\}_{i=1}^{N}consisting ofNNobservation points.xix_{i}represents the horizontal axis, such as wavenumber or wavelength;yiy_{i}represents the spectral intensity at that point.
We define a spectral dataset asY:={yi}i=1NY:=\{y_{i}\}_{i=1}^{N}. We assumeN′N^{\prime}spectral datasetsYj:={yi,j}i=1NY_{j}:=\{y_{i,{j}}\}_{i=1}^{N}(j=1,…,N′j=1,\dots,N^{\prime}) sharing the observation points{xi}i=1N\{x_{i}\}_{i=1}^{N}but representing distinct physical states, such as datasets containing material properties.
We define the paired dataset as𝒟={(Yjobs,zj)}j=1N′\mathcal{D}=\{(Y_{j}^{\mathrm{obs}},z_{j})\}_{j=1}^{N^{\prime}}, whereYjobsY_{j}^{\mathrm{obs}}is the observed spectrum of samplejjandzjz_{j}is the corresponding physical property.
This dataset𝒟\mathcal{D}constitutes the dataset assumed by the proposed method.

We formulate the problem of selecting a spectral modelMMby combining the spectral data𝒴\mathcal{Y}and physical prior knowledgeZZ(e.g., material properties), as follows.arg​maxMp​(M|Z,𝒴)\displaystyle\mathop{\rm arg\penalty 10000\ max}\limits_{M}p({M}|Z,\mathcal{Y})(1)

Note that we first formulate the problem in terms of the full Bayesian model posterior.
As shown below, this posterior can be decomposed into a spectrum-only evidence term and a physical-property-consistency term.
The proposed method then adopts the latter term as the model-selection criterion, in accordance with the aim of this study.

## II.2Model

This section presents a Bayesian hierarchical model for spectral deconvolution that incorporates physical property values, mirroring scientific practices (Figure1).
The proposed framework consists of two layers. The first is a spectral deconvolution model analyzing the spectrum. The second is a regression model that relates the physical property values to the spectral data.
After describing the individual layers, we explain the spectral deconvolution model of the process followed by scientists.

## II.2.1Spectral deconvolution model

The spectral deconvolution model represents the spectral data as a linear combination of basis functions, such as Gaussian functions.
The regression of spectral data using the spectral deconvolution model yields information such as the number of peaks, peak positions, and peak variances[17].
Consider the spectral data consisting ofNNobservations{xi,yi}i=1N\{x_{i},y_{i}\}_{i=1}^{N}.
The spectral deconvolution model, utilizing Gaussian basis functions subject to independent and identically distributed (i.i.d.) normal noise, is expressed as follows:Figure 1:Graphical model of the proposed method.MMdenotes the spectral model. For each samplejj, the spectral parameterθj\theta_{j}defines both the posterior predictive spectrumYjY_{j}and the observed spectrumYjobsY_{j}^{\mathrm{obs}}through the spectral likelihood model. The physical propertyZZis modeled by Gaussian process regression using the latent function valueFFconditioned on the spectral information. The red (blue) box indicates the components of spectral deconvolution (Gaussian process regression).p​(Y|θ)\displaystyle p(Y|\theta)=\displaystyle=∏i=1N12​π​σ​exp⁡(−(yi−g​(xi;θ))22​σ2).\displaystyle\prod_{i=1}^{N}\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_{i}-g(x_{i};\theta))^{2}}{2\sigma^{2}}\right).(2)

ggdenotes the spectral fitting function,θ\thetathe regression parameters, andσ\sigmathe standard deviation of the noise. The representative examples ofggincludeg​(x;θ)\displaystyle g(x;\theta)=\displaystyle=∑j=1Mwj​exp⁡(−(x−μj)22​aj2).\displaystyle\sum_{j=1}^{M}w_{j}\exp\left(-\frac{(x-\mu_{j})^{2}}{2a_{j}^{2}}\right).(3)

MMdenotes the number of peaks in the fitting model, andθ={wj,μj,aj}j=1M\theta=\{w_{j},\mu_{j},a_{j}\}_{j=1}^{M}represents the set of parameters.

## II.2.2Physical-property regression model

The physical-property regression model connects the spectral data to the corresponding physical property values.
We employed Gaussian process regression as the Bayesian physical-property regression model in this study.
In the physical-property regression model, a single sample constitutes a pair of spectral dataY:={yi}i=1NY:=\{y_{i}\}_{i=1}^{N}and a physical property valuezz.
This can be extended to multiple samples, as follows. Given a set of spectral and measurement data of sample sizeN′N^{\prime},{𝒴,Z}:={Yj,zj}j=1N′\{\mathcal{Y},Z\}:=\{Y_{j},z_{j}\}_{j=1}^{N^{\prime}}, the Gaussian process regression model[2]is formulated asp​(Z|F,𝒴)=(α2​π)N′2​exp⁡[−12​(Z−F)T​α​I​(Z−F)].\displaystyle{\it p}(Z|F,\mathcal{Y})=\left({\frac{\alpha}{2\pi}}\right)^{\frac{N^{\prime}}{2}}\exp\left[-\frac{1}{2}\left(Z-F\right)^{T}\alpha I\left(Z-F\right)\right].(4)

We defineF:=F​(𝒴)=(f​(Y1),…,f​(YN′))F:=F(\mathcal{Y})=(f(Y_{1}),\dots,f(Y_{N^{\prime}})). The prior distributionp​(F)p(F)is assumed to be anN′N^{\prime}-dimensional normal distribution with zero mean and covariance matrixKK. The hyperparameterα\alphadenotes the noise precision, which is the inverse of the noise variance in the likelihood model.p​(F)=(1(2​π)N′​|K|)1/2​exp⁡(−12​FT​K−1​F)\displaystyle p(F)=\left(\frac{1}{(2\pi)^{N^{\prime}}|K|}\right)^{1/2}\exp\left(-\frac{1}{2}F^{T}K^{-1}F\right)(5)

Here,k​(Yi,Yj)k(Y_{i},Y_{j})denotes a kernel function representing the similarity betweenYiY_{i}andYjY_{j}.

## II.2.3Model of spectral deconvolution process followed by scientists

We modeled the method followed by scientists for extracting high-precision information by analyzing the spectral data in combination with physical prior knowledge.
The simplest physical prior knowledge is the value of a property related to a spectrum.
Given the spectral data and corresponding physical properties, scientists analyze the spectral features, such as specific regions or peaks, that are correlated with variations in the physical properties.
The decision of scientists to focus on specific regions while down-weighting others corresponds to the operation of extracting only the dimensions of relevant variables.
Thus, the above represents a variable selection process in regression analysis, where the spectral intensities at each wavenumber serve as explanatory variables predicting the physical property values.
To reflect this requirement in the model, it is effective to model a predictive relationship in which spectral structures serve as explanatory variables for the physical property values.
Incorporating this perspective into the model, we treat spectral features as predictors of the physical properties, so that spectral components relevant to the target property are preferentially weighted during model selection. Introducing a causal link from the spectra to the physical properties enables predictive performance to guide spectral-structure estimation, ensuring that physically meaningful components are prioritized.

By mirroring this scientific spectral deconvolution process, the causal relationships can be modeled as depicted in the graphical model in Figure1.
Conventional spectral deconvolution methods focus solely on estimating the number of peaks and their parameters from the spectral data, without accounting for their causal relationships with the physical properties.
In contrast, the spectral deconvolution method followed by scientists estimates the number of peaks and their parameters while maintaining a causal link between the spectral data and physical property values.
This represents a causal relationship in which specifying a spectral model (e.g., the number of peaks) and parameters (e.g., positions and variances) generates a spectrum from which the measured valuezzis derived.
The following statistical model is derived from this graphical model.p​(M,ϑ,𝒴,𝒴obs,F,Z)\displaystyle p(M,\vartheta,\mathcal{Y},\mathcal{Y}^{\text{obs}},F,Z)=\displaystyle=p​(Z|F,𝒴)​p​(F)​p​(𝒴|ϑ)\displaystyle{\it p}(Z|F,\mathcal{Y}){\it p}(F){\it p}(\mathcal{Y}|\vartheta)(6)×p​(𝒴obs|ϑ)​p​(ϑ|M)​p​(M).\displaystyle\times{\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta){\it p}(\vartheta|M){\it p}(M).

Here, letϑ:={θj}j=1N′\vartheta:=\{\theta_{j}\}_{j=1}^{N^{\prime}}; then,p​(𝒴|ϑ),p​(𝒴obs|ϑ),p​(ϑ|M){\it p}(\mathcal{Y}|\vartheta),{\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta),{\it p}(\vartheta|M)are defined as follows:p​(𝒴|ϑ):=∏j=1N′p​(Yj|θj),\displaystyle{\it p}(\mathcal{Y}|\vartheta):=\prod_{j=1}^{N^{\prime}}{\it p}(Y_{j}|\theta_{j}),(7)p​(𝒴obs|ϑ):=∏j=1N′p​(Yjobs|θj),\displaystyle{\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta):=\prod_{j=1}^{N^{\prime}}{\it p}(Y^{\mathrm{obs}}_{j}|\theta_{j}),(8)p​(ϑ|M):=∏j=1N′p​(θj|M).\displaystyle{\it p}(\vartheta|M):=\prod_{j=1}^{N^{\prime}}{\it p}(\theta_{j}|M).(9)

Given the spectral data𝒴obs\mathcal{Y}^{\mathrm{obs}}and property valuesZZ, the posteriorp​(M|Z,𝒴obs)p(M|Z,\mathcal{Y}^{\mathrm{obs}})for the spectral modelMMis obtained by marginalizing the joint probability.p​(M|Z,𝒴obs)\displaystyle p(M|Z,\mathcal{Y}^{\mathrm{obs}})∝p​(Z,𝒴obs,M)\displaystyle\propto p(Z,\mathcal{Y}^{\mathrm{obs}},M)=∫𝑑F​𝑑𝒴​𝑑ϑ​p​(Z,F,𝒴,𝒴obs,ϑ,M)\displaystyle=\int dFd\mathcal{Y}d\vartheta p(Z,F,\mathcal{Y},\mathcal{Y}^{\mathrm{obs}},\vartheta,M)(10)

Rearranging the marginalization integral leads to the following interpretable form.p​(M|Z,𝒴obs)\displaystyle p(M|Z,\mathcal{Y}^{\mathrm{obs}})∝∫𝑑𝒴​[{∫𝑑F​p​(Z|F,𝒴)​p​(F)}​{∫𝑑ϑ​p​(𝒴|ϑ)​p​(𝒴obs|ϑ)​p​(ϑ|M)}​p​(M)]\displaystyle\propto\int d\mathcal{Y}\,\left[\left\{\int dF\>p(Z|F,\mathcal{Y})p(F)\right\}\left\{{{\int d\vartheta\,p(\mathcal{Y}|\vartheta){\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta)p(\vartheta|M)}}\right\}p(M)\right]=∫𝑑𝒴​p​(Z|𝒴)​{∫𝑑ϑ​p​(𝒴|ϑ)​p​(ϑ|𝒴obs,M)}​p​(𝒴obs|M)​p​(M)\displaystyle=\int d\mathcal{Y}\>p(Z|\mathcal{Y})\left\{{{\int d\vartheta\,p(\mathcal{Y}|\vartheta){\it p}(\vartheta|\mathcal{Y}^{\mathrm{obs}},M)}}\right\}{\it p}(\mathcal{Y}^{\mathrm{obs}}|M)p(M)(11)=p​(𝒴obs|M)​p​(M)​∫𝑑𝒴​p​(Z|𝒴)​p​(𝒴|𝒴obs,M)\displaystyle={\it p}(\mathcal{Y}^{\mathrm{obs}}|M)p(M)\int d\mathcal{Y}\>p(Z|\mathcal{Y})p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)(12)=p​(𝒴obs|M)​p​(M)​Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)],\displaystyle=p(\mathcal{Y}^{\mathrm{obs}}|M)p(M)E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right],(13)

where, theϑ\varthetaintegral marginalizes the spectral deconvolution model, theFFintegral marginalizes the Gaussian process regression model, and the𝒴\mathcal{Y}integral marginalizes over the connection between layers in the hierarchical Bayesian spectral deconvolution model for scientists.
Each marginalization will be explained in the next section.

Assuming a uniform prior ofp​(M)p(M)over candidate models, model comparison based onp​(M|Z,𝒴obs)p(M|Z,\mathcal{Y}^{\mathrm{obs}})is equivalent to comparison based on the model evidencep​(Z,𝒴obs|M)p(Z,\mathcal{Y}^{\mathrm{obs}}|M).
Equation (13) shows that the full Bayesian model evidence can be decomposed into two conceptually distinct contributions:p​(Z,𝒴obs|M)=p​(𝒴obs|M)​Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)].p(Z,\mathcal{Y}^{\mathrm{obs}}|M)=p(\mathcal{Y}^{\mathrm{obs}}|M)E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right].(14)

The first contribution is the spectrum-only evidencep​(𝒴obs|M)p(\mathcal{Y}^{\mathrm{obs}}|M), which evaluates how well the candidate spectral modelMMexplains the observed spectra themselves.
The second contribution is the physical-property consistency term,Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)],E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right],(15)

which evaluates whether the latent spectral structures inferred under modelMM, after conditioning on the observed spectra, can consistently explain the physical-property values.
This distinction becomes explicit by taking the negative logarithm of the model evidence.
The full Bayesian free energy is defined asF​Efull​(M)=−log⁡p​(Z,𝒴obs|M).FE_{\mathrm{full}}(M)=-\log p(Z,\mathcal{Y}^{\mathrm{obs}}|M).(16)

Using the decomposition above, this free energy can be written asF​Efull​(M)=F​Espec​(M)+F​Ephys​(M),FE_{\mathrm{full}}(M)=FE_{\mathrm{spec}}(M)+FE_{\mathrm{phys}}(M),(17)

whereF​Espec​(M)=−log⁡p​(𝒴obs|M)FE_{\mathrm{spec}}(M)=-\log p(\mathcal{Y}^{\mathrm{obs}}|M)(18)

is the spectrum-only Bayesian free energy, andF​Ephys​(M)=−log⁡p​(Z|𝒴obs,M)=−log⁡Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)]FE_{\mathrm{phys}}(M)=-\log p(Z|\mathcal{Y}^{\mathrm{obs}},M)=-\log E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right](19)

is the physical-property-consistency free energy.
These two terms evaluate different aspects of the candidate model:F​EspecFE_{\mathrm{spec}}measures the fit to the observed spectra, whereasF​EphysFE_{\mathrm{phys}}measures the consistency between the inferred spectral structures and the physical-property values.
The purpose of this study is not to select the spectral model that best fits the observed spectra alone, but to select the model whose inferred spectral structures are most informative for the physical-property values.
Therefore, in the proposed method, we use the physical-property-consistency term as the model-selection criterion.
We define the physical-property-informed model posterior asp~​(M|Z,𝒴obs)∝Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)].\tilde{p}(M|Z,\mathcal{Y}^{\mathrm{obs}})\propto E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right].(20)

The corresponding physical-property-informed free energy is defined asF​E~​(M)=−log⁡p~​(M|Z,𝒴obs).\widetilde{FE}(M)=-\log\tilde{p}(M|Z,\mathcal{Y}^{\mathrm{obs}}).(21)

In the proposed method, the candidate spectral model with the smallestF​E~​(M)\widetilde{FE}(M)is selected.

## II.3Posterior inference for the model

Estimating the physical-property-informed model posteriorp~​(M|Z,𝒴obs)\tilde{p}(M|Z,\mathcal{Y}^{\mathrm{obs}})for the scientific spectral model, which encodes the physical properties, requires evaluating the marginalization integrals overθ\theta,FF, and𝒴\mathcal{Y}, as detailed in Eq. (13).
These operations correspond to the marginalization within the spectral deconvolution model, Gaussian process regression model, and interface linking the two layers.
Marginalization proceeds sequentially overϑ\vartheta,FF, and𝒴\mathcal{Y}.
This section presents the method for each step in this sequence.

## II.3.1Marginalization of spectral deconvolution model

The method for sampling from the posterior of the spectral deconvolution model using Replica Exchange Monte Carlo is described here.
The purpose of the marginalization calculation for the spectral deconvolution model,∫𝑑θ​p​(𝒴|ϑ)​p​(𝒴obs|ϑ)​p​(ϑ|M)\int d\theta\,p(\mathcal{Y}|\vartheta){\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta)\,p(\vartheta|M), is to compute a sample set from the predictive distributionp​(𝒴|𝒴obs)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}}).
Sampling from this predictive distributionp​(𝒴|𝒴obs)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}})can be achieved using the following procedure, as seen in Eq. (11).
The method proceeds by first drawing the parametersϑ\varthetafrom the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M). Then, sampling𝒴\mathcal{Y}from the spectral deconvolution likelihoodp​(𝒴|ϑ)p(\mathcal{Y}|\vartheta)(Eq. (2)) conditioned on these values yields the sample set from the predictive distributionp​(𝒴|𝒴obs)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}}).
Because the likelihood functionp​(𝒴|ϑ)p(\mathcal{Y}|\vartheta)is Gaussian, sampling from it is numerically straightforward. Therefore, the primary computational challenge lies in sampling from the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M).

Sampling from posterior distributions in high-dimensional statistical models is often performed using Markov chain Monte Carlo methods. Because posterior distributions in spectral deconvolution can be strongly multimodal, standard Metropolis–Hastings sampling[13]may require many iterations to move between modes and can converge slowly[21,24].
This study employed the Replica Exchange Monte Carlo (REMC) method, an extended-sampling method[15], to address these sampling challenges.
Constructing an extended artificial ensemble and exchanging states can efficiently enhance Markov chain mixing using extended-sampling methods[15].
We employed an established approach[17]that marginalizes the spectral model while avoiding this difficulty.

Sampling from the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M)for the spectral deconvolution model does not require the simultaneous use of all spectral data.
The likelihood functionp​(𝒴obs|ϑ)p(\mathcal{Y}^{\mathrm{obs}}|\vartheta)factorizes into the individual spectral likelihoodsp​(Yjobs|θ)p({Y_{j}}^{\mathrm{obs}}|\theta), as shown in Eq. (8).
By Bayes’ theorem, the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M)is proportional to the likelihood functionp​(𝒴obs|ϑ)​p​(ϑ|M){\it p}(\mathcal{Y}^{\mathrm{obs}}|\vartheta)p(\vartheta|M). Therefore, the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M)also corresponds to the product of the posterior distributionsp​(θ|Yjobs){\it p}(\theta|{Y_{j}}^{\mathrm{obs}})for individual spectra.
Sampling from the posterior distributionp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M)can be achieved by sampling from the posterior distribution of the individual spectrap​(θ|Yjobs){\it p}(\theta|{Y_{j}}^{\mathrm{obs}}).
Hence, we describe a method for sampling from the posterior distributionp​(θ|Yjobs){\it p}(\theta|{Y_{j}}^{\mathrm{obs}})of a single spectral data pointYobs:=YjobsY^{\mathrm{obs}}:=Y_{j}^{\mathrm{obs}}using the replica exchange method.

Building on this, we define the probability distributionp​(θ|Yobs,M)p(\theta|Y^{\mathrm{obs}},M)by introducing the inverse temperature parameterβ\betainto the probability distributionpβ​(θ|Yobs,M)p_{\beta}(\theta|Y^{\mathrm{obs}},M)of the parameter set.pβ​(θ|Yobs,M)p_{\beta}(\theta|Y^{\mathrm{obs}},M)is calculated aspβ​(θ|Yobs,M)∝exp⁡(−N​β​E​(θ,M))​p​(θ),\displaystyle p_{\beta}(\theta|Y^{\mathrm{obs}},M)\propto\exp(-N\beta E(\theta,M))p(\theta),(22)E​(θ,M):=12​N​σ2​∑i=1N(yi−g​(xi;θ,M))2.\displaystyle E(\theta,M):=\frac{1}{2N\sigma^{2}}\sum_{i=1}^{N}(y_{i}-g(x_{i};\theta,M))^{2}.(23)

As can be seen from this equation, whenβ=1\beta=1, the sampling matches the target distributionp​(θ|Yobs)p(\theta|Y^{\mathrm{obs}}).
However, reducingβ\betacorresponds to sampling from the prior distribution as the distribution approaches it.
REMC is an efficient method for simultaneous sampling from different temperaturesβl\beta_{l}, enabling the simultaneous distribution of the parameter values{θl}l=1L\{\theta_{l}\}_{l=1}^{L}corresponding toβl\beta_{l}to be obtained.P​(θ1,θ2​⋯​θL|Yobs,M)=∏l=1LPβl​(θl|Yobs,M){\it P}(\theta_{1},\theta_{2}\cdots\theta_{L}|Y^{\mathrm{obs}},M)=\prod_{l=1}^{L}{\it P}_{\beta_{l}}(\theta_{l}|Y^{\mathrm{obs}},M)(24)

is sampled by repeating the following procedure.
- 1

Sampling from the individual distributionp​(θl|Yobs,βl){\it p}(\theta_{l}|Y^{\mathrm{obs}},\beta_{l})

By using sampling methods such as the Metropolis–Hastings algorithm[13], we sample the parameterθl\theta_{l}frompβl​(θl|Yobs,M){\it p}_{\beta_{l}}(\theta_{l}|Y^{\mathrm{obs}},M).
- 2

Probabilistically swap sampling at eachβ\beta

Swapθl\theta_{l}andθl+1\theta_{l+1}with the probabilitymin⁡(1,r)\min(1,r).r=p​(θ1,⋯,θl+1,θl,⋯,θL|Yobs,M)p​(θ1,⋯,θl,θl+1,⋯,θL|Yobs,M)=pβl​(θl+1|Yobs,M)​pβl+1​(θl|Yobs,M)pβl​(θl|Yobs,M)​pβl+1​(θl+1|Yobs,M)=exp⁡{N​[βl+1−βl]​[E​(θl+1,M)−E​(θl,M)]}\begin{split}\;\;\;\;\;r&=\frac{{\it p}(\theta_{1},\cdots,\theta_{l+1},\theta_{l},\cdots,\theta_{L}|Y^{\mathrm{obs}},M)}{{\it p}(\theta_{1},\cdots,\theta_{l},\theta_{l+1},\cdots,\theta_{L}|Y^{\mathrm{obs}},M)}\\
&=\frac{{\it p}_{\beta_{l}}(\theta_{l+1}|Y^{\mathrm{obs}},M){\it p}_{\beta_{l+1}}(\theta_{l}|Y^{\mathrm{obs}},M)}{{\it p}_{\beta_{l}}(\theta_{l}|Y^{\mathrm{obs}},M){\it p}_{\beta_{l+1}}(\theta_{l+1}|Y^{\mathrm{obs}},M)}\\
&=\exp\left\{N[\beta_{l+1}-\beta_{l}][E(\theta_{l+1},M)-E(\theta_{l},M)]\right\}\end{split}(25)

Exchanging the states across multiple inverse temperaturesβ\betahelps the sampling to converge faster forp​(θ|𝒴obs)p(\theta|\mathcal{Y}^{\mathrm{obs}})atβ=1\beta=1.
Combining the samples from these spectral posteriorsp​(θ|𝒴obs,M)p(\theta|\mathcal{Y}^{\mathrm{obs}},M)creates the global posterior setp​(ϑ|𝒴obs,M)p(\vartheta|\mathcal{Y}^{\mathrm{obs}},M).
Finally, drawing𝒴\mathcal{Y}from the Gaussian likelihoodp​(𝒴|ϑ)p(\mathcal{Y}|\vartheta)using these parameters gives the final sample set{𝒴k}k=1Ns​a​m​p\{\mathcal{Y}_{k}\}_{k=1}^{N_{samp}}. This set forms the spectral predictive distributionp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)withNs​a​m​pN_{samp}samples.

## II.3.2Marginalization of Physical-Property Regression Models

This section describes the marginalization calculation for the physical-property regression model defined in Sec.II.2.2.
The spectral samples{Yk}k=1Nsamp\{Y_{k}\}_{k=1}^{N_{\mathrm{samp}}}drawn fromp​(Y|ϑ)p(Y|\vartheta)are combined with the measurement dataZZto form the dataset{𝒴k,Z}k=1Ns​a​m​p\{\mathcal{Y}_{k},Z\}_{k=1}^{N_{samp}}.Ns​a​m​pN_{samp}denotes the sample size drawn from the predictive distributionp​(𝒴|ϑ)p(\mathcal{Y}|\vartheta).
While performing this calculation, it is important to note that the physical propertyZZdoes not change across the sampleskk.
For each sampled set{𝒴k,Z}\left\{\mathcal{Y}_{k},Z\right\}, the marginal likelihoodp​(Z|𝒴k)p(Z|\mathcal{Y}_{k})can be analytically computed, as follows.
Denoting theN′×N′N^{\prime}\times N^{\prime}identity matrix asIN′I_{N^{\prime}}and definingΛ=K+α−1​IN′\Lambda=K+\alpha^{-1}I_{N^{\prime}}, Gaussian process regression yields the conditional probabilityp​(Z|𝒴k)p(Z|{\mathcal{Y}}_{k})after integrating outFF, as shown in the following equation.p​(Z|𝒴k)=∫𝑑F​p​(Z|F,𝒴k)​p​(F)\displaystyle p(Z|{\mathcal{Y}}_{k})=\int dFp(Z|F,{\mathcal{Y}}_{k})p(F)(26)=\displaystyle=(12​π)N′/2​|Λ−1|1/2​exp⁡{−12​ZT​Λ−1​Z}\displaystyle\left(\frac{1}{2\pi}\right)^{N^{\prime}/2}|\Lambda^{-1}|^{1/2}\exp\left\{-\frac{1}{2}Z^{T}\Lambda^{-1}Z\right\}

Thus, the set ofNs​a​m​pN_{samp}marginalized likelihoodsp​(Z|𝒴k)p(Z|\mathcal{Y}_{k}), denoted as{p​(Z|𝒴k)}k=1Ns​a​m​p\{p(Z|\mathcal{Y}_{k})\}_{k=1}^{N_{samp}}, is obtained.

## II.3.3Marginalization of models of spectral deconvolution processes used by scientists

Marginalization over𝒴\mathcal{Y}means taking the expectation (average value) ofp​(Z|𝒴)p(Z|\mathcal{Y})with respect to the probability distributionp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M), where𝒴\mathcal{Y}is the set of all possible values,𝒴obs\mathcal{Y}^{\mathrm{obs}}represents the observed values, andMMdenotes the model. This is shown in the following equation.p~​(M|Z,𝒴obs)\displaystyle\tilde{p}(M|Z,\mathcal{Y}^{\mathrm{obs}})∝∫𝑑𝒴​p​(Z|𝒴)​p​(𝒴|𝒴obs,M)\displaystyle\propto\int d\mathcal{Y}\ p(Z|\mathcal{Y})p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)=Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)]\displaystyle=E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right](27)

The expectation in Eq. (II.3.3) was evaluated by Monte Carlo averaging over the sampling set{p​(Z|𝒴k)}k=1Nsamp\{p(Z|\mathcal{Y}_{k})\}_{k=1}^{N_{\mathrm{samp}}}.
Here, each𝒴k\mathcal{Y}_{k}was sampled from the predictive distributionp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M),
which was generated using the sampling sequence of the parameter setϑ\varthetaobtained from the spectral deconvolution model.
Thus, the physical-property-informed model posterior was approximated asp~​(M|Z,𝒴obs)∝Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)]≈1Nsamp​∑k=1Nsampp​(Z|𝒴k).\tilde{p}(M|Z,\mathcal{Y}^{\mathrm{obs}})\propto E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right]\approx\frac{1}{N_{\mathrm{samp}}}\sum_{k=1}^{N_{\mathrm{samp}}}p(Z|\mathcal{Y}_{k}).(28)

Building on this approximation, computing the physical-property-informed free energy (FE~\widetilde{\rm FE}) asF​E~​(M)=−log⁡Ep​(𝒴|𝒴obs,M)​[p​(Z|𝒴)]≈−log⁡[1Nsamp​∑k=1Nsampp​(Z|𝒴k)]\widetilde{FE}(M)=-\log E_{p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)}\left[p(Z|\mathcal{Y})\right]\approx-\log\left[\frac{1}{N_{\mathrm{samp}}}\sum_{k=1}^{N_{\mathrm{samp}}}p(Z|\mathcal{Y}_{k})\right]

enables spectral model selection.

## IIIDemonstration

This section evaluates the effectiveness of the proposed method.
As outlined in the Introduction, the proposed method estimates the number of peaks in complex spectra dominated by noise or where the background component model remains unknown.
Therefore, we generated artificial datasets characterized by either noise dominance or an unknown background to verify the effectiveness of the proposed method.
The proposed method was applied to actual measurement data—the IR spectra of polylactic acid—to demonstrate its effectiveness in practical environments.
We compared the results with those of an existing Bayesian spectral deconvolution method, which relies solely on spectral data without considering physical properties.
The detailed results for each experimental case are presented below.

## III.1Validation Using Noise-Dominant Synthetic Data

To evaluate whether the proposed method can robustly estimate the number of peaks even when noise is as dominant as the signal, we verified the effectiveness of the proposed method using noise-dominated artificial spectral data.
This dataset, comprising paired spectra and physical property values, was generated as follows.
First, we generated the spectral data{xi,yi}i=1N\{x_{i},y_{i}\}_{i=1}^{N}featuring two distinct peaks.
The position of the first peakμ1\mu_{1}was drawn from a uniform distribution over the range3.5≦x≦4.753.5\leqq x\leqq 4.75, with its intensityw1w_{1}comparable to the noise standard deviation (σ=0.2\sigma=0.2).
The position of the second peak,μ2\mu_{2}, fell within5.25≦x≦6.55.25\leqq x\leqq 6.5, whereas its intensityw2w_{2}was uniformly sampled in the range1.0≦w2≦5.01.0\leqq w_{2}\leqq 5.0to ensure it was significantly larger than the noise.
The measurement domain consisted of 600 equally spaced pointsxix_{i}in the interval3.0≤x≤7.03.0\leq x\leq 7.0, resulting in a total sample size ofN=600N=600.
Based on this configuration, six spectral sets were generated by randomly varying the peak positions within the specified interval and intensities within the specified ranges, according to the criteria described above.
We defined the physical propertyΔ\Deltaof each spectrum as equaling ten times the peak separation:Δ=10​|μ1−μ2|\Delta=10|\mu_{1}-\mu_{2}|.
This procedure yielded the spectral dataset𝒴∈ℝ600×6\mathcal{Y}\in\mathbb{R}^{600\times 6}containingN′=6N^{\prime}=6spectra, each withN=600N=600data points. We concurrently defined the physical property vectorZ=(z1=Δ1,z2=Δ2,…,z6=Δ6)∈ℝ6Z=(z_{1}=\Delta_{1},z_{2}=\Delta_{2},\dots,z_{6}=\Delta_{6})\in\mathbb{R}^{6}.

The parameter settings and prior distributions for the proposed method are described below.
The spectral model parametersθ=(μ,a,w)\theta=(\mu,a,w)were given prior distributions for use in the marginalization of the spectral deconvolution model (Sec.II.3.1) and in generating the sampling sequence from the posterior distribution (Eq.22).
The priorp​(μ)p(\mu)for the peak positionμ\muwas uniform over3.25≦μ≦6.53.25\leqq\mu\leqq 6.5; the priorp​(a)p(a)for the peak widthaawas uniform over0.005≦a≦0.050.005\leqq a\leqq 0.05; and the priorp​(w)p(w)for the peak intensitywwwas uniform over0.2≦w≦50.2\leqq w\leqq 5.
A burn-in period of 5000 steps was used for the REMC method, followed by 15,000 sampling steps. The temperatures were set atL=40L=40withd=1.15d=1.15, andβl\beta_{l}followed the function proposed by Nagata et al.[28].βl={0.0for​l=1,dl−Lfor​l=2,3,…,L\beta_{l}=\begin{cases}0.0&\quad\text{for }l=1,\\
d^{{l-L}}&\quad\text{for }l=2,3,\dots,L\end{cases}(29)

In the marginalization of the regression model for the physical property value (SectionII.3.2), the following kernel function was used.k​(Yi,Yj):=C02​(1+|Yi−Yj|222​C1​C22)−C1\displaystyle k(Y_{i},Y_{j}):=C_{0}^{2}\left(1+\frac{\left|Y_{i}-Y_{j}\right|_{2}^{2}}{2C_{1}C_{2}^{2}}\right)^{-C_{1}}(30)

The kernel hyperparameters{C0,C1,C2}\{C_{0},C_{1},C_{2}\}were estimated using the empirical Bayes method. These parameters maximize the likelihood functionp​(Z|𝒴isample)p(Z|\mathcal{Y}^{\rm sample}_{i}).
The sampling sequence for the spectral predictive distributionp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)was calculated during the marginalization of the model encapsulating the analytical approach used by scientists (Sec.II.3.3). This calculation used the sampling sequence of the vectorϑ\vartheta, which is composed of the parametersθ\theta.
The sequence ofϑ\varthetawas extracted at five-step intervals to minimize the correlation. This procedure ensured that the samples were i.i.d.
The expected value ofp​(Z|𝒴)p(Z|\mathcal{Y})was computed based onp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)(Eq. (II.3.3)).
The number of sampling sequences forp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)was set to 100. This setting balances the computational efficiency with rapid convergence in the expectation calculation.Figure 2:Noise-dominant synthetic spectral dataset used to validate the proposed method. Panels (a)–(f) show six samples generated under different conditions. In each panel, the blue solid line represents the observed spectrumYY, which was generated by adding high-intensity Gaussian noise to two Gaussian peaks. The left peak is completely buried in the noise, reproducing a situation in which peak estimation is difficult when using conventional methods. The red dashed lines indicate the true peak positions(μ1,μ2)(\mu_{1},\mu_{2}), and the physical property valueΔ\Deltashown above each panel is defined asΔ=10​|μ2−μ1|\Delta=10|\mu_{2}-\mu_{1}|.Table 1:Comparison of model-selection results for the noise-dominant synthetic spectral dataset. For each candidate model, the table shows the Bayesian free energyF​EFEcalculated by conventional Bayesian spectral deconvolution, the physical-property-informed free energyF​E~\widetilde{FE}calculated by the proposed method, and the corresponding model probabilities obtained by normalizingexp⁡[−F​E​(M)]\exp[-FE(M)]orexp⁡[−F​E~​(M)]\exp[-\widetilde{FE}(M)]over candidate models.Bayesian spectral deconvolutionProposed methodModelFEProbability𝐅𝐄~\mathbf{\widetilde{FE}}Probability1-peak4.255×1034.255\times 10^{3}1.03.977×1033.977\times 10^{3}02-peak4.347×1034.347\times 10^{3}03.962×1033.962\times 10^{3}1.0Figure 3:Example of fitting curves at the maximum a posteriori (MAP) solution for a synthetic spectrum (Δ=18.38\Delta=18.38). Panels (a) and (b) show the fitting results for the 1-peak and 2-peak models. The blue line represents the observed spectrum, and the orange dashed line represents the fitting curve at the MAP solution for each candidate model.

The conventional Bayesian spectral deconvolution method and the proposed method were applied to the generated dataset{𝒴,Z}\{\mathcal{Y},Z\}.
The conventional method selected a single-peak spectral model, whereas the proposed method correctly selected a two-peak model (Table1).
Fig.3presents the fitting results for the MAP solutions of each model.
The MAP solution is the estimate of the parameterθ\thetamaximizing the posterior distributionp​(θ|Y)p(\theta|Y)given the observed dataYY.
The spectral deconvolution model assumes uniform prior distributions. The calculation of the MAP solutionθMAP\theta_{\rm MAP}reduces to the maximization of the log-likelihood function.
Taking the logarithm of Eq. (2) yields the following expression.log⁡p​(Y|θ)\displaystyle\log p(Y|\theta)=\displaystyle=∑i=1N(−(yi−g​(xi;θ))22​σ2−log⁡(2​π​σ))\displaystyle\sum_{i=1}^{N}\left(-\frac{(y_{i}-g(x_{i};\theta))^{2}}{2\sigma^{2}}-\log(\sqrt{2\pi}\sigma)\right)(31)

The second term on the right-hand side is a constant independent ofθ\theta. Maximizing this expression is equivalent to minimizing the squared error term∑i=1N(yi−g​(xi;θ))2\sum_{i=1}^{N}(y_{i}-g(x_{i};\theta))^{2}.
The MAP solution minimizes the discrepancy between the spectral data and fitted curve.
The proposed method correctly estimates the true peak positions and intensities (Fig.3).
The conventional method struggles with noise-dominant spectral data, where the peak and noise intensities are comparable. However, the proposed method effectively estimates the number of peaks in these challenging scenarios. These results confirm the validity of the approach for peak estimation.

## III.2Validation Using Synthetic Data with Unknown Backgrounds

The effectiveness of the proposed method was verified using artificial spectral data, which simulated spectra containing unknown background components.
The artificial dataset contained pairs of spectra and physical property values. The generation process is described below.
The spectral data{xi,yi}i=1N\{x_{i},y_{i}\}_{i=1}^{N}were constructed with two distinct peaks.
The first peak positionμ1\mu_{1}follows a uniform distribution over3.5≦x≦4.03.5\leqq x\leqq 4.0. Its intensityw1w_{1}was randomly sampled from a uniform distribution over0.1≦w1≦0.20.1\leqq w_{1}\leqq 0.2. The second peak positionμ2\mu_{2}is located within5.5≦x≦6.05.5\leqq x\leqq 6.0. Its intensityw2w_{2}was also drawn from a uniform distribution over0.1≦w2≦0.20.1\leqq w_{2}\leqq 0.2.
Six hundred measurement pointsxix_{i}were distributed at equal intervals between3.0≦x≦7.03.0\leqq x\leqq 7.0.
The total number of sample points,NN, in the spectral data was 600.
Each spectrum was generated by first adding a background component based on a sigmoid function.
This background,B​(x)B(x), was defined using the parameters of amplitudeAA, slopess, and center positioncc, as follows:B​(x)=A1+exp⁡(−s​(x−c))B(x)=\frac{A}{1+\exp(-s(x-c))}

.
The parametersAA,ss, andccwere randomly sampled from the following uniform distributions:0.15≦A≦0.200.15\leqq A\leqq 0.20,4≦s≦64\leqq s\leqq 6, and4.8≦c≦5.24.8\leqq c\leqq 5.2. This background component was then added to the peak signals and noise.
The spectral deconvolution assumed that the background structure was unknown to verify the effectiveness of the method.
Six spectral samples were generated by randomly varying the peak positions, intensities, and background shapes.
The physical propertyΔ\Deltawas defined as ten times the peak separation:Δ=10​|μ1−μ2|\Delta=10|\mu_{1}-\mu_{2}|.
The resulting dataset𝒴∈ℝ600×6\mathcal{Y}\in\mathbb{R}^{600\times 6}consisted ofN′=6N^{\prime}=6spectra withN=600N=600data points each. The corresponding physical property values areZ=(z1=Δ1,z2=Δ2,…,z6=Δ6)∈ℝ6Z=(z_{1}=\Delta_{1},z_{2}=\Delta_{2},\dots,z_{6}=\Delta_{6})\in\mathbb{R}^{6}.

The spectral deconvolution process assumed an unknown background model. The asymmetric least squares (AsLS) method performed background removal without any specific model assumptions.
The AsLS method applies asymmetric weighting to the residuals between the observed data and estimated values[7]. This approach eliminates the influence of the peak components. The procedure estimates a smooth background without requiring a prior model.
This technique optimizes the tradeoff between the data fit and background smoothness.
The method estimates the backgroundBe​s​t={bi}i=1NB_{est}=\{b_{i}\}_{i=1}^{N}minimizing the following objective functionSS:S=∑i=1Nwi​(yi−bi)2+λ​∑i=1N(Δ2​bi)2S=\sum_{i=1}^{N}w_{i}(y_{i}-b_{i})^{2}+\lambda\sum_{i=1}^{N}(\Delta^{2}b_{i})^{2}

,
whereΔ2\Delta^{2}denotes the second-order difference operator, andwiw_{i}is an asymmetric weight determined by the sign of the residual.
For data points above the background (yi>biy_{i}>b_{i}), the weight is set towi=pw_{i}=p, andwi=1−pw_{i}=1-pfor all other cases.λ\lambdaandppdenote the smoothing and asymmetry parameters, respectively.
In this verification, the parameters for the AsLS method were set toλ=1000\lambda=1000andp=0.0001p=0.0001.
Although the AsLS method is a powerful technique for subtracting unknown backgrounds, it has certain limitations. It may fail to completely remove the background or mistakenly eliminate actual spectral peak structures if the smoothing parameter is set inappropriately, if spectral smoothness varies significantly across the regions, or if the background and peak structures share similar smoothness characteristics.

The proposed method was applied to the preprocessed dataset.
Here, we describe the parameter settings and prior distributions used in its application.
In the marginalization of the spectral deconvolution model (Sec.II.3.1), uniform prior distributions were assigned to obtain the sampling sequence from the posterior distribution (Eq.22) of the spectral model parametersθ=(μ,a,w)\theta=(\mu,a,w), as follows.
Specifically, the prior distributions for the peak positionp​(μ)p(\mu), peak intensityp​(w)p(w), and peak widthp​(a)p(a)were set as uniform distributions over the ranges3.5≤μ≤6.53.5\leq\mu\leq 6.5,0.001≤w≤0.50.001\leq w\leq 0.5, and0.005≤a≤0.180.005\leq a\leq 0.18, respectively.
Furthermore, in the REMC method used for sampling, the burn-in period was set to 5000 steps, followed by 15,000 sampling steps.
The number of temperatures was set toL=40L=40andd=1.26d=1.26. Following the research by Nagata et al.[28],βl\beta_{l}was set according to Eq. (29).Figure 4:Synthetic spectral dataset containing unknown background components. Panels (a)–(f) show six different spectra generated by adding a sigmoidal background and Gaussian noise to two Gaussian peaks. The red dotted lines indicate the true peak positionsμ1\mu_{1}andμ2\mu_{2}, andΔ\Deltashown in the heading is defined as10​|μ2−μ1|10|\mu_{2}-\mu_{1}|.Figure 5:Synthetic spectral dataset prior to background subtraction. This figure displays the raw, unprocessed spectra containing unknown sigmoidal background components, generated to evaluate the robustness of the analytical method under baseline fluctuations. Panels (a)–(f) simulate varying observational conditions by combining two ideal Gaussian peaks with a nonlinear sigmoidal background and observational Gaussian noise. The red dotted lines indicate the true peak center positions,μ1\mu_{1}andμ2\mu_{2}. The valueΔ\Deltashown in each title is defined as ten times the peak separation,Δ=10​|μ2−μ1|\Delta=10|\mu_{2}-\mu_{1}|. These pre-correction data serve as a reference to visually demonstrate how the degree of peak overlap (varyingΔ\Delta) and the gradient of the background affect the overall spectral profile and complicate subsequent peak detection processes.Table 2:Comparison of peak-number model selection for synthetic spectra containing unknown background components. For each candidate model, the table shows the Bayesian free energyF​EFEcalculated by conventional Bayesian spectral deconvolution, the physical-property-informed free energyF​E~\widetilde{FE}calculated by the proposed method, and the corresponding model probabilities obtained by normalizingexp⁡[−F​E​(M)]\exp[-FE(M)]orexp⁡[−F​E~​(M)]\exp[-\widetilde{FE}(M)]over candidate models.Bayesian spectral deconvolutionProposed methodModelFEProbabilityFE~\widetilde{\rm FE}Probability2-peak9.503×1039.503\times 10^{3}0.01.320×1031.320\times 10^{3}0.733-peak6.432×1036.432\times 10^{3}1.01.321×1031.321\times 10^{3}0.27

The marginalization of the physical-property regression model (Sec.II.3.2) utilized the following kernel function:k​(Yi,Yj):=C02​exp⁡(−|Yi−Yj|222​C12).\displaystyle k(Y_{i},Y_{j}):=C_{0}^{2}\exp\left(-\frac{\left|Y_{i}-Y_{j}\right|_{2}^{2}}{2C_{1}^{2}}\right).(32)

The kernel hyperparameters{C0,C1}\{C_{0},C_{1}\}were estimated using the empirical Bayes method. These parameters maximize the likelihood functionp​(Z|𝒴isample)p(Z|\mathcal{Y}^{\rm sample}_{i}).
The marginalization of the model representing the approach used by scientists calculated the sampling sequence for the spectral predictive distributionp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)(Sec.II.3.3).
This calculation utilized the sampling sequence of the vectorϑ\vartheta, which concatenates the parametersθ\thetaobtained by marginalizing the spectral deconvolution model for each spectrum.
The sequenceϑ\varthetawas extracted at 25-step intervals to minimize the correlations. This procedure ensured that the sequence is i.i.d.
The expected value ofp​(Z|𝒴)p(Z|\mathcal{Y})was computed based onp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)(Eq. (II.3.3)).
The rapid convergence of the expectation calculation and requirement for computational efficiency determine the sample size. The number of sampling sequences forp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\mathrm{obs}},M)was set to 100.

We compared the conventional Bayesian spectral deconvolution with the proposed method using the artificial dataset{𝒴,Z}\{\mathcal{Y},Z\}.
Background removal preprocessing generated pseudo-peak structures. The conventional method selected a three-peak spectral model containing these artifacts. The proposed method correctly selected a two-peak model (Table2).
The spectral deconvolution results obtained by the proposed method accurately estimated the true peak positions and intensities (Fig.6).
Conventional methods struggle with spectral data containing unknown backgrounds. The proposed approach effectively determines the number of peaks in these challenging scenarios. These results confirm the validity of the method for noise-dominant data with complex backgrounds.Figure 6:Example of fitting curves at the MAP solution for a synthetic spectrum (Δ=18.60\Delta=18.60). Panels (a) and (b) show the fitting results for the 2-peak and 3-peak models. The blue line represents the observed spectrum, and the orange dashed line represents the fitting curve at the MAP solution for each candidate model.

## III.3Application to IR spectral data

This study verified the effectiveness of the proposed method using actual IR spectra data of polylactic acid.
Crystallinity of a material signifies the ratio of its crystalline to amorphous phases. IR spectroscopy evaluates the degree of crystallinity[23], which governs the biodegradability of polylactic acid.
Degradation proceeds preferentially in amorphous regions, which are easily penetrated by water molecules and enzymes, whereas tightly packed molecular chains in crystalline regions inhibit degradation.
Understanding the microscopic crystalline state remains essential for predicting the biodegradability potential.
The wavenumber region from900​cm−1900\penalty 10000\ \mathrm{cm}^{-1}to1000​cm−11000\penalty 10000\ \mathrm{cm}^{-1}contains a group of low-intensity peaks[25], which respond sensitively to the polymer backbone conformation.
The peak at956​cm−1956\penalty 10000\ \mathrm{cm}^{-1}indicates amorphous structures, whereas the920​cm−1920\penalty 10000\ \mathrm{cm}^{-1}band marks regular helicalα\alphacrystals.
The balance between these regions indicates biodegradability. Accurate quantification relies on extracting small peaks in this region.
This study utilized 68 poly(lactic acid) samples synthesized under various crystallization temperatures and concentrations[30]. The dataset consisted of IR spectra from800​cm−1800\penalty 10000\ \mathrm{cm}^{-1}to1800​cm−11800\penalty 10000\ \mathrm{cm}^{-1}. It also included the degradation rates for each sample.
Previous studies report 14 peak structures in this specific wavenumber region[34,18].
The background of the poly(lactic acid) IR spectrum is generally unknown. Empirical preprocessing typically employs the AsLS method[35], which is a non-parametric technique for estimating the unknown background structure[26].
In this experiment, the existing spectral deconvolution methods and the proposed approach were applied to AsLS-preprocessed data. The verification focused on the extraction of peak structures between900​cm−1900\text{ cm}^{-1}and1000​cm−11000\text{ cm}^{-1}. These peaks correlate strongly with the biodegradability of the material and are characterized by extremely small intensities.
The analysis focused on the region between900​cm−1900\penalty 10000\ \mathrm{cm}^{-1}and1000​cm−11000\penalty 10000\ \mathrm{cm}^{-1}. The evaluation determined whether to estimate one peak or two peaks in this range.
The estimation yielded a total peak count of either 14 or 13. The spectral dataYYconsisted of 2074 evenly spaced points:Y=(y1,y2,…,y2074)Y=(y_{1},y_{2},\dots,y_{2074}).
As described above, the spectral data were preprocessed in advance using the AsLS method[35].
Figure7shows the preprocessed spectral data.
The degradation rateD​gDg, defined as the percentage change in weight after each polymer was immersed in an enzymatic buffer at37∘​C37^{\circ}\mathrm{C}for 2 days, was used as the physical property valueZZ.
The resulting set of spectra,𝒴∈ℝ2074×68\mathcal{Y}\in\mathbb{R}^{2074\times 68}, and degradation ratesZ=(z1=D​g1,z2=D​g2,…,zN′=D​gN′)∈ℝ68Z=(z_{1}=Dg_{1},z_{2}=Dg_{2},\dots,z_{N^{\prime}}=Dg_{N^{\prime}})\in\mathbb{R}^{68}were used as the datasets.Figure 7:IR spectral dataset of polylactic acid used as the real dataset. Each curve represents one measured spectrum plotted over the wavenumber range800800–1800​cm−11800\penalty 10000\ \mathrm{cm}^{-1}. For visibility, the spectra are displayed in panels grouped according to the spectrum number: (a) 1–12, (b) 13–24, …, (f) 61–68. These data constituteY={Yj}j=1N′Y=\{Y_{j}\}_{j=1}^{N^{\prime}}in the hierarchical model.

We describe the prior distributions and sampling parameters used in the demonstration of the proposed method.
The prior distributions were set as shown in Table3.
For the prior distribution of the peak positions, we referred to the peak occurrence ranges identified in previous studies[34,18].
The number of burn-in steps was set to 5000, followed by 195,000 sampling steps.
The temperature parameters were set toL=70L=70andd=1.35d=1.35, andβl\beta_{l}was determined according to Eq.(29).
Because the real IR spectra contain unknown noise, the spectral noise variance was estimated based on the maximum likelihood by using the sampling results of Bayesian spectral deconvolution, following the process of Tokuda et al.[31].
In the marginalization of the physical-property regression model (Sec.II.3.2), we used the following kernel function:k​(Yi,Yj):=C02​exp⁡(−|Yi−Yj|222​C12).\displaystyle k(Y_{i},Y_{j}):=C_{0}^{2}\exp\left(-\frac{\left|Y_{i}-Y_{j}\right|_{2}^{2}}{2C_{1}^{2}}\right).(33)

The hyperparameters of the kernel function,{C0,C1}\{C_{0},C_{1}\}, were estimated using an empirical Bayes method as the values that maximize the likelihood functionp​(Z|𝒴isample)p(Z|\mathcal{Y}^{\rm sample}_{i}).
In the marginalization of the spectral deconvolution process model representing the approach used by scientists, we computed a sample sequence from the predictive distribution of the spectra,p​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\rm obs},M). This was accomplished using the sample sequence of the vectorϑ\vartheta, which consists of the parametersθ\thetaobtained by marginalizing the spectral deconvolution model for each spectrum (Sec.II.3.3).
At this stage, to ensure that the sequence ofϑ\varthetaobtained by marginalizing the spectral deconvolution model was approximately i.i.d., we computed the autocorrelation of the samples and extracted every 25th sample, as this interval reduced the correlation to a sufficiently low level.
Based onp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\rm obs},M), we computed the expectation ofp​(Z|𝒴)p(Z|\mathcal{Y})(Eq. (II.3.3)).
Considering the computational efficiency and relatively fast convergence of this expectation calculation, the number of samples drawn fromp​(𝒴|𝒴obs,M)p(\mathcal{Y}|\mathcal{Y}^{\rm obs},M)was set to 100.Table 3:Prior distributions assigned to the parameters of each peak in the IR spectra of polylactic acid. The prior distribution of the peak positionμj\mu_{j}is given as a uniform distributionU​(⋅,⋅)U(\cdot,\cdot), and the corresponding wavenumber range (in units ofcm−1\mathrm{cm}^{-1}) is specified for eachjj. In addition, uniform distributions are assigned to the peak widthaaand peak intensitywwfor all peaks, and these are used as the prior distributions of the spectral deconvolution model.Prior distributions ofμ\muPeak Number (jj)p​(μj)p(\mu_{j})Peak Number (jj)p​(μj)p(\mu_{j})1U​(1740,1780)U(1740,\ 1780)8U​(1195,1220)U(1195,\ 1220)2U​(1432,1472)U(1432,\ 1472)9U​(1110,1150)U(1110,\ 1150)3U​(1348,1388)U(1348,\ 1388)10U​(1070,1100)U(1070,\ 1100)4U​(1345,1368)U(1345,\ 1368)11U​(1025,1065)U(1025,\ 1065)5U​(1300,1315)U(1300,\ 1315)12U​(915,935)U(915,\ 935)6U​(1250,1290)U(1250,\ 1290)13U​(945,960)U(945,\ 960)7U​(1160,1195)U(1160,\ 1195)14U​(860,880)U(860,\ 880)Prior distributions ofaaandwwParameterSettingp​(a)p(a)U​(0,13)U(0,\ 13)p​(w)p(w)U​(0,1.2)U(0,\ 1.2)Figure 8:Results of MAP fitting for the IR spectrum of polylactic acid under the two candidate peak-number models. The blue line represents the observed spectrum, and the orange dashed line represents the MAP fit. Panels (a) and (b) show the results for 13 and 14 peaks, respectively. This figure illustrates how the assumed number of peaks affects the reconstruction of the target region.Table 4:Comparison of model-selection results for peak-number models applied to the IR spectral dataset. For each candidate model, the table shows the Bayesian free energyF​EFEcalculated by conventional Bayesian spectral deconvolution, the physical-property-informed free energyF​E~\widetilde{FE}calculated by the proposed method, and the corresponding model probabilities obtained by normalizingexp⁡[−F​E​(M)]\exp[-FE(M)]orexp⁡[−F​E~​(M)]\exp[-\widetilde{FE}(M)]over candidate models. This table serves as an indicator for evaluating whether the proposed method can support the appropriate peak-number model even in the presence of pseudo-peaks arising from the background.Bayesian spectral deconvolutionProposed methodModelFEProbability𝐅𝐄~\mathbf{\widetilde{FE}}Probability13-peak1.1277×10−21.1277\times 10^{-2}0.501−1.0015×104-1.0015\times 10^{4}0.014-peak1.6612×10−21.6612\times 10^{-2}0.499−1.0042×104-1.0042\times 10^{4}1.0

We applied the conventional Bayesian spectral deconvolution method and the proposed method to the generated dataset{𝒴,Z}\{\mathcal{Y},Z\}.
The conventional method assigned nearly equal posterior probabilities to the 13- and 14-peak models, whereas the proposed method strongly favored the 14-peak model, which is consistent with peak assignments reported in previous IR studies (Table4).
More precisely, the conventional method assigned comparable posterior probabilities to the 13- and 14-peak models, whereas the proposed method strongly favored the 14-peak model, consistent with previous IR peak assignments.
Figure8shows the fitting curve obtained from the MAP solution for a spectrumY60Y_{60}.
This fitting result suggests that the proposed method extracted two weak peaks in the region associated with degradation behavior.
AppendixA.2shows all the fitting curves.
These results confirm that the proposed method can effectively estimate the number of peaks even for real spectral data with an unknown background, a task that is difficult for the conventional method.

## III.4DiscussionFigure 9:Correspondence between ARD-based feature importance and spectra. Panels (a), (c), and (e) show the observed spectra, and panels (b), (d), and (f) show the ARD-estimated feature importance for each coordinate, where larger values indicate greater contributions to predicting the physical propertyZZ. The pairs (a,b), (c,d), and (e,f) correspond to the noise-dominant synthetic data, synthetic data with an unknown background, and polylactic acid IR data, respectively. Red-shaded regions indicate the possible true peak ranges in the synthetic data and the prior ranges of the two target peak positions in the real data.

Using the proposed method, which mimics the spectral deconvolution process followed by scientists by integrating the physical-property information with spectral data, we confirmed that property-informed peak-number estimation can be achieved even for spectra containing high-intensity noise and background.
Depending on the information obtained from the physical properties, the method may also misestimate the number of peaks.
Such behavior was observed when a Hamiltonian model was estimated for an X-ray photoelectron spectroscopy (XPS) spectrum (see AppendixBfor details).
This spectrum contains three peak structures, whereas the physical property is uniquely determined by the relative intensities of only two of them.
The peak structure extracted by the proposed method, which existing methods could not recover, is, by construction, related to the physical property.
Such an extracted peak structure is unlikely to be erroneous, and the proposed method should therefore be regarded not as a standalone method for estimating the correct peak structure, but as a method for recovering peak structures overlooked by existing Bayesian spectral deconvolution methods.
We do not claim that the proposed method can replace existing methods; rather, we argue that a more refined understanding of the spectral structure can be obtained by using it as a complementary tool alongside existing methods.

We examined whether the proposed method behaves in a manner consistent with the analytical process followed by scientists, namely, focusing on important spectral regions based on the physical-property information.
To quantify which spectral regions were emphasized by the physical-property regression model, we applied Gaussian process regression with an ARD kernel, using the spectral data𝒴\mathcal{Y}as the explanatory variable and the physical propertyZZas the response variable.
The ARD kernel is a Gaussian process framework that introduces an independent length scale for each input dimension and identifies, in an empirical Bayes manner, the dimensions that contribute to the prediction.
When ARD is introduced into an RBF kernel, it takes the formk​(𝐱,𝐱′)=σf2​exp⁡(−12​∑i=1d(xi−xi′)2ℓi2).k(\mathbf{x},\mathbf{x}^{\prime})=\sigma_{f}^{2}\exp\!\left(-\frac{1}{2}\sum_{i=1}^{d}\frac{(x_{i}-x_{i}^{\prime})^{2}}{\ell_{i}^{2}}\right).(34)

A length scaleℓi\ell_{i}is assigned to each dimensionii.
A smallerℓi\ell_{i}allows the function to vary more sharply along that dimension. Therefore, the dimension can be interpreted as being more important for predicting the outputZZ.
In this study, the intensity at each wavenumber was treated as an input dimension, and the estimated importance[importance​of​wave​number]∝ℓi−2[{\rm importance\>\>of\>\>wave\>\>number}]\propto\ell_{i}^{-2}(35)

was visualized as a function of the wavenumber to quantify the spectral regions emphasized by the physical-property regression model.
The kernel used for physical-property regression in the proposed method does not include the length scaleℓi\ell_{i}and therefore differs from the ARD kernel; strictly speaking, this analysis is not a direct evaluation of the proposed method itself, although it can still reveal the overall tendency of the emphasized spectral regions.
The distribution of important spectral structures estimated by ARD focused on specific regions around the assumed peak structures.
This suggests that the effectiveness of the proposed method is consistent with our original expectation.
The overall distribution of important spectral structures estimated by ARD was spread over a wide region with a complex shape, rather than being confined to specific regions around the assumed peak structures (Fig.9).
Such a complex distribution of importance would be difficult for humans to use effectively.
The ability to exploit information from such complex, important spectral regions may be regarded as an advantage of the proposed method, which hierarchically integrates the two-stage scientific process of modeling the relationship between the physical properties and spectra, as well as the spectra themselves.

## IVConclusion

In this study, we explicitly formulated, as a probabilistic model, the mapping between physical properties (or chemical structure) and spectral shape that scientists implicitly use in spectral deconvolution.
Thus, we developed a framework that enables peak-number estimation under high-intensity noise and unknown background, conditions under which conventional Bayesian spectral deconvolution based only on spectral data often fails.
The proposed method is formulated as a hierarchical Bayesian model that (i) estimates the spectral structure while preserving the uncertainties in the peak number, position, and intensity through Bayesian spectral deconvolution,
and (ii) describes the relationship between the estimated spectrum and physical properties through Gaussian process regression, thereby feeding physical-property information back into the spectral model selection, that is, peak-number estimation.
For strongly multimodal posterior distributions, REMC is used to perform stable marginalization, and the number of peaks is selected based on posterior model probabilities.

In synthetic experiments where the noise intensity was comparable to the peak intensity, the conventional method selected one peak under conditions in which noise was as dominant as the peaks,
whereas the proposed method correctly selected two peaks by exploiting consistency with the physical properties.
In synthetic experiments with an unknown background, the conventional method could select an incorrect model because of pseudo-peaks introduced by preprocessing,
whereas the proposed method correctly identified the true number of peaks.
When applied to real IR spectra of polylactic acid, the method
extracted weak peaks related to biodegradability in a manner consistent with previous IR studies,
while retaining valid peak-number estimation under an unknown background.

The significance of this framework lies not only in fitting spectral shapes but also in enabling model selection from the viewpoint of spectral structures that can explain the physical property values.
As a result, it can extract and present candidate peaks buried in noise or background in a manner consistent with the goal of exploring the mechanisms underlying the physical property.
However, the results suggest that peaks unrelated to the target physical property may be overlooked when that property is determined uniquely by using only a subset of the peak information.
Future research will extend this framework by integrating multiple physical properties and other measurements, including structural information, to establish a more general foundation for automated spectral analysis and knowledge extraction in materials science.

## Acknowledgments

This work was supported by JSPS KAKENHI grant numbers 22K13979, 23K28150, 24K22309, 24H00247, 25K00986, and 25H01470; JST; and PRESTO grant numbers JPMJPR212A, JST CREST JPMJCR2431, and NEDO JPNP22100843-0.

## VReferences

## References
- [1]D. R. Baer, K. Artyushkova, C. R. Brundle, J. E. Castle, M. H. Engelhard, K. J. Gaskell, J. T. Grant, R. T. Haasch, M. R. Linford, C. J. Powell, A. G. Shard, P. M. A. Sherwood, and V. S. Smentkowski(2019)Practical Guides for X-Ray Photoelectron Spectroscopy (XPS): First Steps in planning, conducting and reporting XPS measurements.37.External Links:Document,ISSN 0734-2101, 1520-8559Cited by:§I.
- [2]C. M. Bishop(2006)Pattern recognition and machine learning (information science and statistics).Springer-Verlag,Berlin, Heidelberg.External Links:ISBN 0387310738Cited by:§II.2.2.
- [3]L. Buglioni, F. Raymenants, A. Slattery, S. D. A. Zondag, and T. Noël(2022)Technological innovations in photochemistry for organic synthesis: flow chemistry, high-throughput experimentation, scale-up, and photoelectrochemistry.122(2),pp. 2752–2906.Note:PMID: 34375082External Links:Document,LinkCited by:§I.
- [4]A. Dazzi and C. B. Prater(2017)AFM-IR: technology and applications in nanoscale infrared spectroscopy and chemical imaging.117(7),pp. 5146–5173.Note:PMID: 27958707External Links:Document,Link,https://doi.org/10.1021/acs.chemrev.6b00448Cited by:§I.
- [5]A. E. Derome(2013)Modern nmr techniques for chemistry research.Elsevier.Cited by:§I.
- [6]J. Diehl, J. Knollmüller, and O. Schulz(2024-06)Bias-free estimation of signals on top of unknown backgrounds.1063,pp. 169259.External Links:ISSN 0168-9002,Link,DocumentCited by:§I.
- [7]P. H. C. Eilers and H. F.M. Boelens(2005)Baseline correction with asymmetric least squares smoothing.Technical reportLeiden University Medical Centre Report.Cited by:§III.2.
- [8]R. Fan, X. Yang, C. F. Drury, and Z. Zhang(2018-08-15)Curve-fitting techniques improve the mid-infrared analysis of soil organic carbon: a case study for brookston clay loam particle-size fractions.Scientific Reports8(1),pp. 12174.External Links:ISSN 2045-2322,Document,LinkCited by:§I.
- [9]A. Fasano, P. Ade, M. Aravena, E. Barria, A. Beelen, A. Benoit, M. Béthermin, J. Bounmy, O. Bourrion, G. Bres, M. Calvo, A. Catalano, C. D. Breuck, F. Désert, C. Dubois, C. Durán, T. Fenouillet, J. Garcia, G. Garde, J. Goupy, C. Hoarau, W. Hu, G. Lagache, J. Lambert, F. Levy-Bertrand, A. Lundgren, J. Macías-Pérez, J. Marpaud, A. Monfardini, G. Pisano, N. Ponthieu, L. Prieur, S. Roni, S. Roudier, D. Tourres, C. Tucker, and M. V. Cuyck(2024)CONCERTO: instrument model of fourier transform spectroscopy, white-noise components.External Links:2406.16334,LinkCited by:§I.
- [10]C. C. Giac and T. V. Thanh(2025)Establishing a spectroscopic analysis procedure for identifying the molecular structure of organic compounds to enhance chemistry students’ problem-solving skills.World Journal of Chemical Education13(1),pp. 1–6.External Links:ISSN 2375-1657,Link,DocumentCited by:§I.
- [11]N. Han and R. J. Ram(2020)Bayesian modeling and computation for analyte quantification in complex mixtures using Raman spectroscopy.143,pp. 106846.External Links:ISSN 0167-9473,Document,LinkCited by:§I.
- [12]A. G. Harrison(2018)Chemical ionization mass spectrometry.Routledge.Cited by:§I.
- [13]W. K. Hastings(1970)Monte Carlo sampling methods using Markov chains and their applications.57(1),pp. 97–109.External Links:DocumentCited by:item1,§II.3.1.
- [14]C. F. Holder and R. E. Schaak(2019)Tutorial on powder X-ray diffraction for characterizing nanoscale materials.13(7),pp. 7359–7365.Note:PMID: 31336433External Links:Document,LinkCited by:§I.
- [15]Y. IBA(2001-06)EXTENDED ensemble Monte Carlo.12(05),pp. 623–656.External Links:ISSN 1793-6586,Link,DocumentCited by:§II.3.1.
- [16]S. Kashiwamura, S. Katakami, Yamagami,Ryo, K. Iwamitsu, H. Kumazoe, K. Nagata, T. Okajima, I. Akai, and M. Okada(2022)Bayesian spectral deconvolution of X-ray absorption near edge structure discriminating between high- and low-energy domains.91(7),pp. 074009.External Links:DocumentCited by:§I.
- [17]M. O. Kenji Nagata(2012)Bayesian spectral deconvolution with the exchange Monte Carlo method.28,pp. 82–89.External Links:ISSN 0893-6080,DocumentCited by:§I,§II.2.1,§II.3.1.
- [18]G. Kister, G. Cassanas, and M. Vert(1998)Effects of morphology, conformation and configuration on the IR and Raman spectra of various poly(lactic acid)s.Polymer39(2),pp. 267–273.External Links:ISSN 0032-3861,Document,LinkCited by:§III.3,§III.3.
- [19]K. Kneipp, H. Kneipp, I. Itzkan, R. R. Dasari, and M. S. Feld(1999)Ultrasensitive chemical analysis by Raman spectroscopy.99(10),pp. 2957–2976.Cited by:§I.
- [20]A. Kotani, H. Mizuta, T. Jo, and J.C. Parlebas(1985)Theory of core photoemission spectra in CeO2.53(9),pp. 805–810.External Links:ISSN 0038-1098,DocumentCited by:§B.1.
- [21]K. Łatuszyński, M. T. Moores, and T. Stumpf-Fétizon(2025)MCMC for multi-modal distributions.arXiv preprint arXiv:2501.05908.Cited by:§II.3.1.
- [22]C. Macaro and R. Prado(2014)Spectral decompositions of multiple time series: a Bayesian non-parametric approach.79(1),pp. 105–129(English).Note:Research Support, U.S. Gov’t, Non-P.H.S.External Links:Document,Link,ISSN 1860-0980,https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3925306/Cited by:§I.
- [23]L. P. Malone, S. M. Best, and R. E. Cameron(2024)Accelerated degradation testing impacts the degradation processes in 3D printed amorphous PLLA.Frontiers in Bioengineering and Biotechnology12,pp. 1419654.External Links:DocumentCited by:§III.3.
- [24]E. Marinari and G. Parisi(1992-07)Simulated tempering: a new Monte Carlo scheme.19(6),pp. 451–458.External Links:ISSN 1286-4854,Link,DocumentCited by:§II.3.1.
- [25]E. Meaurio, N. López-Rodríguez, and J. Sarasua(2006)Infrared spectrum of poly(l-lactide): application to crystallinity studies.Macromolecules39(26),pp. 9291–9301.External Links:DocumentCited by:§III.3.
- [26]M. Meyns, F. Dietz, C. Weinhold, H. Züge, S. Finckh, and G. Gerdts(2023)Multi-feature round silicon membrane filters enable fractionation and analysis of small micro- and nanoplastics with Raman spectroscopy and nano-FTIR.Analytical Methods15(5),pp. 606–617.External Links:Document,LinkCited by:§III.3.
- [27]Y. Mototake, M. Mizumaki, I. Akai, and M. Okada(2019-03)Bayesian hamiltonian selection in X-ray photoelectron spectroscopy.88(3),pp. 034004.External Links:ISSN 1347-4073,Link,DocumentCited by:§B.1.
- [28]K. Nagata and S. Watanabe(2008)Asymptotic behavior of exchange ratio in exchange Monte Carlo method.21(7),pp. 980–988.External Links:ISSN 0893-6080,DocumentCited by:§B.2,§III.1,§III.2.
- [29]J. Near, A. Harris, C. Juchem, R. Kreis, M. Marjańska, G. Öz, J. Slotboom, M. Wilson, and C. Gasparovic(2021-05)Preprocessing, analysis and quantification in single-voxel magnetic resonance spectroscopy: Experts’ consensus recommendations.34,pp. e4257.External Links:DocumentCited by:§I.
- [30]K. Takahashi, Y. Amamoto, H. Kikutake, M. Ito, A. Takahara, and T. Onishi(2021)Random forest analysis of X-ray diffraction and scattering data on crystalline polymer.20(3),pp. 103–105.Note:(in Japanese)External Links:DocumentCited by:§III.3.
- [31]S. Tokuda, K. Nagata, and M. Okada(2017-02)Simultaneous estimation of noise variance and number of peaks in Bayesian spectral deconvolution.86(2),pp. 024001.External Links:ISSN 1347-4073,Link,DocumentCited by:§III.3.
- [32]C. Wang, L. Xiao, C. Dai, A. H. Nguyen, L. E. Littlepage, Z. D. Schultz, and J. Li(2020-01-29)A statistical approach of background removal and spectrum identification for SERS data.10(1),pp. 1460.External Links:ISSN 2045-2322,Document,LinkCited by:§I.
- [33]K. Yui(2023)Fusion of spectroscopy and geology: earth’s interior environment revealed 5 through light.52(1),pp. 230110a.External Links:DocumentCited by:§I.
- [34]J. Zhang, H. Tsuji, I. Noda, and Y. Ozaki(2004)Weak intermolecular interactions during the melt crystallization of poly(l-lactide) investigated by two-dimensional infrared correlation spectroscopy.The Journal of Physical Chemistry B108(31),pp. 11514–11520.External Links:DocumentCited by:§III.3,§III.3.
- [35]Z. Zhang, S. Chen, and Y. Liang(2010)Baseline correction using adaptive iteratively reweighted penalized least squares.135,pp. 1138–1146.External Links:Document,LinkCited by:§III.3.

## Appendix AFitting results of this study

This section presents the detailed fitting curves for all samples of the artificial data and polylactic acid IR spectral data discussed in Section 3.
Specifically, we compare the spectral model based on the MAP solution, which minimizes the error estimated by the proposed method, with the observed spectral data.
In each figure shown below, the solid blue line represents the observed spectral data, and the dashed orange line represents the fitting curve reconstructed by the proposed method.

## A.1Fitting results for artificial data

This subsection presents the fitting results for all six artificial spectra generated for different peak-to-peak distancesΔ\Delta.
The figure shows that regardless of the value ofΔ\Delta, that is, the degree of peak overlap, the proposed method (orange dashed line) accurately captures the true two-peak structure underlying the observed data (blue solid line).
Even when the noise intensity matches the peak intensity, the method provides appropriate peak-number and peak-shape estimates without overfitting false peaks.Figure 10:Fitting results for artificial data 1 to 3. The solid blue line indicates the observed spectral data. The dashed orange line shows the reconstructed fitting curve obtained using the proposed method.Figure 11:Fitting results for artificial data 4 to 6. The solid blue line indicates the observed spectral data. The dashed orange line shows the reconstructed fitting curve obtained using the proposed method.

## A.2IR Spectrum Fitting Results

This subsection lists the fitting results for each model applied to the IR spectra of polylactic acid obtained under 68 conditions with different crystallization temperatures and concentrations (Figs.12–23).
These results indicate that the proposed method stably extracts two weak peaks in the biodegradability-related region.(a)Spectrum 1(b)Spectrum 2(c)Spectrum 3(d)Spectrum 4(e)Spectrum 5(f)Spectrum 6Figure 12:IR fitting results (Spectra 1–6). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 7(b)Spectrum 8(c)Spectrum 9(d)Spectrum 10(e)Spectrum 11(f)Spectrum 12Figure 13:IR fitting results (Spectra 7–12). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 13(b)Spectrum 14(c)Spectrum 15(d)Spectrum 16(e)Spectrum 17(f)Spectrum 18Figure 14:IR fitting results (Spectra 13–18). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 19(b)Spectrum 20(c)Spectrum 21(d)Spectrum 22(e)Spectrum 23(f)Spectrum 24Figure 15:IR fitting results (Spectra 19–24). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 25(b)Spectrum 26(c)Spectrum 27(d)Spectrum 28(e)Spectrum 29(f)Spectrum 30Figure 16:IR fitting results (Spectra 25–30). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 31(b)Spectrum 32(c)Spectrum 33(d)Spectrum 34(e)Spectrum 35(f)Spectrum 36Figure 17:IR fitting results (Spectra 31–36). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 37(b)Spectrum 38(c)Spectrum 39(d)Spectrum 40(e)Spectrum 41(f)Spectrum 42Figure 18:IR fitting results (Spectra 37–42). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 43(b)Spectrum 44(c)Spectrum 45(d)Spectrum 46(e)Spectrum 47(f)Spectrum 48Figure 19:IR fitting results (Spectra 43–48). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 49(b)Spectrum 50(c)Spectrum 51(d)Spectrum 52(e)Spectrum 53(f)Spectrum 54Figure 20:IR fitting results (Spectra 49–54). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 55(b)Spectrum 56(c)Spectrum 57(d)Spectrum 58(e)Spectrum 59(f)Spectrum 60Figure 21:IR fitting results (Spectra 55–60). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 61(b)Spectrum 62(c)Spectrum 63(d)Spectrum 64(e)Spectrum 65(f)Spectrum 66Figure 22:IR fitting results (Spectra 61–66). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.(a)Spectrum 67(b)Spectrum 68Figure 23:IR fitting results (Spectra 67–68). The blue solid line represents the observed spectral data, and the orange (green) dashed line represents the fitting curve for the 14-peak (13-peak) model.

## Appendix BDemonstration Using XPS Spectra

This section presents the results obtained by applying the conventional Bayesian spectral deconvolution method and the proposed method for peak-number estimation in inner-shell XPS spectra.

## B.1Verification Dataset

We used a dataset containing artificially generated inner-shell XPS spectral data generated from an XPS spectroscopic model and the corresponding physical parameters related to the electronic levels specified in the data-generating process[27].
Here, we employed the spectroscopic model proposed by Kotani et al.[20]for 4f-orbital electrons associated with inner-shell electrons in the 3d orbital of rare-earth compounds.
Specifically, we generated the data from the parameter regions of the spectroscopic model corresponding to La2O3, which exhibits a two-peak structure in the region of interest, and CeO2, which exhibits a three-peak structure.

The 4ffelectrons have the following three eigenstates:|f0⟩|f^{0}\rangle,|f1⟩|f^{1}\rangle, and|f2⟩|f^{2}\rangle.
In the|f0⟩|f^{0}\ranglestate, the 4fforbital is unoccupied; in the|f1⟩|f^{1}\ranglestate, it is occupied by one electron; and in the|f2⟩|f^{2}\ranglestate, it is occupied by two electrons.
In the state space of these 4ffelectrons, the effective Hamiltonian that reproduces the XPS spectroscopic process is given as follows.H\displaystyle H=εL​∑νaL​ν†​aL​ν+εf0​∑νaf​ν†​af​ν+εc​ac†​ac\displaystyle=\varepsilon_{L}\sum_{\nu}a_{L\nu}^{\dagger}a_{L\nu}+\varepsilon_{f}^{0}\sum_{\nu}a_{f\nu}^{\dagger}a_{f\nu}+\varepsilon_{c}a_{c}^{\dagger}a_{c}+VNf​∑ν(af​ν†​af​ν+af​ν​af​ν†)\displaystyle+\frac{V}{\sqrt{N_{f}}}\sum_{\nu}(a_{f\nu}^{\dagger}a_{f\nu}+a_{f\nu}a_{f\nu}^{\dagger})+Uf​f​∑ν≠ν′af​ν†​af​ν​af​ν′†​af​ν′\displaystyle+U_{ff}\sum_{\nu\neq\nu^{\prime}}a_{f\nu}^{\dagger}a_{f\nu}a_{f\nu^{\prime}}^{\dagger}a_{f\nu^{\prime}}−Uf​c​∑νaf​ν†​af​ν​(1−ac†​ac).\displaystyle-U_{fc}\sum_{\nu}a_{f\nu}^{\dagger}a_{f\nu}(1-a_{c}^{\dagger}a_{c}).(36)

Here,εL\varepsilon_{L},εf0\varepsilon_{f}^{0}, andεc\varepsilon_{c}denote the energies of the conduction electrons (5​d5dand6​s6selectrons),4​f4felectrons, and core electrons, respectively, in4​f4frare-earth metals.
The indexν\nu(ν=1,…,Nf\nu=1,\dots,N_{f},Nf=14N_{f}=14) represents the spin and orbital quantum number of thefforbital.
The parametersVV,Uf​fU_{ff}, and−Uf​c-U_{fc}denote the energies of the hybridization interaction between the4​f4fand conduction electrons, Coulomb interaction between4​f4felectrons, and Coulomb potential from the core hole acting on the4​f4felectrons, respectively.
In both the initial and final states, the energy of the|f0⟩|f^{0}\ranglestate is set to zero as the reference energy level.
With this setting, the number of parameters in the effective HamiltonianHHis reduced to the following:Δ(=εf0−εL)\Delta\,(=\varepsilon_{f}^{0}-\varepsilon_{L}),VV,Uf​fU_{ff},Uf​cU_{fc}, andΓ\Gamma.
The parameter set of the effective HamiltonianHHis defined as follows.θ={Δ,V,Uf​f,Uf​c,Γ}\displaystyle\theta=\{\Delta,V,U_{ff},U_{fc},\Gamma\}(37)

The initial state refers to the system before X-ray irradiation, with all electrons in their ground states. The final state refers to the system after X-ray irradiation, in which a core hole has been created by the removal of a core electron.
The minimum-energy eigenstate of the initial state is|G⟩|G\rangle. The three energy levels of the final state areEj​(θ)E_{j}(\theta)(j=0,1,2j=0,1,2), with the eigenstate|Fj⟩|F_{j}\rangle.

Fermi’s golden rule provides the transition probability between these states.F​(ω;θ)=∑j=02|⟨Fj|ac|G⟩|2​δ​(ω−Ej​(θ)+EG​(θ)).\displaystyle F(\omega;\theta)=\sum_{j=0}^{2}|\langle F_{j}|a_{c}|G\rangle|^{2}\delta(\omega-E_{j}(\theta)+E_{G}(\theta)).(38)

By convolvingF​(ω;θ)F(\omega;\theta)with the Lorentz function and adding Gaussian noiseε\varepsilonwith varianceσ2\sigma^{2}, the spectral dataYYare obtained as follows.y​(ω)=∑j=02|⟨Fj|ac|G⟩|2​Γ/π(ω−(Ej​(θ)−EG​(θ)))2+Γ2+ε\displaystyle y(\omega)=\sum_{j=0}^{2}\frac{|\langle F_{j}|a_{c}|G\rangle|^{2}\Gamma/\pi}{(\omega-(E_{j}(\theta)-E_{G}(\theta)))^{2}+\Gamma^{2}}+\varepsilon(39)

Γ\Gammais the half-width of the Lorentz function.Table 5:XPS Spectrum Reproduction Parameters for La2O3and CeO2CompoundΔ\DeltaVVUf​fU_{ff}Uf​cU_{fc}Γ\GammaLa2O312.50.5710.512.70.5CeO21.600.7610.512.50.7

The parameters corresponding to La2O3and CeO2used to construct this dataset are listed in Table5.
Building on this, the table shows that the most prominent difference between the parameter sets for La2O3and CeO2lies inΔ\Delta.
Given this distinction, we treatΔ\Deltaas the physical quantityZZhereinafter.
With this definition in place, the following trends were observed asΔ\Deltavaried.
For a smallΔ\Delta, multiple peaks appear in the spectrum, and each peak has a pronounced intensity.
For a largeΔ\Delta, the intensity of the peak on the high-energy side decreases, yielding a shape close to that of a two-peak structure.
The generated data are shown in Fig.24.
For the spectrum atΔ=12.5\Delta=12.5, the peak intensity corresponding toE2E_{2}becomes nearly zero.
This is because the interaction between the|f2⟩|f^{2}\rangleand|f0⟩|f^{0}\ranglestates becomes weaker as the energy of the|f2⟩|f^{2}\ranglestate increases.
This suggests thatΔ\Deltaplays an essential role in changing the peak-number properties.
Therefore, we generatedN′=6N^{\prime}=6spectral datasets𝒴\mathcal{Y}at equal intervals fromΔ=1.6\Delta=1.6toΔ=12.5\Delta=12.5.
Each spectrumYYconsisted of 400 equally spaced points, that is,Y=(y1,y2,…,y400)Y=(y_{1},y_{2},\dots,y_{400}).
By setting the standard deviationσ\sigmaof the noise added to the spectra to0.010.01, we generated a set of spectra𝒴∈ℝ400×6\mathcal{Y}\in\mathbb{R}^{400\times 6}and physical quantitiesZ=(z1=Δ1,z2=Δ2,…,zN′=ΔN′)∈ℝ6Z=(z_{1}=\Delta_{1},z_{2}=\Delta_{2},\dots,z_{N^{\prime}}=\Delta_{N^{\prime}})\in\mathbb{R}^{6}.

To investigate the properties of the generated dataset, we applied Bayesian spectral deconvolution, as described in SectionII.3.1, to a dataset composed of spectral models with the noise levelσ=0\sigma=0.
As the spectral model, we used a linear sum of Gaussian functions and estimated the number of peaksMM.
The selection ofMMbased on the Bayesian FE confirmed that only the spectrum atΔ=12.5\Delta=12.5was estimated to have two peaks, whereas all the others were estimated to have three peaks (Table6).
As noted above, only the spectrum atΔ=12.5\Delta=12.5shows a nearly zero peak intensity forE2E_{2}, resulting in a two-peak structure.
These results confirm that Bayesian spectral deconvolution correctly estimates the number of peaks according to the spectral shape.

Next, to investigate the relationship between the physical quantityZZand the spectrum𝒴\mathcal{Y}, we regressedZZonYYusing an ARD model, which enables Gaussian process regression together with evaluation of the importance of the explanatory variables.
Figure25shows the importance of the explanatory variables obtained from ARD regression.
In Fig.25, the horizontal axis represents the energy coordinateω\omega, and the vertical axis represents the importance.
This result suggests that in the regression of the physical quantityZZ, only two of the three peaks in the spectrum are important.
From the viewpoint of correspondence with the physical property, this implies that the two-peak structure is important.
Accordingly, when the proposed framework is applied to this dataset, a model that focuses only on these two peaks is expected to be selected as the spectral model.Figure 24:Spectra generated for different values ofΔ\Delta.Figure 25:Feature importance obtained by ARD.Table 6:Bayesian FE for each value ofΔ\Delta.Δ\DeltaK=2K=2K=3K=31.603.325e+032.664e+032.812.878e+032.440e+035.233.478e+031.887e+037.652.169e+031.785e+0310.01.915e+031.696e+0312.51.832e+031.858e+03

## B.2Results of Applying the Proposed Method

The parameters for each method in the proposed framework were set as described below to ensure clarity and consistency.
A linear sum of the Gaussian functions was used as the spectral model for Bayesian spectral deconvolution.
The exchange Monte Carlo parameters in the spectral deconvolution model were defined as follows.
The number of temperature pointsLLwas set to 40, and based on the study by Nagata et al.[28],βl\beta_{l}was set according to the following configuration.βl={0.0for​l=1,dl−Lfor​l=2,3,…,L.\beta_{l}=\begin{cases}0.0&\quad\text{for }l=1,\\
d^{{l-L}}&\quad\text{for }l=2,3,\dots,L.\end{cases}(40)

The burn-in period for the sampling process was set to 4000 steps, and the total number of samples was set to 10,000 steps.
From the resulting sequence ofθ\thetasamples, we extracted 16 values ofθ\thetaat 5-step intervals and used them to estimatep​(Y|Yobs,M)p(Y|Y^{\mathrm{obs}},M).Figure 26:Top-ranked models and theFE~\widetilde{\rm FE}atσ=0.01\sigma=0.01.

The hyperparameters of the Gaussian process regression module were determined as follows.
A rational quadratic kernel was adopted as the kernel function.
To compute the Gaussian process regression modulep​(Z|𝒴)p(Z|\mathcal{Y}), 30 samples were drawn fromp​(Y|Yobs,M)p(Y|Y^{\mathrm{obs}},M), and Gaussian process regression was applied to each sampled dataset{𝒴isample}i=130\{\mathcal{Y}^{\rm sample}_{i}\}_{i=1}^{30}to estimatep​(Z∣𝒴)∼130​∑i=130p​(Z∣𝒴isample).p(Z\mid\mathcal{Y})\sim\frac{1}{30}\sum_{i=1}^{30}p(Z\mid\mathcal{Y}^{\rm sample}_{i}).

The kernel hyperparameters were optimized by an empirical Bayes method as the values that maximizep​(Z∣𝒴isample)p(Z\mid\mathcal{Y}^{\rm sample}_{i}).

We applied the proposed method to the dataset{𝒴,Z}\{\mathcal{Y},Z\}and evaluated whether a two-peak or three-peak model was more plausible for each physical quantityZZ.
Applying the proposed framework yielded the results shown in Fig.26.
The upper panel of Fig.26shows the selected spectral models, ordered from left to right by increasing Bayesian FE; black pixels correspond to two-peak models, whereas beige pixels correspond to three-peak models.
The lower panel shows theFE~\widetilde{\rm FE}of the spectral models shown in the upper panel.
Figure26confirms that a two-peak model is selected for many regions of the spectral data that exhibit a three-peak structure.
This result is consistent with the physical prior knowledge that emphasizes only two peaks in estimating the physical quantityZZ(see SectionB.1).

## 


- 


Major funding support from
