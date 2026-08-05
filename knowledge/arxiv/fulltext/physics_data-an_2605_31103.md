# Model-Agnostic Signal Discovery with Machine Learning: Bridging the Gap Between Theory and Practice

**arXiv ID**: 2605.31103v1
**Authors**: Oz Amram, Marco Letizia, Mikael Kuusela
**Published**: 2026-05-29
**Categories**: physics.data-an, hep-ex, stat.ML
**Comments**: 37 pages, 7 figures. Part of the VERaiPHY initiative
**HTML URL**: https://arxiv.org/html/2605.31103v1

## Abstract

Searches for new phenomena in complex scientific data are predominantly model-dependent, optimized for specific hypotheses, and therefore limited in their coverage of the space of possible signals. Recently, new AI-based model-agnostic search strategies, many of which have been pioneered in high-energy physics, have been proposed which provide a complementary paradigm, prioritizing broad exploration over tailored analyses. These techniques offer an opportunity to enhance the overall discovery potential of modern experiments, especially in regimes where theoretical guidance is scarce. In this document, we review the conceptual framework behind the main classes of AI-based model-agnostic strategies. We discuss the potential pitfalls of these methods, and strategies for their validation and interpretation. We aim for this document to serve as a useful reference both for practitioners and for researchers interested in learning more about these model-agnostic search strategies.

## Full Text

Abstract

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
- License: CC BY 4.0arXiv:2605.31103v1 [physics.data-an] 29 May 2026

Model-Agnostic Signal Discovery with Machine Learning:
Bridging the Gap Between Theory and Practice

Part of the VERaiPHY initiative

Oz Amram1⋆\star,
Marco Letizia2,3†\daggerand
Mikael Kuusela4‡{\ddagger}

1Fermi National Accelerator Laboratory, Batavia, IL 60510, USA

2MaLGa-DIBRIS, Università di Genova, Via Dodecaneso 35, I-16146 Genoa, Italy

3INFN, Sezione di Genova, Via Dodecaneso 33, I-16146 Genoa, Italy

4Department of Statistics and Data Science, Carnegie Mellon University, Pittsburgh, PA 15213, USA

⋆\staroz.amram@cern.ch†\daggermarco.letizia@edu.unige.it‡{\ddagger}mkuusela@andrew.cmu.edu

## Abstract

Searches for new phenomena in complex scientific data are predominantly model-dependent, optimized for specific hypotheses, and therefore limited in their coverage of the space of possible signals. Recently, new AI-based model-agnostic search strategies, many of which have been pioneered in high-energy physics, have been proposed which provide a complementary paradigm, prioritizing broad exploration over tailored analyses. These techniques offer an opportunity to enhance the overall discovery potential of modern experiments, especially in regimes where theoretical guidance is scarce. In this document, we review the conceptual framework behind the main classes of AI-based model-agnostic strategies. We discuss the potential pitfalls of these methods, and strategies for their validation and interpretation. We aim for this document to serve as a useful reference both for practitioners and for researchers interested in learning more about these model-agnostic search strategies.

Copyright attribution to authors.
This work is a submission to SciPost Phys. Comm. Rep.
License information to appear upon publication.
Publication information to appear upon publication.Received Date
Accepted Date
Published Date

## 
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

## 1Introduction

One of the primary research activities in the field of high-energy physics (HEP) is the analysis of large datasets to search for evidence for new phenomena.
To accommodate the large volume and high complexity of the data, and achieve gains in sensitivity, searches for new phenomena often restrict their scope to specific models or classes of new particles.
Other approaches instead attempt to make minimal assumptions and probe a broad range of possibilities, but achieve reduced sensitivity as compared to dedicated searches.
This gives rise to two families of methods:model-dependentandmodel-agnostic(ormodel-independent) approaches.

Model-dependent searches are designed on the basis of well-specified background and signal hypotheses.
They look for deviations from a background model while incorporating properties of hypothetical signals (such as particle masses, decay modes, or kinematic distributions) and optimize the analysis to enhance sensitivity to these signatures, for example by focusing on a few relevant high-level features such as an invariant mass.
For any specific hypothesis to be tested, these methods are generally the most powerful.
Indeed the likelihood-ratio test, used ubiquitous in HEP data analyses, is guaranteed by the Neyman–Pearson lemma[1]to be the most powerful test for fully specified background and signal hypotheses.
However, their sensitivity is typically limited to a narrow region of the whole space of possible new physics scenarios and observables, and they heavily rely on high-fidelity models for the background processes.

In contrast, model-agnostic searches are designed to minimize assumptions about the signal and/or the background.
It is in fact useful to distinguish between background- and signal-agnostic methods as illustrated in Figure1.
These approaches are valuable when there is little guidance from theory or when predictions via Monte Carlo simulations are not particularly accurate or reliable.
In this review we will focus on the case where minimal assumptions are being made about the signal hypothesis. Different techniques will be required depending on the degree to which the background hypothesis is well specified.
While model-agnostic methods enable exploration of a broader spectrum of potential new physics signatures, they lack the sensitivity of model-dependent strategies for specific signals and often require careful statistical validation to control false discovery rates.
They also face crucial challenges in their interpretation, both in the case of a significant discrepancy and in the reporting of exclusion limits. Furthermore, it is worth highlighting that a model-agnostic search is still typically restricted to a subset of final states and observables that are physically motivated or experimentally accessible.

In practice, most analyses fall somewhere between these two extremes. For example, bump hunts[2], which search for localized excesses, can be considered partially model-independent: they do not depend on specific particle-physics models and often rely on data-driven estimates of the background[3,4,5,6], yet they still assume that any signal will appear as a localized excess in a particular variable (for example, an invariant-mass distribution) within a predefined signal region. Another approach is to consider a comprehensive enumeration of final states, typically hundreds to thousands, while defining a small set of observables for each, and compare the observed data in each final state to simulations of the background processes.
One then defines a statistical procedure to quantify the largest contiguous deviations across the entire search space.
Such a strategy was first deployed in experiments at the Tevatron and HERA[7,8,9,10,11,12]and has been continued by current LHC experiments[13,14].
This approach makes minimal assumptions about the signal but assumes backgrounds are well modeled by simulation.
While this method has the benefit of covering a large signal parameter space, it has several limitations.
Anomalies are again generally assumed to appear as contiguous deviations in the selected observables.
Moreover, since no multivariate information is utilized, anomalies appearing in final states with large backgrounds are likely to be missed.
Finally, the heavy reliance on simulation, which may have imperfections in exotic final states, limits the sensitivity of the search.
Modern techniques seek to improve upon this scenario in one or more respects.

In the last several years, there has been a significant body of work on new classes of model-agnostic search strategies enabled by advances in machine learning[15,16].
Excitingly, these new methods have now begun to be adopted by the large experimental collaborations as a complementary component of their search programs[17,18,19,20,21,22,23,24,25].
Though new physics has not yet been found, these searches have demonstrated the power of these approaches to discover new phenomena that may have been missed by conventional model-dependent approaches.
It is likely that in the coming years the usage of these methods in collider searches will continue to grow, and that their potential will increasingly be recognized in other areas of physics, such as cosmology and astrophysics, where similarly complex datasets and limited theoretical guidance motivate the use of flexible, model-agnostic approaches.

While these searches have great promise, the new methods they employ and their underlying philosophies are unfamiliar to many researchers in the physical sciences.
Standard practices on the validation of these methods, and how results from these searches should be reported, have yet to be established.

In this document we attempt to close this knowledge gap, providing a concise review of the methods and strategies for their validation.
In Section2, we overview the basic statistical formalism of searches, and then review the major classes of new model-agnostic techniques, focusing on the major conceptual points rather than machine learning specifics.
In Sections3and4we focus on methods for the validation of these strategies in two case studies.
In Section5, we further discuss interpretation strategies for these new methods, both for interpreting a significant excess and methods to derive exclusion limits.
We conclude in Section6.

This article contributes to VERaiPHY (Validation & Evaluation for Robust AI in PHYsics), a PHYSTAT review series establishing verification and validation standards for machine learning across particle physics, astrophysics, and cosmology.

## 2Foundations of model-agnostic searchesFigure 1:Landscape of model-agnostic signal detection. The various methods can be categorized according to their strength of assumptions about the background distribution (pbp_{b}) and the signal distribution (psp_{s}).

Existing model-agnostic search strategies can be broadly grouped into two categories.
The first category comprises methods that perform the entire statistical test: they take the observed data sample as input and directly output the statistical significance of any deviation from expectations.
Such approaches can be used as a standalone analysis or run in parallel with traditional model-dependent searches targeting a specific final state.
In this review we discuss these strategies within the formalism oftwo-sample hypothesis testing.
The second category, which we denote asmodel-agnostic signal selection strategies, includes approaches that form only part of the full analysis, and do not include a statistical test as part of the method. These methods function as anomaly detectors, identifying interesting events or regions of phase space by assigning an anomaly score in a model-agnostic manner.
The selected anomalous events can then be further analyzed using either model-aware or model-agnostic statistical procedures to determine whether they are compatible with expectations under the reference background hypothesis.

In this section we first discuss the common statistical formalism of searches in high energy physics, and then overview these two complementary classes of model-agnostic search strategies.Figure 2:One-dimensional illustration of the difference between a collective anomaly, represented by a Gaussian bump on top of a reference exponential distribution, and an out-of-distribution event.

## 2.1Statistical formalism of searches

In the physical sciences, and particularly in fundamental physics, it is often of interest to determine whether a set of measured data deviates from the expected reference background distribution predicted by a corresponding reference background model (our current state of knowledge, for example, the Standard Model of Particle Physics or the CDM model in cosmology). This can be expressed as testing whether the distribution of the measured data includes an additional signal component on top of the background distributionpdata​(z)=(1−)​pb​(z)+ps​(z).p_{\rm data}(z)=(1-\lambda)\,p_{b}(z)+\lambda\,p_{s}(z).(1)

Hereps​(z)p_{s}(z)andpb​(z)p_{b}(z)denote the probability distributions of the signal and the background, respectively. The signal distribution is unknown, while the background distribution is typically not available in closed analytical form but can often be sampled either through Monte Carlo simulations of the underlying physical processes or through measurements in signal-free control regions. The parameter0≤≤10\leq\lambda\leq 1represents the signal strength and is also unknown111We note that this not the most general parameterization, as new phenomena can also introduce effects not parameterizable by a single linear parameter, (e.g. negative deviations from the reference via quantum interference effects), however we omit these complexities for now to illustrate the main ideas.

When the signal component is unspecified or unknown, the search for this type of population-level discrepancies is sometimes referred to ascollective anomaly detection. This approach stands in contrast to pointwise anomaly detection—such as outlier or out-of-distribution detection—which focuses on determining whether individual data points are atypical underpbp_{b}. See Figure2for an illustrative example.

To perform a complete statistical test for the presence of a signal, a test statisticttis defined to measure how much the data differs from the background only hypothesis.
Large values of the test statistic indicates a potential tension with the null (background-only) hypothesisH0H_{0}.
To quantify this statement, the distribution of the test under the null hypothesisp​(t|H0)p(t|H_{0})needs to be known or estimated. Consequently, thepp-value is defined aspvalue=P​(t≥tobs|H0)=∫tobs∞p​(t|H0)​𝑑t,\textrm{p}_{\rm value}=P(t\geq t_{\rm obs}|H_{0})=\int_{t_{\rm obs}}^{\infty}p(t|H_{0})dt,(2)

wheretobst_{\rm obs}is the value of the observed test statistic, as illustrated in Fig.3. Thepvalue\textrm{p}_{\rm value}is then the probability to obtain data as or more extreme as the observed ones under the null hypothesis, and the result of the test is considered statistically significant ifpvalue\textrm{p}_{\rm value}is smaller than a pre-selected rate of type-I errors (false-positive rate), defined as=P​(t≥t|H0).\alpha=P(t\geq t|H_{0}).(3)

In particle physics, it is customary to express the statistical significance of a result in terms of a Z-score, defined asZ=(1−pvalue)−1Z={}^{-1}(1-\textrm{p}_{\rm value}), where-1denotes the quantile function of the standard normal distribution.

In a classical model-dependent search, where both the signal (alternative) and background hypotheses are fully specified, the Neyman–Pearson lemma states that the most powerful test statistic is the likelihood ratio between the background-only and signal + background hypotheses:Ls+b,b=ps+b​(z)pb​(z)=(1−)​pb​(z)+ps​(z)pb​(z)=(1−)+ps​(z)pb​(z)=(1−)+Ls,b.L_{s+b,b}=\frac{p_{s+b}(z)}{p_{b}(z)}=\frac{(1-\alpha)p_{b}(z)+\alpha p_{s}(z)}{p_{b}(z)}=(1-\alpha)+\alpha\frac{p_{s}(z)}{p_{b}(z)}=(1-\alpha)+\alpha L_{s,b}.(4)

As we can see, this is just a monotonic rescaling of the likelihood ratio between signal and backgroundLs,bL_{s,b}222Note that the monotonicity betweenLs+b,bL_{s+b,b}andLs,bL_{s,b}only holds for a single observation. When analyzing a collection of observations, the likelihood for the full collection will be a product of these single-observation likelihoods and due to cross terms there is no simple monotonic relationship between the∏iLs,b​(xi)\prod_{i}L_{s,b}(x_{i})and∏iLs+b,b​(xi)\prod_{i}L_{s+b,b}(x_{i}).
It can be shown that a supervised machine learning classifier trained to discriminate between two datasets effectively learns a monotonic transformation of the likelihood ratio. This property, often referred to as the likelihood-ratio trick[26], has many useful applications in hypothesis testing. In practice, this means that a classifier trained to distinguish labeled signal and background events, for example using simulated samples, can construct a nearly optimal test statistic. However, such a methodology requires a fully specified signal hypothesis. The challenge for model-agnostic searches is therefore to design powerful test statistics without assuming a specific signal model.

## Global and localpp-value

In searches for new phenomena, the statistical interpretation of an observed excess is commonly expressed in terms of alocaland aglobalpp-value. These two quantities differ when multiple hypothesis tests are performed in a single search. This often occurs because some parameter of the signal such as an invariant mass is unknown and a different hypothesis test is performed for different candidate values. The localpp-value quantifies the probability, under the null hypothesis, of obtaining a fluctuation at least as significant as the one observed at a specific point in the parameter space being tested (for instance, a particular hypothesis of the invariant mass). This measure reflects the local incompatibility of the data with the null hypothesis but does not account for the fact that many such hypotheses may have been tested. When multiple hypotheses have been tested (e.g., a search across a wide mass spectrum), the probability of observing a large fluctuation for at least one hypothesis. This so-calledlook-elsewhere effect(LEE) is corrected for by evaluating theglobalpp-value, which represents the probability of obtaining, anywhere in the search region, an excess at least as significant as the one observed. As a result, the globalpp-value is typically larger than the corresponding local value, leading to a reduced global significance once the LEE is taken into account. This effect is known in the statistical literature as themultiple testing problem. Though not directly a manifestation of the LEE, model-independent searches often face a similar tradeoff between the breadth of signal hypotheses being covered and sensitivity to detect any particular signal hypothesis.

## Simple and composite hypotheses

In the context of hypothesis testing, a distinction is made betweensimpleandcompositehypotheses. A simple hypothesis specifies the probability distribution of the data completely, with all parameters fixed (for example, a background-only model with known normalization and shape). This is the case, for instance, in fully model-dependent searches. In contrast, a composite hypothesis encompasses a family of possible distributions characterized by one or more free parameters, such as an unknown signal strength or particle mass. According to the Neyman–Pearson lemma, for testing two simple hypotheses there exists amost powerfultest, that is, a test that maximizes the probability of correctly rejecting the null hypothesis for a given significance level. However, this result does not extend to composite hypotheses: when continuous signal hypotheses are involved (such as a signal with an unknown cross section or mass), no single test statistic can be uniformly most powerful across all parameter values[27]. In practice, one constructs tests based on the likelihood ratio, often using profile likelihood methods, which typically provide tests with good sensitivities and frequentist properties even in the absence of a strictly most powerful test.

## No optimal model-independent test

In model-independent tests, the set of alternative hypotheses may be quite large.
One would ideally design a statistical test that has maximum power to detect deviations coming from all possible alternatives. However, it has been proven that this is not possible. Statistical tests cannot have power to detect all alternative hypotheses[28]. This means that any model-independent search strategy will be insensitive to some set of deviations.
Therefore, it behooves these strategies to use a set of physically motivated assumptions or parameter choices in their construction, so that they achieve sensitivity to genuine physical anomalies and diminish their sensitivity to unphysical deviations caused by statistical noise or instrumental failures.
This also motivates the use of multiple strategies, which may make complementary assumptions, and thus have complementary sensitivities, in the search for unknown signals.Figure 3:Illustration of the distribution of the test statistic under the null hypothesis and thepp-value (red region).

## 2.2Two-sample testing for model-independent searches

A natural framework to formalize the statistical methodology for model-independent searches is throughtwo-sample hypothesis testing. Suppose we have two datasets,𝒳={x1,…,xn}\mathcal{X}=\{x_{1},\dots,x_{n}\}and𝒴={y1,…,ym}\mathcal{Y}=\{y_{1},\dots,y_{m}\}, with points in add-dimensional space,xi,yj∈Rdx_{i},y_{j}\in\mdmathbb{R}^{d}, drawn frompbp_{b}andpdatap_{\rm data}respectively. The goal of the statistical test is to asses whether the null hypothesis that both sets come from the same distribution,H0:pb=pdataH_{0}:p_{b}=p_{\rm data}(hence=0\alpha=0according to Eq. (1)), can be rejected. The alternative hypothesisH1H_{1}is simply the negation ofH0H_{0}and no specific signal hypothesis is introduced.
In the context of searches for new physics, the null hypothesis corresponds to the background-only hypothesis, where the observed data are consistent with the predictions of the Standard Model. Conversely, the alternative hypothesis implies a deviation from the Standard Model expectation, such as the presence of a new particle or interaction. Within the landscape of Fig.1, these approaches make strong assumptions about the background, as it requires the reference distribution to be known well, and minimal assumptions about the signal.

A test statistic for a two-sample test can then be defined as a function of the observed and reference data:t:Rn×d×Rm×d→R.t:\mdmathbb{R}^{n\times d}\times\mdmathbb{R}^{m\times d}\to\mdmathbb{R}.(5)

The distributionp​(t|H0)p(t|H_{0})is often not available in closed analytical form and must therefore be estimated. Common approaches rely on randomized resampling methods such as permutation tests or bootstrapping. In a permutation test, for instance, the test statistic is repeatedly computed on random reshufflings of the labels characterizing the reference and the data samples, thereby generating an empirical distribution of possible outcomes under the null hypothesis[29]. If the data contain a contribution from new physics, the observed value of the test statistic on the original partition will typically appear extreme compared to those obtained from the randomized datasets, since the new-physics contribution becomes diluted by mixing signal and background events. Alternatively, when a reliable generator of background data is available, the null distribution can be estimated by repeatedly evaluating the test statistic on pairs of independent samples drawn from the background distributionpbp_{b}, thereby strictly satisfying the background-only hypothesis. This is a common situation in particle physics, where, even though Standard Model predictions are well understood, complex detector effects make the probability distribution of the data analytically intractable, making the use of sophisticated Monte Carlo simulators essential.

## The role of ML-based methods

This type of model-independent collective anomaly detection is particularly demanding in high-precision fields such as HEP. Difficulties arise from both the large number of events and the high-dimensional nature of the datasets, and the expectation that deviations from the background model may be small (exhibiting a poor signal-to-noise ratio), hidden (appearing in uncommon or weakly constrained observables), or both. Traditional two-sample test approaches are either one-dimensional (e.g., the Kolmogorov–Smirnov test) or rely on binning the data (e.g., a binned2test), which becomes infeasible in more than a few dimensions and is strongly affected by the choice of binning scheme.
Machine learning-based methods for two-sample testing have been proposed in the last few years as promising approaches to address these challenges, due to their ability to fit complex patterns in multidimensional data.
A class of proposals is based on the idea of using classifiers to separate the background data from the measured data (see for instance Refs.[30,31,32,33,34,35,36]), without explicit hypotheses on the nature of potential anomalies. Classifier performance metrics, such as accuracy or the area under the ROC curve, can then serve as test statistics. By exploiting the ability of classifiers to learn the likelihood ratio, one can design powerful, data-driven hypothesis tests that mimic the Neyman–Pearson construction. Recent studies[36,37,38]have shown that such likelihood-ratio–based approaches can outperform traditional classifier metrics in sensitivity. Other approaches, inspired by the data-science and machine learning literature, are based on introducing a test statistic from a notion of distance between distributions that is multivariate in nature. Examples of these methods include the Kullback–Leibler divergence, the maximum mean discrepancy[39,40]and the Wasserstein distance[41,42,43].

ML-based methods also fall within the framework of composite hypothesis testing. Classifiers operate under specific training assumptions and (hyper-)parameter choices. Since the true underlying distributions and nuisance parameters are not known exactly, the resulting test statistics are not guaranteed to be most powerful in a uniform sense. Nevertheless, they can offer near-optimal sensitivity within the region of the parameter space where the training is representative, effectively serving as flexible, data-driven approximations to the exact likelihood ratio. This challenge is closely related to the multiple testing problem discussed above: each distinct choice of model architecture, training dataset, or hyper-parameter configuration effectively defines a separate test. Recent proposals have suggested leveraging this fact to improve the sensitivity of learning-based analyses by aggregating results from multiple trained models or hyper-parameter settings[44,45,46]. Such ensemble-based strategies can indeed enhance discovery potential by capturing complementary features of the data. However, they do not yield a single test that is most powerful under all possible alternatives, and if applied excessively they can lead to an overall loss of power due to overfitting or implicit trials effects.

## The reference hypothesis

One difficulty in the application of two-sample testing methods is the construction of the reference hypothesis.
In HEP, we are fortunate to have access to very high quality simulators which can be used to simulate the standard model and encode the reference hypothesis.
For some final states these simulators are sufficient to describe the data within known systematic uncertainties and can be used to conduct a two-sample test.
However, in many other final states, particularly those involving contributions from backgrounds relating to the strong nuclear force, it is known that the simulators
are not of a sufficiently high quality to accurately describe the data with the necessary precision.
In standard supervised analyses these final states therefore require data-driven methods to estimate the normalization and shape of the standard model background.
Whether these methods can be extended to construct a sufficiently high-quality multi-dimensional background estimate which can serve as reference distribution for modern ML-based two-sample test methods is an open research question. Indeed, if the background estimate is not sufficiently precise, the statistical test may identify a discrepancy between the background sample and the observed data even in the absence of any new-physics signal.


A related collective anomaly detection strategy that differs from two-sample tests are tests for the violation of a symmetry in the data in an unsupervised way[47,48,49,50].
The basic idea of these methods is to test if a symmetry-transformed version of the data is statistically distinguishable from the original data.
If so, it means the symmetry is violated in some way.
Such symmetry violations are collective phenomena, related to distributional properties of the data rather than specific instances.
They differ from the aforementioned general methods in that they focus on a particular type of symmetry-violating alternative hypothesis.
This limits their scope of alternatives, but allows them to be performed without an explicit reference distribution needed for a typical two-sample test.

## 2.3Methods for model-agnostic signal selection

Rather than directly performing the full statistical test for the presence of anomalies, some methods seek instead to identify subsets of the data which are enriched in signal events.
This is often employed when one does not have a full model of the reference hypothesis, meaning a direct two-sample test cannot be performed.
Instead, the potentially anomalous subset is identified, and then used in different ways depending on the application.
In some cases, a statistical analysis is performed on the anomalous subset, using some auxiliary information to estimate their likelihood under the null hypothesis, and obtain app-value.
In other applications, often realtime anomaly detection systems, the anomalous subsets are saved for later downstream analysis, or flagged for human inspection, but no statistical analysis is directly performed.
Approaches to the task of model-agnostic signal-enhancement can be generally categorized into two classes.

The first class of techniques is based on the idea ofoutlier detection(see Figure2).
Usually in the search for anomalies, background events dominate the data sample.
Portions of the data sample known to have negligible signal can be used to learn the distribution of the dominant background.
Data instances which are very unlikely under the background distribution can therefore be considered anomalies. In essence, this technique defines1pb​(z)\frac{1}{p_{b}(z)}as an anomaly score.

The second set of techniques, calledweak supervision, perform a type of collective anomaly detection to learn the unique characteristics of the signal that distinguish it from background.
Classifiers are trained to distinguish between a subsample of the data containing potential anomalies and a data-driven estimate of the background.
If there is an anomalous signal present in the data subsample, a classifier will learnps​(z)pb​(z)\frac{p_{s}(z)}{p_{b}(z)}, the optimal signal versus background classifier.
This classifier can then be used to identify anomalous events on an orthogonal data sample.
Constructing appropriate samples for weakly supervised training relies on additional domain-specific assumptions, often leveraging the localization of the signal in some feature.

There are additional techniques which live somewhere in between full model agnostic approaches and traditional supervised methods. These usually use some representative signal models as a loose prior[51,52]. As the focus of this review is on fully model-agnostic methods, we will not discuss them further.

## 2.3.1Outlier detection

Outlier detection is based on learning the multidimensional distribution of background events and then identifying anomalies as events that are dissimilar with respect to this learned distribution (see Figure2). Since data samples are typically dominated by background processes, these methods are often trained directly on a subset of the data itself.

Learning multidimensional probability distributions that allow for direct estimation of the probability density is a challenging task, so many applications instead rely on a proxy objective to encode the background probability density. A commonly used machine-learning model for outlier detection is the autoencoder, first proposed for applications in particle physics in[53,54]. Autoencoders are neural networks that take input data of dimensionZ∼RdZ\sim\mdmathbb{R}^{d}and encode it, via an encoder networkE​(z)E(z), into a latent space of smaller dimensionY∼RkY\sim\mdmathbb{R}^{k}, withk<dk<d. A decoder networkD​(y)D(y)then maps this latent representation back to the original space in an attempt to reconstruct the input.
Formally, the network is defined byE​(z)=yE(z)=yandD​(y)=z′D(y)=z^{\prime}, and it is typically trained by minimizing a L2 reconstruction loss,ℒ=∥z−D​(E​(z))∥2\mathcal{L}=\lVert z-D(E(z))\rVert^{2}.

When trained on a sample dominated by background events, the autoencoder learns to perform this compression and decompression efficiently for such events. An anomalous event is then effectivelyout of distributionwith respect to the training data, causing the autoencoder to reconstruct it poorly. The resulting L2 reconstruction loss can therefore be used as an anomaly score.
This L2 loss can be seen as proxy for a quantity like∼1pb​(z)\sim\frac{1}{p_{b}(z)}, but in practice it has several limitations.

An alternative strategy to autoencoders is to learnpb​(z)p_{b}(z)directly through density estimation techniques.
This can be accomplished, for example, using variational autoencoders[55,56], which enhance the original autoencoder architecture by enforcing a multivariate Gaussian structure in the latent space via additional terms in the loss function.
The Gaussian structure allows the estimation of the likelihood of a data point, by first transforming it into its latent vectoryyand then evaluating the likelihood ofyyunder the known multivariate Gaussian distribution.
Other machine learning models, such as normalizing flows or flow matching diffusion models[57,58], also allow multivariate density estimation and can therefore be used for outlier detection[59,60].
These models are generally believed to scale more effectively and to model complex multivariate densities more accurately than variational autoencoders.

## Fundamental Limitations

One inherent limitation of all outlier detection methods, which implicitly define anomalies as regions of low probability densities, is that probability densities are not invariant under coordinate transformations (see the work in Ref.[61], product of a discussion that took place at thePhyStat-Anomaly workshop).
This means that the notion of regions of low probability density, and therefore what an outlier detection method defines as an anomaly, depends on the coordinate system.
Under an invertible transformation of the datay=f​(z)y=f(z), the probability density changes topy​(y)=pz​(f−1​(y))​|dd​y​f−1​(y)|p_{y}(y)=p_{z}(f^{-1}(y))|\frac{d}{dy}f^{-1}(y)|(6)

where the last term is the Jacobian of the transformation.
For non-trivial mappings, this Jacobian can radically alter the location of high- and low-density regions when going fromxxtoyy.
or example, ify=z2y=z^{2}, andpy​(y)∼e−k​yp_{y}(y)\sim e^{-ky}thenpz​(z)∼z​e−k​z2p_{z}(z)\sim ze^{-kz^{2}}.
This change of variables radically alters the interpretation of they=z=0y=z=0point, aspz​(0)p_{z}(0)is the peak of the probability distribution but is the minimum forpy​(0)=0p_{y}(0)=0.
Alternatively, iff​(x)f(x)is the cumulative distribution function ofxx, then inyyall points will have uniform density and no point will be rarer than any other.
In practice this means that the choice of data representation and pre-processing transformations define significant inductive biases that determine what kind of anomalies the method will be sensitive to.
Signals which do not live in the low-density regions of the chosen data representation will be missed by outlier detection methods.
Therefore, significant care should be put in the choice of data representation for any outlier detection strategy.
See Ref.[62]for an extended discussion of these limitations.

Note that for ratios of probability densities, likeLs,b​(x)L_{s,b}(x), the Jacobian of the coordinate transformation in the numerator and denominator cancels out and therefore the classification score is invariant. This is one of the main advantages of likelihood-ratio-based methods, as discussed in the other sections.

Another significant challenge specific to outlier detection-based methods is their so calledcomplexity bias.
For autoencoders, because the anomaly score is based on a compression task, more complex data instances (of a higher intrinsic dimension) tend to receive larger anomaly scores regardless of whether they are present in the training sample.
Interestingly, similar biases have been observed for density estimation methods when evaluating out of distribution samples[63,64].
One manifestation of this bias is that an autoencoder trained exclusively on QCD jets is able to identify top jets as anomalous, whereas an autoencoder trained on top jets struggles to identify QCD jets as anomalous[65].
Normalized autoencoders[66,67]attempt to mitigate this issue by turning autoencoders into energy based probabilistic models.
In this approach, the network is penalized for accurately reconstructing out-of-distribution data, leading to a better representation ofpb​(z)p_{b}(z)than that obtained with a standard autoencoder.

## 2.3.2Weak supervision

Weak supervision seeks to train a classifier to learn to identify anomalies using only the data sample.
Typical classifiers rely on labeled events for training, which are not available for most data samples containing anomalies.
In Classification Without Labels (CWoLA)[68], noisy labels based on mixed samples of events are used instead.
Suppose one has two samples,M1M_{1}andM2M_{2}, which are composed of a mixture of signal and background events.
The composition of each sample is unknown, but for some reason one knows thatM1M_{1}has a larger fraction of signal events in it (f1f_{1}) thanM2M_{2}does (f2f_{2}).
Then, training a classifier to distinguish between fromM1M_{1}andM2M_{2}will converge to the optimal signal versus vs background classifier.
This is because the likelihood ratio betweenM1M_{1}andM2M_{2}is just a rescaled version of the likelihood ratio between signal and background:LM​1,M​2​(z)=pM​1​(z)pM​2​(z)=f1​ps​(z)+(1−f1)​pb​(z)f2​ps​(X)+(1−f2)​pb​(z)=f1​Ls,b+(1−f1)f2​Ls,b+(1−f2).L_{M1,M2}(z)=\frac{p_{M1}(z)}{p_{M2}(z)}=\frac{f_{1}p_{s}(z)+(1-f_{1})p_{b}(z)}{f_{2}p_{s}(X)+(1-f_{2})p_{b}(z)}=\frac{f_{1}L_{s,b}+(1-f_{1})}{f_{2}L_{s,b}+(1-f_{2})}.(7)

One can check that forf1>f2f_{1}>f_{2}this is just a monotonic rescaling ofLs,bL_{s,b}and therefore defines an equivalent classifier.
This is clear in the limit off2→0f_{2}\to 0, which occurs when theM2M_{2}sample is essentially pure background, which occurs in many HEP applications of this technique.

The training setup shown graphically in Figure4.Figure 4:An illustration of weakly supervised training. A classifier is trained to distinguish between two mixed samples of signal and background events. Taken from[68].

The key assumption underlying weak supervision is that the background events in the two samples are sampled from the same underlying distribution.
If this is true, the only way to distinguish the two samples is the difference in relative signal fractions between the two samples so the classifier will learn to distinguish signal versus background.
If there is any bias such that the background events from the two samples do not come from the same distribution, then this will typically dominate the loss (because anomalies are typically rare, sof1<<1f_{1}<<1) such that the network will learn this background bias rather than signal vs background discrimination.

To apply this technique to anomaly detection, one must define a method to construct the mixed samplesM1M_{1}andM2M_{2}from the unlabeled data.
There is no generalized procedure to do this.
Applications of weak supervision rely on domain-specific physics knowledge to appropriately define the samples.
As discussed further in Section4, many different techniques have been proposed to construct theM2M_{2}sample based on interpolation, reweighting and transport methods[69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90].

The most well studied application of weak supervision is for resonant searches, first proposed in[69,70].
In a weakly supervised resonance search the signal is assumed to be localized in a narrow region of some pre-defined resonance mass. This allows the signal-enriched sample,M1M_{1}to be defined using a window in the resonant variable, and theM2M_{2}sample can be constructed through interpolation of background events outside this window.
An example application of this method to a resonant signal is given in Section4.

Similar methods have also been applied to astrophysical data to automate the detection of stellar streams[91,92,93,94].
Exploring additional domains where such samples can be constructed and weak supervision applied is an open research direction.

Because the weakly supervised classifier is trained on events from the signal region of the analysis, it should then not be applied to those same events to identify anomalous events.
Otherwise, an overfitting of the classifier would lead to a bias in the search result.
However, one would like to avoid ’wasting’ some portion of the data to only to train the classifier, which would reduce the statistical sensitivity
of the search.
Instead,kk-fold cross-validation schemes have been used, in which the data sample is split intokkseparate folds.
The data fromk−1k-1folds are used to train the classifier which is then applied to thekkth fold to select events and perform statistical analysis.
The procedure is then repeatedkktimes, rotating usage the different folds so that each fold is used to select events exactly once.

It has recently been pointed out[95,96]that because a given region is used to both define the event selection and search for an excess, statistical
fluctuations can be amplified, incurring an effective LEE.
This means that thepp-values from any statistical analysis making use of cross-validation should be a considered a ‘local’ value which must be calibrated with toys
to determine its global significance.
More research needs to be done to establish best practices to mitigate this affect and properly calibrate globalpp-values in a computationally tractable manner.

A well-understood statistical effect in weakly supervised searches is that the efficiency to select signal events as anomalous depends strongly on the amount of
signal in the dataset.
If there is no signal present in the dataset, then the weakly supervised training procedure will have the impossible task of attempting to differentiate two datasets of pure background events.
The resulting classifier will then likely overfit some random statistical difference between the two samples.
It will therefore have very low efficiency at selecting any anomalies.
However, if there is a large amount of signal present in the dataset, the asymptotic properties of weak supervision discussed above will manifest, and the performance classifier will approach that of a supervised classifier, resulting in large signal efficiency.
For intermediate signal strengths the performance increases as a function of the signal strength.
As discussed in Section5.3, this property complicates the extraction of exclusion limits from weakly supervised anomaly detection searches.

## 2.4Comparison of Approaches

Given these various options, one might wonder which method should be employed in a given application. We provide a recommendation in terms of a simplified flowchart in Fig.5.

When one has access to high quality reference data encoding the null hypothesis, we recommend two-sample tests as they are arguably the most signal-model-independent strategy.
Two-sample tests also perform a full statistical test whereas the other methods require an additional application-specific strategy to extract a statistically meaningful statement.
However, in many cases one does not have the required high quality reference data, in which case one of the signal-enhancing methods must be employed.
In this scenario, weak supervision is preferred when searching for group / collective anomalies, due to their coordinate invariance and asymptotic optimality properties.
Weak supervision requires an approximate background sample to be constructed, often in a data-driven way.
These data-driven background estimates usually necessitate some assumption on the signal (e.g. a resonance).
In situations where this is not possible, or one is not searching for a collective anomaly (such as in realtime detection applications), we recommend outlier detection strategies.
We also comment that because outlier detection strategies do not train on the signal region data they bear the most similarity to traditional search strategies and therefore may offer best ease-of-use.

Once the signal-enhancing methods have been employed to identify potential anomalies, a statistical test still needs to be deployed to extract a significance.
Such a statistical test will require an estimate of the background, which will require the use of some domain-specific assumptions or methods (e.g. a bump-hunt fit to search for a resonance).

It should be noted that if one would like to perform a two-sample test and retain sensitivity to outliers, an appropriate test must be chosen.
For example in the one dimensional setting, the Kolmogorov-Smirnov test is known to be insensitive to tail effects and would likely miss outliers, whereas an Anderson-Darling test might be sensitive to such outliers.
Likelihood-ratio-based tests should in principle be sensitive to such outliers.
As if the reference density indeed goes to zero for the outlier point, the likelihood ratio should go to infinity.
However, in practice these tests rely on learning the likelihood ratio empirically from the data and may struggle to learn it well from only a single outlying data instance.
More work is needed to understand the behavior of these multivariate two-sample tests in this regime.Figure 5:A flowchart illustrating an proposed set of criteria to determine when to use the three main classes of anomaly detection methods.

## 3Two-sample Test Case Study: NPLM

## 3.1Foundations

The New Physics Learning Machine (NPLM) is an approach to signal-agnostic searches designed to perform a Goodness-of-Fit (GoF) test, i.e. a particular type of hypothesis test that assesses whether observed data are compatible with a given reference distribution without relying on a specific alternative hypothesis. Its purpose is to detect generic deviations from the reference model.

The Neyman–Pearson (NP) framework for hypothesis testing[1], by contrast, is based on comparing the relative likelihood of two competing hypotheses and provides the optimal test statistic for simple hypotheses. NPLM leverages this principle to implement a GoF test by learning an alternative hypothesis directly from the data. In this way, it combines the hypothesis-testing foundation of the NP approach with the model-independence characteristic of GoF tests. The connection between goodness-of-fit tests and the Neyman–Pearson construction underlying NPLM was first discussed in Ref.[97]and, more recently, in Ref.[37].

We consider here NPLM as a two-sample testing case study for two main reasons. First, it provides a representative example of a broader class of model-agnostic methods based on two-sample testing, in which a flexible model is trained to distinguish observed data from a reference sample (see, e.g., Ref.[36]). Second, it is currently the only approach of this type that incorporates the treatment of systematic uncertainties, which are discussed in more detail in Section3.2.

More concretely, the goal is to compare a reference background modelRR(for example the SM or the CDM model) with data by exploring a parametrized family of modelsHwH_{w}, which defines a composite alternative hypothesis. The method is designed to approximate the maximum log-likelihood ratiot​(𝒳)=2​maxw⁡log⁡ℒ​(Hw|𝒳)ℒ​(R|𝒳),t(\mathcal{X})=2\max_{w}\log\frac{\mathcal{L}(H_{w}|\mathcal{X})}{\mathcal{L}(R|\mathcal{X})},(8)

computed on the data of interest𝒳\mathcal{X}.
Concretely, the alternative hypothesis is defined as a local deformation of the background distributionnw​(z)=efw​(z)​nb​(z),n_{w}(z)=e^{f_{w}(z)}\,n_{b}(z),(9)

whereℱ={fw}\mathcal{F}=\{f_{w}\}is a rich family of functions parametrised byww, for example neural networks or kernel methods. Here, the symboln​(z)n(z)denotes anumber density, namely the probability density function normalized to the number of expected events under a certain physical hypothesis. For example, for the background model it would readnb​(z)=N​(b)​pb​(z)n_{b}(z)=N(b)\,p_{b}(z). This captures both changes in the shape of the distribution and shifts in the overall event rate, as in counting experiments[32,35]. In practice, as anticipated in Section2.2, a classifier is trained on measurements and background data to directly approximate the ratio of the data-generating distributionsfw^​(z)≈log⁡ndata​(z)nb​(z),f_{\hat{w}}(z)\approx\log\frac{n_{\rm data}(z)}{n_{b}(z)},(10)

wherew^\hat{w}are the optimal parameters at the end of training.

The algorithm is trained to minimize a loss function consisting of two components: a fitting term, designed to enforce Eq. (10) (for example, a binary cross-entropy loss as in Ref.[35]), and a regularization term that constrains the model’s complexity (such as anL2L^{2}penalty).
At the end of training, the model is evaluated in-sample on the entire dataset using the metrictobs​(𝒳,𝒴)=−2​[N​(b)m​∑z∈𝒴(efw^​(z)−1)−∑z∈𝒳fw^​(z)],t_{\rm obs}(\mathcal{X},\mathcal{Y})=-2\left[\frac{N(b)}{m}\sum_{z\in\mathcal{Y}}\left(e^{f_{\hat{w}}(z)}-1\right)-\sum_{z\in\mathcal{X}}f_{\hat{w}}(z)\right],(11)

which is a Monte Carlo–based rewriting of the extended log-likelihood ratio, as detailed in Refs.[32,35]. This quantity defines the NPLM test statistic. Here,𝒳\mathcal{X}denotes the data sample of interest of sizenn,𝒴\mathcal{Y}a background sample of sizemm(also referred to asthe reference sample), andN​(b)N(b)the expected number of measured events under the reference background model.

This method enables the construction of a likelihood-ratio test without the need to specify the hypotheses a priori, as they are inferred directly from the training dataset. If the data sample exhibits anomalous behavior relative to the background sample, the learned functionfw^​(z)f_{\hat{w}}(z), which encodes the reweighting between the data-generating PDFs as expressed in Eq. (10), can be examined to identify the most discrepant regions in the input-feature space and their combinations, for example an invariant mass not given as an input to the model. An illustration of the pipeline is provided in Fig.6.Figure 6:An illustration of the NPLM method (input data is unbinned).

The null hypothesis for the NPLM test is typically estimated through repeated evaluations of the test statistic on pairs of samples drawn from the background distribution, as described in Section2.2. In practice, at each evaluation, a reference sample𝒴\mathcal{Y}is compared with a toy data sample drawn from the same background distribution to simulate measured data that are free of new-physics components. It is generally advantageous to perform the test on unbalanced datasets, with the reference sample larger than the data sample, i.e.,m>nm>n. This allows the model to learn an accurate representation of the reference distribution in Eq. (10) and makes the outcome of the test less sensitive to statistical fluctuations affecting the reference sample.

Ref.[37]provides comparisons with standard metrics and methods widely used in statistics and machine learning, such as the binned2test, the Kolmogorov–Smirnov test, the area under the ROC curve, and classifier two-sample tests[31]. A recent comparison of NPLM with other statistical tests can be found in Ref.[38].

## 3.2Systematic uncertainties

In the context of two-sample testing for signal-agnostic searches, NPLM is currently the only approach that incorporates a treatment of systematic uncertainties affecting the simulation of background data[98]. The goal of this development is to enhance robustness against a potentially misspecified background model, as depicted in Fig.1. The methodology is inspired by the profile likelihood-ratio approach commonly used in statistical analyses at the LHC[99]. Each source of uncertainty in the background Monte Carlo simulation is associated with a nuisance parameter , so that the reference background model is promoted to a family of modelsRRand interpreted as a composite hypothesis. The alternative hypothesis is again formulated as a deformation of the background model, as in Eq. (5), hence depending on bothwwand . The test statistic the model aims at computing is nowt​(𝒳)=2​log⁡maxw,⁡ℒ​(Hw,|𝒳)max⁡ℒ​(R|𝒳).t(\mathcal{X})=2\log\frac{\max_{w,\nu}\mathcal{L}(H_{w,\nu}|\mathcal{X})}{\max\mathcal{L}(R|\mathcal{X})}.(12)

The main additional step with respect to the standard NPLM pipeline consists in learning how the reference background distribution deforms under variations of the nuisance parameters. This is achieved by using neural networks to approximate the density ratio between different realizations of the background model. Specifically, a classifier is trained to distinguish background samples generated with different values of the nuisance parameters from a nominal (central-value) reference sample, thereby learning the response of the background distribution to systematic variations. Assuming that systematic effects are small, this dependence is modeled using a low-order Taylor expansion in the nuisance parameters,r(z;)=nb​(z)nb0​(z)≈exp[(z)1+12(z)22+⋯],r(z;\nu)=\frac{n_{b}(z)}{n_{b_{0}}(z)}\approx\exp\left[\nu\,{}_{1}(z)+\frac{1}{2}{}^{2}\,{}_{2}(z)+\cdots\right],(13)

where the functions(z)i{}_{i}(z)are represented by neural networks and with the series truncated at some finite order. Once the nuisance-parameter dependence has been learned, it is incorporated into the two-sample test with minimal conceptual differences with respect to the standard NPLM pipeline at the level of the test construction. The comparison between data and simulation is then performed while allowing the nuisance parameters to vary, selecting the background model that best describes the data in the absence of new physics through a profiled likelihood-ratio construction, as detailed in Ref.[98]. Potential discrepancies are therefore assessed relative to an optimally adjusted reference hypothesis, reducing the risk of false discoveries driven by systematic mismodeling. At the same time, the test remains sensitive to genuine discrepancies that cannot be absorbed by nuisance variations.

## 3.3The role of model selection

With the rise of ML-powered approaches to data analysis and anomaly detection, various methods have been proposed over the past few years (the reader can find an exhaustive review in[100]), some of which have already been applied to experimental data (see for example[101]and[102]). Despite their potential, the adoption of these techniques introduces new challenges, particularly in understanding how model selection (the choice of hyperparameters) can impact sensitivity and introduce biases.
Let us consider, as an illustrative example, the case of the kernel-based NPLM test. The space of functions that is explored by the classifier to fit the density ratio is parametrized as a combination of Gaussian kernelsfw​(z)=∑iwi​k​(z,zi),k​(z,z′)=exp⁡[−(z−z′)222].f_{w}(z)=\sum_{i}w_{i}\,k(z,z_{i}),\quad k(z,z^{\prime})=\exp\left[-\frac{(z-z^{\prime})^{2}}{2{}^{2}}\right].(14)

If the bandwidth (a hyperparameter) is small, the model would favor narrow resonances while, if it is large, the model will more easily detect broader excesses in the data with respect to the reference predictions. On the one hand, this can be exploited to enhance sensitivity to specific signal hypotheses of interest. On the other hand, this effect is present for any hyperparameter of a learning model, including the architecture of a neural network and the parameters driving regularization, whose impact on the outcome of the test is more opaque. If the goal is to maintain signal agnosticity as much as possible, strategies must be developed to address this issue. In[46], the authors explored the possibility to leverage multiple testing to “turn a bug into a feature”, namely to combine multiple tests characterized by different choices of hyperparameters in ways that are robust against the LEE. It was shown that the sensitivity of the resulting test is more homogeneous across a number of benchmark of possible new physics signatures. This strategy can be applied to different framework beyond NPLM. However, it should be kept in mind that there is, generally speaking, a tradeoff between sensitivity and model-agnosticity.

## 3.4Validation of the null hypothesis

In two-sample testing, the null hypothesisH0H_{0}asserts that the two data-generating distributions are identical. Informally,validation of the null hypothesisrefers to verifying that the test behaves as intended whenH0H_{0}is true. In practice, this means confirming that the test controls the Type I error at the nominal level (the chosen significance level ) and that the resultingpp-values are uniformly distributed underH0H_{0}.

When the null distribution of the test statistic is estimated via permutations, and all test hyperparameters are fixeda prioriand are not selected using label-dependent procedures, these properties are guaranteed by construction. In particular, for permutation-based tests, there exists anon-asymptoticguarantee[29]: if the data are exchangeable underH0H_{0}and thepp-value is computed correctly, then the test controls the Type I error at level for any finite sample size, up to Monte Carlo error due to a finite number of permutations.

Nevertheless, checking Type I errors and the distribution ofpp-values remains good practice regardless on howp​(t|H0)p(t|H_{0})has been estimated, as such checks may help identify implementation errors or other bugs in the testing pipeline that are not apparent from theoretical considerations alone. Empirical validation becomes crucial when the null distribution is derived from asymptotic approximations, when multiple tests are combined, or when the data exhibit potential dependence333For example due to temporal correlations in time-series data or other forms of dependence between observations that violate the independence assumptions of the test., as these situations can lead to miscalibration and incorrect Type I error rates.

NPLM is inspired by the maximum likelihood-ratio test, and it is therefore natural to investigate whether the distribution of its test statistic under the null hypothesis follows, or can be approximated by, a2distribution with a number of degrees of freedom (dof) related to the number of trainable parameterswwin the learning model, at least in certain regimes. If such an approximation holds, it could be used to compute app-value without the need to estimatep​(t|H0)p(t|H_{0})using toy experiments, or to ensure that the test statistic is well behaved and not heavy-tailed. This is a desirable property, as heavy tails can inflate Type I errors or reduce statistical power.

For a standard likelihood-ratio test with composite nested hypotheses, the asymptotic distribution ofp​(t|H0)p(t|H_{0})follows a2distribution with a number of dof equal to the difference in the number of parameters between the alternative and reference models. This result does not generally hold for NPLM. Although no formal results establish this connection, several studies[32,33,98,35]suggest that regularization of the underlying learning model can lead to a regime in which approximate compatibility with a2distribution is empirically recovered.444It is natural to expect a connection between the level of regularization and the amount of available data, given that asymptotic results formally apply only in the limit of infinite statistics.This approximate condition can then be exploited to tune the model hyperparameters and obtain a well-calibrated test. The exact number of dof of the target2distribution depends on the specific NPLM implementation, but is generally related to the complexity of the function space spanned by the learning model. For example, in the neural-network-based NPLM implementations of Refs.[32,33], it is simply given by the number of trainable parameters of the network, interpreted as the parameters characterizing the alternative hypothesis. It is worth noting that highly regularized models tend to produce test-statistic distributions that are more sharply peaked near zero. While this behavior helps avoid heavy tails, it also significantly restricts the model’s flexibility and may reduce its ability to detect sharp or highly localized anomalous features in the data.

Since current evidence for the2approximation ofp​(t∣H0)p(t\mid H_{0})in NPLM is empirical rather than theoretical,pp-values are in practice estimated using toy experiments. The2fit is therefore used primarily as a diagnostic and calibration tool, for instance to guide hyperparameter tuning.

Finally, in the presence of systematic uncertainties, an additional validation step is required: one must verify that the distribution of the test statistic under the null hypothesis is approximately independent of the nuisance parameters. In practice, this involves estimating the null distribution using toy datasets generated from the reference model at different points in the nuisance-parameter space. Failure of this condition may lead to miscalibration and incorrect Type I error rates.

## 3.5Assessing performance

A central issue in deploying a signal-agnostic test concerns the validation of its performance. One possibility is to establish the sensitivity of the method in controlled benchmark scenarios, where the anomalous signal is specified. To obtain a robust estimate, one would ideally compare a signal-agnostic method against a well-defined ground truth. This role is naturally played by a likelihood-ratio test with fully specified signal and background hypotheses, as guaranteed by the Neyman–Pearson lemma. Since analytical PDFs are often unavailable, this test can be implemented either through standard techniques based on the choice of optimal observables and cuts, or by training a fully supervised classifier on (simulated) signal and background data to estimate the likelihood ratio, as discussed in Section2.1.
This signal-aware test yields an estimate of the highest significance (lowestpp-value) that any analysis can in principle attain. Consequently, thepp-value obtained with a signal-agnostic method can be compared to this estimatedidealpp-value. While such comparisons are inherently dependent on the choice of benchmark signals and cannot fully characterize performance across the entire space of possible new-physics scenarios, they nevertheless provide valuable insight into the potential loss of statistical power of the method for specific classes of signals. In this sense, benchmark studies offer a controlled way to quantify how much sensitivity is sacrificed in exchange for signal agnosticity. For instance, the authors of Refs.[32,33]used this procedure to assess the performance of the NPLM method across a limited set of HEP scenarios, thereby quantifying the typical sensitivity loss with respect to fully supervised analyses.

## 3.6Applications and prospects

The primary motivation for deploying the NPLM method is the search for new physics at the LHC. A practical strategy in this context is to focus on a specific final-state topology and perform the analysis using a set of variables that fully characterizes the event kinematics. At its current stage of development, NPLM is best suited to studies involving a relatively small number of features, such as dimuon final states, which provide particularly clean experimental channels with systematic uncertainties that are well understood and under control. While efforts are ongoing to deploy NPLM in real data analyses within LHC physics and beyond, several studies have explored possible extensions aimed at overcoming some of its current limitations. One such approach investigates the use offoundation modelsto improve sensitivity in high-dimensional settings[103].

More broadly, two-sample testing methods can be applied to any scenario in which one seeks to assess whether two datasets are drawn from the same underlying probability distribution. Various tasks can be naturally formulated within this statistical framework. For instance, Ref.[104]explores the use of the NPLM pipeline fordata quality monitoring, namely the real-time monitoring of particle detectors. In this application, the model hyperparameters are chosen to prioritize fast execution over model complexity. Finally, the evaluation and comparison of data-generating methods, whether based on traditional Monte Carlo techniques or on modern generative models, can also be naturally addressed within this framework, as shown for example in Refs.[38,105].

## 4Outlier Detection and Weak Supervision Case Study: Dijet Resonance Searches

The most well-studied case of classification-based anomaly detection in particle physics are resonance searches.
In a resonance search, signals manifest as a relatively narrow peak in some invariant mass distribution on top of a falling background distribution.
Bump hunt searches have been performed for a long time in particle physics.
They make minimal assumptions and typically have sensitivity to many models of new particles.
However in final states with large backgrounds, they can loose sensitivity to rare signals as the signal bump is buried under the large background.
Anomaly detection techniques can thus be used to enhance sensitivity to signals which produce distinctive features in addition the resonance.

The assumptions of a narrow resonance search, in particular the localization of the signal, can be used to define the mixed samples needed for weak supervision.
Though typically one does not know the mass of the sought-after signal,
one can guess a window in the mass distribution where one hopes that the signal is localized to.
If a signal is present in the window, the sample of events inside the window will contain some non-zero signal fraction, while events outside of the window will not.
Events in this window can then serve as the potentially signal-rich mixed sample.
Events outside this region will have very similar background events to those inside the window, but may contain some differences.
Assuming the features of the background change smoothly as a function of the resonant variable, the background in the signal region can be estimated via an interpolation from the sideband regions.
This is illustrated in Figure7Figure 7:An illustration of the resonance-based overdensity scenario. The signal is localized in particular region of the resonant variable. Within that region there is an overdensity in the feature space from the signal events that is not present in the sidebands. Figure taken from[73].

Different approaches have been taken to use the sideband events to construct the background-rich mixed sample.
The first methods[69,70,71]used a weighted sample of the events from the sidebands adjacent to the signal-window.
Others have improved upon this approach by training some sort of generative-like model from the sidebands and then interpolating it into the signal region.
Samples are then drawn from this generative model to construct the background-rich sample.
The first of these methods was CATHODE[73,74]which used a normalizing flow trained in the sidebands.
Other methods include SALAD[76,77]which uses simulation to help with the interpolation, CURTAINS[78,82]which ’transports’ events from the sidebands, , and FETA[79]which uses transport and simulation.
These methods seem to perform roughly similarly[85].
Other methods use density estimates to construct the likelihood ratio rather than a classifier[72,75,88].

The most well-studied case are dijet resonances, in which one looks for resonance decaying to two jets with anomalous substructure.
There is a large phenomenology of jets which can produce substructure distinct from that of typical QCD jets.
Jet substructure features have minimal correlation with the resonance mass, allowing one to perform a bump-hunt after an anomaly detection selection.

There have been several results anomaly detection methods to dijet final states at the LHC[17,19,23,24,25,21].
Two recent searches from the CMS[23,24]and ATLAS Collaborations[20]offer useful case studies for the application of these methods.
The CMS search deployed several different complementary anomaly detection strategies. An outlier detection method, based on a variational autoencoder (VAE) was employed. Three different weakly supervised strategies were used, each differing their construction of the two mixed samples: CWoLa Hunting[69,70], Tag N’ Train[71], and CATHODE[73].555A semi-supervised method, QUAK[51], was also employed. However as this is only a partially model-agnostic approach it will not be discussed further.The ATLAS search also deployed two different weakly supervised methods: SALAD[76,77]and CURTAINS[78].
This variety of methods employed makes them useful case studies for general validation procedures for anomaly detection searches.

## 4.1Mass decorrelation

In a bump-hunt analysis, spurious excesses can arise due to correlation between the anomaly score and the resonance mass if care is not taken.
This is a particular danger for weakly supervised methods which use windows in the resonance mass to define the ‘signal-like’ sample for training.
If the features used for classification are correlated with the resonance mass, the learned anomaly score can become significantly correlated with the resonance mass as well.
Consequently, the selection criterion on the anomaly score can significant distort the resonance mass distribution.
In the extreme case the learned anomaly score can preferentially select events in the pre-defined mass window as signal-like, which would create a localized excess of background events mimicking a signal.

Outlier detection methods can also distort the background mass distribution through a different mechanism.
Since the outlier detection methods are defined to select rare events as anomalous, and invariant masses typically have steeply falling distributions, outlier detection methods will often preferentially select events in the high mass tails as more anomalous.
This can significant distort the shape of the background mass distribution, making extraction of a signal difficult.

Preventing these sorts of mass sculpting effects are therefore of the utmost importance in building a reliable resonant anomaly detection analysis.
For the weakly supervised methods this can be achieved by using features uncorrelated with the resonance mass, and/or by improving the construction of the background-rich sample such that it has minimal kinematical differences with respect to the signal-rich sample.
For outlier detection methods, the use of mass-uncorrelated features can also be employed.
Applying event weights to the training, to upweight events in the high mass tails to equalize their density respect to the copious low mass events can also be employed.
However in the case of steeply falling distributions whose density changes by orders of magnitude, the necessary large weights can become impractical for training.
For outlier detection, because the learned anomaly score function is fixed, a post-training decorrelation between the anomaly score and the resonance mass can also be performed.
Such a strategy is much more difficult to deploy for weakly supervised methods, which have variable behavior.

The recent CMS dijet anomaly search[23]employed several strategies to mitigate the issue of mass sculpting.
The weakly supervised algorithms used a set of features only weakly correlated to the resonance mass, through a correlation with jetpTp_{T}.
Their implementation of the CWoLa Hunting[69,70]and TNT[71]weakly supervised algorithms then used a jetpTp_{T}-based reweighting between the signal-rich and background-rich samples to eliminate any residual kinematic bias during the training.
The accuracy of the background-rich sample constructed by the CATHODE[73]method was sufficient to not require this step.
The VAE, which used inputs correlated with the jetpTp_{T}, applied a post-hoc correction to decorrelate the anomaly score from the resonance mass.

## 4.2Validation Methods

There are two key properties that an anomaly-detection-based analysis must satisfy to ensure a sound result.
The first is that the false-positive rate is controlled.
That is, the employed strategy cannot be biased so as to report excesses at higher rates than expected under the background-only (null) hypothesis.
The second is that the method is effective at finding anomalies: for some example signals of a realistic strength the method will result in a statistically significant rejection of the null hypothesis, ideally at the level of discovery (55\sigma).
These are the same validations that must be done for any search strategy, however the validation of these properties are complicated in several ways by the anomaly detection methodology.

It is worth distinguishing here between the validation of outlier detection methods and weakly supervised methods, the latter of which has unique challenges complicating its validation.
For unsupervised methods, the anomaly detection algorithm is trained ‘ahead of time’, without any dependence on the signal region data. The anomaly detection algorithm therefore ‘frozen’, prior to unblinding, similarly to a supervised classifier.
For the weakly supervised methods, the training uses the signal region data, and the behavior of the anomaly detector will depend on the properties of the signal region data.
This means the exact classification algorithm will not be fully known prior to unblinding. This means the entire training and signal extraction procedure must be validated in tandem, which is more involved than validating a frozen unsupervised model.
This property also complicates the extraction of exclusion limits from weakly supervised searches, as discussed in Appendix A of Ref.[23].

## 4.2.1Validation of the Null Hypothesis

Validating that an AD method is properly calibrated under the null hypothesis – i.e., that it does not produce spurious excesses on background-only samples – is crucially important
This validation can be done in simulation, in a data control region, or by using artificial data samples obtained from a generative model.
Each strategy has a complementary set of benefits and limitations.
Therefore, the use of multiple strategies is desirable to ensure a robust validation of the method.

## Validation in simulation

The most straightforward validation strategy is the deployment of the algorithms on simulated Monte Carlo (MC) samples.
These Monte Carlo samples should be as realistic to the application on data as possible.
For the validation of weakly supervised methods, the common practice of using event weights to account for physics processes with different cross sections cannot be employed.
This is because these weights will affect the training dynamics and can influence the performance of the weakly supervised algorithm.
For example, 10,000 events each with weight 0.01 will have much less statistical noise than 100 events with weight 1; the former may therefore be easier to learn from.
When applied to real data all events will have weight 1, so the MC sample used for validation should as well.
To achieve this, events from different physics processes should be randomly sampled in proportion to their cross section.
This ensures the right composition of events in the sample while maintaining the statistical properties that will be expected on data.
The anomaly detection algorithms can then be run on this MC dataset without any signals to verify that the aforementioned mass sculpting does not occur.

While validation on the MC sample is very useful, it can also be limited in several respects.
First, MC simulation is known to have mismodelings as compared to the data, particularly for QCD processes and jet substructure observables.
While these MC sets are being used only for validation purposes, and it is not required that they exactly match the data, features present in the data not captured by the MC, such as rare detector reconstruction effects or subtle kinematic correlations, could cause issues for the anomaly detection algorithms and would not show up in MC validations.
Additionally, algorithms which make explicit use of MC samples as part of their background estimate (such as SALAD[76,77]) would not be properly tested if the same MC sample is used for validation, as realistic data-MC differences would be absent.
Systematically varied MC samples, perhaps originating from a different generator, could be used in these cases to approximate these affects, but it is likely this would not fully capture fully realistic data-MC differences.
MC samples are also of a limited size, and for QCD processes with large cross sections one often has fewer simulated events available than will be present in the actual data sample.
Running tests on these samples with limited size could fail to catch biases that are only apparent with larger statistics.
Though bootstrapping methods can be used, the limited sample size means it is difficult to run a large suite of toys to test the variability of the weakly supervised algorithms and ensure the null hypothesis is properly calibrated.

## Validation in data control regions

For these reasons, additional validation strategies are desirable to further test these algorithms.
An additional validation strategy is to run the algorithms on a data sample from a control region which is known from previous studies, or assumed based on physical arguments, to contain a negligible fraction of anomalies.
This control region should be designed to be as similar to the signal region as possible, both in terms of the number of events, and the distribution of kinematics and classification features, for a realistic test.
In a fully model independent search, it is difficult to define a control region which can be assumed to have negligible signal.
Assumptions must be made about the characteristics of the signal to justifiably claim some portion of the data is signal depleted.
For the dijet resonance searches, such a control region was defined based on an kinematic property of each event: the rapidity separation between the two jets.
Resonant signals targeted by the search would be produced via thess-channel and therefore lead to jets with a smaller rapidity separation than the dominanttt-channel QCD background.
This event property is orthogonal to the substructure features being used to look for anomalies and therefore retains the model-agnostic nature of the search.

It is possible that some other signal, not produced via thess-channel dijet topology, could indeed populate such a control region and be identified by the anomaly detection algorithm.
For example, a resonance decaying to three or more jets with anomalous substructure could result in two jets with high rapidity separation and thus populate the control region in the dijet search.
The anomaly detection methods would identify these anomalous events, leading to a rejection of the null hypothesis in the control region, complicating validation.
However, this is a general problem for all searches: one cannot rule out some other new physics model, differing from the one being searched for, contaminating a control region.
Though we note because of the broad sensitivity of anomaly detection methods, they may be more sensitive to this possibility than other searches.
Nevertheless, despite these philosophical issues, using such a control region still serves as very useful validations and was used in both the recent CMS and ATLAS searches.
In the case of any significant excess observed in such a control region, it would be necessary to study further whether it originates from a potentially genuine anomaly or a bias in the algorithm.

Control regions also have practical limitations that motivate further validation strategies.
Kinematic differences between the control region and the signal region can affect the behavior of the algorithms, potentially masking potential bias.
Additionally, control regions have finite numbers of events, limiting the ability to conduct to repeated toy experiments to test for statistical bias.
Additionally, for some searches, defining a suitable control region, with enough similarity to the signal region to serve as a useful validation, may be difficult or impossible.

## Validation on artificial samples

The recent ATLAS dijet search[20]employed a novel strategy dubbedDOWN-UP-SAMPLEas a further form of validation.
They trained a generative model on a random, small fraction of their signal region data.
This generative model is used to generate mock background samples which could be used used for pseudoexperiments to test for bias.
The initial downsample of the signal region data effectively dilutes the presence of potential anomalies, which are assumed to be rare so as to not been found by previous searches.
This means the generative model will learn the background distribution only rather than additionally learning features of potential hidden anomalies.
Tests in simulation were performed to confirm this property.
Because it is trained on the signal region data, the features learned by the generative model should have very realistic correlations, and new samples can easily generated to run a large number of pseudoexperiments of a realistic size.
This method allowed the ATLAS search to identify a significant bias in their method at low resonance masses which was not fully apparent from the other validation strategies.

One potential limitation of this validation strategy is that if the anomaly detection technique itself uses a generative model, such as in CATHODE[73]or CURTAINS[78], it may have an easier time modeling this artificial background than the true data.
All generative models have inductive biases which lead to imperfections, such as preferring smoothly varying features or underestimating tails.
A dataset coming from a generative model would already have these imperfections, and therefore the generative model trained in the pseudoexperiment would have an easier time fully modeling such an artificial dataset than it will when applied to the true dataset.
This effect could be mitigated by training the initial generative model with a significantly different architecture so as not to align its inductive biases with the model trained in the pseudoexperiment.

## 4.2.2Validation on true signals

The other necessary validation is ensuring that the anomaly detection algorithm can successfully identify a set of true anomalies.
This necessarily involves selecting a set of benchmark signal models to be used for testing purposes.

This set of benchmarks should be chosen to cover a wide phenomenological range, while still matching the target search topology.
For the dijet search this means considering many different models which produce two jets, but differing in the substructure of those two jets.
The CMS search considered benchmark models in producing jets with between two and six ‘prongs’ of energies and varied jet masses.
Employing such a wide range of signatures validates that the anomaly detection algorithm indeed have sensitivity to a broad class of models.
It may also expose a class of models which the search is not especially sensitive, which can inform future efforts.
It is not required or expected that the anomaly detection method is sensitive toallpossible models.
Every methodology will employ a set of assumptions and choose a set of input features which will leave it insensitive to some models.

## Validation in simulation

Events from these signal models can be injected into the aforementioned realistic MC sample, and the entire anomaly detection analysis pipeline, from the AD selection to extraction of significance, performed on this dataset.
The number of signal events injected should be varied to test performance for different signal strengths.
This is particularly important for weakly supervised methods whose performance changes significantly as a function of the signal strength.
The signal injections sizes should still be kept in a reasonable range, reflecting realistic signal strengths that could potentially live within the data.
Unless the search is probing an entirely new frontier or final state, extremely large signals would likely have been seen by previous searches, making performance validation in such a regime unnecessary.

## Validation in data

A validation of the AD methods identifying a true anomaly in data is also desirable.
This can be achieved by ‘rediscovering’ rare standard model processes using the chosen anomaly detection.
Such a validation requires there to be a standard model process similar enough to the characteristics of the sought after signal such that it fits within the scope of the AD method.
Rediscovery of top quarks[106]and the Upsilon[107]using anomaly detection methods have been demonstrated using open data from CMS.

In the case of the dijet search, there is no comparable standard model resonance decaying into two jets with anomalous substructure.
Instead, the recent CMS search instead used the pair production of high-momenta (boosted) top quarks as a validation process[24].
This standard process has no central resonance, but does produce two jets with anomalous substructure.
Due to the lack of a central resonance, this validation required a modification of the training strategy of the weakly supervised methods, and a change to the final signal extraction procedure.
With these changes, the AD method was shown to be able to successfully enhance the fraction of boosted top quarks from a small component of the data sample (<1%<1\%) to a large, dominant portion of the selected ’anomalous’ events.
This procedure validates that the core basis behind the AD method functions as expected, which is an important.
But due to the changes required to probe a different signal topology, some details of the procedure, such as the signal extraction method, are not validated in this approach.
Therefore it should be viewed as complementary to the aforementioned validation in simulation.
Any such validation strategy in data will be highly analysis dependent, and for many cases there may be no suitably similar standard model process to use.

## 4.3Assessing performance

How to assess the performance of the anomaly detection algorithms on the benchmark signals is also worth discussing.
Training a supervised classifier for each chosen signal can give a useful upper bound on the performance of the AD method.
However, in most cases it is expected the AD method will fall well short of this.
The minimal baseline that the AD performance must clear is that it improves the sensitivity beyond an inclusive search method, which makes no anomaly-like selection.
If possible, the inclusive search should in all other ways be identical to the anomaly detection analysis; using the same inputs objects and statistical analysis procedure, just without the selection on an anomaly score.
The significance improvement for the AD selection is approximately given by the signal efficiency of the selection (s) divided by the square root of the background efficiency (b),sb\frac{{}_{s}}{\sqrt{{}_{b}}}.
This is a non-trivial hurdle to clear; sometimes even classifiers with seemingly moderate classification performance (AUC∼0.7{\sim}0.7) do not result in significance improvements larger than one.
Ideally, to demonstrate discovery potential, the anomaly detection algorithm should enhance significances which were below the level of evidence (<3<3\sigma) in the inclusive search to discovery-level (55\sigma).
The performance of AD algorithm can also be compared to other simple selection criteria appropriate to the search.
For the dijet search the performance of the AD methods was compared to simple jet substructure selections commonly employed in searches.
For analyses focused on event-level anomalies, comparisons could be made to selections on global event quantities often employed in searches such as the scalar sum of object momenta (ST), the missing transverse energy (MET), or number of reconstructed objects in the event.
Reporting the performance of these AD algorithms with respect to these baselines is important to clearly demonstrate the gains of the AD methods.

The recent CMS search compared the performance of its AD methods to an inclusive search, as well as two sets of simple cut-based approaches, one targeting two-prong and the other targeting three-prong jets.
Their performance was also compared to supervised classifiers trained with the same features as the AD methods.
These comparisons were done for all∼20{\sim}20benchmark signal models considered.
Significance improvements with respect to the inclusive search as large as a factor of 6 were found for some signal models.
AD performance was generally a factor of two or more inferior to a supervised classifiers.
For several more challenging signals, no AD algorithm achieved improvement with respect to the inclusive search, indicating the need
for further method development or new strategies.

While the usage of benchmark signal models has great utility, they will likely not capture the full model space that an AD search will be sensitive to.
If the signal models are available to the analyzers during development of the search methodology, one may worry that the AD algorithms have been tuned to give good performance on these models.
If a significant tuning has occurred, the performance of the AD methods on unknown untested signals may be worse than the tested benchmarks.
Therefore, in future searches it would be desirable to test the performance of AD algorithms on a set of ‘validation’ signals which were not used during development of the AD algorithm and only tested at the time the algorithm is finalized and being applied to data.
This would give external readers confidence on that the benchmark performance can indeed be extrapolated as rough estimates of sensitivity to untested signals.
Ideally the nature of the signal would be blinded to the analyzers, but chosen by an external party to fall within the scope of the search.
This would be similar to the hidden signals used in the evaluation of prior community anomaly detection challenges[15,16].
However such a blinding may be difficult to achieve within experimental collaborations.

## 5Search Interpretation and Follow Up

A frequent question is how the results from such model-agnostic searches should be interpreted.
As compared to conventional searches, these model-agnostic strategies have important differences in interpretation strategies, both in the case of a significant excess and in the reporting of exclusion limits.

In the case these model-agnostic methods results in a significant excess, steps must be taken to verify its nature.
Identifying that the features of the anomalous event match those of a realistic new particle, rather than features arising from subtle instrumental or reconstruction related effect, would help verify its physical origin.
The identification of the excess’s phenomenological properties would also allow followup supervised analyses, targeting the specific signature matching the excess, to be employed to confirm the excess.

## 5.1Considerations for a follow-up targeted search

It should be noted that a targeted search designed based on the results of an anomaly detection search on the same dataset, cannot have a well-calibrated p-value.
This is because the targeted search would not have been performed if there had not been an excess seen by the anomaly detection search, so it has an unquantifiable LEE.
However, if the targeted search is performed on an independent dataset, then it can have a well-calibrated p-value.
Validation from a targeted search performed on the same dataset can still provide value in the form of additional robustness checks and more easily interpretable methodology, but its p-value should not be reported.

Therefore, to enable a full verification, it may be beneficial for any anomaly detection strategy to pre-define a holdout dataset.
This holdout dataset would be used only for analysis by the targeted search, in case of a significant excess seen by the anomaly detection method.
In ongoing experiments, such a holdout dataset may not be needed as any anomaly could be verified in future datasets, but for analyses with fixed datasets it is an important consideration.

The size of the holdout dataset is not an obvious choice.
An optimized targeted analysis will have better sensitivity than a model-agnostic one, so reserving 50% of the data for holdout would ensure the targeted follow up to have equivalent or greater statistical power than the model-agnostic one.
However, such a large holdout set would significantly reduce the statistical power of the initial model-agnostic strategy.
The ratio of sensitivities between a model-agnostic and targeted search strategy will depend on the nature of the anomaly and therefore cannot be determined a priori.
If the targeted search had two times or more the sensitivity as a model-agnostic strategy,
which is a reasonable assumption given current performance, a holdout size of 20% would ensure enough statistical power for confirmation.
A holdout size in the range of 20%-50% therefore seems reasonable.

## 5.2Excess interpretation

Before a targeted search can be performed, the nature of any observed anomaly must first be understood.
Several interpretation strategies have been investigated for both the two-sample test and for the model-agnostic signal selection methods.

## Feature distribution comparisons

One of the simplest interpretation strategies is to compare the feature distributions of the highest anomaly score events from the signal excess were compared to those of typical background events.
This comparison allows a determination of what is unique about those events causing them to be identified as anomalous.
This is among the simplest interpretability strategies, but was shown to be effective in the CMS dijet search[23].
The method could be applied to two-sample tests as well, by plotting the distribution of features for data events with the highest likelihood ratio between data and reference.
The method relies on the analyzer selecting the features a priori to check the difference between the anomalous and regular events.
If the anomalous behavior involves the correlated behavior of two or more features, it may not be clearly apparent in simple one-dimensional distributions.
Similar checks could then be performed in two-dimensional distributions or on derived features which are functions of two or more of the input features.
Some trial and error may be required to find the features which properly characterize the anomaly.

## Permutation feature importance

For classifier-based approaches, including NPLM and weakly supervised approaches, it can be useful to interpret the behavior of the classifier itself to assess what it has learned.
In[23], a classifier-interpretation method based on the permutation feature importance[108]was employed.
In the set of most anomalous events, a single chosen feature was permuted with those from a set of random other events, and the change in the classification score was computed.
The average change in the classification score across the variations was used to compute a feature importance score.
Repeating this procedure for all the input features, and then comparing their scores, allows an assessment of which features were most important in the classification of the event as anomalous.

## Active subspace method

In[36], the authors propose to interpret a trained classifier by analyzing the information encoded in the gradient of a classifier’s decision function.
When a classifier is trained for a model-agnostic two-sample test, its output defines a surface that separates the measured data from the background sample.
The gradient of this surface with respect to the input features indicates the local directions in feature space that most influence the classifier’s decision, and thus the directions along which the two samples differ.
By computing the covariance of these gradients over the data and performing an eigenvalue decomposition, the method extracts a set ofactive subspaces: dominant linear combinations of features to which the classifier is most sensitive.
Projecting events onto these subspaces returns low-dimensional, physically interpretable summaries that highlight which characteristics of the anomalous events drive the observed discrepancy.
Such information can help determine whether the excess exhibits features consistent with a realistic new-physics signal or if it is more compatible with detector or reconstruction artifacts.
The resulting interpretable directions can also guide the construction of targeted supervised analyses that specifically test the phenomenology suggested by the discrepancy that has been detected.

## Reweighting the background sample

Another approach to understanding the nature of a discrepancy found by a classifier-based two-sample test was presented in[32]in the context of the NPLM test.
As discussed in Section3, the classifier effectively learns a reweighting of the background distribution to match the distribution of the measured data (see Eq. (10)).
This learned reweighting function can be evaluated on the background events, either directly in terms of the input features or projected onto a high-level quantity such as an invariant mass.
If the measured data and background sample are compatible, the fitted functionfw^​(z)f_{\hat{w}}(z)will evaluate to approximately zero across the feature space.
Conversely, deviations offw^​(z)f_{\hat{w}}(z)from zero indicate regions where the data differ from the expected background, thereby providing a physically interpretable characterization of the discrepancy.

These strategies were found to be effective at determining the rough characteristics of the signal for both simulated signal injections and in the rediscovery of high momenta top quarks in the CMS dijet search[23,24].
Once the characteristics of the signal have been determined, a follow-up analysis which targets the specific signature of the excess can be performed.
This targeted analysis will likely achieve higher sensitivity than the model-agnostic method, as the targeted analysis can employ optimized selection criteria, background estimation and signal extraction strategies.
If the properties excess are not fully determined, several variations of the targeted analysis may be necessary to span the possibilities.
As the targeted search was based on a the results of a search performed on the same dataset, it cannot be considered a fully blinded analysis and therefore faces an difficult-to-quantify LEE. As such, it should be used only to verify that a local excess indeed exists in the region reported by the model-agnostic strategy, but caution should be taken in reporting its global significance.
A full confirmation therefore requires the same targeted strategy to be performed on an orthogonal dataset.

## 5.3Exclusion limits

Besides reporting any significant excesses, the other typical outcome of a new physics search are exclusion limits.
These exclusion limits rule out the existence of a particular new particle or phenomenon, under certain model assumptions, within a certain parameter space.
Such exclusion limits are used to the compare the sensitivities of different analyses, to assess the viability of different theories, and to identify gaps in coverage to be filled in by new analyses or experiments.

For a model-agnostic search, reporting exclusion limits is complicated by two factors.
The first is that given the broad sensitivity of these analyses it is not possible to report exclusion limits which comprehensively summarize the sensitivity of the search.
Even when a broad set of benchmark signal models are considered, there will undoubtedly be additional models to which the analysis is sensitive.
This issue could be ameliorated if such searches could easily be re-interpretable by the community, and the search’s sensitivity to additional models could be tested after-the-fact by any interested party.
Unfortunately, since these analyses are based on non-standard methodologies, they are oftentimes much more difficult to re-interpret than standard ones.

For the outlier-detection methods, reinterpretation seems more tractable.
At a high-level, these analyses are functionally similar to standard search strategies, which have been reinterpreted by the community many times.
The only difference is that the selection criteria is based on unsupervised outlier detection models, whose efficiency is not easy to parameterize.
Instead of a universal parameterization, to estimate the selection efficiency on a new signal two alternate strategies are possible.
The first is for the experiment to publicly release the machine learning model, so that it can be applied to additional signals by anyone in the community.
This strategy was adopted by a recent CMS search for resonances decaying to a Higgs plus an anomalous jet[109].
One potential concern for this approach may be that reinterpretation efforts typically use external fast simulation packages such as Delphes[110], which attempt to mimic realistic experimental simulations but are known to be imperfect.
A machine learning model trained on real data or realistic full simulations may show quite different performance on a fast-simulation sample if there is significant mismodeling.
This problem is not unique to anomaly detection, and methods such as surrogate models[111]are being explored to accommodate these limitations.
An alternative approach is to develop a dedicated portal maintained by the experiment to which new signals from the community can be submitted.
Submitted signals are then simulated by the experiment’s full simulation pipeline, and then used to evaluate the efficiency.
This approach was adopted by a recent ATLAS unsupervised search[18,112].

For weakly supervised methods and two-sample tests, reinterpretation is more challenging.
These methods directly use information from the signal region for training.
This means that the performance of the algorithm depends on the presence or absence of signal.
If there is no signal presence in the dataset, the classifier will have poor performance at detecting a hypothetical signal.
Thus directly reinterpreting a null-result search using the model which was trained on the data will yield very poor exclusion limits.
However, estimating what would have been observed by the analysis had there been a signal in the data, which is necessary to determine whether the signal is excluded by the observed results, requires an estimate of how the classifier would have performed in such a scenario.
Therefore the classifier must be retrained for different signal strengths, to determine how its performance changes as a function of the amount of signal in the dataset.
This parameterized efficiency can then be used to extract exclusion limits.
For weakly supervised methods, this procedure was first performed in the first ATLAS dijet search[18].
A more comprehensive description of the procedure is described in detail in Appendix C of the recent CMS dijet search[23].

This type of procedure suffers from limitations.
Firstly, it is quite computationally costly, as it requires running the full analysis procedure for many different signals and injection strengths and systematic variations.
As of now, this makes it impractical to do comprehensive scans of parameter space with this method.
The other major challenge is finding a realistic sample to use for these injection studies.
For the weakly supervised searches, these injections have been done by injecting signal events directly into the data.
However, the presence of some unknown signal in the data, below the detection threshold of the analysis, could affect the performance of these injections.
In Ref.[23], this was studied and determined not to produce undercoverage in the resulting exclusion limits to a significant degree, but this may not hold true in all cases.
In the future the usage of proxy samples to perform these injections may be preferable, but it is difficult to construct samples that mimic the data to a sufficient degree and are known to be signal-free.

For two-sample tests such as NPLM, the distribution of the test statistic under the null hypothesis is independent of the measured data if estimated with toy data samples (which are signal-free by construction). This means that the same null hypothesis can be tested against different sets of data with different amounts of signal injection to set exclusion limits, assuming that the background data are accurate.

This procedure also has significant challenges with reinterpretation.
To evaluate the exclusion limit requires access to the full signal region data, which is often not released by experimental collaborations.
This means exclusion limits on additional signals cannot be readily derived by those outside experimental collaborations.
One strategy to enable reinterpretation in this scenario would be to fully preserve the analysis workflow and use a portal-based approach to evaluate the analysis sensitivity to additional signals[113].
Developing faster approximate methods to estimate the analysis sensitivity would also be of great practical use.
Building upon methods from the statistics literature[114]which attempt to globally characterize what alternative hypothesis a particular test has power for could also be interesting for an assessment of more general exclusion limits.

## 6Conclusion and outlook

These new model-agnostic search strategies have great promise to expand the discovery potential of modern experiments in fundamental physics.
However, they have significant conceptual differences with respect to standard analyses, both in their goals, methods, validation strategies, and interpretation.
We have endeavored to provide a concise review the main conceptual and practical features of these methods, with a particular focus on the strategies which have been employed to validate their effectiveness.
At time of writing there have been only a handful of applications of these methods by experimental collaborations[17,18,19,20,21,22,23,24,25].
We hope this document is a useful reference as the community familiarizes itself with these new methods and establishes best practices for their validation and interpretation.

## Acknowledgments

This article is part of VERaIPHY (Validation & Evaluation for Robust AI in PHYsics), a coordinated effort that unites researchers from fundamental physics, computer science and statistics to discuss principled frameworks for assessing the reliability and scientific validity of modern machine learning methods.

## Author contributions

OA and ML collaborated to draft Sections 1, 2, 5 and 6.
ML led the drafting of Section 3 and OA led Section 5.
MK provided guidance and advising.

## Funding information

This report is available under Fermilab open technical publications as FERMILAB-PUB-26-0009-CMS-PPD. O.A. is supported by Fermi Forward Discovery Group, LLC under Contract No. 89243024CSC000002 with the U.S. Department of Energy, Office of Science, Office of High Energy Physics. M.L. acknowledges the financial support of the European Research Council (grant SLING 819789).

## References
- [1]J. Neyman and E. S. Pearson,On the Problem of the Most Efficient Tests of Statistical
Hypotheses,Phil. Trans. Roy. Soc. Lond. A231(694-706), 289 (1933),10.1098/rsta.1933.0009.
- [2]G. Choudalakis,On hypothesis testing, trials factor, hypertests and the
BumpHunter,InPHYSTAT 2011(2011),1101.0390.
- [3]V. Khachatryanet al.,Observation of the Diphoton Decay of the Higgs Boson and
Measurement of Its Properties,Eur. Phys. J. C74(10), 3076 (2014),10.1140/epjc/s10052-014-3076-z,1407.0558.
- [4]G. Aadet al.,Measurement of Higgs boson production in the diphoton decay
channel in pp collisions at center-of-mass energies of 7 and 8 TeV with the
ATLAS detector,Phys. Rev. D90(11), 112015 (2014),10.1103/PhysRevD.90.112015,1408.7084.
- [5]A. M. Sirunyanet al.,Search for high mass dijet resonances with a new background
prediction method in proton-proton collisions ats=\sqrt{s}=13 TeV,JHEP05, 033 (2020),10.1007/JHEP05(2020)033,1911.03947.
- [6]G. Aadet al.,Search for new resonances in mass distributions of jet pairs
using 139 fb-1ofp​pppcollisions ats=13\sqrt{s}=13TeV with the ATLAS
detector,JHEP03, 145 (2020),10.1007/JHEP03(2020)145,1910.08447.
- [7]B. Abbottet al.,Search for new physics in eX data at DØ
using SLEUTH: A quasi-model-independent search strategy for new physics,Phys. Rev. D62, 092004 (2000),10.1103/PhysRevD.62.092004,hep-ex/0006011.
- [8]A. Aktaset al.,A General search for new phenomena in ep scattering at HERA,Phys. Lett. B602, 14 (2004),10.1016/j.physletb.2004.09.057,hep-ex/0408044.
- [9]F. D. Aaronet al.,A General Search for New Phenomena at HERA,Phys. Lett. B674, 257 (2009),10.1016/j.physletb.2009.03.034,0901.0507.
- [10]T. Aaltonenet al.,Model-Independent and Quasi-Model-Independent Search for New
Physics at CDF,Phys. Rev. D78, 012002 (2008),10.1103/PhysRevD.78.012002,0712.1311.
- [11]T. Aaltonenet al.,Model-Independent Global Search for New High-p(T) Physics at
CDF(2007),10.2172/922303,0712.2534.
- [12]T. Aaltonenet al.,Global Search for New Physics with 2.0 fb-1at CDF,Phys. Rev. D79, 011101 (2009),10.1103/PhysRevD.79.011101,0809.3781.
- [13]M. Aaboudet al.,A strategy for a general search for new phenomena using
data-derived signal regions and its application within the ATLAS
experiment,Eur. Phys. J. C79(2), 120 (2019),10.1140/epjc/s10052-019-6540-y,1807.07447.
- [14]A. M. Sirunyanet al.,MUSiC: a model-unspecific search for new physics in
proton–proton collisions ats=13​TeV\sqrt{s}=13\,\text{TeV},Eur. Phys. J. C81(7), 629 (2021),10.1140/epjc/s10052-021-09236-z,2010.02984.
- [15]G. Kasieczkaet al.,The LHC Olympics 2020 a community challenge for anomaly
detection in high energy physics,Rept. Prog. Phys.84(12), 124201 (2021),10.1088/1361-6633/ac36b9,2101.08320.
- [16]T. Aarrestadet al.,The Dark Machines Anomaly Score Challenge: Benchmark Data and
Model Independent Event Classification for the Large Hadron Collider,SciPost Phys.12(1), 043 (2022),10.21468/SciPostPhys.12.1.043,2105.14027.
- [17]G. Aadet al.,Dijet resonance search with weak supervision usings=13\sqrt{s}=13TeVp​pppcollisions in the ATLAS detector,Phys. Rev. Lett.125(13), 131801 (2020),10.1103/PhysRevLett.125.131801,2005.02983.
- [18]G. Aadet al.,Search for New Phenomena in Two-Body Invariant Mass
Distributions Using Unsupervised Machine Learning for Anomaly Detection at
s=13  TeV with the ATLAS Detector,Phys. Rev. Lett.132(8), 081801 (2024),10.1103/PhysRevLett.132.081801,2307.01612.
- [19]G. Aadet al.,Anomaly detection search for new resonances decaying into a
Higgs boson and a generic new particleXXin hadronic final states usings=13\sqrt{s}=13TeVp​pppcollisions with the ATLAS detector,Phys. Rev. D108, 052009 (2023),10.1103/PhysRevD.108.052009,2306.03637.
- [20]G. Aadet al.,Weakly supervised anomaly detection for resonant new physics
in the dijet final state using proton-proton collisions at s=13  TeV
with the ATLAS detector,Phys. Rev. D112(7), 072009 (2025),10.1103/2yq5-vj59,2502.09770.
- [21]G. Aadet al.,Search for new physics in final states with semivisible jets
or anomalous signatures using the ATLAS detector,Phys. Rev. D112(1), 012021 (2025),10.1103/44zp-mh1q,2505.01634.
- [22]G. Aadet al.,Search for Beyond the Standard Model physics with anomaly
detection in multilepton final states inp​pppcollisions ats=13\sqrt{s}=13TeV
with the ATLAS detector(2025),2508.19778.
- [23]V. Chekhovskyet al.,Model-agnostic search for dijet resonances with anomalous jet
substructure in proton–proton collisions ats\sqrt{s}= 13
TeV,Rept. Prog. Phys.88(6), 067802 (2025),10.1088/1361-6633/add762,2412.03747.
- [24]A. Hayrapetyanet al.,Machine-learning techniques for model-independent searches in
dijet final states(2025),10.5281/zenodo.16656501,2512.20395.
- [25]C. Collaboration,Search for resonances decaying to a Higgs boson in the bb
final state and an anomalous jet,CMS-PAS-B2G-24-015 (2025).
- [26]T. Hastie,The elements of statistical learning: data mining, inference,
and prediction(2009).
- [27]J. Carzon, A. Ghosh, R. Izbicki, A. Lee, L. Masserano and D. Whiteson,On Focusing Statistical Power for Searches and Measurements in
Particle Physics(2025),2507.17831.
- [28]A. Janssen,Global power functions of goodness of fit tests,Annals of Statistics pp. 239–253 (2000).
- [29]L. Wasserman,All of statistics: a concise course in statistical inference,Springer Science & Business Media (2013).
- [30]J. Friedman,On multivariate goodness-of-fit and two-sample testing,Statistical Problems in Particle Physics, Astrophysics, and Cosmology
p. 311 (2003).
- [31]D. Lopez-Paz and M. Oquab,Revisiting classifier two-sample tests,InInternational Conference on Learning Representations(2017).
- [32]R. T. D’Agnolo and A. Wulzer,Learning New Physics from a Machine,Phys. Rev. D99(1), 015014 (2019),10.1103/PhysRevD.99.015014,1806.02350.
- [33]R. T. D’Agnolo, G. Grosso, M. Pierini, A. Wulzer and M. Zanetti,Learning multivariate new physics,Eur. Phys. J. C81(1), 89 (2021),10.1140/epjc/s10052-021-08853-y,1912.12155.
- [34]I. Kim, A. Ramdas, A. Singh and L. Wasserman,Classification accuracy as a proxy for two-sample testing,The Annals of Statistics49(1), 411 (2021).
- [35]M. Letizia, G. Losapio, M. Rando, G. Grosso, A. Wulzer, M. Pierini, M. Zanetti
and L. Rosasco,Learning new physics efficiently with nonparametric methods,Eur. Phys. J. C82(10), 879 (2022),10.1140/epjc/s10052-022-10830-y,2204.02317.
- [36]P. Chakravarti, M. Kuusela, J. Lei and L. Wasserman,Model-independent detection of new physics signals using
interpretable semisupervised classifier tests,The Annals of Applied Statistics17(4), 2759 (2023).
- [37]G. Grosso, M. Letizia, M. Pierini and A. Wulzer,Goodness of fit by Neyman-Pearson testing,SciPost Phys.16, 123 (2024),10.21468/SciPostPhys.16.5.123,2305.14137.
- [38]S. Grossi, M. Letizia and R. Torre,Comparing Generative Models with the New Physics Learning
Machine(2025),2508.02275.
- [39]A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Schölkopf and A. Smola,A kernel two-sample test,Journal of Machine Learning Research13(25), 723 (2012).
- [40]A. Chatalic, M. Letizia, N. Schreuder and L. Rosasco,An efficient permutation-based kernel two-sample test,arXiv preprint arXiv:2502.13570 (2025).
- [41]A. Ramdas, N. García Trillos and M. Cuturi,On wasserstein two-sample testing and related families of
nonparametric tests,Entropy19(2), 47 (2017).
- [42]S. Grossi, M. Letizia and R. Torre,Refereeing the referees: evaluating two-sample tests for
validating generators in precision sciences,Mach. Learn. Sci. Tech.6(1), 015052 (2025),10.1088/2632-2153/adb3ee,2409.16336.
- [43]B. T. Tran and N. Schreuder,Minimax-optimal two-sample test with sliced wasserstein,arXiv preprint arXiv:2510.27498 (2025).
- [44]F. Biggs, A. Schrab and A. Gretton,Mmd-fuse: Learning and combining kernels for two-sample testing
without data splitting,Advances in Neural Information Processing Systems36, 75151
(2023).
- [45]A. Schrab, I. Kim, M. Albert, B. Laurent, B. Guedj and A. Gretton,Mmd aggregated two-sample test,Journal of Machine Learning Research24(194), 1 (2023).
- [46]G. Grosso and M. Letizia,Multiple testing for signal-agnostic searches for new physics
with machine learning,Eur. Phys. J. C85(1), 4 (2025),10.1140/epjc/s10052-024-13722-5,2408.12296.
- [47]C. G. Lester and R. Tombs,Using unsupervised learning to detect broken symmetries, with
relevance to searches for parity violation in nature. (Previously: ”Stressed
GANs snag desserts”)(2021),2111.00616.
- [48]R. Tombs and C. G. Lester,A method to challenge symmetries in data with self-supervised
learning,JINST17(08), P08024 (2022),10.1088/1748-0221/17/08/P08024,2111.05442.
- [49]P. L. Taylor, M. Craigie and Y.-S. Ting,Unsupervised searches for cosmological parity violation: An
investigation with convolutional neural networks,Phys. Rev. D109(8), 083518 (2024),10.1103/PhysRevD.109.083518,2312.09287.
- [50]M. Craigie, P. L. Taylor, Y.-S. Ting, C. Cuesta-Lazaro, R. Ruggeri and T. M.
Davis,Unsupervised Searches for Cosmological Parity Violation:
Improving Detection Power with the Neural Field Scattering Transform(2024),2405.13083.
- [51]S. E. Park, D. Rankin, S.-M. Udrescu, M. Yunus and P. Harris,Quasi Anomalous Knowledge: Searching for new physics with
embedded knowledge,JHEP21, 030 (2020),10.1007/JHEP06(2021)030,2011.03550.
- [52]C. L. Cheng, G. Singh and B. Nachman,Incorporating Physical Priors into Weakly Supervised Anomaly
Detection,Phys. Rev. Lett.135(2), 021801 (2025),10.1103/8259-wt5p,2405.08889.
- [53]T. Heimel, G. Kasieczka, T. Plehn and J. M. Thompson,QCD or What?,SciPost Phys.6(3), 030 (2019),10.21468/SciPostPhys.6.3.030,1808.08979.
- [54]M. Farina, Y. Nakai and D. Shih,Searching for New Physics with Deep Autoencoders,Phys. Rev. D101(7), 075021 (2020),10.1103/PhysRevD.101.075021,1808.08992.
- [55]D. P. Kingma and M. Welling,Auto-encoding variational Bayes,InProc. 2nd Int. Conf. on Learning Representations(2014),1312.6114.
- [56]O. Cerri, T. Q. Nguyen, M. Pierini, M. Spiropulu and J.-R. Vlimant,Variational Autoencoders for New Physics Mining at the Large
Hadron Collider,JHEP05, 036 (2019),10.1007/JHEP05(2019)036,1811.10276.
- [57]D. J. Rezende and S. Mohamed,Variational inference with normalizing flows,in Proc. 32nd Int. Conf. on Machine Learning - vol. 37 (2016),10.5555/3045118.3045281,1505.05770.
- [58]Y. Lipman, M. Havasi, P. Holderrieth, N. Shaul, M. Le, B. Karrer, R. T. Q.
Chen, D. Lopez-Paz, H. Ben-Hamu and I. Gat,Flow matching guide and code(2024),2412.06264.
- [59]V. Mikuni and B. Nachman,High-dimensional and permutation invariant anomaly
detection,SciPost Phys.16(3), 062 (2024),10.21468/SciPostPhys.16.3.062,2306.03933.
- [60]F. Vaselli, M. Pierini, M. M. Glowacki, T. Aarrestad, K. Govorkova, V. Loncar,
D. Danopoulos and F. Pantaleo,It’s not a FAD: first results in using Flows for unsupervised
Anomaly Detection at 40 MHz at the Large Hadron Collider,InML4Jets 2025,10.48550/arXiv.2508.11594(2025),2508.11594.
- [61]G. Kasieczka, R. Mastandrea, V. Mikuni, B. Nachman, M. Pettee and D. Shih,Anomaly Detection under Coordinate Transformations,Phys.Rev.D107, 015009 (2022),10.1103/PhysRevD.107.015009,2209.06225.
- [62]Y. L. Li, D. Lu, P. Kirichenko, S. Qiu, T. G. J. Rudner, C. B. Bruss and A. G.
Wilson,Out-of-distribution detection methods answer the wrong
questions(2025),2507.01831.
- [63]P. Kirichenko, P. Izmailov and A. G. Wilson,Why normalizing flows fail to detect out-of-distribution data,NIPS ’20. Curran Associates Inc.,ISBN 9781713829546 (2020).
- [64]J. Serrà, D. Álvarez, V. Gómez, O. Slizovskaia, J. F. Núñez and J. Luque,Input complexity and out-of-distribution detection with
likelihood-based generative models(2020),1909.11480.
- [65]T. Buss, B. M. Dillon, T. Finke, M. Krämer, A. Morandini, A. Mück,
I. Oleksiyuk and T. Plehn,What’s Anomalous in LHC Jets?,SciPost Phys.15, 168 (2022),10.21468/SciPostPhys.15.4.168,2202.00686.
- [66]B. M. Dillon, L. Favaro, T. Plehn, P. Sorrenson and M. Krämer,A Normalized Autoencoder for LHC Triggers,SciPost Phys.Core6, 074 (2022),10.21468/SciPostPhysCore.6.4.074,2206.14225.
- [67]A. Hayrapetyanet al.,Wasserstein normalized autoencoder for anomaly detection(2025),2510.02168.
- [68]E. M. Metodiev, B. Nachman and J. Thaler,Classification without labels: Learning from mixed samples in
high energy physics,JHEP10, 174 (2017),10.1007/JHEP10(2017)174,1708.02949.
- [69]J. H. Collins, K. Howe and B. Nachman,Anomaly Detection for Resonant New Physics with Machine
Learning,Phys. Rev. Lett.121(24), 241803 (2018),10.1103/PhysRevLett.121.241803,1805.02664.
- [70]J. H. Collins, K. Howe and B. Nachman,Extending the search for new resonances with machine
learning,Phys. Rev.D99(1), 014038 (2019),10.1103/PhysRevD.99.014038,1902.02634.
- [71]O. Amram and C. M. Suarez,Tag N’ Train: a technique to train improved
classifiers on unlabeled data,JHEP01, 153 (2021),10.1007/JHEP01(2021)153,2002.12376.
- [72]B. Nachman and D. Shih,Anomaly Detection with Density Estimation,Phys. Rev. D101, 075042 (2020),10.1103/PhysRevD.101.075042,2001.04990.
- [73]A. Hallin, J. Isaacson, G. Kasieczka, C. Krause, B. Nachman, T. Quadfasel,
M. Schlaffer, D. Shih and M. Sommerhalder,Classifying Anomalies THrough Outer Density Estimation
(CATHODE),Phys.Rev.D106, 055006 (2021),10.1103/PhysRevD.106.055006,2109.00546.
- [74]A. Hallin, G. Kasieczka, T. Quadfasel, D. Shih and M. Sommerhalder,Resonant anomaly detection without background sculpting,Phys.Rev.D107, 114012 (2022),10.1103/PhysRevD.107.114012,2210.14924.
- [75]G. Stein, U. Seljak and B. Dai,Unsupervised in-distribution anomaly detection of new physics
through conditional density estimation,In34th Conference on Neural Information Processing Systems(2020),2012.11638.
- [76]A. Andreassen, B. Nachman and D. Shih,Simulation Assisted Likelihood-free Anomaly Detection,Phys. Rev. D101(9), 095004 (2020),10.1103/PhysRevD.101.095004,2001.05001.
- [77]K. Benkendorfer, L. L. Pottier and B. Nachman,Simulation-assisted decorrelation for resonant anomaly
detection,Phys. Rev. D104(3), 035003 (2021),10.1103/PhysRevD.104.035003,2009.02205.
- [78]J. A. Raine, S. Klein, D. Sengupta and T. Golling,CURTAINs for your Sliding Window: Constructing Unobserved
Regions by Transforming Adjacent Intervals,Front.Big Data6, 899345 (2022),10.3389/fdata.2023.899345,2203.09470.
- [79]T. Golling, S. Klein, R. Mastandrea and B. Nachman,Flow-enhanced transportation for anomaly detection,Phys. Rev. D107(9), 096025 (2023),10.1103/PhysRevD.107.096025,2212.11285.
- [80]J. F. Kamenik and M. Szewc,Null hypothesis test for anomaly detection,Phys. Lett. B840, 137836 (2023),10.1016/j.physletb.2023.137836,2210.02226.
- [81]M. F. Chen, B. Nachman and F. Sala,Resonant anomaly detection with multiple reference datasets,JHEP07, 188 (2023),10.1007/JHEP07(2023)188,2212.10579.
- [82]D. Sengupta, S. Klein, J. A. Raine and T. Golling,CURTAINs flows for flows: Constructing unobserved regions with
maximum likelihood estimation,SciPost Phys.17(2), 046 (2024),10.21468/SciPostPhys.17.2.046,2305.04646.
- [83]T. Finke, M. Krämer, M. Lipp and A. Mück,Boosting mono-jet searches with model-agnostic machine
learning,JHEP08, 015 (2022),10.1007/JHEP08(2022)015,2204.11889.
- [84]G. Bickendorf, M. Drees, G. Kasieczka, C. Krause and D. Shih,Combining resonant and tail-based anomaly detection,Phys. Rev. D109(9), 096031 (2024),10.1103/PhysRevD.109.096031,2309.12918.
- [85]T. Golling, G. Kasieczka, C. Krause, R. Mastandrea, B. Nachman, J. A. Raine,
D. Sengupta, D. Shih and M. Sommerhalder,The interplay of machine learning-based resonant anomaly
detection methods,Eur. Phys. J. C84(3), 241 (2024),10.1140/epjc/s10052-024-12607-x,2307.11157.
- [86]E. Buhmann, C. Ewen, G. Kasieczka, V. Mikuni, B. Nachman and D. Shih,Full phase space resonant anomaly detection,Phys. Rev. D109(5), 055015 (2024),10.1103/PhysRevD.109.055015,2310.06897.
- [87]R. Das and D. Shih,Single interpolated generative model for anomalies,Phys. Rev. D112(7), 074040 (2025),10.1103/rj53-2x6j,2410.20537.
- [88]R. Das, G. Kasieczka and D. Shih,Residual ANODE(2023),2312.11629.
- [89]K. Bai, R. Mastandrea and B. Nachman,Non-resonant anomaly detection with background
extrapolation,JHEP04, 059 (2024),10.1007/JHEP04(2024)059,2311.12924.
- [90]G. Kasieczka, J. A. Raine, D. Shih and A. Upadhyay,Complete Optimal Non-Resonant Anomaly Detection(2024),2404.07258.
- [91]D. Shih, M. R. Buckley, L. Necib and J. Tamanas,Via Machinae: Searching for Stellar Streams using Unsupervised
Machine Learning,Mon.Not.Roy.Astron.Soc.509, 5992 (2021),10.1093/mnras/stab3372,2104.12789.
- [92]D. Shih, M. R. Buckley and L. Necib,Via machinae 2.0: Full-sky, model-agnostic search for stellar
streams in gaia dr2(2023),2303.01529.
- [93]M. Pettee, S. Thanvantri, B. Nachman, D. Shih, M. R. Buckley and J. H. Collins,Weakly-supervised anomaly detection in the milky way(2023),2305.03761.
- [94]D. Sengupta, S. Mulligan, D. Shih, J. A. Raine and T. Golling,skycurtains: model-agnostic search for stellar streams with
Gaia data,Mon. Not. Roy. Astron. Soc.536(2), 1104 (2024),10.1093/mnras/stae2570,2405.12131.
- [95]P. Shyamsundar, N. Smith and M. Szewc,Unaccounted-for look-elsewhere effect in k-fold cross adaptive
anomaly searches(2025).
- [96]M. Hein, B. Nachman and D. Shih,Look everywhere effects in anomaly detection(2025),2512.13787.
- [97]S. Baker and R. D. Cousins,Clarification of the Use of Chi Square and Likelihood
Functions in Fits to Histograms,Nucl. Instrum. Meth.221, 437 (1984),10.1016/0167-5087(84)90016-4.
- [98]R. T. d’Agnolo, G. Grosso, M. Pierini, A. Wulzer and M. Zanetti,Learning new physics from an imperfect machine,Eur. Phys. J. C82(3), 275 (2022),10.1140/epjc/s10052-022-10226-y,2111.13633.
- [99]S. Navaset al.,Review of particle physics,Phys. Rev. D110(3), 030001 (2024),10.1103/PhysRevD.110.030001.
- [100]V. Belis, P. Odagiu and T. K. Aarrestad,Machine learning for anomaly detection in particle physics,Rev. Phys.12, 100091 (2024),10.1016/j.revip.2024.100091,2312.14190.
- [101]V. Chekhovskyet al.,Model-agnostic search for dijet resonances with anomalous jet
substructure in proton–proton collisions ats\sqrt{s}= 13
TeV,Rept. Prog. Phys.88(6), 067802 (2025),10.1088/1361-6633/add762,2412.03747.
- [102]G. Aadet al.,Dijet resonance search with weak supervision usings=13\sqrt{s}=13TeVp​pppcollisions in the ATLAS detector,Phys. Rev. Lett.125(13), 131801 (2020),10.1103/PhysRevLett.125.131801,2005.02983.
- [103]K. Metzger, L. Xu, M. Sodini, T. K. Arrestad, K. Govorkova, G. Grosso and
P. Harris,Anomaly-preserving contrastive neural embeddings for
end-to-end model-independent searches at the LHC,Phys. Rev. D112(7), 072011 (2025),10.1103/5n77-ynsp,2502.15926.
- [104]G. Grosso, N. Lai, M. Letizia, J. Pazzini, M. Rando, L. Rosasco, A. Wulzer and
M. Zanetti,Fast kernel methods for data quality monitoring as a
goodness-of-fit test,Mach. Learn. Sci. Tech.4(3), 035029 (2023),10.1088/2632-2153/acebb7,2303.05413.
- [105]P. Cappelli, G. Grosso, M. Letizia, H. Reyes-González and M. Zanetti,Learning to Validate Generative Models: a Goodness-of-Fit
Approach(2025),2511.09118.
- [106]O. Knapp, O. Cerri, G. Dissertori, T. Q. Nguyen, M. Pierini and J.-R. Vlimant,Adversarially Learned Anomaly Detection on CMS Open Data:
re-discovering the top quark,Eur. Phys. J. Plus136(2), 236 (2021),10.1140/epjp/s13360-021-01109-4,2005.01598.
- [107]R. Gambhir, R. Mastandrea, B. Nachman and J. Thaler,Isolating Unisolated Upsilons with Anomaly Detection in CMS
Open Data,Phys. Rev. Lett.135(2), 021902 (2025),10.1103/vvv3-5kkl,2502.14036.
- [108]A. Altmann, L. Toloşi, O. Sander and T. Lengauer,Permutation importance: a corrected feature importance
measure,Bioinformatics26(10), 1340 (2010),10.1093/bioinformatics/btq134.
- [109]A. Hayrapetyanet al.,Search for resonances decaying to an anomalous jet and a Higgs
boson in proton-proton collisions ats\sqrt{s}= 13 TeV(2025),2509.13635.
- [110]J. de Favereau, C. Delaere, P. Demin, A. Giammanco, V. Lemaître,
A. Mertens and M. Selvaggi,DELPHES 3, A modular framework for fast simulation of a
generic collider experiment,JHEP02, 057 (2014),10.1007/JHEP02(2014)057,1307.6346.
- [111]S. Bieringer, G. Kasieczka, J. Kieseler and M. Trabs,Classifier surrogates: sharing AI-based searches with the
world,Eur. Phys. J. C84(9), 972 (2024),10.1140/epjc/s10052-024-13353-w,2402.15558.
- [112]S. V. Chekanov, W. Islam, R. Zhang and N. Luongo,ADFilter—A Web Tool for New Physics Searches with
Autoencoder-Based Anomaly Detection Using Deep Unsupervised Neural
Networks,Information16(4), 258 (2025),10.3390/info16040258,2409.03065.
- [113]B. Nachman and D. Noll,FlexCAST: Enabling Flexible Scientific Data Analyses(2025),2507.11528.
- [114]A. Janssen and H. Ünlü,Regions of alternatives with high and low power for
goodness-of-fit tests,Journal of statistical planning and inference138(8), 2526
(2008).

## 


- 


Major funding support from
