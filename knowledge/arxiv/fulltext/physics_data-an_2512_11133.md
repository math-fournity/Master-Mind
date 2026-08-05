# Machine Learning

**arXiv ID**: 2512.11133v1
**Authors**: Javier M. Duarte, Uros Seljak, Kazu Terao
**Published**: 2025-12-11
**Categories**: physics.data-an, hep-ex, hep-ph, hep-th
**Comments**: Particle Data Group Review of Machine Learning, 2025 update, also available at https://pdg.lbl.gov/2025/reviews/rpp2025-rev-machine-learning.pdf
**HTML URL**: https://arxiv.org/html/2512.11133v1

## Abstract

This chapter gives an overview of the core concepts of machine learning (ML) -- the use of algorithms that learn from data, identify patterns, and make predictions or decisions without being explicitly programmed -- that are relevant to particle physics with some examples of applications to the energy, intensity, cosmic, and accelerator frontiers.

## Full Text

Contents

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
- License: CC BY 4.0arXiv:2512.11133v1 [physics.data-an] 11 Dec 2025\reviewtitle

Machine Learning\reviewauthorJ.M. Duarte (UC San Diego), U. Seljak (UC Berkeley; LBNL) and K. Terao (SLAC; Stanford U.)\reviewlabelml\ischaptertrue\externaldocumentcrossref\pdgtitle\written

August 2025

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

This chapter gives an overview of the core concepts of machine learning (ML)—the use of algorithms that learn from data, identify patterns, and make predictions or decisions without being explicitly programmed—that are relevant to particle physics with some examples of applications to the energy, intensity, cosmic, and accelerator frontiers.
ML is an enormous field that has grown substantially in the last decade, largely driven by the emergence of so-called deep learning (DL)[2015Natur.521..436L,schmidhuber2015deep].
ML has a long history in particle physics going back to the late 1980s and early 1990s; see Refs.[Radovic:2018dip,Guest:2018yhq,Carleo:2019ptp]for recent reviews.
ML is a subset of artificial intelligence (AI), which generally refers to computational systems that can perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.

Physicists are exploring and contributing to machine learning at an unprecedented rate, which poses a challenge for those who wish to have an up-to-date view of the field.
This motivated an effort to createA Living Review of Machine Learning for Particle and Nuclear Physics[Feickert:2021ajf], which can be accessed here:https://iml-wg.github.io/HEPML-LivingReview/.
At the time of writing, the Living Review included more than 1,800 references organized hierarchically by topic.
Although we make references to some of these papers, this chapter focuses on the methodology and does not attempt to give a comprehensive review of the applications.

Machine learning and artificial intelligence have a mathematical foundation that is closely tied to statistics (see Ch.\crossrefstat), the calculus of variations, approximation theory, and optimal control theory.
Nevertheless, there have been tremendous advances in recent years, driven by increased computational power, enormous datasets, and new insights, that are impacting physics and society.

The topic can be organized along a few axes, which we use to structure this section.
First, there are different learning paradigms, for example, supervised learning, unsupervised learning, and reinforcement learning.
Within these paradigms, there are various tasks; for example, classification and regression—which have been the primary use of ML in particle physics—are examples of supervised learning.
In addition to the learning paradigm and tasks, there are various types of machine learning models that generically process some input and produce some output.
The types of models vary based on what they are modeling (\eg, so-called discriminative vs. generative models), as well as how they are implemented (\eg, neural networks, decision trees, or kernel machines).
Next, there are the issues around training or learning within the context of a given task and model class, which connects to optimization and regularization.
We will briefly discuss the various considerations that emerge in the application of machine learning methods to physics, such as the treatment of systematic uncertainty, the interpretability of the models, and the incorporation of symmetry.

## 1.1A gentle introduction with a representative example

We will use a specific, familiar example to introduce the various ingredients in context before factorizing and abstracting them.
Consider the task ofclassifyingenergy deposits in a particle detector as coming from electrons or protons.
For this example, let the detector data consist of energy deposits inddsensors so that the data can be represented as afeature vectorx∈ℝdx\in\mathbb{R}^{d}.
Different components ofxxmay correspond to physical quantities with different units (\eg, units of energy, momentum, or position).

Due to the complex interactions of particles in the detector, we do not have an explicit probability model for the high-dimensional data for the electron and proton scenarios, but we do have a simulator that allows us to generate Monte Carlo samples for each.
This allows us to assemble atraining dataset{xi,yi}i=1,…,n\{x_{i},y_{i}\}_{i=1,\dots,n}, whereyyis alabelthat identifies how the example was generated (\eg,y=0y=0for electrons andy=1y=1for protons).
We would like to find a function that accuratelypredictsthe label on new data.
Because we have feature-label pairs, this is asupervised learningproblem.
We can use aneural networkto provide a flexible family of functionsfϕ:ℝd→ℝf_{\phi}:\mathbb{R}^{d}\to\mathbb{R}, whereϕ\phidenotes the internal parameters of the neural network (\ie, the weights and biases that we will discuss in Sec.8.4).
The goal oftrainingis to find the value of the parametersϕ\phithat provide the ‘best’ predictions.
This is made concrete through aloss functionℒ​(y,fϕ​(x))\mathcal{L}(y,f_{\phi}(x)).
Instead of the obvious zero-one loss, which is 0 iffϕ​(x)=yf_{\phi}(x)=yand 1 if not, we use the squared-lossℒsq​(y,fϕ​(x))=(y−fϕ​(x))2\mathcal{L}_{\rm sq}(y,f_{\phi}(x))=(y-f_{\phi}(x))^{2}, which will be motivated in Sec.2.3.
We can evaluate the average of the loss on the training set of sizenn, known as theempirical riskortraining lossℛemp​(fϕ)=∑i=1nℒ​(yi,fϕ​(xi))/n\mathcal{R}_{\textrm{emp}}(f_{\phi})=\sum_{i=1}^{n}\mathcal{L}(y_{i},f_{\phi}(x_{i}))/n.Trainingrefers to numerically minimizing the empirical risk.
We can numerically optimize the model throughgradient descent, which iteratively adjusts the parameters of the network according toϕt+1=ϕt−λ​∇ϕℛemp​(fϕ)\phi^{t+1}=\phi^{t}-\lambda\nabla_{\phi}\mathcal{R}_{\textrm{emp}}(f_{\phi}), whereλ\lambdais thelearning rate.

Once the optimization is complete and we obtain the solutionϕ^\hat{\phi}, it is natural to assess the quality of the trained modelfϕ^f_{\hat{\phi}}on an independenttesting dataset111It is important to never use the testing dataset to make decisions about the model.
For this purpose, another independent dataset, usually called thevalidation dataset, should be used (see Sec.2.4)..
The empirical risk evaluated on the testing set is often larger than on the training set, and large differences indicateoverfitting, meaning that the model does not generalize well to the unseen data.
The ability to accurately predict on unseen data is referred to asgeneralizationand the empirical risk on the test data provides a measure of thegeneralization error.
In order to reduce the generalization error one might explore different model choices (\eg, neural network architectures), additional regularization terms in the loss function, different learning rates, optimization algorithms, or early stopping criterion in the optimization.

In order to produce a binary electron vs. proton decision from the continuous output of the neural network, one typically chooses a threshold (\ie, classify as proton iffϕ^​(x)>cf_{\hat{\phi}}(x)>c).
The choice of the thresholdccis often referred to as a working point and it sets the tradeoff between electron and proton efficiencies, fake rates, and purities.
Areceiver operating characteristic curve, or ROC curve, is used to summarize the tradeoff between true positive rate (TPR) and false positive rate (FPR).
Importantly, the characterization of the efficiency and rejection power (or equivalently the ROC curve) requires labeled data.
In a particle physics context, it is recognized that the simulation is not perfect and the mismodeling is associated to the presence of systematic uncertainty.
The discrepancy between the distribution of the training dataset and the distribution of the data where the model will be applied is referred to asdomain shiftordistribution shift.
While mismodeling in the training dataset might lead to a suboptimal classifier, the real source of systematic uncertainty comes from the mismatch between the data used to characterize the performance of the classifier and the unlabeled data that the classifier is applied to.
This motivates the use of data-driven methods to calibrate the resulting model.

This example provides a vertical slice through the various aspects of supervised machine learning in particle physics.
Now we factorize and abstract the various ingredients in order to provide a more general treatment with a broader scope.

## 2Supervised learning

Supervised learning generally refers to the class of problems where the training dataset are presented as input-output pairs{(xi,yi)}i=1,…,n\{(x_{i},y_{i})\}_{i=1,\dots,n}, wherexi∈𝒳x_{i}\in\mathcal{X}are the input features andyi∈𝒴y_{i}\in\mathcal{Y}are the corresponding target labels.
Furthermore, it is typically the case thatxix_{i}andyiy_{i}are independent and identically distributed (i.i.d.) according to the data distributionp​(x,y)p(x,y),(xi,yi)​∼i.i.d.​p​(x,y)(x_{i},y_{i})\overset{\text{i.i.d.}}{\sim}p(x,y), thoughp​(x,y)p(x,y)is usually not known explicitly.

The goal of supervised learning is find a functionf:𝒳→Yf:\mathcal{X}\to{Y}that ‘best’ captures the relationship between the input features and the corresponding target labels, similar to parameter estimation described in Sec.\crossrefstat:sec:paramest of the Statistics chapter.
Section2.1discusses how we quantify which function is best.

## 2.1Loss, risk, empirical risk

The termlearningin machine learning generally refers to optimization of some objective, which can be thought of as minimizingrisk.
The risk brings together three main ingredients.
The first is themodel familyℱ\mathcal{F}(wheref∈ℱf\in\mathcal{F}is the quantity that we vary during optimization), the second is theloss functionℒ\mathcal{L}, and the third is a data distributionp​(x,y)p(x,y).
Theriskfor a modelf∈ℱf\in\mathcal{F}is defined as its expected lossℛ​[f]≔𝔼p​(x,y)​[ℒ​(y,f​(x))]≡∫ℒ​(y,f​(x))​p​(x,y)​d​x​d​y,\mathcal{R}[f]\coloneqq\mathbb{E}_{p(x,y)}[\mathcal{L}(y,f(x))]\equiv\int\mathcal{L}(y,f(x))\,p(x,y)\mathop{}\!\mathrm{d}x\mathop{}\!\mathrm{d}y\;,(1)

where𝔼p​[⋅]\mathbb{E}_{p}[\cdot]refers to the expectation with respect to the distributionpp.
Written this way, the risk is a functional, and the idealized goal for machine learning is to solve the optimization problemf∗=arg​minf∈ℱ⁡ℛ​[f],f^{*}=\operatorname*{arg\,min}_{{f\in{\mathcal{F}}}}\mathcal{R}[f]\;,(2)

whereℱ\mathcal{F}would include all possible functions.

One of the defining characteristics of machine learning in practice is that one does not know the data distributionp​(x,y)p(x,y), but does have access to samples from that distribution,\ie{xi,yi}i=1,…,n\{x_{i},y_{i}\}_{i=1,\dots,n}with(xi,yi)​∼i.i.d.​p​(x,y)(x_{i},y_{i})\overset{\text{i.i.d.}}{\sim}p(x,y).
This leads to the correspondingempirical riskℛemp​[f]≔𝔼p^​(x,y)​[ℒ​(y,f​(x))]≡1n​∑i=1nℒ​(yi,f​(xi)),\mathcal{R}_{\textrm{emp}}[f]\coloneqq\mathbb{E}_{\hat{p}(x,y)}[\mathcal{L}(y,f(x))]\equiv\frac{1}{n}\sum_{i=1}^{n}\mathcal{L}(y_{i},f(x_{i}))\;,(3)

wherep^​(x,y)=1n​∑i=1nδ​(x−xi)​δ​(y−yi)\hat{p}(x,y)=\frac{1}{n}\sum_{i=1}^{n}\delta(x-x_{i})\delta(y-y_{i})is referred to as the empirical distribution of the dataset{(xi,yi)}i=1,…,n\{(x_{i},y_{i})\}_{i=1,\dots,n}.
Theempirical risk minimizationprinciple is a core idea in statistical learning theory[vapnik2013nature], which approximatesf∗f^{*}with its empirical analoguef^=arg​minf∈ℱ^⁡ℛemp​[f],\hat{f}=\operatorname*{arg\,min}_{{f\in{\hat{\mathcal{F}}}}}\mathcal{R}_{\textrm{emp}}[f]\;,(4)

whereℱ^\hat{\mathcal{F}}is the set of all possible functions
parametrized by the model parametersϕ\phi. In an idealized
infinite parameter limit machine learning functions,
such as neural networks, are often universal
approximators, meaning they cover all functions andℱ^=ℱ\hat{\mathcal{F}}=\mathcal{F}.
For finite size models, this may not be a valid approximation.
Expressivity of the network characterizes this universality property and is a function of the network architecture and its parameters such as
width and depth of neural network layers.
If the expressivity is too small
it leads to
underfitting.
However, an equally important consideration
is the risk of overfitting if we
optimize Eq.4for too
long or use an unrestricted model class (see Sec.2.5).

While the loss function may quantify some well-motivated notion of risk, it is also common to design loss functions so thatf∗f^{*}has some desired property.
In Secs.2.2–2.5, we will consider several such loss functions where one can show that the correspondingf∗f^{*}has the desired property even if the form of the loss is not obvious. Furthermore, there are often multiple loss functions that can lead to the samef∗f^{*}.
Thus, one can think of machine learning as solving Eq.4with a sufficiently flexible model, powerful optimization algorithms, and practical considerations to break the degeneracy between different loss functions that lead to the samef∗f^{*}.
As we shall see, commonly used loss functions can also be mathematically derived from a probabilistic approach.

## 2.2Regression

The goal of regression is to predict a labely∈𝒴y\in\mathcal{Y}given an input feature vectorx∈𝒳x\in\mathcal{X}.
Typically, the label is a real-valued scalar, but𝒳\mathcal{X}can beℝd\mathbb{R}^{d}or some more structured target (\eg, an image, sequence, graph, quantile, or distribution).
When𝒴\mathcal{Y}is discrete, the task is usually referred to as classification (see Sec.2.3); however, the two are closely related andlogistic regressionis an example where the model predicts a continuous probability associated to the possible label values.
In elementary statistical language, the target labelyyis often called a dependent variable, while the featurexxis called the independent variable. In classical statistics, one often assumes a model for the data such asyi=fϕ​(xi)+ei,y_{i}=f_{\phi}(x_{i})+e_{i}\;,(5)

whereeie_{i}is an additive error term that is often assumed to be independent ofxxand normally distributed.
This leads to classic approaches like least-squares (see Sec.\crossrefstat:sec:ls), and when the modelfϕf_{\phi}is linear inϕ\phi(not inxx!) linear regression, which has a closed-form solution.
However, we can relax these assumptions and consider the general case of an arbitrary joint distributionp​(x,y)p(x,y), which can be written asp​(y|x)​p​(x)p(y|x)p(x)without loss of generality (see Sec.\crossrefprob:sec:probGeneral).
Consider thesquared erroras a loss function, which corresponds to the mean-squared error (MSE) empirical risk:ℒMSE​(y,f​(x))=(y−f​(x))2.\mathcal{L}_{\textrm{MSE}}(y,f(x))=(y-f(x))^{2}\;.(6)

One might expect that the squared error would only be appropriate in the case that the conditional distributionp​(y|x)p(y|x)is normally distributed, but one can use the calculus of variations to show that in generalfMSE∗​(x)=𝔼p​(y|x)​[y],f^{*}_{\textrm{MSE}}(x)=\mathbb{E}_{p(y|x)}[y]\;,(7)

that is the optimal regressor for the MSE is the conditional expectation ofyygivenxx.

One issue with the squared-error as a loss function is that it is very sensitive to outliers.
Alternatively, one can use the absolute error|y−f​(x)||y-f(x)|as a loss function222The absolute error and squared error are often denoted as L1 and L2 errors, respectively, in reference to the corresponding norms..
However, the discontinuous derivative of the absolute (L1) error leads to challenges in optimization.
As a result there are various other loss functions, such as the Huber loss, that aim to be both robust and more amenable to optimization.

Note that this framing of regression yields a functionf​(x)f(x)that only provides a point estimate foryy. An alternative approach to regression is to model the full conditional distributionp​(y|x)p(y|x).
One such example is Gaussian process regression, which is discussed in Sec.8.2.
In that probabilistic approach, one can still obtain a point estimator, such as the conditional expectation or the maximum
a posteriori (MAP) estimatorf∗​(x)=arg​maxy⁡p​(y|x),f^{*}(x)=\operatorname*{arg\,max}_{y}p(y|x)\;,(8)

and one can also derive uncertainty estimates on the predicted valueyy(see Sec.10for more details).
In this setting, the prior distribution on the model family is closely related to the concept of regularization, which we touch on in Secs.2.5and8.2.

When one directly modelsp​(y|x)p(y|x), or goes further to model the joint distributionp​(x,y)=p​(y|x)​p​(x)p(x,y)=p(y|x)p(x), then one can use maximum likelihood for the loss function.
In that approach, the problem is really one of density estimation, which is a type of unsupervised learning that we discuss in Sec.3.3.
These two approaches are a classic examples of two different approaches to modeling.
Regression withfMSE∗​(x)f^{*}_{\textrm{MSE}}(x)is the prototypical example ofdiscriminativemodeling, while modeling the joint distribution is a prototypical example ofgenerativemodeling.
Generally, discriminative approaches with supervised learning outperform generative approaches when there is sufficient data, but generative approaches can be beneficial in data-starved settings[NgJ01].

## 2.3Classification

The goal of classification is to predict one of a finite number of class labelsy∈𝒴y\in\mathcal{Y}given an input feature vectorx∈𝕏x\in\mathbb{X}.
It is similar to regression in this way, but the focus is on discrete target space𝒴\mathcal{Y}.
An important special case is when the label can only take on one of two values (\eg, “signal” or “background”), which is referred to as binary classification and is equivalent to simple hypothesis testing in statistics.
It is common for a classifier to be the composition of two functions:f​(g​(x))f(g(x)).
The first functiong:𝒳→ℝ|𝒴|g:\mathcal{X}\to\mathbb{R}^{|\mathcal{Y}|}predicts continuous probabilities for each class (\ie,gc​(x)≈p​(y=c|x)g_{c}(x)\approx p(y=c|x)).
The second functionf:ℝ|𝒴|→𝒴f:\mathbb{R}^{|\mathcal{Y}|}\to\mathcal{Y}then chooses the discrete labely∈𝒴y\in\mathcal{Y}, such asf​(g​(x))=arg​maxc⁡gc​(x)≈arg​maxy⁡p​(y|x)f(g(x))=\operatorname*{arg\,max}_{c}g_{c}(x)\approx\operatorname*{arg\,max}_{y}p(y|x).
This is the case for both classical methods like logistic regression and modern, deep learning approaches to classification; therefore, we will use the term probabilistic classifier forg​(x)g(x)or just classifier when it is clear in context.

An intuitive loss function for classification is the zero-one loss, which simply counts the number of mis-classifications:ℒ0/1​(y,f​(x))={0,if​f​(x)=y1,otherwise.\mathcal{L}_{\textrm{0/1}}(y,f(x))=\begin{cases}0,&\text{if }f(x)=y\\
1,&\text{otherwise}\;.\end{cases}(9)

The zero-one loss can also be written asℒ0/1​(y,f​(x))=𝟏​(y≠f​(x))\mathcal{L}_{\textrm{0/1}}(y,f(x))=\mathbf{1}(y\neq f(x)), where𝟏​(⋅)\mathbf{1}(\cdot)is the indicator function.
The zero-one loss is non-differentiable, so it does not pair well with gradient-based optimization.

For binary classification, one can usey={0,1}y=\{0,1\}as numerical values for the class labels and thebinary cross-entropyloss functionℒbxe​(y,g​(x))=−[y​log⁡(g​(x))+(1−y)​log⁡(1−g​(x))].\mathcal{L}_{\textrm{bxe}}(y,g(x))=-\left[y\log(g(x))+(1-y)\log(1-g(x))\right]\,.(10)

The resulting model will approximatefbxe∗​(x)f^{*}_{\textrm{bxe}}(x), which takes on the formfbxe∗​(x)=𝔼p​(y|x)​[y]=p​(y=1|x)=p​(x|y=1)​p​(y=1)p​(x|y=0)​p​(y=0)+p​(x|y=1)​p​(y=1).f^{*}_{\textrm{bxe}}(x)=\mathbb{E}_{p(y|x)}[y]=p(y=1|x)=\frac{p(x|y=1)p(y=1)}{p(x|y=0)p(y=0)+p(x|y=1)p(y=1)}\;.(11)

That is the binary cross-entropy loss for binary classification leads to the Bayesian posterior probability that the labely=1y=1given the feature vectorxx(see Bayes theorem in Sec.\crossrefprob:sec:probGeneral).

Equation11highlights an important feature of supervised learning relevant for particle physics: the joint distributionp​(x,y)p(x,y)of the training dataset implies a prior distributionp​(y)p(y)on the labels or classes.
This prior distribution reflects the frequency in the training dataset, not necessarily in the real data.
When applying the resulting model to a different dataset with the same conditional distribution (data likelihood)p​(x|y)p(x|y)for the features and a different priorp′​(y)p^{\prime}(y)for the labels, the probabilistic interpretation of the result will not be properly calibrated, meaningg​(x)≉p​(y|x)g(x)\not\approx p(y|x).
A common choice for binary classification is to use a balanced training dataset withp​(y=0)=p​(y=1)=12p(y=0)=p(y=1)=\frac{1}{2}, while in many cases the truep′​(y=1)p^{\prime}(y=1)in the experimental data might be very small (\ie, low signal-to-background), unknown, or zero (\ie, a hypothetical particle that does not exist).

Ifp′​(y)p^{\prime}(y)andp​(y)p(y)are known then Bayes theorem can be used to re-calibrate the posteriorp​(y|x)p(y|x)from one prior to another.
One example of such re-calibration is the correspondence of binary classification to simple hypothesis tests in frequentist statistics discussed in Sec.\crossrefstat:sec:hyptest of the Statistics chapter.
In that setting, the Neyman-Pearson lemma states that the optimal classifier is given by the likelihood ratiofNP∗​(x)=p​(x|y=1)p​(x|y=0),f^{*}_{\textrm{NP}}(x)=\frac{p(x|y=1)}{p(x|y=0)}\;,(12)

which does not depend on the prior probabilitiesp′​(y=0)p^{\prime}(y=0)orp′​(y=1)p^{\prime}(y=1)as in Eq.11, or, equivalently, assumes equal priorsp′​(y=0)=p′​(y=1)p^{\prime}(y=0)=p^{\prime}(y=1).
Bayes theorem can be used to show that the two functions,fNP∗​(x)f^{*}_{\textrm{NP}}(x)andfbxe∗​(x)f^{*}_{\textrm{bxe}}(x), are related by a one-to-one, monotonic transformationfNP∗​(x)=p​(y=0)p​(y=1)​fbxe∗​(x)1−fbxe∗​(x),f^{*}_{\textrm{NP}}(x)=\frac{p(y=0)}{p(y=1)}\frac{f^{*}_{\textrm{bxe}}(x)}{1-f^{*}_{\textrm{bxe}}(x)}\;,(13)

which is referred to as thelikelihood-ratio trickand plays an important role in simulation-based inference (see Sec.6).

A standard way to evaluate the performance of a classifier is to evaluate the true positive rate (TPR)—the proportion ofy=1y=1samples that are correctly identified based on a fixed thresholdg​(x)>cg(x)>c—as a function of the false positive rate (FPR)—the proportion ofy=0y=0samples that are misidentified based on the same fixed threshold.
Plotting these values generates a graph known as the receiver operating characteristic (ROC) curve.
Importantly, the monotonic transformation of Eq.13does not impact the tradeoff between FPR and TPR, therefore the ROC curves forfNP∗​(x)f^{*}_{\textrm{NP}}(x)andfbxe∗​(x)f^{*}_{\textrm{bxe}}(x)are identical and do not depend on the prior probabilitiesp​(y)p(y).
This property has been leveraged inweakly supervisedapproaches[Metodiev:2017vrx]to train a classifier in data without access to labels as long as one has two datasets with differentp​(y=1)/p​(y=0)p(y=1)/p(y=0)ratios and the same conditional distributionp​(x|y)p(x|y)of the features given the labels.

A generalization of Eq.10that applies to multiple classes, is thecategorical cross-entropylossℒxe​(y,f​(x))=−∑c∈|𝒴|𝟏​(y=c)​log⁡(fc​(x)),\mathcal{L}_{\textrm{xe}}(y,f(x))=-\sum_{c\in|\mathcal{Y}|}\mathbf{1}(y=c)\log(f_{c}(x))\;,(14)

wheref:𝒳→ℝ|𝒴|f:\mathcal{X}\to\mathbb{R}^{|\mathcal{Y}|}and the indicator function picks out the term in the sum for the corresponding class labelyy.
This loss can be derived by maximizing the posterior of Eq.26using a discrete set of class labelsyy, which identifiesfc​(x)=f~​(y=c|x)=p​(y=c|x)f_{c}(x)=\tilde{f}(y=c|x)=p(y=c|x)and thus assumes the constraint∑cfc​(x)=1\sum_{c}f_{c}(x)=1andfc​(x)≥0f_{c}(x)\geq 0(see Sec.8.4.2for an activation function that enforces this).
The functionf~​(y|x)\tilde{f}(y|x)can be interpreted as a conditional distribution,\ie, an approximation to the true posteriorp​(y|x)p(y|x).
The risk associated to the cross entropy loss function isℛxe​[f]=𝔼p​(x,y)​[−∑c∈|𝒴|𝟏​(y=c)​log⁡fc​(x)]=−∑c∈|𝒴|p​(y=c)​𝔼p​(x|y)​[log⁡f~​(y=c|x)].\mathcal{R}_{\textrm{xe}}[f]=\mathbb{E}_{p(x,y)}\left[-\sum_{c\in|\mathcal{Y}|}\mathbf{1}(y=c)\log f_{c}(x)\right]=-\sum_{c\in|\mathcal{Y}|}p(y=c)\mathbb{E}_{p(x|y)}[\log\tilde{f}(y=c|x)]\;.(15)

This is equivalent toℛxe​[f]=𝔼p​(x)​[H​[p​(y|x),f~​(y|x)]]\mathcal{R}_{\textrm{xe}}[f]=\mathbb{E}_{p(x)}[H[p(y|x),\tilde{f}(y|x)]], whereH​[p,f]≡𝔼p​[−log⁡f]=−∫p​(x)​log⁡(f​(x))​d​xH[p,f]\equiv\mathbb{E}_{p}[-\log f]=-\int p(x)\log(f(x))\mathop{}\!\mathrm{d}x(16)

is the cross entropy between the two distributions.
One can use a Lagrange multiplier to enforce the normalization constraint and the calculus of variations to show thatfxe,c∗​(x)=p​(y=c|x),f^{*}_{\textrm{xe},c}(x)=p(y=c|x)\;,(17)

which is equivalent to the solution in Eq.11in the binary case.

This approach is closely related to the loss functions that are used for density estimation, the forward Kullback-Leibler (KL) divergence, and the maximum likelihood estimation.
Minimizing cross entropyH​[p,fϕ]H[p,f_{\phi}]toϕ\phiis equivalent to minimizing the forward KL divergenceKL(p∥fϕ)≔𝔼p[logp(x))−logfϕ]=H[p,fϕ]−H[p],\text{KL}(p\|f_{\phi})\coloneqq\mathbb{E}_{p}[\log p(x))-\log f_{\phi}]=H[p,f_{\phi}]-H[p]\;,(18)

whereH​[p]≔∫p​(x)​log⁡p​(x)​𝑑xH[p]\coloneqq\int p(x)\log p(x)dxis the entropy and independent offϕf_{\phi}.
The KL divergenceKL​[p∥f]≥0\text{KL}[p\|f]\geq 0, and equal if and only ifp=fp=f.

Unlike in the binary classification case, the multi-class classifier is sensitive to the priorsp​(y)p(y)used in training.
This leads to complications as often the class proportions are unknown.
For example, one might be interested in classifying a signal when multiple backgrounds are present and the relative proportion of those different background components is uncertain.
Ideally one would like the class proportions for the background components used in training to match those in the data, which presents an additional training challenge if those proportions are heavily unbalanced.

## 2.4Generalization and model complexity

With a sufficiently flexible model, it is possible to fit the training dataset very well, though the model might notgeneralizewell to unseen data, a phenomenon known asoverfitting.
More concretely, for a nonnegative loss function one might haveℛemp​[f^]→0\mathcal{R}_{\textrm{emp}}[\hat{f}]\to 0, while the true riskℛ​[f^]\mathcal{R}[\hat{f}]might be large.
Conversely,underfittingoccurs when a model is unable to capture the relationship between the inputs and labels accurately, resulting in large empirical and true risks.
While it is generally not possible to evaluateℛ​[f^]\mathcal{R}[\hat{f}]exactly because we do not knowp​(u)p(u), we can use an independent dataset (also called validation dataset) to obtain an unbiased estimate of it.
Thiscross-validationmethod motivates the test-train-validation split of the data.

Intuitively, a model with many parameters has more flexibility and is more prone to overfitting.
However, some highly over-parameterized models (that have large subspaces of their parameters whereℛemp​[fϕ^]→0\mathcal{R}_{\textrm{emp}}[\hat{f_{\phi}}]\to 0) generalize well[zhang2021understanding-2,nakkiran2019deep].
Often this is achieved throughregularization, both explicit and implicit (Sec.2.5).

Two main sources of error prevent models from generalizing beyond their training dataset.
One isbiasarising from erroneous assumptions in the model and the other isvariancearising from sensitivity to statistical fluctuations in the training dataset.
Thebias-variance decompositionis a way of analyzing a model’s expected risk as a sum of bias and variance terms.
Concretely, ifℒ\mathcal{L}is the squared loss, one can decompose the expected risk𝔼𝒟​[ℛemp​[f^ϕ]]\mathbb{E}_{\mathcal{D}}[\mathcal{R}_{\textrm{emp}}[\hat{f}_{\phi}]]over all possible training datasets𝒟\mathcal{D}into three terms[hastie01statisticallearning,Mostafa2012],𝔼𝒟​[ℛ​[f^ϕ𝒟]]\displaystyle\mathbb{E}_{\mathcal{D}}\left[\mathcal{R}[\hat{f}_{\phi}^{\mathcal{D}}]\right]=𝔼𝒟​𝔼p​(x,y)​[(y−f^ϕ𝒟​(x))2]\displaystyle=\mathbb{E}_{\mathcal{D}}\mathbb{E}_{p(x,y)}\left[(y-\hat{f}^{\mathcal{D}}_{\phi}(x))^{2}\right](19)=𝔼p​(x)​[𝔼p​(y|x)​[(y−y¯)2]⏟noise+𝔼𝒟​[(f^ϕ​(x)−f¯​(x))2]⏟variance+(y¯−f¯​(x))2⏟bias],\displaystyle=\mathbb{E}_{p(x)}\left[\underbrace{\mathbb{E}_{p(y|x)}\left[(y-\bar{y})^{2}\right]}_{\text{noise}}+\underbrace{\mathbb{E}_{\mathcal{D}}\left[(\hat{f}_{\phi}(x)-\bar{f}(x))^{2}\right]}_{\text{variance}}+\underbrace{(\bar{y}-\bar{f}(x))^{2}}_{\text{bias}}\right]\,,(20)

wheref¯​(x)≡𝔼𝒟​[f^ϕ𝒟​(x)]\bar{f}(x)\equiv\mathbb{E}_{\mathcal{D}}\left[\hat{f}_{\phi}^{\mathcal{D}}(x)\right]is the “average” prediction of the model over different possible training datasets.
In this expression, the first term is the inherent “noise” in the dataset,\ie, the variance ofyyaround its mean, which is zero ifyyis deterministically related toxx.
The second term is the variance of the model around its average when considering different training datasets, and the third term is the squared bias,\ie, the difference between the average prediction and the true conditional mean.

Classically, there is a correspondence between overfitting and underfitting and the concepts of bias and variance discussed in Sec.\crossrefstat:sec:paramest on parameter estimation.
Overfitting implies high variance: the model class is too complex and retraining yields vastly different models.
Variance tends to increase with model complexity and decrease with more training data.
Underfitting implies high bias: the model class is too simple and has a large error rate.
Thus, there exists a tradeoff between bias and variance, shown schematically in Fig.2.4(left).

However, in modern machine learning, very high-capacity models such as neural networks can be trained to exactly fit the data, and yet obtain high accuracy on test data[Belkin_2019], as shown in Fig.2.4(right).
This phenomenon is known as “double descent.”
The apparent contradiction may be addressed by considering the regularizing (Sec.2.5) effects of neural network training, specifically stochastic gradient descent (Sec.9.2).{pdgxfigure}

Curves for training risk (dashed line) and test risk (solid line) from Belkin et al. in Proceedings of the National Academy of Sciences, 2019.
The classical U-shaped risk curve arising from the bias-variance trade-off (left) and the double descent risk curve (right), which incorporates the U-shaped risk curve (\ie, the “classical” regime) together with the observed behavior from using high capacity function classes (\iethe “modern” regime).

## 2.5Regularization

The trained modelf^\hat{f}, or equivalently, the parameters of the trained modelϕ^\hat{\phi}can be thought of as point estimates off∗f^{*}.
The bias-variance tradeoff means that introducing a small bias can often lead to a significant reduction in variance.
This motivates the explicit addition of aregularizationterm to the loss function, which will introduce some biasfreg∗≠f∗f^{*}_{\textrm{reg}}\neq f^{*}.
A common form of regularization is to penalize by the L2 norm of the parameters (\ie∥ϕ∥2\lVert\phi\rVert^{2}), which is referred to asL2 or Tikhonov regularization.
This appears in the form of penalized maximum likelihood, and it is also commonly used in unfolding[Kuusela:2015xqa].
Alternatively, one can penalize by the L1 norm∥ϕ∥\lVert\phi\rVert, which is known asL1 regularization.
One can also interpret the regularization term as an explicit prior on the parameters, and the resulting model as the Bayesian maximum a posteriori (MAP) estimator.
When L1 or L2 regularization is paired with linear regression, it is known asLASSO regressionorridge regression, respectively.
In addition, L2 regularization paired with kernel machines gives rise to Gaussian process regression.

These two types of explicit regularization generally have solutions with different properties.
For example, L1 regularization naturally induces sparsity,\ie, a fraction of the parameters are nearly zero, whereas L2 regularization tends to keep all parameters nonzero but with lower magnitudes, as illustrated in Fig.2.5.
Because L1 regularization sets certain parameters to zero, it is often used as part of feature selection and model compression techniques, as discussed in Sec.11.{pdgxfigure}

Depiction of L1 (left) and L2 (right) regularization constraint regions and the contours of an unregularized loss function.
The intersection with the L1 constraint region gives an optimal valueϕ^\hat{\phi}that is sparse,\ie,ϕ1=0\phi_{1}=0, while the L2 contraint region yields an optimal valueϕ^\hat{\phi}where bothϕ1\phi_{1}andϕ2\phi_{2}are small, but nonzero.

Another form of regularization is to restrict the model classℱ^\hat{\mathcal{F}}.
For example, a neural network and a sequence of narrow step functions (delta functions) can both be shown to be
universal approximators in infinite parameter size limit, but on real world examples the former generalizes much better than the latter.
Within the class of neural network models, convolutional neural networks are a subset of generic feedforward neural networks that approximately preserve translational symmetry (see Sec.8.4.4for more discussion).
These types of choices are often encoded in the architecture of a neural network and are broadly referred to asinductive biasin the model.

In addition to explicit regularization terms in the loss function or through restrictions to the model class, it is also possible to regularize implicitly.
One implicit regularization is through early stopping[DBLP:journals/corr/RosascoTV14,Kuusela:2015xqa], where we monitor the
loss on the training dataset and the loss on held-out validation dataset.
While the training loss continues to decrease with more gradient descent cycles, the validation loss may not, and early stopping stops the training when validation loss flattens out or begins to increase.
Another powerful form of regularization used in deep learning models is known asdropout[dropout], which randomly removes some some parts of the model during training and can be thought of as implementing a type of model averaging[baldi2013understanding].

The chosen numerical optimization procedure can also act as an implicit regularization.
In the case of highly over-parameterized models where there is a large degenerate parameter space that achieves zero loss,Φ0={ϕ|ℛemp​[fϕ]}=0\Phi_{0}=\{\phi|\mathcal{R}_{\textrm{emp}}[f_{\phi}]\}=0, the dynamics of the optimization algorithm will break the degeneracy and favor some particularϕ^∈Φ0\hat{\phi}\in\Phi_{0}as if an additional regularization term was included.
Despite zero loss and over-parametrization, the corresponding generalization error may be small, a phenomenon calledbenign overfitting[Belkin18].
Different optimization algorithms will have different implicit regularization effects, and thus favor different parameter points inΦ0\Phi_{0}that will have different generalization error[pmlr-v80-gunasekar18a].
Understanding this interaction is a topic of contemporary research in machine learning[zdeborova2020understanding].

Some methods such as Gaussian process (GP) do not require
optimization, and instead use linear algebra to obtain the
solution. Benign overfitting
is explicit for GP in that in the absence
of noise the solution goes through
all the training data, yet it generalizes well if the kernel
is well chosen. Infinitely
wide neural networks have
an explicit correspondence to
Gaussian process[neal1994priors].
When applied to deep
networks this leads to the concept of neural tangent kernel[JacotHG18].

## 3Unsupervised learning

Unsupervised learning generally refers to the class of problems that use unlabeled training dataset{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}, wherexi∈𝒳x_{i}\in\mathcal{X}are the input features. Furthermore, it is typically assumed that(xi)​∼i.i.d.​p​(x)(x_{i})\overset{\text{i.i.d.}}{\sim}p(x), thoughp​(x)p(x)is usually not known explicitly. Finally, the loss function in unsupervised learning takes on the special formℒ​(x,f​(x))\mathcal{L}(x,f(x)).
This class of learning has many
different applications, such as
density estimation, anomaly detection,
generative learning, representation learning and clustering, each
with the corresponding set of methods. Some
of these tasks can be achieved with
the same methods,\egnormalizing flows (see Sec.3.4.3) can perform density estimation,
generative sampling
and anomaly detection.

## 3.1Representation learning, compression, and autoencoders

A recurring topic in machine learning and statistics is how to represent the data.
Much of classical statistics involves constructing a low-dimensional summary statistic that extracts the relevant information from the data for a particular task (a sufficient statistic in the language of classical
statistics).
There is a spectrum of representations with tradeoffs. At one end of this spectrum is lossless compression that allows one to encode the data into a smaller, intermediate representation that carries all the information since it can be decoded back into the original data.
At the other end of the spectrum is something like the likelihood ratio, which is a single scalar that carries the relevant information needed for hypothesis testing for a single hypothesis, but it discards all the other information that might be needed for other tasks, such as testing other hypotheses.
An intermediate point in this spectrum is the process of feature engineering, which refers to the creation of new features𝒳′\mathcal{X}^{\prime}from the original features𝒳\mathcal{X}in hopes that the downstream task will be easier with the new features.
For example, instead of working directly with the energy and momentum of particles, one might compute invariant masses or angles between particles.
This type of feature engineering generally improves performance for shallow neural networks and decision trees; however, with the rise of deep learning this is often no longer necessary and may limit performance compared to working with the original features[Guest:2018yhq].
One can think of the intermediate layers of a neural network between the input and the output a representation of the data that is good for the task at hand, and by training all the layers of the network simultaneously (or “end-to-end”) one can see the intermediate layers as a learned representations.
For a review, see Ref.[bengio2013representation].

An example of a linear dimensionality reduction representation and data compression is principal component analysis (PCA) of datax∈ℝd{x}\in\mathbb{R}^{d}at fixed latent space dimensionalitykk(k<dk<d), which finds the orthogonal linear transformation,O{O},O:ℝk→ℝd,z↦O​z,O​O⊺=Id{O}:\mathbb{R}^{k}\to\mathbb{R}^{d},{z}\mapsto{O}{z},\,{O}{O}^{\intercal}{=}I_{d}(21)

that maximizes the data variance in the latent space.
Maximizing the variance of the transformed data is equivalent to minimizing the average reconstruction error (the residual variance in data space),ℒreco​(x,f​(x))=∥x−f​(x)∥2.\mathcal{L}_{\text{reco}}(x,f(x))=\lVert x-f(x)\rVert^{2}\;.(22)

A PCA can thus be interpreted as a linear, orthogonal model that is trained to minimize theL2L_{2}-distance between the input data and the reconstructed data given the fixed dimensionalitykk.
In practice, the PCA problem can be solved analytically without the use of optimization algorithms or the loss function: the principal components are given by the eigenvectors of the data covariance matrix.

A suitable latent space dimensionality,kk, is chosen by ordering the eigenvalues,λi\lambda_{i}, of the data covariance in descending order, and keeping only the first few eigenvectors that correspond to the largest eigenvalues.
The cut is often made at dimensionalities that capture around 90% of the data variance.
For many data sets this results ink≪dk\ll d. The average reconstruction error that originates from the discarded eigenvalues isσreco2=∑i=k+1dλi\sigma_{\mathrm{reco}}^{2}{=}\sum_{i=k+1}^{d}\lambda_{i}.

Another common type of representation learning and
nonlinear dimensionality reduction is based on theautoencoderf=g∘e:𝒳→𝒳f=g\circ e:\mathcal{X}\to\mathcal{X}, wheree:𝒳→𝒵e:\mathcal{X}\to\mathcal{Z}is referred to as theencoderandg:𝒵→𝒳g:\mathcal{Z}\to\mathcal{X}is referred to as thegeneratorordecoder. Typically the dimensionality of𝒵\mathcal{Z}is much less than𝒳\mathcal{X}, andz=e​(x)z=e(x)can be thought of as a compressed representation of the input.
The intermediate space𝒵\mathcal{Z}is sometimes referred to as the bottleneck or the latent space of the autoencoder.
If the bottleneck is sufficiently large and the encoder and decoder are sufficiently flexible, then the functionffcould just be the identity (\ie, lossless compression).
However, if the encoder and decoder are not sufficiently flexible or the dimensionality of the latent space is not large enough there will be some reconstruction error.
Therefore, the reconstruction error of Eq.22serves as a natural loss function of an autoencoder.

Once trained, the encodere​(x)e(x)can be used independently of the decoder to provide a generic low-dimensional representation of the data. The flexibility of this approach is attractive; however, there are no guarantees that this representation will be optimal for the other task. Indeed, the transition from pre-trained autoencoders to end-to-end learning is one of the important trends that characterized the onset of the deep learning era.

While achieving zero reconstruction error may seem good as it would imply lossless compression, it often performs poorly in practice.
First, the encoder may be overfit to the training dataset and not generalize well to held out data.
This can be addressed by adding a
prior to the training, discussed in Sec.3.4.1.
Second, it may not be robust to domain shift (see Sec.10.2).

## 3.2Clustering

The goal of clustering is to group the data{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}intokkgroups, orclusters, usually withk≪nk\ll n.
Intuitively, if two data points belong to the same cluster, then they should be similar in some sense.
Conversely, if two data points are very different, then they should be assigned to different clusters.
The notion of similarity usually is based on some heuristic, and there are a variety of algorithmic and probabilistic clustering algorithms.
In some caseskkis specified, while in others it is determined by the clustering algorithm.
There is also a distinction between flat clustering that directly partitions the data intokkclusters and hierarchical clustering where clusters are nested hierarchically as the name suggests.
In many cases, clustering uses some notion of distanced​(xi,xj)d(x_{i},x_{j}), which may be theLpL_{p}norm∥xi−xj∥p\lVert x_{i}-x_{j}\rVert_{p}.

One of the most common clustering algorithms is known askk-means, wherekkis specified by the user and results in setsS={S1,…,Sk}S=\{S_{1},\dots,S_{k}\}that minimize the variance of each cluster.
Thus, the objective isarg​min𝐒​∑i=1k∑𝐱∈Si‖𝐱−𝝁i‖2=arg​min𝐒​∑i=1k|Si|​Var⁡Si=arg​min𝐒​∑i=1k12​|Si|​∑𝐱,𝐲∈Si‖𝐱−𝐲‖2{\displaystyle{\underset{\mathbf{S}}{\operatorname{arg\,min}}}\sum_{i=1}^{k}\sum_{\mathbf{x}\in S_{i}}\left\|\mathbf{x}-{\boldsymbol{\mu}}_{i}\right\|^{2}={\underset{\mathbf{S}}{\operatorname{arg\,min}}}\sum_{i=1}^{k}|S_{i}|\operatorname{Var}S_{i}}={\displaystyle{\underset{\mathbf{S}}{\operatorname{arg\,min}}}\sum_{i=1}^{k}\,{\frac{1}{2|S_{i}|}}\,\sum_{\mathbf{x},\mathbf{y}\in S_{i}}\left\|\mathbf{x}-\mathbf{y}\right\|^{2}}(23)

whereμi\mu_{i}is the mean of points inSiS_{i}.kk-means can be interpreted as a Gaussian mixture density estimation ofp​(x)p(x), where all
the Gaussians are isotropic. It can be generalized to a Gaussian mixture model, where both the means and the covariance matrix are estimated.

Among the other class of algorithms that determinekk, density-based spatial clustering of applications with noise (DBSCAN) is one of the most frequently used.
DBSCAN clusters points based on a distance metric (\eg, Euclidean) defined for each application.
Two hyperparameters areϵ\epsilon, the maximum distance threshold to determine whether a neighboring point belongs to the same cluster, and the minimum sample size for a group of close points to be identified as a valid cluster or noise.
While DBSCAN is robust against irregularly shaped clusters with a simple distance-based metric, single threshold parameterϵ\epsilonshared to distinguish all clusters can be challenging.
Hierarchical DBSCAN (HDBSCAN) generalizes to varying densities by building a hierarchy of density-based clusters across allϵ\epsilonvia mutual-reachability distances, then extracts the most stable clusters from a condensed tree.

Finally, neural networks are often used for clustering in particle physics.
One use case is to transform the data points into a latent space where clustering is performed using an unsupervised, traditional algorithm.
For example, an input dataset may not follow an isotropic gaussian distribution which is assumed bykk-means, but one can design a neural network to learn a transformation into the latent space where this assumption holds.
Another use case is to use neural network directly for clustering operation.
Examples include object detection[Acciarri_2017]and segmentation[Domine:2019zhm,Koh:2020snv]in computer vision (see Sec.8.4.4) as well as clustering of graph nodes via edge classification[Farrell:DLPS2017,Farrell:2018cjr,DeepLearnPhysics:2020hut,ExaTrkX:2021abe,Dezoort:2021kfk](see Sec.8.4.7).

## 3.3Density estimation

The goal of density estimation is to estimate a distributionp​(x)p(x)based on samples{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}withxi​∼i.i.d.​p​(x)x_{i}\overset{\text{i.i.d.}}{\sim}p(x). Conceptually, this is the same goal as when fitting a parameterized distributionf​(x;θ)f(x;\theta)to data using the method of maximum likelihood as described in Sec.\crossrefstat:sec:ml of the chapter on statistics. In practice, the difference in the machine learning context has to do with the flexibility of the model and the dimensionality of the data. A highly-flexible model, which can effectively approximate any distribution, is referred to as a non-parametric model (though, ironically, usually this means the model has many parameters). In contrast, typical maximum likelihood fits in particle physics are based on restricted families of distributions with relatively few parameters and the data is typically one- or two-dimensional, though occasionally five- or six-dimensional.

Maximizing the likelihood function in Eq.\crossrefstat:eq:likelihood,ℒ​(θ)=∏i=1nf​(xi;θ)\mathcal{L}(\theta)=\prod_{i=1}^{n}f(x_{i};\theta)is equivalent to minimizing the empirical risk:ℛemp,xe​[fϕ]=−1n​∑i=1nlog⁡fϕ​(x),\mathcal{R}_{\text{emp,xe}}[f_{\phi}]=-\frac{1}{n}\sum_{i=1}^{n}\log f_{\phi}(x)\;,(24)

where we adopt the notation used in this chapter.
The loss is simplyℒ​(x,fϕ​(x))=−log⁡fϕ​(x)\mathcal{L}_{\textrm{}}(x,f_{\phi}(x))=-\log f_{\phi}(x), and the corresponding risk isℛxe​[fϕ]=𝔼p​(x)​[−log⁡fϕ​(x)],\mathcal{R}_{\text{xe}}[f_{\phi}]=\mathbb{E}_{p(x)}[-\log f_{\phi}(x)]\;,(25)

which is the cross entropyH​[p,fϕ]H[p,f_{\phi}].
For density estimation, the model is usually constructed to enforce∫fϕ​(x)​𝑑x=1\int f_{\phi}(x)dx=1andfϕ​(x)≥0f_{\phi}(x)\geq 0so that it can be interpreted as a distribution.
With this constraint, one can show thatfxe∗​(x)=p​(x)f^{*}_{\text{xe}}(x)=p(x).
This is not the only form of training:
flow matching and diffusion methods
train on a different objective,
discussed further below.

The concepts of generalization and overfitting are
particularly acute inunsupervisedlearning, where
the likelihood maximization of equation24,
combined with universal approximator assumption, must converge ontop^​(x)=1n​∑i=1nδ​(x−xi)\hat{p}(x)=\frac{1}{n}\sum_{i=1}^{n}\delta(x-x_{i}), the empirical distribution of the dataset{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}.
This distribution has the highest likelihood on the training dataset and the lowest likelihood on the
test data where it givesp^​(x)=0\hat{p}(x)=0as long as the test dataset are not
identical to the
training dataset. So the empirical distribution of the training dataset has the worst possible generalization property, yet
it is the solution we converge to for
sufficiently expressive architectures
in the absence of
any regularization. In contrast,
in supervised learning we often observe
the phenomenon of benign overfitting,
where even zero loss can generalize well.

In addition to approaches to density estimation that involve learning in the sense of minimizing a loss or risk function, we note that there are also classical density estimation techniques such as histogramming and kernel density estimation[parzen1962estimation,davis2011remarks,Cranmer:2000du]. These techniques often fail in very high dimensions.

## 3.4Generative models

Deep generative models are powerful machine learning models that can learn complex, high-dimensional distributions and generate samples from them. Because of their inherently probabilistic formulation, generative models are rapidly becoming an indispensable tool for scientific data analysis in a range of domains. The goal of generative
models is to draw samples
fromp​(x)p(x). For some
formulations of learnedp​(x)p(x), such as
normalizing flows,
the samples can be
drawn directly. For
other explicit formulations ofp​(x)p(x),
such as Boltzmann machines, one can use
sampling techniques such
as Monte Carlo Markov chain sampling. There
are however many other
approaches to drawing
samples fromp​(x)p(x)that do not rely on its
explicit form.

Generative models can be contrasted against discriminative models that are primarily used for supervised learning tasks. Roughly, discriminative models are used for prediction andf​(x)f(x)provides a point estimate of the targetyy, and they are more closely connected to function approximation. In contrast, generative models describe the data distributionp​(x)p(x)(or the joint data distributionp​(x,y)p(x,y)in a supervised setting). An enlightening discussion of these two approaches can be found in Ref.[NgJ01].

There are a number of different types of deep generative models that have various pros and cons as they do not all have the same capabilities. We will focus on variational autoencoders (VAEs)[kingma2013auto,rezende2014stochastic], generative adversarial networks (GANs)[GANs,radford2015unsupervised], normalizing flows (NFs)[pmlr-v37-rezende15,2014arXiv1410.8516D,dinh2016density,kingma2018glow,kobyzev2020normalizing],
and flow-matching and diffusion models[lipman2023flowmatchinggenerativemodeling,SongE19,SDE,Albergo],
though other approaches have been explored in this quickly developing area of research. Consider these three distinct types of functionality:
- •

generation:ability to sample or “generate” a data pointxi∼p​(x)x_{i}\sim p(x).
- •

likelihood for generated data:ability to evaluate the probability density (likelihood)p​(xi)p(x_{i})for a data pointxix_{i}sampled from the modelxi∼p​(x)x_{i}\sim p(x).
- •

likelihood for arbitrary data:ability to evaluate the probability densityp​(xi)p(x_{i})for an arbitrary data pointxi∈𝒳x_{i}\in\mathcal{X}.

Each of the models above can be used for generation; however, only normalizing flows provide all three capabilities. For reasons that we will describe below, GANs and VAEs do not provide a tractable likelihood function, and they are sometimes referred to asimplicit models. This establishes a connection to simulation-based inference where most scientific simulators are also implicit models with an intractable likelihood. Because normalizing flows have a tractable likelihood, they can be trained via maximum likelihood (Eq.24) as described in Sec.3.3. GANs and VAEs, on the other hand, need to employ some other loss function to be trained. In the case of VAEs, training is based on the ELBO used in variational inference (see Sec.2.3and the discussion around the reverse KL divergence below Eq.18). While GANs are also implicit models they data they can generate is typically restricted to a lower-dimensional manifoldℳ⊂𝒳\mathcal{M}\subset\mathcal{X}, meaning that almost all real training dataset doesn’t “live on” the subspace of possibilities that the model can produce. In this case, the likelihood is for almost all data is zero, and so even ELBO-based training will not work. The breakthrough idea introduced in Ref.[GANs]was to use adversarial training where a classifier would be used to quantify how different the data generated from the model is from the data from the target distribution.

VAEs, GANs, and normalizing flows introduce a mappingg​(z,θ)g(z,\theta)from a base random variablezzto the space of the data𝒳\mathcal{X}. The mapg​(z,θ)g(z,\theta)is typically implemented with a neural network. The random variablezzis sampled from some known base distributionp​(z)p(z)that is both easy to sample and has a density that is easy to evaluate. Typically, the base distribution is a multivariate normal.

In the literature on GANs and normalizing flows, this base random variable is often referred to as a latent variable andp​(z)p(z)is often referred to as a prior distribution.
In the case of VAEs, one additionally adds some normally-distributed (Gaussian) random noiseϵ\epsilonto the output so thatx=g​(z,θ)+ϵx=g(z,\theta)+\epsilon. In this case,xxandzzare not deterministically related andzzis a legitimate latent variable in the model andp​(z)p(z)can be interpreted as the prior on that latent variable. In this case, the model can populate the full space of the data. Unfortunately, the marginal likelihoodp​(x)=∫p​(x,z)​𝑑zp(x)=\int p(x,z)dzinvolves an intractable integral, thus maximum likelihood training is infeasible. However, the likelihood termp​(x|z)p(x|z)is tractable (\iethe Gaussian noise), so training with the ELBO is possible.

Note that the dimensionality ofzzneed not be the same as that ofxx. Ifz∈ℝqz\in\mathbb{R}^{q}and𝒳=ℝd\mathcal{X}=\mathbb{R}^{d}withq<dq<d, then all pointsg​(z,θ)g(z,\theta)will lie on add-dimensional surface inℝd\mathbb{R}^{d}. In the case of a VAE, the Gaussian noiseϵ\epsilonmeans that the generated dataxxwill be distributed in a thin region around the surface defined byg​(z,θ)g(z,\theta).
The presence of a bottleneck (\ieq<dq<d) leads to advantages and disadvantages. The disadvantages for GANs is that the likelihood assigned to almost all real world data (\iedata not generated by the model) will be zero, so training is more difficult and many tasks in probabilistic inference won’t be applicable. However, often real world data is also effectively described by a low-dimensional subspace in the full space of the data – random images look like noise, while natural images are in some sense special. For this reason, images produced by GANs for instance often have better visual quality than those produced by other techniques. This points to the ambiguity encountered in quantifying how close two distributions are, and also motivates the use of distance measures such as the Earth movers distance or Wasserstein distance[arjovsky2017towards,wiatrak2019stabilizing]. Conversely, the lack of a bottleneck (\ieq=dq=d) leads to very large models and scalability issues when the data is high dimensional.

Recent work has also focused on combining ideas from VAEs, GANs, and normalizing flows so that the generative model does involve a bottleneck but can still provide tractable likelihoods for density estimation restricted to that manifold[pmlr-v37-rezende15,rezende2020normalizing,gemici2016normalizing,Brehmer:2020vwc,bohm2020probabilistic]. Some of these models can also be used in the context of anomaly detection and out of distribution detection by identifying data that is off the manifold.

The parametrization of the mapping (the architecture of the neural network) should match the structure of the data and be expressive enough. For problems
with explicit symmetries it is beneficial to include them into the
architecture of the network explicitly, which restricts the
allowed space of the models and matches
their inductive bias (implicit
regularization inherently built into the choice
of architecture of the network) to the data.
Different architectures have been proposed[kingma2018glow,van2017neural,karras2017progressive,karras2019style],
and to achieve the best performance on a new dataset one needs extensive hyperparameter explorations[lucic2018gans].

## 3.4.1Variational autoencoders

The autoencoder was described in Sec.3.1as model for compression and representation learning. The model isf=g∘e:𝒳→𝒳f=g\circ e:\mathcal{X}\to\mathcal{X}, wheree:𝒳→𝒵e:\mathcal{X}\to\mathcal{Z}is referred to as theencoderandg:𝒵→𝒳g:\mathcal{Z}\to\mathcal{X}is referred to as thegeneratorordecoder.
The standard autoencoder is not a probabilistic model, but additional probabilitic structure can be added.

One approach is VAE mentioned above[kingma2013auto,rezende2014stochastic].
By equipping the latent space with a prior distributionp​(z)p(z), the decoder of the autoencoderg​(z,θ)g(z,\theta)implies a distribution on a manifold in the output space𝒳\mathcal{X}. VAEs additionally add some normally-distributed (Gaussian) random noiseϵ\epsilonto the output so thatx=g​(z,θ)+ϵx=g(z,\theta)+\epsilon. This implies thatpθ​(x|z)p_{\theta}(x|z)is a tractable quantity, and it is interpreted as the likelihood in this context.

In a VAE one also elevates the encoder to have a probabilistic form. Instead of encodingz=e​(x)z=e(x)in a deterministic way, one seeks a distribution overzzgivenxx. A natural target for the probabilistic encoder would be to probabilistically invert the decoder.
This inverse problem is solved by the posterior distributionp​(z|x)p(z|x)via Bayes theoremp​(z|x)=p​(x|z)​p​(z)p​(x).p(z|x)=\frac{p(x|z)p(z)}{p(x)}\;.(26)

While the likelihood and the prior may both be tractable, the normalizing constantp​(x)=∫p​(x,z)​𝑑zp(x)=\int p(x,z)dzinvolves an intractable integral (the same intractable integral that makes maximum likelihood training of the VAE infeasible).

One approach to Bayesian inference in these settings is variational inference (VI). In VI one approximates the posterior with some parametric familyqϕ​(z|x)q_{\phi}(z|x)in a parametric form,
and then optimizes the ELBO with respect to its parametersϕ\phi.ELBO=𝔼q​(z)logp(x|z)−DKL[q(z)||p(z)]≤log𝔼q​(z)[p​(x,z)q​(z)]=logp(x),\displaystyle{\rm ELBO}=\mathbb{E}_{q(z)}{\log p({x}|z)}-D_{\text{KL}}[q(z)||p(z)]\leq\log\mathbb{E}_{q(z)}\left[\frac{p(x,z)}{q(z)}\right]=\log p({x})\;,(27)

where we used Jensen’s inequality for
concave functions (log\log) and the reverse
Kullback-Leibler (KL) divergence term isDKL[q(z)||p(z)]=𝔼q​(z)[logq(z)−logp(z)]≥0.D_{\text{KL}}[q(z)||p(z)]=\mathbb{E}_{q(z)}[\log q(z)-\log p(z)]\geq 0\,.(28)

In a VAE, the variational model for the posteriorqϕ​(z|x)q_{\phi}(z|x)is often assumed to be an uncorrelated Gaussian (this is often called mean field approximation) defined by the meanμ\muand varianceΣ\Sigma. Instead of optimizing the mean and variance independently for eachxx, VAEs use neural networks to predict the meanμϕ​(x)\mu_{\phi}(x)and the varianceΣϕ​(x)\Sigma_{\phi}(x). This is calledamortized inference, since after an up-front training cost the approximate posteriorqϕ​(z|x)q_{\phi}(z|x)can be evaluated efficiently with a single forward pass of the neural network. Note the standard auto-encoder is recovered if one only used the meanμϕ​(x)\mu_{\phi}(x)for the encoder and did not add noiseϵ\epsilonto the decoder.

Both the probabilistic encoderqϕ​(z|x)q_{\phi}(z|x)and the probabilistic decoderpθ​(x|z)p_{\theta}(x|z)are trained jointly by optimizing the ELBO.
Unlike the standard autoencoder, which only minimizes the reconstruction error, ELBO optimization of Eq.27has a tradeoff between minimizing the reconstruction error in the first term (averaged over the approximate posteriorq​(z)q(z)), which encourages high quality reconstructions, and minimizing the KL divergence term, which forces the posteriorq​(z)q(z)to be as close to the chosen priorp​(z)p(z), and thus controls the sample quality by matching the aggregate posterior with a chosen prior distribution[FixElbo]. This term regularizes the
VAE latent space, such that every sample
drawn from the priorp​(z)p(z)correspond
to a valid sample. Successful VAE training requires to find a delicate balance between the two contributing terms to the ELBO. Whether the VAE training process succeeds in striking this balance depends on a number of factors, including the network architectures, the chosen prior and the class of allowed posterior distributions.
Once trained, the VAE can be used as a generative model by sampling from the priorzi∼p​(z)z_{i}\sim p(z)and then decoding according topθ​(x|z)=g​(z,θ)+ϵp_{\theta}(x|z)=g(z,\theta)+\epsilon.

VAEs allow for expressive architectures, enjoy the benefits of regularization through data compression and have a firm theoretical foundation. Compared to GANs[GANs]3.4.2, VAEs are of particular interest to the scientific community as they provide a lower bound to the marginal likelihood (albeit potentially
with a large gap) and a posterior distribution for the latent variables.

It is also interesting to consider a special case of the autoencoder and VAE where the encoder and decoder are restricted to be linear transformations, which is effectively PCA. In PCA the (linear) decoder can be writteng​(z)=O​zg(z)=Oz, whereOOis a matrix. As in the case of the autoencoder, PCA is not a probabilistic model, but probabilistic structure can be added.
Probabilistic PCA[TippingBishop1999]assumes that the latent variables follow a Gaussian distribution with mean zero and covarianceΛ\Lambda, whereΛ\Lambdais a diagonal matrix with the rank-ordered eigenvaluesλi\lambda_{i}along its diagonal. The
true distribution of the PCA components may be non-Gaussian, but a Gaussian is the maximum entropy approximation given their first two moments. Note that in probabilistic PCA these moments are measured on training dataset (when finding the principal components).

One can generalize probabilistic PCA to use nonlinear encoder and decoder as in an autoencoder. A Gaussian prior is a poor ansatz for the latent space distribution of data proceed by an autoencoder. Instead one can learn the density of the training samples in latent space using a normalizing flow.
This model was introduced inℳ\mathcal{M}-flows[Brehmer:2020vwc]and
in probabilistic autoencoder (PAE)[bohm2020probabilistic], which achieves similar performance to a VAE in
terms of sample quality without explicit ELBO optimization.
In all these cases the dimensionality of the latent space is a hyperparameter to be chosen or optimized by the user.
Unlike a standard VAE, these models do not add noise to the decoded output, thus the data is strictly restricted to the manifold defined by the decoderg​(z,θ)g(z,\theta). However, unlike a GAN there is a well defined way to take an arbitrary data pointxx, project it onto the manifold, and calculate the density of the data point projected onto the manifold. Thus these models can also be used in the context of anomaly detection and out of distribution detection by identifying data that is off the manifold.

## 3.4.2Generative adversarial networks

GANs[GANs]also
typically choose a low dimensional latent spacezzwith a known prior distributionp​(z)p(z), typically a normal (Gaussian) distribution
with zero mean and unit variance.
GANs do not add noise to the outputg​(z,θ)g(z,\theta), so the likelihoodp​(x|z)p(x|z)(and marginal likelihoodp​(x)p(x)) for almost all of the data space is 0, which precludes training by maximum likelihood and the ELBO.
Instead of training on ELBO, GANs train on a dissimilarity measure defined implicitly by a discriminatorD​(x)D(x)(also referred to as the critic). Calculating the dissimilarity often involves it’s own learning problem (\ie, adversarial training of the discriminator).

The training is usually framed as a mini-max gameming⁡maxD⁡ℒGAN=ming⁡maxD⁡{𝔼x∼p​(x)​log⁡D​(x)+𝔼z∼p​(z)​log⁡[1−D​(g​(z))]}.\min_{g}\max_{D}\mathcal{L}_{\text{GAN}}=\min_{g}\max_{D}\{\mathbb{E}_{x\sim p(x)}\log D(x)+\mathbb{E}_{z\sim p(z)}\log[1-D(g(z))]\}.(29)

The goal of the discriminator is to distinguish between true and
generated data, hence we want to maximize
this loss with respect toDD, assigning 1 to true data and 0 to generated data. The goal
of generator is to fool the discriminator
such that it cannot distinguish between
true and generated data, hence we want to
minimize this loss with respect toggat fixedDD. This can be viewed as a game theoretical setup in a zero sum
game between generator and discriminator.

Instead of this game theory interpretation we
can view the internal objectivemaxD⁡ℒGAN\max_{D}\mathcal{L}_{\text{GAN}}as an implicit loss function that measures the
dissimilarity between the target and
generated distributions.
The loss of Eq.29corresponds to
the Jensen-Shannon (JS) divergence, which is a symmetrized form of KL divergence. However, JS divergence is hard to directly work with, and the adversarial training could bring many problems such as vanishing gradient, mode collapse (tendency of generator to cluster the
samples around the training samples, with holes between them) and non-convergence[arjovsky2017towards,wiatrak2019stabilizing]. One of the core issues is that the distribution generated by the GAN is not guaranteed
to cover the entire space.
To address these issues Wasserstein GANs train onming⁡maxD⁡ℒWGAN=ming⁡maxD⁡{𝔼x∼p​(x)​D​(x)−𝔼z∼p​(z)​D​(g​(z))}.\min_{g}\max_{D}\mathcal{L}_{\text{WGAN}}=\min_{g}\max_{D}\{\mathbb{E}_{x\sim p(x)}D(x)-\mathbb{E}_{z\sim p(z)}D(g(z))\}.(30)

Here again the goal of discriminator is to
make the loss as large as possible
between the true data and the generated
data, while the goal of generator is
to make it as small as possible, so that the discriminator cannot distinguish between the two.
There is no requirement forD​(x)D(x)to
be between 0 and 1, which helps with
the above mentioned problems of JS
divergence. Instead, this is
replaced with a requirement thatD​(x)D(x)is 1-Lipshitz, i.e.
the absolute value of the norm of the gradient of the discriminator output with respect to the input has to
be less or equal to 1.

Eq.30can be interpreted as the
dual form of the 1-Wasserstein distance
between the true and generated distribution[arjovsky2017wasserstein]. Wasserstein
distances are a measure of dissimilarity
between two distributions used
in the context of optimal transport, a
mathematical theory of how to define a notion of distance between probability distributions. Since the transport distance
increases with the separation between
the two distributions when they
are non-overlapping, there is no
gradient collapse that plagues other
measures.
In its primal formpp-Wasserstein distance,p∈[1,∞)p\in[1,\infty), between two probability distributionsp1p_{1}andp2p_{2}, is defined asWp​(p1,p2)=infγ∈Π​(p1,p2)(𝔼(x,y)∼γ​[|x−y|p])1pW_{p}(p_{1},p_{2})=\inf_{\gamma\in\Pi(p_{1},p_{2})}\left(\mathbb{E}_{(x,y)\sim\gamma}\left[|x-y|^{p}\right]\right)^{\frac{1}{p}},
whereΠ​(p1,p2)\Pi(p_{1},p_{2})is the set of all possible joint distributionsγ​(x,y)\gamma(x,y)with marginalized distributionsp1p_{1}andp2p_{2}. In 1D the Wasserstein distance has a closed form solution via cumulative distribution functions (CDFs), but this evaluation is intractable in high dimensions.

In the dual form of 1-Wasserstein distance, one instead maximizes Eq.30over all possible functionsD​(x)D(x)that are 1-Lipschitz. One way to
implement this is through weight clipping of the parameters of discriminator network, but a simpler solution is to add a
gradient norm penalty term explicitly to the
loss function[NIPS2017_4588e674].

Because of the discriminative nature of the dissimilarity measure
defined in data space, GANs and Wasserstein GANs often generate more realistic
samples than VAE or normalizing flows in high dimensions such as
natural images (although flow matching and diffusion models can outperform GANs). However, GANs do not provide an encoder
from data to latent space nor a tractable likelihoodp​(x)p(x).

## 3.4.3Normalizing flows and autoregressive models

Normalizing flows (NFs) provide a powerful framework for density estimation and sampling[pmlr-v37-rezende15,2014arXiv1410.8516D,dinh2016density,papamakarios2017masked,kingma2018glow,kobyzev2020normalizing]. These models map the dataxxto latent variableszzthrough a sequence of invertible transformationsf=f1∘f2∘⋯∘fnf=f_{1}\circ f_{2}\circ\dots\circ f_{n}, such thatz=f​(x)z=f(x)orx=g​(z)=f−1​(x)x=g(z)=f^{-1}(x). As in the VAE and GAN,zzis modeled as a random number with a simple base distributionpZ​(z)p_{Z}(z), which is typically chosen to be a standard normal (Gaussian) distribution. Since NFs are invertible
the dimensionality of the latent
space equals the dimensionality of the data space, in contrast to VAE and GANs where the
latent space dimensionality is
often lower.
The probability density of the model be evaluated using the change of variables formula:pX​(x)=pZ​(f​(x))​|det(∂f​(x)∂x)|=pZ​(f​(x))​∏l=1n|det(∂fl​(x)∂x)|,p_{X}(x)=p_{Z}(f(x))\left|\det\left(\frac{\partial f(x)}{\partial x}\right)\right|=p_{Z}(f(x))\prod_{l=1}^{n}\left|\det\left(\frac{\partial f_{l}(x)}{\partial x}\right)\right|,(31)

where we have added subscripts topX​(x)p_{X}(x)andpZ​(z)p_{Z}(z)for clarity.
The Jacobian determinantdet(∂fl​(x)∂x)\det(\frac{\partial f_{l}(x)}{\partial x})must be efficient to compute for density estimation to be practical, and the transformationflf_{l}should be easy to invert for sampling.
In contrast to VAE and GANs, standard normalizing flows preserve the dimensionality of the data space as they are invertible (though there are normalizing flows that are defined on lower dimensional manifolds embedded in the data space[pmlr-v37-rezende15,rezende2020normalizing,gemici2016normalizing,Brehmer:2020vwc,bohm2020probabilistic]). As such, unlike GANs and VAEs, they can be trained via maximum likelihood (Eq.24) as described in Sec.3.3.

There are several popular architectures
of NFs. A method used by NICE,
RealNVP and Glow[2014arXiv1410.8516D,dinh2016density,kingma2018glow]is to split the space
into two disjoint setsz1z_{1}andz2z_{2},
and then use an identity forward mapz→xz\rightarrow xforx1x_{1},x1=z1x_{1}=z_{1},
and an affine transformation forx2x_{2}of the formx2=exp⁡(s​(z1))⊙z2+m​(z1),x_{2}=\exp(s(z_{1}))\odot z_{2}+m(z_{1}),(32)

where⊙\odotis elementwise product
andm​(z1)m(z_{1}),s​(z1)s(z_{1})are neural networks.
The Jacobian of this map is lower
triangular, and its determinant is simply the product of elements along the diagonal, which is
tractable, as is the inverse of the transformation. At the
next layer one then performs a
different split of dimensions intoz1z_{1}andz2z_{2}. The affine transformation
can be further generalized to a nonlinear form using
rational splines[durkan2019neural].

One can interpret the sequence of invertible transformationsf1∘f2∘⋯∘fnf_{1}\circ f_{2}\circ\dots\circ f_{n}asnndiscrete time steps in a continuous flow. In particular, one can think of a continuous-time flow described by an ordinary differential equation (ODE) and then interpret the discrete time steps as the result of a numerical integration of that ODE. This is the approach taken by the Ffjord algorithm[grathwohl2018ffjord]and other variants. A residual
flow has an updatefi​(x)=xi+δ​ui​(x)f_{i}(x)=x_{i}+\delta u_{i}(x), which forδi=n−1\delta_{i}=n^{-1}and takingn→∞n\rightarrow\inftylimit gives rise to an ordinary differential equation (ODE)d​xt=ut​(xt)​d​t.dx_{t}=u_{t}(x_{t})dt.(33)

Hereutu_{t}is the velocity field
that defines the flow and is a vector field. One can build the density estimator for all intermediate timesttpt​(x)p_{t}(x)using its divergence,ln⁡pt​(xt)=ln⁡p0​(x0)−∫0t∇⋅us​(xs)​𝑑s,\ln p_{t}(x_{t})=\ln p_{0}(x_{0})-\int_{0}^{t}\nabla\cdot u_{s}(x_{s})ds,(34)

wherep0p_{0}att0t_{0}is the initial base distribution andp1p_{1}att=1t=1is the target distribution.
Continuous normalizing flows parametrizeutu_{t}as a neural network. They are very expressive, but expensive to train using
maximum likelihood.

A different approach creating a deep generative model with a tractable likelihood is to
modelp​(x)p(x)autoregressively asp​(x)=∏i=1np​(xi|x1,x2,…,xi−1).p(x)=\prod_{i=1}^{n}p(x_{i}|x_{1},x_{2},\dots,x_{i-1})\;.(35)

This form describes each
new dimension conditionally on all
previous dimensions. It can model a general
likelihoodp​(x)p(x)as a sequence of
conditional 1d distributions, whose
conditional dependence on the
parametersx1,x2,…,xi−1x_{1},x_{2},\dots,x_{i-1}can be modeled with
neural networks. Ifxxis a
time series this form imposes a causal
structure wherexix_{i}depends on
all previous timesxjx_{j},j<ij<i.
WaveNet[2016arXiv160903499V]and PixelCNN[PixelCNN]) are two well known examples.
Sampling from an autoregressive model
is sequential, and can be slow in
high dimensions. Inverse autoregressive
flow reverses this process and makes
sampling fast, but the likelihood evaluation is
slow. Some normalizing flows have
autoregressive coupling layers, such as masked
autoregressive flow (MAF)[papamakarios2017masked].

All of the methods above use maximum likelihood training of likelihoodp​(x)p(x)against network parameters, so
the training is to minimize KL divergence between the data
distribution and a Gaussian in latent space. This can be overly sensitive
to small variance directions that
dominate the likelihood, without
being sensitive to the global
structure of the data.
An alternative is to
use Optimal Transport Wasserstein distance between
the density of the generated samples and the data, which can be evaluated either
in data space or in latent space.
As Wasserstein distance is difficult to evaluate
in high dimensions, one can instead use slices, 1d projections of the
data along different directions in
high dimensional space, to
build the flow[SINF].
Because this training is less sensitive to
small variance directions than maximum likelihood
training it achieves
better results on anomaly
detection tasks[SINF].

We end by noting that normalizing flows, autoregressive models, and other deep generative models that provide a tractable likelihood are powerful tools for simulation-based inference. They can provide surrogate models trained from large simulated datasets when the simulators have intractable likelihood functions, which is usually the case. As described in Sec.6, one would like to work with models that can provide conditional density estimation in order to model either the likelihoodp​(x|θ)p(x|\theta)or the posteriorp​(θ|x)p(\theta|x)[Cranmer:2016lzt,NIPS2016_6084]. These techniques are being actively explored and applied to a number of scientific problems.

## 3.4.4Flow-matching and diffusion models

In flow-matching models,
we start from a base distribution such as a Gaussianp0=𝒩​(0,I)p_{0}=\mathcal{N}(0,I), and use ODEs to generate
samples with a flow
vector fieldutθ​(x)u_{t}^{\theta}(x)as in Eq.33.
As discussed above, continuous
normalizing flows are expensive to train via maximum likelihood.
Instead, one can learn directly
the velocity field parametrized as a neural networkutθ​(xt)u_{t}^{\theta}(x_{t})with parametersθ\thetavia the flow-matching lossℒ=𝔼t∼U​(0,1),x∼pt​[ut​(xt)−utθ​(xt)]2,\mathcal{L}=\mathbb{E}_{t\sim U(0,1),~x\sim p_{t}}\left[u_{t}(x_{t})-u_{t}^{\theta}(x_{t})\right]^{2},(36)

where the expectation is uniform over timettand over all intermediate
distributionsptp_{t}. This equation
is however not practical since we
do not know the targetut​(x)u_{t}(x). Instead,
one can take advantage of the target
conditional velocity fieldut​(xt|z)u_{t}(x_{t}|z), wherez∼p^z\sim\hat{p}is a training data sampleℒ=𝔼t∼U​(0,1),x∼pt,z∼p^​[ut​(x|z)−utθ​(xt)]2.\mathcal{L}=\mathbb{E}_{t\sim U(0,1),~x\sim p_{t},~z\sim\hat{p}}\left[u_{t}(x|z)-u_{t}^{\theta}(x_{t})\right]^{2}.(37)

It has been shown that this
conditional target velocity field training
also leads to the correct
distribution in the flow models[lipman2023flowmatchinggenerativemodeling,Albergo]. Figure3.4.4, taken from Ref.[holderrieth2025introductionflowmatchingdiffusion], illustrates
the main idea, which is that
training a conditional flow, and
averaging over all the training data,
is the same as training on unconditional flow.

The advantage of this formulation is that conditional velocity fields are a lot simpler to construct. A typical
case is a flow from the initial
Gaussianp0​(x|z)=𝒩​(0,I)p_{0}(x|z)=\mathcal{N}(0,I)to a delta function at zp1​(x|z)=δz​(x)p_{1}(x|z)=\delta_{z}(x). A
very simple linear flow that
achieves this ispt​(x|z)=𝒩​(t​z,(1−t)2​I)p_{t}(x|z)=\mathcal{N}(tz,(1-t)^{2}I). The flow itself moves from
a random Gaussian variableϵ∼𝒩​(0,I)\epsilon\sim\mathcal{N}(0,I)to the
data pointzz, soxt=ϵ​(1−t)+t​zx_{t}=\epsilon(1-t)+tz. Finally, the conditional velocity field is given byu​(xt|z)=z−ϵu(x_{t}|z)=z-\epsilon, so the training loss isℒ=𝔼t∼U​(0,1),ϵ∼𝒩​(0,I),z∼p^​[z−ϵ−utθ​(ϵ​(1−t)+t​z)]2.\mathcal{L}=\mathbb{E}_{t\sim U(0,1),~\epsilon\sim\mathcal{N}(0,I),~z\sim\hat{p}}\left[z-\epsilon-u_{t}^{\theta}(\epsilon(1-t)+tz)\right]^{2}.(38)

This leads to a simple
training algorithm where one
randomly chooses a minibatch of
datazz, random Gaussian variablesϵ\epsilon, and a timettto
update the parametersθ\thetabased on stochastic gradient descent using the loss of Eq.38.
The simplicity and efficiency of this training
procedure has led flow matching
to become one of the leading generative
models for large image based data.
Sampling from flow-matching
models requires randomly choosing an initial conditionx0∼N​(0,I)x_{0}\sim N(0,I)and discretizing Eq.33. Note that this is
a deterministic ODE and all the
randomness is in the initial
conditions.

Diffusion models also start from a Gaussian base distribution, but also continuously add noise during the evolution in time,\ie, they are based on a stochastic differential equation (SDE)x0∼p0,d​xt=utθ​(xt)​d​t+σt22​st​(xt)+σt​d​Wt,x_{0}\sim p_{0},\,\,\,dx_{t}=u_{t}^{\theta}(x_{t})dt+\frac{\sigma^{2}_{t}}{2}s_{t}(x_{t})+\sigma_{t}dW_{t},(39)

where we define scorest​(xt)=∇ln⁡pt​(xt)s_{t}(x_{t})=\nabla\ln p_{t}(x_{t}).
Here,d​WtdW_{t}is the stochastic term, which adds Brownian motion (also called a Wiener process) in the form of
uncorrelated Gaussian random noise. Note that withσt=0\sigma_{t}=0, a diffusion model becomes a flow model.
The noise varianceσt\sigma_{t}is a
free parameter that can be tuned for optimal performance. If our target is a static distribution so thatpt=pp_{t}=pthenut=0u_{t}=0and we obtain the Langevin
equation.

In diffusion, we also need to learn
the gradient field via the score
function, and as before we can
replace the marginal score with
conditional score during the
training to obtain score matching
training procedureℒ=𝔼t∼U​(0,1),x∼pt,z∼p^​[∇ln⁡pt​(x|z)−stθ​(xt)]2.\mathcal{L}=\mathbb{E}_{t\sim U(0,1),~x\sim p_{t},~z\sim\hat{p}}\left[\nabla\ln p_{t}(x|z)-s_{t}^{\theta}(x_{t})\right]^{2}.(40)

In
the simple Gaussian example withpt​(xt)=𝒩​(αt​z,βt2​I)p_{t}(x_{t})=\mathcal{N}(\alpha_{t}z,\beta_{t}^{2}I),
whereα0=β1=0\alpha_{0}=\beta_{1}=0andα1=β0=1\alpha_{1}=\beta_{0}=1, we have
a trajectoryxt=αt​z+βt​ϵx_{t}=\alpha_{t}z+\beta_{t}\epsilon, and the score lossℒ=𝔼t∼U​(0,1),ϵ∼𝒩​(0,I),z∼p^​[ϵβt+stθ​(αt​z+βt​ϵ)]2.\mathcal{L}=\mathbb{E}_{t\sim U(0,1),~\epsilon\sim\mathcal{N}(0,I),~z\sim\hat{p}}\left[\frac{\epsilon}{\beta_{t}}+s_{t}^{\theta}(\alpha_{t}z+\beta_{t}\epsilon)\right]^{2}.(41)

It would appear that in diffusion,
one must train both the flow and
the score, but for simple linear
models the two can be related to
one another, and one can
choose the flow-matching or score-matching training procedure. For
the example in Eq.39, the corresponding score-matching training isx0∼p0,d​xt=[(βt2​α˙α−βt​β˙t+σt22)​st​(xt)+α˙α​xt]​d​t+σt​d​Wt.x_{0}\sim p_{0},\,\,\,dx_{t}=\left[\left(\beta_{t}^{2}\frac{\dot{\alpha}}{\alpha}-\beta_{t}\dot{\beta}_{t}+\frac{\sigma^{2}_{t}}{2}\right)s_{t}(x_{t})+\frac{\dot{\alpha}}{\alpha}x_{t}\right]dt+\sigma_{t}dW_{t}.(42)

One of the advantages of
score- and flow-based methods is
that
one can reduce the architectural restrictions
imposed by normalizing flows or autoregressive
models. Score- and flow-based training avoid the normalization requirement.
Score-based models learn gradients of log probability density functions on a large number of noise-perturbed data distributions, and then generate samples by Langevin-type sampling.

The generative models
described in this subsection are called flow-based models[lipman2023flowmatchinggenerativemodeling], score-based generative models[SongE19], diffusion probabilistic models[SDE],
or stochastic interpolants[Albergo]. They
have several advantages over other model families. They often outperform GAN-level sample quality without adversarial training, and enable exact log-likelihood computation
through their connection to continuous-time flows, which can be represented as a
probability flow ordinary differential equation[SDE].
The main advantage is that the
distributionp​(x)p(x)can be specified solely by its score or flow.
This in turn
enables more flexible model
architectures than what can be
used in normalizing flows or autoregressive models.{pdgxfigure}


Illustration of the marginalization trick for flow-based models (left) and diffusion models (right), which simulate a probability path with ODEs or SDEs, respectively (Holderrieth and Erives, 2025).
The data distributionp^\hat{p}is the blue background, while the initial Gaussian distribution is the red background.
The top graphs represent conditional probability paths, while the bottom graphs represent marginal probability paths.
Both samples and trajectories are shown.

## 3.5Anomaly detection and out-of-distribution detection

Unsupervised anomaly detection techniques detect anomalies in an unlabeled test data set under the assumption that the majority of the in-distribution data are normal under some measure, while out-of-distribution (OOD) data are not.
In the context of autoencoders
a popular technique is to use the
reconstruction error of Eq.22to
identify an outlier as one with a
large reconstruction error[PhysRevD.101.076015,Farina_2020,Heimel_2019]. One issue with this
method is that for higher dimensional
latent space and flexible neural network architectures the
encoder-decoder map become identity for
any input data,f​(x)=xf(x)=x, regardless of whether inputxxis from the in-distribution training dataset or from the out-of-distribution data. The choice of
autoencoder latent space dimensionality is thus an
important hyperparameter that must be
tuned.

Another set of anomaly detection techniques construct a model representing normal behavior from a given in-distribution training dataset, and then evaluate the likelihood of a test instance to be generated by the utilized model. For instance, one can use density
estimation methods such as normalizing
flows (section3.4.3) to learn the density (likelihood) of the in-distribution training datasetp​(x)p(x), and apply it to
the test data. The expectation is that
out-of-distribution data will have a
lower density (likelihood) under the in-distribution
density model.
This expectation is however not always met in high dimensions and the
method suffers because
likelihood-based training is sensitive to the smallest variance directions[ren2019likelihood].
Low-variance directions may contain little or no information on the global structure of the image, so there is a mismatch
between the training objective and outlier detection objective.
Lower dimensional autoencoders with NF in the latent space
deal better with this issue[bohm2020probabilistic].

A related issue is that of typicality: an in-distribution data sample likelihood
will typically be lower
than the maximum value, so an out-of-distribution data sample that
is closer to the peak would have a higher likelihood. If
this happens in low-variance
directions that dominate the likelihood, normalizing flows can assign higher likelihoods to out-of-distribution data than to in-distribution training data[nalisnick2018deep].
A number of techniques have been proposed to
circumvent these limitations, such as
likelihood regret[xiao2020likelihood], likelihood-ratio[ren2019likelihood],
likelihood in autoencoder latent space[bohm2020probabilistic], and Wasserstein distance training of the likelihoodp​(x)p(x)[SINF,CMS:2025lmn]. These methods can achieve better anomaly detection performance
than the autoencoder reconstruction error[Brehmer:2020vwc,bohm2020probabilistic,CMS:2025lmn].
However, even perfect density estimation cannot guarantee good anomaly detection performance[Le_Lan_2021,Kasieczka:2022naq].

Supervised anomaly detection techniques require a data set that has been labeled as in-distribution and out-of-distribution and involves training a classifier (the key difference to many other statistical classification problems is the inherent unbalanced nature of outlier detection). These methods
assume some form for what out-of-distribution data may look like, and their success relies
on whether the assumed form is a realistic
representation of actual out-of-distribution data. When this assumption is
valid these methods
can be more powerful than unsupervised
methods, but the reverse is also true.
A hybrid between the two approaches is to
train a classifier without labels[Collins:2018epr]. All
these approaches are largely
complementary to each other[Collins_2021]. Examples of different
anomaly detection methods applied to
HEP are the LHC Olympics 2020 and Dark Machines challenges[Kasieczka:2021xcg,Aarrestad:2021oeb].

## 4Self-supervised learning

Self-supervised learning (SSL) also aims to distill useful features in the data without requiring supervision labels for every sample in the input data.
Self-supervised methods make use of large unlabeled datasets to build meaningful representations.
They can generally be categorized asautoassociative, where the model is trained to reproduce or reconstruct its own (masked) input orcontrastive, where the model is trained to learn a mapping that is insensitive to different “views” of the data.
These methods are often used to build “foundation models” (FMs) discussed in Sec.9.11, which are pre-trained using self-supervised learning and fine-tuned using supervised learning for different downstream tasks.
However, FMs are not the only possible use case.

A classic autoassociative task is masked language modeling popularized by the bidirectional encoder representations from transformers (BERT) model[bert].
In this task, BERT ingests a sequence of words, a fraction of which are randomly masked, and tries to predict the original words that have been masked.
For example, in the sentence “The Milky Way is a [MASK] galaxy,” BERT would need to predict “spiral.”
This helps BERT learn bidirectional context.
A variant of this approach is next token prediction, popularized by the generative pretrained transformer (GPT)[gpt3].
A common theme in these methods istokenization, in which elements of the input data are mapped to discrete vectors, known as tokens.
These approaches have been applied in the context of particle jets[mpmv1,mpmv2,omnijetalpha], enabling the construction of backbone models that can be fine-tuned for different tasks and provide improvements for small training samples.

Sensory data (\eg, 1D waveforms, 2D images, or 3D scenes) pose a significant challenge for autoassociative tasks compared to symbolic data such as language, math, and high-level physical concepts like jets and particles.
For symbolic data, the masking unit is naturally defined (\eg, a word for language) and associated with a strong semantic meaning, which yields a well-defined learning objective for mask-based self-supervision.
On the contrary, sensory data captures raw information and a unit of data (\ega single pixel in an image) does not carry meaningful information alone.
This challenge has resulted in in-depth R&D for self-supervision techniques in computer vision.
The masked autoencoder (MAE) laid the initial ground work[MaskedAutoencoders2021]: the authors discovered that a large fraction of masking (\ie, 75%) is crucial for successful training using an asymmetric encoder-decoder architecture.
Distillation with no labels (DINO) made another breakthrough by introducing a self-distillation technique where a student and teacher model pair—the teacher model typically being an exponential moving average of the student model—are forced to agree across different augmentations (\eg, cropping, adding jitter, and rotating) of the same data instance[caron2021emerging,oquab2023dinov2].
For effective representation learning of 3D geometrical shapes, multi-view projection matching techniques[dust3r_cvpr24,duisterhof2025mastrsfm,wang2025vggt]are promising and a strong promise and relevant to time projection chamber (TPC) image data in high energy physics.
Exploration of these specialized techniques in computer vision has impacted HEP applications[young2025particletrajectoryrepresentationlearning,Hao:2025abk].

In contrastive learning, portions of the input data are paired together and the model is tasked to find matching pairs.
Pairs can be constructed based on different data modalities, such as text and images, or based on data augmentations, that may be generic, such as adding noise, or domain-specific, like symmetry transformations.
For example, the contrastive language-image pre-training (CLIP)[clip]allows joint pretraining of a text encoder and an image encoder, such that a matching image-text pair have image encoding vector𝐳i\mathbf{z}_{i}and text encoding vector𝐳j\mathbf{z}_{j}that span a small angle,\ie, have a large cosine similarityc​(𝐳i,𝐳j)=𝐳i⋅𝐳j|𝐳i|​|𝐳j|=cos⁡θi​j,\displaystyle c(\mathbf{z}_{i},\mathbf{z}_{j})=\frac{\mathbf{z}_{i}\cdot\mathbf{z}_{j}}{|\mathbf{z}_{i}||\mathbf{z}_{j}|}=\cos\theta_{ij}\;,(43)

withθi​j\theta_{ij}being the angle between the encoding vectors.
This approach has been applied in astrophysics[astroclip].

Positive pairs may also be constructed by applying data augmentations.
For example, in the case of galaxy images, one may augment the data by performing image rotations, adding noise, size scaling, or adding point spread function smoothing, all of which are realistic transformations expected in a real galaxy image survey[Hayat2021,ChenK0H20].
For particle jets, tailored augmentations may include rotations about the jet axis, translations in the(η,ϕ)(\eta,\phi)plane, smearing the positions of the soft jet constituents, and collinear splitting of the jet constituents[Dillon:2021gag,PhysRevD.106.056005,10.21468/SciPostPhysCore.7.3.056,largescale].
Another augmentation strategy is based on re-simulating the stochastic shower and detector interactions, thus generating multiple physical realizations of a primary particle’s evolution[resimulation,ssljetphysics].

A well-known approach for contrastive learning with augmentations is SimCLR[simclr].
In this approach, the contrastive loss for a positive pair of an input and its augmentation(𝐳i,𝐳i′)(\mathbf{z}_{i},\mathbf{z}_{i}^{\prime})is defined in terms of the cosine similarity of Eq.43asℒ​(𝐳,𝐳i′)=−ln⁡exp⁡[c​(𝐳i,𝐳i′)/τ]∑j≠i∈batch[exp⁡[c​(𝐳i,𝐳j)/τ]+exp⁡[c​(𝐳i,𝐳j′)/τ]],\mathcal{L}(\mathbf{z},\mathbf{z}_{i}^{\prime})=-\ln\frac{\exp[c(\mathbf{z}_{i},\mathbf{z}_{i}^{\prime})/\tau]}{\displaystyle\sum_{j\neq i\in\text{batch}}\left[\exp[c(\mathbf{z}_{i},\mathbf{z}_{j})/\tau]+\exp[c(\mathbf{z}_{i},\mathbf{z}_{j}^{\prime})/\tau]\right]}\;,(44)

and the total loss is given by the sum over all positive pairs in the batch,∑i∈batchℒ​(𝐳i,𝐳i′)\sum_{i\in\text{batch}}\mathcal{L}(\mathbf{z}_{i},\mathbf{z}_{i}^{\prime}).
The loss decreases when the distance between positive pairs decreases or when the distance between negative pairs increases.
The hyperparameterτ\tauis known as temperature and controls the relative influence of positive and negative pairs.
SimCLR has been applied in radio astronomy[BaronPerez:2025], neutrino physics[Wilkinson:2025nxv], and collider physics[Dillon:2021gag].
Another application of contrastive regularization is self-distillation introduced in DINO discussed above.
Self-distillation is a powerful technique that can be applied regardless of the target task, and improves the quality of self-supervision for many computer vision models for both image and point cloud data.

Finally, an alternative paradigm is the joint-embedding predictive architecture (JEPA)[ijepa], which learns meaningful representations by modeling missing or unseen embeddings directly in the latent space without a decoder or full input
reconstruction.
The advantages of this approach are no data augmentations are required and unnecessary details of the input can be ignored.
This approach has been applied to particle jets[jjepa,hepjepa]and Square Kilometer Array (SKA) light cones[Ore:2024jim].
A comparison between the different self-supervised learning approaches can be found in Fig.4, reproduced from Ref.[ijepa].{pdgxfigure}

Common architectures for self-supervised learning, in which the system learns to assign a large scalar value to incompatible inputs, and a low scalar value to compatible inputs (M. Assran, et al. in ICCV, 2023).
Joint-embedding architectures (left) learn to output similar embeddings for compatible inputsx,yx,yand dissimilar embeddings for incompatible inputs.
Generative architectures (center) learn to directly reconstruct a signalyyfrom a compatible signalxx, using a decoder network that is conditioned on additional (possibly latent) variableszzto facilitate reconstruction.
Joint-embedding predictive architectures (right) learn to predict the embeddings of a signalyyfrom a compatible signalxx, using a predictor network that is conditioned on additional (possibly latent) variableszzto facilitate prediction.

## 5Optimal control, reinforcement learning, and active learning

Many problems in science and engineering can be cast as a control problem, which comprises a cost functional that is a function of state and some control variables that specify some underlying dynamical system. This is relevant for the control of accelerators where the dynamical system is physical. This formalism can also be used to describe the design of experiments, planning of an observational survey, and other decision making processes relevant to the scientific method. It is closely connected to planning, dynamic programming, and reinforcement learning. Optimal control generalizes the framing of learning presented in Sec.2.1.

## 5.1Optimal control

Optimal control theory deals with finding a control for a dynamical system over a period of time such that the objective function is optimized. The underlying system can be discrete or continuous and may be deterministic or stochastic. The commonalities and differences between optimal control and reinforcement learning can be best understood through the formalism of a Markov decision process (MDP), which is a discrete-time stochastic control process.

A Markov decision process comprises four components often organized as a 4-tuple(S,A,Pa,Ra){\displaystyle(S,A,P_{a},R_{a})}, where:SSis a set of states called the state space,AAis a set of actions called the action space,Pa​(s,s′)=Pr⁡(st+1=s′∣st=s,at=a){\displaystyle P_{a}(s,s^{\prime})=\Pr(s_{t+1}=s^{\prime}\mid s_{t}=s,a_{t}=a)}is the probability that actionaain statessat timettwill lead to states′s^{\prime}at timet+1t+1,Ra​(s,s′){\displaystyle R_{a}(s,s^{\prime})}is the immediate reward (or expected immediate reward) received after transitioning from statessto states′s^{\prime}, due to actionaa.

The policy functionπ\piis a mapping from state space to action space that can be either deterministic or probabilistic. For examples, the policy that drives a computer chess playing system, decides which move to make given the current state of the board. Similarly, policies dictate which experiment should be built next, which field of the sky should be observed, or how to adjust the operational parameters of an accelerator.
The dynamics of the resulting system are then fixed by combining the policy with the underlying MDP. The evolution of the resulting dynamical system behaves like a Markov chain since the action chosen in statessis completely determined byπ​(s)\pi(s)andPr⁡(st+1=s′∣st=s,at=a){\displaystyle\Pr(s_{t+1}=s^{\prime}\mid s_{t}=s,a_{t}=a)}implies the Markov transition matrixPr⁡(st+1=s′∣st=s){\displaystyle\Pr(s_{t+1}=s^{\prime}\mid s_{t}=s)}.

The objective optimal control is to choose a policyπ\pithat will maximize a cumulative function of the instantaneous rewardsRaR_{a}. A common choice is the expected discounted sum:𝔼​[∑t=0∞γt​Rat​(st,st+1)],{\mathbb{E}\left[\sum_{t=0}^{\infty}{\gamma^{t}R_{a_{t}}(s_{t},s_{t+1})}\right]}\;,(45)

whereat∼π​(st)a_{t}\sim\pi(s_{t})are the actions given by the policy, the expectation computed with respect to the distributionst+1∼Pat​(st,st+1){\displaystyle s_{t+1}\sim P_{a_{t}}(s_{t},s_{t+1})}, andγ\gammais the discount factor satisfying0≤γ≤1{\displaystyle 0\leq\ \gamma\ \leq\ 1}. The discount factor is usually close to 1 and sometimes reparameterized asγ=1/(1+r)\gamma=1/(1+r), whererris called the discount rate. A lower discount factor motivates the decision maker to favor taking actions early, rather than postpone them indefinitely.

A policy that maximizes the objective function is called an optimal policy and denotedπ∗\pi^{*}, though the optimal policy need not be unique. Importantly, the Markov property implies that the optimal policy is only a function of the current state.
Dynamic programming can be used to find the optimal policy for MDPs with finite state and action spaces. For instance, in value iteration (a.k.a. backward induction) can be used to solve the “Bellman equation”[bellman1957]. For continuous-time systems, the optimal policy is defined by the Hamilton–Jacobi–Bellman equation[kirk2004optimal].

In many settings, it is assumed that the statessis fully known when action is to be taken and there are no latent variables. When this assumption is not true, the problem is called a partially observable MDP.
These problems are generally more difficult and the dynamic programming algorithms do not directly apply[aastrom1965optimal].

## 5.2Reinforcement learning

The main difference between the classical dynamic programming methods and reinforcement learning (RL) algorithms is that the latter do not assume knowledge of an exact mathematical model of the MDP and they target large MDPs where exact methods become infeasible. For example, RL was used in the context of jet physics to search for the most likely jet clustering when the number of constituents was too large for the exact dynamic programming algorithm to be used[Brehmer:2020brs].
In addition, RL can be used when the probabilities or rewards are unknown. Instead, the transition probabilities are often accessed indirectly through interaction with a real or simulated environment.

Numerous variations to RL exist, which include so-called model-based and model-free approaches (referring to models of the instantaneous rewards and the state transitions) and on-policy and off-policy (which describes how the actions taken during learning are related to the current policy). See Ref.[sutton1998reinforcement]for an introduction and Ref.[arulkumaran2017deep]for a recent review. Some examples of RL use in particle physics are in Refs.[Carrazza:2019efs,Mendizabal:2025sbf,Wojcik:2024lfy].

## 5.3Multi-arm bandits

Multi-arm bandit problems are a classic reinforcement learning problem where one tries to maximize the expected gain by allocating a limited set of resources to various alternatives. The name is a reference to a gambler with a fixed amount of money that must choose between multiple slot machines (or “one-armed” bandits) when the payoff for the individual machines is unknown.
A hallmark of multi-arm bandit problems is that they involve a tradeoff between exploration (playing machines to estimate their payoff) and exploitation (playing machines with the highest estimated payoff).
Multi-armed bandits are used to manage large projects, organizations, and scheduling problems. The theory has a long history going back to Robbins in 1952 that used it to study the sequential design of experiments[robbins1952some]and Gittins who derived an optimal policy under some conditions[gittins1979bandit].

## 5.4Bayesian optimization

A closely related set of techniques involve optimizing some expensive black box functionf​(x)f(x).
For instance, the function may be computationally expensive to evaluate or low-latency,\egit may involve manually re-configuring a system. This is particularly relevant for analysis optimization in particle physics where evaluatingf​(x)f(x)involves processing large numbers of simulated collisions. Another common use case involves optimizing the hyperparameters of a learning algorithm.

Without any assumptions about the functionf​(x)f(x)this is hopeless; however, if one assumes something about the functions (\egsome notion of smoothness) then one can leverage function evaluations evaluations{f​(xt)}t=1,…,T\{f(x_{t})\}_{t=1,\dots,T}to say something about what value the function might take on at other values ofxx. This is usually cast in Bayesian terms, and Gaussian processes (Section8.2) are often used to model the distribution overf​(x)f(x). The optimization techniques that use this framing are generically referred to as Bayesian optimization[mockus2012bayesian].

Optimization in this context is usually characterized by anexploration-exploitationtradeoff, similar to what is found in multi-arm bandits. Here, exploration refers to function evaluations that characterize the function in regions that haven’t been evaluated, while exploitation refers to evaluations near what is predicted to be its maximum. This setting is similar to reinforcement learning in that it involves sequential decisions (\ie, where to evaluate the function next), but usually the target functionf​(x)f(x)is assumed to be static. In that sense, the state referred to in the language of an MDP is the state of knowledge about the function after sequential evaluations{f​(xt)}t=1,…,T\{f(x_{t})\}_{t=1,\dots,T}. The reward at timettis not the value of the functionf​(xt)f(x_{t}), but some quantity that characterizes what was learned about the function’s maximum. In this literature, one often refers to theacquisition function, which plays a similar role as the expected value of the reward in RL. Common acquisition functions include the probability of improvement, the expected improvement, and an upper-confidence bound[brochu2010tutorial].

## 5.5Active learning

Active learning is closely related to Bayesian optimization, described above. In Bayesian optimization one estimates the functionf​(x)f(x)from some set of evaluations{yt=f​(xt)}t=1,…,T\{y_{t}=f(x_{t})\}_{t=1,\dots,T}; however, the goal is to find the maximumx∗=arg⁡maxx⁡f​(x)x^{*}=\arg\max_{x}f(x). In active learning, the goal is not to find the maximum off​(x)f(x), but to approximate the function as one does in supervised learning. The main difference compared to vanilla supervised learning is that the labeled training dataset isn’t provided a priori in a passive way, but the learning algorithm actively decides where to generate(xt,yt=f​(xt))(x_{t},y_{t}=f(x_{t}))pairs. The functionf​(x)f(x)is sometimes referred to as anoracle. Active learning is particularly attractive when obtaining labeled data is a costly process.

More broadly, a challenge of many machine learning applications is obtaining labeled data, which can be a costly process. If a system could learn from small amounts of data, and choose by itself what data it would like the user to label via an external process called oracle, it would make machine learning more powerful. Such frameworks are also called experiment design or active learning. In active learning, a model is trained on a small amount of data (the initial training dataset), and an acquisition function (often based on the model’s uncertainty) decides on which data points to ask for a label. The acquisition function selects one or more points from a pool of unlabeled data points, with the pool points lying outside of the training dataset. Once we label the selected data points, these are added to the training dataset, and a new model is trained on the updated training dataset. This process is then repeated, with the training dataset increasing in size over time. The advantage of such systems is that they often result in dramatic reductions in the amount of labeling required to train an ML system (and therefore cost and time).

## 6Simulation-based inference

The goal of simulation-based inference (related to, but distinct from, likelihood-free inference) is to extend the statistical procedures described in the Chapter on Statistics (\egparameter estimation, hypothesis tests, confidence intervals, and Bayesian posterior distributions) to the situation where one does not know the explicit likelihoodp​(x|θ)p(x|\theta), the probability of the data given the parametersθ\theta, but has access to a simulator that defines the likelihoodp​(x|θ)p(x|\theta)implicitly[Cranmer:2019eaq,Brehmer:2020cvb]. In a typical setup we
would like to solve the so
called inverse problem
of getting the posterior of the
parameters given the data,p​(θ|x)p(\theta|x), but we cannot
use Bayes theorem directly because
we do not have explicitp​(x|θ)p(x|\theta).

In particle physics and cosmology, the simulators usually use Monte Carlo event generators (see Sec.\crossrefmcgen) to sample unobserved latent variableszz, such as thezpz_{p}phase space of the hard scattering (see Sec.\crossrefkinema:sec:pardecay),zsz_{s}associated to showering and hadronization,zdz_{d}associated to the interaction of particles with the detector
(see Sec.\crossrefpassage), or
initial Gaussian modes of the universe realization. As such, the full simulation chain can be expressed approximately asp​(x|θ)=∫𝑑z​p​(x,z|θ)=∫d​zd​∫d​zs​∫d​zp​p​(x|zd)​p​(zd|zs)​p​(zs|zp)​p​(zp|θ),p(x|\theta)=\int dzp(x,z|\theta)=\int\mathop{}\!\mathrm{d}z_{d}\int\mathop{}\!\mathrm{d}z_{s}\int\mathop{}\!\mathrm{d}z_{p}\,p(x|z_{d})p(z_{d}|z_{s})p(z_{s}|z_{p})p(z_{p}|\theta)\;,(46)

whereθ\thetaare the Lagrangian parameters that dictate the hard scattering. Evaluating the marginal likelihoodp​(x|θ)p(x|\theta)is intractable as it would require evaluating the integral above for each event.

While the marginal likelihood is intractable, simulators provide the ability to generate synthetic dataxi​∼i.i.d.​p​(x|θ)x_{i}\overset{\text{i.i.d.}}{\sim}p(x|\theta)for any value of the parametersθ\theta. One can use a suitable proposal distributionp~​(θ)\tilde{p}(\theta), sampleθi​∼i.i.d.​p~​(θ)\theta_{i}\overset{\text{i.i.d.}}{\sim}\tilde{p}(\theta), generate synthetic dataxi∼p​(x|θi)x_{i}\sim p(x|\theta_{i}), and then assemble a training dataset{xi,θi}i=1,…,n\{x_{i},\theta_{i}\}_{i=1,\dots,n}that can be used to train various machine learning models.

There is thus a close analogy between
simulation-based inference and
data driven machine learning tasks discussed so far, replacingθ\thetawithyy. One difference
is that in simulation-based inference we can always generate new
samples by running additional simulations,
while we typically view training dataset in machine
learning as fixed. This property of
simulation-based inference enables active learning,
where the additional simulations are
chosen such as to minimize the error
on the desired statistical inference task.
Another difference is that we often
have access to the joint likelihoodp​(x,z|θ)p(x,z|\theta), wherezzare unobserved
latent variables333For this reason we prefer to use simulation-based inference instead of likelihood-free inference: joint likelihoodp​(x,z|θ)p(x,z|\theta)is often available, it is the
marginal integral over latent spacezzthat is assumed to be intractable..

Typically in particle physics, one uses histograms or kernel density estimation to model the distribution of observables (low-dimensional summary statistics such as the invariant mass) of simulated data[Diggle1984MonteCM].
Alternatively, one can use an explicit parametric family (such as a falling exponential or a Gaussian distribution) to modelf^​(x|θ)≈p​(x|θ)\hat{f}(x|\theta)\approx p(x|\theta).
That model is then used as as a surrogate for the unknown density implicitly defined by the simulator.
A related approach is known as approximate Bayesian computation (ABC), which approximates the likelihood through an acceptance probability that synthetic data is sufficiently close to the observed data[rubin1984,beaumont2002approximate].
In practice, these techniques are limited to low-dimensional representations of the data.
Thus the potential of recent machine learning approaches to simulation-based inference is to extend this approach to higher-dimensional data, while maintaining the already well-established statistical procedures.

For instance, one can use normalizing flows (see Sec.3.4.3) and the loss functions for density estimation (see Sec.3.3) to learn a surrogate model for the likelihoodf^​(x|θ)≈p​(x|θ)\hat{f}(x|\theta)\approx p(x|\theta)[Cranmer:2016lzt].
Similarly, one can use conditional density estimation to learn a surrogate model for the posteriorf^​(θ|x)≈p​(θ|x)\hat{f}(\theta|x)\approx p(\theta|x), which may involve including the prior-to-proposal ratiop~​(θ)/p​(θ)\tilde{p}(\theta)/p(\theta)[NIPS2016_6084].
In addition to the unsupervised learning techniques, one can also use supervised learning to learn the likelihood-ratior​(x|θ0,θ1)=p​(x|θ0)/p​(x|θ1)r(x|\theta_{0},\theta_{1})=p(x|\theta_{0})/p(x|\theta_{1})by leveraging thelikelihood-ratio trickof Eq.13[Cranmer:2015bka,Brehmer:2018hga].

In some cases one can also augment the training dataset to include the joint likelihood-ratior​(xi,zi|θ0,θ1)≔p​(xi,zi|θ0)/p​(xi,zi|θ1),r(x_{i},z_{i}|\theta_{0},\theta_{1})\coloneqq p(x_{i},z_{i}|\theta_{0})/p(x_{i},z_{i}|\theta_{1})\;,(47)

which can be used to reduce the variance for the squared-error or cross-entropy losses[Brehmer:2018hga,Stoye:2018ovl].
While the marginal likelihoodp​(x|θ)p(x|\theta)is intractable due to the high-dimensional integral over the latent space, the joint likelihood is often tractable since no integration is necessary.

In some cases performing the
marginal integral of Eq.46is
tractable even for high dimensional
latent spacezz.
One of the approaches to make
it feasible in high dimensional
latent space is to
make simulations differentiable with respect
to all of its parameters, global variablesθ\thetaand latent variableszz.
While differentiable simulations have not traditionally been developed for scientific applications, the success of machine learning based on backpropagation combined with gradient descent (see Sec.9.1), has inspired a renewed interest.
One example is FlowPM cosmologicalNN-body simulation, which takes advantage of Mesh-Tensorflow to achieve a GPU-accelerated, distributed, and differentiable simulation[modi2020flowpm].
Availability of simulation gradients in turn
enables gradient based
Monte Carlo Markov chain methods to
perform high dimensional marginal integral over the latent spacezzand over parameter spaceθ\theta[Jasche:2012kq].

Often SBI uses predetermined summary statistics, such as binned histograms in particle physics, or power spectrum in
cosmology, to avoid the curse of dimensionality. It is however possible to
train on uncompressed high dimensional data in cosmology by exploiting the symmetries[2024PNAS..12109624D]. Yet another alternative is to
train the network to search for the
best possible summary statistic.
The summary statistic can then simply beθ^\hat{\theta}, which is the estimate of
the parametersθ\thetathat emerge
from a supervised training on simulations. In SBI these can often be biased even after training, and one possible solution is to form a
pseudo-likelihood to model the bias as a function of the true value ofθ\theta[Ribli_2019].

## 6.1Latent space reconstruction and unfolding

While much of the work on simulation-based inference described above is aimed at inferring the parametersθ\thetaof the simulator, there is work that aims to infer the latent variableszz.
A common approach in particle physics is
to think of the parametersθ\thetaas parameters of a theory, such as masses, coupling constants, or Lagrangian parameters, whilezzmight describe the kinematics of a collision before the detector response.
Inferring the distributionp​(z|{x1,…,xn})p(z|\{x_{1},\dots,x_{n}\})from a dataset of multiple observations is commonly referred to as unfolding in particle physics, and deconvolution in other contexts. Unfolding is a classic inverse problem, and the collection of ideas being used for machine-learning based simulation-based inference are also being applied in this setting[2022JInst..17P1024A].
For example, the OmniFold method[Andreassen:2019cjw]iteratively reweights a dataset in an unbinned way using machine learning to produce a simultaneous measurement of many observables.
In this method, samplesx→r\vec{x}_{r}from detector-level MC simulation are first corrected by a learned weighting functionω​(x→r)\omega(\vec{x}_{r})to match data.
Then, samplesx→p\vec{x}_{p}from particle-level MC simulation are corrected by another learned weighting functionν​(x→p)\nu(\vec{x}_{p})to match theω​(x→r)\omega(\vec{x}_{r})-weighted MC simulation.
The method is iterated multiple times, to achieveν​(x→p)\nu(\vec{x}_{p})-weighted MC events whose event yields and kinematics match those observed in data.
The H1[H1:2021wkz]and ATLAS[ATLAS:2024xxl]Collaborations have used the OmniFold method in experimental measurements.
It has also been applied to T2K[Huang:2025ziq]and CMS[Komiske:2022vxg]open data.

In cosmology, a common task is to
reconstruct initial density distribution of the
dark matter, or its final distribution, from data such as galaxy positions. This can then be used for
various downstream tasks such as
cosmological parameter inference or
making maps of dark matter in our
universe. High dimensional SBI can be used for this
task[2025JCAP...09..039P]. An alternative
is Bayesian inverse problem inference
using the
forward modelg​(z,θ)g(z,\theta), which can be an N-body simulation with some
simple galaxy formation model added to it[Jasche:2012kq,Wang2014a,Seljak2017a].
Standard
Bayesian methodology using for example MCMC can be used to
solve this task and find the posteriorp​(z,θ|x)p(z,\theta|x), which specifies
initial distribution of dark matter. To draw samples of final dark matter
distribution, and of
the reconstructed
data, we can first draw samples from
the posteriorp​(z,θ|x)p(z,\theta|x), and then evaluate forward modelg​(z,θ)g(z,\theta)for each sample.

## 7Data representations, inductive bias, and example applications

In Sec.2we describe the input data as living in an abstract spacexi∈𝒳x_{i}\in\mathcal{X}.
In this section, we briefly discuss some of the common types of structured data that are encountered in physics and refer to the corresponding models classes that have been developed to work with them. We elaborate on the model classes in more detail in the following section.

The most basic and common type of data structure is when𝒳=ℝd\mathcal{X}=\mathbb{R}^{d}. This is often referred to astabular datasince the entire data set{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}can be thought of as a table withnnrows andddcolumns.
It is common to think of an individual entryxix_{i}as a vector indd-dimensional Euclidean space, where the coordinates correspond to the columns of this table.
In some cases individual components ofxix_{i}might be integers or take on only discrete values, in which case describing the space of the data as real-valued is a slight abuse of notation and representation.
For many years this was the dominant type of data in high energy physics as it is a natural input type for shallow neural networks, multilayer perceptrons, support vector machines, and tree-based methods found in popular tools such asTMVA[Hocker:2007ht].

For categorical data, one typically uses a numerical representation such asinteger encodingwhere different categories are mapped to integers with a corresponding dictionary. Another common representation of categorical data is based on the so-calledone-hot encoding(aka ‘one-of-K’ or ‘dummy’), in which case the category is mapped to akk-dimensional binary vector wherekkis the number of categories and each component of this vector corresponds to a particular category.
In the one-hot encoding, only one of the components is non-zero.
Finally, there are approaches in one learns anembeddingthat maps discrete categories intoℝd\mathbb{R}^{d}; an example of this isWord2Vec[mikolov2013efficient].
Interestingly, such embeddings can preserve various types of semantics; for instance, the vectorwalking - walkis similar to the vectorswimming - swamas are the vectors connecting countries and their capital cities.
This allows for a loose sense of algebra on the word embeddings such aswalking - swimming + swam = walk.
Similar types of embeddings have also been used in a number of scientific use-cases including biological sequences (\eg, DNA, RNA, and proteins) for bioinformatics applications[asgari2015continuous].

Particle physics data often is represented with an extension of the simple tabular data structure where the number of columns is not fixed. For instance, if the rows correspond to data for individual collisions, the number of electrons (and positrons) reconstructed in the event is variable. Thus the number of columns needed to represent the energy, momentum, and charge of these particles is also variable. A common solution to this problem is to fix a maximum number of particles and thentruncateandzero-padto fit the data into a fixed tabular representation, though this is not the natural representation of the data and it leads to a loss of information.

Sequential datais also commonly encountered in physics (\egin time series). Here an individual entryxi=(xi1,…,xit,…​xiTi)x_{i}=(x_{i}^{1},\dots,x_{i}^{t},\dots x_{i}^{T_{i}})wherettis index for the ordered sequence,TiT_{i}is the length of the sequence (which might be variable), and the data associated to each “time”xit∈ℝdx_{i}^{t}\in\mathbb{R}^{d}.
This is similar to the previous example where the energy, momentum, and charge of thettth electron in theiith event would bexitx_{i}^{t}and the electrons might be sorted according to their energy or transverse momentum.
Sequential data is also encountered in natural language processing, wherexitx_{i}^{t}correspond to individual words in a sentence. Recurrent neural networks (see Sec.8.4.5) are particularly well suited to sequential data.
Examples applications from the Living Review include Refs.[Guest:2016iqz,Nguyen:2018ugw,Bols:2020bkb,goto2021development,deLima:2021fwm,ATL-PHYS-PUB-2017-003].

Image-like datais one of the most dominant forms of data in industrial applications of deep learning, is very relevant for astronomy and cosmology, and also appears in particle physics in various forms. Image-like data typically involvesdd-dimensional features associated to a regular grid or lattice that does not vary across the individual instancesxix_{i}. The canonical example is a standard image from a camera withW×HW\times Hpixels where theppth pixel has dataxip∈ℝ3x_{i}^{p}\in\mathbb{R}^{3}corresponding to the threechannelsin the RGB color model. It is important to recognize that the data corresponding to the 2-dimensional image is not 2-dimensional; instead, it is(W×H×c)(W\times H\times c)-dimensional, whereccis the number of channels. In astronomy, an image may be grey scale (c=1c=1) or there may be morechannels(c>3c>3) corresponding to different color filters. In other applications, the grid or lattice might be 3- or 4-dimensional. For example, the data associated to a regularly segmented calorimeter can be thought of as a 3-dimensional image and the data associated to a lattice simulation of a classical or quantum system can be thought of as a 4-dimensional image. Convolutional neural networks, described in Sec.8.4.4, are particularly well suited to image-like data. Example applications from the Living Review include Refs.[Pumplin:1991kc,Cogan:2014oua,Almeida:2015jua,deOliveira:2015xxd,ATL-PHYS-PUB-2017-017,Lin:2018cin,Komiske:2018oaa,Barnard:2016qma,Komiske:2016rsd,Kasieczka:2017nvn,Macaluso:2018tck,li2020reconstructing,li2020attention,Lee:2019cad,collado2021learning,Du:2020pmp,Filipek:2021qbe,Nguyen:2018ugw,ATL-PHYS-PUB-2019-028,Andrews:2018nwy,Chung:2020ysf,Du:2019civ,Andrews:2021ejw,Pol:2021iqw].

It is also possible that the data (or features) associated to one “pixel” or lattice site may itself be structured. For example, the single read-out plane of a liquid argon time projection chamber (LArTPC) may involve a 1-dimensional or 2-dimensional grid, but the data associated to each “pixel” is itself a sequence or waveform. Example applications in neutrino physics from the Living Review include Refs.[Aurisano:2016jvx,Acciarri:2016ryt,Hertel:DLPS2017,Adams:2018bvi,Domine:2019zhm,Aiello:2020orq,Adams:2020vlj,Domine:2020tlx,DeepLearnPhysics:2020hut,Koh:2020snv,Yu:2020wxu,Psihas:2020pby,Alonso-Monsalve:2020nde,Abratenko:2020pbp,Clerbaux:2020ttg,Liu:2020pzv,Abratenko:2020ocq,Chen:2020zkj,SBND:2020eho,Qian:2021vnh,abbasi2021convolutional,Drielsma:2021jdv,Rossi:2021tjf,Hewes:2021heg,Acciarri:2021oav,Belavin:2021bxb,Maksimovic:2021dmz,Gavrikov:2021ktt,Garcia-Mendez:2021vts,Carloni:2021zbc,MicroBooNE:2021nss]. Similarly, in lattice quantum chromodynamics, the data associate to a particular site (or link) would be group valued (\egxip∈S​U​(3)x_{i}^{p}\in SU(3)as in Refs.[Boyda:2020hsi,Kanwar:2020xzo]).

Both sequential and image-like data have a notion of temporal or spatial structure. While it is possible to unroll an image into a(W×H×c)(W\times H\times c)-dimensional vector, that would erase the spatial structure and obfuscate the fact that nearby pixels are highly correlated. Similarly, one could permute the time index for sequential data, but that would destroy the temporal structure of the data. The complementary point of view is that the model class should also be aware of the structure of the data. Recurrent and convolutional neural networks are good examples ofinductive biasas the models incorporate the structure of the data. In some cases this can be formalized in terms of symmetry. For example, if we train model to classify images of cats and dogs, we would like it’s prediction to be invariant to where in the image the cat is. This type of translational invariance can be enforced in the design of the model class.

While permuting the elements of a sequence destroys the temporal structure of a time series, attaching a temporal indexttto a set of objects with featuresxitx_{i}^{t}can also be problematic. If the data corresponding toxix_{i}are really a set{xi1,…,xiTi}\{x_{i}^{1},\dots,x_{i}^{T_{i}}\}(\eg, a point cloud), then we would like the output of the model to bepermutation invariantorpermutation equivariantdepending on if the output is per-set or per-element, respectively. A standard sequential or convolutional model will not generally be permutation invariant, but models such as deep sets, various types of graph neural networks, and transformers can be made to enforce permutation symmetry.
Example applications from the Living Review include Refs.[Komiske:2018cqr,Qu:2019gqs,Mikuni:2020wpr,Shlomi:2020ufi,Dolan:2020qkr,Fenton:2020woz,Lee:2020qil,collado2021learning,Mikuni:2021pou,Shmakov:2021qdz,Shimmin:2021pkm,ATL-PHYS-PUB-2020-014,Qu:2022mxj].

The temporal and spatial structure of sequences and image like data can also be generalized. For instance, a 1-dimensional sequence can be generalized to a tree structured data like one finds in the hierarchical clustering of jets or as in a directed-acyclic graph (DAG). Generalizations of recurrent neural networks have been constructed that can operate over these more complex data structures[Louppe:2017ipp,Cheng:2017rdo]. More generally, one can considered graph-structured data composed of nodes and edges or multi-graphs that group together three nodes into faces orkknodes intokk-edges. Graph neural networks are a class of models that work with this type of data. The emerging subfield of geometric deep learning aims to unify the notation, terminology, and theory that connect these considerations of the structure of the data and the corresponding model architecture. Example applications in the Living Review include Refs.[Henrion:DLPS2017,Ju:2020xty,Abdughani:2018wrw,Martinez:2018fwc,Ren:2019xhp,Moreno:2019bmu,Qasim:2019otl,Chakraborty:2019imr,Chakraborty:2020yfc,1797439,1801423,1808887,Iiyama:2020wap,1811770,Choma:2020cry,Alonso-Monsalve:2020nde,guo2020boosted,Heintz:2020soy,Verma:2020gnq,Dreyer:2020brq,Qian:2021vnh,Pata:2021oez,Biscarat:2021dlj,Rossi:2021tjf,Hewes:2021heg,Thais:2021qcb,Dezoort:2021kfk,Verma:2021ceh,Hariri:2021clz,Belavin:2021bxb,Atkinson:2021nlt,Konar:2021zdg].

If the data are expected to have a symmetry associated to them but one is working with a model class that does not enforce this symmetry, thendata augmentationis a common procedure used to improve generalization performance. Here one starts with an initial dataset{xi}i=1,…,n\{x_{i}\}_{i=1,\dots,n}and produces an augmented dataset{xi′}i′=1,…,n′\{x_{i}^{\prime}\}_{i^{\prime}=1,\dots,n^{\prime}}through some data augmentation strategy. For example, one might apply a random rotationRi′R_{i^{\prime}}to an image to producexi′=Ri′​(xi)x_{i}^{\prime}=R_{i^{\prime}}(x_{i})if one assumes rotational invariance in the underlying problem.

In some cases some of the individual features (components) ofxxare functions of other features. For instance, one may include components of a four-vector(E,px,py,pz)(E,p_{x},p_{y},p_{z})as well as redundant information such as transverse momentum, azimuthal angles, rapidity, etc. In this case, the data is restricted to a lower-dimensional surface embedded in𝒳\mathcal{X}. Even if the features aren’t redundant, statistically the data are often effectively restricted to a small subspace of statistically likely samples and those that are exceedingly unlikely. For instance, the space of natural images is a small and highly structured subspace of all possible images, which are dominated by what we would perceive visually as noise. The termdata manifoldis used to describe this restricted subspace where the data are to be found, even though it does not necessarily satisfy the formal requirements of a manifold in the mathematical sense.

These considerations on the structure of the data not only apply not to the input dataxi∈𝒳x_{i}\in\mathcal{X}, but also to the output datayi∈𝒴y_{i}\in\mathcal{Y}. For instance, one might want a sequence-to-sequence model as in machine translation of written text[bff0e6bd8f4a4f0d9735bf1728fb43ef]or to learn a function that takes sets as input and produces graphs as output as in the Set2Graph mode[NEURIPS2020_fb4ab556]. One might also want the input and output of the model to be different in representations of an underlying symmetry group and for the model to enforce group-equivariance[Boyda:2020hsi,Kanwar:2020xzo]. The development of the necessary modeling components to enable practitioners to compose and train these types of models is a significant development for the field of physics.

## 8Flavors of ML models

## 8.1Support vector machines

Support vector machines (SVMs) are a class of supervised learning models used for classification and regression. The learning algorithm involves a convex optimization problem that has a unique solution and can be solved with quadratic programming techniques. In this sense, they are robust and easier to characterize than neural networks that involve non-convex optimization.

Linear support vector machines are used for binary classification, where𝒳=ℝd\mathcal{X}=\mathbb{R}^{d}and the target labels are conventionally defined as𝒴={−1,1}\mathcal{Y}=\{-1,1\}. The classification is simply based on which side of a hyperplane the data lie. Any hyperplane can be written as the set of pointsxxsatisfyingwT​x−b=0{\displaystyle{w}^{T}{x}-b=0}, wherew,b∈ℝdw,b\in\mathbb{R}^{d}are the parameters of the model. The vectorwwis normal to the hyperplane, but not necessarily normalized. The quantityb‖w‖{\tfrac{b}{\|{w}\|}}quantifies the offset of the hyperplane from the origin along the normal vectorww.

If the training dataset is linearly separable, then there is a region bounded by two parallel hyperplanes, called themargin, that separate the two classes of data. The maximum margin classifier is uniquely defined by making the distance between these two hyperplanes as large as possible. The boundaries of the margin can be defined bywT​xi−b=±1{\displaystyle{w}^{T}{x}_{i}-b=\pm 1}, and the width of the margin is given by2‖w‖{\tfrac{2}{\|{w}\|}}. Figure8.1illustrates this forx∈ℝ2x\in\mathbb{R}^{2}.{pdgxfigure}

Illustration of a maximum margin classifier for a linear support vector machine in the separable case.

Since the width of the margin is maximized when‖w‖\|w\|is minimized, we can state the goal of the (hard) maximum-margin classifier in the linear separable case as the following constrained optimization problem:
Minimize‖w‖2\|{w}\|^{2}subject to the constraintyi​(wT​xi−b)≥1{\displaystyle y_{i}({w}^{T}{x}_{i}-b)\geq 1}fori=1,…,n.i=1,\ldots,n.Thewwandbbthat solve this problem uniquely determine the resulting classifier,y^​(x)=sgn⁡(wT​x−b)\hat{y}(x)=\operatorname{sgn}({w}^{T}{x}-b).
This geometric description makes it clear that the maximum-margin hyperplane is completely determined by thosexi{{x}}_{i}that lie nearest to it: the eponymoussupport vectors.

## 8.2From Bayesian linear regression to kernel regression and Gaussian processes

As discussed in Sec.2.2,
linear
regression is a specific case of
regression
where the solution is parameterized as
a linear combination of basis
functionsϕ​(x)\phi(x),fϕ​(x)=∑kwk​ϕk​(x)=w⊺​ϕ,f_{\phi}(x)=\sum_{k}w_{k}\phi_{k}(x)=w^{\intercal}\phi,(48)

using a short-hand vector
notation. If we aggregate all the basis functions of the training data intoΦ​(x)\Phi(x)and allxxintoXX, and assuming a
Gaussian noise modelϵ∼𝒩​(0,σn2)\epsilon\sim\mathcal{N}(0,\sigma_{n}^{2}), we can write
the noise probability distribution asp​(y|X,w)=𝒩​(w⊺​Φ,σn2​I).p(y|X,w)=\mathcal{N}(w^{\intercal}\Phi,\sigma_{n}^{2}I).(49)

In overparametrized models,
this needs to be regularized,
with explicit L2 norm of the weights, as discussed in Sec.2.5.
If we view the process in the Bayesian context, we add a weight priorp​(w)=𝒩​(0,Σp)p(w)=\mathcal{N}(0,\Sigma_{p})to the
data likelihood.
With this one can define the
posterior of the weights asp​(w|X,y)∝p​(y|X,w)​p​(w)=𝒩​(σn−2​A−1​Φ​y,A−1),p(w|X,y)\propto p(y|X,w)p(w)=\mathcal{N}(\sigma_{n}^{-2}A^{-1}\Phi y,A^{-1}),(50)

whereA=σn−2​Φ​Φ⊺+Σp−1A=\sigma_{n}^{-2}\Phi\Phi^{\intercal}+\Sigma_{p}^{-1}.

Our main task is not to predict the weights
themselves, but to predictf∗f^{*}given somex∗x^{*}.
In the Bayesian view,
one must model average over the weights,p​(f∗|x∗,X,y)=∫d​w​p​(f∗|x∗,w)​p​(w|X,y)=𝒩​(σn−2​ϕ​(x∗)⊺​A−1​Φ​y,ϕ​(x∗)T​A−1​ϕ​(x∗)),p(f^{*}|x^{*},X,y)=\int\mathop{}\!\mathrm{d}wp(f^{*}|x^{*},w)p(w|X,y)=\mathcal{N}(\sigma_{n}^{-2}\phi(x^{*})^{\intercal}A^{-1}\Phi y,\phi(x^{*})^{T}A^{-1}\phi(x^{*})),(51)

where we usedp​(f∗|x∗,w)=N​(0,σn2)p(f^{*}|x^{*},w)=N(0,\sigma_{n}^{2}).
This can be rewritten asp(f∗|x∗,X,y)=𝒩(ϕ(x∗)TΣpΦ(K+σn2I)−1y,ϕ(x∗)⊺Σpϕ(x∗))−ϕ(x∗)ΣpΦ(K+σn2I)−1ΦTΣpϕ(x∗)),p(f^{*}|x^{*},X,y)=\mathcal{N}(\phi(x^{*})^{T}\Sigma_{p}\Phi(K+\sigma_{n}^{2}I)^{-1}y,\phi(x^{*})^{\intercal}\Sigma_{p}\phi(x^{*}))-\phi(x^{*})\Sigma_{p}\Phi(K+\sigma_{n}^{2}I)^{-1}\Phi^{T}\Sigma_{p}\phi(x^{*})),(52)

whereK=ΦT​Σp​ΦK=\Phi^{T}\Sigma_{p}\Phi.
In general we callk​(x,x′)=ϕT​(x)​Σp​ϕ​(x′)k(x,x^{\prime})=\phi^{T}(x)\Sigma_{p}\phi(x^{\prime})a kernel or covariance function betweenxxandx′x^{\prime}.
The final expression for the regression mean and covariance has a
formf∗=K​(x∗,X)​[K​(X,X)+σn​I]−1​y,f^{*}=K(x^{*},X)[K(X,X)+\sigma_{n}I]^{-1}y,(53)

with covariancecov​(f∗)=K​(x∗,x∗)−K​(x∗,X)​[K​(X,X)+σn2​I]−1​K​(x∗,X).\mathrm{cov}(f^{*})=K(x^{*},x^{*})-K(x^{*},X)[K(X,X)+\sigma_{n}^{2}I]^{-1}K(x^{*},X).(54)

One can see that the prediction
takes the observed valuesyyat the
training dataXX, and predicts the value atx∗x^{*}by incorporating
the strength of their correlations
viaK​(x∗,X)K(x^{*},X). In addition, the
prediction also suppresses the
training points with a small inverse covariance, a generalization
of inverse noise weighting.

This expression simply rewrites the standard Bayesian
regression, and the kernel is
still defined as an inner product
of the regression basis functionsϕ​(x)\phi(x)with respect toΣp\Sigma_{p}. However, the kernel
can be replaced by any kernel form that
describes the level of correlations
betweenxxandx′x^{\prime}, a process known as thekernel trick. A general
condition for the kernel to be
valid is that the covariance
matrix is always invertible.
In a Gaussian
process the kernel is often stationary, defined ask​(x,x′)=f​(|x−x′|)k(x,x^{\prime})=f(|x-x^{\prime}|). This and many
other kernels
cannot be related to a finite
set of basis functionsϕ​(x)\phi(x),
which is why it is often stated that Gaussian process corresponds to an infinite
basis function expansion.
Yet another form of the kernels
are neural tangent kernels of neural networks in the infinitely wide network limit[JacotHG18].

Another path to Gaussian processes
is via kernel regression, where one makes kernel regression
Bayesian[bishop2006pattern].
Standard kernel regression, also called
Nadaraya-Watson regression, is of
the formf∗=∑xk​(x,x∗)​y​(x)/∑xk​(x,x∗)f^{*}=\sum_{x}k(x,x^{*})y(x)/\sum_{x}k(x,x^{*}),
which can be interpreted as a soft
version of thekk-nearest neighbors algorithm.
Bayesian kernel regression in the form of a Gaussian process replaces kernel sums with matrix operations, and
is closer to linear regression than
to the nearest neighbor methods.

One advantage of Gaussian process is that one can work with a family of kernel functions parameterized by some hyperparametersη\eta. One can then optimize the hyperparameters via gradient-ascent on the marginal likelihood function. In contrast, hyperparameter tuning in other models typically requires a grid search or some other black-box optimization procedure evaluated on held out data or some form of cross-validation.

While we only describe Gaussian process regression, there is a corresponding Gaussian process classification.
Rasmussen and Williams provides an excellent review of Gaussian processes[williams2006gaussian]. Numerically, Gaussian process libraries are confronted with computing the inverse of the covariance kernel, which scales like𝒪​(n3)\mathcal{O}(n^{3})in computational complexity.
Gaussian
processes are often used as
emulators or surrogate models, specially in the context of low dimensional inputxxand low number of training datannto avoid the steep𝒪​(n3)\mathcal{O}(n^{3})scaling. They
are used widely in cosmology, and there are a growing number of applications in (astro-)particle physics[Gandrakota:2022wyl].
Recent works explore the design of physics-inspired kernels and use Gaussian processes to model the intensity for a Poisson point process like those found in experimental particle physics andγ\gamma-ray and X-ray astronomy[Frate:2017mai,Mishra-Sharma:2020kjb,Foster:2021ngm].
Gaussian processes are also extensively
used in Bayesian
optimization (Section5), because the
uncertainty quantification that
is automatically provided by the Gaussian process enables exploration-exploitation strategies where
to evaluate the function next.

## 8.3Decision trees

## Tree-based models

Classification and regression trees (CART) typically partition the input space intoJJdisjoint regions𝒳=𝒳1∪⋯∪𝒳J\mathcal{X}=\mathcal{X}^{1}\cup\cdots\cup\mathcal{X}^{J}through a sequence ofJ−1J-1binary splits based on an individual components ofx∈𝒳x\in\mathcal{X}(\egx4<0.7x_{4}<0.7)[Breiman1984ClassificationAR]. The model is piecewise constant and assigns the valuebj∈𝒴b_{j}\in\mathcal{Y}to thejjth terminal region𝒳j\mathcal{X}^{j}.
The model can be writteny^​(x)=fϕ​(x)=∑jbj​𝟏​(x∈𝒳j).\hat{y}(x)=f_{\phi}(x)=\sum_{j}b_{j}\mathbf{1}(x\in\mathcal{X}^{j})\;.(55)

The parametersϕ\phiof the model comprise the components index and thresholds for the successive splittings and the coefficientsbjb_{j}.

Tree learning refers to the algorithm used to choosing the tree structure and determining the predictions at leaf nodes. Optimization of the tree structure involves a difficult discrete optimization since the change in the loss with respect to the tree structure is non-differentiable and it is intractable to explore the combinatorially large space of possible trees with brute force. Therefore, the discrete optimization component of tree learning typically involves some approximate algorithm based on heuristics. In contrast, optimization of thebjb_{j}for a given tree structure can exploit gradient-based optimization algorithms.

Common approaches to building the decision tree start with a root node and grow with splits based on individual attributes (components ofxx). These are referred to as top-down induction strategies. There are various impurity heuristics used for choosing the best attribute to split on such as the Gini index, cross-entropy and mis-classification error. Generally they aim to find a split that will refine the the terminal nodes such that they have higher purity than the parent node.

Because most tree learning algorithms consider splits aligned with individual feature components, there are some failure modes for tree-based models. However, tree-based models work well with tabular data composed of a mix of continuous and discrete features. Tools such asXGBoost[xgboost]and LightGBM[lightgbm]are competitive on tabular data benchmarks like TabArena[tabarena]and are widely used in industry; the boosted decision trees (BDTs) implemented in
StatPatternRecognition[Narsky:2005xpa]andTMVA[Hocker:2007ht]have been one of the most used techniques in particle physics[Radovic:2018dip].

Individual trees are often referred to as weak learners and they can be combined in various ways described below. Regularization is also an important consideration with tree-based models as one can always learn a tree that assigns exactly one training dataset point per terminal node and memorize the training dataset exactly. One approach to this is calledpre-pruning, which simply terminates the growing of the trees if the number of training samples reaching the terminal node drops below some threshold, the purity of a terminal nodes is below some threshold, or if the improvement in purity due to a proposed split is not above a threshold. Another regularization approach is calledpost-pruning, which uses a validation data set that is disjoint from the training dataset to probe generalization performance. In this approach, after initially growing a tree with the training dataset, a sequence of pruned trees is considered where splits are removed based on some heuristic. The tree in this sequence of pruned trees that minimizes the generalization error on the validation set is chosen. Alternatively, in tools such asXGBoostthere is an explicit regularization term included in the loss function (see Eq.62).

## Ensemble methods

The idea of ensemble methods is to combine multiple models into a more performant one by exploiting the bias-variance tradeoff[louppe2014understanding]. This is most commonly achieved through averaging (\egbagging and random forests), which primarily reduces variance, or boosting (\eg, AdaBoost and gradient boosting), which primarily reduces bias. Here, bias refers to the difference between the Bayes optimal model and the average model produced by the learning procedure with different training sets and variance quantifies how much the learned model varies from one training set to another.

The motivation of boosting is to combine the outputs of many “weak” models to produce a more expressive model. Compared to averaging techniques like bagging and random forests, the model is built sequentially on modified versions of the data and the final predictions are combined through a weighted sumy^​(x)=∑t=1Tβt​y^t​(x),\hat{y}(x)=\sum_{t=1}^{T}\beta_{t}\hat{y}_{t}(x)\;,(56)

whereβt\beta_{t}expand the parameters of the modelϕ\phi.

## Bagging

The idea behind bagging (bootstrap aggregation) is to createTTbootstrap training datasetsB1,…,BTB_{1},\dots,B_{T}drawn from the training dataset{xi,yi}i=1,…,n\{x_{i},y_{i}\}_{i=1,\dots,n}, then learn a modely^t\hat{y}_{t}for each, and finally construct an average modely^​(x)=(1/T)​∑ty^t​(x)\hat{y}(x)=(1/T)\sum_{t}\hat{y}_{t}(x). If one hadTTindependent training datasets each of sizenn, then the bias of the average model would be the same as the original model, but the variance would be reduced by a factor ofTT. By using bootstrap resampling, the bias may increase but the reduction in variance often dominates, which leads to improved performance.

## Random forests

Random forests refers to a type of “perturb and combine algorithm” that combines bagging and random attribute subset selection. Again one builds treesy^t​(x)\hat{y}_{t}(x)from bootstrap training datasetsBtB_{t}, but instead of choosing the best split among all attributes, one select the best split among a random subset ofkkattributes. Ifkkincludes all attributes, then it is equivalent to bagging.

## AdaBoost

In AdaBoost (adaptive boost) the sequence of treesy^1,…,y^T\hat{y}_{1},\dots,\hat{y}_{T}are trained with reweighted versions of the original training dataset such that the weight of individual training sample is based on the prediction error in the previous iteration[freund1997decision]. This requires working with a loss function that and learning procedure for the individual iterations that is amenable to weighted training dataset{xi,yi,wi}i=1,…,n\{x_{i},y_{i},w_{i}\}_{i=1,\dots,n}. Incorporating the weightswiw_{i}is straight forward when the risk is expressed as an expectation, since the emperical risk of Eq.3is just replaced with the weighted average. Similarly, the heuristic for many of the tree-based learning algorithms (\egthe Gini index) also have natural generalizations with weighted events.

In the context of classification, the weighted error of the modely^t​(x)\hat{y}_{t}(x)iserrt=∑iwi(t)​𝟏​[yi≠y^t​(xi)]∑iwi(t).\textrm{err}_{t}=\frac{\sum_{i}w_{i}^{(t)}\mathbf{1}[y_{i}\neq\hat{y}_{t}(x_{i})]}{\sum_{i}w_{i}^{(t)}}\;.(57)

Based on this weighted error, the coefficientβt\beta_{t}of the componenty^t​(x)\hat{y}_{t}(x)in Eq.56is given byβt=log⁡(1−errterrt).\beta_{t}=\log\left(\frac{1-\textrm{err}_{t}}{\textrm{err}_{t}}\right)\;.(58)

Then for the next iteration the weights of the misclassified events are updated asw(t+1)=w(t)​exp⁡(βt)w^{(t+1)}=w^{(t)}\exp(\beta_{t})and then renormalized so that the sum of all weights is 1. This reweighted dataset is then used to train the next modely^t+1​(x)\hat{y}_{t+1}(x)and the entire procedure is initialized with uniform weightswit=0=1/nw_{i}^{t=0}=1/n.

There is an analogous procedure for regression with the squared loss function based on the residualsri=yi−y^t​(xi)r_{i}=y_{i}-\hat{y}_{t}(x_{i})(see for example Ref.[Hocker:2007ht]for details).

## Gradient boosting

One of the most powerful forms of tree based models, which is implemented in the toolXGBoostis referred to asgradient boosting[friedman2001greedy]. In this setup, the model is purely additive as in the case of random forests, so the model is Eq.56with allβt=1\beta_{t}=1. Note this is without loss of generality since theβt\beta_{t}can be absorbed into thebjb_{j}of Eq.55. As with AdaBoost, the model is built sequentially through the sequencey^1,…,y^T\hat{y}_{1},\dots,\hat{y}_{T}.

At each iteration, a new termftf_{t}will be added to the sum in Eq.56. For a given decision tree defined by splits on attributes, one can approximate the objective function (the loss functionℒ\mathcal{L}plus a regularization termΩ\Omega) as a function ofbjb_{j}in a second order Taylor series:obj(t)=∑i=1n[ℒ​(yi,y^i(t−1))+gi​ft​(xi)+12​hi​ft2​(xi)]+Ω​(ft)+constant,\text{obj}^{(t)}=\sum_{i=1}^{n}[\mathcal{L}(y_{i},\hat{y}_{i}^{(t-1)})+g_{i}f_{t}(x_{i})+\frac{1}{2}h_{i}f_{t}^{2}(x_{i})]+\Omega(f_{t})+\mathrm{constant}\;,(59)

wheregi=∂y^i(t−1)ℒ​(yi,y^i(t−1))g_{i}=\partial_{\hat{y}_{i}^{(t-1)}}\mathcal{L}(y_{i},\hat{y}_{i}^{(t-1)})(60)

andhi=∂y^i(t−1)2ℒ​(yi,y^i(t−1))h_{i}=\partial_{\hat{y}_{i}^{(t-1)}}^{2}\mathcal{L}(y_{i},\hat{y}_{i}^{(t-1)})\;(61)

InXGBoost, the regularization term is taken to beΩ​(f)=γ​J+12​λ​∑j=1Jbj2,\Omega(f)=\gamma J+\frac{1}{2}\lambda\sum_{j=1}^{J}b_{j}^{2}\;,(62)

whereJJis the number of terminal nodes in the tree. With the second-order approximation of the objective, one can directly solve for the optimalbjb_{j}for the next tree and the corresponding value of the optimized objective function. The improvement in the objective function can then be used as a heuristic for choosing the best split. Specifically, defineGj=∑i∈IjgiG_{j}=\sum_{i\in I_{j}}g_{i}andHj=∑i∈IjhiH_{j}=\sum_{i\in I_{j}}h_{i}, whereIjI_{j}is the set of indices of data points assigned to thejjth leaf. The heuristic used inXGBoostfor splitting a node isGain=12​[GL2HL+λ+GR2HR+λ−(GL+GR)2HL+HR+λ]−γ.\textrm{Gain}=\frac{1}{2}\left[\frac{G_{L}^{2}}{H_{L}+\lambda}+\frac{G_{R}^{2}}{H_{R}+\lambda}-\frac{(G_{L}+G_{R})^{2}}{H_{L}+H_{R}+\lambda}\right]-\gamma\;.(63)

This formula can be interpreted as the score on the new left leaf plus the score on the new right leaf minus the score on the original leaf minus a regularization penalty on the additional leaf. If the gain from splitting a leaf is smaller thanγ\gamma, then the total Gain is negative and the split will not be added, which can be seen as implementing a form of pruning.

## 8.4Neural networks

In this section we focus on the different types of components used in modern neural network architectures.
Gradient-based optimization techniques are most commonly used for training neural networks, and they are described in Sec.9.1. Similarly, other important aspects to effectively training neural network models such as parameter initialization and early stopping are discussed in Sec.9.

The vanishing and exploding gradient problem is a common challenge for gradient-based optimization of neural networks and is described in Sec.9.5.
That problem is referred to repeatedly in this section because it has motivated the development of numerous architectural components described below.

## 8.4.1Feed-forward multilayer perceptron

One of the core components in neural networks is the fully-connected, feedforward network ormultilayer perceptron(MLP), which is composed ofLLlayers:f=f(L)∘⋯∘f(1)f=f^{(L)}\circ\dots\circ f^{(1)}. Thellth layer defines a function that maps adl−1d_{l-1}-dimensional input vector, calledfeatures, to andld_{l}-dimensional outputf(l):ℝdl−1→ℝdlf^{(l)}:\mathbb{R}^{d_{l-1}}\to\mathbb{R}^{d_{l}}. A unit producing an individual component of thedld_{l}-dimensional output is called aneuronor afilterinterchangeably. Forl<Ll<L, the functionsflf_{l}are called hidden layers, and the number of neurons (dld_{l}) is referred to as the width of the hidden layers. The layers in an MLP take on the form:f(l)​(u)=σ(l)​(W(l)​u+b(l)),f^{(l)}(u)=\sigma^{(l)}(W^{(l)}u+b^{(l)})\;,(64)

whereW(l)∈ℝdl×dl−1W^{(l)}\in\mathbb{R}^{d_{l}\times d_{l-1}}is called theweight matrix, the components of the vectorb(l)∈ℝdlb^{(l)}\in\mathbb{R}^{d_{l}}are referred to as thebiases,u∈ℝdl−1u\in\mathbb{R}^{d_{l-1}}is the input from the previous layer,W(l)​uW^{(l)}udenotes a matrix-vector product, andσ(l)\sigma^{(l)}is a non-linearactivation functionthat is usually applied element-wise. The parameters of the network comprise the full collection of weights and biases,ϕ=(W(1),…,W(L),b(1),…,b(L))\phi=(W^{(1)},\dots,W^{(L)},b^{(1)},\dots,b^{(L)}).

## 8.4.2Activation functions

The activation functionsσ\sigmain neural networks are nonlinear functions and key to the expressiveness of the resulting family of functions. Two traditionally used functions are thelogistic or sigmoidfunctionσ​(x)=1/(1+e−x)\sigma(x)=1/(1+e^{-x})andhyperbolic tangentfunctiontanh⁡(x)=(ex−e−x)/(ex+e−x)\tanh(x)=(e^{x}-e^{-x})/(e^{x}+e^{-x}). These functions
are bounded to be(0,1)(0,1)and(−1,1)(-1,1)respectively, and are symmetric about the input value of zero. On the other hand, away from the zero input value, a gradient of both functions quickly vanishes and this poses a challenge in using gradient-based optimization method (see Sec.9.1). This can be avoided, to some extent, by normalizing the input values and carefully initializing the values ofW(l)W^{(l)}andb(l)b^{(l)}. These are discussed in Sec.9.7,9.8and9.9. Yet, it becomes difficult to maintain a null input value for adeepneural network, a model with many layers. Instead, a popular choice for a deep neural network is therectified linear unit(ReLU):ReLU​(x)={xifx>00otherwise\text{ReLU}(x)=\begin{cases}x&\text{if $x>0$}\\
0&\text{otherwise}\end{cases}(65)

whose computational cost is small and ensures that the gradient does not vanish forx∈(0,+∞)x\in(0,+\infty)[Fukushima1980,Nair2010RectifiedLU]. An alternative to preserve a non-zero gradient in negative input values are calledleaky ReLUand modifies the output to0.01​x0.01xforx∈(−∞,0)x\in(-\infty,0)[Maas13rectifiernonlinearities]. Another variant, calledparametric ReLU(PReLU), turns the coefficient0.010.01into a variable that is optimized as a part of the model during optimization[He2015DelvingD].

The choice of activation functions depends on the model architecture and applications. As described, while the use of ReLU types are a typical choice for a deep neural network,
a logistic function is a popular choice at the final layer for classification tasks.
In the area of neural scene representation, sinusoidal activation functions have been found to be surprisingly effective[sitzmann2019siren].

Recently, additional smooth loss functions have been found to work well with larger models, such as the Gaussian-error linear unit (GELU)[hendrycks2023gaussianerrorlinearunits],GELU​(x)=12​(1+erf​(x2))\text{GELU}(x)=\frac{1}{2}\left(1+\text{erf}\left(\frac{x}{\sqrt{2}}\right)\right)(66)

and
swish function[ramachandran2017searchingactivationfunctions]swishβ​(x)=x1+e−β​x,\text{swish}_{\beta}(x)=\frac{x}{1+e^{-\beta x}},(67)

which smoothly interpolates between a linear function (β=0\beta=0) and ReLU (β=∞\beta=\infty).
In addition, the value ofβ=1\beta=1corresponds to the sigmoid-weighted linear unit (SiLU)[elfwing2017sigmoidweightedlinearunitsneural].

## Softmax

A softmax function is often used to normalize elements of a discrete vectoruu, or to interpret the output as a probability over a set ofnndiscrete categories.
Given a real-valued input vectoru∈ℝnu\in\mathbb{R}^{n}, the softmax function computes the output vectorv∈ℝnv\in\mathbb{R}^{n}theiith component is given by:vi=exp⁡(ui)∑j=1nexp⁡(uj).v_{i}=\frac{\exp({u_{i}})}{\displaystyle\sum_{j=1}^{n}\exp({u_{j}})}\;.(68)

The result has the property thatvi∈(0,1)v_{i}\in(0,1)and∑vi=1\sum v_{i}=1. The components of the input vectoruuare often referred to aslogitsin reference to their connection to the logistic function used in logistic regression. The softmax function is commonly used as the last layer in multi-class classifier. The softmax is also used in the context of attention (see Sec.8.4.6).

## 8.4.3Universal approximation and deep learning

There are a number of universal approximation theorems in the theory of neural networks.
One of the first was that even with one hidden layer(L=2)(L=2), an MLP can approximate any continuous function if the nonlinear activation functionσ\sigmais not a polynomial and the widthd1d_{1}is large enough[cybenko1989approximation].
However, it is often more efficient (in terms of the number of parameters) to increase thedepthof the networkLL[NIPS2011_8e6b42f1].

Training a deep network (\ieL>2L>2) that generalizes well can be difficult, requiring large training datasets, many gradient updates, and suitable regularization.
The introduction of large labeled training sets, advances in computing (\eggraphic processing units or GPUs which enabled orders of magnitude acceleration in parallel computation including matrix multiplies[10.1145/1553374.1553486]), development of ReLU, research progress in initialization and optimization algorithms for model parameters, and regularization techniques likedropout[dropout]all played an important role in the rise ofdeep learning[lecun_2018,schmidhuber2015deep].
Though the name deep learning was originally a reference to the depthLLof such networks, modern deep learning is characterized more by the composition of various types of modules that are trained through gradient-based optimization.
Below we introduce some other common network architectures.

## 8.4.4Convolutional neural networks

Convolutional neural networks (CNNs) are widely used for image-like data.
They implement the convolution of the input imageuuand afilterWW(also referred to as a kernel).
The parameters of the filter are learnable and the convolution involves traversing over input and calculating the inner product of the filterWWwith the part of the input in thereceptive field, which has the same spatial shape as the filter and is centered at the target pixel.
At each location—indexed byiiandjjbelow—there is a pixel that may have a vector of features associated with it.
In the context of CNNs, these components of these features—indexed byccandc′c^{\prime}below—are often referred to aschannelsin reference to the red, green, and blue color channels in a traditional image.
The convolution operation is often denoted with a∗\ast, and the result can be expressed asvc​(j)=(W∗uc)​(j)=∑c′∑iWc,c′​(i)​uc′​(‘​‘​j−i​”),v_{c}(j)=(W\ast u_{c})(j)=\sum_{c^{\prime}}\sum_{i}W_{c,c^{\prime}}(i)u_{c^{\prime}}(``j-i")\;,(69)

where‘​‘​j−i​”``j-i"is shorthand for the pixel index corresponding to the translation from pixeljjtoii.
By repeating the operation over all pixels, the result of a kernel convolution is also an image as illustrated in Fig.8.4.4.
Note that the the number of channels in the outputvvdoes not need to be the same as in the input, and the collection of filtersWc,c′W_{c,c^{\prime}}is often referred to as a filter bank.
The entire image for a fixed channel index is often referred to as afeature map.

A key feature of the CNN architecture is that it isequivariantto translations, meaning that if the input image is shifted (\eg,u​(i)→u′​(i)=u​(i−k)u(i)\to u^{\prime}(i)=u(i-k)), then the output is also shifted by the same amount (\eg,v​(j)→v′​(j)=v​(j−k)v(j)\to v^{\prime}(j)=v(j-k)).
This equivariance property is a natural consequence of using convolutions.
A fully connected MLP would not generally have this symmetry; however, it is enlightening to imagine transferring the computation performed by a CNN to the weights and biases of a fully connected MLP, which would result in duplicating the weights of the filters multiple times.
In this view, the CNN can be interpreted as a fully connected MLP withshared weights, which would maintain the equivariance property.
This view is helpful for gaining intuition about the inductive bias of models and makes clear that a CNN is a subset of the fully connected MLPs that satisfy the translation equivariance property.{pdgxfigure}

[width=1.0]A pictorial description of a kernel convolution over four input pixels. It takes a product of the weight matrix (kernel) and the local input matrix centered at a target pixel. The operation is repeated over the input image using the same kernel. The size of the output image depends on the size of the kernel, stride, and padding. In this figure, the kernel size of 3, stride of 1, and padding of 0 is used.

One may wonder how CNNs identify features with a spatial size larger than a typical kernel size.
One mechanism for this is by stacking multiple convolutional layers,\eg, the composition of two 3×\times3 kernels will lead to an effective 5×\times5 kernel in terms of the receptive field.
In addition, a typical CNN architecture uses pooling (described below), which effectively downsamples the image so that it can be processed at different resolutions.
The effective receptive field in the input image may be much larger than the kernel size in this case.
An alternative approach is to use aninception module, which is designed to extract features simultaneously using kernels of different size[7298594].

## Pooling

Poolingplays an important role in convolutional neural networks both practically and in terms of their mathematical properties.
A pooling operation is a type of aggregation or downsampling that takes many pixels as input and produce one pixel for output.
Typically, the pooling operation is applied independently for each channel or feature component.
The most popular pooling operations aremaxandaveragepooling.
Max pooling picks the highest activation pixel value within the specified receptive field, while the average pooling computes the average pixel value in the receptive field.
The idea of pooling generalizes to other architectures, including graph neural networks where the receptive field includes the neighbors of a particular node in the graph (see Sec.8.4.7).
Pooling can make the model robust to small, local deformations in the input, a property calledgeometric stability[DBLP:journals/corr/CohenS16a,bietti2021sample,bronstein2021geometric].
This type of local deformation is important and distinct from the equivariance to rigid translations provided by the convolutional structure.
Repeated pooling operations that eventually lead to a single feature vector with no spatial index is what gives rise to the invariance of common CNN architectures to translations (\ie, an image with a dog will be labeled ‘dog’ regardless of where the dog is in the image).

## CNN architectures for image analysis

A typical CNN for extracting a 1-dimensional array of features is designed with repeating blocks of convolution layers and pooling operations[Simonyan2015VeryDC].
Figure8.4.4shows an example evolution of a data tensor through the succession of convolution and pooling operations to extract a 1-dimensional array of features, which then can be fed into a block of MLP for an image classification (or a regression) task.
This type of architecture is referred to as anencoderorfeature extractor.{pdgxfigure}[width=1.0]An example CNN architecture to extract a 1-dimensional array of features from an image via succession of convolution layers and pooling operations. The (square) kernel, stride, and padding size of a convolution operation are 3, 1, and 1 in respective order. The pooling operation uses a square kernel size of 2. The number of filters at the first convolution layer is 6, and is increased by a factor of 2 at subsequent convolution layers.

The reduction in the spatial size of an image is performed slowly, typically by a factor of 2, which is the minimum possible reduction factor.
After the reduction of the spatial extent, the number of channels is typically increased (also by a factor of 2 in most cases), converging one set of feature maps into a larger number of downsampled feature maps.
There may be more than one convolution layer within each spatial resolution (\ie, between the grouping operations).
Following these design principles, CNN encoders typically becomedeep, consisting of dozens or sometimes hundreds of convolution layers, and face challenges of vanishing gradient problem (see Sec.9.5).
A standard practice to mitigate this issue is to explicitlynormalizethe input tensor input in each convolution layer using algorithms such asbatch normalization.
This will be discussed in Sec.9.9.

There are three main categories of computer vision tasks where CNNs are often used:
- •

image classification or regressionrequires a prediction of single value for the whole image (\ie, a category or target value),
- •

object detectionproduces a list location information, typically as a rectangular shaped bounding box, for detecting arbitrary number of objects in the input image, and
- •

semantic segmentationbrings a classification task down at the pixel-level (or regression although less common) to identify the class or a feature of every pixel in an image.

As discussed previously, a CNN feature extractor followed by MLP is often used for image classification and regression tasks in wide range of applications including particle physics. Many successful CNN architectures for object detection and semantic segmentation applications share key designs which we briefly discuss below.{pdgxfigure}

[width=0.6]CNN classifier for identifying highly boosted W bosons at ATLAS.

## Region convolutional neural network

(R-CNN) is one of the most successful design for object detection[NIPS2015_14bfa6bb].
R-CNN has been explored in HEP experiments where the number and location of signal (\eg, neutrino interactions) are not known apriori in large image data such as neutrino detectors[Acciarri_2017,Radovic:2018dip,Domine:2020tlx].
R-CNN consists of multiple CNNs.
The first is a feature extractor which produces a spatially compressed feature tensor.
For every pixel in the compressed tensor, the second CNN applies1×11{\times}1convolution to predict two information: anobject scoreto inspect whether or not there is a target object in the (spatially compressed) pixel, and prediction of the location and size of a rectangular, axis-aligned bounding box that contains the object (if exists).
This second CNN is called theregion proposal network(RPN), and the bounding box is called theregion of interest(ROI).
For each ROI with an object score above threshold (hyperparameter), the third CNN operates in the corresponding sub-field of an already-compressed tensor (\ieby the first CNN) to perform a classification for an object inside the ROI.
This approach can produce multiple ROIs for the same object with a high overlap.
Those predictions are reduced using non-maximum suppression (NMS) algorithm which computes the intersection-over-union (IoU) to combine overlapping ROIs that are likely detecting the same object.

## Residual networks and skip connections{pdgxfigure}

[width=0.7]Two types of skip connections: the top is from ResNet where the input is element-wise added to the output tensor of a block of convolution layers while the bottom shows a concatenation of the input to the output tensor as employed in other models including U-Net and DenseNet.

The expressivity of a neural network increases as more hidden layers are added, but gradient-based optimization of deep models can be notoriously difficult due to vanishing gradients (see Sec.9.5).
One powerful technique to address this challenge is aresidual network(ResNet), which is a modular architecture design that can be applied to neural network models[7780459].
Suppose af​(x)f(x)as the target transformation to be learned by a few stacked layers wherexxis the input to the first layer.
The authors of ResNet hypothesized that it may be easier for a model to learn a residual transformationf~​(x)≔f​(x)−x\tilde{f}(x)\coloneqq f(x)-x, thus the objective to learn isf~​(x)+x\tilde{f}(x)+xwheref~​(x)\tilde{f}(x)denotes the output of stacked layers.
This form assumesf~​(x)\tilde{f}(x)andxxshare the same tensor dimension and size.
If they differ in the feature dimension, equivalently the count of channels in an image tensor, one could use 1×\times1 convolutions to transform and match the dimension.
Adding the input tensorxxto the output of a convolution operationf~​(x)\tilde{f}(x)in ResNet is a form ofskip connection. For a residual block that outputsy=f~​(x)+xy=\tilde{f}(x)+x, the backpropagated gradient to the inputxxbecomes∂ℒ∂x=∂ℒ∂y⋅(I+∂f~∂x),\frac{\partial\mathcal{L}}{\partial{x}}=\frac{\partial\mathcal{L}}{\partial y}\cdot\left(I+\frac{\partial\tilde{f}}{\partial{x}}\right),(70)

meaning it sums an identity path with the gradient through the residual branch, helping prevent vanishing gradients.
ResNet authors demonstrated performance improvement at depths exceeding 1000 layers where the non-residual counterpart could not improve beyond a few dozen layers.
The ResNet design is widely used in many CNN architectures as it is modular,\ie, aresidual block, and can be applied per a stack of convolution layers (\eg, U-ResNet introduced for LArTPC detectors uses ResNet modules within a U-Net architecture[Adams:2018bvi,Domine:2019zhm]).

## U-Net

is one of the of most successful models used for semantic segmentation[10.1007/978-3-319-24574-4_28].
Since the output of U-Net is also an image, it is more interpretable compared to models for image-level classification or regression.
The model is used widely in HEP experiments in both 2D and 3D image data[Adams:2018bvi,Domine:2019zhm,Koh:2020snv,SBND:2020eho,Abratenko:2020ocq].
The architecture of U-Net consists of a CNN encoder anddecoder.
A decoder consists of convolution andtransposed convolutionlayers (also called deconvolution).
The operation of a transposed convolution can be seen as the opposite of a convolution: for every input pixel, its value is multiplied by the kernel and copied to the output.
In contrast to a regular convolution layer that reduces input pixels via the kernel, a transposed convolution layer broadcasts input pixels via the kernel, producing an output that is larger than the input.
In the decoder of U-Net, transposed convolution layers are used to upsample spatially compressed feature tensors back to the original image resolution.
Standard convolution layers are placed between upsampling operations.
Features for every output pixel can be used for either a classification or a regression task.
The idea behind encoder-decoder architecture is to extract features in the encoder, and the decoder interpolates those features back to the original spatial resolution.
The downsampling operation (\eg, max pooling) in the encoder is, however, a lossy process where spatial information is permanently lost.
This is a major obstacle to achieve a high precision semantic segmentation task.
The U-Net architecture overcomes this challenge by concatenating intermediate tensors in the encoder block with the tensors of the corresponding spatial size in the decoder block.
This is a type of askip connectiondiscussed previously, which dramatically improves the performance of semantic segmentation.

## 8.4.5Recurrent neural networks{pdgxfigure}

[width=.8]Pictorial description of a RNN (on the left) which takes an input and produces an output at every step with a hidden-to-hidden connection. The right diagram is unrolled over discrete steps. The yellow box represents a cell: a set of operations unique to each architecture.Recurrent neural networks(RNNs)[Rumelhart1986]are a family of neural networks designed for sequential data (\eg, time series). Consider sequential data wherextx_{t}represents each step in a sequence witht∈[1,n]t\in[1,n]. A typical RNN takes the following form:ht=gh​(ht−1,xt,θ)h_{t}=g_{h}(h_{t-1},x_{t},\theta)(71)

wherehth_{t}andθ\thetadenote thehidden stateof the system and parameters ofghg_{h}, the RNN model. The termrecurrentrefers the nature of the model operating on the previous state of the system (and hence the whole history). RNNs operate on three types of tasks:
- •

One-to-manytakes a single input and generates a sequence (e.g. generates a sequence data, such as a sentence or waveform, given a category).
- •

Many-to-onetakes a sequence and generates an output (e.g. sequence-labeling).
- •

Many-to-manytakes a sequence and generates a sequence where the length of input and output sequence may be same (e.g. classification of individual element in a sequence) or different (e.g. sequence to sequence mapping).

Figure8.4.5shows an example for a many-to-many task, where{xt}t=1:n\{x_{t}\}_{t=1:n},{yt}t=1:n\{y_{t}\}_{t=1:n}, and{ht}t=0:n\{h_{t}\}_{t=0:n}denote the inputs, outputs, and hidden states respectively. A set of operations at each time step is called acell. A simple RNN cell may look like:ht\displaystyle h_{t}=gh​(W​xt+V​ht−1+b)\displaystyle=g_{h}(Wx_{t}+Vh_{t-1}+b)(72)yt\displaystyle y_{t}=go​(U​ht)\displaystyle=g_{o}(Uh_{t})

whereW∈ℝdh×diW\in\mathbb{R}^{d_{h}\times d_{i}},V∈ℝdh×dhV\in\mathbb{R}^{d_{h}\times d_{h}},U∈ℝdo×dhU\in\mathbb{R}^{d_{o}\times d_{h}}are matricesghg_{h}andgog_{o}represent functions.did_{i},dhd_{h}, anddod_{o}are the dimension of input, hidden state, and output.b∈ℝdhb\in\mathbb{R}^{d_{h}}is a bias term. An example application is sequence-labeling where the goal is foryty_{t}to classify each inputxtx_{t}in the sequence. In that case, one might usegh=tanhg_{h}=\tanhandgo=softmaxg_{o}=\operatorname{softmax}and use a loss function that averages classification accuracy over the sequence.{pdgxfigure}

[width=0.8]Bidirectional RNN (left) provides contexts in the preceding and subsequent parts of the input sequence. RNN encoder-decoder (right) can generate an output with a different sequence length from an input. Each cell in the decoder may take a previously generated element, starting from a special marker that signals the beginning of the sequence (BoS) and ending when the end of sequence is generated.

Variations in RNN architectures result from the design of cells (described below) and flow of information across the cells. For instance, a bidirectional RNN (Figure8.4.5left) employs two set of RNNs, one processing the sequence in the forward direction and the other in the backward direction, and the hidden states from both directions are then combined to capture the context from both parts of the sequence. An RNN encoder-decoder (Figure8.4.5right) use one RNN to generate a context vector that encodes the whole input sequence, and use a separate RNN to generate another sequence from the encoded context. This can be used for machine translation.

## LSTM and GRU

An RNN applies the same functionsghg_{h}andgog_{o}in Eq.72repeatedly for each element of the sequence. This repeated component is similar to the shared weights for a convolutional filter in a CNN.

A hyperbolic tangent (tanh\tanh) is traditionally a popular choice forghg_{h}as it regulates the magnitude of the hidden states and prevents it from diverging. Yet, this simple model is challenging to train for a long sequence of data[bengio1994learning,pmlr-v28-pascanu13]. This is partially due to the fact thattanh\tanhcontributes to the vanishing gradient problem and because repeated multiplication of the same weight matrices (i.e.VVandWWin Eq.72) can lead to gradients that can either explode or vanish (see Sec.9.5). Additionally, the way the signal accumulates means that changes early in the sequence have different impact from changes late in the sequence.{pdgxfigure}

[width=0.85]LSTM (left) and GRU (right) are both gated neural network designed to address a vanishing gradient problem for RNNs.Long short-term memory(LSTM)[HochSchm97]is a model designed to address the issue of vanishing gradient for RNNs. In this model, acontextis introduced as a way to enable the model to hold long-term memory while the hidden states remain to hold short-term memory. The contextctc_{t}and hidden statehth_{t}at stepttare computed as follows:ct=ft​⨀ct−1+it​⨀c~tht=ot​⨀ctwhereft=σ​(Wf​xt+Vf​ht−1+bf)it=σ​(Wi​xt+Vi​ht−1+bi)ot=σ​(Wo​xt+Vo​ht−1+bo)c~t=tanh⁡(Wc​xt+Vc​ht−1+bc)\begin{aligned} c_{t}&=f_{t}\bigodot c_{t-1}+i_{t}\bigodot\tilde{c}_{t}\\
h_{t}&=o_{t}\bigodot c_{t}\end{aligned}\hskip 20.0pt\text{where}\hskip 20.0pt\begin{aligned} f_{t}&=\sigma\left(W^{f}x_{t}+V^{f}h_{t-1}+b^{f}\right)\\
i_{t}&=\sigma\left(W^{i}x_{t}+V^{i}h_{t-1}+b^{i}\right)\\
o_{t}&=\sigma\left(W^{o}x_{t}+V^{o}h_{t-1}+b^{o}\right)\\
\tilde{c}_{t}&=\tanh\left(W^{c}x_{t}+V^{c}h_{t-1}+b^{c}\right)\end{aligned}(73)

whereσ\sigmaand⨀\bigodotdenote logistic function and an element-wise (\ie, Hadamard) product andftf_{t},iti_{t}, andoto_{t}are referred to asgates.
Each gate outputs a value between 0 and 1, and is associated with unique weights,WWandVV, and a biasbb.
One can seectc_{t}is a combination of the previous context vectorct−1c_{t-1}and a new context vectorc~t\tilde{c}_{t}.
Theforgetgateftf_{t}controls which and how much of the past context should be kept or forgotten.
Theinputgateiti_{t}controls how much of the present contextc~t\tilde{c}_{t}should propagate to the current statectc_{t}.
The output gateoto_{t}controls which and how much of the context vector should represent the present hidden statehth_{t}.
From Figure8.4.5, one can see that the context vectorctc_{t}evolves with a gated addition operation.
As such, it can be seen as an uninterrupted path for gradients to flow.
This is similar to a residual connection (see ResNet in Sec.8.4.4), which enabled training of CNNs with thousands of layers.

Another gated model to solve a vanishing gradient problem is thegated recurrent unit(GRU)[bff0e6bd8f4a4f0d9735bf1728fb43ef].
The GRU is similar to the LSTM with a few simplifications: the GRU merges the context vector and the hidden states and combines three gates into two.
As a result, it requires less computational resources while retaining a similar level of performance for long sequences.
The GRU operations are defined as follows:ht=zt​⨀ht−1+(1−zt)​h~twherert=σ​(Wr​xt+Vr​ht−1+br)zt=σ​(Wz​xt+Vz​ht−1+bz)h~t=tanh⁡(Wh​xt+Vh​(rt​⨀ht−1)+bh)h_{t}=z_{t}\bigodot h_{t-1}+(1-z_{t})\tilde{h}_{t}\hskip 20.0pt\text{where}\hskip 20.0pt\begin{aligned} r_{t}&=\sigma\left(W^{r}x_{t}+V^{r}h_{t-1}+b^{r}\right)\\
z_{t}&=\sigma\left(W^{z}x_{t}+V^{z}h_{t-1}+b^{z}\right)\\
\tilde{h}_{t}&=\tanh\left(W^{h}x_{t}+V^{h}\left(r_{t}\bigodot h_{t-1}\right)+b^{h}\right)\end{aligned}(74)

wherertr_{t}andztz_{t}are referred to asresetandupdategate.
As one can see in Figure8.4.5, the reset gate in GRU performs the same task as the forget gate in LSTM by removing or reducing the elements of its memory (\iethe hidden state).
The update gateztz_{t}determines the relative proportion of the previous hidden stateht−1h_{t-1}and the new contexth~t\tilde{h}_{t}to be mixed in producing the new hidden state.

In addition to sequential data, the LSTM and GRU units can be used for data that has a tree-like structure.
In this setting, the networks are often referred to as recursive neural networks or TreeRNN and they have found applications in natural language processing and jet physics[socher2011parsing,socher2011semi,chen2015sentence,Louppe:2017ipp,Cheng:2017rdo].

## 8.4.6Attention and transformers

The idea behindattentionis to form a representation for the input, but different parts of the input are weighted differently according to the task at hand.
By making the weights learnable, the network can learn to attend to the relevant parts of the input.
For theiith task, one can form a task-specific contextcic_{i}by computing the weighted average of the hidden state representationshjh_{j}for each component of the input.
A softmax function is used to produce attention scoresαi​j\alpha_{ij}for thejjth input andiith task because it assigns a positive value to each component of the input and sums to one,∑jαi​j=1\sum_{j}\alpha_{ij}=1.
Putting these ingredients together, we have theadditive attention mechanismci=∑j=1nαi​j​hjwhereαi​j=softmaxj(βi​j),c_{i}=\sum_{j=1}^{n}\alpha_{ij}h_{j}\hskip 20.0pt\text{where}\hskip 20.0pt\alpha_{ij}=\operatornamewithlimits{softmax}_{j}(\beta_{ij})\;,(75)

wheresoftmaxj\operatornamewithlimits{softmax}_{j}indicates that normalizing sum runs over the indexjjand the logitsβi​j\beta_{ij}can be computed from a neural network.
In the case of a cell of an RNN encoder-decoder network (see Fig.8.4.5) that is decoding elementiiwith an incoming input statesi−1s_{i-1}, the logits for the attention mechanism can be computed asβi​j=U​tanh⁡(W​si−1+W~​hj+bi),\beta_{ij}=U\tanh\left(Ws_{i-1}+\widetilde{W}h_{j}+b_{i}\right)\;,(76)

whereUU,WW, andW~\widetilde{W}are the weights andbbis the bias term of the model.
Figure76from Ref.[olah2016attention]illustrates the full attention mechanism.
This idea was first implemented by a model calledRNNSearchthat made a breakthrough in machine translation by combining a bidirectional RNN with an additive attention mechanism[38ed090f8de94fb3b0b46b86f9133623].{pdgxfigure}[width=0.6]An illustration of the attention mechanism from Olah and Carter, “Attention and Augmented Recurrent Neural Networks.”
Lower boxes labeledArepresent input elements in the sequence and upper boxes labeledBindicate output elements. The left-most line originating from the firstBcorresponds to the statesi−1s_{i-1}in the text.

The valuesαi​j\alpha_{ij}can be used to visualize the influence of thejjth input element on theiith output element, which improves interpretability of the model[olah2016attention]as shown in Fig.8.4.6.

In additive attention (Eq.75), the hidden representationshjh_{j}, also calledvalues, are combined through a weighted average based on the coefficientsαi​j\alpha_{ij}, resulting in a task-specific context vectorcic_{i}.
These values are often arranged in a matrix labeledV∈ℝm×dvV\in\mathbb{R}^{m\times d_{v}}, where themmrows of the matrix correspond to individual hidden state vectors of lengthdvd_{v}.
Theαi​j\alpha_{ij}can also be represented as an×mn\times mmatrixα\alpharesulting from applying the softmax function to then×mn\times mmatrixβ\beta, normalized independently for each row.
With this notation, Eq.75could be rewritten asc=softmax⁡(β)​Vc=\operatorname{softmax}(\beta)V, where the softmax is normalized per row.

One powerful and widely used variant of the attention mechanism isscaled dot-product attention.
In scaled dot-product attention, instead of using an neural network to compute the logitsβ\betaas in Eq.76, the logits are computed by forming a dot product between an incomingqueryandkey.
The set ofnnquery vectors can be arranged into the matrixQ∈ℝn×dQ\in\mathbb{R}^{n\times d}and the set ofddkey vectors can be arranged into the matrix (transpose)K⊺∈ℝd×mK^{\intercal}\in\mathbb{R}^{d\times m}.
One can interpret the keys as trying to detect certain types of queries and routing the attention to the relevant value.
Typically, the dot-product is scaled by a factor of1/d1/\sqrt{d}.
The resulting task-dependent context isci=softmaxj(qi⋅kj/d)⁡vjc_{i}=\operatornamewithlimits{softmax}_{j}(q_{i}\cdot k_{j}/\sqrt{d})v_{j}.
A common, though confusing, notation is simplyc=Attention⁡(Q,K,V)=softmax⁡(Q​K⊺d)​V,c=\operatorname{Attention}\left(Q,K,V\right)=\operatorname{softmax}\left(\frac{QK^{\intercal}}{\sqrt{d}}\right)V\;,(77)

whereccis an×dvn\times d_{v}matrix organizing thenncontext vectors of lengthdvd_{v}that are tailored summaries of the input vector for each of thenntasks.

Thetransformerarchitecture is a powerful encoder-decoder model based on the scaled-dot product attention mechanism.
It was originally designed for sequential data and subsequently used in other areas of research including computer vision.
One advantage of scaled-dot product attention is that computing the attention weights does not involve any sequential processing.
This allows the models to better leverage the parallelism of the hardware to train more expressive models faster than before.
In place of the gated units of an RNN that are key to avoiding the vanishing gradient problem, the transformer architecture employs a residual connections at every attention module (\ie, the input tensor is added to the output as in Fig.8.4.4).

The second major ingredient in the transformer architecture ismulti-head attention.
A multi-head attention module executes multiple scaled dot-product attention modules in parallel.
The queryQQ, keyKK, and valueVVmatrices in each scaled dot-product attention module are obtained by applying linear transformations (with learnable weights) to the commonQQ,KK, andVVinput matrices.
Each of them can be considered a different (albeit related)perspectivefrom which to derive attention.

For a sequence-to-sequence mapping task, the output of encoder is used to derive keyKKand valueVVmatrices for the multi-head attention module in the decoder.
The decoder is then responsible for mapping between the key-value features derived from the input (the encoder) and the queries from the decoder (which is still executed sequentially) in order to produce the final decoded output.

Finally, we note that the transformer architecture does not just employ an attention mechanism in the decoder.
By employing attention in the encoder as well the model has more capacity to “interpret” the input—a concept referred to asself-attention.
Transformer models have contributed to breakthroughs in many areas of scientific and industrial research[bommasani2021opportunities].
While transformers are very powerful, they also require a larger number of training samples due to the weaker inductive bias than other models.{pdgxfigure}

Visualization of the attention weights in a sequence-to-sequence problem from Olah and Carter, “Attention and Augmented Recurrent Neural Networks.”
The thickness of the lines is proportional to the attention weightsαi​j\alpha_{ij}.

## 8.4.7Graph networks and geometric deep learning

Graphs are a powerful archetype for representing structure data.
A graph consists ofnodesas elements andedgesbetween between them.
Graphs are sufficiently flexible to describe many types of structured data including images and sequences.
Graph-based neural networks can also be seen as a generalization of many common types of machine learning models such as recurrent and convolutional neural networks[bronstein2021geometric].
The termgeometric deep learningrefers to this recent formulation that focuses largely on the symmetries of the data.

An earlier attempt to organize the variations on different flavors of graph-based neural networks can be found in Ref.[47094].
In their formalism, a graph network may be represented asG​(𝐮,V,E)G(\mathbf{u},V,E)where𝐮\mathbf{u}represents an array of global features,V={𝐯i}i=1:NvV=\{\mathbf{v}_{i}\}_{i=1:N^{v}}represents a set ofNvN^{v}nodes with𝐯i\mathbf{v}_{i}as features for theiith node (e.g. such as RGB channels if a node represents a pixel in image data), andE={(𝐞k,rk,sk)}k=1:NeE=\{(\mathbf{e}_{k},r_{k},s_{k})\}_{k=1:N^{e}}represents a set ofNeN^{e}edges with𝐞k\mathbf{e}_{k}as features for thekkth edge.
An edge may be (bi)directional whererkr_{k}andsks_{k}denotes the destination and origin nodes respectively.
The features of a graph may evolve with threeupdatefunctionsϕ\phiand threeaggregatefunctionsρ\rho:𝐞k′=ϕe​(𝐞k,𝐯rk,𝐯sk,𝐮)𝐯i′=ϕv​(𝐞¯i,𝐯i,𝐮)𝐮′=ϕu​(𝐞¯′,𝐯¯′,𝐮)𝐞i′=ρe→v​(Ei′)whereEi′={(𝐞k′,rk,sk)}rk=i,k=1:Ne𝐞¯′=ρe→u​(E′)whereE′=∪iEi′={(𝐞k′,rk,sk)}k=1:Ne𝐯¯′=ρv→u​(V′)whereV′={𝐯i′}i=1:Nv\begin{aligned} \mathbf{e}_{k}^{\prime}&=\phi^{e}(\mathbf{e}_{k},\mathbf{v}_{r_{k}},\mathbf{v}_{s_{k}},\mathbf{u})\\
\mathbf{v}_{i}^{\prime}&=\phi^{v}(\bar{\mathbf{e}}_{i},\mathbf{v}_{i},\mathbf{u})\\
\mathbf{u}^{\prime}&=\phi^{u}(\bar{\mathbf{e}}^{\prime},\bar{\mathbf{v}}^{\prime},\mathbf{u})\\
\end{aligned}\hskip 20.0pt\begin{aligned} \mathbf{e}_{i}^{\prime}&=\rho^{e\rightarrow v}(E_{i}^{\prime})&\hskip 5.0pt\text{where}\hskip 10.0pt&E^{\prime}_{i}=\{(\mathbf{e}^{\prime}_{k},r_{k},s_{k})\}_{r_{k}=i,k=1:N^{e}}\\
\bar{\mathbf{e}}^{\prime}&=\rho^{e\rightarrow u}(E^{\prime})&\hskip 5.0pt\text{where}\hskip 10.0pt&E^{\prime}=\cup_{i}E_{i}^{\prime}=\{(\mathbf{e}_{k}^{\prime},r_{k},s_{k})\}_{k=1:N^{e}}\\
\bar{\mathbf{v}}^{\prime}&=\rho^{v\rightarrow u}(V^{\prime})&\hskip 5.0pt\text{where}\hskip 10.0pt&V^{\prime}=\{\mathbf{v}_{i}^{\prime}\}_{i=1:N^{v}}\\
\end{aligned}(78)

where𝐞′\mathbf{e}^{\prime},𝐯′\mathbf{v}^{\prime}, and𝐮′\mathbf{u}^{\prime}denote the updated node, edge, and graph features. In Graph Networks, three types of information are updated in the following order. The first step isϕe\phi^{e}to update every edge. The second step updates every node: foriith node, computeρe→v\rho^{e\rightarrow v}to aggregate updated attributes from the edges withrk=ir_{k}=ithen computeϕv\phi^{v}to update the node attributes.
The third step updates the graph attributes throughϕu\phi^{u}which takes the original state𝐮\mathbf{u}, aggregated node and edge attributes byρv→u\rho^{v\rightarrow u}andρe→u\rho^{e\rightarrow u}respectively.

Graph neural networks[1555942](GNNs) are the class of neural networks that work on graph-structured data.
A related data format in computer vision and physics is thepoint cloud, which is an unordered set of points (\ie, a graph with no edges). Operations on point cloud need to be permutation invariant (\egmin\min,max\max,++,⋅\cdot), and analysis of 3-dimensional physical object represented by point cloud need to be rotation and translation invariant as in the case for an image. PointNet[Qi_2017_CVPR,Qi2017PointNetDH], a GNN that performs an object classification on point cloud of 3-dimensional positions, treats each point as a node, applies MLPs asϕv\phi^{v}to update node features, and global max-pooling operation asρv→u\rho^{v\rightarrow u}.
There is no explicit edge definition in PointNet (though the model applies affine transformation to all points using spatial transformer network[NIPS2015_33ceb07b], which could be considered as a separate graph operation, to introduce rotation and translation invariance and to capture topological features).
Deep sets[NIPS2017_f22e4747]follow the same manner exceptϕv\phi^{v}takes the global entities𝐮\mathbf{u}.
This is same for PointNet when performing point cloud segmentation:ϕv\phi^{v}takes a step of simply concatenating𝐮\mathbf{u}to node entities to combine a local and global features.
Dynamic graph CNN[10.1145.3326362]is a variant that (re)define edges dynamically using attention mechanism:ρe→v\rho^{e\rightarrow v}aggregateskkneighbor nodes where the inter-node distance is defined as a Cartesian distance in the feature space.ϕv\phi^{v}remains a MLP and, while edges are defined, there is no associated entity. A similar technique is used in nonlocal neural network[8578911]to efficiently propagate local feature information to points that may be far in the 3D cartesian coordinate.
Message-passing neural network[pmlr-v70-gilmer17a](MPNN) explicitly defines a feature vector as edge entities.
In MPNN,ρe→v\rho^{e\rightarrow v}performs element-wise sum of features and feed intoϕe\phi^{e}, explicitly passing features across nodes as the name suggests.
While these are representative models that are frequently used in particle physics applications[IceCube:2018gms,Komiske:2018cqr,Qasim_2019,Moreno:2019neq,Moreno:2019neq,Qu:2019gqs,DeepLearnPhysics:2020hut,Alonso-Monsalve:2020nde,Ju:2020xty,NEURIPS2020_fb4ab556,Hewes:2021heg], it is only a tiny fraction of GNN models developed over the past decade.

Graph-based models are particularly interesting for science applications because they offer a natural way to organize the entities in the data and encode how those components interact each other.
This particular type of inductive bias is referred to asrelational inductive biasin Ref.[1555942].
Graph edges may be intrinsically defined in the data (\eg, when representing a social network) or not (\eg, a point cloud).
In the latter case, the graph structure must be chosen.
A naive approach may be defining a fully-connected graph.
However, for applications on hundreds of thousands of nodes (\eg, high resolution 3D point cloud), this may require a prohibitive amount of memory and computation.
On the other hand, if the graph is too sparse, it may negatively impact the performance.
One may need to compare the model performance among differently constructed graphs and balance against computational burden.
Ideally, the graph would be based on some knowledge of the interactions, but in the absence of such knowledge, popular graph construction methods include fully-connected,kk-nearest neighbors, a Delaunay graph, minimum spanning tree, and locality-sensitive hashing[Pata:2023rhh].

Classification and regression tasks for graphs can be formulated such that the prediction is made for the entire graph or its individual nodes or edges. Graph-level prediction is like classifying an entire image, while node-level prediction is like semantic segmentation where individual pixels are classified.
For clustering of points, GNNs can approximate a transformation function for nodes into the latent space where an optimal clustering of points can be performed.
For instance, Ref.[Kieseler:2020wcq]proposes theobject condensationapproach to extract particle information from a graph of detector measurements as well as grouping of the measurements.
The model predicts the properties of a smaller number of particles than there are measurements, in essence reducing the graph without explicit assumptions on the number of targeted particles.
Certain nodes are chosen to be the “condensation” point of a particle, to which the target properties are attached.
A special loss function mimics attractive and repulsive electromagnetic potentials to ensure nodes belonging to the same particle are close in the latent space.
Alternatively, one can formulate clustering as an edge classification task[Farrell:2018cjr,DeepLearnPhysics:2020hut,ExaTrkX:2021abe,Dezoort:2021kfk].
See Ref.[Shlomi_2021]for a comprehensive review on particle physics applications.

## 8.5Model design with physics inductive bias

Designing neural networks that respect the structure of particle physics can materially improve sample efficiency, robustness to systematics, and physical interpretability.
Rather than relying on generic inductive biases (\eg, translation equivariance in image CNNs), particle-physics–informed models hard-wire symmetries, conservation laws, and kinematics into the architecture or loss.
This reduces the hypothesis space to functions that are a priori plausible, which is particularly valuable when training data is scarce, for extrapolation outside the training distribution, and for tasks where trust and uncertainty quantification matter as much as raw accuracy.

Exploitation of symmetry groups and henceequivarianceis arguably one of the most important forms of physics-informed approaches.
At the constituent level, events and jets are sets of particles, so permutation symmetry is fundamental. Deep sets and graph neural networks implement this by aggregating over particles with symmetric operations[Komiske:2018cqr]. Beyond permutation symmetry, Lorentz symmetry is the natural arena for high energy physics experiments.
Networks can be built from Lorentz scalars and tensors or by representing features as four-vectors and ensuring intermediate outputs transform equivariantly under boosts and rotations[pmlr-v119-bogatskiy20a,Gong:2022lye,Hao:2022zns,Bogatskiy:2022czk,Bogatskiy:2023nnw,Brehmer:2024yqw,Spinner:2024hjm].
Gauge symmetry offers another avenue where symmetry-aware design pays off. In lattice gauge theory, gauge-equivariant networks ensures locality and exact invariance under gauge transformations[2019arXiv190204615C,Boyda:2020hsi,10.5555/3495724.3495890,PhysRevD.103.074504,Batzner_2022].

While these models explicitly integrate laws of physics into mathematical operations and model architecture designs, it is also possible to implicitly enforce physics constraints through a loss definition and model optimization method.
For instance, physics-informed neural networks (PINNs) introduce regularization terms that force predicted physics quantities to follow laws of physics in the form of partial differentiable equations (\eg, acceleration as the time derivative of velocity)[RAISSI2019686,krishnapriyan2021characterizing].
Variants of PINNs incorporate differentiable physics models as a part of a model architectures[Newbury2024ARO].
Finally, it is also possible to introduce physics constraints in an optimization process.
For example, for a machine learning model for data reconstruction, an output of the model may go through a forward physics simulator that infers the original input to the reconstruction model.
By minimizing the difference between the original input and the inferred one, the reconstruction model is forced to learn a solution that is consistent with the forward physics model[NEURIPS2020_a878dbeb].

## 9Learning algorithms

## 9.1Gradient-based optimization

Given a parameterized modelf​(x,θ)f(x,\theta)and a loss functionℒ​(x,θ)\mathcal{L}(x,\theta), wherexxandθ\thetadenotes data and model parameters, one way to optimizeθ\thetais to first apply an appropriate initialization,θt=0\theta_{t=0}(e.g. Sec.9.7for neural networks), and perform an iterative update:θt=θt−1−λ​∇θℒ​(x,θ),\theta_{t}=\theta_{t-1}-\lambda\nabla_{\theta}\mathcal{L}(x,\theta),(79)

whereλ\lambdais a small, real valued hyperparameter calledlearning rate. To see how this works, defineδ​θ≡θt−θt−1\delta\theta\equiv\theta_{t}-\theta_{t-1}and considerδ​(∇θℒ​(x,θ))\delta(\nabla_{\theta}\mathcal{L}(x,\theta)):δ​(∇θℒ​(x,θ))≈δ​θ⋅∇θℒ​(x,θ)=−λ​|∇θℒ​(x,θ)|2\delta\left(\nabla_{\theta}\mathcal{L}(x,\theta)\right)\approx\delta\theta\cdot\nabla_{\theta}\mathcal{L}(x,\theta)=-\lambda|\nabla_{\theta}\mathcal{L}(x,\theta)|^{2}(80)

which would monotonically decrease
the loss function, and locally
move the parameter values in the
desired direction of loss
function minimization.
This algorithm is calledgradient descent(GD). We note thatλ\lambdaneeds to be sufficiently small for the approximation to hold. Whenλ\lambdais too large, this can be a cause of a gradient explosion discussed in Sec.9.7.

## 9.2Stochastic gradient descent

Stochastic gradient descent(SGD) follows GD but replaces the exact gradient term∇θℒ​(x,θ)\nabla_{\theta}\mathcal{L}(x,\theta)with a stochastic approximation, where
we subsample the data in the loss function usingNNsamples, whereN<nN<n,∇θ𝔼p^​(x)​ℒ≈1N​∑iN∇θℒi,\nabla_{\theta}\mathbb{E}_{\hat{p}(x)}\mathcal{L}\approx\displaystyle\frac{1}{N}\sum_{i}^{N}\nabla_{\theta}\mathcal{L}_{i},(81)

whereℒi\mathcal{L}_{i}is the loss function for
data sampleii.
It should be noted thatNNneeds to be randomly and independently sampled for the approximation to hold. Implementation of SGD follows three steps: take new samples of sizeNN, approximate the gradient, then update the parametersθ\theta.

In the case of optimizing the loss using a static database (\ieone cannot take newNNsamples for every update),mini-batch learningis often employed. This replaces the first step with a randomly sampledbatchof data, which is a subset of all the samples in the database. In this case, however, since a batch of data used for each parameter update is not entirely independent, a model may overfit. In practice, a part of the whole dataset is reserved as avalidationsample, and the model performance is carefully monitored during the optimization process to avoid overfitting via an early stopping criterion (see Sec.9.6and Fig.9.6).

SGD with slowly decreasing learning rate can be shown to converge to a local minimum
almost surely under mild conditions, and to a
global minimum for unimodal loss functions. SGD may
also prevent getting stuck in
shallow local minima of the loss function, thereby
reaching a better local minimum for multi-modal
loss functions. The noise in SGD with a
constant learning rate can be
viewed as a form of Langevin dynamics, which under proper conditions on the learning
rate and mini-batch size
converges to the stationary posterior
distribution of the weights[MandtHB17]. Thus SGD at a constant
learning rate can be viewed as a sampler
bouncing around and exploring the
posterior surface for better solutions,
descending onto the best found solution
as the learning rate is decreased, a process
related to temperature annealing in
global optimization.

Another advantage of SGD is simply the computational
cost: rather than evaluating the loss over all
the data samples at each update, we use a small
subset of data instead at each update. Furthermore,
mini-batching can take
advantage of vectorization libraries and GPU
architectures. Large batch training requires
specialized methods of training, such as
layer-wise adaptive rate scaling (LARS)[you2017largebatchtrainingconvolutional].

## 9.3Optimization algorithms

GD and SGD are the basic building blocks for
more advanced optimization algorithms.
One can improve the convergence rate of gradient
based optimization
by considering the learning rateλ\lambdato depend on
individualθi\theta_{i}. Second order algorithms such
as Newton’s method
take into account second order derivatives (Hessian) to find the minimum, and give an exact solution
in a single update when the loss is quadratic
around the peak. However,
this requires a matrix inversion of the Hessian,
which is exceedingly expensive in ML applications,
where the number of network parameters is very large. As a consequence, second order optimization
is rarely used in ML.

There are several improvements to the
basic SGD even in the absence of
Hessian information. Momentum based optimization
takes a physics perspective of a viscous fluid
in an external potential, where one updates
current velocity with the potential
gradient (force), followed by an update in
position based on velocity. This approach
therefore uses previous gradients in addition to the current one to
compute a running average of the gradient,
with a forgetting factor that controls how far
back the averaging goes. This
helps move faster towards the minimum in ravines, where
gradient descent is usually inefficient due to
the high condition number of the Hessian.

Beyond SGD with momentum, modern optimizers adapt step sizes across parameters or layers using recent gradient statistics and decouple regularization from the update. RMSprop tracks a running RMS of gradients and scales steps inversely to damp oscillations. Adam adds momentum (first moment) and variance (second moment) estimates to provide per-parameter adaptive updates. AdamW[loshchilov2019decoupledweightdecayregularization]improves Adam[kingma2017adammethodstochasticoptimization]by decoupling weight decay from the adaptive step, applying true L2 regularization directly to weights, which typically yields better generalization and has become a common default in vision and language models. For very large-batch regimes, layer-wise trust-ratio methods such as LARS (Layer-wise Adaptive Rate Scaling)[you2017largebatchtrainingconvolutional]and LAMB (Layer-wise Adaptive Moments optimizer for Batch training)[you2020largebatchoptimizationdeep]scale each layer’s effective learning rate by the ratio of parameter norm to gradient norm, enabling stable training with batch sizes of tens of thousands. More recently, Lion[chen2023symbolicdiscoveryoptimizationalgorithms]uses the sign of the momentum update instead of a second-moment estimate, reducing memory and often improving speed and generalization; it can also be combined with decoupled weight decay. In practice, these optimizers are paired with warmup, cosine or exponential decay schedules, and sometimes gradient clipping; the best choice depends on model size, data regime, and whether you prioritize fast convergence, large-batch scalability, or final generalization.

## 9.4Automatic differentiation and backpropagation

In practice,f​(x,θ)f(x,\theta)might take a complex form and may include a large set of parameters. The term∇θℒ=∇θℒ​(f​(x,θ))\nabla_{\theta}\mathcal{L}=\nabla_{\theta}\mathcal{L}(f(x,\theta))requires computing partial derivatives with respect to individual parameterθi\theta_{i}. Ifffis a composite model (i.e.f=fn​(fn−1​(⋯,θn−1),θn)f=f_{n}(f_{n-1}(\cdots,\theta_{n-1}),\theta_{n})), and if all offi:1,nf_{i:1,n}are differentiable, a chain rule can be applied:∇θiℒ=∂ℒ​(f​(x,θ))∂θi=∂ℒ∂xn⋅∂xn∂xn−1​⋯​∂xi∂θi\nabla_{\theta_{i}}\mathcal{L}=\frac{\partial\mathcal{L}(f(x,\theta))}{\partial\theta_{i}}=\frac{\partial\mathcal{L}}{\partial x_{n}}\cdot\frac{\partial x_{n}}{\partial x_{n-1}}\cdots\frac{\partial x_{i}}{\partial\theta_{i}}(82)

wherexnx_{n}denotes the output ofnnth composite functionfnf_{n}. In order to compute∇θiℒ\nabla_{\theta_{i}}\mathcal{L}forfif_{i}, it needs computation of a gradient at all preceding (or subsequent if seen in the forward context) functions. As the gradients accumulate across differentiable functions in the reverse order of the model composition, this technique is calledbackpropagation[Rumelhart1986]. An example offfthat satisfies conditions to apply backpropagation is a neural network, which consists of repeating blocks of a (differentiable) activation function and an affine transformation.

When the modelf​(x,θ)f(x,\theta)is implemented as a computer program in practice,automatic differentiation(AD), also calledalgorithmic differentiation, is used to compute the derivatives. AD exploits the fact that any computer program consists of a sequence of elementary arithmetic operations (\ie, addition, subtraction, multiplication, and division) and functions (\eg,log\log,exp\exp,sin\sin, andcos\cos) and apply chain rules to compute the target derivative. AD has advantages over traditional approaches including symbolic and numerical differentiation. The symbolic differentiation faces a serious difficulty of converting a program into a single expression, and the numerical differentiation suffers from round-off errors. Finally, both methods scale poorly in speed of computation for calculating partial derivatives with a large number of inputs. AD delivers much faster speed and does not suffer from increasing errors for calculating higher derivatives.

There are two modes of AD: theforwardandbackwardmode. Consider a composite functionf(x,θ)=fn(fn−1(⋯f1(x,θ1)⋯),θn−1),θn)f(x,\theta)=f_{n}(f_{n-1}(\cdots f_{1}(x,\theta_{1})\cdots),\theta_{n-1}),\theta_{n}). The forward mode applies the chain rule in the same order of the forward evaluation offfby computing∂f1/∂x\partial f_{1}/\partial xfirst, then∂f2/∂f1\partial f_{2}/\partial f_{1}, and continue to∂fn/∂fn−1\partial f_{n}/\partial f_{n-1}. The backward mode traverses the reverse direction: starting from the last (outer-most) function∂fn/∂fn−1\partial f_{n}/\partial f_{n-1}, next∂fn−1/∂fn−2\partial f_{n-1}/\partial f_{n-2}, and continue to∂f1/∂x\partial f_{1}/\partial x. Therefore, the backpropagation of gradients can be implemented using the backward AD, in which the target variable to be differentiated is fixed and the derivative is computed with respect to each sub-expression recursively as shown in Eq.82. The forward mode is simpler to implement as the order of gradient calculation follows the order of composite functions to be executed. The reverse mode typically requires less amount of computation than the forward mode,
but more memory is required to store intermediate function output values to calculate derivatives efficiently. Another consideration is the mapping of dimensionalityf:ℝk→ℝℓf:\mathbb{R}^{k}\rightarrow\mathbb{R}^{\ell}as it concerns the number of variables to sweep from each end. The forward mode is efficient whenk≪ℓk\ll\ellwhile the reverse mode takes an advantage ifℓ≪k\ell\ll k. For instance, in the case of an image classification where(k,ℓ)=(pixel count,1)(k,\ell)=(\text{pixel count},1), the reverse AD is more efficient.

Development of a differentiable physics simulator is an active area of research and AD-enabled programming frameworks are at the core of those research work. AD-enabled simulator can be used to solve an inverse problem of inferring the physics model parameters (e.g. calibration) or the input (i.e. reconstruction)[Gasiorowski_2024,Heinrich_2023]. A fully differentiable physics simulator often requires, however, a custom algorithm to approximate gradients to handle cases where gradient calculation is not straightforward (e.g. due to stochastic processes)[AEHLE2025109491]. Beyond AD, a specifically designed neural network that ensures accurate gradient calculation is also frequently used, sometimes in combination with AD-enabled framework[NEURIPS2020_a878dbeb,lei2022implicitneuralrepresentationdifferentiable].

## 9.5The vanishing and exploding gradient problems

Gradient based optimization crucially depends on the size of gradient with respect to each model parameter. If the magnitude of gradient is too large with respect to the distance to an optimal parameter value, it may repeatedly overshoot the target and cause an oscillation preventing convergence. If the gradient is too small, it may take an impractically long time to converge. As shown in Eq.82, the gradient ofiith functionfif_{i}is a product of gradients from the subsequent functions. If those gradients are too large or too small, the magnitude can can either increase or decrease exponentially in the number of layers. These are calledexplodingandvanishinggradient problem respectively.

Modern deep neural networks consist with many composite functions (\ie, layers) and are particularly prone to this effect. Let us consider a simple RNN. From Eq.72, we can write the backpropagating gradient:∂ht∂ht−1=diagonal​(f′​(W​xt+V​ht−1+b​1))​W\frac{\partial h_{t}}{\partial h_{t-1}}=\text{diagonal}\left(f^{\prime}\left(Wx_{t}+Vh_{t-1}+b1\right)\right)W(83)

wheref′f^{\prime}denotes the derivative of an activation function. The gradient of the contribution to the lossℒi\mathcal{L}_{i}from theiith element in the sequence with respect to thejjth hidden statehjh_{j}is therefore:∂ℒi∂hj=∂ℒi∂hi​Vi−j​∏j<t≤idiagonal​(f′​(W​xt+V​ht−1+b​1))\frac{\partial\mathcal{L}_{i}}{\partial h_{j}}=\frac{\partial\mathcal{L}_{i}}{\partial h_{i}}V^{i-j}\prod_{j<t\leq i}\text{diagonal}\left(f^{\prime}\left(Wx_{t}+Vh_{t-1}+b1\right)\right)(84)

where we can see thatVVcontributes multiplicatively withi−j{i-j}powers wheni−j>1i-j>1. This example is explored in depth for recurrent models[bengio1994learning,pmlr-v28-pascanu13]but is common for all types of deep neural networks.

In practice, one may explicitly inspect the magnitude of gradients propagating across layers to ensure an effective optimization. One way to mitigate an exploding gradient is to set the maximum gradient valueδmax\delta_{\text{max}}as a model hyperparameter andclipany larger gradientsδ\deltawhere it appears in the backpropagation:δ=δmax‖δ‖​δ\displaystyle\delta=\frac{\delta_{\text{max}}}{\|\delta\|}\deltaif‖δ‖>δmax.\displaystyle\|\delta\|>\delta_{\text{max}}.(85)

This is calledgradient clipping[pmlr-v28-pascanu13].

Alternatively, there are many architecture designs that are motivated by the vanishing and exploding gradient problem or which aim to help propagate gradients across many layers. These considerations drove the design of gated models like the LSTM and GRU for sequential data and also motivated the ReLU non-linearity. Other example architectural designs or components motivated by these considerations include identity mapping and skip connections used in ResNet, U-Net, and DenseNet, which allow gradients to flow across many layers.

Other factors contributing to vanishing and exploding gradient include initialization of model parameters and normalization of input data. These factors contribute in keeping the magnitude of activation, which also concerns the magnitude of gradient, within a reasonable range. A recommended practice for a gradient-based optimization of a neural network is to maintain the input values centered around zero and a similar level of covariance across the inputs (and the outputs that are the inputs to the next layer)[8c8eccbbe8a040118afa8f8423da1fe2]. These factors are discussed in the following.

## 9.6Early stopping{pdgxfigure}

An example instance of overfitting. The training loss (vertical axis) shown in blue decreasing over iterations (horizontal axis) while the loss values evaluated on test samples shown in orange start to increase at around 26,000 iterations as indicated by the vertical line.

Early stopping is a form of regularization used to avoid overfitting when an iterative method, such as gradient descent, is used as a learning algorithm. Imagine a plot of the training loss and test loss as a function of iterations (\ieparameter updates). As learning proceeds, the training loss will generally decrease. However, the test loss will often decrease initially and then start to increase, which is the classic sign of overfitting as shown in Fig.9.6. The basic idea of early stopping is simply to stop training before overfitting takes place. In some approaches to early stopping theoretical analysis of the learning problem provides a prescription for when to stop the training[yao2007early]; however, the most straight forward approaches use a held-out validation dataset to monitor the generalization performance[prechelt1998early].

## 9.7Initialization of model parameters

An improper initialization can slow down the optimization process or even result in a loss of convergence. Whileb(l)b^{(l)}is typically initialized to zero,W(l)W^{(l)}values need to be stochastic to avoid identical updates during optimization. One way is to sampleW(l)W^{(l)}from a zero-centered Gaussian distribution with a small variance (e.g. 0.01)[Krizhevsky2012ImageNetCW]. However, this method does not guarantee the same variance in the input to each layer, which depends on the size of the input layer, and makes it difficult to train a deep neural network[Simonyan2015VeryDC]. TheGlorotorXavierinitialization takes this into account and sets the variance of a Gaussian distribution to beσ2=1/d(l−1)\sigma^{2}=1/d^{(l-1)}assuming a symmetric activation function around zero, such as a logistic function or hyperbolic tangent[pmlr-v9-glorot10a]. TheHeinitialization uses the varianceσ2=0.5/d(l−1)\sigma^{2}=0.5/d^{(l-1)}, and is a simple extension of Xavier initialization for leaky, parametric, and standard ReLU activation[He2015DelvingD].

## 9.8Input normalization

Input data to a neural network is often pre-processed for the same goals discussed previously: values are shifted to have the mean of zero and scaled to keep a similar covariance across features. Furthermore, a data may be transformed using techniques including PCA and whitening (sphering) to keep input features independent and uncorrelated from each other[8c8eccbbe8a040118afa8f8423da1fe2].

## 9.9Batch normalization

Even with careful normalization of the input data and initialization of model parameters, the mean and covariance of the data representations in hidden layers will evolve during training and may pose challenges for learning for downstream layers. This is called aninternal covariate shift[DBLP:journals/corr/IoffeS15]and may cause negative effects to an optimization process. Accordingly, techniques to explicitly normalize features in between hidden layers are often employed for a deep neural network. One of them isbatch normalization (BN), which shifts and scales the input to a hidden layer:u~(l)=γ​u(l)−μBσB2+ϵ+β\tilde{u}^{(l)}=\gamma\frac{u^{(l)}-\mu_{B}}{\sqrt{\sigma^{2}_{B}+\epsilon}}+\beta(86)

whereu(l)u^{(l)}andu~(l)\tilde{u}^{(l)}refer to the raw and normalized input to thellth layer,μB\mu_{B}andσB\sigma_{B}represent the mean and mean-squared-error ofu(l)u^{(l)}calculated using abatchof input data used to update the network parameters.γ\gammaandβ\betaare part of model parameters that are updated during the optimization. After optimization is complete, these parameters are fixed for model evaluation during production.ϵ\epsilonis a small, fixed constant value to ensure numerical stability. While it is popular (especially in computer vision), a downside of BN is its dependency on the batch size. In situations where the batch size is limited to be a small number (\eg, memory limitation for a large data or a model), the performance using BN could degrade sinceβ\betaandγ\gammavalues may not be generalized for the dataset during training.

There are several variants to batch normalization with considerations on how to group a subset of values inulu^{l}. For instance, an image naturally has three groupings: a set of pixels across spatial axis, features within one pixel (\ie, imagechannels), alongside with a grouping across multiple images (\ie, batch). Different groupings have been studied and found and some are found effective to particular type of applications: layer normalization groups values along the channel and spatial dimensions[ba2016layer], instance normalization groups along the spatial dimension but not along the batch nor channel[ulyanov2017instance], and group normalization is similar to layer normalization but forms multiple sub-groups of channels[wu2018group]. These variants do not apply normalization across samples within a batch, and thus are agnostic to the batch size.

## 9.10Transfer learning: pre-training and fine-tuning

Transfer learningis a technique to improve performance and accelerate optimization process by reusing a pre-trained machine learning model for a new task.
The two tasks and corresponding datasets may differ, but fundamental features, such as implicitly learned symmetries in the underlying data, may be reusable across tasks and datasets.
Transfer learning typically takes two steps: the first is to alter the model or data if necessary, then continue updating some or all of the model parameters on the new data or task,fine-tuningthe model.
The first step is required, for example, when solving a different task that requires a different architecture (\eg, regression vs. classification), or when input data format requires a change (\eg, original model trained on three channel image, such as RGB images, while new data has a single channel).
Transfer learning has been widely practiced in the field of computer vision where large, labeled data sets are available[10.1007/978-3-319-10602-1_48,ILSVRC15,Cordts2016Cityscapes,Yi16]: a CNN trained for classifying images of an animal can be largely reused for object detection, or even for analyzing image data in science (\eg, particle trajectories recorded by an imaging detector).
It is a critical aspect for the development of general AI as well as interdisciplinary sharing of models across research fields.

While transformers were initially introduced for machine translation, later models such as GPT[gpt,gpt3]and BERT[bert]showed that these models can be generalized to multiple NLP tasks through transfer learning bypre-trainingfor several seemingly different tasks, including sentence classification, semantic similarity, question answering, and commonsense reasoning[gpt].
These models are collectively referred to as large language models (LLMs) and some have been fine-tuned for physics domains[10.1063/5.0238090,PhysRevAccelBeams.28.044601].

## 9.11Foundation models

A key to successful transfer learning is an effective pre-training process through which general (and thus re-usable) representations are learned by a model.
When a large, comprehensive dataset within a certain domain is combined with an effective representation learning method, typically using self-supervision or multi-task supervision, which forces a model to learn foundational concepts, the resulting model may potentially be generalized for any task defined in the data domain.
Such AI models are referred to asfoundation models(FMs), which are a central theme of general AI research today[tan2023promiseschallengesmultimodalfoundation].
The LLMs such as GPTs are the first and the most successful FMs to date.
The core of LLM pre-training is based on self-supervised learning (see Sec.4), where,\eg, a model is tasked to predict the next or missing word in a sentence.
To solve this task, a model must learn not only grammar or parts of speech but also a concept of visual colors and the probability distribution over possible colors an apple can take.
Using the vast online corpus as a training data, LLMs are trained to learn foundational representations of the world interpreted and generated by humans in the form of texts.

The critical properties of FMs include theemergence,homogenization, andscalability[tan2023promiseschallengesmultimodalfoundation].
Emergence means the system behavior is implicitly induced rather than explicitly constructed (\eg, a model’s capability to generalize through self-supervised pre-training).
Homogenization implies a single model or a system that can perform multiple tasks.
Scalability is improvement in model performance when increasing the computing resources, number of model parameters, and size of training dataset.
These properties are also used to evaluate the quality of FMs.
Following the initial success of LLMs, R&D of FMs has expanded to computer vision and audio data domains.{pdgxfigure}[place=h]Schematic of a foundation model based on HEP data.
Data is used to pre-train a large model, which can then be fine-tuned (or adapted) to various downstream tasks.

Many modern FMs combine multiple data modalities (\eg, image generation from text input, audio generation from text and image input)[DBLP:journals/corr/abs-2102-12092,clip,https://doi.org/10.48550/arxiv.2204.11824].
Multi-modal FMs are trained to correlate features from different data modalities either during a pre-training or fine-tuning stage.
For example, the CLIP model achieves this by minimizing the distance between extracted features from an image and its corresponding caption (text) data[clip].
It should be noted, however, pre-training FMs on sensory data (\eg, 1D waveforms, 2D images, or 3D scenes) is more difficult compared to symbolic data (\eg, language, math, or high-level physics data) as discussed in Sec.4.

HEP datasets present unique R&D opportunities to advance understanding of FMs.
Particles in high energy collisions follow well-established physics models and can be learned by FMs similar to words in natural language[mpmv1,mpmv2].
Large public datasets of galaxies recorded in multiple modalities (\eg, images and spectroscopy data) enable a contrastive learning approach based on CLIP[astroclip].
Similarly, a high-fidelity simulator in HEP can be used to formulate contrastive learning objectives across different scenarios in a stochastic process[resimulation].
Finally, HEP detectors offer big, high-precision data sets with challenging tasks to extract complicated physics information[young2025particletrajectoryrepresentationlearning].
A schematic of a foundation model based on HEP data is shown in Fig.9.11.

## 10Incorporating uncertainty

A fundamental aspect of data analysis is the quantification of uncertainty. This broad topic includes the traditional distinction between statistical and systematic uncertainty, procedures for propagation of errors, and the incorporation of uncertainty in to the statistical models (\egwith nuisance parameters) that are used in Bayesian or frequentist statistical procedures (see Sec.\crossrefstat). Accounting for systematic uncertainty can be seen as a requirement, but ideally systematic uncertainties are also taken into account in the design of the analysis so as to mitigate their effect. The introduction of machine learning into the analysis pipeline requires revisiting the techniques used for uncertainty quantification and exposes many fundamental issues that have nothing to do with the use of machine learning per se. See Ref.[Dorigo:2020ldg]for a recent review on this topic.

In machine learning research and industrial settings, the mismatch between the data distributionptrain​(x,y)p_{\textrm{train}}(x,y)used for training and the data distributionpprod​(x,y)p_{\textrm{prod}}(x,y)that the model will be applied to in production is referred to ascovariate shiftordomain shift. For example, one might train a classifier to identify cats and dogs with images from a well lit studio and then apply the classifier on images taken in doors with poor lighting conditions and a scratched lens. Not surprisingly, the mis-classification rate of the classifier will be different between the two settings.

Physicists are keenly aware that the simulations that we use to describe the data are not perfect, and this mismodeling corresponds to a large fraction of the of systematic uncertainties accounted for in published works. Since simulated data is often used to train machine learning models (\ieptrain​(x,y)p_{\textrm{train}}(x,y)), it is important to understand and account for how this mismodeling will influence results when applied to real data (\iepprod​(x,y)p_{\textrm{prod}}(x,y)).

One of the primary approaches to incorporating this type of uncertainty is to introduce nuisance parametersν\nucorresponding to the uncertain inputs to the simulation.
One then parametrizes various types of perturbations (\eg, corrections to efficiencies or energy scales) in the hopes that the resulting family of distributionsp​(x|y,ν)p(x|y,\nu)is flexible enough to encompass the true data distribution for classyy. In this approach one does not have just two “domains” for the data (\ie,ptrainp_{\textrm{train}}andpprodp_{\textrm{prod}}), but a continuous family of domains parameterized by the nuisance parametersν\nu.

With this framing in mind, there are several approaches to incorporating uncertainty into an analysis that includes ML-based components:
- •

propagation of errors:one works with a modelf​(x)f(x)and simply characterizes how uncertainty in the data distribution propagate through the function to the down-stream task irrespective of how it was trained.
- •

domain adaptation:one incorporates knowledge of the distribution for domains (or the parameterized family of distributionsp​(x|y,ν)p(x|y,\nu)) into the training procedure so that the performance off​(x)f(x)for the down-stream task is robust or insensitive to the uncertainty inν\nu.
- •

parameterized models:instead of learning a single function of the dataf​(x)f(x), one learns a family of functionsf​(x;ν)f(x;\nu)that is explicitly parameterized in terms of nuisance parameters and then accounts for the dependence on the nuisance parameters in the down-stream task.
- •

data augmentation:one trains a modelf​(x)f(x)in the usual way using training dataset from multiple domains by sampling from some distribution overν\nu.

In this setting it is best to consider the trained modelf​(x)f(x)orf​(x;ν)f(x;\nu)to be a fixed function and decouple the variability associated to training or the choice of architecture. The fact that one could have chosen a different architecture or learning algorithm should be treated in the same way as other choices that are made in the data analysis pipeline. While it is reasonable to want downstream inference and decisions to be robust to these choices, they are of a different nature than the uncertainty in the modeling of the data distribution. We return to this point in Sections10.5and10.6.

## 10.1Propagation of errors

In this Section, we consider the common scenario in which one has used some machine learning technique to train a modelf​(x)f(x)for classification or regression and wants to assess the sensitivity of the output off​(x)f(x)to uncertainty in the inputxx. We regard the functionf​(x)f(x)as fixed and we are not concerned with how the model was trained.

Propagating uncertainty through a ML-based modelf​(x)f(x)is not fundamentally different than for any other function, and one can use the standard propagation of errors formula of Sec.\crossrefprob:sec:errprop. As always, it is important to recognize the limitations of the propagation of errors formula, which is accurate when the uncertainty onxxis Gaussian and the functionf​(x)f(x)is approximately linear within the region set by the uncertainty onxx.

Similarly, classifiers are often used for particle identification or event selection. In that case, one is primarily interested in the efficiencyϵ\epsilonto satisfy a cut on the classifier output. The efficiency depends on the distributionp​(x|y)p(x|y)through the equationϵy=P​(f​(x)>fcut|y)=∫H​(f​(x)−fcut)​p​(x|y)​𝑑x\epsilon_{y}=P(f(x)>f_{\textrm{cut}}|y)=\int H(f(x)-f_{\textrm{cut}})p(x|y)dx, whereHHis the Heaviside step function andyyis an index or label for the category of data that is being considered (\eg, signal vs. background or electron vs. jet). Thus, the question in this context is what is the uncertainty on the efficiencyϵy\epsilon_{y}due to uncertainty in the distributionp​(x|y)p(x|y). In practice, the quantification of the uncertainty in the efficiencyϵy\epsilon_{y}is usually based on either a calibration measurement on real data or estimated with simulated data. These procedures typically treat the classifier as a black-box, and thus nothing precludes using those procedures on a ML-based classifier. An early example of this approach for b-tagging can be found in Ref.[ALEPH:1997umh].

In the case where simulation is used to estimate the efficiencyϵy\epsilon_{y}and its uncertainty, one usually varies nuisance parametersν\nuassociated to the simulation. One then uses simulated samples to approximateϵy​(ν)=P​(f​(x)>fcut|y,ν)=∫H​(f​(x)−fcut)​p​(x|y,ν)​𝑑x\epsilon_{y}(\nu)=P(f(x)>f_{\textrm{cut}}|y,\nu)=\int H(f(x)-f_{\textrm{cut}})p(x|y,\nu)dx. Again, the procedure for incorporating uncertainty isn’t fundamentally different if the classifierf​(x)f(x)is based on machine learning or a hand-crafted observable.

## 10.2Domain adaptation

While estimating the uncertainty for a ML-based model is not fundamentally different than any other hand-crafted observable used for regression or classification, the worry of many physicists is that by working with a high-dimensional set of featuresxxthat one is more susceptible to mismodeling of subtle correlations. This is a valid concern, and it should be appreciated that a great deal of prior knowledge and physical insight goes into the construction of hand-crafted observables so that they will be robust to the most uncertain aspects of data. However, much of this craft is based on heuristics that are difficult to systematize. Furthermore, one can only validate that such an observable is robust if one can explicitly evaluate the performance for a perturbed distribution. Thus in the settings where one can validate the robustness to a perturbed scenarioν0\nu_{0}, one must have access top​(x|y,ν0)p(x|y,\nu_{0}).

One approach to formalize this type of robustness is to consider the dependence on the distribution of the output of the modelf​(x)f(x)to the nuisance parameters. In statistics, if the distribution offfis independent of the nuisance parameters, thenffis referred to as apivotal quantity. This is a property that we can incorporate directly into the training procedure to target a particular notion of robustness. The authors of Ref.[Louppe:2016ylz]introduced an adversarial approach (similar to what is used in the generative adversarial network of Sec.3.4.2) to penalize a model during training if the distribution of the output varies with the nuisance parameters. To construct the training dataset{xi,yi,νi}i=1,…,n\{x_{i},y_{i},\nu_{i}\}_{i=1,\dots,n}, one must sampleyyandν\nuaccording to some proposal distribution (similar to a prior, but only used for the creation of training dataset, not necessarily for statistical inference), corresponding to a joint distributionp​(x,y,ν)p(x,y,\nu). Instead of minimizing the target lossℒf\mathcal{L}_{f}(\egcross-entropy or squared-error) with respect to the parametersϕf\phi_{f}that parameterize the modelff, one trains with a minimax strategy that also includes an adversaryqqwith parametersϕr{\phi_{r}}. The trained model is characterized by the saddle pointϕ^f,ϕ^r=arg⁡minϕf⁡arg⁡maxϕr⁡Eλ​(ϕf,ϕr),\hat{\phi}_{f},\hat{\phi}_{r}=\arg\min_{\phi_{f}}\arg\max_{\phi_{r}}E_{\lambda}(\phi_{f},\phi_{r})\;,(87)

where the value functionEλE_{\lambda}includes the target loss as well as a regularization term associated to the adversaryEλ​(ϕf,ϕr)=ℒf​(ϕf)−λ​ℒr​(ϕf,ϕr).E_{\lambda}(\phi_{f},\phi_{r})=\mathcal{L}_{f}(\phi_{f})-\lambda\mathcal{L}_{r}(\phi_{f},\phi_{r})\;.(88)

The constantλ\lambdais a hyperparameter, since generally there is a tradeoff between the two terms and only in special cases can the model that minimizesℒf\mathcal{L}_{f}also be a pivotal quantity. The regularization termℒr​(ϕf,ϕr)=𝔼p​(x,y,ν)​[−log⁡qϕr​(ν|fϕf​(x))]\mathcal{L}_{r}(\phi_{f},\phi_{r})=\mathbb{E}_{p(x,y,\nu)}[-\log q_{\phi_{r}}(\nu|f_{\phi_{f}}(x))](89)

is an example of conditional density estimation (see Sec.3.3), where the modelqϕr​(ν|f)q_{\phi_{r}}(\nu|f)is trying to predict the distribution of the nuisance parameterν\nugiven the output of the modelf​(x)f(x). This term is maximized whenffis independent ofν\nu. Earlier work had also used an adversarial technique for domain adaptation, but was limited to just two domains[edwards2015censoring,ganin2015unsupervised,2014arXiv1412.4446A], while hereν\nuparametrizes a continuous family of distributions and can have multiple components corresponding to different sources of uncertainty. Furthermore, the previous work aimed to make the distribution for a high-dimensional, intermediate representation of the data be invariant to the domain shift as opposed to just the final outputf​(x)f(x).

One way of interpreting Eq.87is that the goal is to minimize a regularized loss functionℒ~​(ϕf)=arg​maxϕr⁡Eλ​(ϕf,ϕr)\tilde{\mathcal{L}}(\phi_{f})=\operatorname*{arg\,max}_{\phi_{r}}E_{\lambda}(\phi_{f},\phi_{r}), where the optimization with respect toϕr\phi_{r}is not exposed. This motivates another approach in which the regularization is not achieved through a learned adversary, but by a measure of discrepancy between distributions that can be computed directly from samples. In particular, the authors of Ref.[Kasieczka:2020yyl]proposed the use ofdistance correlationto avoid what can be a challenging min-max optimization problem.

In either case, the optimization of the hyperparameterλ\lambdais based on the downstream task. For example, in Ref.[Louppe:2016ylz]considered the case whereffwas a signal vs. background binary classifier where the nuisance parameterν\nuwas associated to uncertainty in the background model. The hyperparameterλ\lambdawas then optimized to maximize the approximate median significance (AMS). Similarly, the authors of Refs.[Shimmin:2017mfk]and[Kasieczka:2020yyl]considered new physics searches in the context of boosted jet tagging, where the hyperparameter controls the sculpting of the side-bands used for background estimation.

While these strategies modify the training procedure so that the sensitivity to the nuisance parameters is reduced, it does not typically eliminate it. As a result, one still needs to propagate the uncertainty in the data distribution through the learned model as described in the preceding section.
Furthermore, care must be taken in interpreting the loss of sensitivity to the nuisance parameter.
For example, for theoretical uncertainties estimated as the difference between two different calculations (\ie, two-point uncertainties), decorrelation methods may reduce the apparent uncertainty while the true uncertainty remains much larger[Ghosh:2021hrh].

Note, this adversarial technique has also been employed in other settings where one would like to decorrelate the output of the classifier with an observed quantity so that it can be used for background estimation[Shimmin:2017mfk], although other techniques like moment decomposition[Kitouni:2020xgb]may suffice without full decorrelation.
Widely used alternative approaches to decorrelation include uboost[Stevens:2013dya], DDT[Dolen:2016kst], and using dedicated training samples that vary the chosen quantity to be decorrelated[CMS-DP-2020-002]. Other examples of the domain adaptation and decorrelation use cases from the Living Review include Refs.[Louppe:2016ylz,Dolen:2016kst,Moult:2017okx,Stevens:2013dya,Shimmin:2017mfk,Bradshaw:2019ipy,ATL-PHYS-PUB-2018-014,Kasieczka:2020yyl,Xia:2018kgd,Englert:2018cfo,Wunsch:2019qbo,Rogozhnikov:2014zea,10.1088/2632-2153/ab9023,clavijo2020adversarial,Kasieczka:2020pil,Kitouni:2020xgb,Ghosh:2021hrh].

## 10.3Parameterized models

An alternative to learning a modelf​(x)f(x)that is pivotal—\ie, whose distribution is independent of the nuisance parameterν\nu—is to learn a family of modelsf​(x;ν)f(x;\nu)that is parameterized in terms of the nuisance parameters.
In general, there is a tradeoff between the two terms of Eq.88for a single modelf​(x)f(x).
In a parameterized model,f​(x;ν)f(x;\nu)optimizes the performance of the model for every value ofν\nu.
Parameterized classifiers were first advocated in Ref.[Cranmer:2015bka]in the context of simulation-based inference (see Sec.10.7) and in Ref.[Baldi:2016fzo]for new physics searches.
It has also been applied to simulation-based inference for effective field theory parameters in Ref.[Brehmer:2018eca]and Ref.[Ghosh:2021roe]provides additional pedagogical examples.

The training of a parameterized model is similar to the standard procedure. For example, if one originally wanted to minimize the squared loss functionℒ​(y,f​(x))=(y−f​(x))2\mathcal{L}(y,f(x))=(y-f(x))^{2}with training dataset{xi,yi}i=1,…,n\{x_{i},y_{i}\}_{i=1,\dots,n}, then the corresponding training procedure for the parameterized model would be as follows.
One would need to construct a training set{xi,yi,νi}i=1,…,n\{x_{i},y_{i},\nu_{i}\}_{i=1,\dots,n}as described in the preceding section, construct a parameterized modelf​(x;ν)f(x;\nu)that takes as input the original feature vectorxxas well as the nuisance parametersν\nu, and then train using the same lossℒ​(y,f​(x;ν))=(y−f​(x;ν))2\mathcal{L}(y,f(x;\nu))=(y-f(x;\nu))^{2}.

One complication of the parameterized approach is that it is no longer possible to evaluate the model on a dataset{xi}\{x_{i}\}and pass on only{fi}\{f_{i}\}for downstream analysis tasks sincef​(xi;ν)f(x_{i};\nu)still depends onν\nu. Instead, one delay evaluating the model to some down-stream stage when the dependence onν\nuwould accounted for.
For example, in the context of a likelihood based analysis where one is testing a hypothesis where the nuisance parameters take on a particular valueνtest\nu_{\textrm{test}}, then one will consider the data distributionp​(x|νtest)p(x|\nu_{\textrm{test}}), and at that point one would evaluate the model at the corresponding nuisance parameter value,\ief​(x;νtest)f(x;\nu_{\textrm{test}}). Explicit examples are given in Refs.[Cranmer:2015bka,Brehmer:2018eca,Ghosh:2021roe,Dorigo:2020ldg]. While this may seem complicated, it actually corresponds to what is done in a typical likelihood-based fit when the statistical model has nuisance parameters;\iethe likelihood-ratio corresponds to the modelf​(x;ν)f(x;\nu)as in Eq.13.

## 10.4Data augmentation

An intuitive approach to building in robustness to systematic effects that can lead to domain shift, is simply to augment the training dataset so that it includes examples corresponding to several values of the nuisance parameter or systematic variations. As before one can construct a dataset{xi,yi,νi}i=1,…,n\{x_{i},y_{i},\nu_{i}\}_{i=1,\dots,n}, but instead of leveraging the information aboutνi\nu_{i}, one simply discards this information. This corresponds to sampling from the marginal distributionxi,yi∼p​(x,y)=∫𝑑ν​p​(x,y|ν)​p​(ν)x_{i},y_{i}\sim p(x,y)=\int d\nu p(x,y|\nu)p(\nu), and is often referred to assmearing. One can then use this smeared dataset for supervised learning in the traditional way. While it is possible that this approach will lead to improved robustness to systematic variations (\iegeneralization forν\nuother than the nominal value) than if systematic uncertainty weren’t considered at all), this intuitive approach has several shortcomings. The approach does not yield a pivotal quantity as in the adversarial approach, so propagation of uncertainty through the network is still required. Moreover, there is no direct way to control the tradeoff between independence from the nuisance parameter and the original target loss as in the adversarial approach. Finally, it can lead to significant performance loss compared to what is possible with the parameterized approach. These tradeoffs were studied in Refs.[Baldi:2016fzo,Ghosh:2021roe]with both pedagogical and physically-motivated examples.

## 10.5Aleatoric and epistemic uncertainty

In the machine learning and risk assessment literature, uncertainty is often characterized in terms ofaleatoricandepistemicuncertainty[OBERKAMPF200411,OHAGAN2004239,DBLP:journals/corr/abs-1910-09457,NIPS2017_2650d608]. Familiarity with these terms is useful, but the distinction between the two can be ambiguous, the terms are not always consistently used, and they do not clearly map onto the concepts used physics.

For example, Ref.[DBLP:journals/corr/abs-1910-09457], states that “roughly speaking, aleatoric (a.k.a., statistical) uncertainty refers to the notion of randomness, that is, the variability in the outcome of an experiment which is due to inherently random effects”, while “epistemic (a.k.a., systematic) uncertainty refers to uncertainty caused by a lack of knowledge (about the best model).” This seems clear enough, but in that same reference (and in Ref.[KIUREGHIAN2009105]) the aleatoric uncertainty is considered irreducible, while the epistemic uncertainty could be reduced with additional information.
This may seem backwards for many physicists since often in particle physics, we think of how uncertainties scale as we collect more data but keep the experimental design fixed. In that case, the statistical uncertainty will be reduced with time while the systematic uncertainty will remain constant444Further complicating the relationship between the terms is that many experimental uncertainties that are characterized as systematic are actually statistical in nature as auxiliary measurements and control regions are used to constrain the corresponding nuisance parameters..
There is no paradox here, it is simply a different point of view. The emphasis of the risk assessment community is not on collecting more data with the same experimental design, but collecting different types of data that will inform the models themselves. Clearly even for physicists, data from new experiments or calibration measurements could also reduce our systematic uncertainties.
While there are exceptions in the literature, the bulk of it associates aleatoric uncertainty with the randomness of classical probability (\ie, the statistical uncertainty associated to repeating the same experiment many times) and epistemic uncertainty with our state of knowledge.

Perhaps a more important distinction between the perspective of physicists and machine learning researchers has to do with the use of the term “model” and what exactly is uncertain. In physics, the systematic and epistemic uncertainty is typically associated to our understanding of the underlying physics and “the model” usually refers to the physics model, detector model encapsulated in a simulation. In contrast, for machine learning research, “the model” usually refers to the trained modelf^∈ℱ\hat{f}\in\mathcal{F}used as described in Section2.1(or the class of functionsℱ\mathcal{F}itself). This makes sense if we recall that in the bulk of machine learning research, one has little insight into the process that generated the data (\eg, images of cats and dogs, or natural language). In that sense, the epistemic uncertainty in machine learning is usually associated to uncertainty in the model parametersϕ\phiafter training, which would be reduced if one could collect more training dataset (see Ref.[NIPS2017_2650d608]for this point of view).

In the literature on uncertainty quantification (UQ), which is more closely connected to physics given the role of computer simulations, the terminology is more fine grained and less ambiguous. That community uses the terms parameter uncertainty (\ienuisance parameters), structural uncertainty (\ie, mismodelling), algorithmic uncertainty (\ienumerical uncertainty), experimental uncertainty (\ie, uncertainty from experimental resolution and statistical fluctuations), and interpolation uncertainty (\ie, uncertainty due to interpolating between different parameter values due to lack of computational resources).

## 10.6Model averaging and Bayesian machine learning

The core of
Bayesian machine learning is the
model averaging view. Here
one often takes a more ambitious view of learning than described in Sec.2.1, which is framed mainly as function approximation. While in Sec.2.1, the goal is to find a function that minimizes the risk, in Bayesian machine learning one explicitly builds a probability modelqϕ​(x,y)q_{\phi}(x,y)for the training dataset𝒟={xi,yi}i=1,…,n\mathcal{D}=\{x_{i},y_{i}\}_{i=1,\dots,n}. It is the same change in perspective that one has when one views the squared error loss functionℒMSE=(y−fϕ​(x))2\mathcal{L}_{\text{MSE}}=(y-f_{\phi}(x))^{2}as the log-likelihood for a probability modely∼N​(f​(x),σ)y\sim N(f(x),\sigma). In addition, one assumes some prior on the model parametersp​(ϕ)p(\phi), which is often a Gaussian distribution, and is analogous to Tikhonov regularization (see Sec.2.5). In this way, a single trained modelf^=fϕ^\hat{f}=f_{\hat{\phi}}is the MAP point estimate and the more complete Bayesian solution is the entire posterior distribution over the model parametersp​(ϕ|𝒟)p(\phi|\mathcal{D}). With this view, it is clear how increasing the number of training examplesnnwill lead to a reduction in uncertainty onϕ\phi. However, this notion of epistemic uncertainty has little to do with the notion of systematic uncertainty as the term is used by particle physicists.

Bayesian methods can be applied to
non-probabilistic regression problems,
in which case they can provide uncertainty
quantification.
Consider the case of regression in traditional (non-Bayesian) machine learning. The trained modelfϕ^​(x)f_{\hat{\phi}}(x)is used to predict the target labelyy. For a fixedxx, the model does not provide any notion of uncertainty on the prediction. One could propagate uncertainty onxxthroughf​(x)f(x), but that is also not the desired quantity to characterize the intrinsic spreadp​(y|x)p(y|x)in the data, which may exist even ifxxhas negligible uncertainty. In contrast, Gaussian process regression (a Bayesian method) does provide a natural way to communicate the uncertainty on the prediction, which is possible because one first had to specify a prior on the mean and covariance of the Gaussian process.

In the context of Bayesian deep learning and Bayesian
neural networks, one would place a prior on the weights and biases of the neural networkp​(ϕ)p(\phi)and then use one of the many emerging techniques to calculate the approximate posteriorp​(ϕ|𝒟)p(\phi|\mathcal{D}). However, we should recognize that we have little-to-no insight into the parameters of a deep neural network, so the prior onϕ\phiis hardly well-justified. Furthermore, just as in all Bayesian approaches, the prior is not invariant to reparametrizing the model:ϕ→η​(ϕ)\phi\to\eta(\phi). While it is difficult to justify the choice of the prior on the parameters (and, thus, the resulting posterior), the resulting model may perform well empirically. In such high-dimensional parameter spaces, the bias-variance tradeoff can be dramatic.

Bayesian model averaging (BMA) performs
Bayesian average over the posteriorp​(ϕ|𝒟)p(\phi|\mathcal{D}). This can
be applied to any quantityfϕf_{\phi}, such as a
regression or classification
predictionyy. Suppose we can draw from
the posteriorϕ∼p​(ϕ|𝒟)\phi\sim p(\phi|\mathcal{D}).
For each draw we can evaluate the predicted regression variabley=fϕ​(x)+ϵy=f_{\phi}(x)+\epsilon, whereϵ\epsilonis some noise to account for uncertainty in the predictions. We can denote this process
as a draw fromp​(y|x,ϕ)p(y|x,\phi),y∼p​(y|x,ϕ)=N​(fϕ​(x),σϵ2)y\sim p(y|x,\phi)=N(f_{\phi}(x),\sigma_{\epsilon}^{2}), whereσϵ2\sigma_{\epsilon}^{2}is the noise variance. The BMA then performsp​(y|x,𝒟)=∫𝑑ϕ​p​(ϕ|𝒟)​p​(y|x,ϕ).p(y|x,\mathcal{D})=\int d\phi p(\phi|\mathcal{D})p(y|x,\phi).(90)

In practicep​(y|x,ϕ)p(y|x,\phi)is evaluated by drawing
samples ofyyandϕ\phi, so the posterior
is defined implicitly by the samples. For
example, the mean prediction is obtained
by averagingfϕ​(x)f_{\phi}(x)over the samples
ofϕ\phi, and the covariance matrix is similarly
evaluated by averaging the second moments over the samples
ofϕ\phi.

Ref.[Yao_2018]provides a different perspective on BMA analyzed in what are referred to as theℳ\mathcal{M}-open andℳ\mathcal{M}-closed settings[Yao_2018]. Theℳ\mathcal{M}-closed
setting refers to the situation where the true data generating process is in the space of models, even if it is unknown to us. In contrast, theℳ\mathcal{M}-open setting refers to when the true data generating process is not in model space (\iethe model is mis-specified). Interestingly, in theℳ\mathcal{M}-open case one can potentially do better than any one model in the model class by considering an average over the models, since averaging can create a new model that is not in the model class. BMA provides one such averaging, but other averages, which are not weighted byp​(ϕ|𝒟)p(\phi|\mathcal{D}), can be a better choice. When the weights of each model are optimized against appropriate loss the resulting procedure is called stacking, which has been shown to be superior to BMA in theℳ\mathcal{M}-open setting[Yao_2018]. Ref.[SnoekOFLNSDRN19]performed experiments indicating that in some cases model averaging can also improve predictive uncertainty estimates under domain shifts.

Neural network model averaging beyond BMA comes in several different
flavors. Two successful model averaging
procedures are Monte Carlo dropout[GalG16], which uses dropout ensembling, and deep ensembles[Lakshminarayanan17], which use random initialization ensembling. These methods may not only be superior to BMA, they are also often significantly faster than BMA.
Whether these model averages are an approximation to BMA, or an alternative to it, remains a debated topic, and both views have been advocated.
BMA itself can be accelerated using approximate methods, such as stochastic Variational Inference with reparametrization trick[KingmaSW15].

Finally, in the context of Bayesian model uncertainty estimation, there are two practical ways to capture: repulsive ensembles and evidential regression. Repulsive ensembles are standard deep ensembles trained with an extra diversity penalty so the ensemble members make deliberately different but plausible predictions, improving coverage with fewer models. Evidential regression uses one network to predict the parameters of a simple probabilistic family plus an “evidence” term; when data are ambiguous it learns low evidence and returns wider intervals, and when data are plentiful it narrows them. The latter has been studied for uncertainty quantification for neutrino applications[Koh_2023]. In practice, both approaches can yield similarly well‑calibrated uncertainties. An open direction is to bring such calibrated epistemic uncertainty into the density estimators of generative models (\eg, flows, VAEs, or diffusion), for example via ensemble/Bayesian variants with diversity or evidential parameterizations, so we can represent and propagate uncertainty over whole distributions, not just point predictions.

## 10.7Connection to probabilistic machine learning

We end this Section by reinforcing the connection between uncertainty quantification in traditional machine learning and the more probabilistic approaches to machine learning exemplified by simulation-based inference (see Sec6) and deep generative models (see Sec.3.4). In the standard approach to supervised learning (\egclassification and regression) the modelf​(x)f(x)provides a point estimate foryy. Estimating an uncertainty onyygoes a step further, but the complete picture would be to model the posterior distributionp​(y|x)p(y|x). Gaussian processes (see Sec.8.2) are an example, but the form of the models is limited to Gaussian posteriors. In Sec6we discussed approaches to modelp​(y|x)p(y|x)using conditional density estimation[Cranmer:2016lzt,NIPS2016_6084,Cranmer:2019eaq]. If we extend this task to include a family of distributions parameterized by some nuisance parametersν\nu, then the task is to modelp​(y|x,ν)p(y|x,\nu), which is structurally similar.

In the context of classification, the output is already probabilistic, and the interpretation of the resulting classifier isf^MSE​(x)≈p​(y=1|x)\hat{f}_{\text{MSE}}(x)\approx p(y=1|x)(see Eq.11). Incorporating the dependence on the nuisance parameter, then connects to the likelihood-ratio trick (see Eq.13), approaches to simulation-based inference that involve learning the likelihood-ratio, and the parameterized approaches described in Sec.10.3.

If one pairs the training procedure for classification, regression, or density estimation used in the approaches above with model averaging techniques such as BMA, then it would be possible to incorporate both uncertainty associated to finite training dataset and the uncertainty associated to systematic uncertainties. However, as described in Sec.10.5and Sec.10.1, it is not clear that in physics applications it is desirable to account for the variability associated to training when the more common practice is to regard the trained modelf^​(x)\hat{f}(x)as fixed.

While these probabilistic approaches to machine learning are attractive conceptually, it is known in the machine learning community that classifiers often are poorly calibrated and often overly confident in their predictions. This is a problem even if one regards the trained modelf^​(x)\hat{f}(x)as fixed. Various approaches, including model averaging, are being pursued to improve the calibration of trained models, but the problem is unlikely to be eliminated entirely. Miscalibration can be verified by evaluating the true positive and false positive rates on held out data. This is common practice in experimental particle physics, where the output of a binary classifier is rarely taken at face value. Instead, the true and false positive rates are estimated with simulated data or control samples as described in Sec.10.1. Furthermore, the true and false positives can be characterized as a function of the nuisance parameters. These procedures can be used to help calibrate parameterized models based on the likelihood-ratio trick (see Refs.[Cranmer:2015bka,Ghosh:2021roe]).
Unfortunately, calibration in the context of density estimation is more challenging. This connects to topics and challenges in anomaly detection (see Sec.3.5).

## 11Model compression and deployment in experiments

The software and computing needs of training a machine learning model are different than those encountered when it is deployed for use.
The two stages are referred to astrainingandinference,\iemaking a predictionf^​(x)\hat{f}(x)given an inputxxand a trained modelf^\hat{f}.
Sometimes this transition also involves using different programming languages for implementing the trained model from the ones used for training them.
Modern machine learning frameworks support various serialization formats to exchange trained models.
For instance,ONNX[onnx]provides an open source format for many types of models, is widely supported, and can be found in many frameworks, tools, and hardware.
This is important when integrating a trained model into the software frameworks used by the large experiments.

While hardware acceleration with GPUs is important for efficiently training modern machine learning techniques, there are also advantages of hardware acceleration at inference time.
This may include GPUs or field programmable gate arrays (FPGAs), and the Living Review includes many example works focusing on efficient inference for a given hardware architecture[Strong:2020mge,Gligorov:2012qt,Weitekamp:DLPS2017,Nguyen:2018ugw,Bourgeois:2018nvk,1792136,Balazs:2021uhg,Rehm:2021zow,Mahesh:2021iph,Amrouche:2021tio,Pol:2021iqw,Goncharov:2021wvd].
Programming FPGAs requires the use of dedicated hardware description languages (HDLs) such as VHDL or Verilog as well as a design methodology that is aware of the limitations and nature of the relevant device.
Recently, high-level synthesis (HLS) tools[vitis,quartus,catapult], which ingest algorithms written in C/C++ code, have lowered the barrier to entry for using FPGAs.
Several tools, including hls4ml[Duarte:2018ite], FINN[FINN,blott2018finnr], Conifer[Summers:2020xiy], and fwXmachina[Hong:2021snb], have been developed to automatically create firmware from ML algorithms.
These tools have been used for applications ranging from jet tagging[Khoda:2022dwz,Odagiu:2024bkp,CMS-DP-2025-032]to muon transverse momentum regression[CMSP2L1T], on-detector data compression[DiGuglielmo:2021ide], charged particle tracking[Elabd:2021lgo,Huang:2023bny], calorimeter reconstruction[Iiyama:2020wap], and anomaly detection[Govorkova:2021utb,CMS-DP-2024-059,CMS-DP-2024-121].{pdgxfigure}

[place=!t]Illustration of the iterative magnitude-based parameter pruning and retraining with regularization procedure from Han et al. in NeurIPS, 2015.
The top-5 accuracy loss is shown as a function of parameter reduction (sparsity) for VGG-16 on ImageNet following different pruning procedures.
Without retraining, L1 regularization performs better than L2, but L2 performs better than L1 with retraining.
Iterative pruning gives the best result.

For applications where latency is a key concern (\eg, triggering at collider experiments), various accelerators have been investigated[Duarte:2018ite,DiGuglielmo:2020eqx,Summers:2020xiy,1808088,Iiyama:2020wap,Mohan:2020vvi,Carrazza:2020qwu,Rankin:2020usv,Heintz:2020soy,Rossi:2020sbh,Aarrestad:2021zos,Hawks:2021ruw,Teixeira:2021yhl,Hong:2021snb,DiGuglielmo:2021ide,Migliorini:2021fuj,Govorkova:2021utb].
To enable the use of an ML model in resource-constrained or latency-sensitive experimental settings, reducing the size and computational complexity of the model throughcompressionis often essential.
Compression techniques aim to improve the computational efficiency of models, while keeping the performance as close as possible to the original.
The two most ubiquitous methods arequantization[nagel2019datafree,han2016deep,meller2019same,zhao2019improving,banner2019posttraining,bertmoons,NIPS2015_5647,zhang2018lq,ternary-16,zhou2016dorefa,JMLR:v18:16-456,xnornet,micikevicius2017mixed,Zhuang_2018_CVPR,wang2018training,hawq,hawqv2], which modifies the number of bits used to calculate and store results in the model, andpruning[optimalbraindamage,han2016deep,lotteryticket,learningraterewinding,supermask,stateofpruning], which removes model parameters.
However, symbolic regression[Tsoi:2023isc]and knowledge distillation[Bal:2023bvt]have also been explored to learn compact algorithms.

While it is common to use 32-bit floating-point precision, for many applications, this may not be required to ensure adequate performance.
Reduced-precision formats, such as integer or fixed-point precision, may be used instead.
We can distinguishpost-training quantization(PTQ), in which model parameters are quantized after a traditional training is performed with 32-bit floating-point precision, andquantization-aware training(QAT), in which the training procedure is modified to emulate reduced precision formats.
QAT results in better performance for a smaller bit width, but requires (re)training with a dedicated framework[Coelho:2020zfu,hawq,hawqv2,Sun:2024soe,brevitas].
Serializing and exchanging quantized models is a challenge addressed by theQONNXformat, which extendsONNXto represent arbitrary-precision quantized neural networks[Pappalardo:2022nxk].

Pruning is the removal of unimportant weights, quantified in some way, from a neural network.
The two main categories areunstructured pruning, where weights are removed without considering their location within a network, andstructured pruning, where weights connected to a particular node, channel, or layer are removed.
Pruning reduces the number of computations that must be performed to produce an inference result, thus reducing the hardware resources or algorithm latency.
The development of pruning algorithms and understanding their behavior is an active area of research[stateofpruning].
One relatively simple method is iterative, magnitude-based pruning[learningeff,Duarte:2018ite], as shown in Fig.11.
In this process, the model is trained with L1 or L2 regularization (discussed in Sec.2.5), resulting in a set of optimal parameters, where some are close to zero.
Those parameters with values below a certain threshold can be set to exactly zero (thereby removing them from the model), and training can be repeated.
Successive iterations of this procedure can remove more parameters until the desired reduction in parameters, orsparsity, is achieved.
This process usually results in models that have slightly reduced performance, although the performance loss is typically negligible for sparsities≲\lesssim90%[learningeff].
Pruning and quantization can also be applied together[Hawks:2021ruw].

Finally, some solutions for deployment of ML models involve using cloud resources[Kuznetsov:2020mcj,SunnebornGudnadottir:2021nhk]or using hardware coprocessors, like GPUs and FPGAs,as a service[sonic,sonic_neutrinos,sonic_cms,sonic_tracking].
In this approach, coprocessor resources are decoupled from CPUs, and CPU-based clients can send inference requests to coprocessor-based servers via network calls.
The advantages of this approach are coprocessors can accept inference requests from local or remote CPUs, certain types of coprocessors can be allocated for specific tasks, the coprocessor-to-CPU ratio can be optimized, the separation of software support for coprocessor and CPU workflows reduces the maintenance burden, and developments from industry can be more easily leveraged[sonic_cms].

## References

## 


- 


Major funding support from
