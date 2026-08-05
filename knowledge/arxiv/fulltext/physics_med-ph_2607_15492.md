# Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation

**arXiv ID**: 2607.15492v1
**Authors**: Adarsh Pashikanti, Shrey Chowdhary, Alex Ho, Weizhen Li, Emilia Entcheva, Jan Christoph
**Published**: 2026-07-16
**Categories**: physics.med-ph, nlin.CD, physics.bio-ph
**HTML URL**: https://arxiv.org/html/2607.15492v1

## Abstract

The heart's contractions are triggered by action potential waves, which propagate through the cardiac muscle and exhibit diverse spatio-temporal dynamics during different heart rhythms. The dynamics are modeled with partial differential equations (PDEs) in cardiac electrophysiology simulations. However, fitting such models to measurement data to develop digital twins or patient-specific computer models is challenging. Here, we introduce differentiable cardiac electrophysiology simulations that can be fitted automatically to spatio-temporal measurement data of action potential waves in cardiac tissue. By comparing the simulated dynamics with the observation data, we define a loss function that is minimized via gradient-based optimization. Backpropagating the loss gradient through the differentiable PDE solver enables us to learn the parameters and recover the full dynamics, even with sparse, noisy, or partial observations. Implemented using both the finite-difference and smoothed particle hydrodynamics methods, our simulation framework can be applied to pixel-, voxel-, or point-based data, such as 2D or 3D slabs, or arbitrary shapes, such as the heart's ventricles. Using this methodology, we locate early activation sites inside a 3D bi-ventricular simulation geometry and fit a phenomenological model to imaging data of a voltage spiral wave in a cardiac monolayer cell culture. With experimental data, we employed a perceptual loss based on the Video Joint-Embedding Predictive Architecture, which enables fitting to noisy imaging data, and a generative diffusion model to estimate initial conditions and constrain solutions. Differentiable cardiac electrophysiology simulations could improve the diagnosis of rhythm abnormalities in patients and facilitate the development of personalized models or digital twins of the heart.

## Full Text

Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.15492v1 [physics.med-ph] 16 Jul 2026

## Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter EstimationAdarsh PashikantiThese authors contributed equally to this work.Cardiovascular Research Institute, University of California, San Francisco, San Francisco, USADepartment of Physics, University of California, Berkeley, Berkeley, USAShrey ChowdharyThese authors contributed equally to this work.Cardiovascular Research Institute, University of California, San Francisco, San Francisco, USAAlex HoThese authors contributed equally to this work.Cardiovascular Research Institute, University of California, San Francisco, San Francisco, USAWeizhen LiDepartment of Biomedical Engineering, The George Washington University, Washington D.C., USAEmilia EntchevaDepartment of Biomedical Engineering, The George Washington University, Washington D.C., USAJan Christophjan.christoph@ucsf.eduhttp://cardiacvision.ucsf.eduCardiovascular Research Institute, University of California, San Francisco, San Francisco, USADivision of Cardiology, University of California, San Francisco, San Francisco, USADepartment of Biomedical Engineering & Therapeutic Sciences, University of California, San Francisco, USA

## Abstract

The heart’s contractions are triggered by action potential waves,
which propagate rapidly through the cardiac muscle and exhibit diverse spatio-temporal dynamics during different heart rhythms.
The dynamics are governed by biophysical laws arising in reaction-diffusion systems and modeled with partial differential equations (PDEs) in cardiac electrophysiology simulations.
However, fitting such models to measurement data to develop digital twins or patient-specific computer models is challenging.
Here, we introduce differentiable cardiac electrophysiology simulations that can be fitted automatically to spatio-temporal measurement data of action potential waves in cardiac tissue.
By comparing the simulated dynamics with the observation data, we define a loss function that is minimized via gradient-based optimization.
Backpropagating the loss gradient through the differentiable PDE solver with respect to the model parameters and initial condition enables us to learn the parameters and recover the full dynamics, even with sparse, noisy, or partial observations.
Implemented using both the finite-difference and smoothed particle hydrodynamics (SPH) methods, our simulation framework can be applied to pixel-, voxel-, or point-based data, such as 2D or 3D slabs, or arbitrary anatomical shapes, such as the heart’s ventricles.
For instance, we recover spiral wave dynamics from observations across a 2D grid, scroll waves from observations across a 3D bulk’s surface, or early activation sites inside a 3D bi-ventricular geometry from epicardial observations.
We also fit one phenomenological model to another, and to imaging data of a voltage spiral wave in a cardiac monolayer cell culture.
With experimental data, we employed a perceptual loss based on the Video Joint-Embedding Predictive Architecture, which enables fitting to noisy imaging data, and a generative diffusion model to estimate initial conditions and constrain solutions.
Our results demonstrate that differentiable physics simulations are a powerful methodology for fitting cardiac electrophysiology models to data.
Utilizing such techniques could improve the diagnosis of rhythm abnormalities in patients and facilitate the development of personalized models or digital twins of the heart.Keywords

Digital Twin, Cardiac Electrophysiology, Differentiable Physics Simulations, Machine Learning††preprint:APS/123-QED

## IIntroduction

Computer simulations of the heart are increasingly used for disease modeling, arrhythmic risk stratification, drug or medical device evaluation, treatment planning, and procedural guidance.
These developments have fueled growing interest in the concept of a digital twin of the heart: a patient-specific computational model that integrates anatomy, physiology, and measurement data to reproduce and predict cardiac function.
However, personalizing such models remains a major challenge because the heart’s dynamical state and physiological parameters are difficult to obtain.
From a dynamical systems perspective, not only can some dynamical variables, such as the transmembrane voltage, only be observed indirectly or incompletely, but other hidden variables cannot be observed at all.
While it is possible to measure the heart’s anatomy using magnetic resonance imaging (MRI) or ultrasound, functional measurements of the heart’s electrophysiology rely on sparse, indirect, or incomplete data.
For instance, the 12-lead electrocardiogram (ECG) is a reflection of the heart’s electrical state on the body surface. It is an indirect, low-resolution measurement.
Direct approaches, such as catheter-based electrode mapping[25]or voltage-sensitive optical mapping[15], provide higher resolutions, however, only on the heart’s surface, not from within the heart muscle.
Further, only optical mapping provides measurement data of transmembrane voltage, and is a truly panoramic high-resolution measurement.
Catheter mapping is a sparse, point-by-point measurement that yields electrograms, rather than a physiological variable.
Accordingly, the complete set of variables of a biophysical model describing the heart’s dynamics must be inferred using state and parameter estimation techniques.
Together, this challenge is particularly pronounced in cardiac electrophysiology simulations, where nonlinear reaction-diffusion dynamics govern the propagation of action potential waves through a complex tissue anatomy and produce highly intricate spatio-temporal dynamics during arrhythmias[17,54,2,58,16], yet, the full dynamics must be inferred from limited observation data.

A wide range of techniques has been developed to address state and parameter estimation in cardiac systems and related nonlinear dynamical models,
ranging from data assimilation[5,28,37,29,45,44,47], Kalman filters[37,44], particle swarm optimization[61,13,41,59,10], gradient-based optimization[41], least squares[19], stochastic optimization approaches such as simulated annealing[42]or genetic algorithms[63,7,11], physics-informed neural networks[46], and Bayesian approaches[55], among others.
As much as the techniques vary in their mathematical foundations, from an application perspective, their respective strengths and limitations make them better suited for certain applications than others.
Particle swarm optimization and genetic algorithms were primarily used to fit action potentials in single cells, while data assimilation was primarily used to reproduce wave dynamics in tissues.
Bayesian and iterative approaches with reaction-Eikonal models[52]were used with 12-lead ECG and 3D MRI data for personalizing bi-ventricular electrophysiology[56,26,12]and electromechanics[20]simulations of sinus rhythm.
Together, these techniques have enabled parameter inference and dynamical state reconstructions, including reconstructions of activation sequences, repolarization times, or wave patterns at the tissue level.
However, many existing techniques struggle to fully exploit spatio-temporal data, particularly when fitting models to irregular, arrhythmic wave dynamics.

Recent advances in automatic differentiation, differentiable programming, and machine learning have given rise to the emerging field of differentiable physics, which offers a unifying framework for integrating physical models with gradient-based optimization[30,65].
By constructing simulation pipelines that are fully differentiable, it becomes possible to propagate gradients through numerical solvers and directly optimize simulation parameters using backpropagation, see Fig.1.
This paradigm has been enabled by modern automatic differentiation tools such as JAX[8]and PyTorch[53], and has already shown promise in various areas, such as fluid and molecular dynamics[67,60].
Differentiable physics solvers were introduced for simulating cardiac mechanics[64], parameter estimation of spiral wave dynamics in excitable media[39], and, in conjunction with neural networks, for fitting cardiac action potentials[32].
In cardiac electrophysiology, differentiable simulations offer a powerful alternative to traditional fitting procedures, enabling integration of biophysical models, irregular geometries, and diverse data modalities.

In this work, we build on these developments and introduce differentiable cardiac electrophysiology reaction-diffusion simulations that enable efficient, automated fitting to spatio-temporal data, including, for instance, simulated data in slab- and heart-shaped tissue models and action potential spiral waves in a petri dish.
We used several complementary techniques in conjunction with the gradient-based optimization that facilitate learning, such as iterative multi-horizon fitting.
In particular, with experimental data, we employed a perceptual loss based on the Video Joint-Embedding Predictive Architecture (V-JEPA) that overcomes limitations associated with a pixel-based loss and enables fitting to noisy, artifact-afflicted data, and a denoising diffusion probabilistic model (DDPM) to estimate initial conditions and further constrain the solution space towards a particular biophysical model.
We assess the efficacy of our approach under various conditions with partial, sparse, or noisy observations.
For instance, we fit a 3D model to epicardial observations of a simulated focal wave pattern originating in the septum of a bi-ventricular geometry, recover simulated spiral wave dynamics from sparse observations across a grid, scroll waves inside a bulk from surface observations, and fit a 2D model to noisy imaging data of an action potential spiral wave in a monolayer cell culture.Figure 1:Gradient-based fitting to spatio-temporal data using differentiable cardiac electrophysiology simulations.ACoupled partial differential equations (PDEs) as a biophysical model for excitable wave dynamics in a reaction-diffusion system.
Gradient descent finds the optimal simulation (initial state and matching parameters) that minimizes the lossℒ\mathcal{L}between data and model (illustration).BInitial state(v0,r0)(v_{0},r_{0})and trajectory(v​(t),r​(t))(v(t),r(t))solved with differentiable solver. Loss gradient backpropagated through solver to update the model’s state and parameters.CIterative refinement of simulation and minimization of loss over optimization steps (epochs).Figure 2:Simulations of electrical action potential waves (red: depolarized tissue, white/gray: resting tissue) in 2D and 3D tissues.A2D focal wave originating from a point source (voltage variablevvonly, timesteps 0-50).B2D spiral wave (red: voltage variablevv, blue: refractory variablerr, 1 rotation occurs within approx. 20-50 timesteps).C3D scroll wave dynamics inside slab/bulk.D3D scroll wave in idealized bi-ventricular geometry (LV: left ventricle, RV: right ventricle).
Simulations were performed using the finite differences (A-C) and smoothed particle hydrodynamics (SPH) methods (D) with several different models (Aliev-Panfilov, Mitchell-Schaeffer, and others).
All dynamics were subsequently learned using differentiable simulations.

## IIMethods

We employed the finite differences and smoothed particle hydrodynamics (SPH) methods to simulate nonlinear waves of electrical excitation in two-dimensional (2D) sheets, three-dimensional (3D) slab/bulk tissues, and 3D idealized bi-ventricular-shaped heart models, see Fig.2.
Further, we imaged voltage spiral waves in cardiac monolayer cell cultures, see Fig.17.
We then fitted differentiable electrophysiology simulations to the spatio-temporal data, starting with rough initial guesses of the model parameters and dynamical states.
In sectionsIII.1-III.5, we assumed that the model equations are known, in sectionIII.6, we learned the dynamics with different model equations than those used for data generation, and with the experimental data in sectionIII.7, we did not know and had to assume the model equations.

## II.1Biophysical Modeling of Action Potential Waves

We simulated electrical action potential waves in cardiac muscle tissue using two distinct two-variable phenomenological reaction-diffusion models[1,49].
We used the Aliev-Panfilov (AP) model[1]with 2 state variables and 6 parameters, and the Mitchell-Schaeffer (MS) model[49]with 2 state variables and 5 parameters,
to produce spatio-temporal action potential wave data.
Generally, the models comprise coupled partial differential equations (PDEs) describing the excitable and refractory kinetics, along with a diffusion term that supports the propagation of nonlinear waves of electrical excitation through the tissue.
While more detailed ionic models describe richer or finer features of action potential dynamics, with some of their variables and parameters relating to sodium, potassium, and calcium ion channels, simpler phenomenological models (AP, MS) capture the essence of the dynamics.
We primarily used the AP model[1]:∂v∂t\displaystyle\frac{\partial v}{\partial t}=\displaystyle=∇⋅(D​∇v)−k​v​(v−a)​(v−1)−v​r\displaystyle\nabla\cdot(D\nabla v)-kv(v-a)(v-1)-vr(1)∂r∂t\displaystyle\frac{\partial r}{\partial t}=\displaystyle=(ε0+μ1​ru+μ2)​(k​v​(a+1−v)−r)\displaystyle\left(\varepsilon_{0}+\frac{\mu_{1}r}{u+\mu_{2}}\right)(kv(a+1-v)-r)(2)

Here, the 6 parameters{D,a,k,ϵ0,μ1,μ2}\{D,a,k,\epsilon_{0},\mu_{1},\mu_{2}\}determine the properties of the waves (e.g. wave propagation speed, wavelength, excitation threshold, distance between waves, number of waves, etc.).
The AP parameter values used in the different parts of the study are shown in table1.
We performed simulations in 2D sheets, 3D bulks / slabs, and 3D heart-shaped geometries.
The simulations in the regular geometries, see Fig.2A-C), were integrated using the finite differences method.
The simulations in the heart-shaped, bi-ventricular geometries, see Fig.2D), were performed using the smoothed particle hydrodynamics (SPH) method using the SPHinXsys library[68,69].
The 2D simulations were performed in simulation domains with a size of128×128128\times 128pixels.
The 3D bulk / slab simulations were performed in a simulation domain with a size of64×64×1664\times 64\times 16voxels.

## II.2Differentiable Simulations of Cardiac Electrophysiology

We developed differentiable cardiac electrophysiology simulations using the JAX library[8]and related packages from the JAX ecosystem.
JAX is a Python library for accelerator-oriented array computation and program transformation, designed for high-performance numerical computing and large-scale machine learning.
In particular, JAX provides the environment for gradient-descent-based optimization and differentiable physics simulations as it can automatically differentiate native Python and Numerical Python (NumPy) functions.
We developed two versions of differentiable cardiac electrophysiology simulations: one based on the finite differences method and the other on the smoothed particle hydrodynamics (SPH) method, see sectionsII.2.1andII.2.2, which allows us to perform simulations on regular and irregular geometries.

## II.2.1Finite Differences Method

The finite differences simulations were implemented as a fully differentiable pipeline utilizing the JAX ecosystem.
The spatial domain was discretized using finite difference stencils (e.g., a 9-point Laplacian) implemented natively in JAX.
This allowed the operations to be Just-In-Time (JIT) compiled via the Accelerated Linear Algebra (XLA) compiler, allowing highly efficient, parallelized execution on graphics processing units (GPUs).
For temporal integration, we utilized Diffrax[34], a JAX-based library for differentiable differential equation solvers.
The coupled system of partial differential equations (PDEs) was integrated using theTsit5solver, an explicit Runge-Kutta method of order 5(4).
To maintain numerical stability, we employed a Proportional-Integral-Derivative (PID) controller for adaptive step sizing with both relative and absolute tolerances set to10−410^{-4}.
Crucially, exact gradients of the observation loss with respect to the biophysical parameters and initial dynamical state were computed using reverse-mode automatic differentiation.
To mitigate the massive memory overhead typical of computing gradients via the adjoint method in long spatio-temporal sequences[39], we applied theRecursiveCheckpointAdjoint()method.
Doing so keeps the gradient computation exact while maintaining a computationally feasible memory footprint that scales as𝒪​(N​log⁡N)\mathcal{O}(N\log N)in the number of solver stepsNN.
Finally, the reaction-diffusion parameters and spatial fields were parameterized using the JAX-based Equinox library[33].
By encapsulating the model parameters and spatial discretizations as PyTrees (eqx.Module), Equinox provides an object-oriented architecture that integrates with JAX’s functional programming constraints.
The parameter recovery and state estimation were subsequently driven by the Optax library.
We utilized the Adam optimizer[35]coupled with either a constant learning rate or an exponential decay learning rate schedule across our multi-horizon training blocks described in sectionII.3.3.

## II.2.2Smoothed Particle Hydrodynamics (SPH) Method

The SPH simulations were implemented using JAX-MD[60], a differentiable molecular dynamics framework, reimplementing the cardiac electrophysiology simulation part of the open-source SPHinXsys library[68,69]as a fully differentiable pipeline.
The simulations were initialized using a bi-ventricular template geometry loaded from a surface mesh, see Fig.3.
Particles were placed on a regular grid inside the mesh, and a 50-step iterative relaxation procedure was applied to achieve a near-uniform particle distribution, in which particles repel one another via a pressure-like force derived from the SPH kernel gradient.
Spatial interpolation was performed with the Wendland C2 kernel (5th-order, compact support radius2​h2h,h=1.2​Δ​xh=1.2\,\Delta x), and neighbor lists were managed using JAX-MD’s sparse neighbor list with a cutoff of2​h2h.
A kernel correction (renormalization) matrix𝐁\mathbf{B}was computed per particle to enforce first-order consistency of the SPH gradient operator.
A transmural scalar fieldψ∈[0,1]\psi\in[0,1]was computed by solving a diffusion equation on the particle set, with Dirichlet boundary conditions ofψ=1\psi=1on the epicardium andψ=0\psi=0on the endocardium.
Fromψ\psi, a fiber direction𝐟0\mathbf{f}_{0}was assigned to each particle by rotating a circumferential base direction about the local sheet normal, with the helix angle varying linearly from−70∘-70^{\circ}at the endocardium to+80∘+80^{\circ}at the epicardium, following standard rule-based fiber assignment methods[21].
Action potential propagation was modeled using the AP model, see sectionII.1, augmented with an anisotropic diffusion tensor𝐃=Diso​𝐈+Dani​𝐟0​𝐟0⊤\mathbf{D}=D_{\mathrm{iso}}\mathbf{I}+D_{\mathrm{ani}}\mathbf{f}_{0}\mathbf{f}_{0}^{\top}aligned with the local fiber direction.
The reaction-diffusion system was integrated using a Strang splitting scheme: a half-step of AP reaction, a full diffusion step, and a second half-step of AP reaction, which yields second-order accuracy in time.
The reaction terms for the voltagevvand refractory variablerrwere integrated using a quasi-steady-state (QSS) exponential integrator, which is analytically exact for linear-coefficient ODEs and improves stability at larger time steps.
Diffusion was advanced using a second-order Runge-Kutta scheme with the SPH Laplacian corrected by the anisotropy tensor and the per-particle correction matrix𝐁\mathbf{B}.
As with the finite differences method, the entire simulation pipeline was implemented in JAX and is end-to-end differentiable.
Gradients of the observation loss with respect to the initial dynamical state and model parameters were computed usingjax.value_and_gradwith gradient checkpointing applied to the diffusion integration steps to manage memory.
Parameter recovery was performed using the Adam optimizer[35]with a learning rate of10−410^{-4}via Optax.Figure 3:Bi-ventricular simulations of cardiac electrophysiology using the smoothed particle hydrodynamics (SPH) method.ASurface geometry and approximation of volume with particles. We simulated focal and reentrant rhythms, see Figs.2D),9-12.BInitialization used in sectionIII.3to begin the gradient descent-based learning. The initial learned voltage and refractory variablesv0′​(x→)v^{\prime}_{0}(\vec{x})andr0′​(x→)r^{\prime}_{0}(\vec{x})were set to a random Perlin noise field (here shown withv,r>0.1v,r>0.1thresholding), while observations of the voltage variablev¯\bar{v}were obtained only from the epicardium.

## II.3Gradient-based Learning of Spatio-Temporal Cardiac Action Potential Wave Dynamics

In this study, we aim to learn spatio-temporal action potential wave dynamics inside an excitable tissue.
We treat the excitable tissue as a dynamical system𝐒\mathbf{S}.
The system’s configuration is defined by a dynamical state𝐲\mathbf{y}, which is a vector of state variables{y1,y2,…}\{y_{1},y_{2},\dots\}(e.g. excitability, refractoriness, etc.), and the system’s dynamics correspond to the evolution of this state vector over time.
We assume a system of coupled partial differential equations (PDEs) that describe or approximate the dynamics, see eqs. (1) and (2) for an example.
Accordingly, the dynamics are described by:{aligned}​∂𝐲∂t=f​(𝐲,∇2𝐲,…,𝐱,t;𝜽),𝐱∈Ω,t∈(0,T]\aligned\frac{\partial\mathbf{y}}{\partial t}&=f\!\left(\mathbf{y},\nabla^{2}\mathbf{y},\ldots,\mathbf{x},t;\bm{\theta}\right),&&\mathbf{x}\in\Omega,\;t\in(0,T]

whereffare a specific set of equations of motion, see eqs. (1)-(2),𝜽\bm{\theta}is a set of model parameters, andΩ\Omegais the spatial domain of a spatially extended system.
The initial condition corresponds to the configuration of all state vectors throughout the spatial domain of the system at timet=0t=0:{aligned}​𝐲​(𝐱,t=0)=𝐲0​(𝐱),𝐱∈Ω\aligned\mathbf{y}(\mathbf{x},t=0)&=\mathbf{y}_{0}(\mathbf{x}),&&\mathbf{x}\in\Omega

where𝐲0=(v0,r0)\mathbf{y}_{0}=(v_{0},r_{0})for two-variable models.
Here, we aim to estimate the initial condition𝐲0​(𝐱)\mathbf{y}_{0}(\mathbf{x})and a set of parameters{θ1,…,θn}\{\theta_{1},\dots,\theta_{n}\}that minimize a loss function:{align}L(y_t_0, …,y_t_n )

evaluated over a series of subsequent observations of a subset of the dynamical state variables (the ones that can be observed) at observation time pointst0,…,tnt_{0},\dots,t_{n}, see sectionII.3.1.
In particular, we assume that the model parameters and the dynamical state𝐲\mathbf{y}are unknown at the beginning of the learning.
The problem corresponds to a state and parameter estimation task.

In this study, the learning was performed by observing the excitatory or voltage variablevv, see sectionII.3.1, and by subsequently continuously adjusting the initial condition and model parameters using gradient-based optimization until the loss is minimized.
In some tasks, we assumed that the voltage variable could only be observed in certain locations of the spatial domain, e.g. on parts of the surface or in sparse locations.
The dynamics were learned using the Adam[35]optimizer with either a constant learning rate of10−310^{-3}, or a linearly or exponentially decreasing learning rate, see also sectionII.3.3.
Learning was performed on NVIDIA RTX A5000 and A6000 graphics processing units (GPUs), and took between 4 and 24 hours depending on the task.

## II.3.1Loss Function

In all simulations, we computed at a minimum a total loss comprising an observation loss and a regularization loss :ℒ=\displaystyle\mathcal{L}=ℒo​b​s+ℒr​e​g\displaystyle\mathcal{L}_{obs}+\mathcal{L}_{reg}(3)

The observation lossℒo​b​s\mathcal{L}_{obs}measures the discrepancy or mean squared error between the observed excitatory or voltage variablev¯\bar{v}and the learned variablev′v^{\prime}:ℒo​b​s=\displaystyle\mathcal{L}_{obs}=1N​∑(v¯​(𝐱,t)−v′​(𝐱,t))2\displaystyle\frac{1}{N}\sum(\bar{v}(\mathbf{x},t)-v^{\prime}(\mathbf{x},t))^{2}(4)

over all observed data (pixels, points) within a specified time frame (e.g. horizon, see sectionII.3.3).
The regularization lossℒr​e​g\mathcal{L}_{reg}is a penalty term that activates when the learned dynamic variablesv′v^{\prime}andr′r^{\prime}leave their typical range, and enforces them to be0≤v′≤10\leq v^{\prime}\leq 1andr′≥0r^{\prime}\geq 0:ℒr​e​g=\displaystyle\mathcal{L}_{reg}=∑max⁡(−u,0)+∑max⁡(−r,0)+∑max⁡(v−1,0)\displaystyle\sum\max(-u,0)+\sum\max(-r,0)+\sum\max(v-1,0)(5)

For example, ifv′<0,r=1→ℒ=−v′v^{\prime}<0,r=1\rightarrow\mathcal{L}=-v^{\prime}with the AP model.
In addition toℒo​b​s\mathcal{L}_{obs}andℒr​e​g\mathcal{L}_{reg}, we introduced other losses whenever necessary.
With sparse data, see sectionIII.5, we introduced a smoothness lossℒs\mathcal{L}_{s}, which corresponds to the mean squared gradient magnitude of the learned refractory variable:ℒs=α⋅‖∇r′‖22\displaystyle\mathcal{L}_{s}=\alpha\cdot\|\nabla r^{\prime}\|_{2}^{2}(6)

where∇\nabladenotes the discrete spatial gradient computed using forward differences, andα\alphais a weighting factor controlling the strength of the contribution of this loss to the overall loss.
The smoothness loss penalizes large spatial gradients in the field of the learned refractory variabler′r^{\prime}, which arise, for instance, with sparse observations, see sectionIII.5.
We only used the smoothness loss with sparse data in addition to the total lossℒ\mathcal{L}and setα=0\alpha=0otherwise.

With experimental data, see sectionIII.7, we augmented the total lossℒ\mathcal{L}with a perceptual loss:ℒ=\displaystyle\mathcal{L}=ℒo​b​s+ℒr​e​g+ℒp\displaystyle\mathcal{L}_{obs}+\mathcal{L}_{reg}+\mathcal{L}_{p}(7)

the perceptual loss being:ℒp=1T​∑t‖fθ​(vt′)‖fθ​(vt′)‖−fθ​(v¯t)‖fθ​(v¯t)‖‖2\displaystyle\mathcal{L}_{p}=\frac{1}{T}\sum_{t}\left\|\frac{f_{\theta}(v^{\prime}_{t})}{\|f_{\theta}(v^{\prime}_{t})\|}-\frac{f_{\theta}(\bar{v}_{t})}{\|f_{\theta}(\bar{v}_{t})\|}\right\|^{2}(8)

wherevt′v^{\prime}_{t}andv¯t\bar{v}_{t}denote the simulated and observed frames at timett, respectively.
The perceptual lossℒp\mathcal{L}_{p}is computed in the feature space of a frozen vision transformer encoderfθf_{\theta}pre-trained via a Video Joint-Embedding Predictive Architecture (V-JEPA)[23].
We pre-trained the encoder on simulated single- and multi-spiral AP dynamics, and held the encoder weights fixed throughout optimization.
Both the simulated and observed frames were z-score normalized using the global mean and standard deviation of the synthetic training dataset, and the perceptual loss was computed as the mean squared error (MSE) betweenℓ2\ell_{2}-normalized per-frame feature vectors.
We also introduced a phase lossℒϕ\mathcal{L}_{\phi}defined as:ℒϕ=αϕ⋅‖ϕ−ϕ′‖\displaystyle\mathcal{L}_{\phi}=\alpha_{\phi}\cdot\|\phi-\phi^{\prime}\|(9)

whereϕ\phiandϕ′\phi^{\prime}are the ground-truth and learned phase angles andαϕ\alpha_{\phi}is a weighting factor.
However, we abandoned the phase loss because we obtained better performance with the perceptual loss.

## II.3.2Initial Parameter Guesses

Initial guesses for the learned parametersθi′={θ1′,θ2′,…​θi′}\theta^{\prime}_{i}=\{\theta_{1}^{\prime},\theta_{2}^{\prime},...\theta_{i}^{\prime}\}were set to random values within certain reasonable parameter-specific bounds, often resulting in substantial mismatches between the initial guessesθi′\theta^{\prime}_{i}and the ground-truth valuesθi\theta_{i}of at least 20% and in some cases more than 50-100% per parameter.
Fig.S4shows true parameters (black bar, left), initial parameter guesses (center, gray), and learned parameters for 3 different cases (2D focus, 2D spiral, sparse observations).
In the lower panel in Fig.S4A), the initial value for the diffusion coefficient wasD=0.01D=0.01, while the true value wasD=0.0011D=0.0011.
Fig.7shows that the parameters can fluctuate wildly across a wide range of values throughout learning, possibly diverging further from the initial guess before converging back to the ground-truth.
With cross-model learning, see sectionIII.6, we first learned approximations of the parameters in a single cell (0D), then continued with the learned parameters in a 1D ring, and finally used those approximations to initialize the 2D learning.

## II.3.3Multi-Horizon Learning Schedule

Learning was performed sequentially across multiple segments of the observed dynamics.
For example, if the entire observation data shows 3 rotations of a spiral wave, we divided the 3 rotations into segments corresponding to the first, second, and third rotations, or into finer divisions, such as quarter rotations.
We refer to each segment as a ’horizon’ and the learning over multiple segments as multi-horizon learning.
Importantly, horizons can overlap.
We empirically found that multi-horizon learning outperforms learning the dynamics all at once in a single horizon, even when learning it over many epochs, see Fig.S3B,C).
Further, we found that dividing the dynamics into many horizons dramatically outperforms selecting fewer horizons.
If the horizon is too long, then the loss quickly saturates, because small changes in the parameters and initial condition lead to large deviations in the dynamical trajectories, whereas short horizons yield much smaller deviations and non-saturating losses.
As a result, we abandoned using long single or few horizons and instead used rolling multi-horizon learning schedules with many (e.g.30−6030-60) overlapping subsequent horizons for learning a brief period of the spatio-temporal dynamics (e.g. a focal wave or a few spiral wave rotations).
In the above example with 3 spiral rotations, a simple multi-horizon schedule with few horizons could consist of 6 non-overlapping horizons, each covering half a rotation, and a rolling multi-horizon schedule with many horizons could consist of 60 overlapping horizons, each covering half a rotation as well, but with 95% overlap between subsequent horizons.

Generally, the multi-horizon learning scheduleSScompriseskkhorizons, starts with the first horizon, and continues with subsequent horizons:S={ℋ1,ℋ2,ℋ3,…,ℋk}S=\{\mathcal{H}^{1},\mathcal{H}^{2},\mathcal{H}^{3},...,\mathcal{H}^{k}\}

Each horizon comprisesnntime steps{t1,t2,…,tn}\{t_{1},t_{2},...,t_{n}\}at which we obtain observation data:ℋi={v¯​(t1),v¯​(t2),…,v¯​(tn)}\mathcal{H}^{i}=\{\bar{v}(t_{1}),\bar{v}(t_{2}),...,\bar{v}(t_{n})\}

of the voltage variablevv.
Each subsequent horizon is shifted by one time step or strides=1s=1.
The number of time steps or observations together with the stridessequals the horizon durationhh.
Throughout this study, we used equidistant temporal samplingΔ​t=ti+1−ti=ti+2−ti+1\Delta t=t_{i+1}-t_{i}=t_{i+2}-t_{i+1}etc. for the observations.
Accordingly, with a rolling multi-horizon learning schedule composed of horizons with durationh=10h=10, we learned over the following sequence of horizons and observations:ℋ1=\displaystyle\mathcal{H}^{1}={v¯​(t1),v¯​(t2),…,v¯​(t10)}\displaystyle\{\bar{v}(t_{1}),\bar{v}(t_{2}),...,\bar{v}(t_{10})\}ℋ2=\displaystyle\mathcal{H}^{2}={v¯​(t2),v¯​(t3),…,v¯​(t11)}\displaystyle\{\bar{v}(t_{2}),\bar{v}(t_{3}),...,\bar{v}(t_{11})\}ℋ3=\displaystyle\mathcal{H}^{3}={v¯​(t3),v¯​(t4),…,v¯​(t12)}\displaystyle\{\bar{v}(t_{3}),\bar{v}(t_{4}),...,\bar{v}(t_{12})\}ℋ4=\displaystyle\mathcal{H}^{4}=…\displaystyle...(10)

The horizon duration can vary across the sequence of horizons, see tables2and3and Fig.S2.
In each horizon, we continue to estimate the parameters and the dynamical state using the estimates from the previous horizon.
With rolling overlapping horizons ands=1s=1, we used the second estimated state of the previous horizon to construct the initial state of the next horizon:(v′,r′)2i−1→(v¯,r′)1i(v^{\prime},r^{\prime})^{i-1}_{2}\rightarrow(\bar{v},r^{\prime})^{i}_{1}

wherer′r^{\prime}is the estimated refractory variable andv¯\bar{v}is the current observation of the voltage variable (their respective spatial fields).
In the case of non-overlapping horizons, we used the last state to initiate the first state of the next horizon.
The lossℒ\mathcal{L}is calculated per horizon, and learning is performed over a number of epochsnen_{e}specified for each horizon.
We varied the number of epochsnen_{e}over the course of the learning, see tables2and3.
A simple rolling multi-horizon schedule would be to learn 3 spiral wave rotations, observed across 80 time steps, usingk=60k=60horizons, each with a duration ofn=20n=20time steps, and a strides=1s=1, for example.
However, we used learning schedules that increased the horizon duration in stages, see table2, as this promoted parameter convergence, see Fig.7, and improved long-term predictions.

## II.3.4Initialization

We found that choosing the right initial condition or initial dynamical state(v0′,r0′)(v_{0}^{\prime},r_{0}^{\prime})before learning can strongly affect the learning, and developed initialization schemes based on empirical testing.
Throughout this study, we assumed that only the voltage variablevvcould be observed, and that it could be only partially observed in some situations.
For instance, in sectionIII.3, it could only be observed across the epicardium, in sectionIII.4on two opposing surfaces of a bulk, and in sectionIII.5in sparse locations.
Accordingly, the initial state(v0′,r0′)(v_{0}^{\prime},r_{0}^{\prime})used in the first epoch had to be constructed from the observationv¯0\bar{v}_{0}at timet=0t=0and guesses for the remaining missing data: the refractory field had to be guessed entirely, and the voltage variable had to be guessed in locations without observations.
At the same time, we aimed to initialize the learning without making too many assumptions about the dynamics.Figure 4:Learning the initial condition of a focal wave during the early phase of the rolling multi-horizon learning schedule shown in Fig.S2D).
The maps show the learned voltage fieldv′​(x,y)v^{\prime}(x,y)(red) and the learned refractory fieldr′​(x,y)r^{\prime}(x,y)(blue) of the AP model.
Initially, the true refractory fieldr​(x,y,0)r(x,y,0)is unknown and must be guessed.
We setr0′=v0¯⋅(1+σ)r_{0}^{\prime}=\bar{v_{0}}\cdot(1+\sigma)as an approximation of the observationv¯0\bar{v}_{0}, see eq. (11).
With this guess, the learned voltage wave propagates both forward and backward (top row).
Within the first 100 epochs, the refractory field is modified such that the voltage wave propagates only forward.
The initial state eventually saturates and can only be refined further towards ground-truth when moving on to the next horizon
(horizon 1: time steps 1-10, horizon 2: time steps 2-11, horizon 3: time steps 3-12, etc.).
In Fig.15B), the initial condition is learned within the first 3-4 horizons.

With the 2D simulations in sectionsIII.1andIII.2, we chose the following initial guess for the refractory variable:ro′=\displaystyle r^{\prime}_{o}=v¯0⋅(1+σ)\displaystyle\bar{v}_{0}\cdot(1+\sigma)(11)

wherev¯0\bar{v}_{0}is the observation of the voltage wave at timet=0t=0in horizon 1 andσ\sigmais Gaussian noise, see also Fig.S1A).
This initialization scheme effectively creates a noisy copy of the voltage wave as the refractory wave.
Other initializations, such asr0′=0r^{\prime}_{0}=0,r0′=1r^{\prime}_{0}=1, orr0′=σr^{\prime}_{0}=\sigmaled to less effective learning, see Figs.S1andS3A), or numerical instability.
In the sparse 2D simulations in sectionIII.5, we used the same initialization as in the continuous 2D case, but applied eq. (11) only in the electrode locations on the grid.
With the 3D bulk simulations, we used the observationsv¯​(z=0),v¯​(z=16)\bar{v}(z=0),\bar{v}(z=16)of the voltage variable across the two opposing observed top and bottom surfaces, see Fig.III.4, together with a weighted average of these two surface patterns as an initialization forvvin the depth of the bulk.
Accordingly, we used eq. (11) forr0′r^{\prime}_{0}across the two surfaces and their weighted average for the bulk.
In the bi-ventricular simulations in sectionIII.3, we chose random spatial patterns for the initialv0′v^{\prime}_{0}andr0′r^{\prime}_{0}fields throughout the ventricles, see Fig.3B), and the observationv¯0\bar{v}_{0}att=0t=0across the epicardium.
The random pattern was generated using Perlin noise and thresholding, see Fig.3B).
With the 2D cross-model learning, see sectionIII.6, we used a denoising diffusion probabilistic model (DDPM) trained on 2D simulation data, similarly as described in Baranwal et al.[3], simulated with the AP model to generate such data when conditioned with MS spiral wave data.
Subsequently, the DDPM could translate MS voltage patterns into AP spirals with both excitatory and refractory components, which then served as the initial conditions for the learning.
Moreover, the DDPM could translate any spiral-shaped pattern, e.g. those obtained in imaging experiments, and produce a corresponding AP initial condition.
The translation of an MS excitation variable to an AP excitation variable was done via an SDEdit[48]style approach, and the generation of the associated refractory variable was done via a RePaint[43]style approach.

## II.3.5Cardiac Monolayer Cell Culture

We fitted simulations to two different cell cultures, see sectionIII.7and Fig.17.
The data shown in Fig.17A) was obtained from Monteiro da Rocha et al.[51].
It shows a calcium spiral wave imaged with fura-2.
We used the calcium wave as a proxy for the voltage wave.
The data was cropped from the corresponding Supplementary Video (.mp4 fileformat) and converted into a numpy array with floating point precision values normalized between[0,1][0,1].
The data shown in Fig.17B) was generated specifically for this study.
Human iPSC-CM (iCell2 from CDI/Fujifilm) were grown in glass-bottom35​m​m35mmdishes (with14​m​m14mmcircular area) and treated as previously described[27,40].
Briefly, the glass bottom was coated with 50 µg/ml fibronectin, and cells were plated at high density (270,000270,000cells per dish). Cells were maintained in a humidified CO2 incubator at37∘​C37^{\circ}C, with regular exchange of culture medium.
Measurements were done on day 6 after plating, in OptiMem medium.
To promote spiral induction, samples were treated with 3nM dofetilide for 30min.
Spirals were induced through rapid pacing.
Fluorescent voltage recordings were obtained after labeling with 1 µm Berst1 voltage-sensitive dye[31,36].
The optical mapping system used to collect data was described previously[27,40].
Briefly, a Basler camera (Basler acA720-520um, Ahrensburg, Germany) was used to record videos at 100 Hz.
The field of view was1.86​c​m21.86cm^{2}.
A 660-nm LED (M660L4, Thorlabs, Newton, NJ, USA) provided oblique trans-illumination and light was collected after an emission filter (ET595/40m+700LP, Chroma, Bellows Falls, VT, USA).
Signals were acquired with an USB3.0-based Pylon Viewer software.

## IIIResults

We found that differentiable cardiac electrophysiology simulations can be used to estimate states and parameters of 2D and 3D action potential wave dynamics across various tissues and configurations.
The dynamics and parameters can be learned from sparse, partial, and noisy observations of the voltage variable, yielding full numerical reconstructions of the reaction-diffusion dynamics.
For instance, we were able to locate focal waves originating in the septum from epicardial observations, see Fig.9, scroll waves inside a bulk from observing two opposing surfaces of the bulk, see Fig.13, recover full-resolution 2D reentrant spiral waves measured with a sparse grid of electrodes, see Fig.15, and fit a model to an action potential spiral wave imaged in a cardiac monolayer cell culture, see Fig.17.
In particular, we found that the method is best suited for learning chaotic spiral or scroll wave dynamics.

## III.12D Focal Waves

Fig.4shows the learning process of a simple focal wave propagating through a simulated 2D tissue with isotropic conduction.
The action potential wave was simulated using the AP model, see sectionII.1, and propagates from the lower right to the upper left.
We employed a rolling multi-horizon learning schedule, as shown in Fig.S2D and table2, and observed the voltage variablevvat full resolution and without noise across all snapshots within each horizon.
We assumed that the model equations are known.
Overall, the wave is observed within 70 time steps, and, at the beginning of the learning, it has already traveled away from its origin.
The first observation is the snapshot on the left in the top row in Fig.4.
As only the voltage variablevvcan be observed, the true initial dynamical state(v0,r0)(v_{0},r_{0})is unknown, and an initial state(v0′,r0′)(v^{\prime}_{0},r^{\prime}_{0})must be guessed to initiate the learning, see sectionII.3.4.
The first row (Horizon 1, Epoch 1) shows the first epoch, which starts with the guessed initial state(v¯0,r0′)(\bar{v}_{0},r^{\prime}_{0})composed of the observationv¯0\bar{v}_{0}(first row) and the guess forr0′r^{\prime}_{0}(second row).
We usedr0′∼v¯r^{\prime}_{0}\sim\bar{v}, see eq. (11) for details.
With this initialization, the action potential lacks a refractory tail and propagates both forward and backward during the first epochs.
Within the first 100 epochs, the initial refractory fieldr′r^{\prime}is varied via gradient-based optimization,
such that the learned voltage wave eventually sheds the backward-propagating part and subsequently propagates only forward, as it should.
By the end of Horizon 1, comprising 600 epochs, the learned dynamics exhibit an action potential wave that propagates roughly as expected, from the lower right to the upper left.
At the same time, the parameters are continuously varied during learning to further reduce the loss, see also Fig.7.Figure 5:Reconstruction of spiral wave dynamics using multi-horizon learning schedule with a differentiable simulation.
Effect of observation and learning duration on state and parameter reconstruction accuracy,
The accuracy is measured as the agreement between original and learned spiral wave dynamics when the two dynamics are evolved into the future and compared to each other, see also Fig.6.
Learning ends at 0. Afterwards, the fully learned dynamics co-evolve precisely with the original dynamics for over 20 rotations.ALoss curve showing multi-horizon learning schedule (10 horizons with 10 time steps each, 10 horizons with 20 time steps each, 10 horizons with 40 time steps each). At the beginning of each new horizon, the loss peaks.BMean absolute pixel-wise error between original and learned dynamics over time with different learning schedules: 3, 10, 15, 20, and 27 horizons as shown in
Time units normalized and specified in number of spiral rotations.
Learning ends att=0t=0and the learned state and parameters are used to simulate the dynamics over 30 rotations into the future.
Our multi-horizon gradient-descent-based learning scheme recovers model parameters and the dynamical state so well that, if the learned dynamical state is evolved into the future, it matches the original dynamics precisely over many rotations (green line).
With 27 horizons, the dynamics are identical over 20 rotations.
or 67 time steps or 20,000 epochs, the dynamics is learned overCTop row: Original spiral wave dynamics with alternans, meandering and wave break.
With 27 horizons learning over 60 time steps or about 4 rotations, we achieve very high reconstruction accuracies. The learned dynamics co-evolve for over 20 rotations, despite alternans, breathing, and spiral wave break-up.Figure 6:Agreement between learned and original ground-truth (GT) spiral wave dynamics after gradient-descent-based learning with different observation and learning durations using the rolling multi-horizon learning schedule shown in Fig.S2D).
After learning with sufficiently many observations and epochs (∼\sim4 rotations), the two dynamics co-evolve congruently over long periods of time (>20 rotations), while with fewer epochs and observations, the learned dynamics diverge quickly, see also Fig.5.
Snapshots show dynamics after 2, 4, 6, 8, etc. rotations (1 rotation≈\approx15 time steps).
Learning stopped at 0 and the two dynamics are evolved independently afterwards.
The time-series were measured at the center of the simulation domain (blue: original dynamics, red: learned).ALearning stopped prematurely after 6,000 epochs (10 horizons, 600 epochs each horizon).
The learned dynamics diverge quickly from the ground-truth and coincidentally self-terminate.BLearning stopped prematurely after 14,000 epochs (20 horizons). While there is still strong initial agreement, the dynamics diverge after 6-7 action potentials.CFully learned dynamics after 21,000 epochs (27 horizons). Due to the increasing horizon duration, all model parameters and the initial dynamical state att=0t=0are recovered so well that the dynamics co-evolve congruently over many rotations, see also Fig.5.
Observation durations range between 1-4 rotations, see also Fig.5B).

We found that the rolling multi-horizon scheme shown in Fig.S2D) is critical for achieving better dynamical state reconstructions than the state shown in the third panel toward the end of the first horizon (Horizon 1, Epoch 500), see also Fig.S3C).
The learned initial voltage and refractory fields(v0′,r0′)1(v^{\prime}_{0},r^{\prime}_{0})^{1}at the end of horizon 1 are just coarse approximations and not as continuous as their original counterparts.
The parameter guesses are poor at the end of horizon 1.
Moreover, without the multi-horizon scheme, the learning saturates: the state and parameters do not improve further with longer horizons and more epochs, but only improve with additional horizons, see also Fig.S3B,C).
The details of the rolling multi-horizon learning schedule are provided in table2.
Each horizon in Fig.4contains 10 observations{v¯1,v¯2,…,v¯10}\{\bar{v}_{1},\bar{v}_{2},...,\bar{v}_{10}\}(spatial patterns).
The observation loss is computed over the 10 observations, and the dynamics are learned over 600 epochs per horizon.
At the end of the first 10 horizons, the dynamics were learned over 6,000 epochs total.
In total, the wave is learned over 30 horizons or 70 time steps.
As each horizon starts with the next time step, the diffusion of the voltage wave provides a smoother, slightly better initial guess for the next horizon, enabling the learning to achieve better and better approximations over the sequence of horizons.
Employing the rolling multi-horizon learning scheme, it is possible to identify the full dynamical state and all 6 model parameters of the Aliev-Panfilov (AP) model, see table4and Fig.S4B).
The initial condition is approximated sufficiently well in the first 2-3 horizons, while the parameters need longer to be recovered in subsequent horizons.
The parameters{D,a,k}\{D,a,k\}converge relatively quickly and can be recovered within margins of less than1%1\%, while{ϵ0,μ1,μ2}\{\epsilon_{0},\mu_{1},\mu_{2}\}require longer and can be recovered only within margins of5%5\%, see table4.
Importantly, the initial parameter guesses can be substantially off from the ground-truth values, yet can still be recovered within a few percent, see Fig.S4B).
Because the focal wave eventually dies out at the boundaries, the observation time is limited, and it is difficult to evaluate learning accuracy on data other than the data used for learning.
Nevertheless, by the end of the learning schedule, the learned and original waves are congruent and visually indistinguishable, and we obtain satisfactory parameter estimations.
Yet, the parameter estimations are not as good as with spiral wave dynamics, see next section.

## III.22D Spiral Waves

Figs.5and6show reconstructions of spiral wave dynamics, which we observed for up to 4-5 rotations.
As in sectionIII.1, the wave dynamics were simulated using the AP model and then also learned using a differentiable version of the AP model.
The learning started with rough guesses of the initial state, as described in eq. (11), and the parametersθi={D,a,ϵ0,k,μ1,μ2}\theta_{i}=\{D,a,\epsilon_{0},k,\mu_{1},\mu_{2}\}.
Importantly, the initial parameter guesses were off substantially from the actual ground-truth values, see blue, gray, and black dots and traces in Fig.7.
The dynamics in Figs.5and6are composed of a meandering, drifting spiral wave exhibiting breathing phenomena, alternans, and occasional breakup.
Next to such dynamics, we also fitted dynamics composed of multiple drifting and interacting spiral waves, see Fig.15.
Continuously adapting both the initial state(v0′,r0′)(v^{\prime}_{0},r^{\prime}_{0})and all parametersθi\theta_{i}in each epoch yields new dynamical trajectories, as also shown in Figs.4,6, and15B).
Subsequently, computing the observation loss over all
time steps and backpropagating gradients through the solver enable finding better and better initial states and parameter values that further minimize the loss.
Fig.5A) shows that the loss is continuously decreasing in each horizon, spikes at the beginning of each next horizon, but then continues to decrease further and reaches lower values than in the previous horizon.
We found that this resetting helps achieve lower and lower loss values, see also Figs.S3C),5A),8A), and15.
The multi-horizon learning schedule used in Figs.4,5-8and15, comprises 3 stages: 10 horizons with 10 time steps each, which were learned over 600 epochs each, followed by 10 horizons with 20 time steps each, which were learned over 800 epochs each, and lastly 10 horizons with 40 time steps each, which were learned over 1,000 epochs each, see also table2.
We found that increasing the horizon duration is critical for obtaining better parameter estimates.
The parameter history curves in Fig.7show the learned parameters over the course of the learning for three repeated runs (black, gray, blue), and how some of the parameters respond to increasing the horizon duration at 6,000 and 14,000 epochs.
While the parameters{D,a,k}\{D,a,k\}generally converge quickly, the parameters{ϵ0,μ1,μ2}\{\epsilon_{0},\mu_{1},\mu_{2}\}take much longer to converge, and their convergence is promoted by increasing the horizon duration.
While initially the learning benefits from shorter horizons, later it is beneficial when the learned and ground-truth dynamics need to match over longer periods.
At first, increasing the horizon duration yields a higher loss.
However, with continued learning, the loss decreases to lower values than if the learning had continued with shorter horizon durations.Figure 7:Convergence of learned Aliev Panfilov model parameters{D,a,k,ϵ0,μ1,μ2}\{D,a,k,\epsilon_{0},\mu_{1},\mu_{2}\}towards ground-truth values (dashed line) starting with 3 different initial parameter guesses (black, gray, blue) with the dynamics shown in Figs.5and6.
The behavior is the same for all parameter combinations we tested.
Vertical lines same as in Fig.5A).
Increasing horizon durations (at 6,000 and 14,000 epochs) induces pivoting and leads to faster convergence.

The spiral wave dynamics can be learned so well within about 4-5 rotations that it becomes possible to forecast their evolution precisely over 20-30 rotations into the future, see Figs.5,6, and8.
Figs.5C) and6show the learned and ground-truth spiral wave dynamics after learning, and how they co-evolve and diverge when the final learned state(v′,r′)∗(v^{\prime},r^{\prime})^{*}and parameters{D,ϵ0,a,k,μ1,μ2}∗\{D,\epsilon_{0},a,k,\mu_{1},\mu_{2}\}^{*}are used to initiate a new simulation, and this simulation is compared to the corresponding ground-truth simulation over the same period.
The eventual divergence is expected as spiral wave dynamics are chaotic, and small differences in the initial conditions or model parameters generally lead to large accumulated errors over time.
Correspondingly, low divergence indicates very small mismatches between the ground-truth and learned configurations.
The first rows in Fig.5C) and panels A,B) in Fig.6show the divergence (pixel-wise error) when the learning was stopped prematurely after 1-3 rotations (or less than approximately 20 horizons, or 40 time steps, or 14,000 epochs).
The last row in Fig.5C) and Fig.6C) show essentially perfect congruence of the learned and ground-truth spiral wave dynamics with negligible pixel-wise error for the next 10-20 rotations (when learning is performed over 27 horizons, or 21,000 epochs, or 67 time steps, or about 4.5 rotations).
Correspondingly, Fig.5B) shows the mean absolute error over time for the different learning durations (green: very low error for 20 rotations), as well as the learning duration depicted as horizontal bars for comparison (learning stops at 0).
The vertical bars in the loss curve in Fig.5A) and the parameter histories in Fig.7indicate the epochs associated with the learning durations.
With spiral wave dynamics, all parameters can be recovered within a margin of less than0.05%0.05\%, see table4.
The barplots in Fig.S4A) show the ground-truth and learned parameters along with two different sets of initial parameter guesses.
In total, three very different initial parameter guesses all converge to the ground-truth parameter values, see Fig.7, with some initial guesses being substantially off (e.g.DDbeing about 10x larger than ground-truth value).
Lastly, Fig.8shows that it is possible to obtain precise predictions of the spiral wave core’s trajectory over more than 10 rotations. Here, the learning was performed over 23 horizons on a different example of spiral wave dynamics (with different parameters).
Based on the examples we studied, it appears that parameters converge faster with richer spiral wave dynamics.
In other words, learning is more effective with, for instance, meandering than with stationary spiral waves.
This finding aligns with the higher parameter-estimate margins observed with focal waves.
In summary, spiral wave dynamics can be learned so well that they can be predicted far into the future, even with substantial initial parameter mismatch, and even though they are chaotic and their evolution is generally hard to predict.Figure 8:Learning and predicting meandering spiral wave dynamics.ALoss curve during learning with rolling multi-horizon schedule (vertical bars correspond to panels in C). Total of 24 horizons with 10 (horizons 1-10), 20 (horizons 11-20), and 40 time steps (horizons 21-24) each.BSpiral wave pattern (red: voltage) and difference between ground-truth and learned dynamics (right, learning stopped prematurely) together with phase singularities (PS) marking rotational core (at time step 80).CSpiral wave core trajectories predicted into the future after learning the dynamics (black: ground-truth, red: 10,000 epochs / 15 horizons, orange: 14,000 epochs / 20 horizons, yellow: 15,000 epochs / 21 horizons, green: 17,000 epochs / 23 horizons) plotted over 150 time steps into the future (≈12\approx 12rotations).Figure 9:Learning of transmural bi-focal action potential wave pattern from epicardial observations using differentiable smoothed particle hydrodynamics (SPH) simulations.ABi-ventricular simulation geometry. LV: left ventricle, RV: right ventricle. The two foci (red dots marked by white arrows) originate on the endocardial surface of the septum and the LV free wall.BEpicardial breakthrough of focal waves (apical view). The LV and septal foci break through the surface at around 60 and 180 time steps, respectively (black arrows).CEarly activation sites / focal origins (red: ground-truth, blue: predicted) represented by electrically activated particles withv>0.5v>0.5att=40t=40simulation time steps.DGround-truth (GT) action potential wave pattern (red: depolarized tissue) on anterior wall.ELearned action potential wave dynamics after 1, 1,000, 3,000, 5,000, and 20,000 epochs in a single horizon. The observation loss is only computed across the epicardial surface (both RV and LV).
After 20,000 epochs, the ground-truth and learned wave dynamics are indistinguishable across the epicardium, see also Fig.10C).

## III.3Recovery of Transmural Action Potential Waves inside Bi-Ventricular Geometry from Epicardial Observations

Figs.9-12show the reconstruction of transmural action potential wave dynamics from epicardial observations using a single-horizon learning schedule.
The observation loss is calculated across the epicardial surface only, comparing the ground-truth and learned voltage values.
In Fig.9, the dynamics correspond to a bi-focal wave pattern that emerges after the application of two stimuli (att=0t=0) on the endocardial surface of the left ventricle (LV) in an idealized bi-ventricular geometry.
One stimulus (Focus 1) was applied to the septum, and the other (Focus 2) was applied a bit lower on the LV free wall, see Figs.9A,C) and10A,B).
The waves were simulated using the AP model, see sectionII.1.
The two focal waves propagate outward through the heart walls and eventually emerge on the epicardial surface, see Fig.9B,D).
Using our differentiable cardiac SPH simulation, we can learn the three-dimensional transmural dynamics from observations of the wave dynamics across the epicardial surface.
The loss guiding the gradient descent is computed across the spatio-temporal sequence of epicardial action potential wave patterns.
Each epoch, the algorithm modifies the parameters{θ1′,θ2′,…​θi′}\{\theta_{1}^{\prime},\theta_{2}^{\prime},...\theta_{i}^{\prime}\}and initial state(v0′,r0′)(v_{0}^{\prime},r_{0}^{\prime})att=0t=0to minimize the loss and match subsequent simulations with the ground-truth dynamics observed on the epicardial surface, see Fig.9E).
To initiate the learning, the initial state(v0′,r0′)(v_{0}^{\prime},r_{0}^{\prime})was set to a random spatial pattern, as shown in Fig.3B).
We chose this initialization intentionally to avoid making assumptions about potential subsurface patterns, such as the locations of foci.
Instead, with random initialization, the gradient-based algorithm discovers the solution fully automatically from a non-biased random initial state.
In practice, the initialization meant that the first simulations corresponded to a composition of focal and reentrant waves emerging at random locations, see first row in Fig.9E).
Note that the learning was performed using a single-horizon scheme, as illustrated in Fig.S2B), learning dynamics in 300 simulation time steps over 20,000 epochs.Figure 10:Localization of endocardial early activation sites from epicardial action potential wave dynamics.AView onto endocardial left ventricular (LV) free wall att=60t=60simulation time steps during learning after 1, 1,000, 3,000, 5,000, and 20,000 epochs. The focal point source (Focus 2) emerges on the endocardium after 20,000 epochs, see also Fig.9E). Right: Ground-truth (GT).BCorresponding view onto septum with distorted focal pattern (Focus 1) emerging after 20,000 epochs in proximity to the original source. Right: Ground-truth (GT). Data in Fig.9C) derived from panels A,B) att=40t=40.CDifference between ground-truth (GT) and learned dynamics att=60t=60becomes negligible after 20,000 epochs on the epicardial surface and the endocardial RV and LV free wall.DDiscrepancies between ground-truth and learned dynamics toward the end of the sequence att=300t=300on the endocardial surface.ESubstantial differences emerge inside the septum as the learned dynamics evolve (att=300t=300).
This indicates that activity in deeper tissue is harder to reconstruct and that single-horizon learning cannot fully recover the initial state, c.f. Figs.S2and12B).

During learning, the learned epicardial voltage wave patternv′v^{\prime}matches the ground-truth voltage wave patternvvearly on because the loss is computed across the epicardial surface, see Fig.9E).
After 5,000 epochs, both breakthrough patterns originating from foci 1 and 2 are captured well across the entire epicardial surface.
After 20,000 epochs, the learned epicardial wave pattern is visually indistinguishable from the ground-truth wave pattern.
However, it takes longer for the learned dynamics within the heart wall to match the ground-truth dynamics, see Fig.10.
After 20,000 epochs, two foci have formed on the endocardial surface, one on the septum and the other on the LV free wall, close to the original ground-truth stimuli locations, see Fig.10A,B).
Fig.9C) shows electrically active locations in the early learned states (e.g. att=40t=40,v>0.5v>0.5per particle), which roughly match the original foci locations.
While the focal pattern in the septum is distorted, it is captured well in the LV free wall, presumably because it is located closer to the epicardial surface.
We obtained similar results when applying a single stimulus either in the LV or the septum.Figure 11:Recovery of 3D electrical scroll wave from epicardial observations.ATop: learned voltage variablev′v^{\prime}(red: depolarized tissue) on the epicardial surface of the posterior wall att=10t=10simulation time steps after 100, 3,000, and 10,000 epochs of learning. Bottom: Difference to ground-truth.BTop: Learned refractory variabler′r^{\prime}(blue: refractory tissue) att=10t=10after 100, 3,000, and 10,000 epochs. Bottom: Difference to ground-truth.
While the voltage variable is directly observable, the refractory dynamics must be recovered because they cannot be directly observed.
Learning was performed within a single horizon.

After only 1 horizon, some of the parameters are recovered reasonably well (e.g.aa: 1.8% mismatch), while others still have to converge (e.g.μ1\mu_{1}: 19% mismatch).
We assume that the foci locations could be refined further by using a multi-horizon scheme, as used in sectionIII.2.
The learned initial state after one horizon, which is approximately shown in Fig.10A,B) at 20,000 epochs, is a much better starting point than the random initialization used at the beginning of the learning.
Subsequenty, it could be used to start another horizon, and a sequence of horizons would yield much better, refined reconstructions of the foci, similarly as shown for the 2D focal pulse in Fig.4.
Nevertheless, the multi-horizon schedule is only effective if subsequent horizons are shifted by a few time steps and include additional future time steps, see Fig.S2D).
Therefore, further refinements would require more data or a high temporal sampling rate, which may be a limitation with focal wave patterns measured across a finite number of samples.
However, if the sole objective is to determine early activation sites, a single horizon may already be sufficient to determine those, as demonstrated in Fig.9C).
A multi-horizon scheme is beneficial if the objective is to forecast sustained dynamics, such as spiral or scroll waves, see sectionsIII.2andIII.4.

We found that the horizon duration over which learning of the intramural wave sources is performed is critical.
The sequence in Figs.9and10includes 300 simulation time steps, which we learned in a single horizon.
We found that, if the sequence included only 200 time steps, and we aimed to recover a single pulse originating in the septum, then the learned dynamics would decay, because there are no waves on the epicardial surface (where the loss is computed) until later in the sequence.
The breakthrough of the action potential wave occurs only att=180t=180time steps.
This is too late for the gradient-based optimization: the gradient descent scheme has already downregulated the system’s excitability, the wave decays, and the optimization gets stuck in a local minimum.
However, with 300 simulation time steps, the pulse is recovered correctly.

Note that in Fig.10C), towards the end of the sequence att=300t=300simulation time steps, the difference between the learned and ground-truth epicardial wave patterns is negligible, while in panels D,E), the endocardial / intramural wave pattern exhibits substantial differences.
These differences within the heart walls arise from small differences in the learned initial state, which lead to larger divergence and errors over time.
The finding highlights that, even though the epicardial loss is small, the learned intramural wave pattern is not necessarily accurate and might be a degenerate solution.
Additional horizons, boundary conditions imposed on the dynamics, or further assumptions, such as a limited number of wave sources, could help to alleviate such issues.Figure 12:Endocardial view of learned scroll wave pattern after a single horizon with 20,000 epochs.AComparison of ground-truth (GT) voltagevvand learned voltagev′v^{\prime}over time (t=1,50,90t=1,50,90simulation time steps).
The reconstruction accuracy on the endocardium is lower because the voltage variable can only be measured on the epicardium.
Nevertheless, bothvvandv′v^{\prime}depict a counter-clockwise rotating scroll wave located in the septum and posterior wall, andv′v^{\prime}could be refined further during additional learning in subsequent horizons, as demonstrated in sectionIII.2and Figs.5and6.BComparison of ground-truth (GT) and learned voltage (red) and refractory (blue) variables early in the sequence (t=10t=10).
While the reconstruction accuracy ofrris much better on the epicardium, see Fig.11B), it is poor on the endocardium. Nevertheless, the learning has produced a refractory waveback, and this pattern could be refined further as demonstrated in sectionIII.2.

Next to focal patterns, we also reconstructed a 3D electrical scroll wave within the bi-ventricular geometry, see Figs.11and12.
As with the focal wave, the learning was performed only within a single horizon.
Fig.11A) shows that the scroll wave shape can be recovered across the epicardium almost immediately (<100 epochs), because the voltage pattern is directly observable.
On the other hand, the refractory dynamics cannot be directly observed and must be learned.
Accordingly, panel B) shows the refractory variable as it is learned over the epochs until it forms the refractory waveback.
Note that the panels show the scroll wave early in the sequence att=10t=10.
At later time steps and at fewer epochs (< 3000 epochs) the wave disintegrates similarly as the focal waves shown in Fig.9E).
After 10,000 epochs, the scroll wave becomes a stable, rotating pattern on the epicardium.
As in the focal case, it takes longer for the learned intramural dynamics to match the ground-truth dynamics, see Fig.12.
After 20,000 epochs, the learned voltage variablev′v^{\prime}forms a scroll wave-like shape on the endocardium that roughly matches the original scroll wave, even in the septum, and rotates at the same speed in the same direction.
Nevertheless, the learned refractory variabler′r^{\prime}on the endocardium is only a coarse approximation of the ground-truth pattern, and would require further refinement in subsequent horizons.
Again, the learning would benefit from a multi-horizon learning schedule, as it is demonstrated in the next sectionIII.4.

## III.4Recovery of 3D Scroll Wave Dynamics from Surface Measurements in 3D Bulk

Figs.13and14demonstrate the recovery of 3D scroll wave dynamics in a64×64×1664\times 64\times 16bulk medium with isotropic conduction, in which only the top and bottom surfaces are observed.
The observation loss is computed exclusively across the two64×64×164\times 64\times 1top and bottom surface layers, comparing the ground-truth and learned voltage valuesvvandv′v^{\prime}, while the interior1414layers remain entirely unobserved (bulk is opaque) throughout training, see Fig.13A).
Because the interior initial condition cannot be directly measured, it was initialized as a linearly weighted average of the two observed surfaces, with weights proportional to proximity: the center layer receives equal weight from both surfaces (0.5/0.50.5/0.5), while a layer at depth 3 is weighted0.25/0.750.25/0.75, and so forth.
As in previous sections, the refractory variable was estimated on the surface according to eq. (11).
The parametersθ={D,a,ϵ0,k,μ1,μ2}\theta=\{D,a,\epsilon_{0},k,\mu_{1},\mu_{2}\}were initialized between6−10%6-10\%off from the true values.Figure 13:Reconstruction of 3D scroll wave dynamics inside a bulk/slab from observations of its top and bottom surfaces.AComparison of ground-truth voltagevv(left, opaque) across surface and reconstructed 3D voltagev′v^{\prime}dynamics (right, translucent) throughout volume.
The configuration mimics simultaneous epi- and endocardial measurements of fibrillatory action potential wave dynamics in the atrial or ventricular wall.BView of top and bottom surfaces with fully dissociated wave patterns (left) and corresponding views of reconstructed volumetric 3D scroll wave pattern (right).
Overall, the parameters can be estimated with a residual error of less than0.5%0.5\%, see table5, and the reconstructed dynamics are visually indistinguishable from the ground-truth, see Fig.14.

The ground-truth system was simulated with the Aliev-Panfilov (AP) model and was initialized using a scroll wave with a slightly tilted vortex filament between the top and bottom surfaces, and then evolved forward by 1,000 time steps, producing the more complex chaotic dynamics shown in Fig.14A) (top row).
The chaotic episode was then used as the ground-truth for learning with the first chaotic state as the ground-truth initial condition.
The training window included0–9090time units, corresponding to approximately33–44scroll wave rotations, with each rotation taking approximately2626time units.
During this training window, the top and bottom surfaces were dissociated, each surface exhibiting substantially different wave patterns composed of 1-3 interacting spiral waves, similarly as shown in the left panel in Fig.13B).
Figs.13and14show the learned scroll wave dynamics after the learning was completed, and the true and learned dynamics are co-evolved into the future for comparison.
This learning setup is particularly challenging because the surface observations reflect qualitatively very different wave patterns, and the interior dynamics connecting them must be inferred entirely from the two opposing surfaces without direct observation of the 3D dynamics.Figure 14:Learning of scroll wave dynamics by observing 3-4 rotations across the bulk’s top and bottom surfaces.AGround-truth 3D scroll wave dynamics (red: voltage, first row), recovery of the scroll wave pattern during learning over5555horizons shown at10,00010,000,30,00030,000, and90,00090,000epochs (second row), and residuals between ground-truth and learned voltagevv(third row).
The residual MSE per voxel is negligible in the order of10−4−10−310^{-4}-10^{-3}in the interior of the bulk.
Learning AP scroll waves with the AP model yields near-perfect reconstructions.BCorresponding panels for the refractory variablerr.

We used a multi-horizon learning schedule comprising four "warm-up" horizons of lengths2020,2525,3030, and3535time steps (all starting att=0t=0, totaling8,0008,000epochs), followed by5151rolling horizons of length4040time steps each, with each successive horizon propagated forward by one time step (i.e.,t=0t=0–4040,11–4141,22–4242, …), for a total of110,000110,000epochs (8,0008,000warm-up and102,000102,000training), see also table3.
Each horizon was trained for2,0002,000steps.
Between horizons, the learned system is propagated forward using the learned initial conditions and parameters, and then anchored to the true observed surface voltage valuesvvat the new horizon boundaries.
As in the 2D case, the rolling multi-horizon schedule is critical for learning accurate dynamics: it enables the loss signal from the observed surfaces to be progressively propagated into the unobserved interior as parameter estimates improve.

The multi-horizon training scheme plays an especially important role in recovering the unobserved interior initial conditions.
Supplementary Video 1 visualizes the learned initial conditions across successive horizons, and shows that the interior initial conditions begin as rigid and spatially discontinuous, reflecting little more than the linear interpolation used at initialization.
However, these patterns gradually smooth into a realistic and physically plausible interior state that closely matches the ground-truth scroll wave pattern.
This progressive refinement is only possible because improved parameter estimates allow the surface anchor values to be accurately reflected back into the interior through forward simulation.
Fig.14illustrates this convergence: the top row in panel A) shows the ground-truth scroll wave dynamics (red: voltage), the second row shows the recovery of the scroll wave pattern within the differentiable simulation over the course of5555horizons, and the third row shows the voxel-wise difference (residuals) between the ground-truth voltagevvand learned voltagev′v^{\prime}.
Panel B) shows the corresponding rows for the refractory variablerr.
Both panels display snapshots at10,00010,000,30,00030,000, and90,00090,000training steps, and the learned initial conditions approach the ground-truth at approximately90,00090,000training steps (4545horizons).

After training, all learned parameters converged to within0.003−0.3%0.003-0.3\%of the true parameter values, comparable to the near-exact recovery observed in the 2D spiral wave experiments, see table5.
The internal scroll wave dynamics can be reconstructed exactly with residual errors (MSE: mean square error) per voxel in the order of10−4−10−310^{-4}-10^{-3}in the interior of the bulk.
The rapid convergence in this setting is notable given the limited surface-only observations and the high-dimensional interior state that must be inferred.
To evaluate long-term predictive accuracy, we ran both the learned and ground-truth systems forward for1,0001,000time steps beyond the training window (approximately4040spiral rotations), as shown in Supplementary Video 2.
Over this extended period, both systems dissociate into a single meandering spiral wave with a filament that is approximately straight through the bulk and consistently positioned between the top and bottom surfaces.
No significant differences between the learned and true system are observed across the full1,0001,000time steps, demonstrating that the recovered parameters and initial conditions are accurate enough to sustain precise long-range forecasts even for complex three-dimensional scroll wave dynamics observed only at the boundaries.Figure 15:State and parameter recovery with sparse observations.AGround-truth (GT) multi-spiral wave dynamics showing voltagevv(red) and refractory variablerr(blue) of the AP model.
The observationsv¯\bar{v}were limited to a grid (subsampled every 4th pixel of the voltage variable, 0 otherwise) to mimic sparse measurement data obtained with a multi-electrode array.BLearning and recovery of the dynamics over horizons and cumulative number of epochs (600 epochs per horizon in the first 10 horizons).
In each horizon, the observation window is shifted one time step into the future.
Therefore, the 3rd frame in horizon 8 is the 10th frame in the ground-truth data (gray rectangle).
The final 2nd state in the final epoch of one horizon is used to construct the initial state in the next horizon, as shown in Fig.S2D), where it is mixed with the observationv¯\bar{v}at every 4th pixel.
While the state estimation is mostly completed within∼5,000\sim 5,000epochs, the parameter estimation converges and provides sufficiently accurate parameter estimates after∼40,0000\sim 40,0000epochs, see Fig.S4C) and table4.
With sparse measurements, recovery only succeeds by adding a smoothness loss for the refractory variable.

## III.5Sparse Measurements

Fig.15demonstrates that 2D spiral wave dynamics can be recovered from sparse measurements or observations.
Panel A) shows the ground-truth (GT) multi-spiral wave dynamics (voltage variable: red, refractory variable: blue) obtained with the Aliev-Panfilov (AP) model together with the sparse observations of the voltage variablev¯\bar{v}.
Here, we measured voltage with ’electrodes’ distributed on a regular grid, subsampling the full-resolution dynamics at every 4th pixel, or at1/41/4of the original resolution, or across32×3232\times 32electrodes.
The data mimics measurements obtained with multi-electrode arrays.
The initial condition was set up as in previous sections, using eq. (11), but only for pixels located at the electrode positions.
All other pixels were initially set to zero.
During learning, the observation loss was only computed at the electrode locations.
At the beginning of each new horizon, the learned voltage variablev′v^{\prime}was updated with voltage observationsv¯\bar{v}from the electrode locations.

To counteract artifacts associated with the sparsity, we used a smoothness loss that enforces smooth spatial gradients in the field of the learned refractory variabler′r^{\prime}, as described in sectionII.3.1.
The smoothness loss was introduced in addition to the observation loss and other regularization losses, and affected only the refractory variable.
We setα=0.01\alpha=0.01to avoid inhibiting or completely smoothing out the reaction-diffusion dynamics.
With smallα\alpha, we inhibited only strong discontinuities inr′r^{\prime}between pixels associated with the grid and the other pixels, while the dynamics themselves remained unaffected.
Without the smoothness loss, the dynamics could not be learned at all; instead, we obtained strong spatial discontinuities in the learned dynamics, resembling the electrode grid pattern.

Fig.15B) shows that even complicated multi-spiral wave dynamics can be learned with sparse observations.
The learned spiral wave pattern is visually indistinguishable from the ground-truth spiral wave pattern within 8 horizons or fewer than 5,000 epochs.
Nevertheless, learning with sparse measurements takes longer: the same dynamics can be fully learned within about 20,000 epochs with full-resolution data, but learning with sparse observations requires more epochs to achieve similar accuracies.
Table4provides a comparison of the residual error of the learned parameters with full resolution learning versus with sparse observations, see also Fig.S4C).
In particular, the errors for the parameters{ϵ0,μ1,μ2}\{\epsilon_{0},\mu_{1},\mu_{2}\}stay in the single to double digit percent range after 20,000 epochs.
By comparison, at full resolution, the errors are negligible after 20,000 epochs for the same dynamics.
However, the errors continue to decrease further with continued learning, and eventually, if evolved into the future, the reconstructed sparse dynamics co-evolve congruently with the ground-truth dynamics over many rotations, similarly as shown in Figs.5and6in sectionIII.2.

## III.6Cross-Model Fitting

In sectionsIII.1-III.5, we assumed that the model equations are known and fitted a differentiable version of the Aliev-Panfilov (AP) model to spatio-temporal data generated with the AP model.
Here, we simulated spiral wave dynamics with the Mitchell-Schaeffer (MS) model and subsequently fitted the AP model to the MS data, see Fig.16.
Fig.16A) shows a comparison of ground-truth (GT) MS multi-spiral wave data and the learned or fitted AP simulation after the learning process was completed, and the two patterns co-evolve independently.
Qualitatively, the MS wave pattern is captured well by the AP model, but residual discrepancies remain due to intrinsically different characteristics of the two models, see also the comparison of the traces in panel B).
Accordingly, the pixel-wise difference map in panel A) (bottom) shows mismatches at the wave fronts and backs.
Importantly, to be able to fit one model to another, we first had to fit a sequence of action potentials in a single cell (0D), then action potential waves in a cable (1D) ring (with periodic boundary conditions), before fitting the 2D spatio-temporal dynamics with the obtained parameter estimates.
Before performing the 2D fit, we also used a DDPM, see sectionII.3.4, to generate an appropriate initial condition for the AP model.
All fits were performed fully automatically using gradient-based optimization enabled by the differentiable simulations.
Direct 2D spatio-temporal fitting, as in sectionsIII.1-III.5, with arbitrary initial parameter guesses, did not succeed.Figure 16:Cross-model learning: fitting the Aliev-Panfilov (AP) model to spiral wave data generated with the Mitchell-Schaeffer (MS) model.AComparison of ground-truth (GT) MS voltage data (top) versus fitted AP simulation (center) and pixel-wise difference (bottom). While the MS wave pattern’s topology is captured well, there are residual mismatches between the MS and the fitted AP dynamics visible at the wave fronts and backs.BTrace of the MS (red) and AP (blue) models sampled from a single location of the 2D dynamics.

## III.7Fitting Spiral Waves in a Cardiac Monolayer Cell Culture

Fig.17shows two fits of the AP model to optical mapping data of two spiral waves in two separate experiments: one showing a counter-clockwise and the other a clockwise rotating spiral wave.
The data was obtained in two different cardiac monolayer cell cultures, see sectionII.3.5.
The first spiral wave in panel A) was imaged using calcium-sensitive dye, which we used as a proxy for a voltage wave.
The second spiral wave in panel B) is a voltage or action potential spiral wave imaged using voltage-sensitive dye.
In both cases, the spiral wave dynamics were learned over 1-2 rotations using a differentiable AP model, after which the original spiral wave in the cell culture and the learned simulated spiral wave then co-evolve congruently for about 4-5 rotations before the simulated AP spiral slowly diverges.
In one case the simulated spiral wave is slightly slower and in the other case slightly faster.
Both the original and simulated spiral waves rotate in the same counter-clockwise or clockwise directions around a phase singularity located either at the center or near the boundary.
Both real and simulated spiral waves have a comparable action potential duration or wavelength.
Both regimes in panels A) and B) are very different single spiral wave regimes.
The fits were performed fully automatically using a multi-horizon learning schedule, directly with the 2D data.
The imaging data was pixel-wise normalized, and contains noise and mild imaging artifacts.Figure 17:Automated fitting to a spiral wave in two different monolayer cell cultures using differentiable cardiac electrophysiology simulations.ALeft: Counter-clockwise rotating calcium spiral wave (which we use as a proxy for voltage, red: depolarized, white: resting, normalized units) in the petri dish imaged using calcium-sensitive fluorescent dye. Center and Right: Fitted spiral (red: excitatory variable, blue: refractory variable) in the Aliev-Panfilov (AP) model at the end of the learning within 1-2 rotations (approx.). A diffusion model (DDPM) was used to generate an appropriate initial condition for the AP model.BLeft: Clockwise rotating voltage spiral wave (red: depolarized, white: resting, normalized units) in the petri dish imaged using voltage-sensitive fluorescent dye. Center and Right: Fitted spiral (red: excitatory variable, blue: refractory variable) in the Aliev-Panfilov (AP) model at the end of the learning, see also Supplementary Video 3. Learning occurs within 2 spiral rotations (approx.). A perceptual loss using the V-JEPA framework and a larger simulation domain enable fitting with noise, even when the rotor core is located close to the field-of-view boundary.

Importantly, we found that action potential wave patterns in experimental recordings cannot simply be fitted using a pixel-wise observation loss as with the simulated data.
To fit the PDE model to the experimental data in panel A), the DDPM approach described at the end of sectionII.3.4needed to be applied during initialization and repeatedly at the beginning of each new horizon during the first few horizons to reproject the learned initial state back onto the AP manifold.
This scheme provided the initial state and reset or constrained subsequent learned initial states to avoid degenerate states, while the gradient-based learning refined these states to match the observations.
To fit the PDE model to the experimental data in panel B), three adaptations were required:
(1) First, because the phase singularity of the rotating spiral wave may lie near the edge of the field of view, the PDE was integrated on a spatially expanded domain whose boundaries were positioned automatically so that the spiral tip, which was detected as the centroid of the top-1% temporal-mean|∇v||\nabla v|, fell within the central third of the simulation grid.
Initial conditions in the expanded margin were filled by linearly blending from the nearest observation-boundary pixel (w=1w=1) to a quiescent rest state (w=0w=0), and the observation loss was computed only over the original recording footprint by cropping the expanded simulation output.
(2) Second, pixel-wise loss (MSE) alone proved insufficient to guide optimization.
To address this, we augmented the total loss with a perceptual lossℒp\mathcal{L}_{p}, see also sectionII.3.1.
The total loss for the experimental fit wasℒ=ℒo​b​s+ℒr​e​g+wp⋅ℒp\mathcal{L}=\mathcal{L}_{obs}+\mathcal{L}_{reg}+w_{p}\cdot\mathcal{L}_{p}withwp=2.0w_{p}=2.0and the phase loss disabled throughout.
(3) Third, the model parameters were optimized in log-space via the bounded parameterization described in sectionII.2.1, with wider bounds than with the simulated twin AP/AP data to reflect the absence of a ground-truth reference (D∈[10−4,0.05]D\in[10^{-4},0.05],ε0∈[10−3,0.5]\varepsilon_{0}\in[10^{-3},0.5],a∈[0.01,1.0]a\in[0.01,1.0],k∈[2,20]k\in[2,20],μ1,μ2∈[0.01,0.5]\mu_{1},\mu_{2}\in[0.01,0.5]).
Training proceeded in two sequential stages: an initial run using a progressively expanding horizon schedule (starting at[0,10][0,10]frames and expanding to spans of 51 frames while sliding forward one frame per horizon, with up to 1200 epochs per horizon), followed by a second run initialized from the learned parameters of the first, applying the same expanding-then-sliding schedule to further refine the fit.

## IVDiscussion

We provide a proof-of-principle that differentiable cardiac electrophysiology simulations are an effective tool for fitting biophysical models to spatio-temporal data of action potential wave dynamics.
Using auto-differentiation techniques and gradient descent, it becomes possible to reproduce various normal and abnormal electrical rhythms, such as focal, spiral, or scroll waves in 2D and 3D tissues from partial, sparse, and noisy measurements.
The differentiable SPH simulations in bi-ventricular geometries demonstrate that intramural wave sources can be identified from epicardial measurements, even when they lie inside the septum, far from the epicardium.
The differentiable 2D and 3D slab simulations demonstrate that even complex reentrant spiral and scroll wave dynamics can be inferred from sparse or surface measurements, respectively.
With simulated data, it is possible to retrieve accurate state and parameter estimates, with assumed general model structure (equations), see sectionsIII.1-III.2, and moderate state estimates when the equations are unknown and approximated with distinct model equations, see sectionIII.6.
Thein vitroexample in Fig.17demonstrates that the technique can be applied to experimental and not just simulated data.
Our results suggest that, in future work, differentiable simulations could be used to recover transmural wave dynamics throughout the heart muscle from optical mapping, multi-electrode array (MEA), or catheter mapping recordings during sinus rhythm, premature atrial or ventricular complexes, or reentrant rhythms, such as atrial or ventricular tachycardia or even fibrillation.

The provided examples illustrate potential futureex vivo,in vitro, or clinical imaging applications.
The sparse observations across a grid in sectionIII.5mimic recordings obtained with a MEA.
Even sparser, more irregular sampling could correspond to catheter mapping.
The epi- and/or endocardial observations in sectionsIII.3andIII.4could be obtained with panoramic 3D optical mapping[15]or simultaneous dual-surface optical mapping of the epi- and endocardium[50].
The settings match those found in imaging experiments:
Planar or focal electrical waves can be imaged across the heart surface during ventricular pacing or premature ventricular complexes.
In Figs. 15-17 in Chowdhary & Lebert et al.[15], a focal wave was imaged using panoramic voltage-sensitive optical mapping and captured at 500 fps within about 60 milliseconds or 30 video images propagating across the ventricles.
In Fig.4, we aimed to learn the 2D focal pulse within 70 snapshots and obtained acceptable results using fewer than 40 snapshots.
Correspondingly, in Figs. 18 and 19 in Chowdhary & Lebert et al.[15], reentrant action potential vortex waves were imaged at 500 fps for about 10 seconds.
At this temporal resolution, a single rotation can be imaged in about 30-50 video frames, and each recording contains many rotations.
Correspondingly, with the extended observation time and self-sustained dynamics, we could easily fit a model to multiple rotations and compare forecasts against ground-truth across the heart surface for many more rotations.
Accordingly, the results in Figs.9-14suggest that the spatial and temporal resolutions are sufficient such that our method could be used to recover intramural wave dynamics from panoramic optical mapping data.
For example, it could be possible to reconstruct reentrant wave dynamics during atrial or ventricular fibrillation, or to locate focal waves originating from the Purkinje system during sinus rhythm.
With catheter mapping data, it may be possible to fit regular or repetitive rhythms, such as atrial flutter, provided that the full simulation pipeline, including the electrogram computation, is differentiable.
These are clinically important applications that could enhance the localization and ablation of cardiac arrhythmias, and we aim to pursue further translational studies using differentiable cardiac electrophysiology simulations in future work.

A key finding of our study is that successful application to experimental data requires augmenting differentiable simulations with complementary machine learning approaches, such as the Video Joint-Embedding Predictive Architecture (V-JEPA) perceptual loss or denoising diffusion probabilistic models (DDPMs), see sectionIII.7.
V-JEPA helps overcome limitations of a purely pixel-based loss, and compensates for noise and spatial mismatches between the model and experimental data.
DDPMs can be used to estimate initial conditions, or smooth intermittent dynamical states and reproject degenerate states back onto the biophysical model’s manifold.
These add-ons can be seamlessly integrated with gradient-based optimization, and we found them to be key components with the noisy, artifact-afflicted cell culture data.
Overall, our set of techniques provides a more general framework that enables differentiable simulations to be applied to real-world data and beyond the specific settings considered in other studies.
Our 2D results are closely related to the work by Lettermann et al.[39], Kashtanova et al.[32], Berg et al.[5], and Herrero Martin et al.[46].
Lettermann et al.[39]estimated parameters of the four-variable Bueno-Orovio-Cherry-Fenton[9](BOCF) model during spiral wave dynamics using a very similar gradient-based optimization approach and a pixel-based loss, which restricts the approach to simulated pixel-based data.
They subsequently fitted the two-variable Aliev-Panfilov (AP) model to the BOCF data.
More precisely, they estimated the 10 most influential parameters of the 28-parameter BOCF model, assuming the complete initial dynamical state was already known.
The AP model was fitted to the BOCF data without assuming the initial AP model state (because the corresponding state is a priori unknown), but the fitted AP dynamics quickly diverged from the BOCF dynamics, indicating poor state and parameter recovery.
The results suggest that the much simpler AP model likely cannot reproduce the BOCF dynamics.
By contrast, in our study, we chose two models that are more compatible with each other, utilized our DDPM approach to facilitate the cross-model fitting, and, as a result, the fitted AP dynamics co-evolve quite well with the Mitchell-Schaeffer (MS) dynamics.
Kashtanova et al.[32]fitted cardiac action potentials imaged with optical mapping during pacing using a hybrid approach of differentiable physics simulations and deep learning.
Here, we fitted physics-only differentiable physics simulations to optical mapping data of more complex spiral waves.
Instead of a neural network component, we used the V-JEPA perceptual loss.
Our work is also comparable to that of Berg et al.[5], who used a data assimilation approach to identify model states and parameters in 2D excitable media.
While the context is slightly different, Fig.15in sectionIII.5shows results comparable to those in Fig. 1 in Berg et al..
Nevertheless, while they performed classical parameter sweeps to find optimal parameter values, we instead utilized gradient-based optimization, which generally enables us to find optimal parameters more efficiently, particularly in higher-dimensional parameter spaces.
Our work is also related to that of Herrero Martin et al.[46]and Chiu et al.[14], who used PINNs for parameter inference with 2D and 3D simulation and optical mapping data.
While they were able to estimate spatial heterogeneity and global parameters such as action potential durations, they obtained relatively large errors for individual simulation parameters and modest performance with simulated fibrillatory wave patterns.
None of the aforementioned studies were demonstrated with realistic heart shapes or experimental data showing complex fibrillation-like patterns, and our study provides additional insights regarding sparse, partial, and noisy observations.

Compared to prior work on reconstructing 3D scroll wave dynamics from surface observations, our method achieves lower reconstruction error and improved consistency in the unobserved bulk interior.
In Marcotte et al.[45], reconstruction from surface data exhibits persistent interior error, particularly away from observed boundaries, even with stochastic model perturbations.
The data assimilation approach performs sequential state estimation using an ensemble, where observations of the excitatory variable are assimilated
over time, but the interior state and model parameters are not directly optimized.
Similarly, Hoffman et al.[28]demonstrated that data assimilation based on the Local Ensemble Transform Kalman Filter could recover major features of hidden three-dimensional scroll-wave dynamics from dual-surface observations, but reconstruction errors remained largest in the bulk interior and along wave fronts, particularly as information propagated away from observed surfaces. Hoffman and Cherry[29]further showed that reconstruction quality is highly sensitive to localization radius, observation density, and model mismatch, with ensemble collapse leading to growing interior errors when uncertainty is underestimated.
In Lebert et al.[38]and Stenger et al.[62], the reconstructions were performed using convolutional neural networks (CNNs), which produced large errors near the center of the bulk.
In Baranwal et al.[3]and Stenger et al.[62], denoising diffusion probabilistic models improved reconstruction quality relative to CNNs for long observation windows, but remained sensitive to noise and hallucination artifacts.
Importantly, these purely data-driven approaches reconstructed only the excitatory variable and did not recover hidden state variables or model parameters, making application to experimental imaging data difficult in the absence of paired ground-truth volumetric training data.
In contrast, here we jointly learn the full initial condition and model parameters from observations of only the excitatory variable on the top and bottom surfaces, recovering all interior states for both the excitatory and refractory variables without direct supervision.
This yields near-zero surface loss (∼10−9\sim 10^{-9}) and low bulk errors (∼10−5\sim 10^{-5}–10−410^{-4}).
The multi-horizon training scheme was essential, as it enables surface constraints to propagate into the interior through repeated forward simulation, progressively refining both parameters and initial conditions. Unlike prior work, which evaluates performance during assimilation with continuous observational updates, we assess the learned
system in a predictive setting; the learned dynamics remain stable over 1,000 time steps beyond training (approximately 38 spiral rotations), with residual mean squared errors on the order of10−310^{-3}–10−510^{-5}, demonstrating substantially improved system identification and long-term predictive accuracy.
Together with the fit of the experimental spiral waves in the cell culture, these findings suggest that our approach is potentially able to produce numerical 3D reconstructions of complex wave dynamics, potentially within the fibrillating heart muscle.
For instance, it could be used to uncover epi- and endocardially dissociated atrial fibrillation dynamics[22,18,66]or reconstruct scroll waves during ventricular fibrillation[17,54,16,24,4,57,6,50].

Our method appears particularly effective for more complex spiral wave dynamics and less effective for simpler wave patterns, such as focal or stationary spiral waves.
On the one hand, this may be explained by the extent of the observation data: spiral wave dynamics, if sustained, can be observed over longer periods than a single pulse.
On the other hand, more complex dynamics are more expressive, more unique, and might reveal more information about the system’s state and model parameters than simpler patterns.
As a result, the loss landscape might be more favorable with more complex wave patterns than with simpler ones.
Future work will need to determine whether this behavior is advantageous for analyzing imaging data of atrial or ventricular fibrillation.
An outstanding challenge is choosing the appropriate model equations when attempting to reconstruct fibrillation.
While it is possible to obtain near-perfect reconstructions of spiral and scroll wave dynamics when the model equations are known, see sectionsIII.1-III.5, with model mismatch, see sectionIII.6, or experimental data, see sectionIII.7, the reconstructions are more challenging.
More work is required to assess whether the current biophysical models are inadequate or the fitting framework requires further development.
In the future, our approach might enable systematic assessments of how well cardiac electrophysiology models reproduce fibrillation and related dynamics.

## VConclusions

Gradient-based optimization opens new opportunities in computational cardiology and arrhythmia research that extend beyond the training of neural networks.
Differentiable physics simulations describing cardiac electrophysiology are a promising new tool for personalizing computer simulations of the heart with many potential applications in basic cardiovascular research and diagnostics.

## Conflict of Interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Data Availability Statement

The source code will be made available upon publication.

## Funding

This research was funded by the University of California, San Francisco, the National Institutes of Health (DP2HL168071), and the Sandler Program for Breakthrough Biomedical Research, which is partially funded by the Sandler Foundation (to JC).
The RTX A5000/6000 GPUs used in this study were donated by the NVIDIA Corporation via the Academic Hardware Grant Program (to JC).
This research was also supported in part by grant NSF PHY-2309135 to the Kavli Institute for Theoretical Physics (KITP) and the Gordon and Betty Moore Foundation Grant No. 2019.02 (to EE and JC).


## Author Contributions

AP developed the finite differences-based differentiable simulations.
SC developed the SPH-based differentiable simulations.
AP and AH conceived the multi-horizon learning schedule.
AP, AH, and JC performed the analysis.
AP developed the DDPM approach.
AH developed the V-JEPA approach.
WL and EE performed the voltage-sensitive cell culture imaging experiment.
JC designed the figures and wrote the manuscript with input from AP, AH, SC, and EE.
All authors read and approved the final version of the manuscript.
SC and JC conceived the work.

## References
- [1]R. R. Aliev and A. V. Panfilov(1996)A simple two-variable model of cardiac excitation.Chaos, Solitons & Fractals7(3),pp. 293–301.External Links:DocumentCited by:§II.1,Table 1.
- [2]S. Alonso, M. Bär, and B. Echebarria(2016-08)Nonlinear physics of electrical wave propagation in the heart: a review.Reports on Progress in Physics79(9),pp. 096601.External Links:Document,LinkCited by:§I.
- [3]T. Baranwal, J. Lebert, and J. Christoph(2024-09)Dreaming of electrical waves: generative modeling of cardiac excitation waves using diffusion models.APL Machine Learning2(3),pp. 036113.External Links:ISSN 2770-9019,DocumentCited by:§II.3.4,§IV.
- [4]O. Berenfeld and A. M. Pertsov(1999)Dynamics of intramural scroll waves in three-dimensional continuous myocardium with rotational anisotropy.Journal of Theoretical Biology199(4),pp. 383–394.External Links:ISSN 0022-5193,Document,LinkCited by:§IV.
- [5]S. Berg, S. Luther, and U. Parlitz(2011-09)Synchronization based system identification of an extended excitable system.Chaos: An Interdisciplinary Journal of Nonlinear Science21(3).External Links:ISSN 10541500,DocumentCited by:§I,§IV.
- [6]O. Bernus, K. S. Mukund, and A. M. Pertsov(2007)Detection of intramyocardial scroll waves using absorptive transillumination imaging.Journal of Biomedical Optics12(1),pp. 014035.External Links:Document,LinkCited by:§IV.
- [7]C. T. Bot, A. R. Kherlopian, F. A. Ortega, D. J. Christini, and T. Krogh-Madsen(2012)Rapid genetic algorithm optimization of a mouse computational model: benefits for anthropomorphization of neonatal mouse cardiomyocytes.Frontiers in PhysiologyVolume 3 - 2012.External Links:Link,Document,ISSN 1664-042XCited by:§I.
- [8]J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman-Milne, and Q. Zhang(2018)JAX: composable transformations of python+numpy programs.Cited by:§I,§II.2.
- [9]A. Bueno-Orovio, E. M. Cherry, and F. H. Fenton(2008)Minimal model for human ventricular action potentials in tissue.Journal of Theoretical Biology253(3),pp. 544–560.External Links:ISSN 0022-5193,Document,LinkCited by:§IV.
- [10]D. I. Cairns, M. R. Comstock, F. H. Fenton, and E. M. Cherry(2025-08)CardioFit: a webgl-based tool for fast and efficient parametrization of cardiac action potential models to fit user-provided data.Royal Society Open Science12(8),pp. 250048.External Links:ISSN 2054-5703,Document,LinkCited by:§I.
- [11]D. I. Cairns, F. H. Fenton, and E. M. Cherry(2017-08)Efficient parameterization of cardiac action potential models using a genetic algorithm.Chaos: An Interdisciplinary Journal of Nonlinear Science27(9),pp. 093922.External Links:ISSN 1054-1500,DocumentCited by:§I.
- [12]J. Camps, Z. J. Wang, R. Doste, L. A. Berg, M. Holmes, B. Lawson, J. Tomek, K. Burrage, A. Bueno-Orovio, and B. Rodriguez(2025)Harnessing 12-lead ecg and mri data to personalise repolarisation profiles in cardiac digital twin models for enhanced virtual drug testing.Medical Image Analysis100,pp. 103361.External Links:ISSN 1361-8415,Document,LinkCited by:§I.
- [13]F. Chen, A. Chu, X. Yang, Y. Lei, and J. Chu(2012)Identification of the parameters of the beeler–reuter ionic equation with a partially perturbed particle swarm optimization.IEEE Transactions on Biomedical Engineering59(12),pp. 3412–3421.External Links:DocumentCited by:§I.
- [14]C. Chiu, A. Roy, S. Cechnicka, A. Gupta, A. L. Pinto, C. Galazis, K. Christensen, D. Mandic, and M. Varela(2025)Physics-informed neural networks can accurately model cardiac electrophysiology in 3d geometries and fibrillatory conditions.InStatistical Atlases and Computational Models of the Heart. Workshop, CMRxRecon and MBAS Challenge Papers.,Cham,pp. 98–109.External Links:ISBN 978-3-031-87756-8Cited by:§IV.
- [15]S. Chowdhary, J. Lebert, S. Dickman, M. Manetta, C. Gordon, and J. Christoph(2026)Panoramic voltage-sensitive optical mapping of contracting hearts using cooperative multiview motion tracking with 12 cameras.The Journal of Physiologyn/a(n/a).External Links:DocumentCited by:§I,§IV.
- [16]J. Christoph, M. Chebbok, C. Richter, J. Schröder-Schetelig, P. Bittihn, S. Stein, I. Uzelac, F. H. Fenton, G. Hasenfuss, R. Jr. Gilmour, and S. Luther(2018)Electromechanical vortex filaments during cardiac fibrillation.Nature555,pp. 667 – 672.External Links:DocumentCited by:§I,§IV.
- [17]J. M. Davidenko, A. V. Pertsov, R. Salomonsz, W. Baxter, and J. Jalife(1992)Stationary and drifting spiral waves of excitation in isolated cardiac muscle.Nature355,pp. 349–351.External Links:DocumentCited by:§I,§IV.
- [18]N. de Groot, L. van der Does, A. Yaksh, E. Lanters, C. Teuwen, P. Knops, P. van de Woestijne, J. Bekkers, C. Kik, A. Bogers, and M. Allessie(2016)Direct proof of endo-epicardial asynchrony of the atrial wall during atrial fibrillation in humans.Circulation: Arrhythmia and Electrophysiology9(5),pp. e003648.External Links:DocumentCited by:§IV.
- [19]S. Dokos and N. H. Lovell(2004)Parameter estimation in cardiac ionic models.Progress in Biophysics and Molecular Biology85(2),pp. 407–431.Note:Modelling Cellular and Tissue FunctionExternal Links:ISSN 0079-6107,Document,LinkCited by:§I.
- [20]R. Doste, J. Camps, Z. J. Wang, L. A. Berg, M. Holmes, H. Smith, M. Beetz, L. Li, A. Banerjee, V. Grau, and B. Rodriguez(2026)An automated computational pipeline for generating large-scale cohorts of patient-specific ventricular models in electromechanical in silico trials.Computer Methods and Programs in Biomedicine279,pp. 109290.External Links:ISSN 0169-2607,Document,LinkCited by:§I.
- [21]R. Doste, D. Soto-Iglesias, G. Bernardino, A. Alcaine, R. Sebastian, S. Giffard-Roisin, M. Sermesant, A. Berruezo, D. Sanchez-Quintana, and O. Camara(2019)A rule-based method to model myocardial fiber orientation in cardiac biventricular geometries with outflow tracts.International Journal for Numerical Methods in Biomedical Engineering35(4),pp. e3185.Note:e3185 cnm.3185External Links:Document,Link,https://onlinelibrary.wiley.com/doi/pdf/10.1002/cnm.3185Cited by:§II.2.2.
- [22]J. Eckstein, B. Maesen, D. Linz, S. Zeemering, A. van Hunnik, S. Verheule, M. Allessie, and U. Schotten(2010-10)Time course and mechanisms of endo-epicardial electrical dissociation during atrial fibrillation in the goat.Cardiovascular Research89(4),pp. 816–824.External Links:ISSN 0008-6363,DocumentCited by:§IV.
- [23]L. Eing, C. Luna-Jiménez, S. Mertes, and E. André(2026)Video joint-embedding predictive architectures for facial expression recognition.External Links:2601.09524,LinkCited by:§II.3.1.
- [24]F. Fenton and A. Karma(1998)Vortex dynamics in three-dimensional continuous myocardium with fiber rotation: filament instability and fibrillation.Chaos: An Interdisciplinary Journal of Nonlinear Science8(1),pp. 20–47.External Links:DocumentCited by:§IV.
- [25]L. Gepstein, G. Hayam, and S. A. Ben-Haim(1997)A novel method for nonfluoroscopic catheter-based electroanatomical mapping of the heart.Circulation95(6),pp. 1611–1622.External Links:DocumentCited by:§I.
- [26]K. Gillette, M. A.F. Gsell, A. J. Prassl, E. Karabelas, U. Reiter, G. Reiter, T. Grandits, C. Payer, D. Štern, M. Urschler, J. D. Bayer, C. M. Augustin, A. Neic, T. Pock, E. J. Vigmond, and G. Plank(2021)A framework for the generation of digital twins of cardiac electrophysiology from clinical 12-leads ecgs.Medical Image Analysis71,pp. 102080.External Links:ISSN 1361-8415,Document,LinkCited by:§I.
- [27]Y. W. Heinson, J. L. Han, and E. Entcheva(2023)Portable low-cost macroscopic mapping system for all-optical cardiac electrophysiology.Journal of Biomedical Optics28(1),pp. 016001.External Links:Document,LinkCited by:§II.3.5.
- [28]M. J. Hoffman, N. S. LaVigne, S. T. Scorse, F. H. Fenton, and E. M. Cherry(2016-01)Reconstructing three-dimensional reentrant cardiac electrical wave dynamics using data assimilation.Chaos: An Interdisciplinary Journal of Nonlinear Science26(1),pp. 013107.External Links:ISSN 1054-1500,Document,LinkCited by:§I,§IV.
- [29]M. J. Hoffman and E. M. Cherry(2020-05)Sensitivity of a data-assimilation system for reconstructing three-dimensional cardiac electrical dynamics.Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences378(2173),pp. 20190388.External Links:Document,LinkCited by:§I,§IV.
- [30]Y. Hu, L. Anderson, T. Li, Q. Sun, N. Carr, J. Ragan-Kelley, and F. Durand(2020)DiffTaichi: differentiable programming for physical simulation.External Links:1910.00935,LinkCited by:§I.
- [31]Y. Huang, A. S. Walker, and E. W. Miller(2015-08)A photostable silicon rhodamine platform for optical voltage sensing.Journal of the American Chemical Society137(33),pp. 10767—10776.External Links:Document,ISSN 0002-7863,LinkCited by:§II.3.5.
- [32]V. Kashtanova, M. Pop, I. Ayed, P. Gallinari, and M. Sermesant(2023)Simultaneous data assimilation and cardiac electrophysiology model correction using differentiable physics and deep learning.Interface Focus13(6),pp. 20230043.External Links:DocumentCited by:§I,§IV.
- [33]P. Kidger and C. Garcia(2021)Equinox: neural networks in jax via callable pytrees and filtered transformations.External Links:2111.00254,LinkCited by:§II.2.1.
- [34]P. Kidger(2021)On neural differential equations.Ph.D. Thesis,University of Oxford.Cited by:§II.2.1.
- [35]D. P. Kingma and J. Ba(2017)Adam: a method for stochastic optimization.External Links:1412.6980,LinkCited by:§II.2.1,§II.2.2,§II.3.
- [36]A. Klimas, G. Ortiz, S. C. Boggess, E. W. Miller, and E. Entcheva(2020)Multimodal on-axis platform for all-optical electrophysiology with near-infrared probes in human stem-cell-derived cardiomyocytes.Progress in Biophysics and Molecular Biology154,pp. 62–70.Note:Novel optics-based approaches for cardiac electrophysiologyExternal Links:ISSN 0079-6107,Document,LinkCited by:§II.3.5.
- [37]N. S. LaVigne, N. Holt, M. J. Hoffman, and E. M. Cherry(2017-08)Effects of model error on cardiac electrical wave state reconstruction using data assimilation.Chaos: An Interdisciplinary Journal of Nonlinear Science27(9),pp. 093911.External Links:ISSN 1054-1500,DocumentCited by:§I.
- [38]J. Lebert, M. Mittal, and J. Christoph(2023-01)Reconstruction of three-dimensional scroll waves in excitable media from two-dimensional observations using deep neural networks.Phys. Rev. E107,pp. 014221.External Links:Document,LinkCited by:§IV.
- [39]L. Lettermann, A. Jurado, T. Betz, F. Wörgötter, and S. Herzog(2024)Tutorial: a beginner’s guide to building a representative model of dynamical systems using the adjoint method.Commun. Phys.7(1).Cited by:§I,§II.2.1,§IV.
- [40]W. Liu, J. L. Han, J. Tomek, G. Bub, and E. Entcheva(2023)Simultaneous widefield voltage and dye-free optical mapping quantifies electromechanical waves in human induced pluripotent stem cell-derived cardiomyocytes.ACS Photonics10(4),pp. 1070–1083.External Links:Document,Link,https://doi.org/10.1021/acsphotonics.2c01644Cited by:§II.3.5.
- [41]A. Loewe, M. Wilhelms, J. Schmid, M. J. Krause, F. Fischer, D. Thomas, E. P. Scholz, O. Dössel, and G. Seemann(2016)Parameter estimation of ion current formulations requires hybrid optimization approach to be both accurate and reliable.Frontiers in Bioengineering and BiotechnologyVolume 3 - 2015.External Links:Document,ISSN 2296-4185Cited by:§I.
- [42]D. M. Lombardo, F. H. Fenton, S. M. Narayan, and W. Rappel(2016-08)Comparison of detailed and simplified models of human atrial myocytes to recapitulate patient specific properties.PLOS Computational Biology12(8),pp. 1–15.External Links:Document,LinkCited by:§I.
- [43]A. Lugmayr, M. Danelljan, A. Romero, F. Yu, R. Timofte, and L. Van Gool(2022)RePaint: inpainting using denoising diffusion probabilistic models.InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),pp. 11451–11461.External Links:DocumentCited by:§II.3.4.
- [44]C. D. Marcotte, M. J. Hoffman, F. H. Fenton, and E. M. Cherry(2023-09)Reconstructing cardiac electrical excitations from optical mapping recordings.Chaos: An Interdisciplinary Journal of Nonlinear Science33(9),pp. 093141.External Links:ISSN 1054-1500,DocumentCited by:§I.
- [45]C. D. Marcotte, F. H. Fenton, M. J. Hoffman, and E. M. Cherry(2021-01)Robust data assimilation with noise: applications to cardiac dynamics.Chaos: An Interdisciplinary Journal of Nonlinear Science31(1),pp. 013118.External Links:ISSN 1054-1500,Document,LinkCited by:§I,§IV.
- [46]C. H. Martin, A. Oved, R. A. Chowdhury, E. Ullmann, N. S. Peters, A. A. Bharath, and M. Varela(2022-02)EP-PINNs: cardiac electrophysiology characterisation using physics-informed neural networks.Frontiers in Cardiovascular Medicine8.External Links:Document,LinkCited by:§I,§IV.
- [47]M. J. Mendez, E. M. Cherry, G. S. Hoeker, S. Poelzing, and S. H. Weinberg(2024)Reconstructing ventricular cardiomyocyte dynamics and parameter estimation using data assimilation.Biophysical Journal123(23),pp. 4050–4066.External Links:ISSN 0006-3495,Document,LinkCited by:§I.
- [48]C. Meng, Y. He, Y. Song, S. Jiaming, J. Wu, J. Zhu, and S. Ermon(2022)SDEdit: guided image synthesis and editing with stochastic differential equations.InInternational Conference on Learning Representations (ICLR),External Links:LinkCited by:§II.3.4.
- [49]C. C. Mitchell and D. G. Schaeffer(2003/09/01)A two-current model for the dynamics of cardiac membrane.Bulletin of Mathematical Biology65(5),pp. 767–793.External Links:Document,ISBN 1522-9602,LinkCited by:§II.1.
- [50]B. G. Mitrea, M. Wellner, and A. M. Pertsov(2009)Monitoring intramyocardial reentry using alternating transillumination.In2009 Annual International Conference of the IEEE Engineering in Medicine and Biology Society,Vol.,pp. 4194–4197.External Links:DocumentCited by:§IV,§IV.
- [51]A. Monteiro da Rocha, G. Guerrero-Serna, A. Helms, C. Luzod, S. Mironov, M. Russell, J. Jalife, S. M. Day, G. D. Smith, and T. J. Herron(2016)Deficient cmybp-c protein expression during cardiomyocyte differentiation underlies human hypertrophic cardiomyopathy cellular phenotypes in disease specific human es cell derived cardiomyocytes.Journal of Molecular and Cellular Cardiology99,pp. 197–206.External Links:ISSN 0022-2828,Document,LinkCited by:§II.3.5.
- [52]A. Neic, F. O. Campos, A. J. Prassl, S. A. Niederer, M. J. Bishop, E. J. Vigmond, and G. Plank(2017)Efficient computation of electrograms and ecgs in human whole heart simulations using a reaction-eikonal model.Journal of Computational Physics346,pp. 191–211.External Links:ISSN 0021-9991,Document,LinkCited by:§I.
- [53]A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Köpf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala(2019)PyTorch: an imperative style, high-performance deep learning library.InProceedings of the 33rd International Conference on Neural Information Processing Systems,pp. 8024–8035.Cited by:§I.
- [54]A. M. Pertsov, R. Davidenko, W. T. Baxter, and J. Jalife(1993)Spiral waves of excitation underlie reentrant activity in isolated cardiac muscle.Circulation Research72,pp. 631–650.External Links:DocumentCited by:§I,§IV.
- [55]S. Pezzuto, P. Perdikaris, and F. S. Costabal(2022)Learning cardiac activation maps from 12-lead ecg with multi-fidelity bayesian optimization on manifolds.IFAC-PapersOnLine55(20),pp. 175–180.Note:10th Vienna International Conference on Mathematical Modelling MATHMOD 2022External Links:ISSN 2405-8963,Document,LinkCited by:§I.
- [56]S. Pezzuto, F. W. Prinzen, M. Potse, F. Maffessanti, F. Regoli, M. L. Caputo, G. Conte, R. Krause, and A. Auricchio(2020-11)Reconstruction of three-dimensional biventricular activation based on the 12-lead electrocardiogram via patient-specific modelling.EP Europace23(4),pp. 640–647.External Links:ISSN 1099-5129,Document,Link,https://academic.oup.com/europace/article-pdf/23/4/640/36916991/euaa330.pdfCited by:§I.
- [57]Z. Qu, J. Kil, F. Xie, A. Garfinkel, and J. N. Weiss(2000)Scroll wave dynamics in a three-dimensional cardiac tissue model: roles of restitution, thickness, and fiber rotation.Biophysical Journal78(6),pp. 2761–2775.External Links:ISSN 0006-3495,Document,LinkCited by:§IV.
- [58]W. Rappel(2022)The physics of heart rhythm disorders.Physics Reports978,pp. 1–45.External Links:ISSN 0370-1573,DocumentCited by:§I.
- [59]E. Rheaume, H. Velasco-Perez, D. Cairns, M. Comstock, E. Rheaume, A. Kaboudian, I. Uzelac, E. Cherry, and F. H. Fenton(2023)A modified fitzhugh-nagumo model that reproduces the action potential and dynamics of the ten tusscher et al. cardiac model in tissue.Computing in Cardiology 202350(),pp..External Links:ISSN 2325-887X,DocumentCited by:§I.
- [60]S. S. Schoenholz and E. D. Cubuk(2020)JAX, m.d. a framework for differentiable physics.InProceedings of the 34th International Conference on Neural Information Processing Systems,NIPS ’20,Red Hook, NY, USA.External Links:ISBN 9781713829546Cited by:§I,§II.2.2.
- [61]G. Seemann, S. Lurz, D. U. J. Keller, D. L. Weiss, E. P. Scholz, and O. Dössel(2009)Adaption of mathematical ion channel models to measured data using the particle swarm optimization.In4th European Conference of the International Federation for Medical and Biological Engineering,J. Vander Sloten, P. Verdonck, M. Nyssen, and J. Haueisen (Eds.),Berlin, Heidelberg,pp. 2507–2510.External Links:ISBN 978-3-540-89208-3Cited by:§I.
- [62]Stenger,R., Herzog,S., Kottlarz,I., Rüchardt,B., Luther,S., Wörgötter,F., and Parlitz,U.(2023)Reconstructing in-depth activity for chaotic 3d spatiotemporal excitable media models based on surface data.Chaos: An Interdisciplinary Journal of Nonlinear Science33(1),pp. 013134.External Links:Document,Link,https://doi.org/10.1063/5.0126824Cited by:§IV.
- [63]Z. Syed, E. Vigmond, S. Nattel, and L. J. Leon(2005-10-01)Atrial cell action potential parameter fitting using genetic algorithms.Medical and Biological Engineering and Computing43(5),pp. 561–571.External Links:ISSN 1741-0444,Document,LinkCited by:§I.
- [64]B. J. Thomas, C. Goodbrake, K. Meyer, and M. S. Sacks(2025)High speed cardiac simulations using the jax framework.InFunctional Imaging and Modeling of the Heart,R. Chabiniok, Q. Zou, T. Hussain, H. H. Nguyen, V. G. Zaha, and M. Gusseva (Eds.),Cham,pp. 275–281.External Links:ISBN 978-3-031-94559-5Cited by:§I.
- [65]N. Thuerey, B. Holzschuh, P. Holl, G. Kohl, M. Lino, Q. Liu, P. Schnell, and F. Trost(2025)Physics-based deep learning.External Links:2109.05237,LinkCited by:§I.
- [66]T. E. Walters, G. Lee, A. Lee, R. Sievers, J. M. Kalman, and E. P. Gerstenfeld(2020)Site-specific epicardium-to-endocardium dissociation of electrical activation in a swine model of atrial fibrillation.JACC: Clinical Electrophysiology6(7),pp. 830–845.External Links:ISSN 2405-500X,Document,LinkCited by:§IV.
- [67]R. Winchenbach and N. Thuerey(2026)DiffSPH: differentiable smoothed particle hydrodynamics for hybrid machine learning solutions in fluid mechanics.Journal of Computational Physics555,pp. 114769.External Links:ISSN 0021-9991,Document,LinkCited by:§I.
- [68]C. Zhang, M. Rezavand, Y. Zhu, Y. Yu, D. Wu, W. Zhang, J. Wang, and X. Hu(2021)SPHinXsys: an open-source multi-physics and multi-resolution library based on smoothed particle hydrodynamics.Computer Physics Communications267,pp. 108066.External Links:ISSN 0010-4655,Document,LinkCited by:§II.1,§II.2.2.
- [69]C. Zhang, J. Wang, M. Rezavand, D. Wu, and X. Hu(2021-08)An integrative smoothed particle hydrodynamics method for modeling cardiac function.Computer Methods in Applied Mechanics and Engineering381,pp. 113847.External Links:Document,ISSN 0045-7825Cited by:§II.1,§II.2.2.

## Supplementary Information

## Supplementary Videos

Supplementary Videos will be provided at:https://cardiacvision.ucsf.edu/videos/diffsim/.

## V.1Supplementary TablesParam.DDkkaaϵ0\epsilon_{0}μ1\mu_{1}μ2\mu_{2}Fig.40.00118.00.15000.020.150.15Figs.5,60.00119.00.12000.010.160.2Fig.80.00106.00.05000.090.100.15Figs.9-12Di​s​oD_{iso}8.00.05000.020.200.30Figs.13,140.00118.00.10350.020.150.15Fig.150.00118.00.10000.020.160.12Table 1:Parameters of Aliev-Panfilov[1](AP) model used to simulate electrical action potential wave patterns in different sections of this study.HorizonHorizonsDurationEpochsEpochsNumber(n)nen_{e}TotalStage 11-1010106006,000Stage 211-20102080014,000Stage 321-3010401,00024,000Table 2:Parameters of learning schedule used in Figs.4,5-8and15. The schedule comprises 3 subsequent stages with 10 horizons each and 600, 800, and 1,000 epochs per horizon. The horizon duration increases from 10 to 20 to 40 time steps in each stage, and each horizon is shifted by 1 time step (Δ​t=1\Delta t=1).
After 10, 20, and 30 horizons, the learning was performed over 20, 40, and 70 time steps, respectively.
At the end of the full schedule, the learning was performed over 24,000 epochs.
The schedule can, in principle, vary and include more or fewer stages, horizons, horizon durations, or epochs, see also table3.
In Figs.5,6and8the learning was stopped prematurely (e.g. after Stage 2 or 14,000 epochs).HorizonHor.DurationEpochsEpochsNumber(n)nen_{e}TotalW111202,0002,000W221252,0004,000W331302,0006,000W441352,0008,000Rolling5-5551402,000110,000Table 3:Parameters of learning schedule used in Figs.13and14.
The schedule comprises 4 subsequent "warm-up" horizons (W1-W4), which refine the initial condition, followed by a rolling multi-horizon schedule comprising 51 horizons, which learn the dynamics, see also sectionIII.4.
The horizon duration increases during warm-up and then stays constant during the rolling horizons.
Each horizon is learned over 2,000 epochs.
The 51 multi-horizons are learned over 102,000 epochs.
At the end of the full schedule, the learning was performed over 110,000 epochs.Fig.DDaakkϵ0\epsilon_{0}μ1\mu_{1}μ2\mu_{2}40.00110.15008.00000.02000.15000.15000.00110.14938.01180.01950.15240.15720.05%0.45%0.15%2.70%1.61%4.77%5,60.00110.12009.00000.01000.16000.20000.00110.12009.00000.01000.16000.20000.00%0.00%0.00%0.02%0.00%0.00%150.00110.10008.00000.02000.16000.12000.00110.09987.95640.01850.16370.13331.22%0.15%0.54%7.64%2.32%11.10%Table 4:Ground-truth parameters (top), learned parameters (center), and error (bottom) for the different 2D wave dynamics shown in Figs.4,5and15.
All results were obtained with 20,000 epochs and the same multi-horizon learning schedule.
The errors are negligible with spiral wave dynamics (Fig.5), but can be up to several percent with sparse or limited observations.
The errors in Fig.15would decrease further with additional learning.Fig.DDaakkϵ0\epsilon_{0}μ1\mu_{1}μ2\mu_{2}140.00110.10358.00000.02000.15000.15000.00110.10368.00030.02000.14980.14960.04%0.06%0.00%0.20%0.15%0.27%Table 5:Ground-truth parameters (top), learned parameters (center), and error (bottom) for 3D scroll wave dynamics in a bulk with surface-only observations, as shown in Fig.14.

## V.2Supplementary FiguresFigure S1:AFocal voltage wave patternvv(red) with initial guesses for the learned refractory patternr′r^{\prime}(blue). Left to right:r′=v+σr^{\prime}=v+\sigma,r′=v⋅σr^{\prime}=v\cdot\sigmaandr′=σr^{\prime}=\sigmawith Gaussian noiseσ\sigma. The first option is the best-performing initial condition, see also Fig.S3A). Constant fieldsr′=a,a∈ℝr^{\prime}=a,a\in\mathbb{R}orr′=0r^{\prime}=0lead to numerical instability.BInitial conditions evolved at the end of Epoch 1 in Horizon 1 with 10 time steps.Figure S2:Learning schedule for gradient-descent-based state and parameter estimation of spatio-temporal electrical wave dynamics in excitable media.AExample of simulated spiral wave dynamics observed over about 3 rotations, the observations comprising 80 time steps.BLearning over a single horizon that includes all 80 time steps, starting with an initial guess of the initial condition / first dynamical state (black), with the task to obtain an estimate of all model parameters and the final dynamical state at the final time step (gray).CMulti-horizon learning schedule consisting of 3 subsequent horizons with different lengths (example).
In each horizon, the last learned state (gray) is used to construct the first state of the next horizon (black).DMulti-horizon learning schedule with rolling, overlapping horizons of different lengths, altogether covering the 80 time steps (example). Here, the second learned time step is used to initiate the next horizon.Figure S3:Effect of learning schedule onto loss curve with data shown in Fig.4.ASteeper loss curve withr′∼vr^{\prime}\sim vor focal-shaped (black) vs. homogeneous noisy (red) initialization ofr′r^{\prime}, see also Fig.S1A).BSingle-horizon learning over horizons with 20 (red) or 10 (black) time steps. Loss never reaches levels<10−5<10^{-5}.CSingle-horizon (red) vs. 2-horizon (black) learning schedule with 10 time step horizons. Loss reaches levels<10−5<10^{-5}after fewer than 1500 epochs in horizon 2.D2-horizon learning schedules with constant learning rates of0.010.01(red),0.00010.0001(gray), and0.0010.001(black, ideal).Figure S4:Parameters (black: ground-truth, light gray: initial guess, dark gray: learned) for different wave dynamics.ASpiral wave dynamics shown in Figs.5and6fully learned (2 separate runs) after 70 observation time steps (∼4.5\sim 4.5rotations) within 30 horizons learned over 24,000 epochs.BFocal wave shown in Fig.4. While parameters{D,a,k}\{D,a,k\}have converged,{ϵ0,μ1,μ2}\{\epsilon_{0},\mu_{1},\mu_{2}\}have not fully converged after 80 observation time steps or 40 horizons or 34,000 epochs.CSparse multi-spiral waves shown in Fig.15. As in C), the parameters{ϵ0,μ1,μ2}\{\epsilon_{0},\mu_{1},\mu_{2}\}have not fully converged after 40 horizons, indicating that longer observation times are necessary. In both cases, the parameter history curves indicate that the learned parameters would eventually converge. See Table4for values and errors.

## 


- 


Major funding support from
