# Functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networks

**arXiv ID**: 2605.07060v2
**Authors**: Ryoichiro Agata, Tomohisa Okazaki
**Published**: 2026-05-08
**Categories**: physics.geo-ph, cs.LG, physics.comp-ph, stat.ML
**HTML URL**: https://arxiv.org/html/2605.07060v2

## Abstract

Physics-informed neural networks (PINNs) provide a mesh-free framework for solving PDE-constrained inverse problems, but their extension to Bayesian inversion still faces a fundamental difficulty: prior distributions are typically defined in the weight space of neural networks, whereas physically meaningful prior assumptions are more naturally expressed in function space. In this study, we introduce a unified framework, termed functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networks (fpBPINN), to incorporate functional priors into Bayesian PINN-based inversion. We consider two complementary approaches. The first is a functional-prior-informed Bayesian PINN (FPI-BPINN), in which a neural network weight prior is learned to be consistent with a prescribed functional prior, and Bayesian inference is subsequently performed in weight space. The second is function-space particle-based variational inference for PINNs (fParVI-PINN), which performs Bayesian estimation using ParVI directly in function space. We also show that random Fourier features (RFF) play an important role in representing Gaussian functional priors with neural networks and in improving posterior approximation. We applied the proposed approaches to one-dimensional seismic traveltime tomography and two-dimensional Darcy-flow permeability inversion. These numerical experiments showed that both approaches accurately estimated posterior distributions, highlighting the significance of introducing physically interpretable functional priors into Bayesian PINN-based inverse problems. We also identified the contrasting advantages of FPI-BPINN and fParVI-PINN, namely flexibility and accuracy, respectively.

## Full Text

Functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networks

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.07060v2 [physics.geo-ph] 14 May 2026

1]organization=Japan Agency for Marine-Earth Science and Technology,
country=Japan
2]organization=Disaster Prevention Research Institute, Kyoto University,
country=Japan
3]organization=RIKEN Center for Advanced Intelligence Project,
country=Japan

## Functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networksRyoichiro AgataTomohisa Okazaki[[[

## Abstract

Physics-informed neural networks (PINNs) provide a mesh-free framework for solving PDE-constrained inverse problems, but their extension to Bayesian inversion still faces a fundamental difficulty: prior distributions are typically defined in the weight space of neural networks, whereas physically meaningful prior assumptions are more naturally expressed in function space. In this study, we introduce a unified framework, termed functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networks (fpBPINN), to incorporate functional priors into Bayesian PINN-based inversion. We consider two complementary approaches. The first is a functional-prior-informed Bayesian PINN (FPI-BPINN), in which a neural network weight prior is learned to be consistent with a prescribed functional prior, and Bayesian inference is subsequently performed in weight space. The second is function-space particle-based variational inference for PINNs (fParVI-PINN), which performs Bayesian estimation using ParVI directly in function space. We also show that random Fourier features (RFF) play an important role in representing Gaussian functional priors with neural networks and in improving posterior approximation. We applied the proposed approaches to one-dimensional seismic traveltime tomography and two-dimensional Darcy-flow permeability inversion. These numerical experiments showed that both approaches accurately estimated posterior distributions, highlighting the significance of introducing physically interpretable functional priors into Bayesian PINN-based inverse problems. We also identified the contrasting advantages of FPI-BPINN and fParVI-PINN, namely flexibility and accuracy, respectively.

## keywords:Bayesian inversion\sepPhysics-informed neural networks\sepFunctional prior\sepFunction space\sepUncertainty quantification\sepGaussian process{highlights}

Functional priors provide a unified viewpoint for Bayesian PDE-constrained inversion with PINNs.

FPI-BPINN and fParVI-PINN enable uncertainty quantification with physically interpretable priors.

Random Fourier features improve Gaussian-prior representation and posterior approximation.

## 1Introduction

Inverse problems that estimate unknown parameters in partial differential equations (PDEs) from observational data play a central role in many fields of science and engineering, including geoscience, fluid mechanics, materials science, and thermal engineering. These problems are generally nonlinear and ill-posed and are often strongly affected by observational noise and model uncertainty. Therefore, in addition to deterministic estimation based on discretized forward solvers and optimization, it is important to adopt a Bayesian framework that quantifies uncertainty. Traditionally, forward analyses, adjoint methods, and sampling methods based on grid- or mesh-based representation have been the mainstream Bayesian approaches.

However, in recent years, mesh-free inverse analysis using deep learning techniques has attracted attention as an alternative approach. A representative example is the physics-informed neural network (PINN)Raissi et al. (2019), which provides a framework for treating both forward and inverse PDE problems in a unified manner by incorporating the residual of the governing equation into the loss function. A major advantage of PINNs in inverse problems is that not only the solution of the governing equation but also unknown quantities such as coefficient fields and source terms can be represented by neural networks (NNs), enabling estimation in a fully mesh-free manner. On the other hand, standard PINNs are essentially point-estimation methods and cannot directly handle uncertainty arising from observational noise or data sparseness. Introducing uncertainty quantification (UQ) based on Bayesian inference is therefore effective, but such efforts are still at an early stage. A pioneering example is Bayesian physics-informed neural networks (B-PINNs)Yang et al. (2021), in which Bayesian neural networks (BNNs) are incorporated into PINNs, providing a framework for estimating posterior distributions using Hamiltonian Monte Carlo (HMC)Duane et al. (1987)and Variational Inference (VI)Jordan et al. (1999). Similar problems have also been solved using different Bayesian methodsSun and Wang (2020); Pensoneault and Zhu (2024), such as particle-based variational inference (ParVI)Liu and Wang (2016); Liu et al. (2019)and ensemble Kalman inversion (EnKI)Kovachki and Stuart (2019). B-PINNs demonstrated that forward and inverse PDE problems with noisy data can be treated in a Bayesian manner.
Unlike ordinary Bayesian inference, in which unknown parameters are estimated directly, unknown parameters in BNNs are usually the weights of the NNs. In BNNs, the prior distribution required for Bayesian inference is specified on the NN weights. Typically, simple priors, such as independent and identically distributed (IID) Gaussian distributions or Student’s t-distributions, are assigned to the weights. However, such simple priors in weight space are difficult to interpret physically in the function space represented by the NN outputs and may introduce uncontrolled effects into the inference resultsWang et al. (2019).

A fundamental issue here is therefore the design of prior distributions when PDE parameters are represented by NNs.Tran et al. (2022)identified this as a fundamental limitation of BNNs and proposed a framework for training NN weight priors to match a desired functional prior defined by a Gaussian process (GP) through Wasserstein distance minimization. In other words, function space is more physically and statistically interpretable than weight space, and this viewpoint is also important for PDE inverse problems. The idea of learning priors by focusing on distributions and data in function space has also attracted attention in the context of generative models such as Generative Adversarial Networks (GANs)Goodfellow et al. (2014); Meng et al. (2022)and diffusion modelsHo et al. (2020); Li et al. (2025). However, in the context of learning weight priors that are consistent with a functional prior for PINN-based inverse problems, this issue has not yet been investigated.
Related to this line of research, studies that formulate UQ for BNNs directly in function space have also been developedSun et al. (2019); Wang et al. (2019); Rudner et al. (2022).Wang et al. (2019)proposed function-space ParVI (fParVI), which performs ParVI in function space rather than in weight space, thereby avoiding the degeneration of particle-based methods in overparameterized models. Since this method formulates Bayesian estimation in function space, a functional prior in closed form can be directly incorporated. This approach was also interpreted byD’Angelo and Fortuin (2021)as a deep ensemble with a repulsive term in function space. These approaches that perform Bayesian inference directly in function space were, to the best of our knowledge, first applied to PINN-based inverse problems in the context of solid-Earth geophysics byAgata et al. (2023). Similar ideas have since been proposed independently byRöver et al. (2024); Pilar et al. (2025); Shukla et al. (2026), although introducing appropriate priors is not their main focus.

In this study, we therefore introduce a unified framework, which we call functional-prior-based approaches to Bayesian PDE-constrained inversion using physics-informed neural networks (fpBPINN), for Bayesian inverse problems of PDE parameters based on PINNs. fpBPINN focuses on priors that have a clear meaning in the function space represented by NN outputs. Specifically, we compare two approaches: a functional-prior-informed Bayesian PINN (FPI-BPINN), which first learns an NN weight prior consistent with a prescribed functional prior and then performs Bayesian inference in weight space, and fParVI for PINNs (fParVI-PINN), which performs ParVI for PDE parameters directly in function space. The former offers the flexibility of exploiting existing BNN inference methods after prior learning, whereas the latter allows prior distributions to be described naturally in function space. Furthermore, we point out that, when applying these methods to PINN inverse problems, the introduction of random Fourier features (RFF) into the NN plays an important role in facilitating the learning of frequency components corresponding to the prior distribution in function space. Through one-dimensional (1D) seismic traveltime velocity estimation, we demonstrate the importance of considering a functional prior when aiming for Bayesian estimation consistent with physical intuition and show that both proposed approaches achieve accurate functional-prior-based inference. In two-dimensional (2D) Darcy-flow permeability estimation, we validate the applicability of the proposed methods to more realistic problem settings. We clarify the significance of introducing physically interpretable functional priors into PINN-based inverse problems and compare the advantages of the two approaches.

The remainder of this paper is organized as follows. Section 2 formulates the Bayesian PDE-constrained inversion problem and summarizes the adjoint-based gradient evaluation used in the proposed framework. Section 3 introduces the functional-prior-based Bayesian PINN approaches, including FPI-BPINN and fParVI-PINN. Section 4 presents numerical experiments on 1D seismic traveltime tomography and 2D Darcy-flow permeability inversion. Section 5 discusses the implications, advantages, and limitations of the proposed approaches. Finally, Section 6 provides a conclusion.

## 2Formulation of Bayesian inversion problem

## 2.1Neural network-based formulation of PDE-constrained inversion

LetΩ⊂ℝd\Omega\subset\mathbb{R}^{d}be a spatial domain with boundary∂Ω\partial\Omega.
A general PDE constraint can be formulated in operator form asℱ​(u​(x),m​(x))=0x∈Ω,\displaystyle\mathcal{F}(u(\textbf{x}),m(\textbf{x}))=0\qquad\textbf{x}\in\Omega,(1)ℬ​(u​(x))=0x∈∂Ω,\displaystyle\mathcal{B}(u(\textbf{x}))=0\qquad\textbf{x}\in\partial\Omega,(2)

whereℱ\mathcal{F}andℬ\mathcal{B}represent the (possibly nonlinear) differential operators defining the physics and boundary conditions, respectively.u​(x)u(\textbf{x})is the PDE solution at pointx.
We define a PDE-constrained inverse problem as the problem of estimating the parameter fieldm​(x)m(\textbf{x})that satisfies the PDE constraints (Equations1and2) when the data𝒟\mathcal{D}are given as𝒟={(xi,u​(xi))}i=1Nd,xi∈Ω,\mathcal{D}=\{(x_{i},u(\textbf{x}_{i}))\}_{i=1}^{N_{d}},\textbf{x}_{i}\in\Omega,(3)

wherexi\textbf{x}_{i}are the observation points.
The deterministic inverse problem is formulated as the problem of obtaining the parameter fieldm​(x)m(\textbf{x})that minimizes both the misfit between the observed and predicted data and the residual of the PDE constraint.
The conventional approach to this problem is to represent the solutionu​(x)u(\textbf{x})and the parameter fieldm​(x)m(\textbf{x})by discretizing the domainΩ\Omegausing a grid or mesh.
However, the emergence of PINNs has enabled such inverse problems to be solved in a mesh-free manner, representing the solution and the parameter field using NNs asu​(x)≈fu​(x,𝜽u),x∈Ω,\displaystyle u(\textbf{x})\approx f_{u}(\textbf{x},{\bm{\theta}_{u}}),\qquad\textbf{x}\in\Omega,(4)m​(x)≈fm​(x,𝜽m),x∈Ω,\displaystyle m(\textbf{x})\approx f_{m}(\textbf{x},{\bm{\theta}_{m}}),\qquad\textbf{x}\in\Omega,(5)

wherefuf_{u}andfmf_{m}are the NNs representing the solution and the parameter field, respectively.𝜽u{\bm{\theta}_{u}}and𝜽m{\bm{\theta}_{m}}are the weight parameters of the NNs.

## 2.2Bayesian formulation and calculation of gradient of posterior distribution

In the NN-based formulation, Bayes’ theorem is generally formulated for the weight parameters𝜽m{\bm{\theta}_{m}}rather than the parameter fieldmmitself, following the standard BNN framework, asp​(𝜽m|𝒟)=p​(𝒟|𝜽m)​p​(𝜽m)p​(𝒟)∝p​(𝒟|𝜽m)​p​(𝜽m),p({\bm{\theta}_{m}}|\mathcal{D})=\frac{p(\mathcal{D}|{\bm{\theta}_{m}})\,p({\bm{\theta}_{m}})}{p(\mathcal{D})}\propto p(\mathcal{D}|{\bm{\theta}_{m}})\,p({\bm{\theta}_{m}}),(6)

wherep​(𝜽m)p({\bm{\theta}_{m}})is the prior distribution,p​(𝒟|𝜽m)p(\mathcal{D}|{\bm{\theta}_{m}})is the likelihood, andp​(𝒟)=∫p​(𝒟|𝜽m)​p​(𝜽m)​𝑑𝜽mp(\mathcal{D})=\int p(\mathcal{D}|{\bm{\theta}_{m}})\,p({\bm{\theta}_{m}})\,d{\bm{\theta}_{m}}is the evidence (marginal likelihood).
The probability distribution function (PDF) form​(x)m(\textbf{x}), which we actually want to obtain, is obtained as the predictive distributionp​(m​(x)|𝒟)=∫p​(m​(x)|𝜽m)​p​(𝜽m|𝒟)​𝑑𝜽mp(m(\textbf{x})|\mathcal{D})=\int p(m(\textbf{x})|{\bm{\theta}_{m}})\,p({\bm{\theta}_{m}}|\mathcal{D})\,d{\bm{\theta}_{m}}(7)

wherep​(m​(x)|𝜽m)p(m(\textbf{x})|{\bm{\theta}_{m}})is given by the forward propagation of the NN.
We perform Bayesian estimation ofp​(𝜽m|𝒟)p({\bm{\theta}_{m}}|\mathcal{D})in a form that enables integration (marginalization) over𝜽m{\bm{\theta}_{m}}, e.g., Monte Carlo integration with particle approximation, analytical integration with Gaussian approximation, or related approximations.
In this paper, we focus on particle approximation; i.e.,p​(𝜽m|𝒟)p({\bm{\theta}_{m}}|\mathcal{D})is estimated in the form of ensemble modeling.
Efficient Bayesian inference methods, such as HMC and ParVI, leverage−∇𝜽mlog⁡p​(𝜽m|𝒟)-\nabla_{\bm{\theta}_{m}}\log p(\bm{\theta}_{m}|\mathcal{D}), the gradient of the negative log-posterior PDF with respect to the estimated parameters.
This gradient must be evaluated subject to the PDE constraints (Equations1and2).

Thus, we compute the gradient−∇𝜽mlog⁡p​(𝜽m|𝒟)-\nabla_{\bm{\theta}_{m}}\log p(\bm{\theta}_{m}|\mathcal{D})under the PDE constraints using the Lagrange multiplier method, also known as the adjoint method.
Let𝒥\mathcal{J}denote the loss function, with𝒥=−log⁡p​(𝜽m|𝒟)\mathcal{J}=-\log p(\bm{\theta}_{m}|\mathcal{D}).
To incorporate the PDE and boundary constraints, we introduce the continuous Lagrangian functionalℒc​(𝜽u,𝜽m,λℱ,λℬ)=𝒥​(𝜽u,𝜽m)+⟨λℱ,ℱ​(fu​(𝜽u),fm​(𝜽m))⟩Ω+⟨λℬ,ℬ​(fu​(𝜽u))⟩∂Ω,\mathcal{L}_{c}(\bm{\theta}_{u},\bm{\theta}_{m},\lambda_{\mathcal{F}},\lambda_{\mathcal{B}})=\mathcal{J}(\bm{\theta}_{u},\bm{\theta}_{m})+\left\langle\lambda_{\mathcal{F}},\,\mathcal{F}\bigl(f_{u}(\bm{\theta}_{u}),f_{m}(\bm{\theta}_{m})\bigr)\right\rangle_{\Omega}+\left\langle\lambda_{\mathcal{B}},\,\mathcal{B}\bigl(f_{u}(\bm{\theta}_{u})\bigr)\right\rangle_{\partial\Omega},(8)

whereλℱ\lambda_{\mathcal{F}}andλℬ\lambda_{\mathcal{B}}are the adjoint variables associated with the PDE and boundary constraints, respectively.
Here,⟨⋅,⋅⟩Ω\langle\cdot,\cdot\rangle_{\Omega}and⟨⋅,⋅⟩∂Ω\langle\cdot,\cdot\rangle_{\partial\Omega}denote appropriate duality pairings overΩ\Omegaand∂Ω\partial\Omega.
For notational simplicity, the spatial dependence offu​(𝜽u)f_{u}(\bm{\theta}_{u})andfm​(𝜽m)f_{m}(\bm{\theta}_{m})is omitted.
Taking the variation ofℒc\mathcal{L}_{c}with respect to𝜽u\bm{\theta}_{u}and𝜽m\bm{\theta}_{m}, we obtain the adjoint equations forλℱ\lambda_{\mathcal{F}}andλℬ\lambda_{\mathcal{B}}.
Subsequently,∇𝜽m𝒥\nabla_{\bm{\theta}_{m}}\mathcal{J}can be calculated using the solution of the adjoint equations.
See AppendixA.1for details of the derivation.

In conducting Bayesian estimation, we iteratively evaluate the gradient (Equation38) and update the weight parameters𝜽m{\bm{\theta}_{m}}.
By construction in the adjoint method, the PDE constraintsℱ​(fu​(𝜽u),fm​(𝜽m))=0\mathcal{F}\bigl(f_{u}(\bm{\theta}_{u}),f_{m}(\bm{\theta}_{m})\bigr)=0andℬ​(fu​(𝜽u))=0\mathcal{B}\bigl(f_{u}(\bm{\theta}_{u})\bigr)=0should be satisfied within numerical error at every iteration.
We conduct PINN training to minimize the loss for the PDE constraints (Equations1and2) for the current weight parameters𝜽mcurrent{\bm{\theta}_{m}}^{\rm current}, as𝜽u=arg​min𝜽uℒPDE​(𝜽u,𝜽mcurrent)+ℒboundary​(𝜽u)\displaystyle{\bm{\theta}_{u}}=\mathop{\rm arg~min}\limits_{{\bm{\theta}_{u}}}\mathcal{L}_{\rm PDE}({\bm{\theta}_{u}},{\bm{\theta}_{m}}^{\rm current})+\mathcal{L}_{\rm boundary}({\bm{\theta}_{u}})(9)

whereℒPDE​(𝜽u,𝜽mcurrent)≃∫Ω(ℱ​(u,m))2​𝑑Ω\displaystyle\mathcal{L}_{\rm PDE}({\bm{\theta}_{u}},{\bm{\theta}_{m}}^{\rm current})\simeq\int_{\Omega}\left(\mathcal{F}(u,m)\right)^{2}d\Omega(10)ℒboundary​(𝜽u)≃∫∂Ω(ℬ​(u))2​d​∂Ω.\displaystyle\mathcal{L}_{\rm boundary}({\bm{\theta}_{u}})\simeq\int_{\partial\Omega}\left(\mathcal{B}(u)\right)^{2}d\partial\Omega.(11)

These integrations are approximated by Monte Carlo integration using collocation points randomly generated inΩ\Omegaand on∂Ω\partial\Omega.
Because the weight parameters obtained in the previous iterative step are already close to the optimal values for the current step, a relatively small number of epochs is required for PINN training in each step.

This algorithm separates the iterative update, i.e., Bayesian estimation, for𝜽m{\bm{\theta}_{m}}from the PINN training for𝜽u{\bm{\theta}_{u}}.
This contrasts with commonly used PINN-based inversion methods, where𝜽m{\bm{\theta}_{m}}and𝜽u{\bm{\theta}_{u}}are simultaneously trained based on a single loss function defined asℒtotal=ℒPDE+ℒboundary+𝒥,\displaystyle\mathcal{L}_{\rm total}=\mathcal{L}_{\rm PDE}+\mathcal{L}_{\rm boundary}+\mathcal{J},(12)

where the negative log-posterior𝒥\mathcal{J}corresponds to data misfit in this context.
If we extend such a simultaneous approach to Bayesian estimation, the target posterior PDF would bep​(𝜽m,𝜽u|𝒟)p({\bm{\theta}_{m}},{\bm{\theta}_{u}}|\mathcal{D}).
However, adding𝜽u{\bm{\theta}_{u}}to the Bayesian estimation would substantially increase the dimension of the parameter space and introduce scale differences, which may lead to severe difficulties in the estimation.

## 3Function-space approaches to PINN-based Bayesian PDE-constrained inversion

## 3.1Approach 1: Functional-prior-informed Bayesian physics-informed neural network (FPI-BPINN)

In BNNs, the prior distribution of the weight parameters𝜽m{\bm{\theta}_{m}}is typically set to a simple distribution such as an independent and identically distributed (IID) normal distribution.
However, such a prior is known to be difficult to interpret in the function space of the NN and often leads to uncontrolled adverse effects in the estimation resultsWang et al. (2019); Matsubara et al. (2021).
Instead, we define a plausible stochastic process in the function space of the NN and trainp​(𝜽m)p({\bm{\theta}}_{m})based on it.
The stochastic behavior of the output function of the trained NN is expected to become similar to that of the prescribed function-space stochastic process.
This follows the approach proposed in the general BNN context byTran et al. (2022).
We apply this learned prior PDF to PINN-based Bayesian PDE-constrained inversion. We term this approach FPI-BPINN.

We assume an independent normal distribution for the prior PDF of the weight parameters𝜽m{\bm{\theta}}_{m}, asp​(𝜽m)=𝒩​(𝝁,diag​(𝝈2)),\displaystyle p({\bm{\theta}}_{m})=\mathcal{N}(\bm{\mu},\text{diag}(\bm{\sigma}^{2})),(13)

where𝝁\bm{\mu}and𝝈\bm{\sigma}are the mean and standard deviation of the prior PDF, respectively.
Both have the same dimension as the number of weight parameters𝜽m{\bm{\theta}}_{m}.diag​(⋅)\text{diag}(\cdot)is a diagonal matrix whose diagonal elements are given by the input vector.
Let𝒮​𝒫​(ψ)\mathcal{SP}(\psi)denote the target stochastic process defined in the function space of the NN and parameterized byψ\psi.
We learn𝝁\bm{\mu}and𝝈\bm{\sigma}so thatp​(𝜽m)p({\bm{\theta}}_{m})behaves similarly to𝒮​𝒫​(ψ)\mathcal{SP}(\psi).
In most cases, a Gaussian process is the first candidate for the target stochastic process, i.e.,𝒮​𝒫​(ψ)\mathcal{SP}(\psi)=𝒢​𝒫​(μ𝒢​𝒫​(x),k𝒢​𝒫​(x,x′))\mathcal{GP}(\mu_{\mathcal{GP}}(\textbf{x}),k_{\mathcal{GP}}(\textbf{x},\textbf{x}^{\prime})), whereμ𝒢​𝒫​(x)\mu_{\mathcal{GP}}(\textbf{x})andk𝒢​𝒫​(x,x′)k_{\mathcal{GP}}(\textbf{x},\textbf{x}^{\prime})are the mean function and kernel function, respectively.
A widely used kernel function is the radial basis function (RBF) kernel, which we define ask𝒢​𝒫​(x,x′)=a2​exp⁡(−1l𝒢​𝒫2​‖x−x′‖2),\displaystyle k_{\mathcal{GP}}(\textbf{x},\textbf{x}^{\prime})=a^{2}\exp\left(-\frac{1}{l_{\mathcal{GP}}^{2}}\|\textbf{x}-\textbf{x}^{\prime}\|^{2}\right),(14)

wherel𝒢​𝒫l_{\mathcal{GP}}is the correlation length scale andaais the amplitude of the kernel function, corresponding to the standard deviation of the marginal probability.

Tran et al. (2022)proposed using the Wasserstein distance as a metric for measuring the discrepancy between two probability distributions to construct the loss function for learning.
Instead, we adopt the maximum mean discrepancy (MMD), primarily for computational and implementation simplicity.
MMD is calculated for random samples taken fromp​(𝜽m)p({\bm{\theta}}_{m})and𝒮​𝒫​(ψ)\mathcal{SP}(\psi), asℒMMD=1N2​∑i=1N∑j=1NkMMD​(fm(i),fm(j))−2N2​∑i=1N∑j=1NkMMD​(fm(i),m𝒮​𝒫(j))+1N2​∑i=1N∑j=1NkMMD​(m𝒮​𝒫(i),m𝒮​𝒫(j)),\displaystyle\mathcal{L}_{\rm MMD}=\frac{1}{N^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N}k_{\rm MMD}(f_{m}^{(i)},f_{m}^{(j)})-\frac{2}{N^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N}k_{\rm MMD}(f_{m}^{(i)},m_{\mathcal{SP}}^{(j)})+\frac{1}{N^{2}}\sum_{i=1}^{N}\sum_{j=1}^{N}k_{\rm MMD}(m_{\mathcal{SP}}^{(i)},m_{\mathcal{SP}}^{(j)}),(15)

where{fm(i)}i=1N\{f_{m}^{(i)}\}_{i=1}^{N}and{m𝒮​𝒫(j)}j=1N\{m_{\mathcal{SP}}^{(j)}\}_{j=1}^{N}denote the sets of random samples drawn fromp​(θm)p(\theta_{m})and𝒮​𝒫​(ψ)\mathcal{SP}(\psi), respectively.
Here,kMMD​(⋅,⋅)k_{\rm MMD}(\cdot,\cdot)represents a positive definite kernel function, for which we use the RBF kernel in this study.
The reader should be careful not to confusekMMD​(⋅,⋅)k_{\rm MMD}(\cdot,\cdot)with the kernel functionk𝒢​𝒫​(⋅,⋅)k_{\mathcal{GP}}(\cdot,\cdot)used for the Gaussian process.
The disadvantage of MMD compared with the Wasserstein distance is that the bandwidth of the RBF kernel is introduced as a hyperparameter.
Determining it using the median heuristic works well in our cases.
We obtain𝝁\bm{\mu}and𝝈\bm{\sigma}that minimize the loss function by using a stochastic gradient descent algorithm.

After learning, the prior PDFp​(θm)p(\theta_{m})with the learned𝝁\bm{\mu}and𝝈\bm{\sigma}is incorporated into the Bayesian estimation of the weight parametersθm\theta_{m}.
It can be applied to any Bayesian estimation method that uses the gradient of the posterior PDF.
However, each evaluation of the gradient of the log posterior PDF is computationally expensive because it requires one adjoint computation and one PINN training step.
Thus, in practice, application to a Bayesian estimation method that requires many sequential evaluations of the gradient of the loss function, such as the Hamiltonian Monte Carlo (HMC) methodDuane et al. (1987), may not be promising.
We use Stochastic Gradient Langevin Dynamics (SGLD) plus a repulsion force (SGLD+R)Gallego and Insua (2018)to perform Bayesian estimation.
SGLD+R is a variant of SGLD, a widely used stochastic gradient Markov chain Monte Carlo (SG-MCMC) method, which introduces multiple chains and uses a repulsion force between the chains to prevent the particles from clustering.
From the viewpoint of ParVI, SGLD+R is interpreted as a variant of Stein variational gradient descent (SVGD)Liu and Wang (2016)that adds a noise term to the update equation.
The combination of a stochastic gradient and a repulsion force makes SGLD+R a highly parallelizable Bayesian estimation method, requiring a moderate number of sequential evaluations, typically on the order of10310^{3}, of the gradient of the loss function.
We apply a preconditioning technique to the update equation of SGLD+R to improve the convergence speed (see SectionA.2).

We summarize this two-stage FPI-BPINN procedure in Algorithm1.

## 3.2Approach 2: Function-space particle-based variational inference for PINN (fParVI-PINN)

The second approach, which we term fParVI-PINN, formulates and performs Bayesian estimation directly for the NN output values at selected evaluation points in function space, asp​(m|𝒟)=p​(𝒟|m)​p​(m)p​(𝒟)∝p​(𝒟|m)​p​(m),\displaystyle p(\textbf{m}|\mathcal{D})=\frac{p(\mathcal{D}|\textbf{m})\,p(\textbf{m})}{p(\mathcal{D})}\propto p(\mathcal{D}|\textbf{m})\,p(\textbf{m}),(16)

wherem={fm​(𝐱i)}i=1Nd\textbf{m}=\{f_{m}(\mathbf{x}_{i})\}_{i=1}^{N_{d}}denotes the output values of the NN atNdN_{d}evaluation points.
In fact, this equation appears similar to ordinary Bayesian estimation with a grid-based representation of the parameter field.
fParVIWang et al. (2019)performs Bayesian estimation defined in function space, while using an NN-based parameterization.
fParVI calculates the update vector of ParVI in function space and converts it to the weight space using the Jacobian matrix of the NN.
In the case of SVGD, the most widely used instance of ParVI, the update vector for fParVI is given as𝜽m​il+1=𝜽m​il+ϵl​∂𝐦i∂𝜽m​il⊤​ϕ​(mil+1).\displaystyle\bm{\theta}_{m\,i}^{l+1}=\bm{\theta}_{m\,i}^{l}+\epsilon_{l}\frac{\partial{\bf m}_{i}}{\partial\bm{\theta}_{m\,i}^{l}}^{\top}\bm{\phi}\left(\textbf{m}_{i}^{l+1}\right).(17)ϕ​(𝐦)=1n​∑j=1n{k​(𝐦jl,𝐦)​∇𝐦jllog⁡P​(𝐦jl|𝒟)+∇𝐦jlk​(𝐦jl,𝐦)},\displaystyle\bm{\phi}(\mathbf{m})=\frac{1}{n}\sum_{j=1}^{n}\{k(\mathbf{m}_{j}^{l},\mathbf{m})\nabla_{\mathbf{m}_{j}^{l}}\log P(\mathbf{m}_{j}^{l}|\mathcal{D})+\nabla_{\mathbf{m}_{j}^{l}}k(\mathbf{m}_{j}^{l},\mathbf{m})\},(18)

This algorithm avoids introducingp​(𝜽m)p(\bm{\theta}_{m})into the Bayesian estimation but instead directly incorporates the prior PDF in function space,p​(m)p(\textbf{m}).
For example, we can apply a Gaussian process, for which the mean and covariance are far more controllable and physically interpretable, top​(m)p(\textbf{m}).∇𝐦jllog⁡P​(𝐦jl|𝒟)\nabla_{\mathbf{m}_{j}^{l}}\log P(\mathbf{m}_{j}^{l}|\mathcal{D})can be calculated by slightly modifying the adjoint-method formulation given in Section2.2.

We summarize this learning procedure in Algorithm2.
Although the basic idea of fParVI-PINN was introduced inAgata et al. (2023), we newly clarify why it is necessary to introduce random Fourier features (RFF) to represent a Gaussian process in function space, as shown in the following subsection.
We also summarize the comparison among the weight-space Bayesian PINNs (e.g.,Yang et al. (2021)), FPI-BPINN, and fParVI-PINN in Fig.1.

## 3.3Importance of random Fourier features in representing Gaussian functional priors

We assume the use of a Gaussian process to provide the prior PDFp​(𝜽m)p({\bm{\theta}}_{m})for FPI-BPINN andp​(m)p(\textbf{m})for fParVI-PINN.
Both methods require the PDE-parameter NN to represent a Gaussian process in function space.
It has been reported that a simple fully-connected NN (FCNN) has difficulty learning functional Gaussian processes in certain situations, and that introducing a periodic activation function based on trigonometric functions is effective for improving the learningSendera et al. (2025).
Inspired by their work, we introduce random Fourier featuresTancik et al. (2020)into the PDE-parameter NN to improve its ability to represent Gaussian processes.
An FCNN with RFF is formally defined asfRFF​(x;𝜽)=fL∘fL−1∘⋯∘f1​(γ​(x)).\displaystyle f_{\mathrm{RFF}}(\textbf{x};\bm{\theta})=f_{L}\circ f_{L-1}\circ\cdots\circ f_{1}\bigl(\gamma(x)\bigr).(19)

whereγ​(x):=[cos⁡(2​π​Bx),sin⁡(2​π​Bx)],\displaystyle\gamma(x):=\left[\cos(2\pi\textbf{Bx}),\,\sin(2\pi\textbf{Bx})\right],(20)Bi​j∼𝒩​(0,τ2),\displaystyle B_{ij}\sim\mathcal{N}(0,\tau^{2}),(21)fℓ​(𝐡)=ψ​(𝐖ℓ​𝐡+𝐛ℓ),\displaystyle f_{\ell}(\mathbf{h})=\psi\left(\mathbf{W}_{\ell}\mathbf{h}+\mathbf{b}_{\ell}\right),(22)

wherefℓ​(⋅)f_{\ell}(\cdot)is the neural network function in theℓ\ell-th layer,ψ​(⋅)\psi(\cdot)is the activation function, and𝐖ℓ\mathbf{W}_{\ell}and𝐛ℓ\mathbf{b}_{\ell}are the weight matrix and bias vector in theℓ\ell-th layer, respectively.𝜽={𝐖1,𝐛1,𝐖2,𝐛2,⋯,𝐖L,𝐛L}\bm{\theta}=\{\mathbf{W}_{1},\mathbf{b}_{1},\mathbf{W}_{2},\mathbf{b}_{2},\cdots,\mathbf{W}_{L},\mathbf{b}_{L}\}denotes the weight parameters of the NN.𝐡\mathbf{h}is the input vector to theℓ\ell-th layer.
Although the characteristic frequencyτ\tauis usually treated as a hyperparameter, we set it so that the output function is well adapted to the target Gaussian process.
Such aτ\taucan be derived by comparing the Gaussian function whose bandwidth isτ\tauwith the Fourier transform of the kernel function of the target Gaussian processRasmussen and Williams (2006).
Specifically, in the case of the RBF kernel, we set it asτ=12​π​l𝒢​𝒫.\displaystyle\tau=\frac{1}{\sqrt{2}\pi l_{\mathcal{GP}}}.(23)

See AppendixA.3for details of the derivation.

We demonstrate an example of learning a 1D Gaussian process withl𝒢​𝒫=0.15l_{\mathcal{GP}}=0.15(Fig.2(a)) using an FCNN with and without RFF.
The FCNN employed two hidden layers and 30 hidden units per layer with the Mish activation functionMisra (2019).
The shape of𝐁\mathbf{B}was (15, 1) in the case of RFF.
We observed that the output of the FCNN with RFF based on weight samples obtained from the learned mean and standard deviation closely approximated samples from the target Gaussian process after learning.
The sample covariance matrix also showed good agreement with the target covariance matrix (Fig.2(b)).
By contrast, the FCNN without RFF failed to approximate the target Gaussian process well (Fig.2(c)).
The theoretically derived characteristic frequencyτ=1.5\tau=1.5yielded consistently better convergence of the MMD-based loss function than cases with arbitrarily chosenτ\tau(Fig.3).
Even in fParVI-PINN, which does not require this learning process, such a proper introduction of RFF is necessary to obtain a good approximation of the posterior PDF when a Gaussian-process prior is used.

## 4Numerical experiments

## 4.11D seismic traveltime tomography

To verify the accuracy of UQ using FPI-BPINN and fParVI-PINN, we applied the methods to the same synthetic 1D tomography tests as inAgata et al. (2023), in which a semi-analytical solution is available.
Seismic traveltime tomography is a technique used to determine the seismic velocity structure, i.e., the variation of seismic wave speeds, of the Earth’s interior from seismic traveltime observations, i.e., the duration required for a seismic wave to travel from its source to a seismometer.
The basic equation for determining the traveltime is the eikonal equation, which relates the spatial derivative of the traveltime field to the velocity structure as follows:|∇T​(x,xs)|2\displaystyle|\nabla T(x,x_{\mathrm{s}})|^{2}=\displaystyle=1v2​(x),∀x∈Ω\displaystyle\displaystyle\frac{1}{v^{2}(x)},\quad\forall\,x\in\Omega(24)T​(xs,xs)\displaystyle T(x_{\mathrm{s}},x_{\mathrm{s}})=\displaystyle=0,\displaystyle 0,(25)

whereΩ\Omegais aℝ1\mathbb{R}^{1}domain.T​(x,xs)T(x,x_{\mathrm{s}})is the traveltime at pointxxfrom sourcexsx_{\mathrm{s}},v​(x)v(x)is the velocity field defined onΩ\Omega, and∇\nabladenotes the gradient operator.TTandvvare represented byfuf_{u}andfmf_{m}, respectively.
The second equation defines the point source condition.
We considered the synthetic traveltime data set𝒟\mathcal{D}as𝒟={xi,xs​i,T​(xi,xs​i)}i=1Nd\mathcal{D}=\{x_{i},x_{{\rm s}\,i},T(x_{i},x_{{\rm s}\,i})\}_{i=1}^{N_{d}}(26)

which was used for the Bayesian estimation of the velocity structure.
We set a simple true velocity model, with a constant velocity of 1 km/s in the 1D domain defined by0≤x≤1.2​km0\leq x\leq 1.2\,{\rm km}, to test the UQ performance (see Fig.4(a), for instance).
We employed such a simple structure because the focus here is the ability of UQ, not the estimation of velocity.
We distributed ten points, serving both as receivers and sources, in two regions defined by the intervals0.2≤x≤0.4​km0.2\leq x\leq 0.4\,{\rm km}and0.8≤x≤1​km0.8\leq x\leq 1\,{\rm km}, using 0.05 km spacing.
We referred to the five points in each of the above intervals as Group 1 and Group 2, respectively.
We only considered ray paths of seismic waves between points within the same group.
Therefore, the number of traveltime data points was5×4+5×4=405\times 4+5\times 4=40.
No ray paths exist in the intervals0≤x≤0.2​km0\leq x\leq 0.2\,{\rm km},0.4≤x≤0.8​km0.4\leq x\leq 0.8\,{\rm km}, and1≤x≤1.2​km1\leq x\leq 1.2\,{\rm km}, in which the uncertainty of velocity estimation is expected to be closer to that given by the prior.
The constant velocity readily gives the synthetic traveltime between points analytically.
We did not add artificial noise to the traveltimes, to perform test experiments in an ideal situation.
We set the prior probability in the velocity space as a GP withμ𝒢​𝒫​(x)=1​km/s\mu_{\mathcal{GP}}(x)=1\,{\rm km/s}anda=0.1​km/sa=0.1\,{\rm km/s}.
We set two cases of the correlation length scale,l𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}and0.15​km0.15\,{\rm km}, for comparison.
The likelihood function was given as an IID zero-mean Gaussian noise distribution with standard deviationσe=5×10−3\sigma_{e}=5\times 10^{-3}s, and the data errors of the traveltime observations were assumed to be uncorrelated, yieldingp​(𝒟|m)=1Z​exp⁡(−12​σe2​∑i=140(fu​(xi,xs​i)−T​(xi,xs​i))2),p(\mathcal{D}|\textbf{m})=\frac{1}{Z}\exp\left(-\frac{1}{2\sigma_{e}^{2}}\sum_{i=1}^{40}\left(f_{u}(x_{i},x_{{\rm s}\,i})-T(x_{i},x_{{\rm s}\,i})\right)^{2}\right),(27)

whereiiis the index of the traveltime data andZZis the normalization constant.

In all the experiments, we used FCNNs with RFF.
We applied the Mish activation function to each layer, except for the output layer, where a linear activation was specified.
In the base case, we used two hidden layers for bothfuf_{u}representing the traveltime solution andfmf_{m}representing the velocity structure, with 50 and 30 hidden units per layer, respectively.
Forfmf_{m}, we also considered another setting with three hidden layers and 50 hidden units per layer for comparison.
For FPI-BPINN, we first learnedfmf_{m}from the functional prior of the Gaussian process.
The result of the learning example of the 1D Gaussian process presented in Section3.3was directly applied to the case withl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}.
We conducted training forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}in the same way.
We initialized𝜽m\bm{\theta}_{m}based on the initial𝝁{\bm{\mu}}and𝝈{\bm{\sigma}}(see Algorithm1) and initialized𝜽u\bm{\theta}_{u}using He’s methodHe et al. (2015).
In the learning process of the prior, we used 140 equally distributed points in the domain−0.1≤x≤1.3​km-0.1\leq x\leq 1.3\,{\rm km}as data points.
We prepared 10,000 samples from the GP prior, of which we used 9,000 samples for training and 1,000 samples for validation.
The batch size was 1,000, and the number of epochsLpriorL_{\rm prior}was 50.
As discussed in Section3.1, we used preconditioned SGLD+R (pSGLD+R) for the Bayesian estimation of the weight parametersθm\theta_{m}.
We sampled using pSGLD+R with 16 particles forLpost=L_{\mathrm{post}}=2,000 steps, withnburnin=n_{\mathrm{burnin}}=1,000 steps considered as the burn-in period, except for the case of the NN with three hidden layers andl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}, in whichLpost=L_{\mathrm{post}}=3,000 andnburnin=n_{\mathrm{burnin}}=2000.
Samples were taken every 100 steps, resulting in 160 samples in total.
We fixed the step size of pSGLD+R to10−310^{-3}.
For fParVI-PINN, we adopted fSVGD with 128 particles.
We used the Adam optimizerKingma and Ba (2015)with an initial learning rate of10−210^{-2}to determineϵl\epsilon_{l}, and the number of iterationsLLfor fParVI-PINN was 1,500, except for the case of the NN with three hidden layers andl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}, in which the initial learning rate was 5×\times10-3andL=2,000L=2,000.
We initialized both𝜽m\bm{\theta}_{m}and𝜽u\bm{\theta}_{u}using He’s methodHe et al. (2015).
As a result, 128 samples were obtained.
Although the experimental setting for fParVI-PINN was basically the same as inAgata et al. (2023), we adjusted the setting for RFF following Equation23, as in FPI-BPINN.
In the experiments using both methods, we used full-batch traveltime data.
We took the evaluation points used to define𝐦\mathbf{m}using NNs and the collocation points for PINN training for𝜽u\bm{\theta}_{u}to be the same, and generated them in each iteration by random sampling in the target domain.
We used 200 evaluation points.
We conducted the PINN training using the L-BFGS algorithmLiu and Nocedal (1989)for 10 epochs in each iteration.
See AppendixA.4.1for details of the PINN training.

Linearized traveltime tomography estimates velocity perturbation from a reference model using a Taylor series expansion.
When a conjugate pair of the prior and posterior PDF is adopted, such as Gaussian distributions, Bayesian linear regression for linearized tomography provides a semi-analytical solution for the posterior PDF (seeAgata et al. (2023)).
We treated this solution as the ground truth of the posterior probability.

We first demonstrate the importance of taking a functional-prior-based approach when aiming for Bayesian estimation consistent with physical intuition, by contrasting it with Bayesian estimation based on the weight space of an NN.
In the semi-analytical solution of the functional-prior-based Bayesian estimation, the uncertainty in regions around Group 1 or Group 2, which are associated with ray paths, is relatively small (Fig.4(a)(b)).
The uncertainty elsewhere is larger because of the absence of ray paths.
As the spatial correlation increases froml𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}to0.15​km0.15\,{\rm km}, this uncertainty in the regions without ray paths decreases accordingly.
In this sense, we obtained UQ results that are consistent with physical intuition.
In the weight-space Bayesian estimation using an NN without RFF, we considered the IID normal distribution, which is simple and widely used, as the weight-space prior.
In this case, we set the standard deviation vector of the weight-space prior to𝝈=σ​1{\bm{\sigma}}=\sigma\textbf{1}, where1is a vector of ones.
We varied the value ofσ\sigmain the Bayesian estimations.
The change ofσ=\sigma=0.4 to 0.7 did not increase the uncertainty in the region between observation Groups 1 and 2 sufficiently (Fig.4(c)(d)).
The standard deviation in the region in these cases remained less than 0.05 km/s.
Considering that no ray paths pass through this region, it is reasonable to regard this as an underestimation.
Further increasingσ\sigmato 0.8 did not selectively enlarge the uncertainty between Groups 1 and 2.
Instead, the entire solution diverged (Fig.4(e)).
These results demonstrate that it is difficult to obtain UQ results consistent with physical intuition when taking a weight-prior-based approach to Bayesian estimation based on commonly adopted simple prior distributions.

Both FPI-BPINN and fParVI-PINN provided accurate results for functional-prior-based Bayesian estimation using neural networks.
In both cases ofl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}and0.15​km0.15\,{\rm km}, the results from FPI-BPINN and fParVI-PINN agreed well with the semi-analytical solution of the linearized tomography (Fig.5and6).
fParVI-PINN provided particularly good results, which can be attributed to the direct incorporation of the functional prior of the Gaussian process (Fig.5(a)-(d)).
Although these results are similar to those presented previouslyAgata et al. (2023), the accuracy was improved because of the theoretically optimal choice of the characteristic frequencyτ\tauin the RFF.
By contrast, FPI-BPINN with pSGLD+R yielded 160 samples and provided accurate results despite the smaller number of particles (16 particles) than in fParVI-PINN (128 particles and samples) (Fig.6(a)-(d)).
This is because the flexibility of FPI-BPINN in the choice of Bayesian estimation method allows for the use of an efficient Bayesian estimation method, such as pSGLD+R.
We also found that our fpBPINN methods are not very sensitive to the structure of the PDE-parameter NN, as demonstrated by the corresponding results obtained using an NN with three hidden layers and 50 hidden units per layer forfmf_{m}(Fig.5(e)(f) and6(e)(f)).
To evaluate the results more quantitatively, we calculated MMD, the same quantity used for the loss function in the prior training in FPI-BPINN, for each case to compare the accuracy of the results against the corresponding semi-analytical solution.
Both FPI-BPINN and fParVI-PINN yielded significantly smaller MMD values than the best-performing case of the weight-space IID prior without RFF, in whichσ=0.3\sigma=0.3was chosen by grid search for bothl𝒢​𝒫=0.075l_{\mathcal{GP}}=0.075andl𝒢​𝒫=0.15l_{\mathcal{GP}}=0.15(Table1).
The comparison also shows that fParVI-PINN overall resulted in better performance than FPI-BPINN.

Interestingly, applying the weight-space IID normal distribution prior to an NN with RFF yielded results close to those of functional-prior-based Bayesian estimation.
We considered two cases of the characteristic frequencyτ\tau, which were set based on the correlation lengthl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}andl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}.
These additional cases can be interpreted as partially functional-prior-informed.
Based on the best-performing standard deviationσ=0.7\sigma=0.7chosen for both values ofl𝒢​𝒫l_{\mathcal{GP}}by grid search, the UQ results showed a tendency similar to those of the semi-analytical solutions (Fig.7).
The MMD value was much smaller than that in the best case without RFF and nearly comparable to that of FPI-BPINN (Table1).
These results suggest that embedding frequency features into the neural network according to those of the functional-prior distributions is crucial for obtaining an accurate approximation of the target posterior PDF.

## 4.22D Darcy flow

We considered the estimation of the permeability field in a 2D Darcy flow problem and investigated the applicability of fpBPINN methods to more realistic problems.
The equations for Darcy’s law are given as follows:𝐱=(x,y)∈Ω=[0,1]2\displaystyle\mathbf{x}=(x,y)\in\Omega=[0,1]^{2}(28)−∇⋅(K​(𝐱)​∇u​(𝐱))=0,𝐱∈Ω\displaystyle-\nabla\cdot(K(\mathbf{x})\nabla u(\mathbf{x}))=0,\quad\mathbf{x}\in\Omega(29)

whereKKanduuare the permeability field and the pressure field defined on the 2D domainΩ\Omega, respectively.KKanduuare represented byfmf_{m}andfuf_{u}, respectively.
The boundary conditions are given as follows:u​(𝐱)=0,𝐱∈ΓL:={𝐱∈∂Ω|x=0}\displaystyle u(\mathbf{x})=0,\quad\mathbf{x}\in\Gamma_{L}:=\{\mathbf{x}\in\partial\Omega|x=0\}(30)u​(𝐱)=1,𝐱∈ΓR:={𝐱∈∂Ω|x=1}\displaystyle u(\mathbf{x})=1,\quad\mathbf{x}\in\Gamma_{R}:=\{\mathbf{x}\in\partial\Omega|x=1\}(31)∂u∂n​(𝐱)=0,𝐱∈ΓN:={𝐱∈∂Ω|y=0,1}\displaystyle\frac{\partial u}{\partial n}(\mathbf{x})=0,\quad\mathbf{x}\in\Gamma_{N}:=\{\mathbf{x}\in\partial\Omega|y=0,1\}(32)

The synthetic pressure and flux data set𝒟\mathcal{D}was given as follows:𝒟={𝐱iu,u​(𝐱iu)}i=1Nu∪{𝐱jq,qx​(𝐱jq)}j=1Nq,\displaystyle\mathcal{D}=\{\mathbf{x}_{i}^{u},u(\mathbf{x}_{i}^{u})\}_{i=1}^{N_{u}}\cup\{\mathbf{x}_{j}^{q},q_{x}(\mathbf{x}_{j}^{q})\}_{j=1}^{N_{q}},(33)

where𝐱iu\mathbf{x}_{i}^{u}and𝐱jq\mathbf{x}_{j}^{q}are the evaluation points for pressure and flux data, respectively.
We set a true permeability field (Fig.8(a)) and calculated the pressure field and flux using the finite difference method, with the results used as the synthetic data (Fig.8(b)).
No (semi-)analytical solution was available as a reference for this problem.
Instead, we varied the observation patterns and examined whether the resulting changes in the estimated fields were qualitatively reasonable, in order to assess the robustness of the proposed methods with respect to different data configurations.
In Pattern 1, we distributedNu=N_{u}=100 points randomly in the domain (Fig.8(e)) with a standard deviation of data errorηu=\eta_{u}=0.01.
In Pattern 2, we used the sameNuN_{u}points as in Pattern 1 (Fig.8(h)), but withηu=\eta_{u}=0.05.
In Pattern 3, we distributedNu=N_{u}=50 points in the bottom half of the domain (Fig.8(k)) with the sameηu=\eta_{u}=0.01.
To provide scale information for the permeability field, we also usedNq=N_{q}=10 points for flux data at thex=0x=0andx=1x=1boundaries of the domain (plotted asqxq_{x}in Fig.8(e), (h), and (k)) with data errorηq=\eta_{q}=0.05.
We added artificial Gaussian noise according to the data error level for all synthetic data.
We set the prior probability of the permeability field as a 2D GP withμ​(x)=2.4​km/s\mu(x)=2.4\,{\rm km/s},σa=0.8​km/s\sigma_{a}=0.8\,{\rm km/s}, andl𝒢​𝒫=0.3​kml_{\mathcal{GP}}=0.3\,{\rm km}.
The likelihood function was given as an IID zero-mean Gaussian noise distribution, written asp​(𝒟|m)=1Z​exp⁡(−12​ηu2​∑i=1Nu(fu​(xi)−u​(xi))2−12​ηq2​∑i=1Nq(fq​(xi)−qx​(xi))2),p(\mathcal{D}|\textbf{m})=\frac{1}{Z}\exp\left(-\frac{1}{2\eta_{u}^{2}}\sum_{i=1}^{N_{u}}(f_{u}(x_{i})-u(x_{i}))^{2}-\frac{1}{2\eta_{q}^{2}}\sum_{i=1}^{N_{q}}(f_{q}(x_{i})-q_{x}(x_{i}))^{2}\right),(34)

whereiiis the index of the pressure and flux data.fqf_{q}is an NN-based approximation of the flux, whose details are described in AppendixA.4.2.

Similarly to the 1D case, we used FCNNs with RFF with the Mish activation function.
We used NNs with two hidden layers and 50 hidden units per layer forfuf_{u}andfmf_{m}, which correspond to the pressure solution and permeability structure, respectively.
For FPI-BPINN, we first learnedfmf_{m}from the functional prior of the 2D Gaussian process withl𝒢​𝒫=0.3​kml_{\mathcal{GP}}=0.3\,{\rm km}.
The initialization strategy was the same as in the 1D case.
In every iteration of the learning process of the prior, we newly sampled 1,024 randomly distributed points in the domain.
1,024 samples from the GP prior for calculating the MMD were also taken at every iteration.
The number of epochsLpriorL_{\rm prior}was 2,000.
For FPI-BPINN, we conducted posterior sampling using pSGLD+R with 16 particles forLpost=L_{\mathrm{post}}=4,000 steps withnburnin=n_{\mathrm{burnin}}=2,000.
Samples were taken every 100 steps, resulting in 320 samples in total.
We fixed the step size of pSGLD+R to3×10−43\times 10^{-4}.
For fParVI-PINN, we used fGFSF, the function-space version of Gradient Flow with Smoothed Test Functions (GFSF,Liu et al. (2019)), which is a variant of fParVI.
The algorithm of GFSF is similar to that of SVGD, but the gradient term is not smoothed by the kernel as in SVGD.
This makes the computation of the derivative ofKKincluded in Equation29in the fParVI framework easier.
We used the Adam optimizerKingma and Ba (2015)with an initial learning rate of10−310^{-3}to determineϵl\epsilon_{l}, and the number of iterationsLLfor fParVI-PINN was 1,000.
The initialization strategy was the same as in the 1D case.
As a result, 128 samples were obtained.
In the experiments using both methods, we used full-batch pressure and flux data.
We took 2,000 evaluation points inΩ\Omegato define𝐦\mathbf{m}using NNs, and used the same points as the collocation points for PINN training for𝜽u\bm{\theta}_{u}.
We took 200 collocation points for the boundary conditions.
These points were generated in each iteration by random sampling in the domain.
We conducted the PINN training using the SOAP optimizerVyas et al. (2025), which has been reported to be effective for improving the convergence of PINNsWang et al. (2025), for 100 epochs in each iteration.
See AppendixA.4.2for details of the PINN training.

Using FPI-BPINN, we obtained samples of𝜽m\bm{\theta}_{m}and𝜽u\bm{\theta}_{u}, each of which outputsKKanduuat the grid evaluation points in the domain.
The posterior mean ofKKand the mean ofuucalculated from these samples corresponding to eachKKsample agreed well with the true field in Patterns 1 and 2 (Fig.8(c), (e), (f), and (h)).
On the other hand, Pattern 1 showed a significantly smaller standard deviation, which is a metric for uncertainty, than Pattern 2 except for the region near the flux data.
This was a reasonable result reflecting the condition that the difference in the noise level of the pressure data was significant between Patterns 1 and 2, while that of the flux data was the same.
In Pattern 3, which lacks pressure data in the top half of the domain, the posterior mean ofKKand the mean ofuuagreed well only with the true field in the bottom half of the domain and in the region near the flux data.
The map of the standard deviation ofKKshowed a significant contrast between large and small values in the top and bottom halves of the domain, respectively.
Fig.9(a)(b) and (c)(d) show examples ofKKanduusamples for Patterns 1 and 3, respectively.
The larger variability ofKKanduuin Pattern 3 than in Pattern 1, in particular in the top half of the domain, is apparent.
The distribution ofuudoes not vary significantly among the samples in Pattern 1, reflecting the data coverage over the whole domain.
In the same way, we obtained samples ofKKanduuusing fParVI-PINN and calculated the posterior mean and standard deviation.
The results show a similar tendency to those of FPI-BPINN in all patterns (Fig.10and Fig.11).
The rough distribution patterns observed in the standard deviation ofKKin FPI-BPINN are reduced in fParVI-PINN.
We also observed such a difference in the 1D case, probably because of the different strategy for introducing the functional prior.

Overall, the comparison of the three observation patterns suggests that both FPI-BPINN and fParVI-PINN provided reasonable results for Bayesian estimation of the 2D permeability field under the constraints of the Darcy flow PDE.
It took about 18 hours to complete the calculations in each case of FPI-BPINN using eight NVIDIA A100 GPUs on Earth Simulator 4, made available by the Japan Agency for Marine-Earth Science and Technology (JAMSTEC).
In the case of fParVI-PINN, it took less than seven hours to complete the calculations using the same computational facilities.
Note that the computation codes still need to be optimized for further speedup.

## 5Discussion & Conclusion

In this study, we investigated Bayesian PDE-constrained inversion based on physics-informed neural networks from the viewpoint of functional priors. Physically meaningful prior assumptions are more naturally described in function space; therefore, we introduced a unified framework, fpBPINN. Within this framework, we considered two complementary approaches: FPI-BPINN, which learns a weight-space prior consistent with a prescribed functional prior and then performs Bayesian inference in weight space, and fParVI-PINN, which performs particle-based variational inference directly in function space. We also showed that, when Gaussian processes are used as functional priors, the introduction of random Fourier features is important for representing the corresponding frequency characteristics in the PDE-parameter NN.
Through one-dimensional seismic traveltime tomography and two-dimensional Darcy-flow permeability inversion, we demonstrated that both approaches provided accurate posterior estimates under PDE constraints. These findings suggest that functional-prior-based formulations provide a promising direction for uncertainty quantification in PINN-based inverse problems.

The two approaches considered in this study have complementary strengths and limitations in terms of prior representation, flexibility of posterior inference, and computational scalability.
As demonstrated by the numerical results for the one-dimensional traveltime tomography problem, fParVI-PINN can achieve accurate inference because the prior distribution in function space is incorporated analytically.
Moreover, fParVI-PINN has already been applied to a real-world three-dimensional problemAgata et al. (2026), suggesting that this approach has practical potential when sufficient parallel computational resources are available.
FPI-BPINN, on the other hand, offers a different type of flexibility. Once the weight prior has been learned from the functional prior, the subsequent inference follows the standard BNN framework. In principle, this allows us to adopt a wide range of existing Bayesian inference methods if the computational cost is affordable, including Hamiltonian Monte Carlo. In addition, because the prior-learning step in the present study is based on a sample-based MMD calculation, it may be possible to extend the framework so that priors are learned directly from discrete datasets. This strategy is analogous to approaches explored in Bayesian inference using generative modelsMeng et al. (2022); Li et al. (2025).
These features are in clear contrast to those of fParVI-PINN, which is inherently tied to ParVI and requires a closed-form representation of the functional prior. Conversely, for FPI-BPINN to become practical for larger problems, it will be necessary to reduce the cost of computing the MMD-based prior-learning loss and of generating samples from the functional prior. Improving these components is an important direction for future research.

We considered only Gaussian processes (GPs) as functional priors in all the experiments in this study. The main reason is that GPs are highly physically interpretable. Nevertheless, the proposed framework is not restricted to GPs. In principle, FPI-BPINN can be applied to any stochastic process from which samples can be generated, whereas fParVI-PINN can be applied when the prior can be described in closed form in function space.
The selection of hyperparameters in the functional prior, such as the correlation length and amplitude of the GP, was not investigated systematically in this study. This issue is important because such hyperparameters directly determine prior assumptions on smoothness, correlation scale, and variability of the unknown parameter field. A possible strategy is an empirical-Bayesian approach. For example, in applications of fParVI-PINN to real-world geophysical problemsAgata et al. (2025,2026), the hyperparameters were determined using the widely applicable Bayesian information criterion (WBIC)Watanabe (2013).

In the present study, we focused on the case in which only a single PDE parameter is unknown. In PINN-based inverse problems, however, multiple PDE parameters are often estimated simultaneously, and the corresponding NN has multiple outputs (e.g.,Yin et al. (2021); Kamali et al. (2023); Fukushima et al. (2025)). Extending the present framework to such settings appears to be conceptually straightforward, but its practical applicability to real problems remains to be examined.
In particular, when multiple PDE parameters are inferred simultaneously, an important issue is how to cope with the implicit correlation between the parameters imposed by sharing the same NN weight parameters.

## Acknowledgments

This study was supported by JSPS KAKENHI Grant Number 25K01084 and ERI JURP 2025-B-01 in Earthquake Research Institute, the University of Tokyo. The calculations were carried out using Earth Simulator at JAMSTEC.

## Appendix AAppendix

## A.1Derivation of the gradient of the loss function using the adjoint method

For ease of subsequent derivations, we present the discrete form of the Lagrangian asℒd​(𝜽u,𝜽m,𝝀ℱ,𝝀ℬ)=𝒥​(𝜽u,𝜽m)+∑i=1Nℱwiℱ​λℱ,i​ℱi​(𝜽u,𝜽m)+∑j=1Nℬwjℬ​λℬ,j​ℬj​(𝜽u),\mathcal{L}_{d}(\bm{\theta}_{u},\bm{\theta}_{m},\bm{\lambda}_{\mathcal{F}},\bm{\lambda}_{\mathcal{B}})=\mathcal{J}(\bm{\theta}_{u},\bm{\theta}_{m})+\sum_{i=1}^{N_{\mathcal{F}}}w_{i}^{\mathcal{F}}\lambda_{\mathcal{F},i}\,\mathcal{F}_{i}(\bm{\theta}_{u},\bm{\theta}_{m})+\sum_{j=1}^{N_{\mathcal{B}}}w_{j}^{\mathcal{B}}\lambda_{\mathcal{B},j}\,\mathcal{B}_{j}(\bm{\theta}_{u}),(35)

whereNℱN_{\mathcal{F}}andNℬN_{\mathcal{B}}are the numbers of interior and boundary collocation points, respectively, andwiℱw_{i}^{\mathcal{F}}andwjℬw_{j}^{\mathcal{B}}are quadrature weights.
The quantitiesℱi\mathcal{F}_{i}andℬj\mathcal{B}_{j}denote the PDE residual and boundary residual evaluated at the corresponding collocation points.
To derive the gradient with respect to𝜽m\bm{\theta}_{m}, we consider the total derivative ofℒd\mathcal{L}_{d}:d​ℒdd​𝜽m=∂ℒd∂𝜽m+∂ℒd∂𝜽u​d​𝜽ud​𝜽m+∂ℒd∂𝝀​d​𝝀d​𝜽m,\frac{d\mathcal{L}_{d}}{d\bm{\theta}_{m}}=\frac{\partial\mathcal{L}_{d}}{\partial\bm{\theta}_{m}}+\frac{\partial\mathcal{L}_{d}}{\partial\bm{\theta}_{u}}\frac{d\bm{\theta}_{u}}{d\bm{\theta}_{m}}+\frac{\partial\mathcal{L}_{d}}{\partial\bm{\lambda}}\frac{d\bm{\lambda}}{d\bm{\theta}_{m}},(36)

where𝝀={𝝀ℱ,𝝀ℬ}\bm{\lambda}=\{\bm{\lambda}_{\mathcal{F}},\bm{\lambda}_{\mathcal{B}}\}.
Since the forward solution approximately satisfies the PDE and boundary constraints at the collocation points, the term∂ℒd/∂𝝀\partial\mathcal{L}_{d}/\partial\bm{\lambda}vanishes.
The second term, however, contains the sensitivityd​𝜽u/d​𝜽md\bm{\theta}_{u}/d\bm{\theta}_{m}, whose explicit evaluation is computationally expensive when the dimension of𝜽m\bm{\theta}_{m}is large.
The key idea of the adjoint method is to choose𝝀\bm{\lambda}such that the dependence ond​𝜽u/d​𝜽md\bm{\theta}_{u}/d\bm{\theta}_{m}is eliminated.
This is achieved by satisfying the following condition:∂ℒd∂𝜽u=∂𝒥∂𝜽u+∑i=1Nℱwiℱ​λℱ,i​∂ℱi∂𝜽u+∑j=1Nℬwjℬ​λℬ,j​∂ℬj∂𝜽u:=𝟎.\frac{\partial\mathcal{L}_{d}}{\partial\bm{\theta}_{u}}=\frac{\partial\mathcal{J}}{\partial\bm{\theta}_{u}}+\sum_{i=1}^{N_{\mathcal{F}}}w_{i}^{\mathcal{F}}\lambda_{\mathcal{F},i}\frac{\partial\mathcal{F}_{i}}{\partial\bm{\theta}_{u}}+\sum_{j=1}^{N_{\mathcal{B}}}w_{j}^{\mathcal{B}}\lambda_{\mathcal{B},j}\frac{\partial\mathcal{B}_{j}}{\partial\bm{\theta}_{u}}:=\bm{0}.(37)

Once𝝀\bm{\lambda}is obtained by solving this equation, the total derivative reduces to∇𝜽m𝒥=d​ℒdd​𝜽m=∂ℒd∂𝜽m=∂𝒥∂𝜽m+∑i=1Nℱwiℱ​λℱ,i​∂ℱi∂𝜽m+∑j=1Nℬwjℬ​λℬ,j​∂ℬj∂𝜽m.\nabla_{\bm{\theta}_{m}}\mathcal{J}=\frac{d\mathcal{L}_{d}}{d\bm{\theta}_{m}}=\frac{\partial\mathcal{L}_{d}}{\partial\bm{\theta}_{m}}=\frac{\partial\mathcal{J}}{\partial\bm{\theta}_{m}}+\sum_{i=1}^{N_{\mathcal{F}}}w_{i}^{\mathcal{F}}\lambda_{\mathcal{F},i}\frac{\partial\mathcal{F}_{i}}{\partial\bm{\theta}_{m}}+\sum_{j=1}^{N_{\mathcal{B}}}w_{j}^{\mathcal{B}}\lambda_{\mathcal{B},j}\frac{\partial\mathcal{B}_{j}}{\partial\bm{\theta}_{m}}.(38)

We use the CGNR method to solve the adjoint equation (Equation37) and obtain𝝀\bm{\lambda}.

## A.2Preconditioning technique for SGLD+R

SGLD+R, proposed by Gallego & InsuaGallego and Insua (2018), can be understood as an interacting-particle extension of ordinary SGLD.
Whereas standard multiple-chain SGLD evolves each chain (particle) independently, SGLD+R introduces kernel-based interactions among particles so that they repel each other and do not collapse to the same mode.
As a result, the method improves the exploration of the posterior while retaining the stochastic noise term required for SGLD sampling.
From the viewpoint of SVGD, SGLD+R can be interpreted as SVGD augmented with a noise term so that the resulting interacting-particle dynamics constitutes a valid SG-MCMC sampler.
FollowingGallego and Insua (2018), let𝚯k:=[(𝜽m,1k)⊤,…,(𝜽m,npk)⊤]⊤\bm{\Theta}^{k}:=\left[(\bm{\theta}_{m,1}^{k})^{\top},\ldots,(\bm{\theta}_{m,n_{p}}^{k})^{\top}\right]^{\top}

be the concatenated vector of all particles, wherenpn_{p}is the number of particles andkkis the iteration index.
Then, the general interacting SGLD update is written as𝚯k+1=𝚯k−ϵk​[(𝐃k+𝐐k)​∇ℋ​(𝚯k)+𝚪k]+𝜼k,𝜼k∼𝒩​(𝟎,2​ϵk​𝐃k),\bm{\Theta}^{k+1}=\bm{\Theta}^{k}-\epsilon_{k}\left[(\mathbf{D}_{k}+\mathbf{Q}_{k})\nabla\mathcal{H}(\bm{\Theta}^{k})+\bm{\Gamma}_{k}\right]+\bm{\eta}_{k},\qquad\bm{\eta}_{k}\sim\mathcal{N}(\mathbf{0},2\epsilon_{k}\mathbf{D}_{k}),(39)

whereℋ\mathcal{H}denotes the total negative log-posterior energy of the particle system.
Here,𝐃k\mathbf{D}_{k}is the diffusion matrix induced by the particle interaction kernel,𝐐k\mathbf{Q}_{k}is a skew-symmetric curl matrix that appears in more general Hamiltonian-type variants, and𝚪k\bm{\Gamma}_{k}is the correction term required in the SGLD framework so that the target distribution is preserved.
In SGLD+R, the repulsive force is encoded through the kernel-dependent structure of𝐃k\mathbf{D}_{k}and𝚪k\bm{\Gamma}_{k}.
When the noise term is omitted, the update is equivalent to that of SVGD.
For the detailed definitions of𝐃k\mathbf{D}_{k},𝐐k\mathbf{Q}_{k}, and𝚪k\bm{\Gamma}_{k}, we refer the reader toGallego and Insua (2018).

In our implementation, we use the SGLD+R case of this framework and set𝐐k=𝟎\mathbf{Q}_{k}=\mathbf{0}.
To improve convergence, we further introduce a diagonal preconditioner in the same spirit as preconditioned SGLD.
For each particle, we compute the gradient of the negative log-posterior,𝐠ik:=∇𝜽m,ik𝒥,\mathbf{g}_{i}^{k}:=\nabla_{\bm{\theta}_{m,i}^{k}}\mathcal{J},(40)

and form the moving average of the particle-averaged squared gradients as𝐯k:=β​𝐯k−1+(1−β)​1np​∑i=1np(𝐠ik⊙𝐠ik),\mathbf{v}^{k}:=\beta\mathbf{v}^{k-1}+(1-\beta)\frac{1}{n_{p}}\sum_{i=1}^{n_{p}}\left(\mathbf{g}_{i}^{k}\odot\mathbf{g}_{i}^{k}\right),(41)

whereβ∈[0,1)\beta\in[0,1)is the decay rate and⊙\odotdenotes the elementwise product.
Using this quantity, we define a parameter-wise diagonal preconditioner𝐆k:=diag​((𝐯k+λ​𝟏)−1),\mathbf{G}_{k}:={\rm diag}\left(\left(\sqrt{\mathbf{v}^{k}}+\lambda\mathbf{1}\right)^{-1}\right),(42)

whereλ>0\lambda>0is a small constant for numerical stability.
This is analogous to RMSprop: parameters with persistently large gradients are updated more conservatively, while flatter directions are assigned larger effective step sizes.

To apply this preconditioner to the whole interacting particle system, we define𝐆¯k:=𝐈np⊗𝐆k,\bar{\mathbf{G}}_{k}:=\mathbf{I}_{n_{p}}\otimes\mathbf{G}_{k},(43)

and replace the diffusion matrix in Equation39by𝐃~k:=𝐆¯k​𝐃k.\tilde{\mathbf{D}}_{k}:=\bar{\mathbf{G}}_{k}\mathbf{D}_{k}.(44)

Correspondingly, the preconditioned SGLD+R update is written as𝚯k+1=𝚯k−ϵk​[𝐃~k​∇ℋ​(𝚯k)+𝚪~k]+𝜼~k,𝜼~k∼𝒩​(𝟎,2​ϵk​𝐃~k),\bm{\Theta}^{k+1}=\bm{\Theta}^{k}-\epsilon_{k}\left[\tilde{\mathbf{D}}_{k}\nabla\mathcal{H}(\bm{\Theta}^{k})+\tilde{\bm{\Gamma}}_{k}\right]+\tilde{\bm{\eta}}_{k},\qquad\tilde{\bm{\eta}}_{k}\sim\mathcal{N}(\mathbf{0},2\epsilon_{k}\tilde{\mathbf{D}}_{k}),(45)

where𝚪~k\tilde{\bm{\Gamma}}_{k}is the corresponding correction term associated with𝐃~k\tilde{\mathbf{D}}_{k}in the same sense as𝚪k\bm{\Gamma}_{k}is associated with𝐃k\mathbf{D}_{k}.
The adaptive update of𝐆k\mathbf{G}_{k}is used only during the burn-in period.
After burn-in, the fixed preconditioner, denoted by𝐃~k∗\tilde{\mathbf{D}}_{k}^{\ast}, is used in Equation45instead of𝐃~k\tilde{\mathbf{D}}_{k}.

## A.3Derivation of the characteristic frequency of the random Fourier features

To determine the characteristic frequency of the random Fourier features (RFF), we first confirm the definition used byTancik et al. (2020). In Section 3.2 of their paper, the RFF mapping is defined asγ​(𝐯):=[cos⁡(2​π​𝐁𝐯),sin⁡(2​π​𝐁𝐯)]T,\gamma(\mathbf{v}):=\left[\cos(2\pi\mathbf{B}\mathbf{v}),\sin(2\pi\mathbf{B}\mathbf{v})\right]^{T},(46)

where each element of𝐁\mathbf{B}is sampled from𝒩​(0,τ2)\mathcal{N}(0,\tau^{2}). We derive a theoretical guideline for choosingτ\taufrom the length scale of the target Gaussian process. Suppose that the desired Gaussian process is defined by the RBF kernelk​(x):=exp⁡(−x2l2),k(x):=\exp\left(-\frac{x^{2}}{l^{2}}\right),(47)

wherellis the length scale controlling smoothness. By Bochner’s theorem, the sampling distribution of the RFF should match the power spectral density, namely the Fourier transform of the kernel. Using the Fourier-transform conventionℱ​{g​(t)}​(f):=∫g​(t)​e−i​2​π​f​t​𝑑t,\mathcal{F}\{g(t)\}(f):=\int g(t)e^{-i2\pi ft}\,dt,(48)

the Fourier transform of the RBF kernelRasmussen and Williams (2006)isℱ​{exp⁡(−x2l2)}​(f)=π​l​exp⁡(−π2​l2​f2).\mathcal{F}\left\{\exp\left(-\frac{x^{2}}{l^{2}}\right)\right\}(f)=\sqrt{\pi}l\exp\left(-\pi^{2}l^{2}f^{2}\right).(49)

Ignoring the constant factor with respect toff, this expression is proportional to the probability density of a Gaussian distribution with zero mean and standard deviationτf\tau_{f},exp⁡(−f22​τf2).\exp\left(-\frac{f^{2}}{2\tau_{f}^{2}}\right).(50)

By comparing the exponents, we obtainf22​τf2=π2​l2​f2,\frac{f^{2}}{2\tau_{f}^{2}}=\pi^{2}l^{2}f^{2},(51)

which givesτf2=12​π2​l2.\tau_{f}^{2}=\frac{1}{2\pi^{2}l^{2}}.(52)

Therefore, the bandwidth of the RFF is determined asτ:=τf:=12​π​l.\tau:=\tau_{f}:=\frac{1}{\sqrt{2}\pi l}.(53)

This relation shows that the bandwidth parameter of the RFF layer should be chosen as the standard deviation of the frequency distribution corresponding to the target Gaussian-process length scale.

## A.4PINN training algorithms

## A.4.11D eikonal equation

In the 1D problem considered here, the spatial coordinate is the scalarx∈Ω⊂ℝx\in\Omega\subset\mathbb{R}.
The eikonal equation (Equation24) corresponds to the PDE constraintℱ​(u,m)=0\mathcal{F}(u,m)=0(Equation1), withu=Tu=T(traveltime) andm=vm=v(seismic velocity), and the point source condition (Equation25) serves as the boundary condition.
To avoid singularities in the point source condition, we introduce the following factored form followingSmith et al. (2021); Waheed et al. (2021):T​(x,xs)=T0​(x,xs)​τ​(x,xs),\displaystyle T(x,x_{s})=T_{0}(x,x_{s})\,\tau(x,x_{s}),(54)

whereT0​(x,xs)T_{0}(x,x_{s})is defined asT0​(x,xs)=|x−xs|.\displaystyle T_{0}(x,x_{s})=\left|x-x_{s}\right|.(55)

This factorization automatically satisfies the point source condition, so that the boundary lossℒboundary\mathcal{L}_{\rm boundary}in Equation9is not required.
In 1D, the eikonal equation residual simplifies torEE\displaystyle r_{\rm EE}=\displaystyle=v​(x)−1|∂T/∂x​(x,xs)|,\displaystyle v(x)-\frac{1}{\left|\partial T/\partial x\,(x,x_{s})\right|},(56)

which corresponds toℱ​(u,m)\mathcal{F}(u,m)in Equation1.

The traveltime NNfuf_{u}and the velocity NNfmf_{m}are specified asT​(x,xs)\displaystyle T(x,x_{s})≃\displaystyle\simeqfu​(x,xs,𝜽u)\displaystyle f_{u}(x,x_{s},\bm{\theta}_{u})(57)=\displaystyle=T0​(x,xs)/fτ−1​(x,xs,𝜽u),\displaystyle T_{0}(x,x_{s})/f_{\tau^{-1}}(x,x_{s},\bm{\theta}_{u}),v​(x)\displaystyle v(x)≃\displaystyle\simeqfm​(x,𝜽m)\displaystyle f_{m}(x,\bm{\theta}_{m})(58)=\displaystyle=v0​(x)+fvptb​(x,𝜽m),\displaystyle v_{0}(x)+f_{v_{\rm ptb}}(x,\bm{\theta}_{m}),

wherefτ−1f_{\tau^{-1}}is an NN-based function approximating1/τ​(x,xs)1/\tau(x,x_{s}),v0​(x)v_{0}(x)is the reference velocity set by the user, andfvptb​(x,𝜽m)f_{v_{\rm ptb}}(x,\bm{\theta}_{m})approximates the velocity perturbation.
We approximated1/τ1/\tauandvptbv_{\rm ptb}using NNs, instead of directly computingτ\tauandvvas done in previous studiesSmith et al. (2021); Waheed et al. (2021), to improve convergence performance.
We used fully connected feed-forward networks to implement bothfτ−1f_{\tau^{-1}}andfvptbf_{v_{\rm ptb}}.
Further, the reciprocity condition (i.e.,T​(x,xs)=T​(xs,x)T(x,x_{s})=T(x_{s},x)) was imposed followingGrubas et al. (2023)by using12​(fτ−1​(x,xs,𝜽u)+fτ−1​(xs,x,𝜽u))\frac{1}{2}\left(f_{\tau^{-1}}(x,x_{s},\bm{\theta}_{u})+f_{\tau^{-1}}(x_{s},x,\bm{\theta}_{u})\right)instead offτ−1​(x,xs,𝜽u)f_{\tau^{-1}}(x,x_{s},\bm{\theta}_{u})in Equation57to improve the convergence of the eikonal equation solution.

In the PINN training step (Equation9), with𝜽m\bm{\theta}_{m}fixed, the traveltime NN is trained by minimizingℒPDE\displaystyle\mathcal{L}_{\rm PDE}=\displaystyle=α​∑i=1Nc(fm​(xc(i);𝜽m)−1|∂fu/∂x​(xc(i),xs(i);𝜽u)|)2,\displaystyle\alpha\sum_{i=1}^{N_{c}}\left(f_{m}(x_{c}^{(i)};\bm{\theta}_{m})-\frac{1}{\left|\partial f_{u}/\partial x\,(x_{c}^{(i)},x_{s}^{(i)};\bm{\theta}_{u})\right|}\right)^{2},(59)

whereNcN_{c}is the number of collocation points,xcx_{c}denotes their coordinates, andα\alphais a loss weight typically set to1/Nc1/N_{c}.
The collocation points are selected randomly within the 1D target domainΩ\Omegaand serve as the evaluation points for the PDE residualsRaissi et al. (2019).

## A.4.22D Darcy’s law

In the 2D problem, the spatial coordinate is𝐱=(x,y)∈Ω=[0,1]2\mathbf{x}=(x,y)\in\Omega=[0,1]^{2}.
The Darcy flow equation (Equation29) corresponds to the PDE constraintℱ​(u,m)=0\mathcal{F}(u,m)=0(Equation1), withuudenoting the pressure field andm=Km=Kdenoting the permeability field.
The PDE residual is given byrDarcy\displaystyle r_{\rm Darcy}=\displaystyle=−∇⋅(K​(𝐱)​∇u​(𝐱))\displaystyle-\nabla\cdot\bigl(K(\mathbf{x})\,\nabla u(\mathbf{x})\bigr)(60)=\displaystyle=−∂K∂x​∂u∂x−∂K∂y​∂u∂y−K​(∂2u∂x2+∂2u∂y2),\displaystyle-\frac{\partial K}{\partial x}\frac{\partial u}{\partial x}-\frac{\partial K}{\partial y}\frac{\partial u}{\partial y}-K\!\left(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}\right),

which corresponds toℱ​(u,m)\mathcal{F}(u,m)in Equation1.
All partial derivatives are evaluated by automatic differentiation.
The pressure NNfuf_{u}and the permeability NNfmf_{m}are specified asu​(𝐱)\displaystyle u(\mathbf{x})≃\displaystyle\simeqfu​(𝐱;𝜽u),\displaystyle f_{u}(\mathbf{x};\bm{\theta}_{u}),(61)K​(𝐱)\displaystyle K(\mathbf{x})≃\displaystyle\simeqfm​(𝐱;𝜽m),\displaystyle f_{m}(\mathbf{x};\bm{\theta}_{m}),(62)

where bothfuf_{u}andfmf_{m}are implemented as FCNNs with RFF and the Mish activation function, each having two hidden layers with 50 units per layer.

In the PINN training step (Equation9), with𝜽m\bm{\theta}_{m}fixed, the pressure NN is trained by minimizingℒPDE+ℒboundary\mathcal{L}_{\rm PDE}+\mathcal{L}_{\rm boundary}.
The PDE loss overNcN_{c}interior collocation points{𝐱c(i)}\{\mathbf{x}_{c}^{(i)}\}isℒPDE=1Nc​∑i=1Nc(rDarcy​(𝐱c(i);𝜽u,𝜽m))2.\displaystyle\mathcal{L}_{\rm PDE}=\frac{1}{N_{c}}\sum_{i=1}^{N_{c}}\left(r_{\rm Darcy}\!\left(\mathbf{x}_{c}^{(i)};\bm{\theta}_{u},\bm{\theta}_{m}\right)\right)^{2}.(63)

The boundary loss enforces the Dirichlet and Neumann boundary conditions usingNbN_{b}boundary collocation points{𝐱b(j)}\{\mathbf{x}_{b}^{(j)}\}:ℒboundary\displaystyle\mathcal{L}_{\rm boundary}=\displaystyle=1NbD​∑j∈ΓL∪ΓR(fu​(𝐱b(j);𝜽u)−gD​(𝐱b(j)))2\displaystyle\frac{1}{N_{b}^{D}}\sum_{j\in\Gamma_{L}\cup\Gamma_{R}}\Bigl(f_{u}\!\left(\mathbf{x}_{b}^{(j)};\bm{\theta}_{u}\right)-g_{D}\!\left(\mathbf{x}_{b}^{(j)}\right)\Bigr)^{2}(64)+1NbN​∑j∈ΓN(∂fu∂n​(𝐱b(j);𝜽u))2,\displaystyle+\;\frac{1}{N_{b}^{N}}\sum_{j\in\Gamma_{N}}\left(\frac{\partial f_{u}}{\partial n}\!\left(\mathbf{x}_{b}^{(j)};\bm{\theta}_{u}\right)\right)^{2},

wheregD​(𝐱)=0g_{D}(\mathbf{x})=0onΓL\Gamma_{L}andgD​(𝐱)=1g_{D}(\mathbf{x})=1onΓR\Gamma_{R},NbDN_{b}^{D}andNbNN_{b}^{N}are the numbers of Dirichlet and Neumann boundary collocation points, respectively,
and∂/∂n\partial/\partial ndenotes the outward normal derivative.
The flux used as supplementary observational data (Section4.2) is computed asfq​(𝐱;𝜽u,𝜽m)=−fm​(𝐱;𝜽m)​∂fu∂x​(𝐱;𝜽u),\displaystyle f_{q}\!\left(\mathbf{x};\bm{\theta}_{u},\bm{\theta}_{m}\right)=-f_{m}\!\left(\mathbf{x};\bm{\theta}_{m}\right)\,\frac{\partial f_{u}}{\partial x}\!\left(\mathbf{x};\bm{\theta}_{u}\right),(65)

and enters the negative log-posterior𝒥\mathcal{J}through the likelihood function.

## References
- Agata et al. (2023)Agata, R., Shiraishi, K., Fujie, G., 2023.Bayesian Seismic Tomography Based on Velocity-Space Stein Variational Gradient Descent for Physics-Informed Neural Network.IEEE Transactions on Geoscience and Remote Sensing 61, 1–17.doi:10.1109/TGRS.2023.3295414.
- Agata et al. (2025)Agata, R., Shiraishi, K., Fujie, G., 2025.Physics-informed deep learning quantifies propagated uncertainty in seismic structure and hypocenter determination.Scientific Reports 15, 1846.
- Agata et al. (2026)Agata, R., Shiraishi, K., Fujie, G., Bassett, D., 2026.Bayesian three-dimensional seismic travel-time tomography for active- and passive-source seismic data using physics-informed neural networks.in preparation .
- D’Angelo and Fortuin (2021)D’Angelo, F., Fortuin, V., 2021.Repulsive deep ensembles are Bayesian.Advances in Neural Information Processing Systems 34, 3451–3465.
- Duane et al. (1987)Duane, S., Kennedy, A.D., Pendleton, B.J., Roweth, D., 1987.Hybrid monte carlo.Physics letters B 195, 216–222.
- Fukushima et al. (2025)Fukushima, R., Kano, M., Hirahara, K., Ohtani, M., Im, K., Avouac, J.P., 2025.Physics-informed deep learning for estimating the spatial distribution of frictional parameters in slow slip regions.Journal of Geophysical Research: Solid Earth 130, e2024JB030256.
- Gallego and Insua (2018)Gallego, V., Insua, D.R., 2018.Stochastic gradient MCMC with repulsive forces.arXiv preprint arXiv:1812.00071 .
- Goodfellow et al. (2014)Goodfellow, I.J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., Bengio, Y., 2014.Generative adversarial nets.Advances in neural information processing systems 27.
- Grubas et al. (2023)Grubas, S., Duchkov, A., Loginov, G., 2023.Neural Eikonal solver: Improving accuracy of physics-informed neural networks for solving eikonal equation in case of caustics.Journal of Computational Physics 474, 111789.
- He et al. (2015)He, K., Zhang, X., Ren, S., Sun, J., 2015.Delving deep into rectifiers: Surpassing human-level performance on imagenet classification, in: Proceedings of the IEEE international conference on computer vision, pp. 1026–1034.
- Ho et al. (2020)Ho, J., Jain, A., Abbeel, P., 2020.Denoising diffusion probabilistic models.Advances in neural information processing systems 33, 6840–6851.
- Jordan et al. (1999)Jordan, M.I., Ghahramani, Z., Jaakkola, T.S., Saul, L.K., 1999.An introduction to variational methods for graphical models.Machine learning 37, 183–233.
- Kamali et al. (2023)Kamali, A., Sarabian, M., Laksari, K., 2023.Elasticity imaging using physics-informed neural networks: Spatial discovery of elastic modulus and Poisson’s ratio.Acta biomaterialia 155, 400–409.
- Kingma and Ba (2015)Kingma, D.P., Ba, J., 2015.Adam: A method for stochastic optimization, in: International Conference on Learning Representations.
- Kovachki and Stuart (2019)Kovachki, N.B., Stuart, A.M., 2019.Ensemble Kalman inversion: a derivative-free technique for machine learning tasks.Inverse Problems 35, 095005.
- Li et al. (2025)Li, Y., Zhang, H., Yan, Z., Alkhalifah, T., 2025.DiffusionInv: Prior-enhanced Bayesian Full Waveform Inversion using Diffusion models.arXiv preprint arXiv:2505.03138 .
- Liu et al. (2019)Liu, C., Zhuo, J., Cheng, P., Zhang, R., Zhu, J., 2019.Understanding and accelerating particle-based variational inference, in: International Conference on Machine Learning, PMLR. pp. 4082–4092.
- Liu and Nocedal (1989)Liu, D.C., Nocedal, J., 1989.On the limited memory BFGS method for large scale optimization.Mathematical programming 45, 503–528.
- Liu and Wang (2016)Liu, Q., Wang, D., 2016.Stein variational gradient descent: A general purpose bayesian inference algorithm.Advances in neural information processing systems 29.
- Matsubara et al. (2021)Matsubara, T., Oates, C.J., Briol, F.X., 2021.The ridgelet prior: A covariance function approach to prior specification for bayesian neural networks.Journal of Machine Learning Research 22, 1–57.
- Meng et al. (2022)Meng, X., Yang, L., Mao, Z., del Águila Ferrandis, J., Karniadakis, G.E., 2022.Learning functional priors and posteriors from data and physics.Journal of Computational Physics 457, 111073.
- Misra (2019)Misra, D., 2019.Mish: A self regularized non-monotonic neural activation function.arXiv preprint arXiv:1908.08681 .
- Pensoneault and Zhu (2024)Pensoneault, A., Zhu, X., 2024.Efficient bayesian physics informed neural networks for inverse problems via ensemble kalman inversion.Journal of Computational Physics 508, 113006.
- Pilar et al. (2025)Pilar, P., Heinonen, M., Wahlström, N., 2025.Repulsive Ensembles for Bayesian Inference in Physics-informed Neural Networks.arXiv preprint arXiv:2505.17308 .
- Raissi et al. (2019)Raissi, M., Perdikaris, P., Karniadakis, G.E., 2019.Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.Journal of Computational physics 378, 686–707.
- Rasmussen and Williams (2006)Rasmussen, C.E., Williams, C.K.I., 2006.Gaussian processes for machine learning.MIT Press.
- Röver et al. (2024)Röver, L., Schäfer, B., Plehn, T., 2024.PINNferring the Hubble function with uncertainties.arXiv preprint arXiv.2403.13899 .
- Rudner et al. (2022)Rudner, T.G., Chen, Z., Teh, Y.W., Gal, Y., 2022.Tractable function-space variational inference in Bayesian neural networks.Advances in Neural Information Processing Systems 35, 22686–22698.
- Sendera et al. (2025)Sendera, M., Sorkhei, A., Kuśmierczyk, T., 2025.Revisiting the Equivalence of Bayesian Neural Networks and Gaussian Processes: On the Importance of Learning Activations, in: Conference on Uncertainty in Artificial Intelligence, PMLR. pp. 3675–3700.
- Shukla et al. (2026)Shukla, K., Zou, Z., Kaeufer, T., Triantafyllou, M., Karniadakis, G.E., 2026.Uncertainty quantification in pinns for turbulent flows: Bayesian inference and repulsive ensembles.arXiv preprint arXiv:2604.17156 .
- Smith et al. (2021)Smith, J.D., Azizzadenesheli, K., Ross, Z.E., 2021.Eikonet: Solving the eikonal equation with deep neural networks.IEEE Transactions on Geoscience and Remote Sensing 59, 10685–10696.doi:10.1109/TGRS.2020.3039165.
- Sun and Wang (2020)Sun, L., Wang, J.X., 2020.Physics-constrained Bayesian neural network for fluid flow reconstruction with sparse and noisy data.Theoretical and Applied Mechanics Letters 10, 161–169.
- Sun et al. (2019)Sun, S., Zhang, G., Shi, J., Grosse, R., 2019.Functional variational Bayesian neural networks, in: International Conference on Learning Representations.
- Tancik et al. (2020)Tancik, M., Srinivasan, P., Mildenhall, B., Fridovich-Keil, S., Raghavan, N., Singhal, U., Ramamoorthi, R., Barron, J., Ng, R., 2020.Fourier features let networks learn high frequency functions in low dimensional domains.Advances in Neural Information Processing Systems 33, 7537–7547.
- Tran et al. (2022)Tran, B.H., Rossi, S., Milios, D., Filippone, M., 2022.All You Need is a Good Functional Prior for Bayesian Deep Learning.Journal of Machine Learning Research 23, 1–56.
- Vyas et al. (2025)Vyas, N., Morwani, D., Zhao, R., Shapira, I., Brandfonbrener, D., Janson, L., Kakade, S.M., 2025.SOAP: Improving and Stabilizing Shampoo using Adam for Language Modeling, in: The Thirteenth International Conference on Learning Representations.
- Waheed et al. (2021)Waheed, U.B., Haghighat, E., Alkhalifah, T., Song, C., Hao, Q., 2021.PINNeik: Eikonal solution using physics-informed neural networks.Computers & Geosciences 155, 104833.
- Wang et al. (2025)Wang, S., bhartari, A.K., Li, B., Perdikaris, P., 2025.Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective, in: The Thirty-ninth Annual Conference on Neural Information Processing Systems.URL:https://openreview.net/forum?id=iweeVl1RHU.
- Wang et al. (2019)Wang, Z., Ren, T., Zhu, J., Zhang, B., 2019.Function Space Particle Optimization for Bayesian Neural Networks, in: International Conference on Learning Representations.
- Watanabe (2013)Watanabe, S., 2013.A widely applicable bayesian information criterion.Journal of Machine Learning Research 14, 867–897.
- Yang et al. (2021)Yang, L., Meng, X., Karniadakis, G.E., 2021.B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data.Journal of Computational Physics 425, 109913.
- Yin et al. (2021)Yin, M., Zheng, X., Humphrey, J.D., Karniadakis, G.E., 2021.Non-invasive inference of thrombus material properties with physics-informed neural networks.Computer Methods in Applied Mechanics and Engineering 375, 113603.Algorithm 1FPI-BPINN with SGLD+R0:target stochastic process𝒮​𝒫​(ψ)\mathcal{SP}(\psi), negative log-posterior𝒥\mathcal{J}, PDE lossesℒPDE\mathcal{L}_{\rm PDE}andℒboundary\mathcal{L}_{\rm boundary}, numbers of prior-learning and posterior-inference iterationsLpriorL_{\rm prior}andLpostL_{\rm post}, number of particlesnpn_{p}0:posterior particles{𝜽m,iLpost}i=1np\{\bm{\theta}_{m,i}^{L_{\rm post}}\}_{i=1}^{n_{p}}approximatingp​(𝜽m|𝒟)p(\bm{\theta}_{m}|\mathcal{D})1:Stage I: Learning the prior distribution ofθm{\bm{\theta}_{m}}by MMD minimization2:Initialize𝝁=𝟎\bm{\mu}=\mathbf{0}; set𝝈\bm{\sigma}from He’s variance for weights and from one-tenth of that scale for biases3:forl=0,…,Lprior−1l=0,\ldots,L_{\rm prior}-1do4:Draw{𝜽m(i)}i=1N∼𝒩​(𝝁,diag​(𝝈2))\{\bm{\theta}_{m}^{(i)}\}_{i=1}^{N}\sim\mathcal{N}(\bm{\mu},{\rm diag}(\bm{\sigma}^{2}))5:Compute BNN samples{fm(i)}i=1N\{f_{m}^{(i)}\}_{i=1}^{N}by forward propagation6:Draw function-space samples{m𝒮​𝒫(i)}i=1N∼𝒮​𝒫​(ψ)\{m_{\mathcal{SP}}^{(i)}\}_{i=1}^{N}\sim\mathcal{SP}(\psi)7:EvaluateℒMMD\mathcal{L}_{\rm MMD}using Equation158:Update𝝁\bm{\mu}and𝝈\bm{\sigma}by stochastic gradient descent9:endfor10:Set learned prior parameters𝝁∗←𝝁\bm{\mu}^{\ast}\leftarrow\bm{\mu}and𝝈∗←𝝈\bm{\sigma}^{\ast}\leftarrow\bm{\sigma}11:Stage II: Posterior inference by particle-based SGLD+R12:Draw initial particles{𝜽m,i0}i=1np∼𝒩​(𝝁∗,diag​((𝝈∗)2))\{\bm{\theta}_{m,i}^{0}\}_{i=1}^{n_{p}}\sim\mathcal{N}(\bm{\mu}^{\ast},{\rm diag}((\bm{\sigma}^{\ast})^{2}))13:forl=0,…,Lpost−1l=0,\ldots,L_{\rm post}-1do14:fori=1,…,npi=1,\ldots,n_{p}do15:Obtain𝜽u,il\bm{\theta}_{u,i}^{l}by PINN training with fixed𝜽m,il\bm{\theta}_{m,i}^{l}:16:𝜽u,il=arg​min𝜽uℒPDE​(𝜽u,𝜽m,il)+ℒboundary​(𝜽u)\displaystyle\bm{\theta}_{u,i}^{l}=\mathop{\rm arg~min}\limits_{\bm{\theta}_{u}}\mathcal{L}_{\rm PDE}(\bm{\theta}_{u},\bm{\theta}_{m,i}^{l})+\mathcal{L}_{\rm boundary}(\bm{\theta}_{u})17:Solve the adjoint equation in Section 2.2 (Equation37)18:Compute𝐠il=∇𝜽m𝒥​(𝜽u,il,𝜽m,il)\mathbf{g}_{i}^{l}=\nabla_{\bm{\theta}_{m}}\mathcal{J}(\bm{\theta}_{u,i}^{l},\bm{\theta}_{m,i}^{l})using Equation3819:endfor20:Update{𝜽m,il}i=1np\{\bm{\theta}_{m,i}^{l}\}_{i=1}^{n_{p}}by one SGLD+R step using{𝐠il}i=1np\{\mathbf{g}_{i}^{l}\}_{i=1}^{n_{p}}21:endforAlgorithm 2fParVI-PINN0:functional priorp​(𝐦)p(\mathbf{m}), particle numbernpn_{p}, evaluation points𝐗v{\bf X}_{v}, posterior-inference iterationsLL0:particle approximation of the posterior distribution in function space and weight space,{(𝐦iL,𝜽m,iL)}i=1np\{(\mathbf{m}_{i}^{L},\bm{\theta}_{m,i}^{L})\}_{i=1}^{n_{p}}1:Initialize{𝜽m,i0}i=1np\{\bm{\theta}_{m,i}^{0}\}_{i=1}^{n_{p}}2:forl=0,…,L−1l=0,\ldots,L-1do3:fori=1,…,npi=1,\ldots,n_{p}do4:Evaluate the current function-space particle𝐦il=fm​(𝐗v;𝜽m,il)\mathbf{m}_{i}^{l}=f_{m}({\bf X}_{v};\bm{\theta}_{m,i}^{l})5:Obtain𝜽u,il\bm{\theta}_{u,i}^{l}by PINN training with fixed𝐦il\mathbf{m}_{i}^{l}(equivalently, fixed𝜽m,il\bm{\theta}_{m,i}^{l}):6:𝜽u,il=arg​min𝜽uℒPDE​(𝜽u,𝜽m,il)+ℒboundary​(𝜽u)\displaystyle\bm{\theta}_{u,i}^{l}=\mathop{\rm arg~min}\limits_{\bm{\theta}_{u}}\mathcal{L}_{\rm PDE}(\bm{\theta}_{u},\bm{\theta}_{m,i}^{l})+\mathcal{L}_{\rm boundary}(\bm{\theta}_{u})7:Compute the function-space gradient𝐠il=∇𝐦il𝒥\mathbf{g}_{i}^{l}=\nabla_{\mathbf{m}_{i}^{l}}\mathcal{J}by the adjoint method8:endfor9:Compute the fParVI update vectors{ϕ​(𝐦il)}i=1np\{\bm{\phi}(\mathbf{m}_{i}^{l})\}_{i=1}^{n_{p}}using Equation1810:fori=1,…,npi=1,\ldots,n_{p}do11:Update𝜽m,il+1\bm{\theta}_{m,i}^{l+1}fromϕ​(𝐦il)\bm{\phi}(\mathbf{m}_{i}^{l})through the Jacobian mapping by Equation1712:endfor13:endforTable 1:Comparison of MMD values between the semi-analytical solution and the posterior samples for different methods and two functional-prior settings.
The weight-space IID methods with and without RFF useσ=0.7\sigma=0.7andσ=0.3\sigma=0.3for bothl𝒢​𝒫=0.075l_{\mathcal{GP}}=0.075andl𝒢​𝒫=0.15l_{\mathcal{GP}}=0.15, respectively.FunctionalpriorFPI-BPINN(2 layers)FPI-BPINN(3 layers)fParVI-PINN(2 layers)fParVI-PINN(3 layers)IID w/o RFF(best case)IID w/ RFF(best case)l𝒢​𝒫=0.075l_{\mathcal{GP}}=0.0750.1230.1410.06840.07730.2160.160l𝒢​𝒫=0.15l_{\mathcal{GP}}=0.150.1440.1490.06580.06810.2110.151Figure 1:Schematic comparison among the weight-space Bayesian PINNs (BPINN, e.g.,Yang et al. (2021)), and the proposed fpBPINN approaches, including FPI-BPINN and fParVI-PINN. The items shown in purple are applied to both BPINN and FPI-BPINN.Figure 2:Prior learning results for a one-dimensional Gaussian process withl𝒢​𝒫=0.15l_{\mathcal{GP}}=0.15. (a) Samples from the target Gaussian process and the true covariance matrix. (b) Samples and sample covariance matrices from a BNN represented by an FCNN with RFF before prior learning. (c) Same as (b), but after prior learning. (d) Samples and sample covariance matrices from a BNN represented by an FCNN without RFF before prior learning. (e) Same as (d), but after prior learning.Figure 3:Convergence history of the MMD loss in prior learning for different characteristic frequenciesτ\tauof the RFF. The theoretically derived value,τ=1.5\tau=1.5, provides better convergence than arbitrarily chosen frequencies.Figure 4:Comparison of posterior velocity distributions for 1D seismic traveltime tomography between the semi-analytical results of functional-prior-based Bayesian estimation and those of weight-space Bayesian estimation using an IID Gaussian prior on an FCNN without RFF. Each panel shows the posterior mean and standard deviation of the velocity. (a) Semi-analytical posterior forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (b) Same as (a), but forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}. (c) Weight-space Bayesian PINN result withσ=0.4\sigma=0.4. (d) Same as (c), but withσ=0.7\sigma=0.7. (e) Same as (c), but withσ=0.8\sigma=0.8, where the scale of theyy-axis is enlarged to show that the entire solution diverges.Figure 5:Posterior velocity distributions estimated by fParVI-PINN for the 1D seismic traveltime tomography problem. Each panel shows the posterior mean and standard deviation of the velocity. (a) Semi-analytical posterior forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (b) Same as (a), but forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}. (c) fParVI-PINN result forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (d) fParVI-PINN result forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}. (e) fParVI-PINN result forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}obtained using a larger NN forfmf_{m}with three hidden layers and 50 hidden units per layer. (f) Same as (e), but forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}.Figure 6:Posterior velocity distributions estimated by FPI-BPINN for the 1D seismic traveltime tomography problem. Each panel shows the posterior mean and standard deviation of the velocity. (a) Semi-analytical posterior forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (b) Same as (a), but forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}. (c) FPI-BPINN result forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (d) FPI-BPINN result forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}. (e) FPI-BPINN result forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}obtained using a larger NN forfmf_{m}with three hidden layers and 50 hidden units per layer. (f) Same as (e), but forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}.Figure 7:Posterior velocity distributions for 1D seismic traveltime tomography obtained using simple zero-mean IID Gaussian priors in NN weight space with an FCNN with RFF. Each panel shows the posterior mean and standard deviation of the velocity. (a) Result with the characteristic frequency set forl𝒢​𝒫=0.075​kml_{\mathcal{GP}}=0.075\,{\rm km}. (b) Result with the characteristic frequency set forl𝒢​𝒫=0.15​kml_{\mathcal{GP}}=0.15\,{\rm km}.Figure 8:Results of 2D Darcy-flow permeability estimation obtained using FPI-BPINN for three observation patterns. (a) True permeability fieldKK. (b) Pressure fielduugenerated from the true permeability field. (c)–(e) Posterior mean ofKK, posterior standard deviation ofKK, and posterior mean ofuufor Pattern 1, respectively. (f)–(h) Same as (c)–(e), but for Pattern 2. (i)–(k) Same as (c)–(e), but for Pattern 3. The pressure observation points and boundary flux dataqxq_{x}used in each pattern are also shown in (e), (h), and (k).Figure 9:Examples of posterior samples obtained using FPI-BPINN for the 2D Darcy-flow problem. (a) Three samples of the permeability fieldKKfor Pattern 1. (b) The corresponding pressure field samplesuufor Pattern 1. (c) Three samples ofKKfor Pattern 3. (d) The corresponding samples ofuufor Pattern 3.Figure 10:Results of 2D Darcy-flow permeability estimation obtained using fParVI-PINN for three observation patterns. (a) True permeability fieldKK. (b) Pressure fielduugenerated from the true permeability field. (c)–(e) Posterior mean ofKK, posterior standard deviation ofKK, and posterior mean ofuufor Pattern 1, respectively. (f)–(h) Same as (c)–(e), but for Pattern 2. (i)–(k) Same as (c)–(e), but for Pattern 3. The pressure observation points and boundary flux dataqxq_{x}used in each pattern are also shown in (e), (h), and (k).Figure 11:Examples of posterior samples obtained using fParVI-PINN for the 2D Darcy-flow problem. (a) Three samples of the permeability fieldKKfor Pattern 1. (b) The corresponding pressure field samplesuufor Pattern 1. (c) Three samples ofKKfor Pattern 3. (d) The corresponding samples ofuufor Pattern 3.

## 


- 


Major funding support from
