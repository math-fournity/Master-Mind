# Non-linear control variate in δf particle-in-cell methods using symplectic neural networks

**arXiv ID**: 2606.30622v1
**Authors**: Victor Fournet, Martin Campos Pinto, Emmanuel Franck, Victor Michel-Dansac
**Published**: 2026-06-29
**Categories**: physics.comp-ph, math.NA
**HTML URL**: https://arxiv.org/html/2606.30622v1

## Abstract

We present a novel δf particle-in-cell (PIC) method for the kinetic simulation of electrostatic plasmas in which the bulk density, acting as a control variate, is evolved using symplectic neural networks (SympNets). The SympNets are used as an approximation of the backward flow and trained using the particle trajectories. We introduce a periodic variant of the SympNet architecture that encodes the spatial periodicity of the problem into the network itself. We validate the approach with numerical results in 1D1V and 3D3V for the Vlasov-Poisson system.

## Full Text

Non-linear control variate in 𝛿⁢𝑓 particle-in-cell methods using symplectic neural networks

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
- License: CC BY 4.0arXiv:2606.30622v1 [physics.comp-ph] 29 Jun 2026

## Non-linear control variate inδ​f\delta\!fparticle-in-cell methods
using symplectic neural networksVictor Fournet1Martin Campos Pinto1Emmanuel Franck2Victor Michel-Dansac2
1Max Planck Institute for Plasma Physics, Garching, Germany
2Université de Strasbourg, CNRS, Inria, IRMA, F-67000, Strasbourg, France

## Abstract

We present a novelδ​f\delta\!fparticle-in-cell (PIC) method for the kinetic
simulation of electrostatic plasmas in which the bulk density, acting as a
control variate, is evolved using symplectic neural
networks (SympNets). The SympNets are used as an approximation of the backward flow and trained using the particle trajectories. We introduce a
periodic variant of the SympNet architecture that encodes the spatial
periodicity of the problem into the network itself. We validate the approach with numerical results in 1D1V and 3D3V for the Vlasov-Poisson system.

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

High-fidelity plasma simulations often require solving kinetic equations, which are nonlinear transport equations posed in phase spaces of moderate to high dimension (up to six in the case of three-dimensional space and velocity).

Grid-based methods such as
semi-Lagrangian[36]or Eulerian[3]schemes can compute
the distribution function on a grid, but indddimensions their storage cost scales as𝒪​(nd)\mathcal{O}(n^{d}), wherennis the number of grid points per direction, making fine-resolution
simulations prohibitively expensive. This phenomenon is known as thecurse of dimensionality.
An additional fundamental difficulty isfilamentation: distribution function often develop
fine-scale structures in phase space as time evolves, requiring a fine enough grid
to be accurately resolved.

The Particle-In-Cell (PIC) method[9,10]is a popular method to avoid a full discretisation of the phase space, representing the distribution as a collection ofNpN_{p}numerical markers or macro-particles. The computational cost of the method grows only linearly withNpN_{p}, but
it suffers from statistical noise that decreases inNp−1/2N_{p}^{-\nicefrac{{1}}{{2}}}which comes from the Monte Carlo approximation of the moments of the distribution function.

A classical strategy to reduce this noise is theδ​f\delta\!fapproach[23,15,32,31,19], in which the distribution is
decomposed asf=f0+δ​ff=f_{0}+\delta\!f, wheref0f_{0}is an analytically known bulk
density, while the termδ​f\delta\!fis discretised by numerical particles carrying time-dependent weights
so that the underlying transport equation is the same.
The moments are split in the same way: those of the bulk are evaluated analytically and only theδ​f\delta\!fpart is evaluated by a Monte Carlo approximation.
Iff0f_{0}is a good approximation toff, the weights are small, reducing the
statistical error.
For this reason theδ​f\delta\!fmethod may be interpreted as acontrol variate method[4], a well-known noise reduction technique in Monte Carlo methods.

In many practical problems,f0f_{0}is a steady state of the system, which is a valid choice as long as the
plasma stays close to that equilibrium, as it is often the case for magnetic fusion simulations[26].
However, in regimes where the distribution diverges significantly from its initial state, such as in simulations close to the edge of a tokamak plasma, which involves steep gradients and low density levels[29,30],
a static bulk is no longer adequate and the particle weights become large.
This eventually cancels the noise-reduction benefit.

A natural idea to recover a good noise reduction is then to also evolve the bulk in time.
Several approaches have been developed in this direction[1,13,30]. A common strategy is to assume that the bulk densityf0f_{0}takes the form of a Maxwellian distribution, and to evolve its moments in time using fluid equations[30,12]. This has the advantage that the moments of the distribution function are easy to compute. Another way is to directly represent the bulk on a phase space grid using B-splines[13,1]. For instance in[13], the flow is approximated using a collection of auxiliary particles that are initialized on a grid and then pushed forward by the PIC scheme. The approximated backward flow is then computed using linear or quadratic Taylor expansions around these particles, and the density is transported by this flow and projected on a coarse spline grid. This method works well in 1D1V; however, its isotropic nature limits its performance in higher dimensions where flows may exhibit anisotropic smoothness[13].

Recently, there has been a growing interest in incorporating neural networks in classical methods[34],
in particular for high dimensional problems where they can be used to mitigate the curse of
dimensionality[5]. One example is Physics-Informed Neural Networks (PINNs)[33,14,6,20,40]where the PDE residual is directly incorporated in the loss function, and a space-time approximation is used. Another possibility is to use a time-discrete approach, where the network only approximates the solution in space, and its parameters evolve at each time step. Such examples are discrete PINNs[8,38], Neural Galerkin methods[11], and neural semi-Lagrangian methods[16]. All these works show that neural networks can be a promising approach to approximate functions living in a high dimensional space, while circumventing the curse of dimensionality.

In this work, focusing on the Vlasov-Poisson system as a proof of concept,
we propose an extension of the method described in[13]:
again the bulk densityf0f_{0}is represented on a coarse grid with B-splines, but it is no longer
updated with a backward flow computed from isotropic Taylor expansions. Instead,
we use a neural network to approximate the backward flow associated with particles pushed forward by a given PIC scheme.
Composing this “neural flow” with the initial density provides us with a fine representation of the full solutionff,
which is then projected on a coarse grid of B-splines at a relatively small computational cost to obtain the bulk densityf0f_{0}.
Note that the fine representation is easy to evaluate at any point in phase space, but its moments are difficult to compute due to the phase space filamentations. The spline bulk density does not suffer from this issue, as both its point values and its moments are straightforward to compute. Nevertheless, as it is always updated from the fine representation, it remains close to the full solution which allows us to keep the weights small and reduce the noise.

In long-time simulations, one would eventually need to remap the fine representation, that is, to re-approximate it so as to reset the growing composition of neural flows, at the price of some loss of information, once this composition becomes too costly to evaluate. Performed at every time step in a standard semi-Lagrangian scheme, this remapping is here required only over very long times, which makes our method onlyweaklysemi-Lagrangian, in the spirit of the Characteristic Mapping Method[24]. In all the simulations reported in this work, it was in fact never necessary.

The main advantages of this new method are twofold. First, it strongly mitigates the curse of dimensionality, as neural networks have the ability to efficiently approximate functions with anisotropic smoothness in high dimensions[16,5]. Second, it allows to get rid of the auxiliary particles used in[13]to approximate the flow,
which simplifies its integration with an existing PIC scheme.
Indeed, to train the flow networks at any desired point in time, we use the current and previous particle coordinates computed with the PIC scheme as training data, without requiring them to be on a structured grid.

Since the Vlasov-Poisson system is Hamiltonian, its flow is symplectic.
We choose to approximate it using the well-known paradigm of symplectic neural networks (SympNets, see[21]). Such neural networks are designed to directly incorporate symplecticity into their architecture, bypassing the need to add an additional penalization term in the loss function.
Since we are dealing with periodic boundary conditions, as is natural in plasma physics simulations, we furthermore introduce a newperiodicSympNet architecture that natively encodes the spatial periodicity into the network, once again avoiding an additional penalization term.

The resulting method, which we call theNeuralδ​f\delta\!f-PIC scheme, has the
following features:
- •

The bulk density is updated entirely from particle data, without requiring
auxiliary markers or fine grid semi-Lagrangian steps.
- •

The symplectic structure of the Vlasov flow is preserved at the level of
the fine (lagrangian) representation.
- •

The method extends naturally to high-dimensional phase spaces, as neural network architectures scale well to high dimensional problems and the training data are directly provided by the existing PIC particles.

We stress that the goal of this work is a proof of concept: the Vlasov-Poisson system is used as a controlled and well-understood test bed to assess whether symplectic neural networks coupled can effectively denoise the density by dynamically evolving the bulk on a coarse spline grid. In this study, the objective is not to obtain a method that would be more efficient than a standardδ​f\delta\!f-PIC scheme in every possible regime. Our motivation lies in regimes where a static, or even a Maxwellian, bulk is inadequate and where evolving it is genuinely necessary, such as edge gyrokinetic simulations[30,29]where prohibitive numbers of particles would be required without a dynamic control variate.

The remainder of the paper is organised as follows.Section˜2recalls the Vlasov-Poisson system and the classicalδ​f\delta\!f-PIC framework.Section˜3describes the SympNet architecture and its periodic
extension.Section˜4presents the Neuralδ​f\delta\!f-PIC algorithm.Section˜5reports numerical results in 1D1V and 3D3V.Section˜6concludes with a discussion and perspectives.

## 2Theδ​f\delta\!f-PIC framework

## 2.1The Vlasov-Poisson system and its flow map

We consider the Vlasov-Poisson system (in normalised units) for a electron distribution functionf​(t,x,v)≥0f(t,x,v)\geq 0in a domain[0,T]×L​𝕋d×ℝd[0,T]\times L\mathbb{T}^{d}\times\mathbb{R}^{d},
where the dimension isd∈ℕd\in\mathbb{N},
and whereL​𝕋d:=(ℝ/L​ℤ)dL\mathbb{T}^{d}:=(\mathbb{R}/L\mathbb{Z})^{d}denotes the periodic torus of side lengthLL.
It is governed by the system of equations∂tf+v⋅∇xf−∇xϕ⋅∇vf\displaystyle\partial_{t}f+v\cdot\nabla_{x}f-\nabla_{x}\phi\cdot\nabla_{v}f=0,\displaystyle=0,(1)−Δ​ϕ\displaystyle-\Delta\phi=ρ≔∫f​dv−1,\displaystyle=\rho\coloneqq\int f\,\mathrm{d}v-1,f​(t=0)\displaystyle f(t=0)=finit,\displaystyle=f_{\mathrm{init}},

where the second equation is a normalised Poisson equation for the electric
potentialϕ\phi, with a constant background ion density set to 1 so that the total charge
(assuming∬f​dx​dv=Ld\iint f\,\mathrm{d}x\mathrm{d}v=L^{d}) is zero.

The characteristic curves associated with (1) are the solutions
to the system of nonlinear differential equations,{X˙​(t)=V​(t),V˙​(t)=−∇xϕ​(t,X​(t)),\begin{dcases}\dot{X}(t)=V(t),\\
\dot{V}(t)=-\nabla_{x}\phi(t,X(t)),\end{dcases}(2)

defined fort≥s≥0t\geq s\geq 0and with initial condition(X,V)|t=s=(x,v)(X,V)|_{t=s}=(x,v). Assuming thatϕ\phiis sufficiently smooth, the system (2) has a unique solution and one can define
theforward flowΦs,t:(x,v)=(X​(s),V​(s))↦(X​(t),V​(t)),\Phi_{s,t}\colon(x,v)=(X(s),V(s))\mapsto(X(t),V(t)),

which maps phase-space positions at timessto
positions at timett. We recall that, for all timest≥s≥0t\geq s\geq 0,Φs,t\Phi_{s,t}is a diffeomorphism. The backward flow is denoted byΨs,t≔Φs,t−1\Psi_{s,t}\coloneqq\Phi_{s,t}^{-1}.
This backward flow gives a compact expression of the solution to (1), as evidenced by the following lemma.

## Lemma 2.1([36]).

The following two statements hold.
- •

Let0=t0<t1<⋯<tn=t0=t_{0}<t_{1}<\dots<t_{n}=tbe a partition of the time interval[0,t][0,t]. Then, the inverse flow map between times0andttis equal to the composition of the inverse flow maps over each subinterval:Ψ0,t=Ψt0,t1∘⋯∘Ψtn−1,tn.\Psi_{0,t}=\Psi_{t_{0},t_{1}}\circ\dots\circ\Psi_{t_{n-1},t_{n}}.
- •

The densityffat timettcan be expressed in terms of the initial densityfinitf_{\mathrm{init}}and the flow
map as:f​(t,x,v)=finit​(Ψ0,t​(x,v)).f(t,x,v)=f_{\mathrm{init}}\!\bigl(\Psi_{0,t}(x,v)\bigr).(3)

## 2.2Particle-in-cell approximation

In afull-fPIC method, the distribution function is approximated by a
weighted sum of shape functions centered onNpN_{p}numerical markerszkn=(xkn,vkn)∈ℝ2​dz_{k}^{n}=(x_{k}^{n},v_{k}^{n})\in\mathbb{R}^{2d}:fn​(z)=∑k=1Npwk​φε​(x−xkn)​δ​(v−vkn)≈f​(tn,z),f^{n}(z)=\sum_{k=1}^{N_{p}}w_{k}\,\varphi_{\varepsilon}(x-x_{k}^{n})\delta(v-v_{k}^{n})\approx f(t^{n},z),(4)

wherez=(x,v)z=(x,v), andφε\varphi_{\varepsilon}is a smooth shape function of integral one and widthε>0\varepsilon>0. For solving Vlasov-Poisson equations a classical choice is to use spline functions scaled withε=Δ​x\varepsilon=\Delta xthe step size of the
grid used for the Poisson solver. Specifically, we setφε​(x):=1εd​φ​(xε),\varphi_{\varepsilon}(x):=\frac{1}{\varepsilon^{d}}\varphi\left(\frac{x}{\varepsilon}\right),(5)

with a reference shape functionφ\varphidefined as a centered cardinal B-spline of degreepp:φ​(x)=∏i=1dBp​(xi),with support​[−p+12,p+12]d,\varphi(x)=\prod\limits_{i=1}^{d}B_{p}(x_{i}),\quad\mbox{ with support }\left[-\frac{p+1}{2},\frac{p+1}{2}\right]^{d},(6)

involving standard univariate B-splines defined recursively byB0​(x):=𝟏[−12,12]​(x)and​Bp​(x)=∫x−12x+12Bp−1​(y)​dy​for​p≥1.B_{0}(x):=\mathbf{1}_{\left[-\frac{1}{2},\frac{1}{2}\right]}(x)\quad\mbox{and }B_{p}(x)=\int_{x-\frac{1}{2}}^{x+\frac{1}{2}}B_{p-1}(y)\,\mathrm{d}y\mbox{ for }p\geq 1.

The weightswk=finit​(zk0)Np​g​(zk0)w_{k}=\frac{f_{\mathrm{init}}(z_{k}^{0})}{N_{p}\,g(z_{k}^{0})}(7)

are computed att=0t=0, withggthe sampling distribution of the initial markers, to be determined in the numerical experiments.
Each time step consists of
computing the velocity integral offnf^{n}needed to evaluate the potentialϕ\phiand the right-hand
side of (2), and pushing the markers by a discretisation of the characteristic
equations (2). If we consider an integral of the formI​(α)​(tn)=∫ℝ2​dα​(z)​f​(tn,z)​dzI(\alpha)(t^{n})=\int_{\mathbb{R}^{2d}}\alpha(z)\,f(t^{n},z)\,\mathrm{d}z(8)

and substitutef​(tn)f(t^{n})by its particle approximationfnf^{n}(in theε→0\varepsilon\to 0limit), we findIn​(α)=∫ℝ2​dα​(z)​fn​(z)​dz=∑k=1Npwk​α​(zkn)I^{n}(\alpha)=\int_{\mathbb{R}^{2d}}\alpha(z)\,f^{n}(z)\,\mathrm{d}z=\sum_{k=1}^{N_{p}}w_{k}\,\alpha(z_{k}^{n})(9)

Now, denote bygng^{n}the probability distribution of the markerszknz_{k}^{n},1≤k≤Np1\leq k\leq N_{p}, which is transported by the same characteristic flow asff: we havewk≈f​(tn,zkn)Np​gn​(zkn)w_{k}\approx\frac{f(t^{n},z_{k}^{n})}{N_{p}\,g^{n}(z_{k}^{n})}

henceIn​(a)​(x)≈1Np​∑k=1Npf​(tn,zkn)gn​(zkn)​α​(zkn).I^{n}(a)(x)\approx\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}\frac{f(t^{n},z_{k}^{n})}{g^{n}(z_{k}^{n})}\,\alpha(z_{k}^{n}).

The latter term can be seen as a Monte Carlo estimate: indeed
it is the empirical mean of the random variableXn​(z)=f​(tn,z)gn​(z)​α​(z)X^{n}(z)=\frac{f(t^{n},z)}{g^{n}(z)}\,\alpha(z)

whose expectation is the desired integralIn​(α)​(tn,x)I^{n}(\alpha)(t^{n},x).
The error scales as(σ2​[Xn]/Np)1/2(\sigma^{2}[X^{n}]/N_{p})^{\nicefrac{{1}}{{2}}}, with
the variance[4,18]σ2​[Xn]=𝔼​[(Xn)2]−𝔼​[Xn]2=∫ℝ2​df​(tn,z)2gn​(z)2​α​(z)2​gn​(z)​dz−I​(α)​(tn)2.\sigma^{2}[X^{n}]=\mathbb{E}[(X^{n})^{2}]-\mathbb{E}[X^{n}]^{2}=\int_{\mathbb{R}^{2d}}\frac{f(t^{n},z)^{2}}{g^{n}(z)^{2}}\,\alpha(z)^{2}\,g^{n}(z)\,\mathrm{d}z-I(\alpha)(t^{n})^{2}.(10)

This statistical error, or “noise”, can be reduced by
increasingNpN_{p}or by decreasingσ2​[Xn]\sigma^{2}[X^{n}]. In some applications,
notably gyrokinetic simulations[17], the required
accuracy demands a prohibitively large numberNpN_{p}of particles.
Hence, decreasing the variance is a better way to achieve a lower error in this case.
Theδ​f\delta\!fmethod, seen as acontrol variatetechnique in a Monte Carlo perspective[4], directly reducesσ2​[Xn]\sigma^{2}[X^{n}]without increasingNpN_{p}.
Observe that for computingρ​(tn)\rho(t^{n})at a given pointxx, one would takeα​(zn)=δ​(x−xn)\alpha(z^{n})=\delta(x-x^{n})in (8), or a smoothed version thereof to
avoid singularities in the above discussion: this motivates the use of the shape functionφε\varphi_{\varepsilon}in (4).
We refer to[37,18]for a detailed account of the
connection between PIC methods and Monte Carlo estimation.

For completeness, we summarise here the main steps of the standard full-ffPIC algorithm,
which will serve as a reference for theδ​f\delta\!fvariant introduced in the next section.
At each time stepnn, the algorithm proceeds as follows:
- 1.

Half-step in position.The positions of the markers are advanced by half a time step with periodicity:xkn+1/2=(xkn+Δ​t2​vkn)modL.x_{k}^{n+1/2}=\Bigl(x_{k}^{n}+\frac{\Delta t}{2}\,v_{k}^{n}\Bigr)\bmod L.
- 2.

Charge deposition.The charge density is assembled by depositing
the markers onto a grid of sizeΔ​x\Delta x:ρn+1/2​(x)=∑k=1Npwk​φΔ​x​(x−xkn+1/2),\rho^{n+1/2}(x)=\sum_{k=1}^{N_{p}}w_{k}\,\varphi_{\Delta x}(x-x_{k}^{n+1/2}),

whereφΔ​x\varphi_{\Delta x}is the shape functionφε\varphi_{\varepsilon}from (5) withε=Δ​x\varepsilon=\Delta x.
- 3.

Electric field computation.The Poisson equation−Δ​ϕn+1/2=ρn+1/2-\Delta\phi^{n+1/2}=\rho^{n+1/2}is solved spectrally using a
Fast Fourier Transform (FFT)-based solver on a space grid of sizeΔ​x\Delta x. The electric fieldEn+1/2=−∇ϕn+1/2E^{n+1/2}=-\nabla\phi^{n+1/2}is then interpolated back to
the particle positions using the same shape functionφΔ​x\varphi_{\Delta x}.
- 4.

Full step in velocity.The velocities are updated using the electric field:vkn+1=vkn+Δ​t​En+1/2​(xkn+1/2).v_{k}^{n+1}=v_{k}^{n}+\Delta t\,E^{n+1/2}(x_{k}^{n+1/2}).
- 5.

Half-step in position.The positions are advanced by half a time step with periodicity:xkn+1=(xkn+1/2+Δ​t2​vkn+1)modL.x_{k}^{n+1}=\Bigl(x_{k}^{n+1/2}+\frac{\Delta t}{2}\,v_{k}^{n+1}\Bigr)\bmod L.

The main differences with theδ​f\delta\!fmethod, described in the next section, are that the weightswkw_{k}are fixed throughout the simulation, and that the full velocity integral offnf^{n}is evaluated by a Monte Carlo approximation.

## 2.3Theδ​f\delta\!fmethod

The basic idea of theδ​f\delta\!fmethod is to reduce the amplitude of the Monte Carlo estimate (9) in the evaluation of the velocity integrals.
To achieve this goal the numerical distribution function is decomposed in two parts:f​(tn)=f0+δ​f​(tn)withδ​f​(tn):=f​(tn)−f0f(t^{n})=f_{0}+\delta\!f(t^{n})\qquad\text{ with }\quad\delta\!f(t^{n}):=f(t^{n})-f_{0}(11)

where the velocity integrals off0f_{0}are easy to compute, and onlyδ​f​(tn)\delta\!f(t^{n})is approximated by numerical particles.
For simplicity, we consider in this section the case wheref0f_{0}is constant in time.
A typical choice for suchf0f_{0}is a local Maxwellian, or an equilibrium of the system[26].

The integralsI​(tn,α)I(t^{n},\alpha)are then split accordingly,I​(tn,α)=∫ℝ2​dα​(z)​f0​(z)​dz⏟noiseless+∫ℝ2​dα​(z)​δ​f​(tn,z)​dz⏟Monte Carlo.I(t^{n},\alpha)=\underbrace{\int_{\mathbb{R}^{2d}}\alpha(z)f_{0}(z)\,\mathrm{d}z}_{\text{noiseless}}+\underbrace{\int_{\mathbb{R}^{2d}}\alpha(z)\delta\!f(t^{n},z)\,\mathrm{d}z}_{\text{Monte Carlo}}.(12)

Here the first term can be computed exactly, and the remainderδ​f​(tn)\delta\!f(t^{n})is
approximated by particlesδ​f​(tn,z)≈δ​fn​(z)≔∑k=1Npδ​wkn​φε​(x−xkn)​δ​(v−vkn),\delta\!f(t^{n},z)\approx\delta\!f^{n}(z)\coloneqq\sum_{k=1}^{N_{p}}\delta w_{k}^{n}\,\varphi_{\varepsilon}(x-x_{k}^{n})\delta(v-v_{k}^{n}),(13)

with weights given byδ​wkn≔finit​(zk0)−f0​(zkn)Np​g0​(zk0)≈f​(tn,zkn)−f0​(zkn)Np​gn​(zkn)=δ​f​(tn,zkn)Np​gn​(zkn)\delta w_{k}^{n}\coloneqq\frac{f_{\mathrm{init}}(z_{k}^{0})-f_{0}(z_{k}^{n})}{N_{p}g^{0}(z_{k}^{0})}\approx\frac{f(t^{n},z_{k}^{n})-f_{0}(z_{k}^{n})}{N_{p}g^{n}(z_{k}^{n})}=\frac{\delta\!f(t^{n},z_{k}^{n})}{N_{p}g^{n}(z_{k}^{n})}(14)

Substituting (13) and (14) into the second term of
(12) gives, analogously to (9),∫ℝ2​dα​(z)​δ​f​(tn,z)​dz≈∫ℝ2​dα​(z)​δ​fn​(z)​dz=1Np​∑k=1Npfinit​(zk0)−f0​(zkn)g​(zk0)​α​(zkn).\int_{\mathbb{R}^{2d}}\alpha(z)\delta\!f(t^{n},z)\,\mathrm{d}z\approx\int_{\mathbb{R}^{2d}}\alpha(z)\delta\!f^{n}(z)\,\mathrm{d}z=\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}\frac{f_{\mathrm{init}}(z_{k}^{0})-f_{0}(z_{k}^{n})}{g(z_{k}^{0})}\,\alpha(z_{k}^{n}).(15)

This sum has the same structure as (9), but withfinit​(zk0)f_{\mathrm{init}}(z_{k}^{0})replaced byfinit​(zk0)−f0​(zkn)f_{\mathrm{init}}(z_{k}^{0})-f_{0}(z_{k}^{n}). Its error still
scales asNp−1/2N_{p}^{-\nicefrac{{1}}{{2}}}, but with a prefactor proportional to the magnitude of the
weightsδ​wkn\delta w_{k}^{n}. As long asf0f_{0}closely tracksfnf^{n}, these weights remain
small and the noise is significantly reduced compared to the full-ffestimate
(9).
This approach comes at the cost of updating the bulk and the weights, which should be smaller than that of
increasing the number of particles to achieve the same noise reduction.

We summarise here the main steps of the staticδ​f\delta\!f-PIC algorithm,
and highlight the differences with respect to the full-ffPIC method.
This will serve as a direct reference for the Neuralδ​f\delta\!f-PIC method introduced inSection˜4.
At each time stepnn, the algorithm proceeds as follows:
- 1.

Half-step in position.Same as in the full-ffcase:xkn+1/2=(xkn+Δ​t2​vkn)modL.x_{k}^{n+1/2}=\Bigl(x_{k}^{n}+\frac{\Delta t}{2}\,v_{k}^{n}\Bigr)\bmod L.
- 2.

Weight update.The weights are updatedδ​wkn+1/2=finit​(xk0,vk0)−f0​(xkn+1/2,vkn)Np​g​(xk0,vk0).\delta w_{k}^{n+1/2}=\frac{f_{\mathrm{init}}(x_{k}^{0},v_{k}^{0})-f_{0}(x_{k}^{n+1/2},v_{k}^{n})}{N_{p}\,g(x_{k}^{0},v_{k}^{0})}.
- 3.

Charge deposition.The charge density is split into a noiseless bulk
contribution and a noisyδ​f\delta\!fcontribution,ρn+1/2​(x)=ρ0​(x)+∑k=1Npδ​wkn+1/2​φε​(x−xkn+1/2),\rho^{n+1/2}(x)=\rho_{0}(x)+\sum_{k=1}^{N_{p}}\delta w_{k}^{n+1/2}\,\varphi_{\varepsilon}(x-x_{k}^{n+1/2}),(16)

whereρ0​(x)=∫f0​(x,v)​dv\rho_{0}(x)=\int f_{0}(x,v)\,\mathrm{d}vmay be computed once and stored.
- 4.

Electric field computation.Same FFT-based spectral solver as in the full-ffcase, butEn+1/2E^{n+1/2}is computed using the charge density split in the two terms (16).
- 5.

Full step in velocity.Same as in the full-ffcase:vkn+1=vkn+Δ​t​En+1/2​(xkn+1/2).v_{k}^{n+1}=v_{k}^{n}+\Delta t\,E^{n+1/2}(x_{k}^{n+1/2}).
- 6.

Half-step in position.Same as in the full-ffcase:xkn+1=(xkn+1/2+Δ​t2​vkn+1)modL.x_{k}^{n+1}=\Bigl(x_{k}^{n+1/2}+\frac{\Delta t}{2}\,v_{k}^{n+1}\Bigr)\bmod L.

Compared to the full-ffalgorithm, the main differences are: (i) the charge density
is split into a precomputed bulk part and a particleδ​f\delta\!fpart,
and (ii) the particle weights are no longer fixed but evolve in time to track the
deviation offnf^{n}from the static bulkf0f_{0}.

## 2.4Static versus dynamic bulk densities

In the classicalδ​f\delta\!fapproach presented above, termed the static one, the bulk densityf0f_{0}is fixed throughout the simulation.
While simple and effective for near-equilibrium problems, this becomes inadequate when the distribution significantly evolves:
in this case, the weightsδ​wkn\delta w_{k}^{n}grow and the statistical noise becomes comparable to that of a full-ffPIC scheme.

A natural idea is then to also evolve the bulk densityf0f_{0}, albeit on a slower time-scale than that ofδ​f\delta\!f. This approach has been explored in related works (see for instance[12,1,25]and the references therein). A natural choice, especially when collisions are involved[12], is to assume that the bulkf0f_{0}has the form of a Maxwellian. The parameters (density, average velocity
and thermal velocity) of the backgroundf0f_{0}are then evolved according to fluid equations, with a closure computed from theδ​f\delta\!fpart. The simultaneous evolution ofδ​f\delta\!fand the fluid equations thus defines a self-consistent
hybrid fluid-kinetic procedure.

Another approach, presented in[13], is based on a
Forward-Backward Lagrangian (FBL) reconstruction of the bulk density.
At each remapping step, a collection of passive auxiliary markersz~j\tilde{z}_{j}are reset on a
Cartesian grid of spacingh∗h_{*}, i.e.,z~j:=j​h∗\tilde{z}_{j}:=jh_{*}forj∈ℤdj\in\mathbb{Z}^{d},
and then pushed forward by the PIC flow alongside the standard markers, in order
to track the forward characteristic flow.
The bulk density is then updated via a semi-Lagrangian step of the formf0n:=A∗​𝒯fbl​[𝐳~n]​f0m,f_{0}^{n}:=A_{*}\,\mathcal{T}_{\mathrm{fbl}}[\tilde{\mathbf{z}}^{n}]\,f_{0}^{m},

whereA∗A_{*}is a spline interpolation (or quasi-interpolation) operator on theh∗h_{*}grid, and𝒯fbl​[𝐳~n]\mathcal{T}_{\mathrm{fbl}}[\tilde{\mathbf{z}}^{n}]is a transport operator
that approximates the exact backward flow using a local quadratic inversion
of the auxiliary marker trajectories.
In low dimensions this approach has shown promising results,
however its cost becomes quickly expensive in high dimensions because of the isotropic nature of the backward flow reconstruction.

In this work, we propose to improve the foregoing FBL-δ​f\delta\!fmethod through two main modifications:
- •

First, we replace the local polynomial approximation of the backward flow by a neural network, which is trained on the numerical markers pushed by the underlying PIC code.
- •

Second, we distinguish between two “bulk densities”:
- (i)

afinerepresentation of the full solutionffobtained by composing the initial densityfinitf_{\mathrm{init}}with the backward flow approximated by a neural network, using again the Lagrangian formula (3), that isf​(t,x,v)=finit​(Ψ0,t​(x,v))f(t,x,v)=f_{\mathrm{init}}(\Psi_{0,t}(x,v)), and
- (ii)

acoarserepresentation, obtained by interpolating the fine one on a coarse grid of B-splines.
As the former one is easy to evaluate at any point in phase space but difficult to integrate in velocity due to the phase space filamentations, we use it to update the latter one, which is then used as a bulk density in theδ​f\delta\!fPIC steps.

The neural network that we use to approximate the backward flowΨ0,t\Psi_{0,t}will be detailed in the following section:
it will be trained on the numerical markers computed by the PIC code.
This allows us to compute an appropriate form forf0f_{0}without any assumption on the general shape of the bulk
and without introducing any auxiliary markers as in[13].
Furthermore, the approximation of the backward flow by a neural network can a priori handle very anisotropic flows.

## 3Symplectic neural networks

In this section, we explain the architecture of the neural network used to
approximate the backward flow. The characteristic flow of the Vlasov-Poisson
system is a symplectic map: its Jacobian matrixJΦJ_{\Phi}satisfiesJΦ⊤​Ω​JΦ=ΩJ_{\Phi}^{\top}\Omega J_{\Phi}=\Omega, whereΩ=(0I−I0)\Omega=\bigl(\begin{smallmatrix}0&I\\
-I&0\end{smallmatrix}\bigr)is the standard symplectic matrix.
It is therefore natural to approximate
it by a neural network that is symplectic by construction. We begin, inSection˜3.1, by recalling the
standard SympNet architecture[21].
Then, we describe inSection˜3.2the periodic variant used in our experiments.

## 3.1SympNet architecture

Symplectic neural networks were introduced in[21]as
networks that are symplectic by construction. Their architecture is motivated by the classical result that a symplectic mapΨ:ℝ2​d→ℝ2​d\Psi:\mathbb{R}^{2d}\to\mathbb{R}^{2d}can be approximated by a compositions of multipleshear mapsψup​(x,v)=(x+∇vT​(v)v),ψdown​(x,v)=(xv+∇xV​(x)),\psi_{\mathrm{up}}(x,v)=\begin{pmatrix}x+\nabla_{v}T(v)\\
v\end{pmatrix},\qquad\psi_{\mathrm{down}}(x,v)=\begin{pmatrix}x\\
v+\nabla_{x}V(x)\end{pmatrix},(17)

for scalar potentialsT:ℝd→ℝT:\mathbb{R}^{d}\to\mathbb{R}andV:ℝd→ℝV:\mathbb{R}^{d}\to\mathbb{R}.

These maps have a direct physical interpretation:ψup\psi_{\mathrm{up}}is the
exact unit-time flow of the purely kinetic HamiltonianHT​(x,v)=T​(v)H_{T}(x,v)=T(v), andψdown\psi_{\mathrm{down}}is the exact unit-time flow of the purely potential
HamiltonianHV​(x,v)=V​(x)H_{V}(x,v)=V(x). In particular, the compositionψup∘ψdown\psi_{\mathrm{up}}\circ\psi_{\mathrm{down}}with∇vT​(v)=Δ​t​v\nabla_{v}T(v)=\Delta t\,vand∇xV​(x)=Δ​t​∇xϕ​(x)\nabla_{x}V(x)=\Delta t\,\nabla_{x}\phi(x)is precisely the symplectic Euler
scheme for the Vlasov-Poisson HamiltonianH=|v|2/2+ϕ​(x)H=|v|^{2}/2+\phi(x).

In thegradient-based(SympNet) variant, the potentialsTTandVVare parametrized by shallow neural networks.
Such a neural network is defined by𝒩K,b:ℝd\displaystyle\mathcal{N}_{K,b}\colon\mathbb{R}^{d}→ℝd,\displaystyle\to\mathbb{R}^{d},x\displaystyle x↦𝟏⊤​Σ​(K​x+b),\displaystyle\mapsto\mathbf{1}^{\top}\Sigma(Kx+b),

and it is parameterized by its weights and biasesK∈ℝw×dK\in\mathbb{R}^{w\times d}andb∈ℝwb\in\mathbb{R}^{w}. The functionΣ​(s)\Sigma(s)is of the form∫0sσ\int_{0}^{s}\sigma, withσ:ℝ→ℝ\sigma\colon\mathbb{R}\to\mathbb{R}an activation function (such as a sigmoid or tanh). Classically, we also denote byΣ:ℝw→ℝw\Sigma\colon\mathbb{R}^{w}\to\mathbb{R}^{w}andσ:ℝw→ℝw\sigma\colon\mathbb{R}^{w}\to\mathbb{R}^{w}their elementwise extensions. The vector𝟏∈ℝw×1\mathbf{1}\in\mathbb{R}^{w\times 1}is the vector whose components are all equal to11.
Then, the potentials are defined by shallow networks asVK,b​(x)=𝒩K,b​(x)​and​TK,b​(v)=𝒩K,b​(v),V_{K,b}(x)=\mathcal{N}_{K,b}(x)\text{\quad and \quad}T_{K,b}(v)=\mathcal{N}_{K,b}(v),(18)

where we emphasize thatVK,bV_{K,b}andTK,bT_{K,b}have different weights and biasesKKandbbin practice.
Then, to computeψup\psi_{\mathrm{up}}andψdown\psi_{\mathrm{down}},
we compute the gradients ofVK,bV_{K,b}andTK,bT_{K,b}as∇xVK,b​(x)=K⊤​σ​(K​x+b)≕σ^K,b​(x)​and​∇vTK,b​(v)=K⊤​σ​(K​v+b)≕σ^K,b​(v).\nabla_{x}V_{K,b}(x)=K^{\top}\sigma(Kx+b)\eqqcolon\hat{\sigma}_{K,b}(x)\text{\quad and \quad}\nabla_{v}T_{K,b}(v)=K^{\top}\sigma(Kv+b)\eqqcolon\hat{\sigma}_{K,b}(v).

Thus,ψup\psi_{\mathrm{up}}andψdown\psi_{\mathrm{down}}readψup​(x,v)=(x+σ^K,b​(v)v)​and​ψdown​(x,v)=(xv+σ^K,b​(x)).\psi_{\mathrm{up}}(x,v)=\begin{pmatrix}x+\hat{\sigma}_{K,b}(v)\\
v\end{pmatrix}\text{\quad and \quad}\psi_{\mathrm{down}}(x,v)=\begin{pmatrix}x\\
v+\hat{\sigma}_{K,b}(x)\end{pmatrix}.

A SympNetΨθ\Psi_{\theta}of depth2​ℓ2\elland widthwwis finally defined as the compositionΨθ=ψupℓ∘ψdownℓ∘⋯∘ψup1∘ψdown1,\Psi_{\theta}=\psi_{\mathrm{up}}^{\ell}\circ\psi_{\mathrm{down}}^{\ell}\circ\cdots\circ\psi_{\mathrm{up}}^{1}\circ\psi_{\mathrm{down}}^{1},(19)

withθ=(Kj,bj)1≤j≤2​ℓ\theta=(K^{j},b^{j})_{1\leq j\leq 2\ell}the trainable parameters of the network. Being a composition of
symplectic maps,Ψθ\Psi_{\theta}is symplectic for any setθ\thetaof trainable parameters.

## Theorem 3.1(Universal approximation,[21, Theorem. 3.2]).

Any symplectic mapΨ:ℝ2​d→ℝ2​d\Psi:\mathbb{R}^{2d}\to\mathbb{R}^{2d}can be approximated arbitrarily
well in theC0C^{0}norm by a SympNet of the form (19), given
sufficient depth and width.

## Remark 3.2(SympNet as a learned symplectic integrator).

A SympNet of depthℓ\ellcan be understood as a symplectic splitting
integrator withℓ\ellsteps, where the potentials(Tj,Vj)(T^{j},V^{j})at each step
are learned from data rather than prescribed by the physics. The Störmer-Verlet
scheme forH=|v|2/2+ϕ​(x)H=|v|^{2}/2+\phi(x)is recovered as the special case whereℓ=2\ell=2andΨθ=ψdown2∘ψup2∘ψup1∘ψdown1,\Psi_{\theta}=\psi_{\mathrm{down}}^{2}\circ\psi_{\mathrm{up}}^{2}\circ\psi_{\mathrm{up}}^{1}\circ\psi_{\mathrm{down}}^{1},where the potentials are given as the physical ones instead of neural networks.

## 3.2Periodic SympNet

For the Vlasov-Poisson problem with spatial periodicityx∈L​𝕋dx\in L\mathbb{T}^{d}, the
characteristic flow satisfiesΦs,t​(x+L​ej,v)=Φs,t​(x,v)\Phi_{s,t}(x+Le_{j},v)=\Phi_{s,t}(x,v)for each canonical basis vectoreje_{j}. We encode this constraint into the
SympNet architecture by replacing the standard gradient module inψdown\psi_{\mathrm{down}}by aperiodic gradient module, and by introducing a modulo operator inψup\psi_{\mathrm{up}}.

To parametriseLL-periodic functions, a natural choice (see e.g.[27]) is to use a
one-hidden-layer network with a fixed trigonometric embedding as input features:x∈ℝd⟼(cos⁡(2​π​x/L)sin⁡(2​π​x/L))∈ℝ2​d.x\in\mathbb{R}^{d}\;\longmapsto\;\begin{pmatrix}\cos(2\pi x/L)\\
\sin(2\pi x/L)\end{pmatrix}\in\mathbb{R}^{2d}.(20)

This is a standard approach for learning periodic functions with neural
networks: the trigonometric embedding encodes the
periodicity directly into the input features, so any network built on top
of it is automaticallyLL-periodic.
A natural building block to parameterize aLL-periodic gradient module (to be used in a velocity shear map) is thenV~K1,K2,b1,b2​(x)=𝟏⊤​Σ​(K1​cos⁡(2​π​xL)+b1)+𝟏⊤​Σ​(K2​sin⁡(2​π​xL)+b2),\tilde{V}_{K_{1},K_{2},b_{1},b_{2}}(x)=\mathbf{1}^{\top}\Sigma\left(K_{1}\cos\left(\frac{2\pi x}{L}\right)+b_{1}\right)+\mathbf{1}^{\top}\Sigma\left(K_{2}\sin\left(\frac{2\pi x}{L}\right)+b_{2}\right),(21)

where the weights and biases areK1,K2∈ℝw×dK_{1},K_{2}\in\mathbb{R}^{w\times d}andb1,b2∈ℝwb_{1},b_{2}\in\mathbb{R}^{w},
and whereΣ​(s)=∫0sσ\Sigma(s)=\int_{0}^{s}\sigmaremains the antiderivative of an activation functionσ\sigma.
Since the embedding (20) isLL-periodic, so isV~K1,K2,b1,b2\tilde{V}_{K_{1},K_{2},b_{1},b_{2}},
for any values of the parameters and the activation function.

## Definition 3.3(Periodic gradient module).

A periodic gradient module is defined byσ~K1,K2,b1,b2=∇xV~K1,K2,b1,b2.\tilde{\sigma}_{K_{1},K_{2},b_{1},b_{2}}=\nabla_{x}\tilde{V}_{K_{1},K_{2},b_{1},b_{2}}.(22)

In other words, for allx∈ℝdx\in\mathbb{R}^{d},σ~K1,K2,b1,b2​(x)=\displaystyle\tilde{\sigma}_{K_{1},K_{2},b_{1},b_{2}}(x)=−2​πL​K1⊤​[σ​(K1​cos⁡(2​π​xL)+b1)⊙sin⁡(2​π​xL)]\displaystyle-\frac{2\pi}{L}\,K_{1}^{\top}\!\left[\sigma\left(K_{1}\cos\left(\frac{2\pi x}{L}\right)+b_{1}\right)\odot\sin\left(\frac{2\pi x}{L}\right)\right](23)+2​πL​K2⊤​[σ​(K2​sin⁡(2​π​xL)+b2)⊙cos⁡(2​π​xL)],\displaystyle+\frac{2\pi}{L}\,K_{2}^{\top}\!\left[\sigma\left(K_{2}\sin\left(\frac{2\pi x}{L}\right)+b_{2}\right)\odot\cos\left(\frac{2\pi x}{L}\right)\right],

where⊙\odotdenotes elementwise multiplication. SinceV~\tilde{V}isLL-periodic, so isσ~\tilde{\sigma}.

The symplecticity of the resulting shear map follows from the same argument as
in the non-periodic case.
Dropping the subscripts for clarity, sinceσ~=∇xV~\tilde{\sigma}=\nabla_{x}\tilde{V},
the Jacobian matrix of(x,v)↦ψ~down​(x,v)=(x,v+σ~​(x))(x,v)\mapsto\tilde{\psi}_{\mathrm{down}}(x,v)=\bigl(x,\;v+\tilde{\sigma}(x)\bigr)(24)

is lower triangular with unit diagonal.
Therefore,ψ~down\tilde{\psi}_{\mathrm{down}}is a symplectic map;
this result holds for all weights and biases(K1,K2,b1,b2)(K_{1},K_{2},b_{1},b_{2}).

To make sure that the position shear map isLL-periodic inxx, we introduce a modulo operation, and we defineψ~up​(x,v)=((x+σ^​(v))modL,v).\tilde{\psi}_{\mathrm{up}}(x,v)=\bigl((x+\hat{\sigma}(v))\bmod L,\;v\bigr).(25)

whereσ^\hat{\sigma}is the gradient module introduced in the non-periodic case.

## Definition 3.4(Periodic SympNet).

A periodic SympNet of depth2​ℓ2\ellis the compositionΨθ=ψ~upℓ∘ψ~downℓ∘⋯∘ψ~up1∘ψ~down1,\Psi_{\theta}=\tilde{\psi}_{\mathrm{up}}^{\ell}\circ\tilde{\psi}_{\mathrm{down}}^{\ell}\circ\cdots\circ\tilde{\psi}_{\mathrm{up}}^{1}\circ\tilde{\psi}_{\mathrm{down}}^{1},(26)

where eachψ~downj\tilde{\psi}_{\mathrm{down}}^{j}andψ~upj\tilde{\psi}_{\mathrm{up}}^{j}uses their own parameters(K1j,K2j,b1j,b2j)(K_{1}^{j},K_{2}^{j},b_{1}^{j},b_{2}^{j})and(Kj,bj)(K^{j},b^{j}), respectively.

The trainable parameters of the periodic SympNet are finally grouped in the vectorθ=(K1j,K2j,b1j,b2j,Kj,bj)1≤j≤ℓ.\theta=(K_{1}^{j},K_{2}^{j},b_{1}^{j},b_{2}^{j},K^{j},b^{j})_{1\leq j\leq\ell}.

Note that this vector is larger than the one corresponding to the traditional SympNets. The total number of parameters in this case is3​w​ℓ​(d+1)3w\ell(d+1).
Each factor is symplectic, soΨθ\Psi_{\theta}is symplectic for everyθ\theta,
andΨθ:L​𝕋d×ℝd→L​𝕋d×ℝd\Psi_{\theta}:L\mathbb{T}^{d}\times\mathbb{R}^{d}\to L\mathbb{T}^{d}\times\mathbb{R}^{d}is smooth.

## 4The Neuralδ​f\delta\!f-PIC algorithm

We finally describe our proposed Neuralδ​f\delta\!f-PIC scheme, combining periodic SympNets fromSection˜3with theδ​f\delta\!f-PIC scheme fromSection˜2.

## 4.1Algorithm overview

We recall that the bulk density is approximated by projecting a fine representation (involving a neural network flow) on a coarse spline grid.
This bulk density is updated everyNΨN_{\Psi}time steps.
The goal is then to compute, at each time stepnn, a density of the formfn=f0m+δ​fn,where​m=⌊nNΨ⌋.f^{n}=f_{0}^{m}+\delta\!f^{n},\text{\quad where \quad}m=\left\lfloor\frac{n}{N_{\Psi}}\right\rfloor.
- •

Theδ​f\delta\!fpart is updated at each time step. It involves computing the markers’ positions and velocities(xkn,vkn)(x_{k}^{n},v_{k}^{n}), and their weightsδ​wkn\delta w_{k}^{n}. It takes the form of (13).
- •

The bulk densityf0mf_{0}^{m}is updated everyNΨN_{\Psi}time steps, i.e., whenn=m​NΨn=mN_{\Psi}. It is updated by first computing a neural networkΨθm\Psi_{\theta^{m}}that is trained on data corresponding to particle pairs{(xkn,vkn),(xkn−NΨ,vkn−NΨ)}\{(x_{k}^{n},v_{k}^{n}),(x_{k}^{n-N_{\Psi}},v_{k}^{n-N_{\Psi}})\}at timestnt^{n}andtn−NΨt^{n-N_{\Psi}}. The fine representation is next expressed by composing the approximate backward flows and the initial distribution:f0m~=finit​(Ψθ1∘⋯∘Ψθm),\widetilde{f_{0}^{m}}=f_{\mathrm{init}}(\Psi_{\theta^{1}}\circ\dots\circ\Psi_{\theta^{m}}),(27)

which is then approximated on a coarse B-spline grid,f0m:=A∗​f0m~f_{0}^{m}:=A_{*}\widetilde{f_{0}^{m}}(28)

in order to update the velocity integrals and the weights in theδ​f\delta\!fparticle scheme.
Here,A∗A_{*}is a spline interpolation (or quasi-interpolation) operator: a simple choice is to takeA∗​f0m~​(x,v)=∑𝒊∈{1,…,Nx}d∑𝒋∈{1,…,Nv}df0m~​(x𝒊,v𝒋)​φΔ​x​(x−x𝒊)​φΔ​v​(v−v𝒋),A_{*}\widetilde{f_{0}^{m}}(x,v)=\sum_{{\bm{i}}\in\{1,\dots,N_{x}\}^{d}}\sum_{{\bm{j}}\in\{1,\dots,N_{v}\}^{d}}\widetilde{f_{0}^{m}}(x_{\bm{i}},v_{\bm{j}})\varphi_{\Delta x}(x-x_{\bm{i}})\varphi_{\Delta v}(v-v_{\bm{j}}),(29)

wherex𝒊x_{\bm{i}},v𝒋v_{\bm{j}}are the nodes of a cartesian spline grid withNxN_{x}(respectivelyNvN_{v}) points per
spatial (respectively velocity) dimension, andφΔ​x\varphi_{\Delta x},φΔ​v\varphi_{\Delta v}are B-splines on these respective grids. Note that (29) corresponds to a smoothing of the piecewise interpolation off0m~\widetilde{f_{0}^{m}}on the coarse grid. In practice we have used cubic splines to ensure a smooth bulk density.

The particle pusher and the
Poisson solver remain standard components[9]: a leap-frog
(Strang splitting) scheme advances the markers at the fine timescaleΔ​t\Delta t,
and a spectral FFT-based solver computes the self-consistent electric field.
The novel contribution of this work is the dynamic update of the bulk densityf0mf_{0}^{m}using symplectic neural networks, which are trained on the particle trajectories to
approximate the backward characteristic flow.
The proposed algorithm is illustrated onFigure˜1.ttΔ​t\Delta t++++++++bulk(f0f_{0})newbulknewbulknewbulknewbulk⋯\cdots⋯\cdotsPIC⋯\cdots⋯\cdotsNΨ​Δ​tN_{\Psi}\Delta tNΨ​Δ​tN_{\Psi}\Delta tNΨ​Δ​tN_{\Psi}\Delta tFigure 1:The Neuralδ​f\delta\!falgorithm. Particles are pushed by a PIC scheme
(blue arrows), and after everyNΨN_{\Psi}time steps, the bulk densityf0f_{0}is updated by
first computing a new fine representationf0~\widetilde{f_{0}}which composesfinitf_{\mathrm{init}}with a neural backward flow (a SympNet trained on the particles’ positions at two given times), and approximating this fine representation on a coarse spline grid
as described in (27)–(28).
Note that when an incremental training strategy is used, a given flow network may be reused over different time intervals of increasing size (not pictured here).

## 4.2Incremental training of the neural flows.

Above we have considered for simplicity that each flow of the formΨ[m​Δ​tΨ,(m+1)​Δ​tΨ]\Psi_{[m\Delta t_{\Psi},(m+1)\Delta t_{\Psi}]}, withΔ​tΨ=NΨ​Δ​t\Delta t_{\Psi}=N_{\Psi}\Delta t, was approximated by a distinct neural networkΨθm+1\Psi_{\theta^{m+1}}trained on the particle pairs{(xkm​NΨ,vkm​NΨ),(xk(m+1)​NΨ,vk(m+1)​NΨ)}k=1Np\{(x_{k}^{mN_{\Psi}},v_{k}^{mN_{\Psi}}),(x_{k}^{(m+1)N_{\Psi}},v_{k}^{(m+1)N_{\Psi}})\}_{k=1}^{N_{p}}.
In practice however, it often happen that the previous network, sayΨθm\Psi_{\theta^{m}}, which has been trained for the flow over the time interval[(m−1)​Δ​tΨ,m​Δ​tΨ][(m-1)\Delta t_{\Psi},m\Delta t_{\Psi}], is also able to accurately approximate the flow over the larger time interval[(m−1)​Δ​tΨ,(m+1)​Δ​tΨ][(m-1)\Delta t_{\Psi},(m+1)\Delta t_{\Psi}].
In such a case, a natural strategy is to reuse this networkΨθm\Psi_{\theta^{m}}with its current weightsθm\theta^{m}as a warm start, and train it on the new data corresponding to the extended time interval, that is on the particle pairs{(xk(m−1)​NΨ,vk(m−1)​NΨ),(xk(m+1)​NΨ,vk(m+1)​NΨ)}k=1Np\{(x_{k}^{(m-1)N_{\Psi}},v_{k}^{(m-1)N_{\Psi}}),(x_{k}^{(m+1)N_{\Psi}},v_{k}^{(m+1)N_{\Psi}})\}_{k=1}^{N_{p}}.
We still denote the resulting weights byθm+1\theta^{m+1}, but the corresponding networkΨθm+1\Psi_{\theta^{m+1}}now approximates the flow over a larger time interval.
In terms of network flows, this approach corresponds to replacingΨθm∘Ψθm+1↝Ψθm+1\Psi_{\theta^{m}}\circ\Psi_{\theta^{m+1}}\rightsquigarrow\Psi_{\theta^{m+1}}(30)

and discarding the previous parametersθm\theta^{m}since they are no longer needed.
Compared to training a new network for aΔ​tΨ\Delta t_{\Psi}time interval, this approach saves computational resources and avoids composing several network flows (which may result in a loss of accuracy) where a single one can be used.
We call this strategy anincremental trainingof the neural flows.
In terms of non-linear approximation of complex flows, this approach is similar to a preconditioning. It may also be seen as a form ofcurriculum learning[7,39], where the training data is presented in a sequence of increasing complexity.

In practice we apply this strategy with a prescribed toleranceεtol\varepsilon_{\mathrm{tol}}. At each bulk update step(m+1)(m+1), we first try to extend the time interval covered by the current network.
If the approximation loss reaches the tolerance then this updated network is used for the larger time interval, otherwise the
previous network (with its weightsθm\theta^{m}) is kept and a new network is trained (from scratch) for the last sub-interval, i.e.,[m​Δ​tΨ,(m+1)​Δ​tΨ][m\Delta t_{\Psi},(m+1)\Delta t_{\Psi}].
This adaptive strategy balances the competing goals of minimising the number of stored networks while ensuring that each network remains accurately trained.

## 4.3Initialisation of the markers and the bulk density.

The initialisation consists in drawingNpN_{p}numerical markers in phase space,(xk0,vk0)∈L​𝕋d×ℝd,k=1,…,Np,(x_{k}^{0},v_{k}^{0})\in L\mathbb{T}^{d}\times\mathbb{R}^{d},\quad k=1,\dots,N_{p},(31)

from a sampling distributiongg. In all our experiments we use the Gaussian densityg​(x,v)=1Vtot​1(2​π​vth2)d/2​e−|v|2/(2​vth2),g(x,v)=\frac{1}{V_{\mathrm{tot}}}\frac{1}{(2\pi v_{\mathrm{th}}^{2})^{d/2}}\,e^{-|v|^{2}/(2v_{\mathrm{th}}^{2})},(32)

whereVtot=LdV_{\mathrm{tot}}=L^{d}is the volume of the spatial domain andvth>0v_{\mathrm{th}}>0is a thermal velocity chosen to cover the support offinitf_{\mathrm{init}}in velocity space.
Setting thenf00~=finit\widetilde{f_{0}^{0}}=f_{\mathrm{init}}, the initial bulk density is computed on the coarse spline grid asf00=A∗​finit,f_{0}^{0}=A_{*}f_{\mathrm{init}},(33)

whereA∗A_{*}is the spline quasi-interpolation operator defined in (29).

## 4.4δ​f\delta\!f-PIC phase

Each PIC step with indexn∈ℕn\in\mathbb{N}advances the markers from timetnt^{n}totn+1=tn+Δ​tt^{n+1}=t^{n}+\Delta t,
using a standard leap-frog (Strang splitting) scheme. As above we letNΨ>0N_{\Psi}>0be the number of PIC steps between two updates of the neural network representing the backward flow, and we denote bym=⌊nNΨ⌋m=\lfloor\frac{n}{N_{\Psi}}\rfloorthe index of the last bulk update.
At the beginning of the PIC stepnnwe thus assume that the corresponding bulk densityf0m=A∗​f0m~f_{0}^{m}=A_{*}\widetilde{f_{0}^{m}}(which is frozen until the next bulk update)
has been computed and stored on the coarse spline grid.
Accordingly, its charge densityρ0m​(x)=∫ℝdf0m​(x,v)​dv=∑𝒊∈{1,…,Nx}df0m~​(x𝒊)​φΔ​x​(x−x𝒊),\rho_{0}^{m}(x)=\int_{\mathbb{R}^{d}}f_{0}^{m}(x,v)\,\mathrm{d}v=\sum_{{\bm{i}}\in\{1,\dots,N_{x}\}^{d}}\widetilde{f_{0}^{m}}(x_{\bm{i}})\varphi_{\Delta x}(x-x_{\bm{i}}),(34)

may be computed exactly and stored as well.
- 1.

Half-step in position.We start with a predictive half-step, updating the positions of the particles:xkn+1/2=(xkn+Δ​t2​vkn)modL,x_{k}^{n+1/2}=\Bigl(x_{k}^{n}+\frac{\Delta t}{2}\,v_{k}^{n}\Bigr)\bmod L,(35)

where the modulo operation enforces the periodic boundary conditionx∈L​𝕋dx\in L\mathbb{T}^{d}.
- 2.

Weight update.The weights of theδ​f\delta\!fpart are updated asδ​wkn+1/2=finit​(xk0,vk0)−f0m​(xkn+1/2,vkn)Np​g​(xk0,vk0).\delta w_{k}^{n+1/2}=\frac{f_{\mathrm{init}}(x_{k}^{0},v_{k}^{0})-f_{0}^{m}(x_{k}^{n+1/2},v_{k}^{n})}{N_{p}\,g(x_{k}^{0},v_{k}^{0})}.(36)
- 3.

Electric field computation.The total charge density at the half-step is the sum of the exact contribution (34)
of the spline bulk and the Monte Carlo evaluation of theδ​f\delta\!fpart, corresponding to (15)
withα​(zk)=φΔ​x​(x−xk)\alpha(z_{k})=\varphi_{\Delta x}(x-x_{k}), that is:ρn+1/2​(x)=ρ0m​(x)+∑k=1Npδ​wkn+1/2​φΔ​x​(x−xkn+1/2).\rho^{n+1/2}(x)=\rho_{0}^{m}(x)+\sum_{k=1}^{N_{p}}\delta w_{k}^{n+1/2}\,\varphi_{\Delta x}\!\Bigl(x-x_{k}^{n+1/2}\Bigr).(37)

The Poisson equation−Δ​ϕn+1/2=ρn+1/2-\Delta\phi^{n+1/2}=\rho^{n+1/2}is then solved with a spectral, FFT-based scheme
and the electric fieldEn+1/2≈−∇ϕn+1/2E^{n+1/2}\approx-\nabla\phi^{n+1/2}is interpolated from the resulting point values, using the same shape functionφΔ​x\varphi_{\Delta x}.
We write this entire procedure asEn+1/2=ℱ​((xkn+1/2,δ​wkn+1/2)1≤k≤Np,ρ0m).E^{n+1/2}=\mathcal{F}((x_{k}^{n+1/2},\delta w_{k}^{n+1/2})_{1\leq k\leq N_{p}},\rho_{0}^{m}).
- 4.

Full step in velocity, half-step in position.Equipped with the electric field and positions at the half-step, we complete the update of the velocity and position as follows:vkn+1=vkn+Δ​t​En+1/2​(xkn+1/2),xkn+1=(xkn+1/2+Δ​t2​vkn+1)modL.v_{k}^{n+1}=v_{k}^{n}+\Delta t\,E^{n+1/2}\Bigl(x_{k}^{n+1/2}\Bigr),\qquad\qquad x_{k}^{n+1}=\Bigl(x_{k}^{n+1/2}+\frac{\Delta t}{2}\,v_{k}^{n+1}\Bigr)\bmod L.

## 4.5Update of the neural flow and the bulk density

## Training of the backward flow.

Recall thatNΨ>0N_{\Psi}>0is the number of PIC substeps between two updates of the neural flow network.
According to the incremental training strategy described in Section4.2, at each update stepm+1m+1we first consider the last networkΨθm\Psi_{\theta^{m}}which has been trained to approximate the backward flow over a time interval of the form[r​Δ​tψ,m​Δ​tψ][r\Delta t_{\psi},m\Delta t_{\psi}]withr<mr<m, and train it for the flow corresponding to the
larger time interval[r​Δ​tψ,(m+1)​Δ​tψ][r\Delta t_{\psi},(m+1)\Delta t_{\psi}].

For this we use the particle pairs{(xkr​NΨ,vkr​NΨ),(xk(m+1)​NΨ,vk(m+1)​NΨ)}k=1Np\{(x_{k}^{rN_{\Psi}},v_{k}^{rN_{\Psi}}),(x_{k}^{(m+1)N_{\Psi}},v_{k}^{(m+1)N_{\Psi}})\}_{k=1}^{N_{p}}as training data, and a loss function defined asℒ​(θ)=1Np​∑k=1Np‖Ψθ​(xk(m+1)​NΨ,vk(m+1)​NΨ)−(xkr​NΨ,vkr​NΨ)‖2,\mathcal{L}(\theta)=\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}\bigl\|\Psi_{\theta}(x_{k}^{(m+1)N_{\Psi}},v_{k}^{(m+1)N_{\Psi}})-(x_{k}^{rN_{\Psi}},v_{k}^{rN_{\Psi}})\bigr\|^{2},(38)

so that the resulting networkΨθm+1\Psi_{\theta^{m+1}}is a good approximation of the associated backward flow.
If the optimisation fails to reach the prescribed toleranceεtol\varepsilon_{\mathrm{tol}}, then we train a new network
for the last time interval only, corresponding to the same loss function but withr=mr=m.
The minimisation of (38) is performed in two steps: the first step use the classical optimiser Adam[22], then we switch to thenatural gradientmethod[2], which preconditions the
gradient by the Fisher information matrix of the network. Compared to
standard gradient descent, the natural gradient accounts for the Riemannian
geometry of the parameter space and typically achieves better convergence in
practice[28]. Here, since the loss function(38)corresponds to aL2L^{2}minimisation, the natural gradient method is equivalent to the Gauss-Newton algorithm.
Using this algorithm enables much more precise training,
but at the cost of solving an ill-conditioned linear system with a full matrix
at each iteration of the optimisation process.

## Bulk density update.

Given a composed backward flow at timetm​NΨt^{mN_{\Psi}}, of the formΨm=Ψθr∘⋯∘Ψθm\Psi^{m}=\Psi_{\theta^{r}}\circ\cdots\circ\Psi_{\theta^{m}}(39)

(the precise number of networks in the composition depending on the convergence of the sucessive trainings in the adaptive incremental strategy,
see Section4.2), the bulk density at update stepmmis computed in two steps:
First, the fine representation is defined by the Lagrangian transport formulaf0m~​(x,v)=finit​(Ψm​(x,v)),\widetilde{f_{0}^{m}}(x,v)=f_{\mathrm{init}}\!\bigl(\Psi^{m}(x,v)\bigr),(40)

and it is then approximated on the coarse B-spline grid throughf0m=A∗​f0m~f_{0}^{m}=A_{*}\widetilde{f_{0}^{m}}

as described in (29). The resulting bulk density is then used in the followingNΨN_{\Psi}PIC steps, until the next update of the neural flow.

We note that some structural properties readily follow from our approach:
- •

Positivity: we havef0m~​(x,v)≥0andf0m​(x,v)≥0\widetilde{f_{0}^{m}}(x,v)\geq 0\qquad\text{ and }\qquad f_{0}^{m}(x,v)\geq 0

as a result offinit≥0f_{\mathrm{init}}\geq 0(for the first property) and the spline nodal formula (29) (for the second one).
- •

Mass conservation: using a change of variables and the fact that
a symplectic map preserves the volume in phase space, we have∫ℝd∫L​𝕋df0m~​(x,v)​dx​dv=∫ℝd∫L​𝕋dfinit​(x,v)​dx​dv.\int_{\mathbb{R}^{d}}\int_{L\mathbb{T}^{d}}\widetilde{f_{0}^{m}}(x,v)\,\mathrm{d}x\,\mathrm{d}v=\int_{\mathbb{R}^{d}}\int_{L\mathbb{T}^{d}}f_{\mathrm{init}}(x,v)\,\mathrm{d}x\,\mathrm{d}v.(41)

We note that the mass conservation property does not a priori hold for the spline bulkf0mf_{0}^{m}, but since the latter
is periodically recomputed fromf0m~\widetilde{f_{0}^{m}}, we do not expect large deviations over long time ranges.
Moreover a rescaling of the spline coefficients in (29) is always possible if that should be an issue.
Finally we emphasize that the above structural properties hold foranyvalues of the parametersθr,…,θm\theta^{r},\ldots,\theta^{m}, regardless of training accuracy.

## Remark 4.1.

In long-time simulations, the number of flow networks involved in the composition (39)
can increase significantly, together with the evaluation cost. One mitigation strategy is to periodically project the fine density
on a space of neural networks: everyK<mK<mbulk updates, train a MLPfμf_{\mu}to approximate the full composed mapf0m~\widetilde{f_{0}^{m}}from a sampling of the phase space, and reset the list of learned backward flows. This resets the evaluation
cost back to𝒪​(ℓ​w)\mathcal{O}(\ell w)everyKKbulk updates. In the numerical experiments
reported in this manuscript, the number of bulk updates is small enough that
the cost growth is not a bottleneck, as the cost of training the different networks remains by far the main computational task.
Conceptually, such a reset plays the role of a remapping in the semi-Lagrangian sense: a re-approximation of the solution that discards the accumulated flow and thus loses some information. In this respect, our method is onlyweaklysemi-Lagrangian: in contrast with standard semi-Lagrangian schemes, which remap at every time step, this operation would only be needed in long time simulations. The Characteristic Mapping Method[24]is weakly semi-Lagrangian in the same spirit, the flow map being built over long time intervals rather than remapped at every step.Algorithm 1Summary offull-f,delta-fandneural-delta-fschemes1:Initialisation:Draw markers(xk0,vk0)(x_{k}^{0},v_{k}^{0})fromgg;iffull-f: setf00=0f_{0}^{0}=0,else:f00=finitf_{0}^{0}=f_{\mathrm{init}}or a spline approximation of it.iffull-f: setδ​wk=finit​(xk0,vk0)Np​g​(xk0,vk0)\delta w_{k}=\frac{f_{\mathrm{init}}(x_{k}^{0},v_{k}^{0})}{N_{p}\,g(x_{k}^{0},v_{k}^{0})}Computeρ00=∫f00​𝑑v\rho_{0}^{0}=\int f_{0}^{0}dv.2:forn=0,1,2,…n=0,1,2,\ldotsdo3:// Particles update4:xkn+1/2=(xkn+Δ​t2​vkn)modLx_{k}^{n+1/2}=(x_{k}^{n}+\frac{\Delta t}{2}v_{k}^{n})\bmod L5:Assemble field:6:iffull-f: Setδ​wkn+1/2=δ​wk\delta w_{k}^{n+1/2}=\delta w_{k}:else:δ​wkn+1/2=finit​(xk0,vk0)−f0m​(xkn+1/2,vkn)Np​g​(xk0,vk0)\delta w_{k}^{n+1/2}=\frac{f_{\mathrm{init}}(x_{k}^{0},v_{k}^{0})-f_{0}^{m}(x_{k}^{n+1/2},v_{k}^{n})}{N_{p}\,g(x_{k}^{0},v_{k}^{0})};7:ComputeEn+1/2=ℱ​(xn+1/2,δ​wn+1/2,ρ0m)E^{n+1/2}=\mathcal{F}(x^{n+1/2},\delta w^{n+1/2},\rho_{0}^{m})via (37)8:vkn+1=vkn+Δ​t​En+1/2​(xkn+1/2)v_{k}^{n+1}=v_{k}^{n}+\Delta t\,E^{n+1/2}(x_{k}^{n+1/2})9:xkn+1=(xkn+1/2+Δ​t2​vkn+1)modLx_{k}^{n+1}=(x_{k}^{n+1/2}+\frac{\Delta t}{2}v_{k}^{n+1})\bmod L10:ifneural-delta-fandn+1=(m+1)​NΨn+1=(m+1){N_{\Psi}}then11:// Bulk update12:TrainΨθm+1\Psi_{\theta^{m+1}}by minimising (38)
using natural gradient descent13:Update the fine representation of the density:f0m+1~=f0m~∘Ψθm+1\widetilde{f_{0}^{m+1}}=\widetilde{f_{0}^{m}}\circ\Psi_{\theta^{m+1}}14:Approximate it on the coarse spline grid:f0m+1=A∗​f0m+1~f_{0}^{m+1}=A_{*}\widetilde{f_{0}^{m+1}}15:Computeρ0m+1=∫f0m+1​𝑑v\rho_{0}^{m+1}=\int f_{0}^{m+1}dvand store on spatial grid16:else17:Setf0m+1=f00f_{0}^{m+1}=f_{0}^{0}andρ0m+1=ρ00\rho_{0}^{m+1}=\rho_{0}^{0}18:endif19:endfor

## 5Numerical results

In this section we perform several experiments to assess the accuracy of our neuralδ​f\delta\!f-PIC solver.
To this end we run several Vlasov-Poisson test cases in 1D1V and 3D3V, and compare the results with
a standardδ​f\delta\!f-PIC scheme which relies on a static bulk density as described above.

These test-cases have been chosen because they are standard, however one shoud keep in mind that their solutions do not deviate very much from the initial distribution, so that a standardδ​f\delta\!f-PIC scheme with static bulk density is expected to perform well already. The goal of our experiments is thus to show that the neuralδ​f\delta\!f-PIC scheme performs at least as well as a standardδ​f\delta\!f-PIC scheme, while being able to adapt to more complex situations where the bulk density evolves significantly in time.
In all experiments, the particle pusher uses a Strang splitting scheme and a spectral Poisson solver with 32 grid cells per direction,
and in the neuralδ​f\delta\!fscheme we represent our bulk densities with cubic B-splines on a grid of 32 cells per direction.
We also compare our results with backward semi-Lagrangian (BSL) schemes which compute accurate solutions at the price of meshing the phase space with fine grids: In 1D1V, we use a standard BSL scheme with directional splitting on a fine1024×10241024\times 1024phase-space grid, and in 3D3V we use the BSL6D code presented in[35].

The hyperparameters of the networks are chosen as follows. All SympNets we use here have the same architecture, withℓ=10\ell=10layers of widthw=8w=8withtanh\tanhas activation functions. The total number of parameters per network is then 480 in 1D1V and 960 in 3D3V (we recall that for the periodic Sympnet proposed in this paper, the total number of parameters is3​w​ℓ​(d+1)3w\ell(d+1)).
To train each network, we use the Adam optimizer for 200 epochs, followed by 500 steps of natural gradient descent in 1D1V and 1000 steps of natural gradient in 3D3V. Furthermore, we fixed a tolerance ofεtol=10−5\varepsilon_{\mathrm{tol}}=10^{-5}for the curriculum learning of the networks.

In our experiments, the results turned out to be fairly robust with respect to the network architecture and to the training hyperparameters, as long as the networks are expressive enough and trained for sufficiently many epochs. The parameter that genuinely influences the results isNΨN_{\Psi}, the number of time steps between two consecutive trainings. It should be large enough to keep the number of trainings, and hence the computational cost, moderate, yet small enough so that the marker displacement between two trainings remains not too large to be accurately learned by the network.

We emphasize that the phase-space density we show in all the numerical experiments is the fine bulk densityf0m~\widetilde{f_{0}^{m}}.

## 5.1Numerical study of flow learning

Before investigating the performance of our neuralδ​f\delta\!f-PIC scheme, we investigate the ability of periodic SympNets to learn a given characteristic flow of the Vlasov-Poisson system.

In this section we consider a flow associated with the 1D1V two-stream instability described inSection˜5.2.1below,
between two timesT0=30T_{0}=30andT1=35T_{1}=35, chosen somewhat arbitrarily. Concretely, we first compute a discrete solutionf​(T0)f(T_{0})at timeT0T_{0}by using a grid-based BSL scheme, and next use this solution as the initial condition of a standard PIC scheme (by drawing particles with a Maxwellian probability and weighting them according tof​(T0)f(T_{0})) that we run between timesT0T_{0}andT0+tT_{0}+t, fort∈{1,2,…,5}t\in\{1,2,\ldots,5\}.
The resulting sets of particle coordinates for the timesT0T_{0}andttare then decomposed in two sets of equal size: the first half is used as training data for periodic SympNets of various depths and widths to approximate the backward flowΨ[T0,T1]\Psi_{[T_{0},T_{1}]}as described above, and the second half is used as a test set to evaluate the performance of the trained networks.

InFigure˜2we illustrate the characteristic flowsΨ[T0,T0+t]\Psi_{[T_{0},T_{0}+t]}for different timestt, together with the densitiesf​(t)f(t)obtained by advancing the densityf​(T0)f(T_{0})using a fine grid BSL scheme. Here the flow is illustrated by plotting the isolines of two passive distributions transported by the BSL scheme, starting from the affine distributionsfx=xf_{x}=xandfv=vf_{v}=vat timeT0T_{0}:
the resulting isolines show the grid being transported forward by the flow and the evolving complexity as time increases, with the development of fine structures in phase space.
Note that close to the maximal and minimal velocities the BSL scheme uses a (non-physical) periodic boundary condition which results in strong gradients in the transported grid isolines – this is of little importance for the transport of density, as the latter vanishes close to these extremal velocities.Figure 2:Numerical study fromSection˜5.1: Characteristic flows (top row) and densities (bottom row) corresponding to the 1D1V two-stream instability solved by the BSL scheme between timesT0=30T_{0}=30andT1=35T_{1}=35. The left plots correspond to timeT0T_{0}, the middle plots to timeT0+3T_{0}+3and the right plots to timeT1T_{1}.

InFigure˜3we show the densities transported by the PIC scheme, obtained by smoothing each particle with cubic B-splines
in both thexxandvvdirections, as in (5). We also plot the isolines of the passive distributionsfx=xf_{x}=xandfv=vf_{v}=vas transported by the PIC scheme (using the
transported particles with new weights associated with these distributions).Figure 3:Numerical study fromSection˜5.1: Visualisation of the characteristic flows (top) and densities (bottom) associated with a PIC approximation of the two-stream instability between timesT0=30T_{0}=30andT1=35T_{1}=35withN=5000N=5000particles. Here the flows and the densities are visualized by evaluating
smoothed particle distributions with appropriate weights, as described in the text.

InFigure˜4we then plot the quadratic flow errors obtained by SympNets of different sizes (width and depth), using different numbers of training epochs (as indicated) and different training strategies. Here all the errors correspond to the training of the flowΨ[T0,T1]\Psi_{[T_{0},T_{1}]}, but in the left plots we use a direct training strategy (approximating directly the flow on the time range[T0,T1][T_{0},T_{1}]), while in the right plots we use an incremental training strategy (approximating the flow on the time range[T0,T0+1][T_{0},T_{0}+1], then[T0,T0+2][T_{0},T_{0}+2]starting from the previously trained model, and so on until[T0,T1][T_{0},T_{1}]).
The top row corresponds to a total of 600 Adam and 600 natural gradient steps, while the bottom row corresponds to 600 Adam and 900 natural gradient steps: in the direct strategy we use all these epochs to train the flow on the whole time interval[T0,T1][T_{0},T_{1}], while in the incremental strategy we use a budget of 100 Adam and 100 (resp. 150) natural gradient steps when training for the flows on[T0,T0+t][T_{0},T_{0}+t]witht∈{1,…​4}t\in\{1,\dots 4\}, and use the remaining budget of 200 Adam and 200 (resp. 300) natural gradient steps for the last training on[T0,T1][T_{0},T_{1}].
Finally, for each training strategy and number of epochs, we show on the left the quadratic errors measured on the training set, and on the right the quadratic errors measured on the test set. From these plots we see that the incremental training strategy yields more stable results: a monotonic convergence as the number of layers increases (which is not the case for the direct strategy, a sign that larger networks are harder to train in a direct manner), and very good agreement between the errors measured on the training and testing datasets (which again is not the case with the direct strategy, a sign that the latter is overfitting). We also note that increasing the number of epochs does not significantly improve the results, which indicates that the networks are able to learn the flow with a relatively small number of epochs.(a)Direct training, 600 Adam and 600 natural gradient steps(b)Incremental training, 600 Adam and 600 natural gradient steps(c)Direct training, 600 Adam and 900 natural gradient steps(d)Incremental training, 600 Adam and 900 natural gradient stepsFigure 4:Numerical study fromSection˜5.1: Quadratic errors of the flows learned by networks of different widths and depths,
using a direct training strategy for the left panels ((a) and (c))
and an incremental training strategy for the right panels ((b) and (d)).
For each case, we show two plots: the left ones correspond to the errors measured on the training dataset while the right ones to a set of test particles not used in the training. For each network the errors have been averaged over 10 training runs in order to take the variability of the training process into account.

InFigure˜5we then show the trained flows and associated densities obtained by a SympNet of widthw=8w=8and depthℓ=14\ell=14trained with the incremental strategy. Here the plots are obtained in a similar way as forFigure˜2, by transporting the isolines of the passive distributionsfx=xf_{x}=xandfv=vf_{v}=v(to visualize the flow) and the densityf​(T0)f(T_{0})(to visualize the densityf​(T0+t)f(T_{0}+t)) with the trained flow. These results may be compared to the ones of the reference BSL scheme inFigure˜2, keeping in mind that they are obtained by learning the flow using a set of particles of the same resolution as the one used inFigure˜3.Figure 5:Numerical study fromSection˜5.1: Top: characteristic flows learned by a SympNet of widthw=8w=8and depthℓ=14\ell=14using
a training dataset of 5000 particles as represented inFigure˜3. Bottom: densities obtained by transporting the initial density with the learned flow.

## 5.21D1V test cases

## 5.2.11D1V two-stream instability

Our first test is a typical two-stream instability in 1D1V. The initial condition readsfinit​(x,v)=(1+ε​cos⁡(k​x))​12​2​π​(e−(v−v0)2/2+e−(v+v0)2/2),f_{\mathrm{init}}(x,v)=(1+\varepsilon\cos(kx))\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v-v_{0})^{2}/2}+e^{-(v+v_{0})^{2}/2}\bigr),(42)

withε=0.05\varepsilon=0.05,k=0.3k=0.3andv0=3v_{0}=3. In this situation, two beams with opposite velocities interact. This eventually leads to an instability, creating thin phase-space
filaments. The computational domain is[0,2​π/k]×[−9,9].[0,2\pi/k]\times[-9,9].We useNp=104N_{p}=10^{4}particles, the time
stepΔ​t=0.05\Delta t=0.05, and the bulk-update
periodNΨ=20N_{\Psi}=20. (which means that the bulk is updated every 1 time unit).

Figure˜6compares the Neuralδ​f\delta\!fscheme with the BSL reference and the standardδ​f\delta\!fscheme att=25t=25,5050and9999, in the nonlinear saturation regime. The characteristic vortex structure and the thin phase-space filaments generated by the filamentation of the distribution function are clearly visible. The Neuralδ​f\delta\!f-PIC method reproduces the vortex structure and the filaments seen in the BSL reference withNp=104N_{p}=10^{4}particles, while drastically reducing the noise of the phase-space density compared to the standardδ​f\delta\!fscheme.
Unlike grid-based or particle methods, the neural bulk is a function that can be evaluated at any point of phase space. Figure7illustrates this feature: successive zooms, reveal filamentary structures at scales far below the reach of a grid-based scheme, and without any numerical diffusion. This figure is meant to be illustrative rather than quantitative: we make no claim that these fine filaments are accurately located, they are in fact likely mispositioned, but they show the ability of the representation to resolve arbitrarily fine, non-dissipative structures.(a)t=25t=25(b)t=50t=50(c)t=99t=99Figure 6:1D1V two-stream instability fromSection˜5.2.1: Comparison between the density given by the Neuralδ​f\delta\!fscheme (left), the BSL scheme (middle) and the standardδ​f\delta\!fscheme (right), att=25t=25,t=50t=50andt=99t=99. The Neuralδ​f\delta\!fand the standardδ​f\delta\!fschemes useNp=104N_{p}=10^{4}particles, while the BSL scheme uses a grid of size1024×10241024\times 1024.Figure 7:1D1V two-stream instability fromSection˜5.2.1: Zoom on the phase space densityf​(t,x,v)f(t,x,v)att=99t=99for the 1D1V two-stream instability given by the Neuralδ​f\delta\!fscheme withNp=40000N_{p}=40000particles. On each zoom, the density is evaluated on a1024×10241024\times 1024grid.

Figure˜8compares the three schemes at the final timet=99t=99for an increasing number of particles,Np∈{103,104,4×104}N_{p}\in\{10^{3},10^{4},4\times 10^{4}\}. While the standardδ​f\delta\!fscheme is strongly polluted by noise at low particle counts, the Neuralδ​f\delta\!fscheme remains close to the BSL reference even withNp=103N_{p}=10^{3}particles.(a)Np=103N_{p}=10^{3}(b)Np=104N_{p}=10^{4}(c)Np=4×104N_{p}=4\times 10^{4}Figure 8:1D1V two-stream instability fromSection˜5.2.1: Comparison between the density given by the Neuralδ​f\delta\!fscheme (left), the BSL scheme (middle) and the standardδ​f\delta\!fscheme (right) att=99t=99, for an increasing number of particlesNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}. The BSL scheme uses a grid of size1024×10241024\times 1024.

The top row ofFigure˜9shows the time evolution of the electric energyℰ​(t)=∫L​𝕋d|E​(t,x)|2​dx\mathcal{E}(t)=\int_{L\mathbb{T}^{d}}|E(t,x)|^{2}\,\mathrm{d}xfor the Neuralδ​f\delta\!f-PIC method, the standardδ​f\delta\!f-PIC method and the BSL method, denoted byℰneural​δ​f\mathcal{E}_{\mathrm{neural}\ \delta\!f},ℰδ​f\mathcal{E}_{\delta\!f}andℰSL\mathcal{E}_{\mathrm{SL}}respectively.
The Neuralδ​f\delta\!fmethod correctly captures the evolution of the electric energy and stays very close to the energy given by the BSL method, for all three particle counts.

The bottom row ofFigure˜9shows the time evolution of the empirical weight variance (which correspond to the caseα​(z)=1\alpha(z)=1fromSection˜2.3) for the Neuralδ​f\delta\!fand the standardδ​f\delta\!fmethod. It is computed on the unnormalised weightswk:=Np​δ​wk=(finit​(zk0)−f0m​(zkn))/g​(zk0)w_{k}:=N_{p}\,\delta w_{k}=\bigl(f_{\mathrm{init}}(z_{k}^{0})-{f_{0}^{m}}(z_{k}^{n})\bigr)/g(z_{k}^{0}), by|σδ​fn|2=1Np​∑k=1Np|wkn|2−w¯2,with​w¯=1Np​∑k=1Npwk.|\sigma_{\delta\!f}^{n}|^{2}=\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}|w_{k}^{n}|^{2}-\overline{w}^{2},\text{\quad with \quad}\overline{w}=\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}w_{k}.(43)

Defined this way,|σδ​fn|2|\sigma_{\delta\!f}^{n}|^{2}is an empirical estimate of the population variance, which is independent ofNpN_{p}and governs the Monte-Carlo error on theδ​f\delta\!fpart of the moments throughσδ​f/Np1/2\sigma_{\delta\!f}/N_{p}^{\nicefrac{{1}}{{2}}}.
In the standardδ​f\delta\!f-PIC method, the variance grows rapidly as the distribution evolves away from its initial state, reaching values between150150and300300once the instability saturates aroundt=20t=20, and then oscillates within this range; consistently with its interpretation as a population variance, these values are essentially independent ofNpN_{p}.
The Neuralδ​f\delta\!f-PIC method keeps the variance much lower, from about5050atNp=103N_{p}=10^{3}down to about2525atNp=4×104N_{p}=4\times 10^{4}, since a larger number of markers yields a better-trained flow. The reduction factor thus grows from roughly55atNp=103N_{p}=10^{3}to about1010atNp=4×104N_{p}=4\times 10^{4}. The periodic oscillations correspond to the bulk updates.
Nevertheless, one can observe a growth of the value of the weight even after the computation of the new bulk. One possible way to understand this phenomenon is the following. Denoting by‖w‖Np2:=1Np​∑k=1Npwk2\|w\|^{2}_{N_{p}}:=\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}w_{k}^{2}a scaledℓ2\ell^{2}norm on the weights,
one hasσδ​fn≤(1Np​∑k=1Np|wkn|2)1/2=‖wn‖Np.\sigma_{\delta\!f}^{n}\leq\left(\frac{1}{N_{p}}\sum_{k=1}^{N_{p}}|w_{k}^{n}|^{2}\right)^{1/2}=\|w^{n}\|_{N_{p}}.

Writing the weight aswkn=f0m~​(zkn)−f0m​(zkn)g​(zk0)⏟=⁣:skn+finit​(zk0)−f0m~​(zkn)g​(zk0)⏟=⁣:ekn,w_{k}^{n}=\underbrace{\frac{\widetilde{f_{0}^{m}}(z_{k}^{n})-f_{0}^{m}(z_{k}^{n})}{g(z_{k}^{0})}}_{=:\,s_{k}^{n}}+\underbrace{\frac{f_{\mathrm{init}}(z_{k}^{0})-\widetilde{f_{0}^{m}}(z_{k}^{n})}{g(z_{k}^{0})}}_{=:\,e_{k}^{n}},

one obtainsσδ​fn≤‖wn‖Np≤‖sn‖Np+‖en‖Np,\sigma_{\delta\!f}^{n}\leq\|w^{n}\|_{N_{p}}\leq\|s^{n}\|_{N_{p}}+\|e^{n}\|_{N_{p}},

wheresns^{n}measures the projection error of the bulk on the coarse B-spline grid,
andene^{n}the transport error resulting from the approximation of the backward trajectories by the neural networks.

The first termsns^{n}is determined by the smoothness of the fine representation, the size of the grid and the order of the splines used.
The second termene^{n}is determined by the accuracy of each trained flow, and by the number of flows in the composition. By composing several flows, each small error made on each flow gets amplified by the number of composed flows, resulting in a growth of the weights. A way to reduce this growth would be to reset the flows by a remapping of the bulk density, at the cost of an error on the approximation of the density.
With the incremental training strategy ofSection˜4.5, the bulk at the final timet=99t=99is a composition of3535,4040and3939networks forNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}respectively (against1414,1717and1515att=50t=50), to be compared with the9999bulk updates performed over the run.

For the lowest particle countNp=103N_{p}=10^{3}, the density of particles per grid cell for the Poisson solver is much lower, a little less than 1 particle per cell versus more than 3 per cell whenNp=104N_{p}=10^{4}(we recall that we use 32 grid cells per direction in all test cases). As seen inFigure˜9, this has the consequence that the standardδ​f\delta\!fscheme is unable to track the correct evolution of the electric energy, while the Neuralδ​f\delta\!fscheme is able to roughly follow the semi-Lagrangian scheme despite also having a low number of sample points to train the networks.(a)Electric energy,Np=103N_{p}=10^{3}.(b)Electric energy,Np=104N_{p}=10^{4}.(c)Electric energy,Np=4×104N_{p}=4\times 10^{4}.(d)Weight variance,Np=103N_{p}=10^{3}.(e)Weight variance,Np=104N_{p}=10^{4}.(f)Weight variance,Np=4×104N_{p}=4\times 10^{4}.Figure 9:1D1V two-stream instability fromSection˜5.2.1: time evolution of the electric energy (top row) and of the empirical weight varianceσδ​f2\sigma^{2}_{\delta\!f}(bottom row) for an increasing number of particlesNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}.

InFigure˜10, we assessed the noise reduction in a statistically robust manner, by performing
50 independent realizations of both the standard and Neuralδ​f\delta\!f-PIC
methods with the same number of particles.
Among these simulations, the only change is the initial marker draw.
The error metric is theL2L^{2}-in-time error of the electric energy relative to the BSL reference:(∫0T|ℰ​(t)−ℰBSL​(t)|2​dt)1/2.\left(\int_{0}^{T}\left|\mathcal{E}(t)-\mathcal{E}_{\mathrm{BSL}}(t)\right|^{2}\,\mathrm{d}t\right)^{1/2}.(44)

Overall, we notice a reduction of both the mean and of the variance of the error.
We emphasize that the present study is aproof of concepton the Vlasov-Poisson system. In this setting, the Neuralδ​f\delta\!f-PIC method is, in terms of computational time, far more expensive than the standardδ​f\delta\!f-PIC or the BSL scheme, and we do not claim it to be competitive with a standardδ​f\delta\!fscheme using a larger number of particles to reach a comparable accuracy. The additional memory cost, on the other hand, remains low, since the stored networks are small. Our objective is rather to assess whether symplectic neural networks can effectively denoise the density by dynamically evolving the bulk. This is a prerequisite for the regimes we ultimately target, such as flux-driven or edge gyrokinetic simulations, where the distribution departs strongly from any static or Maxwellian equilibrium, so that evolving the bulk is genuinely necessary, and where simply increasing the number of particles is prohibitively expensive.Figure 10:1D1V two-stream instability fromSection˜5.2.1: Error distribution of the error on the electric energy. In blue are the error for Neuralδ​f\delta\!fscheme, in orange are the error for the standardδ​f\delta\!fscheme. On the left the simulations are done withNp=20000N_{p}=20000particles, and on the right withNp=30000N_{p}=30000particles.

## 5.2.21D1V bump-on-tail instability

The bump-on-tail instability consists of an initial centered Maxwellian together with a beam of particles with a positive velocity:finit​(x,v)=(0.92​π​e−v2/2+0.210​π​e−(v−3.8)2/10)​(1+0.03​cos⁡(0.4​x)).f_{\mathrm{init}}(x,v)=\left(\frac{0.9}{\sqrt{2\pi}}\,e^{-v^{2}/2}+\frac{0.2}{\sqrt{10\pi}}\,e^{-(v-3.8)^{2}/10}\right)\bigl(1+0.03\cos(0.4x)\bigr).(45)

The computational domain is[0,10​π]×[−6,6][0,10\pi]\times[-6,6]withNp=104N_{p}=10^{4},Δ​t=0.05\Delta t=0.05, andNΨ=10N_{\Psi}=10. As in the two-stream instability, we also run this test withNp=103N_{p}=10^{3}andNp=4×104N_{p}=4\times 10^{4}particles to assess the effect of the number of particles.
This test case is more challenging because the solution creates two vortices that move in time, yielding a more complex dynamics that the network has to reconstruct.

Figure˜11compares the Neuralδ​f\delta\!fscheme with the BSL reference and the standardδ​f\delta\!fscheme att=15t=15,2424and3232, withNp=104N_{p}=10^{4}particles. The bump-on-tail instability generates a more complex phase-space structure than the two-stream case: because the domain is larger, two vortices appear, making the flow more difficult to approximate. The Neuralδ​f\delta\!fscheme nonetheless reproduces this structure accurately and strongly reduces the noise of the phase-space density compared to the standardδ​f\delta\!fscheme.(a)t=15t=15(b)t=24t=24(c)t=32t=32Figure 11:1D1V bump-on-tail instability fromSection˜5.2.2: Comparison between the density given by the Neuralδ​f\delta\!fscheme (left), the BSL scheme (middle) and the standardδ​f\delta\!fscheme (right), att=15t=15,t=24t=24andt=32t=32. The Neuralδ​f\delta\!fand the standardδ​f\delta\!fschemes useNp=104N_{p}=10^{4}particles.

Figure˜12shows the same comparison att=32t=32for an increasing number of particles,Np=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}. As for the two-stream case, the standardδ​f\delta\!fscheme is strongly polluted by noise at low particle counts, whereas the Neuralδ​f\delta\!fscheme remains close to the BSL reference.(a)Np=103N_{p}=10^{3}(b)Np=104N_{p}=10^{4}(c)Np=4×104N_{p}=4\times 10^{4}Figure 12:1D1V bump-on-tail instability fromSection˜5.2.2: Comparison between the density given by the Neuralδ​f\delta\!fscheme (left), the BSL scheme (middle) and the standardδ​f\delta\!fscheme (right) att=32t=32, for an increasing number of particlesNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}.

Figure˜13shows the time evolution of the electric energy and of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}for the same three particle counts. The Neuralδ​f\delta\!f-PIC method tracks the reference electric energy given by the BSL scheme at all particle counts. As in the two-stream case, the standardδ​f\delta\!f-PIC method with a static bulk shows a strong growth of the variance, here particularly pronounced because the solution deviates more strongly from the initial distribution, whereas the Neuralδ​f\delta\!f-PIC method reduces it by a factor of a little less than1010; one can again observe a growth of the weights after each bulk update. With the incremental training strategy ofSection˜4.5, the bulk at the final time is a composition of1818,2222and2121networks forNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}respectively, to be compared with the100100bulk updates performed over the run.(a)Electric energy,Np=103N_{p}=10^{3}.(b)Electric energy,Np=104N_{p}=10^{4}.(c)Electric energy,Np=4×104N_{p}=4\times 10^{4}.(d)Weight variance,Np=103N_{p}=10^{3}.(e)Weight variance,Np=104N_{p}=10^{4}.(f)Weight variance,Np=4×104N_{p}=4\times 10^{4}.Figure 13:1D1V bump-on-tail instability fromSection˜5.2.2: time evolution of the electric energy (top row) and of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}(bottom row) for an increasing number of particlesNp=103N_{p}=10^{3},10410^{4}and4×1044\times 10^{4}.

Just like in the 1D1V two-stream instability, we performed
50 independent simulations with both the standard and Neuralδ​f\delta\!fmethods with the same number of particles. The results are illustrated inFigure˜14. In this case, the reduction in the error is more important than for the two-stream instability.Figure 14:1D1V bump-on-tail instability fromSection˜5.2.2: Histogram of the error between the Neuralδ​f\delta\!fmethod (in blue) and the standardδ​f\delta\!fmethod. The reference solution is given by a BSL scheme. The simulations are done withNp=20000N_{p}=20000particles.

## 5.33D3V test cases

We now present test cases for the full 3D3V Vlasov-Poisson problem.
We consider four test cases: the first three are extensions of the 1D1V two-stream instability, the last one is an extension of the bump-on-tail instability.
We useNp=106N_{p}=10^{6}particles for the two-stream and bump-on-tail cases, andNp=108N_{p}=10^{8}for the four-stream and six-stream cases.
In all 3D3V test cases, we use the same time stepΔ​t=0.05\Delta t=0.05as in the 1D1V cases, and a bulk-update period ofNΨ=10N_{\Psi}=10. We recall that, like in 1D1V, the SympNets haveℓ=10\ell=10layers of widthw=8w=8. However, because the total number of parameters also depends on the dimension of the inputs (the total number of parameters of one network is3​w​ℓ​(d+1)3w\ell(d+1)), the networks in 3D3V have960960parameters, while the networks in 1D1V have 480 parameters.
This section is meant to be exploratory: its purpose is to demonstrate that the method runs in a full six-dimensional phase space, rather than to provide a quantitative error analysis. Producing a converged reference solution in 6D is indeed very difficult: even the finest643×63364^{3}\times 63^{3}semi-Lagrangian grid used below is likely under-resolved for the fine filamentation that develops, so the BSL6D results[35]are used only as a qualitative cross-check and not as a converged reference. We also emphasize that all the results reported here are obtained with a non-parallelized and non optimized code running on a single GPU. This constrains the number of particles we can afford, and hence the resolution attainable in 6D; a parallel implementation, which would lift these limitations, is left for future work.

Nonetheless, we consider that the results presented here are encouraging, as they show that the Neuralδ​f\delta\!f-PIC method is able to run 6D test cases on a single process with acceptable accuracy, and to reduce the noise of the phase-space density.

## 5.3.13D3V Two-stream instability

The initial condition isfinit​(x,y,z,vx,vy,vz)=(1+ε​cos⁡(k​x))​12​2​π​(e−(vx−v0)2/2+e−(vx+v0)2/2)​12​π​e−(vy2+vz2)/2,f_{\mathrm{init}}(x,y,z,v_{x},v_{y},v_{z})=(1+\varepsilon\cos(kx))\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{x}-v_{0})^{2}/2}+e^{-(v_{x}+v_{0})^{2}/2}\bigr)\frac{1}{2\pi}e^{-(v_{y}^{2}+v_{z}^{2})/2},(46)

withk=0.3k=0.3,v0=2.4v_{0}=2.4andε=0.05\varepsilon=0.05. The computational domain is[0,2​π/k]×[0,1]2×[−7,7]3.[0,2\pi/k]\times[0,1]^{2}\times[-7,7]^{3}.

Figure˜15shows cross sections of the phase space density at different times. The density is well reconstructed and stays symmetric despite the relatively low number of particles for a 6D domain.Figure˜16shows the evolution of the electric energy and of the empirical weight varianceσδ​f2\sigma_{\delta\!f}^{2},
both for the Neuralδ​f\delta\!f-PIC method and for standardδ​f\delta\!f-PIC method. The two methods are
in qualitative agreement on the electric energy. The weight variance (43)
for the Neuralδ​f\delta\!f-PIC method is reduced by a factor of approximately 10.
The semi-Lagrangian scheme used a grid of size64×32×32×63×31×3164\times 32\times 32\times 63\times 31\times 31. Over the run (9999bulk updates), the incremental training strategy ofSection˜4.5produced1313composed networks.(a)Cross sections of the density att=15t=15(b)Cross sections of the density att=30t=30(c)Cross sections of the density att=45t=45Figure 15:3D3V two-stream instability fromSection˜5.3.1: Cross sections of the phase-space densityf(x,y=0,z=0,vx,vy=0,vz=0)f(x,y=0,z=0,v_{x},v_{y}=0,v_{z}=0),f​(x=0,y,z=0,vx=0,vy,vz=0)f(x=0,y,z=0,v_{x}=0,v_{y},v_{z}=0)andf​(x=0,y=0,z,vx=0,vy=0,vz)f(x=0,y=0,z,v_{x}=0,v_{y}=0,v_{z})att=15t=15,t=30t=30andt=45t=45.(a)Evolution of the electric energyℰ\mathcal{E}.(b)Evolution of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}.Figure 16:3D3V two-stream instability fromSection˜5.3.1: Evolution of the electric energy and of the weight variance.

## 5.3.23D3V four-stream instability

The second extension of the 1D1V two-stream instability is given by the following initial conditionfinit​(x,y,z,vx,vy,vz)=\displaystyle f_{\mathrm{init}}(x,y,z,v_{x},v_{y},v_{z})=(1+ε​cos⁡(k​x)+ε​cos⁡(k​y))\displaystyle(1+\varepsilon\cos(kx)+\varepsilon\cos(ky))(47)×12​2​π​(e−(vx−v0)2/2+e−(vx+v0)2/2)\displaystyle\times\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{x}-v_{0})^{2}/2}+e^{-(v_{x}+v_{0})^{2}/2}\bigr)(48)×12​2​π​(e−(vy−v0)2/2+e−(vy+v0)2/2)\displaystyle\times\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{y}-v_{0})^{2}/2}+e^{-(v_{y}+v_{0})^{2}/2}\bigr)(49)×12​π​e−vz2/2\displaystyle\times\frac{1}{\sqrt{2\pi}}e^{-v_{z}^{2}/2}(50)

withk=0.3k=0.3,v0=2.4v_{0}=2.4andε=0.05\varepsilon=0.05. The computational domain is[0,2​π/k]×[0,1]2×[−7,7]3.[0,2\pi/k]\times[0,1]^{2}\times[-7,7]^{3}.

Figure˜17shows cross sections of the phase space density at different times. The density seems to be well reconstructed.

Figure˜18shows the evolution of the electric energy and of the empirical weight varianceσδ​f2\sigma_{\delta\!f}^{2},
both for the Neuralδ​f\delta\!f-PIC method and for standardδ​f\delta\!f-PIC method. The two methods are
in qualitative agreement on the electric energy. The weight variance
for the Neuralδ​f\delta\!f-PIC method is reduced by a factor of approximately 10. The semi-Lagrangian scheme used a grid of size64×64×32×63×63×3164\times 64\times 32\times 63\times 63\times 31. Here,1212networks were trained over the run.(a)Cross sections of the density att=15t=15.(b)Cross sections of the density att=30t=30.(c)Cross sections of the density att=45t=45.Figure 17:3D3V four-stream instability fromSection˜5.3.2: Cross sections of the phase-space densityf(x,y=0,z=0,vx,vy=0,vz=0)f(x,y=0,z=0,v_{x},v_{y}=0,v_{z}=0),f​(x=0,y,z=0,vx=0,vy,vz=0)f(x=0,y,z=0,v_{x}=0,v_{y},v_{z}=0)andf​(x=0,y=0,z,vx=0,vy=0,vz)f(x=0,y=0,z,v_{x}=0,v_{y}=0,v_{z})att=15t=15,t=30t=30andt=45t=45.(a)Evolution of the electric energyℰ\mathcal{E}.(b)Evolution of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}.Figure 18:3D3V four-stream instability fromSection˜5.3.2: Evolution of the electric energy and weight variance.

## 5.3.33D3V six-stream instability

The third extension of the 1D1V two-stream instability is given by the following initial conditionfinit​(x,y,z,vx,vy,vz)=\displaystyle f_{\mathrm{init}}(x,y,z,v_{x},v_{y},v_{z})=(1+ε​cos⁡(k​x)+ε​cos⁡(k​y)+ε​cos⁡(k​z))\displaystyle(1+\varepsilon\cos(kx)+\varepsilon\cos(ky)+\varepsilon\cos(kz))(51)×12​2​π​(e−(vx−v0)2/2+e−(vx+v0)2/2)\displaystyle\times\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{x}-v_{0})^{2}/2}+e^{-(v_{x}+v_{0})^{2}/2}\bigr)(52)×12​2​π​(e−(vy−v0)2/2+e−(vy+v0)2/2)\displaystyle\times\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{y}-v_{0})^{2}/2}+e^{-(v_{y}+v_{0})^{2}/2}\bigr)(53)×12​2​π​(e−(vz−v0)2/2+e−(vz+v0)2/2)\displaystyle\times\frac{1}{2\sqrt{2\pi}}\bigl(e^{-(v_{z}-v_{0})^{2}/2}+e^{-(v_{z}+v_{0})^{2}/2}\bigr)(54)

withk=0.3k=0.3,v0=2.4v_{0}=2.4andε=0.05\varepsilon=0.05. The computational domain is[0,2​π/k]3×[−7,7]3.[0,2\pi/k]^{3}\times[-7,7]^{3}.

Figure˜19shows cross sections of the phase space density at different times. The density is well-reconstructed and symmetric at the beginning of the simulation, but the solution eventually develops spurious filamentation and loses its symmetry, even though the main structure remains well-captured. This case is the most demanding of all: compared with the four-stream instability, the dynamics evolve in all three spatial directions and the computational domain is larger (the extent inzzis11for the four-stream case versus2​π/0.32\pi/0.3here). As a result, the number of particles is too low for this 6D domain, and some regions of phase space contain no particles even where the distribution should be non-zero, which we believe is the cause of the spurious filamentation. Properly resolving this case would require substantially more particles, hence a parallel implementation; it is therefore at the limit of what the present single-GPU code can handle, and we report it as an illustration of the method’s reach in full 6D rather than as a quantitatively converged result.

Figure˜20shows the evolution of the electric energy and of the empirical weight varianceσδ​f2\sigma_{\delta\!f}^{2},
both for the Neuralδ​f\delta\!f-PIC method and for standardδ​f\delta\!f-PIC method. The two methods are
in qualitative agreement on the electric energy. The weight variance
for the Neuralδ​f\delta\!f-PIC method is reduced by a factor of approximately 10.
The semi-Lagrangian scheme used a grid of size64×64×64×63×63×6364\times 64\times 64\times 63\times 63\times 63. This most demanding case required2222networks over the run.(a)Cross sections of the density att=15t=15.(b)Cross sections of the density att=30t=30.(c)Cross sections of the density att=45t=45.Figure 19:3D3V six-stream instability fromSection˜5.3.3: Cross sections of the phase-space densityf(x,y=0,z=0,vx,vy=0,vz=0)f(x,y=0,z=0,v_{x},v_{y}=0,v_{z}=0),f​(x=0,y,z=0,vx=0,vy,vz=0)f(x=0,y,z=0,v_{x}=0,v_{y},v_{z}=0)andf​(x=0,y=0,z,vx=0,vy=0,vz)f(x=0,y=0,z,v_{x}=0,v_{y}=0,v_{z})att=15t=15,t=30t=30andt=45t=45.(a)Evolution of the electric energyℰ\mathcal{E}.(b)Evolution of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}.Figure 20:3D3V six-stream instability fromSection˜5.3.3: Evolution of the electric energy and weight variance.

## 5.3.43D3V bump-on-tail instability

The 3D3V bump-on-tail initial condition isfinit​(x,y,z,vx,vy,vz)=(0.92​π​e−vx2/2+0.210​π​e−(vx−3.8)2/10)​e−(vy2+vz2)/22​π​(1+0.03​cos⁡(0.4​x)).f_{\mathrm{init}}(x,y,z,v_{x},v_{y},v_{z})=\left(\frac{0.9}{\sqrt{2\pi}}\,e^{-v_{x}^{2}/2}+\frac{0.2}{\sqrt{10\pi}}\,e^{-(v_{x}-3.8)^{2}/10}\right)\frac{e^{-(v_{y}^{2}+v_{z}^{2})/2}}{2\pi}\bigl(1+0.03\cos(0.4x)\bigr).(55)

The computational domain is[0,10​π]×[0,1]2×[−6,6]3[0,10\pi]\times[0,1]^{2}\times[-6,6]^{3}.Figure˜21shows cross sections of the phase space density at different times. The density is well reconstructed.Figure˜22shows the evolution of the electric energy and of the empirical weight varianceσδ​f2\sigma_{\delta\!f}^{2},
both for the Neuralδ​f\delta\!f-PIC method and for standardδ​f\delta\!f-PIC method. The two methods are
in qualitative agreement on the electric energy. The weight variance (43)
for the Neuralδ​f\delta\!f-PIC method is reduced by a factor of approximately 10. Over the run,1515networks were trained.(a)Cross sections of the density att=15t=15(b)Cross sections of the density att=32t=32(c)Cross sections of the density att=38t=38Figure 21:3D3V bump-on-tail instability fromSection˜5.2.2: Cross sections of the phase-space densityf(x,y=0,z=0,vx,vy=0,vz=0)f(x,y=0,z=0,v_{x},v_{y}=0,v_{z}=0),f​(x=0,y,z=0,vx=0,vy,vz=0)f(x=0,y,z=0,v_{x}=0,v_{y},v_{z}=0)andf​(x=0,y=0,z,vx=0,vy=0,vz)f(x=0,y=0,z,v_{x}=0,v_{y}=0,v_{z})att=15t=15,t=32t=32andt=38t=38.(a)Evolution of the electric energyℰ\mathcal{E}.(b)Evolution of the weight varianceσδ​f2\sigma_{\delta\!f}^{2}.Figure 22:3D3V bump-on-tail instability fromSection˜5.3.4: Evolution of the electric energy and weight variance.

## 6Conclusion

We have presented the Neuralδ​f\delta\!f-PIC method, a new approach for the kinetic
simulation of plasmas in which the bulk density, acting as a control
variate, is evolved using a sequence of symplectic neural networks trained on the
particle trajectories. The bulk is then reprojected on a coarse spline grid, which
makes the evaluation of the weights and of the velocity integrals relatively cheap.
The use of SympNets guarantees that the reconstructed backward flow is symplectic by
construction.
We also introduced a periodic variant of the SympNet architecture that natively
encodes the spatial periodicity of the problem, avoiding any penalisation term.

We first verified, on a controlled flow-learning experiment, that periodic SympNets
can accurately approximate the characteristic flow of the Vlasov-Poisson system from
particle data, and that an incremental training strategy
(akin to a preconditioning or a curriculum learning) is both more
stable and less prone to overfitting than a direct training of the flow over the
whole time interval. On the full scheme, numerical experiments in 1D1V and 3D3V show
that the dynamically evolved bulk keeps the particle weights small, reducing the
empirical weight variance by a factor of about55to1010compared to a staticδ​f\delta\!f-PIC scheme, and reducing the error on the electric field accordingly. The
incremental strategy further keeps the number of stored networks well below the
number of bulk updates.
Nevertheless, several limitations remain. The present study is a proof of concept on the
Vlasov-Poisson system: in this setting the method is significantly more expensive than
a standardδ​f\delta\!f-PIC scheme, and its benefit is to be sought in regimes where a static bulk is inadequate. The evaluation cost grows linearly with the
number of composed networks, and the composition of many approximate flows, together
with the spline interpolation, induces a slow growth of the particle weights over time;
controlling this growth, for instance by periodically remapping the density onto a
single network or spline representation, is an important direction for long-time
simulations. Finally, the 3D3V results are exploratory: a fully converged reference is
out of reach in six dimensions, and the simulations are limited by a non-parallel,
single-GPU implementation.

Future work will focus on a parallel implementation, on adaptive strategies for the
bulk-update periodNΨN_{\Psi}and for the network resets, on a control of the weight
growth through remapping, and on the application to gyrokinetic models, which is an
important objective of this approach.

## Acknowledgement

The authors would like to thank Nils Schild for kindly providing the data of the electric energy for the 3D3V tests from the BSL6D code.

## References
- Allfrey and Hatzky [2003]S. J. Allfrey and R. Hatzky.A revisedδ​f\delta\!falgorithm for nonlinear PIC simulation.Comput. Phys. Commun., 154(2):98–104,
2003.
- Amari and Douglas [1998]S.-I. Amari and S. C. Douglas.Why natural gradient?InProceedings of the 1998 IEEE International Conference on
Acoustics, Speech and Signal Processing, ICASSP’98 (Cat. No. 98CH36181),
volume 2, pages 1213–1216. IEEE, 1998.
- Arber and Vann [2002]T. D. Arber and R. G. L. Vann.A Critical Comparison of Eulerian-Grid-Based Vlasov Solvers.J. Comput. Phys., 180(1):339–357, 2002.
- Aydemir [1994]A. Y. Aydemir.A unified Monte Carlo interpretation of particle simulations and
applications to non-neutral plasmas.Phys. Plasmas, 1(4):822–831, 1994.
- Bachmayr et al. [2026]M. Bachmayr, A. Cohen, A. Kunoth, and O. Mula.Computation and Learning in High Dimensions.Oberwolfach Reports, 22(3):2013–2064,
Feb. 2026.ISSN 1660-8933.doi:10.4171/owr/2025/37.URLhttps://ems.press/journals/owr/articles/14299515.
- Beltran-Pulido et al. [2022]A. Beltran-Pulido, I. Bilionis, and D. Aliprantis.Physics-Informed Neural Networks for Solving Parametric
Magnetostatic Problems.IEEE Trans. Energy Convers., 37(4):2678–2689, 2022.
- Bengio et al. [2009]Y. Bengio, J. Louradour, R. Collobert, and J. Weston.Curriculum learning.InProceedings of the 26th annual international conference on
machine learning, pages 41–48, 2009.
- Biesek and de Almeida Konzen [2024]V. Biesek and P. H. de Almeida Konzen.Burgers’ PINNs with implicit Euler Transfer Learning.Rev. Mundi Eng., Tecnol. Gest., 9(4), 2024.
- Birdsall and Langdon [1991]C. K. Birdsall and A. B. Langdon.Plasma Physics via Computer Simulation.IOP Publishing, 1991.
- Bottino and Sonnendrücker [2015]A. Bottino and E. Sonnendrücker.Monte Carlo particle-in-cell methods for the simulation of the
Vlasov–Maxwell gyrokinetic equations.J. Plasma Phys., 81(5), 2015.
- Bruna et al. [2024]J. Bruna, B. Peherstorfer, and E. Vanden-Eijnden.Neural Galerkin schemes with active learning for high-dimensional
evolution equations.J. Comput. Phys., 496:112588, 2024.
- Brunner et al. [1999]S. Brunner, E. Valeo, and J. A. Krommes.Collisional delta-ffscheme with evolving background for transport
time scale simulations.Physics of Plasmas, 6(12):4504–4521,
1999.
- Campos Pinto et al. [2023]M. Campos Pinto, M. Pelz, and P.-H. Tournier.Aδ​f\delta\!fPIC method with forward–backward Lagrangian
reconstructions.Phys. Plasmas, 30(3), 2023.
- De Ryck and Mishra [2022]T. De Ryck and S. Mishra.Error analysis for physics-informed neural networks (PINNs)
approximating Kolmogorov PDEs.Adv. Comput. Math., 48(6), 2022.
- Dimits and Lee [1993]A. M. Dimits and W. W. Lee.Partially Linearized Algorithms in Gyrokinetic Particle Simulation.J. Comput. Phys., 107(2):309–323, 1993.
- Franck et al. [2026]E. Franck, V. Michel-Dansac, L. Navoret, and V. Vigon.Neural semi-Lagrangian method for high-dimensional
advection-diffusion problems.Comput. Methods Appl. Mech. Engrg., 448(B):118481, 2026.
- Garbet et al. [2010]X. Garbet, Y. Idomura, L. Villard, and T. H. Watanabe.Gyrokinetic simulations of turbulent transport.Nucl. Fusion, 50(4):043002, 2010.
- Hatzky et al. [2019]R. Hatzky, R. Kleiber, A. Könies, A. Mishchenko, M. Borchardt, A. Bottino, and
E. Sonnendrücker.Reduction of the statistical error in electromagnetic gyrokinetic
particle-in-cell simulations.Journal of Plasma Physics, 85(1):905850112, 2019.doi:10.1017/s0022377819000096.
- Hu and Krommes [1994]G. Hu and J. A. Krommes.Generalized weighting scheme forδ​f\delta\!fparticle-simulation
method.Phys. Plasmas, 1(4):863–874, 1994.
- Hu et al. [2024]Z. Hu, K. Shukla, G. E. Karniadakis, and K. Kawaguchi.Tackling the curse of dimensionality with physics-informed neural
networks.Neural Netw., 176:106369, 2024.
- Jin et al. [2020]P. Jin, Z. Zhang, A. Zhu, Y. Tang, and G. E. Karniadakis.SympNets: Intrinsic structure-preserving symplectic networks for
identifying Hamiltonian systems.Neural Netw., 132:166–179, 2020.
- Kingma and Ba [2015]D. P. Kingma and J. Ba.Adam: A method for stochastic optimization.InProceedings of the 3rd International Conference on Learning
Representations (ICLR 2015), San Diego, CA, USA, 2015.
- Kotschenreuther et al. [2007]M. Kotschenreuther, P. M. Valanju, S. M. Mahajan, and J. C. Wiley.On heat loading, novel divertors, and fusion reactors.Phys. Plasmas, 14(7), 2007.
- Krah et al. [2024]P. Krah, X.-Y. Yin, J. Bergmann, J.-C. Nave, and K. Schneider.A characteristic mapping method for Vlasov–Poisson with extreme
resolution properties.Communications in Computational Physics, 35(4):905–937, 2024.
- Ku et al. [2016]S. Ku, R. Hager, C. S. Chang, J. M. Kwon, and S. E. Parker.A new hybrid-Lagrangian numerical scheme for gyrokinetic simulation
of tokamak edge plasma.J. Comput. Phys., 315:467–475, 2016.
- Lanti et al. [2020]E. Lanti, N. Ohana, N. Tronko, et al.Orb5: A global electromagnetic gyrokinetic code using the PIC
approach in toroidal geometry.Comput. Phys. Commun., 251:107072, 2020.
- Mildenhall et al. [2021]B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and
R. Ng.NeRF: representing scenes as neural radiance fields for view
synthesis.Commun. ACM, 65(1):99–106, 2021.
- Müller and Zeinhofer [2023]J. Müller and M. Zeinhofer.Achieving High Accuracy with PINNs via Energy Natural Gradient
Descent.In A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and
J. Scarlett, editors,Proceedings of the 40th International Conference
on Machine Learning, volume 202 ofProceedings of Machine Learning
Research, pages 25471–25485. PMLR, 2023.
- Murugappan et al. [2022]M. Murugappan, L. Villard, S. Brunner, B. F. McMillan, and A. Bottino.Gyrokinetic simulations of turbulence and zonal flows driven by steep
profile gradients using a delta-f approach with an evolving background
Maxwellian.Phys. Plasmas, 29(10), 2022.
- Murugappan et al. [2024]M. Murugappan, L. Villard, S. Brunner, G. Di Giannatale, B. F. McMillan, and
A. Bottino.Gyrokinetic flux-driven simulations in mixed TEM/ITG regime using a
delta-f PIC scheme with evolving background.Phys. Plasmas, 31(11), 2024.
- Parker and Lee [1993]S. E. Parker and W. W. Lee.A fully nonlinear characteristic method for gyrokinetic simulation.Phys. Fluids B, 5(1):77–86, 1993.
- Parker et al. [1996]S. E. Parker, H. E. Mynick, M. Artun, J. C. Cummings, V. Decyk, J. V. Kepner,
W. W. Lee, and W. M. Tang.Radially global gyrokinetic simulation studies of transport barriers.Phys. Plasmas, 3(5):1959–1966, 1996.
- Raissi et al. [2019]M. Raissi, P. Perdikaris, and G. E. Karniadakis.Physics-informed neural networks: A deep learning framework for
solving forward and inverse problems involving nonlinear partial differential
equations.J. Comput. Phys., 378:686–707, 2019.
- Ray et al. [2024]D. Ray, O. Pinti, and A. A. Oberai.Deep Learning and Computational Physics.Springer Nature Switzerland, Cham, 2024.ISBN 978-3-031-59344-4 978-3-031-59345-1.doi:10.1007/978-3-031-59345-1.URLhttps://link.springer.com/10.1007/978-3-031-59345-1.
- Schild et al. [2024]N. Schild, M. Räth, S. Eibl, K. Hallatschek, and K. Kormann.A performance portable implementation of the semi-Lagrangian
algorithm in six dimensions.Comput. Phys. Commun., 295:108973, 2024.
- Sonnendrücker et al. [1999]E. Sonnendrücker, J. Roche, P. Bertrand, and A. Ghizzo.The Semi-Lagrangian Method for the Numerical Resolution of the
Vlasov Equation.J. Comput. Phys., 149(2):201–220, 1999.
- Sonnendrücker et al. [2015]E. Sonnendrücker, A. Wacher, R. Hatzky, and R. Kleiber.A split control variate scheme for PIC simulations with collisions.J. Comput. Phys., 295:402–419, 2015.
- Stiasny and Chatzivasileiadis [2023]J. Stiasny and S. Chatzivasileiadis.Physics-informed neural networks for time-domain simulations:
Accuracy, computational cost, and flexibility.Electr. Pow. Syst. Res., 224:109748, 2023.
- Wang et al. [2021]X. Wang, Y. Chen, and W. Zhu.A Survey on Curriculum Learning.IEEE Trans. Pattern Anal. Mach. Intell., 44(9):4555–4576, 2021.
- Zhang et al. [2023]B. Zhang, G. Cai, H. Weng, W. Wang, L. Liu, and B. He.Physics-informed neural networks for solving forward and inverse
Vlasov-Poisson equation via fully kinetic simulation.Mach. Learn.: Sci. Technol., 4(4):045015,
2023.

## 


- 


Major funding support from
