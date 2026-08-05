# Physics-informed neural networks for two-dimensional wall-reactive solute dispersion in canonical shear flows

**arXiv ID**: 2608.00856v1
**Authors**: Nanda Poddar, Subham Dhar
**Published**: 2026-08-01
**Categories**: physics.flu-dyn, math-ph, physics.comp-ph, stat.ML
**HTML URL**: https://arxiv.org/html/2608.00856v1

## Abstract

The dispersion of reactive solutes in shear flows is governed by the interplay between advective stretching, transverse diffusion, and boundary exchange kinetics. While classical analytical methods and grid-based numerical solvers have extensively characterised these transport mechanisms, accurately resolving the spatiotemporal evolution of solute plumes in asymmetric reactive environments remains computationally demanding. In this study, we introduce a physics-informed neural network (PINN) framework to simulate two-dimensional wall-reactive solute dispersion in canonical shear flows (Couette, Poiseuille, and Couette-Poiseuille) bounded by absorbing walls. By embedding the governing convection-diffusion equation and Robin boundary conditions into a unified loss function, the mesh-free PINN reconstructs the spatiotemporal concentration field. The network predictions are validated against an alternating-direction implicit (ADI) finite-difference benchmark, showing close agreement across non-reactive, symmetric, and asymmetric reactive regimes. The computations are carried out at $\mathrm{Pe}=10$ for impermeable walls, symmetric absorption $(β_1,β_2)=(1,1)$, and tenfold asymmetric wall-reactivity contrasts $(β_1,β_2)=(0.2,2)$ and (2,0.2). Leveraging the differentiable nature of the trained PINN, we extract wall-resolved transport diagnostics, including the apparent axial dispersion coefficient, cumulative wall-removal dynamics, and localised uptake fluxes. The results show that the imposed shear profile governs the streamwise organisation of reactive uptake, while unequal wall reactivities induce transverse asymmetry that modifies the macroscopic spreading rate. Overall, this framework establishes PINNs as an interpretable mesh-free tool for analysing boundary-coupled reactive transport in shear flows.

## Full Text

Physics-informed neural networks for two-dimensional wall-reactive solute dispersion in canonical shear flows

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.00856v1 [physics.flu-dyn] 01 Aug 2026

## Physics-informed neural networks for two-dimensional wall-reactive solute dispersion in canonical shear flowsNanda Poddar\aff1,2\correspSubham Dhar\aff3\aff1Department of Mathematics, College of Engineering and Technology, SRM Institute of Science and Technology, Kattankulathur, Tamil Nadu 603203, India\aff2School of Mathematical and Statistical Sciences, University of Galway, Galway H91TK33, Ireland\aff3Department of Civil Engineering, National Taiwan University, Taipei City 10617, Taiwan

## Abstract

The dispersion of reactive solutes in shear flows is governed by the interplay between advective stretching, transverse diffusion, and boundary exchange kinetics. While classical analytical methods and grid-based numerical solvers have extensively characterised these transport mechanisms, accurately resolving the spatiotemporal evolution of solute plumes in asymmetric reactive environments remains computationally demanding. In this study, we introduce a physics-informed neural-network (PINN) framework to simulate two-dimensional wall-reactive solute dispersion in canonical shear flows (Couette, Poiseuille, and Couette–Poiseuille) bounded by absorbing walls. By embedding the governing convection–diffusion equation and Robin boundary conditions into a unified loss function, the mesh-free PINN reconstructs the spatiotemporal concentration field. The network predictions are validated against an alternating-direction implicit (ADI) finite-difference benchmark, showing close agreement across non-reactive, symmetric, and asymmetric reactive regimes. The computations are carried out atPe=10\mathrm{Pe}=10for impermeable walls, symmetric absorption(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1), and tenfold asymmetric wall-reactivity contrasts(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2)and(2,0.2)(2,0.2). Leveraging the differentiable nature of the trained PINN, we extract wall-resolved transport diagnostics, including the apparent axial dispersion coefficient, cumulative wall-removal dynamics, and localised uptake fluxes. The results show that the imposed shear profile governs the streamwise organisation of reactive uptake, while unequal wall reactivities induce transverse asymmetry that modifies the macroscopic spreading rate. Overall, this framework establishes PINNs as an interpretable mesh-free tool for analysing boundary-coupled reactive transport in shear flows.

## keywords:Mass Transport, Computational methods

## 1Introduction

The dispersion of reactive solutes in fluid flows is a ubiquitous phenomenon governing mass transport across a wide spectrum of natural and engineered environments, from groundwater aquifers and environmental flows to chemical reactors and microfluidic devices. The spatiotemporal evolution of these solute plumes is dictated by a complex interplay among advection, molecular diffusion, and chemical kinetics. In shear flows, this coupling is fundamentally amplified; velocity gradients continuously stretch and fold the concentration fields, profoundly altering both the effective macroscopic dispersion and the localised boundary reaction rates. Consequently, a rigorous understanding of these coupled hydro-chemical mechanisms is essential for the accurate prediction of reactive mixing and the optimal design of transport-reliant engineering systems.

The transport of solutes in flowing fluids has been the focus of extensive research for more than seven decades due to its significance in environmental, geophysical, biological, and industrial applications. Understanding the combined effects of molecular diffusion and velocity gradient on solute dispersion was the main goal of early research. Groundbreaking research byTaylor (1953)showed that shear-induced velocity gradients greatly increase longitudinal dispersion beyond molecular diffusion alone. The theoretical basis of solute dispersion in laminar flows was subsequently established byAris (1956), who extended Taylor’s analysis using moment techniques. The initial transient development of diffusion and the approach to normality were subsequently rigorously examined(Lighthill,1966; Chatwin,1970), whileGill and Sankarasubramanian (1970)formulated the exact analysis of unsteady convective diffusion. The method of moments was substantially formalised byBarton (1983), enabling systematic computation of transport coefficients. Three-time regimes are characterised byLatini and Bernoff (2001)for Poiseuille flow. Further explorations of shear dispersion in Poiseuille flows, and straight pipes have since established a robust theoretical framework for characterising concentration distributions(Stokes and Barton,1990; Wu and Chen,2014a,b; Guan and Chen,2024).

However, the conservative tracer and impermeable-boundary assumptions of classical Taylor-Aris theory are rarely satisfied in real-world transport systems. Solutes constantly exchange with surrounding tissues through permeable vessel walls in physiological systems, whereas dissolved species undergo adsorption, absorption, or chemical reactions at the confining interfaces in many environmental applications. These boundary interactions significantly change the mean transport rate and the longitudinal spreading of the solute cloud(Aris,1959; Sankarasubramanian and Gill,1973). The impact of homogeneous, heterogeneous, and kinetic sorptive reactions has been extensively analysed for tubes, open channels, and annular flows(Gupta and Gupta,1972; Smith,1983; Purnama,1988; Das and Mazumder,1989; Ng and Yip,2001; Sarkar and Jayaraman,2002; Mondal and Mazumder,2005; Barik and Dalal,2017; Debnath and Ghoshal,2020). More recently, the complexities of reversible and irreversible boundary reactions have been addressed using sophisticated analytical techniques(Ng,2006; Ng and Rudraiah,2008; Jiang and Chen,2018; Barik and Dalal,2022; Jianget al.,2022), revealing how phase-exchange mechanisms and boundary desorption govern the transient and asymptotic states of the solute cloud.

While steady models are foundational, contemporary research increasingly focuses on complex, time-dependent hydrodynamic environments. Oscillatory and pulsatile flows introduce intricate advective-diffusive coupling, heavily influencing mass transport in estuaries, blood vessels, and engineered channels(Allen,1982; Mazumder and Das,1992; Bandyopadhyay and Mazumder,1999b,a; Paul and Mazumder,2008; Barik and Dalal,2019). Analytical and semi-analytical moment techniques have been further extended to capture higher-order statistics (such as skewness and kurtosis) in these unsteady and porous regimes(Daset al.,2024b; Jiang and Chen,2026). The coupled transport physics is compounded by non-Newtonian rheologyRana and Murthy (2016)and active suspensions(Caldag and Bees,2025). Furthermore, environmental and physiological applications demand the incorporation of vegetation drag, bulk degradation, and magnetohydrodynamic (MHD) effects, leading to highly complex governing equations across steady and oscillatory Couette–Poiseuille flows(Debnath and Ghoshal,2020; Dharet al.,2021; Poddaret al.,2021c,a,2023; Daset al.,2024a; Poddar and Wang,2024; Poddaret al.,2024; Sahaet al.,2024).

Despite the extensive theoretical and experimental characterisation of shear-driven dispersion, numerical simulation of the underlying reactive transport often relies on classical mesh-based discretisation(Mondal and Mazumder,2006; Mondalet al.,2020; Poddaret al.,2021b; Douglas,1955; Peaceman and Rachford,1955). These traditional methods can become computationally demanding, particularly when resolving complex boundary interactions and transient concentration gradients. Recently, Physics-Informed Neural Networks (PINNs) have emerged as a powerful, mesh-free deep learning framework capable of solving nonlinear partial differential equations by embedding physical laws directly into the network’s loss function(Raissiet al.,2019).

Early research mainly showed that PINNs could deduce unknown transport parameters from sparse data and solve forward and inverse advection-diffusion equations. For instance,He and Tartakovsky (2021)demonstrated that PINNs can accurately estimate unknown coefficients from sparse data and reliably recover solutions of advection-dispersion equations over a broad range of Péclet numbers. The numerical accuracy and convergence of advection-diffusion-reaction simulations were then improved by the orthogonal-grid PINN framework ofHouet al.(2022), which incorporated derivative restrictions and structured collocation techniques during training. In recent years, PINNs have been utilised to solve complex environmental transport problems, including coupled surface flow and solute transport(Niuet al.,2023), multispecies contaminant migration with spatially varying transport parameters(Houet al.,2025), adaptive Runge–Kutta PINNs for stiff multicomponent reactive transport(Shuet al.,2026), surrogate modelling of reactive nitrate transport in groundwater(Arabet al.,2026), and passive scalar emission(Rawdenet al.,2026). In inverse advection-diffusion-reaction problems, where unknown reaction rates and transport coefficients are obtained concurrently with the concentration field, PINNs have also been investigated(Mamudet al.,2023). Furthermore, advanced PINN architectures have been increasingly deployed for complex, coupled systems, such as reactive solute transport in parameterised groundwater models(Jiaoet al.,2026), solute concentration distributions in continuous crystallizers(Cuiet al.,2026), and water and nitrogen transport in unsaturated soils(Kamilet al.,2025). Related machine-learning techniques have been utilised to infer flow fields around active colloidal particles(Mohapatraet al.,2025), explore soliton collisions(Qiuet al.,2025), and discover multiple PDE solutions using deep ensembles(Zouet al.,2025). Most studies of solute dispersion adopt a Dirac delta initial condition to model instantaneous tracer release, whereas only a few consider Gaussian pulses(Tenget al.,2023). The singularity associated with the Dirac delta source poses a significant challenge for PINNs, which rely on smooth neural-network approximations and automatic differentiation.

Motivated by these computational challenges and the recent successes of deep learning in fluid mechanics, this study introduces a physics-informed neural network (PINN) framework specifically tailored for two-dimensional reactive solute dispersion in canonical shear flows. While traditional grid-based solvers demand high-resolution meshing to accurately capture sharp concentration gradients near reactive boundaries, our mesh-free approach embeds the governing convection–diffusion equation, localised initial source distributions, and reactive Robin boundary constraints directly into a unified composite loss function. To rigorously establish the physical fidelity of this data-driven approach, the learned PINN solutions are systematically validated against a classical alternating-direction implicit (ADI) finite-difference benchmark(Douglas,1955; Peaceman and Rachford,1955; Mondal and Mazumder,2006). However, the novelty of the present work lies not merely in reconstructing the spatiotemporal concentration field with high accuracy, but in leveraging the continuous, fully differentiable nature of the trained PINN surrogate to extract complex transport diagnostics. By circumventing the discrete approximations required by classical numerical methods, we directly compute the time-dependent effective dispersion coefficient, total surviving mass, and localised wall fluxes across Couette, Poiseuille, and Couette–Poiseuille flows. This continuous representation enables a precise evaluation of reaction-induced transverse asymmetry, cumulative wall-removal dynamics, and the streamwise organisation of reactive uptake. Ultimately, this study demonstrates that PINNs can serve not just as an alternative PDE solver but as a highly interpretable, data-efficient tool for decoding the coupled hydrodynamic and chemical mechanisms governing solute transport.

The remainder of this paper is organised as follows. Section2details the mathematical formulation of the two-dimensional reactive transport model, including the governing equations, initial source configurations, and the mean-centred canonical shear flows. Section3outlines the physics-informed neural network methodology, detailing the composite loss construction, training strategy, physical interpretation of the learned solution, and the ADI finite-difference benchmark. Section4presents the results and discussion, beginning with a rigorous validation of the PINN framework against the ADI benchmark, followed by an in-depth analysis of wall-resolved reactive dispersion, reaction-induced transverse asymmetry, and cumulative wall-removal dynamics. Finally, the main conclusions of this study are summarised in Section5.

## 2Mathematical formulation

## 2.1Geometry and variables

We consider two-dimensional solute transport in a laminar shear flow between two parallel plates located aty∗=±Hy^{*}=\pm H. The coordinatesx∗x^{*}andy∗y^{*}denote the streamwise and wall-normal directions, respectively, andt∗t^{*}denotes time. The solute concentration is denoted byC∗​(x∗,y∗,t∗)C^{*}(x^{*},y^{*},t^{*}). The dimensional flow domain isΩ∗={(x∗,y∗):x∗∈ℝ,−H≤y∗≤H}.\Omega^{*}=\{(x^{*},y^{*}):x^{*}\in\mathbb{R},\;-H\leq y^{*}\leq H\}.

## 2.2Dimensional convection–diffusion model

The solute is transported by a prescribed unidirectional shear flowu∗​(y∗)u^{*}(y^{*})and diffuses isotropically with molecular diffusivityDD. The governing dimensional convection–diffusion equation is∂C∗∂t∗+u∗​(y∗)​∂C∗∂x∗=D​(∂2C∗∂x∗2+∂2C∗∂y∗2),(x∗,y∗)∈Ω∗,t∗>0.\frac{\partial C^{*}}{\partial t^{*}}+u^{*}(y^{*})\frac{\partial C^{*}}{\partial x^{*}}=D\left(\frac{\partial^{2}C^{*}}{\partial x^{*2}}+\frac{\partial^{2}C^{*}}{\partial y^{*2}}\right),\qquad(x^{*},y^{*})\in\Omega^{*},\quad t^{*}>0.(1)

Hereu∗​(y∗)u^{*}(y^{*})represents a canonical parallel-plate shear profile, specified below.

At the plates, the solute undergoes first-order uptake. With reaction ratesκ1\kappa_{1}andκ2\kappa_{2}at the upper wally∗=Hy^{*}=Hand lower wally∗=−Hy^{*}=-H, respectively, the dimensional Robin conditions are−D​∂C∗∂y∗−κ1​C∗=0at​y∗=H,D​∂C∗∂y∗−κ2​C∗=0at​y∗=−H.-D\frac{\partial C^{*}}{\partial y^{*}}-\kappa_{1}C^{*}=0\quad\text{at }y^{*}=H,\qquad D\frac{\partial C^{*}}{\partial y^{*}}-\kappa_{2}C^{*}=0\quad\text{at }y^{*}=-H.(2)

The caseκi=0\kappa_{i}=0corresponds to an impermeable wall, while increasingκi\kappa_{i}represents stronger wall absorption. These first-order Robin conditions are widely used to model irreversible absorption, reversible phase exchange, and retention kinetics at the boundaries of confined flowsPurnama (1988); Ng and Rudraiah (2008); Poddaret al.(2021c).

A localised solute release is prescribed att∗=0t^{*}=0:C∗​(x∗,y∗,0)=C0∗​(x∗,y∗).C^{*}(x^{*},y^{*},0)=C_{0}^{*}(x^{*},y^{*}).(3)

## 2.3Nondimensionalization

We introduce the dimensionless variablesx=x∗−u¯∗​t∗H,y=y∗H,t=D​t∗H2,C=C∗Cref,u​(y)=u∗​(y∗)Uref,u¯=u¯∗Urefx=\frac{x^{*}-\overline{u}^{*}t^{*}}{H},\qquad y=\frac{y^{*}}{H},\qquad t=\frac{Dt^{*}}{H^{2}},\qquad C=\frac{C^{*}}{C_{\mathrm{ref}}},\qquad u(y)=\frac{u^{*}(y^{*})}{U_{\mathrm{ref}}},\quad\overline{u}=\frac{\overline{u}^{*}}{U_{\mathrm{ref}}}

whereUrefU_{\mathrm{ref}}is the characteristic velocity scale associated with the imposed shear flow and the overbar denotes the corresponding cross-sectional average. The corresponding Péclet number and wall-reactivity parameters arePe=Uref​HD,βi=κi​HD,i=1,2.\mathrm{Pe}=\frac{U_{\mathrm{ref}}H}{D},\qquad\beta_{i}=\frac{\kappa_{i}H}{D},\qquad i=1,2.

The dimensionless convection–diffusion equation becomes∂C∂t+Pe​(u​(y)−u¯)​∂C∂x=∂2C∂x2+∂2C∂y2,x∈ℝ,−1<y<1,t>0.\frac{\partial C}{\partial t}+\mathrm{Pe}\,\left(u(y)-\overline{u}\right)\frac{\partial C}{\partial x}=\frac{\partial^{2}C}{\partial x^{2}}+\frac{\partial^{2}C}{\partial y^{2}},\qquad x\in\mathbb{R},\quad-1<y<1,\quad t>0.(4)

In the computations below, this mean-deviated velocity is denoted directly byu(s)​(y)u^{(s)}(y)for each canonical shear profile.
The dimensionless reactive wall conditions are−∂C∂y−β1​C=0at​y=1,∂C∂y−β2​C=0at​y=−1.-\frac{\partial C}{\partial y}-\beta_{1}C=0\quad\text{at }y=1,\qquad\frac{\partial C}{\partial y}-\beta_{2}C=0\quad\text{at }y=-1.(5)

The associated local dimensionless uptake fluxes at the upper and lower plates areJ+​(x,t)=β1​C​(x,1,t),J−​(x,t)=β2​C​(x,−1,t).J_{+}(x,t)=\beta_{1}C(x,1,t),\qquad J_{-}(x,t)=\beta_{2}C(x,-1,t).(6)

HereJ+J_{+}andJ−J_{-}denote the uptake fluxes at the upper and lower plates, respectively. These fluxes provide a local physical measure of how each imposed shear flow transports solute toward the reactive walls.

## 2.4Initial source configurations

To test the sensitivity of reactive dispersion to the form of the initial release, we consider two smooth Gaussian source configurations. The first is a streamwise-localised line-like source,C0L​(x,y)=exp⁡(−x2),x∈[x0,x1],−1≤y≤1.C_{0}^{\mathrm{L}}(x,y)=\exp(-x^{2}),\qquad x\in[x_{0},x_{1}],\quad-1\leq y\leq 1.(7)

This source is localised in the streamwise direction and uniform across the channel height.

The second is a point-like two-dimensional Gaussian source,C0P​(x,y)=exp⁡(−x2−y2),x∈[x0,x1],−1≤y≤1.C_{0}^{\mathrm{P}}(x,y)=\exp(-x^{2}-y^{2}),\qquad x\in[x_{0},x_{1}],\quad-1\leq y\leq 1.(8)

This source is localised in both the streamwise and wall-normal directions and provides a smooth approximation to a point release centred at the channel midplane.

Both choices avoid directly imposing a singular Dirac delta distribution. A Dirac delta is not a classical continuous function and is therefore not compatible with the pointwise mean-square initial-condition loss used in the present PINN formulation. The Gaussian sources may be interpreted as mollified releases; singular-source formulations are left for future work through weak-form PINNs, Green ’s-function-based formulations or distributional residuals.

## 2.5Mean-centred canonical shear-flow choices

In (4), the imposed velocity is written asu​(y)=u(s)​(y),s∈𝒮:={C,Po,CP},u(y)=u^{(s)}(y),\qquad s\in\mathcal{S}:=\{\mathrm{C},\mathrm{Po},\mathrm{CP}\},

whereC\mathrm{C},Po\mathrm{Po}andCP\mathrm{CP}denote Couette, Poiseuille and Couette–Poiseuille flow, respectively. The same source configuration, wall reactivity and axial boundary conditions are imposed for eachs∈𝒮s\in\mathcal{S}; hence, differences in the computed concentration fields are attributable to the imposed shear profile.

The nondimensionalization fixes the velocity scale throughUrefU_{\mathrm{ref}}. The following centring is therefore not a rescaling but a choice of frame. Let⟨f⟩y=12​∫−11f​(y)​dy\langle f\rangle_{y}=\frac{1}{2}\int_{-1}^{1}f(y)\mathrm{d}y

denote the cross-sectional average. For each canonical flow, we writeu(s)​(y)=u~(s)​(y)−⟨u~(s)⟩y,⟨u(s)⟩y=0.u^{(s)}(y)=\widetilde{u}^{(s)}(y)-\left\langle\widetilde{u}^{(s)}\right\rangle_{y},\qquad\left\langle u^{(s)}\right\rangle_{y}=0.(9)

Hereu~(s)​(y)\widetilde{u}^{(s)}(y)denotes the usual dimensionless shear profile, whileu(s)​(y)u^{(s)}(y)is the mean-centred profile used in the transport equation. This is equivalent to observing the solute cloud in a frame moving with the bulk velocity. It removes uniform streamwise translation while retaining the shear responsible for dispersion, wall contact and reactive uptake.

For the dimensionless channel−1≤y≤1-1\leq y\leq 1, the three mean-centred profiles are:
- (F1)

Couette flow.The standard one-moving-wall Couette profile isu~(C)​(y)=1+y2,⟨u~(C)⟩y=12.\widetilde{u}^{(\mathrm{C})}(y)=\frac{1+y}{2},\qquad\left\langle\widetilde{u}^{(\mathrm{C})}\right\rangle_{y}=\frac{1}{2}.

Hence, the mean-deviated Couette profile isu(C)​(y)=1+y2−12=y2,−1≤y≤1.u^{(\mathrm{C})}(y)=\frac{1+y}{2}-\frac{1}{2}=\frac{y}{2},\qquad-1\leq y\leq 1.(10)
- (F2)

Poiseuille flow.The standard pressure-driven parabolic profile isu~(Po)​(y)=12​(1−y2),⟨u~(Po)⟩y=13.\widetilde{u}^{(\mathrm{Po})}(y)=\frac{1}{2}(1-y^{2}),\qquad\left\langle\widetilde{u}^{(\mathrm{Po})}\right\rangle_{y}=\frac{1}{3}.

Therefore, the mean-deviated Poiseuille profile isu(Po)​(y)=12​(1−y2)−13,−1≤y≤1.u^{(\mathrm{Po})}(y)=\frac{1}{2}(1-y^{2})-\frac{1}{3},\qquad-1\leq y\leq 1.(11)
- (F3)

Couette–Poiseuille flow.The combined uncentred profile isu~(CP)​(y)=1+y2+12​(1−y2),⟨u~(CP)⟩y=56.\widetilde{u}^{(\mathrm{CP})}(y)=\frac{1+y}{2}+\frac{1}{2}(1-y^{2}),\qquad\left\langle\widetilde{u}^{(\mathrm{CP})}\right\rangle_{y}=\frac{5}{6}.

Thus, the mean-deviated Couette–Poiseuille profile isu(CP)​(y)=1+y2+12​(1−y2)−56,−1≤y≤1.u^{(\mathrm{CP})}(y)=\frac{1+y}{2}+\frac{1}{2}(1-y^{2})-\frac{5}{6},\qquad-1\leq y\leq 1.(12)

Equivalently,u(CP)​(y)=u(C)​(y)+u(Po)​(y).u^{(\mathrm{CP})}(y)=u^{(\mathrm{C})}(y)+u^{(\mathrm{Po})}(y).

The Couette–Poiseuille configuration is a vital model for investigating transport in which pressure-driven and boundary-driven shear flows interact, a scenario common in complex hydrodynamics and microfluidic applicationsPaul and Mazumder (2008); Barik and Dalal (2019); Poddaret al.(2023).

Consequently, for each shear-flow cases∈𝒮s\in\mathcal{S}and source configurationq∈𝒬:={L,P}q\in\mathcal{Q}:=\{\mathrm{L},\mathrm{P}\}, the concentration fieldC(s,q)​(x,y,t)C^{(s,q)}(x,y,t)satisfies∂C(s,q)∂t+Pe​u(s)​(y)​∂C(s,q)∂x=∂2C(s,q)∂x2+∂2C(s,q)∂y2,x∈ℝ,−1<y<1,t>0.\frac{\partial C^{(s,q)}}{\partial t}+\mathrm{Pe}\,u^{(s)}(y)\frac{\partial C^{(s,q)}}{\partial x}=\frac{\partial^{2}C^{(s,q)}}{\partial x^{2}}+\frac{\partial^{2}C^{(s,q)}}{\partial y^{2}},\qquad x\in\mathbb{R},\quad-1<y<1,\quad t>0.(13)

## 2.6Axial boundary modelling on a finite window

For the PINN and finite-difference computations, the infinite streamwise direction is truncated to a finite intervalx∈[x0,x1],x0=−Lx2,x1=Lx2.x\in[x_{0},x_{1}],\qquad x_{0}=-\frac{L_{x}}{2},\quad x_{1}=\frac{L_{x}}{2}.

The computations are performed over the dimensionless time interval0≤t≤T0\leq t\leq T, whereTTdenotes the final observation time. The computational lengthLxL_{x}is chosen sufficiently large so that the localised solute cloud remains away from the artificial axial boundaries over the time interval considered. Since the initial release is localised near the interior of the domain, we impose homogeneous zero-gradient conditions at the two axial boundaries,∂C∂x​(−Lx2,y,t)=0,∂C∂x​(Lx2,y,t)=0,−1≤y≤1,t>0.\frac{\partial C}{\partial x}\left(-\frac{L_{x}}{2},y,t\right)=0,\qquad\frac{\partial C}{\partial x}\left(\frac{L_{x}}{2},y,t\right)=0,\qquad-1\leq y\leq 1,\quad t>0.(14)

These conditions close the finite computational problem without imposing artificial concentration loss through the streamwise boundaries. The same axial boundary treatment is used in the PINN loss and in the finite-difference benchmark.

## 3Methodology

## 3.1Neural-network approximation as a function-space representation

For each shear-flow cases∈𝒮:={C,Po,CP}s\in\mathcal{S}:=\{\mathrm{C},\mathrm{Po},\mathrm{CP}\}and each source configurationq∈𝒬:={L,P}q\in\mathcal{Q}:=\{\mathrm{L},\mathrm{P}\}, the concentration fieldC(s,q):(x,y,t)↦C(s,q)​(x,y,t)C^{(s,q)}:(x,y,t)\mapsto C^{(s,q)}(x,y,t)

is approximated by a feed-forward neural networkC(s,q)​(x,y,t)≈Cθ(s,q)​(x,y,t):=𝒩θ(s,q)​(x,y,t),C^{(s,q)}(x,y,t)\approx C_{\theta}^{(s,q)}(x,y,t):=\mathcal{N}_{\theta}^{(s,q)}(x,y,t),

whereθ\thetadenotes the trainable weights and biases. Heressidentifies the imposed shear flow, whileqqidentifies the initial source configuration. The neural network may be viewed as a finite-dimensional nonlinear approximation space; training selects a member of this function class that satisfies the governing convection–diffusion equation, the prescribed initial source and the boundary constraints in a least-squares residual sense.

The input layer receives the space–time variables(x,y,t)(x,y,t), and the output layer returns the scalar concentration approximationCθ(s,q)​(x,y,t)C_{\theta}^{(s,q)}(x,y,t). In the computations reported here, we use a fully connected network with four hidden layers, each containing6464neurons withtanh\tanhactivation. The choice of a smooth activation function is important because the residual of the convection–diffusion equation involves first- and second-order derivatives ofCθ(s,q)C_{\theta}^{(s,q)}with respect toxx,yyandtt. These derivatives are evaluated by automatic differentiation.

The overall PINN workflow is summarised in figure1. The schematic shows how the space–time inputs are mapped to the concentration prediction, how automatic differentiation is used to construct the PDE and boundary residuals, and how these residuals are combined into the composite training objective.(a)Physics-informed workflow and composite loss construction.(b)Detailed fully connected neural-network architecture.(c)Compact layer-wise representation of the PINN architecture.Figure 1:Schematic of the physics-informed neural-network framework.

## 3.2Physics-informed residual

For a prescribed shear profileu(s)​(y)u^{(s)}(y), the dimensionless convection–diffusion equation is enforced through the residualℛθ(s,q)​(x,y,t)=∂Cθ(s,q)∂t+Pe​u(s)​(y)​∂Cθ(s,q)∂x−∂2Cθ(s,q)∂x2−∂2Cθ(s,q)∂y2.\mathcal{R}_{\theta}^{(s,q)}(x,y,t)=\frac{\partial C_{\theta}^{(s,q)}}{\partial t}+\mathrm{Pe}\,u^{(s)}(y)\frac{\partial C_{\theta}^{(s,q)}}{\partial x}-\frac{\partial^{2}C_{\theta}^{(s,q)}}{\partial x^{2}}-\frac{\partial^{2}C_{\theta}^{(s,q)}}{\partial y^{2}}.(15)

The exact solution satisfiesℛθ(s,q)=0\mathcal{R}_{\theta}^{(s,q)}=0throughout the interior of the space–time domain. Thus, the PDE loss is defined asℒPDE(s,q)=1Nf​∑j=1Nf|ℛθ(s,q)​(xfj,yfj,tfj)|2,\mathcal{L}_{\mathrm{PDE}}^{(s,q)}=\frac{1}{N_{f}}\sum_{j=1}^{N_{f}}\left|\mathcal{R}_{\theta}^{(s,q)}\left(x_{f}^{j},y_{f}^{j},t_{f}^{j}\right)\right|^{2},(16)

where{(xfj,yfj,tfj)}j=1Nf\{(x_{f}^{j},y_{f}^{j},t_{f}^{j})\}_{j=1}^{N_{f}}are interior collocation points sampled from(x,y,t)∈(x0,x1)×(−1,1)×(0,T).(x,y,t)\in(x_{0},x_{1})\times(-1,1)\times(0,T).

This formulation, in which the governing physical laws serve as soft penalty constraints during network optimisation, provides the mathematical foundation of the PINN frameworkRaissiet al.(2019); He and Tartakovsky (2021).

## 3.3Initial-condition loss

For each shear-flow cases∈𝒮:={C,Po,CP}s\in\mathcal{S}:=\{\mathrm{C},\mathrm{Po},\mathrm{CP}\}and source configurationq∈𝒬:={L,P}q\in\mathcal{Q}:=\{\mathrm{L},\mathrm{P}\}, the initial concentration is prescribed asC​(x,y,0)=C0(q)​(x,y).C(x,y,0)=C_{0}^{(q)}(x,y).

Here, the superscriptssidentifies the imposed shear flow, whileqqidentifies the initial source type. The two source configurations are defined in equations (7) and (8). The sourceC0(L)C_{0}^{(\mathrm{L})}is a line-like Gaussian releaseTenget al.(2023), localised in the streamwise direction and uniform across the channel height. The sourceC0(P)C_{0}^{(\mathrm{P})}is a point-like Gaussian release, localised in both the streamwise and wall-normal directions. Thus, the line-like source isolates shear-driven longitudinal spreading, whereas the point-like source also probes transverse diffusion and wall contact.

The corresponding initial-condition loss isℒIC(s,q)=1N0​∑j=1N0|Cθ(s,q)​(x0j,y0j,0)−C0(q)​(x0j,y0j)|2,\mathcal{L}_{\mathrm{IC}}^{(s,q)}=\frac{1}{N_{0}}\sum_{j=1}^{N_{0}}\left|C_{\theta}^{(s,q)}(x_{0}^{j},y_{0}^{j},0)-C_{0}^{(q)}(x_{0}^{j},y_{0}^{j})\right|^{2},(17)

where{(x0j,y0j)}j=1N0\{(x_{0}^{j},y_{0}^{j})\}_{j=1}^{N_{0}}are sampled over the computational domain att=0t=0.

A true point-source release would formally be represented by a Dirac delta distribution. However, the Dirac delta is not a classical continuous function and is therefore incompatible with a pointwise mean-square initial-condition loss in the standard PINN setting. Since the present network represents a smooth trial functionCθ(s,q)C_{\theta}^{(s,q)}, imposing a singular distribution directly through pointwise residual minimisation is not well posed. The Gaussian sourceC0(P)C_{0}^{(\mathrm{P})}may instead be interpreted as a smooth mollified approximation to a point release, whileC0(L)C_{0}^{(\mathrm{L})}represents the corresponding line-release configuration. Future extensions may incorporate singular source data more directly using weak-form PINNs, Green ’s-function-based representations, adaptive mollification, or distributional residual formulations. Resolving these highly localised initial distributions is critical, as the initial transient stage of dispersion is highly sensitive to the source configuration before approaching the asymptotic Gaussian regimeJianget al.(2022); Rawdenet al.(2026).

## 3.4Boundary-condition losses

The axial boundaries of the truncated computational domain are assigned homogeneous zero-gradient conditions. The corresponding axial boundary loss isℒx​B(s,q)=1Nx​∑j=1Nx[|∂Cθ(s,q)∂x​(x0,yxj,txj)|2+|∂Cθ(s,q)∂x​(x1,yxj,txj)|2],\mathcal{L}_{x\mathrm{B}}^{(s,q)}=\frac{1}{N_{x}}\sum_{j=1}^{N_{x}}\left[\left|\frac{\partial C_{\theta}^{(s,q)}}{\partial x}(x_{0},y_{x}^{j},t_{x}^{j})\right|^{2}+\left|\frac{\partial C_{\theta}^{(s,q)}}{\partial x}(x_{1},y_{x}^{j},t_{x}^{j})\right|^{2}\right],(18)

where{(yxj,txj)}j=1Nx\{(y_{x}^{j},t_{x}^{j})\}_{j=1}^{N_{x}}are sampled on the two axial boundaries.

At the reactive walls, the Robin boundary conditions are enforced through∂C∂y−β2​C=0at​y=−1,−∂C∂y−β1​C=0at​y=1.\frac{\partial C}{\partial y}-\beta_{2}C=0\quad\text{at }y=-1,\qquad-\frac{\partial C}{\partial y}-\beta_{1}C=0\quad\text{at }y=1.

Equivalently, the wall residuals areℛ−,θ(s,q)=∂Cθ(s,q)∂y−β2​Cθ(s,q)at​y=−1,\mathcal{R}_{-,\theta}^{(s,q)}=\frac{\partial C_{\theta}^{(s,q)}}{\partial y}-\beta_{2}C_{\theta}^{(s,q)}\quad\text{at }y=-1,(19)

andℛ+,θ(s,q)=−∂Cθ(s,q)∂y−β1​Cθ(s,q)at​y=1.\mathcal{R}_{+,\theta}^{(s,q)}=-\frac{\partial C_{\theta}^{(s,q)}}{\partial y}-\beta_{1}C_{\theta}^{(s,q)}\quad\text{at }y=1.(20)

The Robin wall loss is thereforeℒy​B(s,q)=1Ny​∑j=1Ny|ℛ−,θ(s,q)​(x−j,−1,t−j)|2+1Ny​∑j=1Ny|ℛ+,θ(s,q)​(x+j,1,t+j)|2.\mathcal{L}_{y\mathrm{B}}^{(s,q)}=\frac{1}{N_{y}}\sum_{j=1}^{N_{y}}\left|\mathcal{R}_{-,\theta}^{(s,q)}(x_{-}^{j},-1,t_{-}^{j})\right|^{2}+\frac{1}{N_{y}}\sum_{j=1}^{N_{y}}\left|\mathcal{R}_{+,\theta}^{(s,q)}(x_{+}^{j},1,t_{+}^{j})\right|^{2}.(21)

The wall loss controls the reactive solute exchange at the plates, while the axial loss closes the finite computational domain without imposing artificial concentration loss across the streamwise boundaries.

## 3.5Composite training objective

The trainable parametersθ\thetaare obtained by minimising the composite physics-informed lossℒtot(s,q)​(θ)=ℒPDE(s,q)+λIC​ℒIC(s,q)+λB​(ℒx​B(s,q)+ℒy​B(s,q)).\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)=\mathcal{L}_{\mathrm{PDE}}^{(s,q)}+\lambda_{\mathrm{IC}}\mathcal{L}_{\mathrm{IC}}^{(s,q)}+\lambda_{\mathrm{B}}\left(\mathcal{L}_{x\mathrm{B}}^{(s,q)}+\mathcal{L}_{y\mathrm{B}}^{(s,q)}\right).(22)

HereλIC\lambda_{\mathrm{IC}}andλB\lambda_{\mathrm{B}}are positive weights that balance the initial-condition and boundary constraints relative to the interior PDE residual. In the computations reported here, these constraints are weighted more strongly to ensure accurate imposition of the localised source, the axial zero-gradient condition, and the reactive-wall conditions.

The minimisation problem is thereforeθ⋆(s,q)=arg​minθ⁡ℒtot(s,q)​(θ),s∈𝒮,q∈𝒬.\theta_{\star}^{(s,q)}=\operatorname*{arg\,min}_{\theta}\,\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta),\qquad s\in\mathcal{S},\quad q\in\mathcal{Q}.(23)

Once trained, the PINN solution is evaluated asCPINN(s,q)​(x,y,t)=Cθ⋆(s,q)​(x,y,t).C_{\mathrm{PINN}}^{(s,q)}(x,y,t)=C_{\theta_{\star}}^{(s,q)}(x,y,t).

The same network architecture, sampling strategy and loss structure are used across the shear-flow cases and source configurations, so that differences in the predicted transport can be attributed tou(s)​(y)u^{(s)}(y),C0(q)C_{0}^{(q)}, and the imposed wall reactivity.

## 3.6Collocation strategy and training

The collocation points are sampled separately for the interior PDE residual, the initial condition, the axial boundary condition and the Robin wall conditions. This separation is essential because the initial and boundary constraints lie on lower-dimensional subsets of the space–time domain and would otherwise be underrepresented by purely uniform sampling in the full domain. Thus, at each training epoch, independent point sets are drawn from the interior domain, the initial plane, the two axial boundaries and the two reactive walls.

The trainable parameters are optimised using the Adam algorithm with an exponentially decaying learning rate. At each epoch, the loss components are evaluated over the corresponding collocation sets, and the network parameters are updated to reduce the composite physics-informed objective. This sampling strategy ensures that the PDE residual, the selected initial source configuration, the artificial axial boundaries, and the reactive wall conditions all contribute explicitly to the training process.

All spatial and temporal derivatives appearing in (15), (19) and (20) are computed by automatic differentiation with respect to the neural-network representationCθ(s,q)​(x,y,t)C_{\theta}^{(s,q)}(x,y,t). This avoids finite-difference approximation of derivatives inside the PINN loss and enables mesh-free enforcement of the dimensionless convection–diffusion equation and Robin wall constraints. By leveraging exact automatic differentiation rather than discrete approximations, the network avoids the classical truncation errors inherent in grid-based derivative calculations, which is a primary advantage of deep learning solvers in fluid mechanicsRaissiet al.(2019); Zouet al.(2025).

## 3.7Computational setup

All computations are performed on the finite domainx∈[−5,5],y∈[−1,1],0≤t≤1,x\in[-5,5],\qquad y\in[-1,1],\qquad 0\leq t\leq 1,

withPe=10\mathrm{Pe}=10. The PINN uses the network architecture described above, namely four hidden layers with6464neurons in each layer andtanh\tanhactivation. For each training epoch, collocation points are sampled separately from the interior domain, the initial plane, the two axial boundaries and the two reactive walls. Unless otherwise stated, the numbers of points used in the PINN loss areNf=8000,N0=1000,Nx​B=800,Ny​B=400.N_{f}=8000,\qquad N_{0}=1000,\qquad N_{x\mathrm{B}}=800,\qquad N_{y\mathrm{B}}=400.

HereNfN_{f}denotes interior residual points,N0N_{0}denotes initial-condition points,Nx​BN_{x\mathrm{B}}denotes axial-boundary points, andNy​BN_{y\mathrm{B}}denotes points on each reactive wall. A sufficiently large finite interval is used to truncate the infinite longitudinal domain. Because the concentration may stay non-zero at the artificial longitudinal boundaries throughout the simulation, homogeneous Neumann boundary conditions are required there. The Neumann condition lessens the impact of domain truncation on the solution of interest by avoiding unnecessarily restricting the concentration field, in contrast to homogeneous Dirichlet conditions. The axial-boundary collocation points are used to impose the homogeneous zero-gradient condition∂Cθ/∂x=0\partial C_{\theta}/\partial x=0atx=−5x=-5andx=5x=5.

The trainable parameters are optimised using the Adam algorithm with an initial learning rate10−310^{-3}. The learning rate is multiplied by a factor0.950.95every500500epochs, allowing rapid initial optimisation followed by progressively smaller parameter updates. The composite loss is evaluated using stronger weights on the initial and boundary constraints,λIC=30,λB=30,\lambda_{\mathrm{IC}}=30,\lambda_{\mathrm{B}}=30,so that the localised initial release and the boundary conditions remain accurately imposed during training. Most reported validation cases are trained for50005000epochs, while selected runs are continued up to2000020000epochs to monitor longer optimisation behaviour and to generate the epoch-wise loss values reported later.

For reproducibility, the ADI finite-difference benchmark uses the same physical domain asNx=101,Ny=51,Δ​t=10−4,T=1.N_{x}=101,\qquad N_{y}=51,\qquad\Delta t=10^{-4},\qquad T=1.

The same initial source profiles, wall-reaction coefficients and shear-flow configurations are used in the PINN and ADI computations. This common setup ensures that the reported PINN–ADI discrepancies measure the approximation accuracy of the learned solution rather than differences in the underlying physical problem.

## 3.8Finite-difference benchmark

To assess the accuracy of the PINN predictions, we compute reference solutions using a finite-difference alternating-direction implicit (ADI) scheme on the same truncated domain. Originally developed for parabolic partial differential equationsPeaceman and Rachford (1955); Douglas (1955), the ADI method provides an unconditionally stable and computationally efficient framework for multi-dimensional transport. In our implementation, the dimensionless convection–diffusion equation is advanced in time by an alternating-direction splitting of the diffusive terms, with the advective contribution evaluated on the same Cartesian grid. The initial source configuration, axial zero-gradient condition and Robin wall conditions are imposed consistently with the PINN formulation.

The ADI solution is used only as a benchmark for validation. Comparisons are performed using full concentration contours and cross-sectionally averaged concentration profiles. The latter are defined by⟨C⟩​(x,t)=⟨C⟩y=12​∫−11C​(x,y,t)​dy.\langle C\rangle(x,t)=\langle C\rangle_{y}=\frac{1}{2}\int_{-1}^{1}C(x,y,t)\mathrm{d}y.(24)

For visualisation, the averaged profiles are plotted in the centroid-shifted coordinatex−xg​(t)x-x_{g}(t), wherexg​(t)=∫x0x1x​⟨C⟩​(x,t)​dx∫x0x1⟨C⟩​(x,t)​dx.x_{g}(t)=\frac{\displaystyle\int_{x_{0}}^{x_{1}}x\,\langle C\rangle(x,t)\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}\langle C\rangle(x,t)\mathrm{d}x}.(25)

The agreement between PINN and ADI solutions is quantified usingL2L_{2}-type errors at selected times, providing a direct validation of the learned solution against a classical grid-based method.

In addition to concentration-based validation, we also use the ADI benchmark to validate the integrated wall-removal diagnostics. LetCADI(s,q)​(x,y,t)C_{\mathrm{ADI}}^{(s,q)}(x,y,t)

denote the ADI solution corresponding to the same shear profile, source configuration and reactive-wall parameters as the PINN solution. The ADI wall uptake fluxes are evaluated analogously asJ+,ADI(s,q)​(x,t)=β1​CADI(s,q)​(x,1,t),J−,ADI(s,q)​(x,t)=β2​CADI(s,q)​(x,−1,t).J_{+,\mathrm{ADI}}^{(s,q)}(x,t)=\beta_{1}C_{\mathrm{ADI}}^{(s,q)}(x,1,t),\qquad J_{-,\mathrm{ADI}}^{(s,q)}(x,t)=\beta_{2}C_{\mathrm{ADI}}^{(s,q)}(x,-1,t).

The corresponding integrated wall uptake rates are𝒥+,ADI(s,q)​(t)=∫x0x1J+,ADI(s,q)​(x,t)​dx,𝒥−,ADI(s,q)​(t)=∫x0x1J−,ADI(s,q)​(x,t)​dx.\mathcal{J}_{+,\mathrm{ADI}}^{(s,q)}(t)=\int_{x_{0}}^{x_{1}}J_{+,\mathrm{ADI}}^{(s,q)}(x,t)\mathrm{d}x,\qquad\mathcal{J}_{-,\mathrm{ADI}}^{(s,q)}(t)=\int_{x_{0}}^{x_{1}}J_{-,\mathrm{ADI}}^{(s,q)}(x,t)\mathrm{d}x.

The cumulative wall uptakes are then computed as𝒰+,ADI(s,q)​(t)=∫0t𝒥+,ADI(s,q)​(τ)​𝑑τ,𝒰−,ADI(s,q)​(t)=∫0t𝒥−,ADI(s,q)​(τ)​𝑑τ,\mathcal{U}_{+,\mathrm{ADI}}^{(s,q)}(t)=\int_{0}^{t}\mathcal{J}_{+,\mathrm{ADI}}^{(s,q)}(\tau)\,d\tau,\qquad\mathcal{U}_{-,\mathrm{ADI}}^{(s,q)}(t)=\int_{0}^{t}\mathcal{J}_{-,\mathrm{ADI}}^{(s,q)}(\tau)\,d\tau,

whereτ\tauis a dummy time-integration variable. Thus,𝒰tot,ADI(s,q)​(t)=𝒰+,ADI(s,q)​(t)+𝒰−,ADI(s,q)​(t).\mathcal{U}_{\mathrm{tot},\mathrm{ADI}}^{(s,q)}(t)=\mathcal{U}_{+,\mathrm{ADI}}^{(s,q)}(t)+\mathcal{U}_{-,\mathrm{ADI}}^{(s,q)}(t).

The corresponding PINN quantity is denoted by𝒰tot,PINN(s,q)​(t).\mathcal{U}_{\mathrm{tot},\mathrm{PINN}}^{(s,q)}(t).

The final-time relative error in cumulative wall uptake is defined asE𝒰(s,q)=|𝒰tot,PINN(s,q)​(T)−𝒰tot,ADI(s,q)​(T)||𝒰tot,ADI(s,q)​(T)|×100.E_{\mathcal{U}}^{(s,q)}=\frac{\left|\mathcal{U}_{\mathrm{tot},\mathrm{PINN}}^{(s,q)}(T)-\mathcal{U}_{\mathrm{tot},\mathrm{ADI}}^{(s,q)}(T)\right|}{\left|\mathcal{U}_{\mathrm{tot},\mathrm{ADI}}^{(s,q)}(T)\right|}\times 100.(26)

This metric directly assesses whether the learned concentration field reproduces the cumulative wall-removal dynamics obtained from the ADI benchmark.

## 3.9Physical interpretation of the learned solution

The trained network provides a differentiable surrogate for the concentration field,CPINN(s,q)​(x,y,t)=Cθ⋆(s,q)​(x,y,t),s∈𝒮,q∈𝒬.C_{\mathrm{PINN}}^{(s,q)}(x,y,t)=C_{\theta_{\star}}^{(s,q)}(x,y,t),\qquad s\in\mathcal{S},\quad q\in\mathcal{Q}.

Beyond pointwise concentration values, this representation allows direct evaluation of physically relevant wall-uptake quantities. In particular, the local dimensionless uptake fluxes at the upper and lower walls are computed asJ+(s,q)​(x,t)=β1​Cθ⋆(s,q)​(x,1,t),J−(s,q)​(x,t)=β2​Cθ⋆(s,q)​(x,−1,t).J_{+}^{(s,q)}(x,t)=\beta_{1}C_{\theta_{\star}}^{(s,q)}(x,1,t),\qquad J_{-}^{(s,q)}(x,t)=\beta_{2}C_{\theta_{\star}}^{(s,q)}(x,-1,t).(27)

HereJ+(s,q)J_{+}^{(s,q)}andJ−(s,q)J_{-}^{(s,q)}denote the uptake fluxes at the upper and lower plates, respectively. The corresponding integrated wall uptake rates are𝒥+(s,q)​(t)=∫x0x1J+(s,q)​(x,t)​dx,𝒥−(s,q)​(t)=∫x0x1J−(s,q)​(x,t)​dx,\mathcal{J}_{+}^{(s,q)}(t)=\int_{x_{0}}^{x_{1}}J_{+}^{(s,q)}(x,t)\mathrm{d}x,\qquad\mathcal{J}_{-}^{(s,q)}(t)=\int_{x_{0}}^{x_{1}}J_{-}^{(s,q)}(x,t)\mathrm{d}x,(28)

and the total integrated uptake rate is𝒥tot(s,q)​(t)=𝒥+(s,q)​(t)+𝒥−(s,q)​(t).\mathcal{J}_{\mathrm{tot}}^{(s,q)}(t)=\mathcal{J}_{+}^{(s,q)}(t)+\mathcal{J}_{-}^{(s,q)}(t).(29)

These quantities measure the instantaneous rate at which solute is removed by the reactive plates.

The cumulative wall uptakes are then defined by𝒰+(s,q)​(t)=∫0t𝒥+(s,q)​(τ)​𝑑τ,𝒰−(s,q)​(t)=∫0t𝒥−(s,q)​(τ)​𝑑τ,\mathcal{U}_{+}^{(s,q)}(t)=\int_{0}^{t}\mathcal{J}_{+}^{(s,q)}(\tau)\,d\tau,\qquad\mathcal{U}_{-}^{(s,q)}(t)=\int_{0}^{t}\mathcal{J}_{-}^{(s,q)}(\tau)\,d\tau,(30)

whereτ\tauis a dummy time-integration variable. The total cumulative wall uptake is𝒰tot(s,q)​(t)=𝒰+(s,q)​(t)+𝒰−(s,q)​(t).\mathcal{U}_{\mathrm{tot}}^{(s,q)}(t)=\mathcal{U}_{+}^{(s,q)}(t)+\mathcal{U}_{-}^{(s,q)}(t).(31)

Thus,𝒥±(s,q)​(t)\mathcal{J}_{\pm}^{(s,q)}(t)describe instantaneous wall-removal rates, whereas𝒰±(s,q)​(t)\mathcal{U}_{\pm}^{(s,q)}(t)describe the accumulated amount of solute removed by each wall up to timett.

To quantify the final partition of removal between the two plates, we define the lower-wall cumulative uptake fractionΦ−(s,q)​(T)=𝒰−(s,q)​(T)𝒰tot(s,q)​(T).\Phi_{-}^{(s,q)}(T)=\frac{\mathcal{U}_{-}^{(s,q)}(T)}{\mathcal{U}_{\mathrm{tot}}^{(s,q)}(T)}.(32)

For the non-reactive case,𝒰tot(s,q)​(T)=0\mathcal{U}_{\mathrm{tot}}^{(s,q)}(T)=0, so this fraction is not interpreted and is used only for reactive configurations. ValuesΦ−(s,q)​(T)≈1/2\Phi_{-}^{(s,q)}(T)\approx 1/2indicate balanced upper- and lower-wall uptake, whereasΦ−(s,q)​(T)>1/2\Phi_{-}^{(s,q)}(T)>1/2andΦ−(s,q)​(T)<1/2\Phi_{-}^{(s,q)}(T)<1/2indicate lower- and upper-wall-dominated removal, respectively.

We also introduce a cumulative wall-dominance indexDw(s,q)​(t)=𝒰−(s,q)​(t)−𝒰+(s,q)​(t)𝒰tot(s,q)​(t).D_{w}^{(s,q)}(t)=\frac{\mathcal{U}_{-}^{(s,q)}(t)-\mathcal{U}_{+}^{(s,q)}(t)}{\mathcal{U}_{\mathrm{tot}}^{(s,q)}(t)}.(33)

This index is interpreted for times at which𝒰tot(s,q)​(t)>0\mathcal{U}_{\mathrm{tot}}^{(s,q)}(t)>0. ThusDw(s,q)​(t)=0D_{w}^{(s,q)}(t)=0corresponds to balanced wall removal,Dw(s,q)​(t)>0D_{w}^{(s,q)}(t)>0indicates lower-wall-dominated uptake, andDw(s,q)​(t)<0D_{w}^{(s,q)}(t)<0indicates upper-wall-dominated uptake. This bounded diagnostic provides a compact measure of the time-dependent asymmetry in cumulative wall removal.

To characterise the streamwise organisation of wall uptake, we define flux-weighted uptake centroidsxJ+(s,q)​(t)=∫x0x1x​J+(s,q)​(x,t)​dx∫x0x1J+(s,q)​(x,t)​dx,xJ−(s,q)​(t)=∫x0x1x​J−(s,q)​(x,t)​dx∫x0x1J−(s,q)​(x,t)​dx.x_{J_{+}}^{(s,q)}(t)=\frac{\displaystyle\int_{x_{0}}^{x_{1}}x\,J_{+}^{(s,q)}(x,t)\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}J_{+}^{(s,q)}(x,t)\mathrm{d}x},\qquad x_{J_{-}}^{(s,q)}(t)=\frac{\displaystyle\int_{x_{0}}^{x_{1}}x\,J_{-}^{(s,q)}(x,t)\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}J_{-}^{(s,q)}(x,t)\mathrm{d}x}.(34)

These centroids are evaluated only when the corresponding integrated wall uptake rate is non-zero. The corresponding flux-weighted spreads areσJ+(s,q)​(t)=[∫x0x1(x−xJ+(s,q)​(t))2​J+(s,q)​(x,t)​dx∫x0x1J+(s,q)​(x,t)​dx]1/2,\sigma_{J_{+}}^{(s,q)}(t)=\left[\frac{\displaystyle\int_{x_{0}}^{x_{1}}\left(x-x_{J_{+}}^{(s,q)}(t)\right)^{2}J_{+}^{(s,q)}(x,t)\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}J_{+}^{(s,q)}(x,t)\mathrm{d}x}\right]^{1/2},(35)

andσJ−(s,q)​(t)=[∫x0x1(x−xJ−(s,q)​(t))2​J−(s,q)​(x,t)​dx∫x0x1J−(s,q)​(x,t)​dx]1/2.\sigma_{J_{-}}^{(s,q)}(t)=\left[\frac{\displaystyle\int_{x_{0}}^{x_{1}}\left(x-x_{J_{-}}^{(s,q)}(t)\right)^{2}J_{-}^{(s,q)}(x,t)\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}J_{-}^{(s,q)}(x,t)\mathrm{d}x}\right]^{1/2}.(36)

The quantitiesxJ±(s,q)​(t)x_{J_{\pm}}^{(s,q)}(t)andσJ±(s,q)​(t)\sigma_{J_{\pm}}^{(s,q)}(t)identify where along the channel the wall uptake is concentrated and how broadly the wall-flux distribution is spread. They therefore reveal the spatial organisation of wall removal that may not be visible from total uptake alone.

In the reactive-wall analysis, we focus on three representative configurations,(β1,β2)=(1,1),(β1,β2)=(0.2,2),(β1,β2)=(2,0.2).(\beta_{1},\beta_{2})=(1,1),\qquad(\beta_{1},\beta_{2})=(0.2,2),\qquad(\beta_{1},\beta_{2})=(2,0.2).

The first corresponds to symmetric wall uptake, while the latter two represent asymmetric absorption with dominant lower- and upper-wall reactivity, respectively. The non-reactive case(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0)is used as a validation baseline.

The same wall-uptake diagnostics are also evaluated from the ADI finite-difference benchmark solution to assess the accuracy of the PINN-predicted cumulative wall removal.

## 4Results and discussion

The results are organised to separate solution validation from physical interpretation. We first assess the PINN approximation using concentration-field errors, cross-sectionally averaged concentration profiles and epoch-wise training histories. We then validate the derived transport quantities, including the apparent axial dispersion coefficient, the total surviving solute mass, the axial variance, and the cumulative wall uptake. After these validation steps, the trained PINN solution is used to examine wall-resolved reactive dispersion through uptake rates, cumulative removal, wall-selective asymmetry and the streamwise organisation of local wall fluxes. The emphasis is therefore not only on reconstructingC​(x,y,t)C(x,y,t), but also on extracting interpretable diagnostics that describe how shear-driven dispersion and wall absorption jointly control solute removal.

## 4.1Concentration-field validation across source and flow configurations

To assess the local spatial accuracy of the learned concentration field, we use the blockwise absolute errorBerr​(x,y,t)=|CPINN​(x,y,t)−CADI​(x,y,t)|.B_{\mathrm{err}}(x,y,t)=\left|C_{\mathrm{PINN}}(x,y,t)-C_{\mathrm{ADI}}(x,y,t)\right|.(37)

HereCPINN​(x,y,t)C_{\mathrm{PINN}}(x,y,t)denotes the concentration field predicted by the trained physics-informed neural network, whileCADI​(x,y,t)C_{\mathrm{ADI}}(x,y,t)denotes the corresponding ADI finite-difference benchmark solution. The quantityBerr​(x,y,t)B_{\mathrm{err}}(x,y,t)therefore measures the local pointwise discrepancy between the PINN and ADI solutions at each selected space–time location.

We first use the non-reactive case,β1=β2=0\beta_{1}=\beta_{2}=0, as a baseline to assess the advection–diffusion component of the learned solution. This baseline isolates the PINN’s ability to reproduce shear-driven spreading before wall absorption is introduced. The two initial source configurations are the line-like Gaussian source (7) and the point-like Gaussian source (8). The line-like source is initially uniform across the channel height, and primarily tests shear-induced axial spreading, whereas the point-like source is localised in both the streamwise and wall-normal directions and therefore also tests transverse diffusion and near-wall concentration evolution.Table 1:L2L_{2}errors between PINN predictions and ADI finite-difference solutions at selected times for the three shear-flow configurations withPe=10\mathrm{Pe}=10andβ1=β2=0\beta_{1}=\beta_{2}=0. Results are reported for both line-like and point-like source configurations.Flow typeReaction rateSource typet=0.001t=0.001t=0.01t=0.01t=0.1t=0.1t=0.5t=0.5t=1t=1Poiseuilleβ1=β2=0\beta_{1}=\beta_{2}=0Line-like0.02404890.02414000.02518670.02695520.0267071Poiseuilleβ1=β2=0\beta_{1}=\beta_{2}=0Point-like0.01085510.01191650.01416330.01743120.0201506Couetteβ1=β2=0\beta_{1}=\beta_{2}=0Line-like0.00813050.00879780.01375220.03981620.0414874Couetteβ1=β2=0\beta_{1}=\beta_{2}=0Point-like0.01237100.01298260.01439720.02629300.0277750Couette–Poiseuilleβ1=β2=0\beta_{1}=\beta_{2}=0Line-like0.02018660.02061410.02953640.05442090.0720882Couette–Poiseuilleβ1=β2=0\beta_{1}=\beta_{2}=0Point-like0.01249940.01309100.01701860.01701860.0391011

The error values in table1provide a quantitative baseline validation across the three mean-centred shear profiles. The corresponding non-reactive blockwise-error plots for all source–flow combinations are reported in the supplementary material. This keeps the main manuscript focused on the reactive cases while retaining the complete concentration-field validation.

We next show representative reactive blockwise-error results in the main manuscript, since wall absorption is the central feature of the present study. The point-like source is used here because it is the source configuration used later for wall-resolved uptake diagnostics. The three cases shown in figures2–4span symmetric wall absorption, lower-wall-dominated absorption, upper-wall-dominated absorption, and the three canonical shear profiles.Figure 2:Blockwise absolute errorBerr=|CPINN−CADI|B_{\mathrm{err}}=|C_{\mathrm{PINN}}-C_{\mathrm{ADI}}|for the point-like source in Couette flow with symmetric wall absorption(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).Figure 3:Blockwise absolute errorBerr=|CPINN−CADI|B_{\mathrm{err}}=|C_{\mathrm{PINN}}-C_{\mathrm{ADI}}|for the point-like source in Poiseuille flow with lower-wall-dominated absorption(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).Figure 4:Blockwise absolute errorBerr=|CPINN−CADI|B_{\mathrm{err}}=|C_{\mathrm{PINN}}-C_{\mathrm{ADI}}|for the point-like source in Couette–Poiseuille flow with upper-wall-dominated absorption(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).

Figures2–4demonstrate that the learned concentration field remains close to the ADI benchmark after reactive wall absorption is introduced. These representative cases are deliberately selected to cover different shear structures and different transverse absorption biases. Thus, the validation is not restricted to the non-reactive limit, but directly supports the reactive wall-uptake analysis developed in the following subsections. The localised error structures are physically expected because the largest discrepancies occur where the concentration gradients are strongest, namely near the evolving plume front and near reactive boundaries. In these regions, advection, transverse diffusion and Robin wall uptake act simultaneously, making the local concentration field more demanding to approximate than in weak-gradient regions of the domain.

Additional blockwise-error results for the line-like reactive cases are provided in the supplementary material. These results complement the representative point-like reactive validation shown in the main manuscript while avoiding excessive repetition of similar contour plots.Table 2:PINN–ADI error metrics for the line-like source under different shear-flow configurations and wall-reaction coefficients. Results are reported at selected times forPe=10\mathrm{Pe}=10.Flow RegimeReaction ratet=0.001t=0.001t=0.01t=0.01t=0.1t=0.1t=0.5t=0.5t=1.0t=1.0Poiseuilleβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00170.00170.00520.01620.0212Couetteβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00670.00660.00880.01690.0161Couette–Poiseuilleβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00620.00610.01120.02090.0199Poiseuilleβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00380.00330.00400.00870.0070Poiseuilleβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00570.00520.00880.01270.0116Poiseuilleβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00730.00620.00660.01010.0120Couetteβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00330.00390.00870.00930.0060Couetteβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00770.00620.00780.01160.0117Couetteβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00680.00590.00820.01010.0095Couette–Poiseuilleβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00320.00240.00830.01200.0077Couette–Poiseuilleβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00550.00440.00740.01570.0097Couette–Poiseuilleβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00460.00540.01040.01710.0137Table 3:PINN–ADI error metrics for the point-like source under different shear-flow configurations and wall-reaction coefficients. Results are reported at selected times forPe=10\mathrm{Pe}=10.Flow RegimeReaction ratet=0.001t=0.001t=0.01t=0.01t=0.1t=0.1t=0.5t=0.5t=1.0t=1.0Poiseuilleβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00180.00280.00770.01460.0181Couetteβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00420.00550.01040.01680.0177Couette–Poiseuilleβ1=0,β2=0\beta_{1}=0,\ \beta_{2}=00.00420.00540.01060.01730.0147Poiseuilleβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00670.00680.00840.00770.0067Poiseuilleβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00380.00420.00750.00870.0076Poiseuilleβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00480.00450.00060.00840.0092Couetteβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00390.00350.00510.00750.0052Couetteβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00480.00500.00670.00690.0077Couetteβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00520.00490.00550.00920.0072Couette–Poiseuilleβ1=1,β2=1\beta_{1}=1,\ \beta_{2}=10.00400.00410.00760.01040.0071Couette–Poiseuilleβ1=2,β2=0.2\beta_{1}=2,\ \beta_{2}=0.20.00580.00570.00730.01200.0082Couette–Poiseuilleβ1=0.2,β2=2\beta_{1}=0.2,\ \beta_{2}=20.00560.00620.00950.01460.0104

Tables2and3extend the quantitative validation beyond the non-reactive baseline by including both source configurations and the selected symmetric and asymmetric wall-reaction cases. The errors remain small across the reported times, indicating that the trained PINN solutions remain close to the ADI benchmark after reactive wall absorption is introduced.

To further assess the accuracy of the learned streamwise transport, we also compare the cross-sectionally averaged concentration profiles. For each solution, the mean concentration is defined as⟨C⟩​(x,t)=12​∫−11C​(x,y,t)​dy.\langle C\rangle(x,t)=\frac{1}{2}\int_{-1}^{1}C(x,y,t)\mathrm{d}y.(38)

The corresponding mean-concentration error isE⟨C⟩​(x,t)=|⟨C⟩PINN​(x,t)−⟨C⟩ADI​(x,t)|.E_{\langle C\rangle}(x,t)=\left|\langle C\rangle_{\mathrm{PINN}}(x,t)-\langle C\rangle_{\mathrm{ADI}}(x,t)\right|.(39)

This diagnostic complements the blockwise two-dimensional error by showing whether the PINN accurately reproduces the streamwise solute distribution after averaging across the channel height.Figure 5:Cross-sectionally averaged concentration comparison and mean-concentration error for the point-like source in Couette flow with symmetric wall absorption(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1). The figure compares⟨C⟩PINN​(x,t)\langle C\rangle_{\mathrm{PINN}}(x,t)with⟨C⟩ADI​(x,t)\langle C\rangle_{\mathrm{ADI}}(x,t)and reports the corresponding errorE⟨C⟩​(x,t)E_{\langle C\rangle}(x,t).Figure 6:Cross-sectionally averaged concentration comparison and mean-concentration error for the point-like source in Poiseuille flow with lower-wall-dominated absorption(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2). The figure compares⟨C⟩PINN​(x,t)\langle C\rangle_{\mathrm{PINN}}(x,t)with⟨C⟩ADI​(x,t)\langle C\rangle_{\mathrm{ADI}}(x,t)and reports the corresponding errorE⟨C⟩​(x,t)E_{\langle C\rangle}(x,t).Figure 7:Cross-sectionally averaged concentration comparison and mean-concentration error for the point-like source in Couette–Poiseuille flow with upper-wall-dominated absorption(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2). The figure compares⟨C⟩PINN​(x,t)\langle C\rangle_{\mathrm{PINN}}(x,t)with⟨C⟩ADI​(x,t)\langle C\rangle_{\mathrm{ADI}}(x,t)and reports the corresponding errorE⟨C⟩​(x,t)E_{\langle C\rangle}(x,t).

Figures5–7show that the PINN also reproduces the cross-sectionally averaged streamwise concentration profiles for representative reactive cases. Thus, the validation includes both local two-dimensional concentration accuracy and averaged streamwise transport accuracy. Additional mean-concentration comparison figures for the line-like reactive cases are reported in the supplementary material. Because cross-sectional averaging removes local wall-normal fluctuations, agreement in⟨C⟩​(x,t)\langle C\rangle(x,t)confirms that the PINN captures the net streamwise redistribution of solute produced by the imposed shear flow and wall absorption.

## 4.2Training convergence of the PINN models

Before extracting wall-resolved reactive-dispersion diagnostics, we examine the training histories of the PINN models. This check is included to verify the numerical optimisation behaviour of the physics-informed objective, whereas the ADI comparisons provide solution-level validation. The monitored quantity is the composite lossℒtot(s,q)​(θ)\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)defined in (22). The selected cases are arranged according to source configuration, shear profile, wall reactivity and activation function, so that the convergence behaviour can be assessed without mixing physically different comparisons in the same panel.(a)s=Cs=\mathrm{C},(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).(b)s=Cs=\mathrm{C},(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).(c)s=CPs=\mathrm{CP},(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).(d)s=CPs=\mathrm{CP},(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).(e)s=Pos=\mathrm{Po},(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).(f)s=Pos=\mathrm{Po},(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).Figure 8:Training loss histories for the line-like sourceq=Lq=\mathrm{L}using the default activationϕ​(z)=tanh⁡z\phi(z)=\tanh z. The panels cover Couette, Poiseuille and Couette–Poiseuille flows under non-reactive, symmetric-reactive and asymmetric-reactive wall conditions. The decrease ofℒtot(s,q)​(θ)\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)indicates stable minimisation of the physics-informed objective for initially cross-sectionally distributed solute fields.

Figure8reports training histories for the line-like sourceq=Lq=\mathrm{L}. These cases test whether the PINN optimisation remains stable when the initial concentration is distributed across the channel height, and the wall-reactivity configuration is varied across non-reactive, symmetric and asymmetric regimes. It shows that the optimisation remains stable for the line-like source across different velocity profiles and reaction strengths. This is important because the line-like source interacts immediately with the full transverse structure of the velocity field and the reactive walls. The comparable decay ofℒtot(s,q)​(θ)\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)across these cases supports the robustness of the training procedure for distributed initial data.(a)ϕ​(z)=tanh⁡z\phi(z)=\tanh z,(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).(b)ϕ​(z)=tanh⁡z\phi(z)=\tanh z,(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).(c)ϕG​(z)=exp⁡(−z2)\phi_{G}(z)=\exp(-z^{2}),(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).Figure 9:Training loss histories for the point-like sourceq=Pq=\mathrm{P}in Poiseuille flow,s=Pos=\mathrm{Po}. Panels(a)(a)and(b)(b)use the default activationϕ​(z)=tanh⁡z\phi(z)=\tanh z, while panel(c)(c)uses the Gaussian activationϕG​(z)=exp⁡(−z2)\phi_{G}(z)=\exp(-z^{2}). The comparison between panels(a)(a)and(c)(c)isolates the effect of the activation function for the same non-reactive case, whereas panel(b)(b)shows the corresponding behaviour after symmetric wall absorption is introduced.

Figure9focuses on the point-like source in Poiseuille flow. This group is useful because it provides a direct activation comparison for the same non-reactive case and includes the corresponding symmetric-reactive case trained with the defaulttanh\tanhactivation. It separates the activation-sensitivity check from the broader flow–reaction comparisons. The point-like source is a stringent case because the initial solute field is localised in both the streamwise and transverse directions. The comparison shows that the defaulttanh\tanh-activated PINN gives stable convergence for both non-reactive and reactive Poiseuille cases, while the Gaussian-activation case provides an additional check that the observed training behaviour is not tied to a single activation choice.(a)q=Lq=\mathrm{L}and(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).(b)q=Pq=\mathrm{P}and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).Figure 10:Training-loss histories for asymmetric reactive cases in Couette–Poiseuille flow,s=CPs=\mathrm{CP}, using the default activationϕ​(z)=tanh⁡z\phi(z)=\tanh z. Panel(a)(a)corresponds to a line-like source with lower-wall-dominated absorption, while panel(b)(b)corresponds to a point-like source with upper-wall-dominated absorption. These two cases test whether the PINN training remains stable when mixed shear, source localisation, and wall-reactivity asymmetry act together.

Figure10reports two additional Couette–Poiseuille cases with asymmetric wall reactivity. These cases are retained in the main manuscript because they test the training behaviour under mixed shear and source-dependent reactive imbalance. This completes the convergence assessment by including two asymmetric reactive configurations in the Couette–Poiseuille profile. This flow contains both linear and parabolic shear contributions, and the asymmetric wall reactivity preferentially removes solute from one side of the channel. The observed decrease ofℒtot(s,q)​(θ)\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)therefore supports the stability of the optimisation procedure in cases where the concentration field is shaped simultaneously by mixed shear, wall-normal diffusion and selective wall absorption.

Entirely, figures8–10show that the PINN objective can be minimised reliably across the source configurations, canonical shear profiles, wall-reactivity regimes and activation functions used in the validation study. These training histories are not used as a substitute for ADI-based accuracy assessment; rather, they document the convergence behaviour of the optimisation process underlying the validated PINN solutions.Table 4:Epoch-wise values of the monitored composite lossℒtot(s,q)​(θ)\mathcal{L}_{\mathrm{tot}}^{(s,q)}(\theta)for Poiseuille-flow training cases under different wall-reaction coefficients.CaseEpoch 5000Epoch 10000Epoch 15000Epoch 20000Panel A: Configurationβ1=0,β2=0\beta_{1}=0,\beta_{2}=010.04052980.00384690.00860440.001656320.04142160.00396630.00857590.001703430.04813220.00620450.00850970.005200940.04251910.01623270.01639970.016218750.04271710.02085910.01994540.0211767Panel B: Configurationβ1=1,β2=1\beta_{1}=1,\beta_{2}=110.01584590.01026400.00332060.003762020.01317760.00937360.00405900.003348830.01615320.00945190.00630480.003962640.02543940.01451210.01272750.008691550.02286910.01249000.01186530.0070485Panel C: Configurationβ1=2,β2=0.2\beta_{1}=2,\beta_{2}=0.210.02606120.01179020.00728500.005674220.02337180.00954310.00652020.005193930.02989990.01317580.01081810.008788540.05303140.01893590.01608590.012715950.03439610.01719180.01418330.0115769Panel D: Configurationβ1=0.2,β2=2\beta_{1}=0.2,\beta_{2}=210.02648320.01770980.00737960.00727920.02288580.01586570.00540810.006209730.02938190.0135830.00413290.006585840.02610470.0146440.00895830.010125150.02519660.01545480.01212910.0120438

To provide a numerical supplement to the graphical loss histories, representative values of the monitored composite loss are reported in table4. This complements the graphical training-loss histories and should be interpreted as an optimisation diagnostic. The ADI comparisons remain the primary solution-level validation of the trained PINN models.

## 4.3Validation of the time-dependent dispersion coefficient

The preceding comparisons establish the accuracy of the PINN at the levels of the two-dimensional concentration field and the cross-sectionally averaged concentration. We next examine whether this agreement is retained for the time-dependent axial spreading rate of the solute cloud. This constitutes a more demanding validation because the dispersion coefficient is obtained from the spatially integrated plume structure and the temporal derivative of its second central moment. Consequently, errors in plume displacement, deformation, or spreading can affect this quantity even when the corresponding concentration fields appear visually close.

Using the cross-sectionally averaged concentration⟨C⟩​(x,t)\langle C\rangle(x,t)and the streamwise centroidxg​(t)x_{g}(t)introduced previously, the normalised second central moment is written asν2​(t)=∫x0x1[x−xg​(t)]2​⟨C⟩​(x,t)​dx∫x0x1⟨C⟩​(x,t)​dx.\nu_{2}(t)=\frac{\displaystyle\int_{x_{0}}^{x_{1}}\left[x-x_{g}(t)\right]^{2}\langle C\rangle(x,t)\,\mathrm{d}x}{\displaystyle\int_{x_{0}}^{x_{1}}\langle C\rangle(x,t)\,\mathrm{d}x}.(40)

The corresponding apparent axial dispersion coefficient isDa​(t)=12​d​ν2​(t)d​t.D_{\mathrm{a}}(t)=\frac{1}{2}\frac{\mathrm{d}\nu_{2}(t)}{\mathrm{d}t}.(41)

This moment-based definition captures the transient evolution of the effective spreading rate and connects the plume-width dynamics to the apparent axial dispersion coefficientAris (1956); Barton (1983).

The absolute PINN–ADI discrepancy is defined byED​(t)=|DaPINN​(t)−DaADI​(t)|.E_{D}(t)=\left|D_{\mathrm{a}}^{\mathrm{PINN}}(t)-D_{\mathrm{a}}^{\mathrm{ADI}}(t)\right|.(42)

Unlike a pointwise concentration error,ED​(t)E_{D}(t)assesses a derived transport quantity involving spatial integration, normalisation, and temporal differentiation. Agreement inDa​(t)D_{\mathrm{a}}(t)therefore provides evidence that the PINN reproduces the evolving streamwise spreading dynamics generated by advection, molecular diffusion and reactive wall removal.Figure 11:Validation of the effective axial dispersion coefficient for Couette flow with the line-like source,q=Lq=\mathrm{L}. The internal panels correspond to the wall-reactivity configurations(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0),(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1)and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2). For each configuration,DaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)is compared withDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t), together with the corresponding absolute discrepancyED​(t)E_{D}(t).

Figure11provides a focused assessment of the line-like source under Couette shear. Because the initial concentration is distributed across the transverse direction, the subsequent variation ofDa​(t)D_{\mathrm{a}}(t)reflects the combined action of the linear velocity gradient, molecular diffusion and selective wall removal. Presenting the three wall-reactivity cases together permits a direct evaluation of whether the PINN retains its accuracy as the transport mechanism changes from non-reactive dispersion to symmetric and asymmetric reactive dispersion.

Physically, the early-time growth ofDa​(t)D_{\mathrm{a}}(t)is dominated by advective stretching and transverse diffusion, while the later-time tendency toward a plateau over the observed interval reflects the developing balance between shear-induced longitudinal spreading and transverse homogenization. In Poiseuille flow, the symmetric velocity profile restricts the maximal shear to the near-wall regions, whereas Couette flow maintains a constant shear rate across the entire domain. Consequently, the effective dispersion coefficientDa​(t)D_{\mathrm{a}}(t)in Couette flow exhibits a fundamentally different transient growth phase, as the solute is continuously stretched without the homogenising effect of a zero-shear centreline.(a)Couette flow withq=Pq=\mathrm{P}and(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).(b)Couette–Poiseuille flow withq=Pq=\mathrm{P}and(β1,β2)=(0,0)(\beta_{1},\beta_{2})=(0,0).Figure 12:Validation of the effective axial dispersion coefficient for non-reactive point-like-source configurations. The panels compareDaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)withDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t)and report the corresponding absolute discrepancyED​(t)E_{D}(t). The comparison between Couette and Couette–Poiseuille flow tests whether the PINN reproduces the spreading of an initially localised solute cloud under distinct shear structures before reactive wall removal is introduced.

Figure12establishes the non-reactive point-source baseline. In contrast to the line-like source, the point-like source introduces an initially localized wall-normal distribution. Its effective dispersion coefficient is therefore influenced by the early transverse redistribution of the solute as well as by its subsequent streamwise stretching. The agreement between the two velocity profiles confirms that the learned solution captures these coupled stages of plume evolution.(a)Couette flow withq=Pq=\mathrm{P}and(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).(b)Couette–Poiseuille flow withq=Pq=\mathrm{P}and(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1).Figure 13:Validation of the effective axial dispersion coefficient for symmetric wall absorption,(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1). The panels compareDaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)withDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t)for point-like releases in Couette and Couette–Poiseuille flow and show the associated absolute discrepancyED​(t)E_{D}(t).

Figure13extends the comparison to equal wall reactivity. Symmetric absorption reduces the surviving solute mass at both boundaries without imposing a preferential transverse direction of removal. Nevertheless, it can modify the normalised second central moment by selectively removing material that reaches the walls. The comparison, therefore, tests whether the PINN captures the effect of symmetric wall uptake on the evolving axial spreading rate.(a)Couette–Poiseuille flow withq=Lq=\mathrm{L}and(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).(b)Poiseuille flow withq=Pq=\mathrm{P}and(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).Figure 14:Validation of the effective axial dispersion coefficient for lower-wall-dominated absorption,(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2). The panels compareDaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)withDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t)for line-like and point-like sources under Couette–Poiseuille and Poiseuille flow, respectively, together with the corresponding absolute discrepancyED​(t)E_{D}(t).

Figure14examines a strongly asymmetric reaction regime in which removal at the lower wall dominates. The unequal values ofβ1\beta_{1}andβ2\beta_{2}alter the wall-normal distribution of the surviving solute and can consequently change its normalised streamwise variance. Including both source configurations and two different velocity profiles provides a stringent test of whether the PINN reproduces the coupling between shear-induced deformation and selective wall absorption.(a)Couette flow withq=Pq=\mathrm{P}and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).(b)Couette–Poiseuille flow withq=Pq=\mathrm{P}and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).Figure 15:Validation of the effective axial dispersion coefficient for upper-wall-dominated absorption,(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2). The panels compareDaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)withDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t)for point-like releases in Couette and Couette–Poiseuille flow and show the corresponding absolute discrepancyED​(t)E_{D}(t).

Figure15considers the reversed wall-reactivity asymmetry. Transferring the stronger absorption from the lower wall to the upper wall changes which part of the sheared concentration field is preferentially removed. The resulting comparison provides an additional test of the PINN because the effect of the reaction asymmetry depends on the interaction between the transverse concentration distribution and the local streamwise velocity.

Taken together, figures11–15establish the accuracy of the time-dependent dispersion coefficient across line-like and point-like sources, Couette, Poiseuille and Couette–Poiseuille flows, and non-reactive, symmetric and asymmetric wall-reactivity regimes. The inclusion of these comparisons in the main manuscript is justified becauseDa​(t)D_{\mathrm{a}}(t)is a physically interpretable transport measure rather than solely a numerical error diagnostic. Agreement betweenDaPINN​(t)D_{\mathrm{a}}^{\mathrm{PINN}}(t)andDaADI​(t)D_{\mathrm{a}}^{\mathrm{ADI}}(t)confirms that the PINN reproduces not only the concentration distribution but also the evolving streamwise spreading rate of the surviving reactive solute.

## 4.4Validation of the total surviving solute mass

The local concentration field and cross-sectional profile comparisons are complemented by a global mass-level validation. For both source configurations, the total surviving solute mass is defined asM0​(t)=∫x0x1∫−11C​(x,y,t)​dy​dx.M_{0}(t)=\int_{x_{0}}^{x_{1}}\int_{-1}^{1}C(x,y,t)\mathrm{d}y\,\mathrm{d}x.(43)

The corresponding absolute discrepancy between the PINN and ADI predictions isEM0​(t)=|M0PINN​(t)−M0ADI​(t)|.E_{M_{0}}(t)=\left|M_{0}^{\mathrm{PINN}}(t)-M_{0}^{\mathrm{ADI}}(t)\right|.(44)

The quantityM0​(t)M_{0}(t)provides a global measure of the amount of solute remaining within the channel. It is therefore sensitive to accumulated concentration errors over the full computational domain and, in the reactive cases, to the integrated effect of wall absorption. Agreement inM0​(t)M_{0}(t)is particularly important because an accurate local concentration field does not by itself guarantee that the total surviving mass or its decay rate is reproduced correctly.(a)Couette flow with the line-like source,q=Lq=\mathrm{L}.(b)Poiseuille flow with the line-like source,q=Lq=\mathrm{L}.(c)Couette–Poiseuille flow with the line-like source,q=Lq=\mathrm{L}.Figure 16:Validation of the total surviving solute massM0​(t)M_{0}(t)for the line-like source under Couette, Poiseuille and Couette–Poiseuille flows. The wall-reactivity configurations are identified within the individual panels. In each case,M0PINN​(t)M_{0}^{\mathrm{PINN}}(t)is compared withM0ADI​(t)M_{0}^{\mathrm{ADI}}(t), together with the corresponding absolute discrepancyEM0​(t)E_{M_{0}}(t).

Figure16shows the total-mass validation for the line-like source. Since the initial solute distribution is spread across the channel height, the evolution ofM0​(t)M_{0}(t)reflects the combined effects of transverse diffusion, shear-induced redistribution and reactive removal at the boundaries. The agreement betweenM0PINN​(t)M_{0}^{\mathrm{PINN}}(t)andM0ADI​(t)M_{0}^{\mathrm{ADI}}(t)confirms that the PINN captures the integrated mass evolution for an initially distributed concentration field.(a)Couette flow with the point-like source,q=Pq=\mathrm{P}.(b)Poiseuille flow with the point-like source,q=Pq=\mathrm{P}.(c)Couette–Poiseuille flow with the point-like source,q=Pq=\mathrm{P}.Figure 17:Validation of the total surviving solute massM0​(t)M_{0}(t)for the point-like source under Couette, Poiseuille and Couette–Poiseuille flows. The wall-reactivity configurations are identified within the individual panels. In each case,M0PINN​(t)M_{0}^{\mathrm{PINN}}(t)is compared withM0ADI​(t)M_{0}^{\mathrm{ADI}}(t), together with the corresponding absolute discrepancyEM0​(t)E_{M_{0}}(t).

Figure17shows the corresponding validation for the point-like source. In this case, the solute is initially localised, so the subsequent evolution ofM0​(t)M_{0}(t)depends on early transverse redistribution as well as on the transport of solute toward the reactive walls. The agreement betweenM0PINN​(t)M_{0}^{\mathrm{PINN}}(t)andM0ADI​(t)M_{0}^{\mathrm{ADI}}(t)verifies that the PINN captures not only the spatial distribution of concentration but also the integrated mass loss generated by the Robin boundary conditions.

The comparison across Couette, Poiseuille, and Couette–Poiseuille flows is useful because the velocity profile controls how rapidly solute is redistributed within the channel and transported toward regions from which transverse diffusion can deliver it to the reactive walls. The symmetric and asymmetric wall-reactivity cases further test whether the learned solution reproduces changes in the global removal rate as the absorption strengths at the two boundaries vary. Consequently, validatingM0​(t)M_{0}(t)provides an independent mass-balance assessment before considering higher-order spreading measures.

From a hydrodynamic perspective, the disparity in total mass decay rates across the Couette, Poiseuille, and combined flows stems directly from the differing near-wall velocity gradients. These gradients modulate the residence time of the solute within the highly reactive boundary layers. A higher near-wall velocity sweeps the solute past the reactive boundaries more rapidly, reducing local absorption opportunities, whereas a lower near-wall velocity increases the local absorption, thereby accelerating the global mass depletion quantified byM0​(t)M_{0}(t).

## 4.5Validation of the axial variance

The validation is next extended to the streamwise spreading of the surviving solute, quantified by the axial varianceν2​(t)\nu_{2}(t). As established in equation (40),ν2​(t)\nu_{2}(t)represents the normalised second central moment of the cross-sectionally averaged concentration profile. The absolute discrepancy between the PINN and ADI predictions for this quantity is defined asEν2​(t)=|ν2PINN​(t)−ν2ADI​(t)|.E_{\nu_{2}}(t)=\left|\nu_{2}^{\mathrm{PINN}}(t)-\nu_{2}^{\mathrm{ADI}}(t)\right|.(45)

The quantityν2​(t)\nu_{2}(t)measures the squared streamwise width of the solute distribution about its instantaneous centroid. Unlike the total surviving massM0​(t)M_{0}(t), which quantifies the amount of solute remaining within the channel,ν2​(t)\nu_{2}(t)characterises the spatial spreading of the surviving solute. The normalisation byM0​(t)M_{0}(t)is essential in the reactive problem because the total mass changes continuously owing to wall absorption. Agreement inν2​(t)\nu_{2}(t)therefore tests whether the PINN reproduces the evolving plume width independently of the overall reduction in solute mass.

To isolate the influence of the velocity profile, two matched point-like-source cases are considered under the same asymmetric wall-reactivity configuration,(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2). The source geometry and wall-reaction parameters are therefore fixed, while the flow is varied between Couette and Couette–Poiseuille profiles.(a)Couette flow withq=Pq=\mathrm{P}and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).(b)Couette–Poiseuille flow withq=Pq=\mathrm{P}and(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2).Figure 18:Validation of the axial varianceν2​(t)\nu_{2}(t)for point-like releases under upper-wall-dominated reactivity,(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2). Panel(a)(a)corresponds to Couette flow, while panel(b)(b)corresponds to Couette–Poiseuille flow. In each case,ν2PINN​(t)\nu_{2}^{\mathrm{PINN}}(t)is compared withν2ADI​(t)\nu_{2}^{\mathrm{ADI}}(t), together with the corresponding absolute discrepancyEν2​(t)E_{\nu_{2}}(t).

Figure18compares the PINN and ADI predictions ofν2​(t)\nu_{2}(t)for two distinct shear structures under identical source and reaction conditions. In Couette flow, the linear velocity gradient continuously stretches the solute distribution in the streamwise direction. In Couette–Poiseuille flow, the combined linear and parabolic contributions produce a different distribution of streamwise velocities across the channel and therefore a different evolution of the axial plume width.

The asymmetric wall-reactivity pair(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2)introduces preferential absorption at one boundary. This selective removal alters the wall-normal composition of the surviving concentration field and, through its interaction with the local streamwise velocity, can modify the axial variance. The matched comparison is therefore more stringent than a comparison involving different reaction parameters because differences between the two panels arise primarily from changes in the imposed velocity profile.

The agreement betweenν2PINN​(t)\nu_{2}^{\mathrm{PINN}}(t)andν2ADI​(t)\nu_{2}^{\mathrm{ADI}}(t)confirms that the PINN reproduces the evolving streamwise width of the surviving solute for both Couette and Couette–Poiseuille flows. The corresponding small values ofEν2​(t)E_{\nu_{2}}(t)further support the accuracy of the learned concentration field at the level of the normalised second central moment. Additional axial-variance comparisons for Couette flow with(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2)and Couette–Poiseuille flow with(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1)are reported in the supplementary material.

## 4.6Validation of cumulative wall-removal dynamics(a)Time-history comparison of𝒰tot​(t)\mathcal{U}_{\mathrm{tot}}(t).(b)Relative error in𝒰tot​(T)\mathcal{U}_{\mathrm{tot}}(T).(c)Scatter validation of𝒰tot​(T)\mathcal{U}_{\mathrm{tot}}(T).Figure 19:ADI–PINN validation of cumulative wall uptake for the point-like Gaussian sourceC0(P)​(x,y)=exp⁡(−x2−y2)C_{0}^{(\mathrm{P})}(x,y)=\exp(-x^{2}-y^{2}).
In panel (a), black solid curves denote the ADI finite-difference benchmark, while dashed curves denote the PINN predictions.
Panel (b) shows the final-time relative errorE𝒰E_{\mathcal{U}}, with the dashed horizontal line denoting a5%5\%reference level.
Panel (c) compares𝒰totPINN​(T)\mathcal{U}_{\mathrm{tot}}^{\mathrm{PINN}}(T)with𝒰totADI​(T)\mathcal{U}_{\mathrm{tot}}^{\mathrm{ADI}}(T); the dashed line denotes perfect agreement, and the dotted lines denote±3%\pm 3\%agreement bands. Marker shapes denote the shear profiles, while colours denote the reactive-wall configurations. The reportedR2R^{2}, RMSE and MAE quantify the final-time agreement between the PINN and ADI predictions.

We next validate the reactive-wall diagnostics for the point-like Gaussian source (8). This source is localised in both the streamwise and wall-normal directions. It therefore provides a stringent test of wall-removal dynamics, because the solute must first spread via transverse diffusion and shear-driven transport before being absorbed by the reactive walls. The validation is performed for the three reactive-wall configurations(β1,β2)=(1,1),(β1,β2)=(0.2,2),(β1,β2)=(2,0.2),(\beta_{1},\beta_{2})=(1,1),\qquad(\beta_{1},\beta_{2})=(0.2,2),\qquad(\beta_{1},\beta_{2})=(2,0.2),

and for the three mean-centred shear flows: Couette, Poiseuille and Couette–Poiseuille flow. Thus, the validation set contains nine flow–reaction cases.

This validation provides a more stringent test than concentration-field comparisons alone, as the total cumulative uptake relies heavily on the temporal accumulation of the boundary concentrations. Agreement in the total cumulative wall uptake,𝒰tot​(t)\mathcal{U}_{\mathrm{tot}}(t)(as defined in equation (31)), requires the PINN to accurately predict not only the advective-diffusive evolution of the interior plume but also the localised wall concentration history governing reactive removal at both boundaries.

In this validation subsection only, superscriptsPINN\mathrm{PINN}andADI\mathrm{ADI}are used to distinguish quantities computed from the trained neural-network solution and from the finite-difference benchmark. Figure19demonstrates that the PINN accurately reproduces the ADI-predicted cumulative wall uptake. The time histories in figure19(a) are in close agreement for all selected shear-flow and reactive-wall configurations, indicating that the trained network captures the temporal accumulation of wall removal. The relative-error plot in figure19(b) shows that the final-time error in𝒰tot​(T)\mathcal{U}_{\mathrm{tot}}(T)remains below5%5\%for all cases, with a maximum error of approximately3.38%3.38\%. The scatter comparison in figure19(c) provides a compact final-time validation: each marker corresponds to one flow–reaction case, with the horizontal coordinate representing𝒰totADI​(T)\mathcal{U}_{\mathrm{tot}}^{\mathrm{ADI}}(T)and the vertical coordinate representing𝒰totPINN​(T)\mathcal{U}_{\mathrm{tot}}^{\mathrm{PINN}}(T). The dashed diagonal line denotes perfect agreement, while the dotted lines indicate±3%\pm 3\%deviations from this line. The reportedR2R^{2}measures the linear agreement between the ADI and PINN final-time uptake values, whereas the root-mean-square error (RMSE) and mean absolute error (MAE) quantify the absolute discrepancy in𝒰tot​(T)\mathcal{U}_{\mathrm{tot}}(T). Together, these results confirm that the trained PINN reproduces both the time-dependent and final-time cumulative wall-removal dynamics with sufficient accuracy for the subsequent reactive-dispersion analysis.

## 4.7Reactive dispersion under wall-resolved absorption(a)Wall-resolved uptake rates.(b)Wall-resolved cumulative uptake.Figure 20:Wall-resolved reactive removal extracted from the trained PINN solution for the point-like Gaussian source.
Panel (a) shows the instantaneous integrated uptake rates𝒥+​(t)\mathcal{J}_{+}(t),𝒥−​(t)\mathcal{J}_{-}(t), and𝒥tot​(t)\mathcal{J}_{\mathrm{tot}}(t).
Panel (b) shows the corresponding cumulative uptakes𝒰+​(t)\mathcal{U}_{+}(t),𝒰−​(t)\mathcal{U}_{-}(t), and𝒰tot​(t)\mathcal{U}_{\mathrm{tot}}(t).
These quantities show how shear-driven dispersion and wall-dependent reactivity combine to determine total and wall-resolved solute removal.Figure 21:Final wall uptake components extracted from the trained PINN solution for the point-like Gaussian source.
The stacked bars show𝒰+​(T)\mathcal{U}_{+}(T)and𝒰−​(T)\mathcal{U}_{-}(T), so that the total bar height gives𝒰tot​(T)\mathcal{U}_{\mathrm{tot}}(T).
The plot provides a compact final-time summary of the wall-resolved removal contributions across the selected shear-flow and reactive-wall configurations.

Having validated the cumulative wall-removal dynamics, we now analyse how the removed solute is partitioned between the two reactive walls. Unless otherwise stated, the wall-uptake diagnostics in the remainder of this section are evaluated from the PINN-predicted concentration field for the point-like Gaussian source.

The total cumulative uptake𝒰tot​(t)\mathcal{U}_{\mathrm{tot}}(t)measures the combined removal by both walls. However, this total quantity alone does not indicate whether the removal is balanced between the upper and lower walls or dominated by one of them. We therefore examine the wall-resolved uptake rates𝒥+​(t)\mathcal{J}_{+}(t),𝒥−​(t)\mathcal{J}_{-}(t)and the corresponding cumulative uptakes𝒰+​(t)\mathcal{U}_{+}(t),𝒰−​(t)\mathcal{U}_{-}(t). This separation is important because symmetric and asymmetric wall reactions can produce different upper–lower uptake balances even when their total removal is comparable.

Figure20shows three physically distinct reactive-dispersion regimes. For the symmetric case(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1), the upper- and lower-wall contributions remain nearly balanced. This is expected because both the wall reactivity and the initial point-like source are symmetric about the channel centreline. This case, therefore, acts as a physical consistency check: the learned solution should not introduce artificial wall preference when the imposed problem is symmetric.

For(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2), the lower wall is ten times more reactive than the upper wall. The lower-wall uptake rate𝒥−​(t)\mathcal{J}_{-}(t)and cumulative uptake𝒰−​(t)\mathcal{U}_{-}(t)therefore dominate the removal. When the wall reactivities are reversed to(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2), the dominant wall-removal pathway is also reversed. These two cases demonstrate reaction-induced breaking of transverse symmetry: even though the source is initially centred, the unequal wall reactions bias the net removal toward the more reactive boundary.

The uptake curves also show that reactive dispersion is not governed by the wall coefficients alone. The wall flux is the product of a reaction coefficient and a wall concentration. Hence, the wall with the largerβi\beta_{i}tends to dominate, but the instantaneous magnitude and timing of uptake depend on how advection and diffusion deliver solute to that wall. The three shear profiles, therefore, create different hydrodynamic pathways for wall contact. Couette flow introduces antisymmetric linear shear, Poiseuille flow introduces a symmetric parabolic shear, and Couette–Poiseuille flow combines both effects. These differences affect the streamwise stretching of the plume and the distribution of near-wall concentration, which then influence𝒥±​(t)\mathcal{J}_{\pm}(t)and𝒰±​(t)\mathcal{U}_{\pm}(t).

The final-time decomposition in figure21condenses the same information into a compact wall-partition summary. The symmetric case gives comparable upper- and lower-wall contributions, while the asymmetric cases show clear dominance of the wall with the larger uptake coefficient. The total bar height also varies with the imposed shear flow, showing that the total removal is controlled jointly by wall reactivity and shear-driven solute redistribution.

## 4.8Wall selectivity and reaction-induced transverse asymmetry(a)Final lower-wall uptake fraction.(b)Cumulative wall-dominance index.Figure 22:Wall-selective reactive-dispersion diagnostics extracted from the trained PINN solution for the point-like Gaussian source.
Panel (a) shows the final lower-wall uptake fractionΦ−​(T)=𝒰−​(T)/𝒰tot​(T)\Phi_{-}(T)=\mathcal{U}_{-}(T)/\mathcal{U}_{\mathrm{tot}}(T).
Panel (b) shows the cumulative wall-dominance indexDw​(t)=[𝒰−​(t)−𝒰+​(t)]/𝒰tot​(t)D_{w}(t)=[\mathcal{U}_{-}(t)-\mathcal{U}_{+}(t)]/\mathcal{U}_{\mathrm{tot}}(t).
Positive values indicate lower-wall-dominated uptake, negative values indicate upper-wall-dominated uptake, and values near zero indicate balanced wall removal.

The wall-resolved uptake curves quantify absolute removal by each boundary. To isolate the relative partition of removal, we use the normalised diagnosticsΦ−​(T)=𝒰−​(T)𝒰tot​(T)\Phi_{-}(T)=\frac{\mathcal{U}_{-}(T)}{\mathcal{U}_{\mathrm{tot}}(T)}

andDw​(t)=𝒰−​(t)−𝒰+​(t)𝒰tot​(t).D_{w}(t)=\frac{\mathcal{U}_{-}(t)-\mathcal{U}_{+}(t)}{\mathcal{U}_{\mathrm{tot}}(t)}.

These quantities separate wall preference from the overall magnitude of uptake. Thus, they are especially useful for identifying reaction-induced transverse asymmetry.

Figure22(a) gives a compact final-time representation of wall selectivity. For(β1,β2)=(1,1)(\beta_{1},\beta_{2})=(1,1), the values remain close toΦ−​(T)=1/2\Phi_{-}(T)=1/2, indicating balanced removal. For(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2),Φ−​(T)>1/2\Phi_{-}(T)>1/2, confirming lower-wall-dominated uptake. For(β1,β2)=(2,0.2)(\beta_{1},\beta_{2})=(2,0.2),Φ−​(T)<1/2\Phi_{-}(T)<1/2, indicating upper-wall-dominated uptake. The dynamic index in figure22(b) gives the corresponding time-dependent picture:Dw​(t)D_{w}(t)remains near zero for symmetric reactivity, becomes positive when the lower wall is more reactive, and becomes negative when the upper wall is more reactive.

This result highlights an important feature of reactive dispersion: the total cumulative uptake measures how much solute is removed, but it fails to capture the spatial distortion of the plume. The diagnosticsΦ−​(T)\Phi_{-}(T)andDw​(t)D_{w}(t)reveal that unequal wall reactivities (e.g.,β1≠β2\beta_{1}\neq\beta_{2}) break the transverse symmetry of the concentration field. This wall-selective uptake effectively creates a depleted concentration boundary layer near the highly reactive wall, steepening the local transverse concentration gradient and driving a continuous, asymmetric diffusive flux from the bulk. Capturing this transverse non-uniformity is essential, as classical one-dimensional models inherently average out the cross-sectional variations that dictate the slow-decaying transient effects in highly asymmetric reactive environmentsDharet al.(2021); Jianget al.(2022); Poddar and Wang (2024).

## 4.9Shear-dependent streamwise organisation of reactive uptakeFigure 23:Local wall uptake flux profiles for the point-like Gaussian source in the asymmetric reactive case(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).
Blue solid curves denoteJ+​(x,t)J_{+}(x,t), while red dashed curves denoteJ−​(x,t)J_{-}(x,t).
The annotation boxes reportmaxx⁡J+​(x,t)\max_{x}J_{+}(x,t)andmaxx⁡J−​(x,t)\max_{x}J_{-}(x,t), highlighting the stronger lower-wall removal associated with the larger lower-wall reactivity.Figure 24:Flux-weighted uptake centroid and spread for the point-like Gaussian source in the asymmetric reactive case(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).
The centroidsxJ±​(t)x_{J_{\pm}}(t)identify the streamwise locations where the upper- and lower-wall uptake profiles are concentrated, whileσJ±​(t)\sigma_{J_{\pm}}(t)measures their spatial spread.
These diagnostics reveal flow-dependent spatial organisation of wall removal even when the total cumulative uptake is similar across the mean-centred shear profiles.

The preceding diagnostics quantify the amount and wall-partitioned removal. We now examine where along the channel this uptake occurs. This is a distinct physical question, because two flows may remove a similar total amount of solute but concentrate the removal in different streamwise regions.

Figure23shows the local wall-flux profiles for the asymmetric reactive case(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2). Since the lower wall is ten times more reactive than the upper wall, the lower-wall fluxJ−​(x,t)J_{-}(x,t)is larger than the upper-wall fluxJ+​(x,t)J_{+}(x,t). However, the streamwise position and width of these flux profiles depend on the imposed shear flow, because the velocity field controls how the solute cloud is stretched and delivered to the wall.

The centroid and spread diagnostics in figure24quantify this spatial organisation. The centroidxJ±​(t)x_{J_{\pm}}(t)gives the effective streamwise location where wall uptake is concentrated, whileσJ±​(t)\sigma_{J_{\pm}}(t)measures the streamwise width of the uptake region. In Couette flow, the mean-centred velocity is antisymmetric, so solute near the upper and lower walls is transported in opposite streamwise directions. This produces a separation between the effective uptake locations at the two walls. In Poiseuille flow, the mean-centred velocity is symmetric about the centre line and has the same value at both walls, so the wall-flux distributions remain more symmetrically organised. In Couette–Poiseuille flow, the linear and parabolic components combine to produce a stronger imbalance between the two wall-adjacent velocities, leading to a more pronounced displacement of the uptake centroid, especially at the more reactive lower wall.

Thus, the reaction coefficient determines how strongly a wall absorbs solute once the solute reaches it, while the shear profile determines where along the channel the solute is delivered to the wall. Figure24therefore demonstrates that wall-reactive dispersion must be characterised not only by the total cumulative uptake𝒰tot​(t)\mathcal{U}_{\mathrm{tot}}(t), but also by the streamwise location and spread of the wall-removal region.

## 4.10Coupled concentration–shear–reaction structureFigure 25:Concentration contours with superposed mean-centred velocity arrows and wall-flux arrows for the point-like Gaussian source in the asymmetric reactive case(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2).
Black arrows inside the channel indicate the imposed shear velocityu(s)​(y)u^{(s)}(y).
Blue and red/orange wall-normal arrows indicate the local upper- and lower-wall uptake fluxesJ+​(x,t)J_{+}(x,t)andJ−​(x,t)J_{-}(x,t), respectively.
The stronger lower-wall arrows visualise the enhanced lower-wall uptake caused byβ2>β1\beta_{2}>\beta_{1}.

We connect the wall-flux diagnostics to the underlying concentration field and imposed shear profile. Figure25shows the PINN-predicted concentration contours together with mean-centred velocity arrows and wall-normal uptake arrows for the point-like Gaussian source with(β1,β2)=(0.2,2)(\beta_{1},\beta_{2})=(0.2,2). This representation gives a direct physical picture of the coupled concentration–shear–reaction mechanism.

The mean-centred shear profile redistributes the solute cloud in the streamwise direction. Transverse diffusion transports solute from the channel interior toward the reactive boundaries. Once the solute reaches the wall, the local uptake is determined by the product of wall concentration and wall reactivity. Hence, the wall-flux arrows are stronger at the lower wall in the asymmetric case becauseβ2>β1\beta_{2}>\beta_{1}. The figure visually confirms the same mechanism quantified by the uptake curves, wall-dominance index, local flux profiles and centroid/spread diagnostics.

This combined view emphasises the central physical contribution of the present study. The PINN is not used only as a mesh-free approximation ofC​(x,y,t)C(x,y,t). Its differentiable representation enables systematic extraction of wall-resolved quantities from the learned solution. These diagnostics show that reactive dispersion in shear flows is governed by three coupled mechanisms: hydrodynamic redistribution of the solute cloud, transverse diffusive delivery to the walls, and wall-dependent absorption. The resulting wall removal is therefore characterised not only by the total amount removed, but also by the dominant wall, the time at which dominance develops, and the streamwise location and spread of the uptake region.

## 5Conclusions

In this study, a physics-informed neural network (PINN) framework is developed to investigate the two-dimensional dispersion of reactive solutes in canonical shear flows bounded by first-order absorbing walls. By embedding the dimensionless convection–diffusion equation, localised initial source distributions, and reactive Robin boundary conditions into a unified composite loss function, the PINN provides a mesh-free framework for imposing the governing equation and boundary constraints within a single optimisation problem.

The physical fidelity of the mesh-free framework was rigorously validated against an alternating-direction implicit (ADI) finite-difference benchmark. The network accurately captured the spatiotemporal evolution of the two-dimensional concentration fields, the cross-sectionally averaged profiles, and the total surviving solute mass across Couette, Poiseuille, and combined Couette–Poiseuille flows. More critically, the continuous and fully differentiable nature of the trained PINN surrogate enabled the precise extraction of derived integral transport characteristics, such as the time-dependent effective dispersion coefficient and the axial variance, without introducing numerical truncation errors typical of discrete methods.

Beyond validating the concentration fields, this study utilised the differentiable network to uncover the detailed mechanics of wall-resolved reactive dispersion. The analysis demonstrated that unequal wall reactivities (e.g.,β1≠β2\beta_{1}\neq\beta_{2}) fundamentally break the transverse symmetry of the concentration field, leading to highly selective, asymmetric wall-removal processes. The introduction of flux-weighted uptake centroids and spread diagnostics revealed that the imposed hydrodynamic shear profile controls the streamwise spatial organisation of this removal. Specifically, the antisymmetric shear of Couette flow creates a distinct spatial divergence in upper- and lower-wall uptake locations, whereas the symmetric Poiseuille flow confines reactive depletion to overlapping streamwise coordinates. These findings confirm that macroscopic reactive dispersion cannot be fully characterised by total solute removal alone; the specific advective-diffusive pathways dictating local wall contact are equally critical.

Ultimately, this work establishes that PINNs provide an interpretable mesh-free framework for analysing complex mass transport problems. Nevertheless, the precise evaluation of the longitudinal dispersion coefficient remains challenging because its computation relies on derivatives of the second moment of the expected concentration field, which are prone to local approximation errors. Future research will consequently focus on improving PINN formulations that enhance derivative accuracy, thereby permitting more reliable prediction of dispersion properties. By combining PINNs with the classical technique of moments and mean concentration expansion, further work may eliminate the need to explicitly resolve the singular initial condition. Diffusiophoretic transport, nonlinear phase-exchange kinetics, and non-Newtonian or oscillatory flow regimes can be studied using this framework. The PINN framework can also be extended to study tracer dispersion in advection-dominated flows.\backsection

[Acknowledgements]
The authors thank their respective institutions for providing a supportive research environment.\backsection

[Declaration of interests]
The authors report no conflict of interest.\backsection

[Data availability statement]
The codes which developed to generate the results in this study are available from the corresponding author upon reasonable request.

## References
- C. M. Allen (1982)Numerical simulation of contaminant dispersion in estuary flows.Proc. R. Soc. Lond. A381,pp. 179–194.Cited by:§1.
- A. Arab, T. Scheytt, T. Nagel, and R. Taherdangkoo (2026)Physics-informed neural network surrogate for reactive nitrate transport in groundwater.Advances in Water Resources213,pp. 105305.External Links:DocumentCited by:§1.
- R. Aris (1956)On the dispersion of a solute in a fluid flowing through a tube.Proc. R. Soc. Lond. A235,pp. 67–77.Cited by:§1,§4.3.
- R. Aris (1959)On the dispersion of a solute by diffusion, convection and exchange between phases.Proc. R. Soc. Lond. A252,pp. 538–550.Cited by:§1.
- S. Bandyopadhyay and B. S. Mazumder (1999a)On contaminant dispersion in unsteady generalised Couette flow.Int. J. Engng Sci.37(11),pp. 1407–1423.Cited by:§1.
- S. Bandyopadhyay and B. S. Mazumder (1999b)Unsteady convective diffusion in a pulsatile flow through a channel.Acta Mechanica134,pp. 1–16.Cited by:§1.
- S. Barik and D. C. Dalal (2017)On transport coefficients in an oscillatory couette flow with nonlinear chemical decay reactions.Acta Mechanica228(7),pp. 2391–2412.External Links:DocumentCited by:§1.
- S. Barik and D. C. Dalal (2019)Multi-scale analysis for concentration distribution in an oscillatory Couette flow.Proc. R. Soc. Lond. A475,pp. 20180483.Cited by:§1,§2.5.
- S. Barik and D. C. Dalal (2022)Analytical solution for concentration distribution in an open channel flow with phase exchange kinetics.Acta Mechanica Sin.38,pp. 321506.Cited by:§1.
- N. G. Barton (1983)On the method of moments for solute dispersion.J. Fluid Mech.126,pp. 205–218.Cited by:§1,§4.3.
- H. O. Caldag and M. A. Bees (2025)Fine-tuning the dispersion of active suspensions with oscillatory flows.Phil. Trans. R. Soc. Math. Phys. Engng Sci.383,pp. 20240259.Cited by:§1.
- P. C. Chatwin (1970)The approach to normality of the concentration distribution of a solute in a solvent flowing along a straight pipe.J. Fluid Mech.43,pp. 321–352.Cited by:§1.
- Y. Cui, T. Liu, M. Zhao, B. Song, X. Ni, and J. Chen (2026)PINN modeling for predicting the solute concentration distribution of COBC with case study on L-glutamic acid crystallization.Chemical Engineering Research and Design225,pp. 363–375.Cited by:§1.
- D. Das, S. Dhar, R. R. Kairi, K. K. Mondal, and N. Poddar (2024a)Analysis of environmental transport of suspended sediment particles in a tidal wetland flow under the effect of floating vegetation absorption.Commun. Nonlinear Sci. Numer. Simul.132,pp. 107888.Cited by:§1.
- D. Das, K. K. Mondal, N. Poddar, and P. Wang (2024b)Transient dispersion of a reactive solute in an oscillatory Couette flow through an anisotropic porous medium.Phys. Fluids36,pp. 023610.Cited by:§1.
- S. K. Das and B. S. Mazumder (1989)Dispersion of reactive solute in liquid flowing through a tube.Int. J. Engng Sci.27,pp. 1203–1209.Cited by:§1.
- S. Debnath and K. Ghoshal (2020)Transport of reactive species in oscillatory couette–poiseuille flows subject to homogeneous and heterogeneous reactions.Applied Mathematics and Computation385,pp. 125387.External Links:DocumentCited by:§1,§1.
- S. Dhar, N. Poddar, K. K. Mondal, and B. S. Mazumder (2021)On dispersion of solute in a hydromagnetic flow between two parallel plates with boundary absorption.Phys. Fluids33,pp. 083609.Cited by:§1,§4.8.
- J. Douglas (1955)On the numerical integration of∂2u/∂x2+∂2u/∂y2=∂u/∂t\partial^{2}u/\partial x^{2}+\partial^{2}u/\partial y^{2}=\partial u/\partial tby implicit methods.J. Soc. Ind. Appl. Math.3,pp. 42–65.Cited by:§1,§1,§3.8.
- W. N. Gill and R. Sankarasubramanian (1970)Exact analysis of unsteady convective diffusion.Proc. R. Soc. Lond. A316,pp. 341–350.Cited by:§1.
- M. Guan and G. Chen (2024)Streamwise dispersion of soluble matter in solvent flowing through a tube.J. Fluid Mech.980,pp. A33.Cited by:§1.
- P. S. Gupta and A. S. Gupta (1972)Effect of homogeneous and heterogeneous reactions on the dispersion of a solute in the laminar flow between two plates.Proc. R. Soc. A330,pp. 59–63.Cited by:§1.
- Q. He and A. M. Tartakovsky (2021)Physics-informed neural network method for forward and backward advection-dispersion equations.Water Resources Research57,pp. e2020WR029479.Cited by:§1,§3.2.
- Q. Hou, Z. Sun, L. He, and A. Karemat (2022)Orthogonal grid physics-informed neural networks: a neural network-based simulation tool for advection–diffusion–reaction problems.Physics of Fluids34(7),pp. 077108.External Links:DocumentCited by:§1.
- Q. Hou, X. Xu, Z. Sun, J. Wang, and V. P. Singh (2025)Physics informed neural network for forward and inverse multispecies contaminant transport with variable parameters.Journal of Hydrology655,pp. 132977.Cited by:§1.
- W. Jiang and G. Chen (2026)Transient dispersion in oscillatory flows: auxiliary-time extension method for concentration moments.J. Fluid Mech.1031,pp. A15.Cited by:§1.
- W. Q. Jiang and G. Q. Chen (2018)Solution of Gill’s generalized dispersion model: solute transport in Poiseuille flow with wall absorption.Intl J. Heat Mass Transfer127,pp. 34–43.Cited by:§1.
- W. Jiang, L. Zeng, X. Fu, and Z. Wu (2022)Analytical solutions for reactive shear dispersion with boundary adsorption and desorption.J. Fluid Mech.947,pp. A37.Cited by:§1,§3.3,§4.8.
- Z. Jiao, X. Zhu, G. Xiong, S. Mo, Y. Meng, J. Wu, and J. Wu (2026)An efficient multi-physics GPT-PINN framework for predicting reactive solute transport in parameterized groundwater systems.Geophysical Research Letters53,pp. e2025GL120217.Cited by:§1.
- H. Kamil, A. Soulaïmani, and A. Beljadid (2025)A comparative study of physics-informed neural network strategies for modeling water and nitrogen transport in unsaturated soils.Journal of Hydrology661,pp. 133624.Cited by:§1.
- M. Latini and A. J. Bernoff (2001)Transient anomalous diffusion in Poiseuille flow.Journal of Fluid Mechanics441,pp. 399–411.External Links:DocumentCited by:§1.
- M. J. Lighthill (1966)Initial development of diffusion in Poiseuille flow.IMA J. Appl. Math.2,pp. 97–108.Cited by:§1.
- R. Mamud, C. T. Zanini, H. S. Migon, and A. J. S. Neto (2023)Solution of advection–diffusion–reaction inverse problems with physics-informed neural networks.InProceeding Series of the Brazilian Society of Computational and Applied Mathematics,Vol.10,pp. 2–7.External Links:DocumentCited by:§1.
- B. S. Mazumder and S. K. Das (1992)Effect of boundary reaction on solute dispersion in pulsatile flow through a tube.J. Fluid Mech.239,pp. 523–549.Cited by:§1.
- A. Mohapatra, A. Kumar, M. Deb, S. Dhomkar, and R. Singh (2025)Inferring activity from the flow field around active colloidal particles using deep learning.J. Fluid Mech.1018,pp. R1.Cited by:§1.
- K. K. Mondal, S. Dhar, and B. S. Mazumder (2020)On dispersion of solute in steady flow through a channel with absorption boundary: an application to sewage dispersion.Theoretical and Computational Fluid Dynamics34(6),pp. 643–658.External Links:DocumentCited by:§1.
- K. K. Mondal and B. S. Mazumder (2005)On the solute dispersion in a pipe of annular cross-section with absorption boundary.Z. Angew. Math. Mech.85,pp. 422–430.Cited by:§1.
- K. K. Mondal and B. Mazumder (2006)On dispersion of settling particles from an elevated source in an open-channel flow.Journal of Computational and Applied Mathematics193(1),pp. 22–37.External Links:DocumentCited by:§1,§1.
- C. O. Ng and N. Rudraiah (2008)Convective diffusion in steady flow through a tube with a retentive and absorptive wall.Phys. Fluids20,pp. 073604.Cited by:§1,§2.2.
- C. O. Ng and T. L. Yip (2001)Effects of kinetic sorptive exchange on solute transport in open-channel flow.J. Fluid Mech.446,pp. 321–345.Cited by:§1.
- C.-O. Ng (2006)Dispersion in steady and oscillatory flows through a tube with reversible and irreversible wall reactions.Proc. R. Soc. Lond. A462,pp. 481–515.Cited by:§1.
- J. Niu, W. Xu, H. Qiu, S. Li, and F. Dong (2023)1-d coupled surface flow and transport equations revisited via the physics-informed neural network approach.Journal of Hydrology625,pp. 130048.External Links:DocumentCited by:§1.
- S. Paul and B. S. Mazumder (2008)Dispersion in unsteady Couette–Poiseuille flows.Int. J. Engng Sci.46,pp. 1203–1217.Cited by:§1,§2.5.
- D. W. Peaceman and H. H. Rachford (1955)The numerical solution of parabolic and elliptic differential equations.J. Soc. Ind. Appl. Math.3,pp. 28–41.Cited by:§1,§1,§3.8.
- N. Poddar, D. Das, S. Dhar, and K. K. Mondal (2023)On scalar transport in an oscillatory Couette–Poiseuille flow under the effects of heterogeneous and bulk chemical reactions: a multi-scale approach.Phys. Fluids35,pp. 043617.Cited by:§1,§2.5.
- N. Poddar, S. Dhar, B. S. Mazumder, and K. K. Mondal (2021a)An exact analysis of scalar transport in hydromagnetic flow between two parallel plates: a multi-scale approach.Proc. R. Soc. A477,pp. 20200830.Cited by:§1.
- N. Poddar, K. K. Mondal, and N. Madden (2021b)Layer-adapted meshes for solute dispersion in a steady flow through an annulus with wall absorption: application to a catheterized artery.Korea-Aust. Rheol. J.33,pp. 11–24.Cited by:§1.
- N. Poddar, S. Dhar, B. S. Mazumder, R. R. Kairi, and K. K. Mondal (2021c)Effects of bulk degradation and boundary absorption on dispersion of contaminant in wetland flow.Intl J. Heat Mass Transfer179,pp. 121669.Cited by:§1,§2.2.
- N. Poddar, G. Saha, K. K. Mondal, S. Dhar, and B. S. Mazumder (2024)Effect of phase exchange kinetics on Taylor dispersion of chemically reactive solutes in an oscillatory magnetohydrodynamics flow between two parallel plates.Phys. Fluids36,pp. 053601.Cited by:§1.
- N. Poddar and P. Wang (2024)Transport of reactive contaminant in a wetland flow with the effects of reversible and irreversible reactions on the bed surface.Intl Commun. Heat Mass Transfer157,pp. 107709.Cited by:§1,§4.8.
- A. Purnama (1988)Boundary retention effects upon contaminant dispersion in parallel flows.J. Fluid Mech.195,pp. 393–412.Cited by:§1,§2.2.
- Y. Qiu, Y. Jin, and J. Chen (2025)Physics-informed neural networks for exploring soliton collisions in the non-integrable schamel equation in plasmas.Physics of Fluids37,pp. 127119.Cited by:§1.
- M. Raissi, P. Perdikaris, and G. E. Karniadakis (2019)Physics-informed neural networks: a deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.Journal of Computational Physics378,pp. 686–707.Cited by:§1,§3.2,§3.6.
- J. Rana and P. N. Murthy (2016)Unsteady solute dispersion in non-newtonian fluid flow in a tube with wall absorption.Proc. R. Soc. A472,pp. 20160294.Cited by:§1.
- J. I. Rawden, C. Vanderwel, and S. Symon (2026)Physics-informed neural networks for passive scalar emission and transport.Phys. Rev. Fluids11,pp. 024501.Cited by:§1,§3.3.
- G. Saha, N. Poddar, K. K. Mondal, and P. Wang (2024)Evolution of concentration distribution and removal of a solute in magnetohydrodynamics channel flow: effects of buoyancy-driven force and induced magnetic field.Proc. R. Soc. A480,pp. 20240091.Cited by:§1.
- R. Sankarasubramanian and W. N. Gill (1973)Unsteady convective diffusion with interphase mass transfer.Proc. R. Soc. Lond. A333,pp. 115–132.Cited by:§1.
- A. Sarkar and G. Jayaraman (2002)The effect of wall absorption on dispersion in annular flows.Acta Mech.158,pp. 105–119.Cited by:§1.
- W. Shu, J. Jiang, J. Wu, Y. Sun, and F. Deng (2026)ASR-pinn: adaptive step-size runge–kutta physics-informed neural network for multi-component reactive solute transport.Journal of Hydrology669,pp. 135127.External Links:DocumentCited by:§1.
- R. Smith (1983)Effect of boundary absorption upon longitudinal dispersion in shear flows.J. Fluid Mech.134,pp. 161–177.Cited by:§1.
- A. N. Stokes and N. G. Barton (1990)The concentration distribution produced by shear dispersion of solute in Poiseuille flow.J. Fluid Mech.210,pp. 201–221.Cited by:§1.
- G. I. Taylor (1953)Dispersion of soluble matter in solvent flowing slowly through a tube.Proc. R. Soc. Lond. A219,pp. 186–203.Cited by:§1.
- J. Teng, B. Rallabandi, and J. T. Ault (2023)Diffusioosmotic dispersion of solute in a long narrow channel.Journal of Fluid Mechanics977,pp. A5.External Links:DocumentCited by:§1,§3.3.
- Z. Wu and G. Q. Chen (2014a)Analytical solution for scalar transport in open channel flow: slow-decaying transient effect.J. Hydrol.519,pp. 1974–1984.Cited by:§1.
- Z. Wu and G. Q. Chen (2014b)Approach to transverse uniformity of concentration distribution of a solute in a solvent flowing along a straight pipe.J. Fluid Mech.740,pp. 196–213.Cited by:§1.
- Z. Zou, Z. Wang, and G. E. Karniadakis (2025)Learning and discovering multiple solutions using physics-informed neural networks with random initialization and deep ensemble.Proc. R. Soc. A481,pp. 20250205.Cited by:§1,§3.6.

## 


- 


Major funding support from
