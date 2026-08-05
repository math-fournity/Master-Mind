# Gaussian non relativistic spontaneously stochastic hydrodynamics

**arXiv ID**: 2607.27540v1
**Authors**: David Montenegro, Giorgio Torrieri
**Published**: 2026-07-30
**Categories**: physics.flu-dyn, cond-mat.stat-mech, hep-th
**HTML URL**: https://arxiv.org/html/2607.27540v1

## Abstract

We study the non-relativistic limit of Gaussian covariant hydrodynamics [1]. We argue that the condition of incompressibility provides additional symmetries matching relativistic hydrodynamics but incompressibility must break down at a ``microscopic`` scale. We then develop the renormalization group equations for average and fluctuations w.r.t. that scale, to understand its effect on flows at intermolecular distances where hydrodynamics gives way to statistical mechanics. The resulting dynamics naturally incorporates spontaneous stochasticity as a macroscopic back reaction of statistical mechanics fluctuations, as well as features reminiscent of anomalous dissipation and ``wild solutions`` as renormalization group counterterms. We frame these considerations into both a phenomenological discussion of the limits of applicability of fluid dynamics, and a discussion of where physics might shed some light on the mathematical issues associated with turbulence.

## Full Text

Gaussian non relativistic spontaneously stochastic hydrodynamics

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
- License: CC BY 4.0arXiv:2607.27540v1 [physics.flu-dyn] 30 Jul 2026

## Gaussian non relativistic spontaneously stochastic hydrodynamicsDavid Montenegro, Giorgio TorrieriUniversidade Estadual de Campinas - Instituto de Fisica Gleb Wataghin
Rua Sérgio Buarque de Holanda, 777
CEP 13083-859 - Campinas SP


## Abstract

We study the non-relativistic limit of Gaussian covariant hydrodynamics [1]. We argue that the condition of incompressibility provides additional symmetries matching relativistic hydrodynamics but incompressibility must break down at a “microscopic“ scale. We then develop the renormalization group equations for average and fluctuations w.r.t. that scale, to understand its effect on flows at intermolecular distances where hydrodynamics gives way to statistical mechanics. The resulting dynamics naturally incorporates spontaneous stochasticity as a macroscopic back reaction of statistical mechanics fluctuations, as well as features reminiscent of anomalous dissipation and “wild solutions“ as renormalization group counterterms. We frame these considerations into both a phenomenological discussion of the limits of applicability of fluid dynamics, and a discussion of where physics might shed some light on the mathematical issues associated with turbulence.

## I  Introduction

## I.1  The background issues

The dynamics of fluids, while traditionally a domain of engineering departments (as “hydraulics“, cynically labelled ”observing phenomena which could not be explained”) or of mathematics departments (as “fluid mechanics“, equally cynically labelled ” explaining phenomena which could not be observed”)[2]is a profoundly physical phenomenon.

Physicists tend to think of fluids as described by an effective theory written in terms of a gradient expansions of conserved currents of a continuum which is locally close to thermal equilibrium[3]. The frame in which this equilibrium is defined is called the hydrodynamic flow frame[4], and it is also the frame in which scalar conserved currents are at rest. The equilibrium parameters (density, temperature and equation of state) together with the flow then determine the dynamics via conservation laws via a series in gradients weighted by a small dimensionless parameter, the dissipative over macroscopic gradient scale,usually known as the Knudsen number. In this sense, therefore, hydrodynamics is a traditional effective field theory.
The great mysteries of hydrodynamics, such as the existence of solutions of the Navier Stokes equations, are usually thought of as abstract mathematics[5,6]in which physics has little or no role, even when the questions asked, such as anomalous dissipation[7]and the existence of Wild/Nightmare solutions[8]appear physically relevant.

However, looking carefully there are mysteries within the physical aspects of fluid dynamics which might challenge this consensus. Away from perfect equilibrium, the flow frame is not so well defined because of diffusive currents, leading to several definitions of flow frames[9,10](in non-relativistic systems the frame at rest with a conserved charge, i.e. the mass density, is usually far more convenient, but the conceptual problem does remain).

This ambiguity masks a deeper problem: Hydrodynamics depends on statistical mechanics, for the equation of state and eventually transport coefficients.
But “Equilibrium“ in statistical mechanics[11]means that all microstates are equally likely, and therefore the macrostate with most microstates is overwhelmingly probable. However, there is no real definition of what approximate equilibrium within a slowly changing environment in this microstates language[12]. More concretely, there is no systematic theory combining the dynamics of stochastic fluctuations with the gradient expansion. Attempts for such a theory have been made with linear response[13,15,14]and Feynman diagram techniques[14,16]. However in the relativistic regime such approaches tend to conclude that hydrodynamics is extremely non-universal[17]away from the continuum limit, in contrast with experiment at both very high (relativistic)[18], very low energy[19]energies and even everyday situations (the ”Brazil nut effect”[20])

To appreciate just how potentially revolutionary are the results described in[18,19], one should look at the supposed resolution of Hilberts 6th problem which was rewarded with a FIelds medal in 2026[6].
But the proof relies crucially on the Grad limit, the assumption that the number of degrees of freedom diverges parametrically faster than the inverse of the Knudsen number. This is exactly what results such as[18,19]show might not be applicable to ”real” fluids. Thus, the linked problems of ”what is the smallest fluid?” and ”how do thermal fluctuations backreact on fluid evolution?” are quintessentially physics questions, to be studied via experimental and theoretical tools familiar from physics.

In the non-relativistic limit, the phenomenon of spontaneous stochasticity[21]suggests that fluctuations are not just perturbations on top of a deterministic theory but emerge in the same regime as where a fluid emerges. It should be noted, in this regard, that spontaneous stochasticity has been shown to allow molecular fluctuations, i.e. exactly the fluctuations determined by microstate distributions[12]to communicate with “mesoscopic“ turbulent scales[22]. This seems to provide deep insights into mathematics issues such as Onsager’s conjecture and anomalous dissipation (which becomes driven by statistical fluctuations), but the scale separation between the microscopic and mesoscopic scale is puzzling.

Because the issue is the effect of fluctuations on scale separation,
quantum field theory techniques such as renormalization[23]therefore look like a promising tool[25,26,24,27]but the seemingly non-perturbative nature of fluid dynamics in such a regime makes a quantitative calculation problematic, as non-perturbative renormalization group techniques[28,29]are generally inapplicable to strongly time-varying problems

Recently, a rederivation of hydrodynamics has been proposed that explicitly deals with these issues[1,30,31,32,33]. The idea is that rather than treat the fluid as a deterministic system evolving through conservation equations (with gradient-expanded constitutive relations giving conserved currents), it can be thought of as a Wiener/Ito process[34], determined by an evolving partition function whose first two derivatives are determined non-perturbatively and constrained by Ward identities. To leading order[1]there is a partition function in every cell but it is always of Gaussian form. This approach has two advantages: Obviously, fluctuations can be included from the start.
But also, the existence of a partition function can be used to treat the symmetries of fluid dynamics via Ward identities. Thus, the symmetries of ideal fluid mechanics are linked to microscopic ergodicity of the microscopic degrees of freedom making up the fluid[32]. Then, the ambiguity of the definition flow in the relativistic regime[9,10]becomes a consequence of the general covariance of the theory. The purpose of this work is to explore the non-relativistic limit of such a picture, with a view to make a link with both spontaneous stochasticity and the local symmetries of non-relativistic fluid dynamics[35], and eventually the more mathematical issues discussed in the introduction.

First of all, one must be careful about what a non-relativistic limit means[36]. The Galileo group is not a subgroup of the Lorentz group so one can not get a unique limit by taking a certain number of generators to zero.
Physically, a non-relativistic continuum is obtained by takingc→∞c\rightarrow\inftyand, concurrently,μ/T→∞\mu/T\rightarrow\inftyso that the particle density is kept finite. But there is no unique way to do that and it generally results in a very different gradient expansion w.r.t. the relativistic one[37].

Symmetries provide a roadmap on how to proceed: It is easy to note that volume preserving diffeomorphism invariance is the symmetry of ideal relativistic hydrodynamics[38]and also of idealincompressiblenon-relativistic hydrodynamics[39]. Physically, volume preserving diffeomorphisms ensure the existence[38]of a conserved entropy current and a Killing vector (flow). As argued in[1], if one interprets this entropy current in a Gibbsian way, it is reasonable that volume preserving diffeomorphisms survive in a fluctuating regime because locally entropy creation can not be distinguished from a thermodynamic fluctuation.

Thus, incompressibility concurrently with the non-relativistic limit, i.e. taking the speed of soundcsc_{s}to infinity together with the speed of light might give a consistent limit.
It is empirically known that non-relativistic fluids tend to be incompressible in the low viscosity limit, especially in the turbulence regime (where incompressibility is related to scale-invariance[40]). The sort of strong interactions that ensure low viscosity will also, given the Pauli exclusion principle, ensure a large speed of sound. Of course too strong interactions in the non-relativistic regime can drive a fluid into a solid phase, where there is no volume preserving diffeomorphism symmetry and also no local equilibrium[32](solids are brittle).
However, in addition to relativity, incompressibility is incompatible with an analytical statistical partition function, something obvious from the non-local definition of pressure[41,42]as well as explicit computations from the equation of state[43,45,44].

The incompressibility assumption also invalidates the Boltzmann equation (from which hydrodynamics is often derived[6,10]), as it is based on sequential scattering, typically leading to ideal gas type laws which have a finite speed of sound.
So far in the literature the problem has been essentially treated by combining the Boltzmann equation with the assumptions that Strouhal and Mach numbers are negligible on the same scale as the Knudsen number[46]. This contradicts the actual non-relativistic kinetic equation estimate[47], wherelimm→∞cs2∼(T/m)1/2→0\lim_{m\rightarrow\infty}c_{s}^{2}\sim(T/m)^{1/2}\rightarrow 0In summary, the literature on the topic is somewhat inconsistent: Incompressibility is taken to be ”fundamental” in the mathematical treatment of non-relativistic hydrodynamics, but everybody knows it is at best an effective description. What makes this troubling is that it is not clear whether the incompressibility approximation is relevant at regimes where both turbulence and spontaneous stochasticity play a role, a question crucial in the relativistic limit[48].

Finally, the flow ambiguity that plays such a central role in[1]is collapsed by incompressibility: The Bernoulli equation[4], in its exact form∇.u=0\nabla.u=0renders the definition of flow unique. Usually the speed of sound is handled via a relation to the equation of state. From a general partition function and the Gibbs-Duhem relations[43,44,45]However, as argued in[1], a thermostatic equation of state breaks general covariance; A generally covariant hydrodynamics will have fluctuations and averages evolving in a way constrained by the gravitational Ward identity.
Together with the linear response equation, this exactly constrains the parameters of a Gaussian partition function provided this function is Gaussian.

A recent topological demonstration that incompressibility uniquely determines fluctuations and their relation with dissipation[49], via the decoupling to all orders of the microscopic and convective backreactions, offers evidence that these issues are resolvable within functional renormalization group techniques[28,29]since the Gaussian functional is a renormalization group fixed point[50]. In this picture, at microscopic scales the fluid is indeed compressible, but this manifests itself at scales unobservable in experiments made with fluids (in practice, to probe intermolecular distances fluids are inevitably destroyed). However, if one looks at fluctuations and their effect on evolution, remnants from the compressible scale manifest themselves in counterterms, which accommodate anomalous dissipation dynamics.

The next subsection will give the basic structure of how[1]and[30]play out in the non-relativistic limit. In the next sections, the details of the evolution, including non-relativistic Ward identities[51,52,53]and functional renormalization group evolution[28,29]combine with this picture.

## I.2  The basic setup

Usually hydrodynamics[4]is written in terms of energy densityee, pressurepp, molecular densitynnas well as a flow vectoruiu_{i}(or equivalentlyβi=ui/T)\beta_{i}=u_{i}/T),from which one builds, via constitutive relations, the energy momentum conserved currentTi​jT_{ij}and the molecular currentJiJ_{i}.

The basic idea behind[1,30], is to try to work directly with the conserved currents and their non-perturbative fluctuations by working out the evolution of the partition function, but approximating it at all times with a Gaussian𝒵=exp⁡[−∫Σ(βi​Ti​j+μ​Jj)​𝑑Σj]≃∏x,x′exp⁡[−12​(J−J¯T−T¯)xT​(DMTMC)x,x′−1​(J−J¯T−T¯)x′].\mathcal{Z}=\exp\left[-\int_{\Sigma}\left(\beta_{i}T^{ij}+\mu J_{j}\right)d\Sigma_{j}\right]\simeq\prod_{x,x^{\prime}}\exp\left[-\frac{1}{2}\begin{pmatrix}J-\bar{J}\\
T-\bar{T}\end{pmatrix}^{\!T}_{x}\begin{pmatrix}D&M^{T}\\
M&C\end{pmatrix}^{-1}_{x,x^{\prime}}\begin{pmatrix}J-\bar{J}\\
T-\bar{T}\end{pmatrix}_{x^{\prime}}\right].(1)

whered3​Σid^{3}\Sigma_{i}is an arbitrary vector with dimensions of the volume (the coordinates of the Lagrangian particle/volume cell),T≡Ti​j−⟨Ti​j​(x)⟩,J≡Ji−⟨Ji​(x)⟩T\equiv T_{ij}-\left\langle T_{ij}(x)\right\rangle,J\equiv J_{i}-\left\langle J_{i}(x)\right\rangleare the conserved currents andCi​j​k​l,Mi​j​k,Di​jC_{ijkl},M_{ijk},D_{ij}are the correlators between currents111note that the exponential is a scalar. Makingd3​Σid^{3}\Sigma_{i}a vector with a velocity allows us to build lagrangian co-moving coordinates of a cell and, crucially, to implement the symmetries characterizing ideal hydrodynamics[38,35], also in a fluctuating environment (where these symmetries give rise to ghost-like redundancies[1,33]) and in the distribution of microstates[32].

The basic idea in[1]is that constraints from Ward identities and linear responses giving equations of motion for⟨Ti​j​(x)⟩,⟨Ji​(x)⟩,Di​k​(x,x′),Mi​j​k​(x,x′),Ci​j​k​l​(x,x′)\left\langle T_{ij}(x)\right\rangle,\left\langle J_{i}(x)\right\rangle,D_{ik}(x,x^{\prime}),M_{ijk}(x,x^{\prime}),C_{ijkl}(x,x^{\prime}). Thus, the initial condition is not a field of flows, densities and pressures, but rather an ensemble of currents characterized by⟨Ti​j⟩,⟨Ji⟩,Di​k,Mi​j​k,Ci​j​k​l\left\langle T_{ij}\right\rangle,\left\langle J_{i}\right\rangle,D_{ik},M_{ijk},C_{ijkl}.
Once this ensemble is given at a given time, however, it can be propagated forward, thus ensuring a non-perturbative stochasticity and every timestep and the observation of local symmetries, which is related to strong hyperbolicity[30].

The Ward identity for Galilean invariance, a Noether second theorem relation relating the first and second cumulantℒ˙0​…−∇.ℒi​j​…=0,ℒi​j​…=𝒪[2]​i​j−δ​(x1−x2)​∑jaj​𝒪[1]​j,𝒪[n]≡δn​ln⁡𝒵δ​𝒥n\dot{\mathcal{L}}_{0\ldots}-\nabla.\mathcal{L}_{ij\ldots}=0,\qquad\mathcal{L}_{ij...}=\mathcal{O}_{[2]ij}-\delta(x_{1}-x_{2})\sum_{j}a_{j}\mathcal{O}_{[1]j},\qquad\mathcal{O}_{[n]}\equiv\frac{\delta^{n}\ln\mathcal{Z}}{\delta\mathcal{J}^{n}}(2)

where𝒪1\mathcal{O}_{1}can refer to averages,⟨Ti​j⟩,⟨Ji⟩\left\langle T_{ij}\right\rangle,\left\langle J_{i}\right\rangle, and𝒪2\mathcal{O}_{2}to second cumulantsDi​k,Mi​j​k,Ci​j​k​lD_{ik},M_{ijk},C_{ijkl}(eq. 12 of[1]gives a concrete example. Here𝒥\mathcal{J}is a generic source).

By the linear response from[13,14,15], we mean an integral equation obtained from an analytical continuation of𝒪2\mathcal{O}_{2}𝒪[1]​(t+Δ​t)=∫tt+Δ​t𝑑t′​𝒪[2]​(t,t′)​𝒪[1]​(t′),𝒪~​(t,k)=12​i​(𝒪~​(t,k)𝒪~​(−i​ϵ​t,k)−1)\mathcal{O}_{[1]}(t+\Delta t)=\int_{t}^{t+\Delta t}dt^{\prime}\mathcal{O}_{[2]}(t,t^{\prime})\mathcal{O}_{[1]}(t^{\prime}),\qquad\tilde{\mathcal{O}}(t,k)=\frac{1}{2i}\left(\frac{\tilde{\mathcal{O}}(t,k)}{\tilde{\mathcal{O}}(-i\epsilon t,k)}-1\right)(3)

Eq. (2) and Eq. (3) are two equations with two unknowns,𝒪[1.2]\mathcal{O}_{[1.2]}so in principle they are exactly the ingredients needed to propagate the parameters of Eq. (1) from their initial condition values.

Non-perturbative Renormalization group flows can then be implemented at the operator lever by considering the Fourier transforms of the operators.𝒪~1,2​i1,i2,…​(k→,t)=∫d3​x​𝒪1,2​i1,i2,…​exp⁡[i​(k→⋅x→)]={𝒪~1,2U​Vk≥k0𝒪~1,2I​Rg≤k0\tilde{\mathcal{O}}_{1,2i_{1},i_{2},...}(\vec{k},t)=\int d^{3}x\,\mathcal{O}_{1,2i_{1},i_{2},...}\exp\left[i\left(\vec{k}\cdot\vec{x}\right)\right]=\left\{\begin{array}[]{cc}\tilde{\mathcal{O}}^{UV}_{1,2}&k\geq k_{0}\\
\tilde{\mathcal{O}}^{IR}_{1,2}&g\leq k_{0}\end{array}\right.(4)

where IR/UV distinguishes between the infrared (incompressible) and ultraviolet (compressible, and eventually fully relativistic) regimes. The Gaussian approximation implicit in Eq. (1) allows us to determine a renormalization group flow[23,28,29].ln⁡𝒵​[k0,J,T,D,M,T]=ln⁡𝒵​[k0+Δ​k0,J+Δ​J,T+Δ​T,D+Δ​D,M+Δ​M]\ln\mathcal{Z}\left[k_{0},J,T,D,M,T\right]=\ln\mathcal{Z}\left[k_{0}+\Delta k_{0},J+\Delta J,T+\Delta T,D+\Delta D,M+\Delta M\right](5)

and to find the fixed point of this evolution. In the Gaussian Wiener/Ito process, this is all we need.

In the rest of the paper, we shall fill in these ingredients in detail. We start with finding the second order Galilean group Ward identity, using the methods of[51,52,53], for both compressible and incompressible fluids. We then work out in detail the renormalization group equations relating the two, and find the exact form of the linear response equations.

## II  The evolution of the fluctuation tensor: Ward identities and the renormalization group flow

## II.1  Ward identities

We start with computing the second order Ward identities in the Galilean case, following the Newton-Cartan formalism introduced in[51,52]and proceeding in Fourier space, where∂i→ki,dd​t→w\partial_{i}\rightarrow k_{i},\frac{d}{dt}\rightarrow w. We have for the fundamental connected correlatorsDi​k​(x,y)=⟨Ji​(x)​Jk​(y)⟩c,Mi​j​k​(x,y)=⟨Ti​j​(x)​Jk​(y)⟩c,Ci​j​k​l​(x,y)=⟨Ti​j​(x)​Tk​l​(y)⟩cD_{ik}(x,y)=\left\langle J_{i}(x)J_{k}(y)\right\rangle_{c},\ M_{ijk}(x,y)=\left\langle T_{ij}(x)J_{k}(y)\right\rangle_{c},\ C_{ijkl}(x,y)=\left\langle T_{ij}(x)T_{kl}(y)\right\rangle_{c}decomposing the current and stress tensor asJi=Jimacro+jimicro,Ti​j=Ti​jmacro+τi​jmicroJ_{i}=J_{i}^{\mathrm{macro}}+j_{i}^{\mathrm{micro}},\ T_{ij}=T_{ij}^{\mathrm{macro}}+\tau_{ij}^{\mathrm{micro}}. The Ward identities must therefore take the formω​Di​kmacro−kj​Mi​j​kmacro−Δi​kJ​J=0,\displaystyle\omega D_{ik}^{\mathrm{macro}}-k_{j}M_{ijk}^{\mathrm{macro}}-\Delta_{ik}^{JJ}=0,(6)ω​Mk​l​imacro−kj​Ci​j​k​lmacro−Δi​k​lJ​T=0,\displaystyle\omega M_{kli}^{\mathrm{macro}}-k_{j}C_{ijkl}^{\mathrm{macro}}-\Delta_{ikl}^{JT}=0,(7)

whereΔi​kJ​J=−ω​Di​kmixed+kj​Mi​j​kmixed,Δi​k​lJ​T=−ω​Mk​l​imixed+kj​Ci​j​k​lmixed\Delta_{ik}^{JJ}=-\omega D_{ik}^{\mathrm{mixed}}+k_{j}M_{ijk}^{\mathrm{mixed}},\Delta_{ikl}^{JT}=-\omega M_{kli}^{\mathrm{mixed}}+k_{j}C_{ijkl}^{\mathrm{mixed}}222The mixed correlation function is⟨𝒪macro,𝒪micro⟩\left\langle\mathcal{O}^{\mathrm{macro}},\mathcal{O}^{\mathrm{micro}}\right\rangle. The corrections satisfy constraints coming from Galilean symmetry. Putting everything together in the (6) and (7), the Ward identities will have the form for the incompressible construction (k0=ωk_{0}=\omegais also used in the non-relativistic equation for simplicity)ω2​(Di​jmacro−Di​jmixed)−2​ω​kl​Mi​j​lmixed−kl​kk​(Ci​j​l​kmacro−Ci​j​l​kmixed)=0​{𝒪macro,|k|≤k0,|ω|≤k0/c,𝒪mixed,|k|≥k0,|ω|≤k0/c,𝒪micro,|ω|≥k0/c.\omega^{2}(D^{\mathrm{macro}}_{ij}-D^{\mathrm{mixed}}_{ij})-2\omega k^{l}M^{\mathrm{mixed}}_{ijl}-k^{l}k^{k}(C^{\mathrm{macro}}_{ijlk}-C^{\mathrm{mixed}}_{ijlk})=0\begin{cases}\mathcal{O}^{\mathrm{macro}},&|k|\leq k_{0},\ |\omega|\leq k_{0}/c,\\[6.00006pt]
\mathcal{O}^{\mathrm{mixed}},&|k|\geq k_{0},\ |\omega|\leq k_{0}/c,\\[6.00006pt]
\mathcal{O}^{\mathrm{micro}},&|\omega|\geq k_{0}/c.\end{cases}(8)

i.e.𝒪macro\mathcal{O}^{\mathrm{macro}}the non-relativistic incompressible form fork≤k0,w≤k0/ck\leq k_{0},w\leq k_{0}/c,𝒪mixed\mathcal{O}^{\mathrm{mixed}}non-relativistic compressible fork≤k0,w≥k0/ck\leq k_{0},w\geq k_{0}/cand𝒪micro\mathcal{O}^{\mathrm{micro}}relativistic otherwise. At the critical frequencies the terms need to match, but not their derivatives, for reasons that we shall explain in the remainder of the paper. The correlations function becomeDi​kmacro=ρ02​⟨ui​uk⟩c,D_{ik}^{\mathrm{macro}}=\rho_{0}^{2}\left\langle u_{i}u_{k}\right\rangle_{c},andkj​kl​Ci​l​j​kmacro=−η2​k4​⟨ui​uk⟩k_{j}k_{l}C_{iljk}^{\mathrm{macro}}=-\eta^{2}k^{4}\left\langle u_{i}u_{k}\right\rangle. Fork≤k0≡ρ01/3k\leq k_{0}\equiv\rho_{0}^{1/3}the fluid is effectively incompresible (so the only correlators are velocity and pressure) above that scale compressibility breaks down. At that point the Ward identity will be either the fully compressible one, or eventually the Lorentz covariant one derived in[1]and extended to finite chemical potential in[30].

The relativistic fluctuating statistical mechanics can, for the purposes of this paper, be considered UV-complete since a Gaussian renormalization group fixed point should exist[1,50].

## II.2  Renormalization group structure

It seems physically inappropriate here to put the full Lorentz invariant Ward identity, given that we know that for most fluids (such as water) velocities at molecular distances are still well below relativistic effects, so it might be logical to concentrate on just the first two columns of Eq. (8), and this might well be the case. However, this is physically irrelevant, since our purpose will be to use the Ward identities and a Gaussian ansatz to build a functional renormalization group (FRG)[23,28,29]type equation linking the incompressible non-relativistic and the relativistic limit (which are linked by the local volume preserving diffeomorphism symmetries). Physically, the point is that both the compressible and the Lorentz scale are inaccessible by experiments where the fluid is there, and the FRG implements this invisibility in the dynamics, with the residual effects of the macroscopic dynamics in the counterterms.

We speculate that corrections to the averages⟨J​(x)⟩,⟨T​(x)⟩\left\langle J(x)\right\rangle,\left\langle T(x)\right\rangle(Eq. (1)), represent what mathematicians call anomalous dissipation[7], roughly the backreaction of stochastic fluctuations at the molecular scale to macroscopic dissipative currents. The corrections to the fluctuationsC,M,DC,M,Drepresent "wildness" (from what mathematicians call Wild solutions[8]), I.e. the spontaneous microscopic turbulence undetectable on macroscopic scales.

We realize this is highly speculative for concepts such as wild solutions, and conjectures such as Onsager‘s arise from abstract mathematics, often within highly idealized non-physical definitions used in rigorous proofs[8,25,7]. But we point out to the conceptual similarity of weak solutions, on which such results are based[7]to what physicists call coarse graining, and universality under test function choice to what physicists mean by renormalization[23], to argue this conjecture is not implausible

Using the notation[28], the standard Legendre transformations areWk​[𝒥,T]=ln⁡Zk​[𝒥,T],W_{k}[\mathcal{J},T]=\ln Z_{k}[\mathcal{J},T],(9)

Thus,𝒥i=δ​Wkδ​ai,Ti​j=δ​Wkδ​bi​j.\mathcal{J}_{i}=\frac{\delta W_{k}}{\delta a_{i}},\quad T_{ij}=\frac{\delta W_{k}}{\delta b_{ij}}.(10)

The Ward identities and the Gaussian ansatz are the tools used to construct and constrain this flow, but they are not separate endpoints or additional physical regimes.Γk​[Φ]=Φ⋅(JT)−Wk​[𝒥,T]−Δ​Sk​[Φ],\Gamma_{k}[\Phi]=\Phi\cdot\left(\begin{smallmatrix}J\\
T\end{smallmatrix}\right)-W_{k}[\mathcal{J},T]-\Delta S_{k}[\Phi],(11)

whereΔ​Sk​[Φ]=12​∫qΦA​(−q)​Rk,A​B​(q)​ΦB​(q)\Delta S_{k}[\Phi]=\frac{1}{2}\int_{q}\Phi_{A}(-q)\,R_{k,AB}(q)\,\Phi_{B}(q). The exact flow equation becomes∂kΓk=12​Tr⁡[(Γk(2)+Rk)−1​∂kRk]\partial_{k}\Gamma_{k}=\frac{1}{2}\operatorname{Tr}\left[\left(\Gamma_{k}^{(2)}+R_{k}\right)^{-1}\partial_{k}R_{k}\right](12)

wheret=ln⁡(Λk)t=\ln\left(\frac{\Lambda}{k}\right)and the∂kRk\partial_{k}R_{k}contains not only the ordinary flow terms, but also a contribution proportional toδ​(k−k0)\delta(k-k_{0}), which represents the sharp matching at the compressibility threshold, indicated in (8), and acts as a momentum-shell selector.∂kRk=Θ​(k0−k)​∂kRk<+Θ​(k−k0)​∂kRk>+δ​(k−k0)​(Rk>−Rk<)\partial_{k}R_{k}=\Theta(k_{0}-k)\,\partial_{k}R_{k}^{<}+\Theta(k-k_{0})\,\partial_{k}R_{k}^{>}+\delta(k-k_{0})\left(R_{k}^{>}-R_{k}^{<}\right)(13)

whereRk<R_{k}^{<}andRk>R_{k}^{>}are the regulators used in the infrared incompressible and compressible ultraviolet theory, respectively. The last term in (13) accounts for the abrupt change in the set of active degrees of freedom at the crossover scale. Low-momentum modes are suppressed by a scale-dependent quadratic term, producing a scale-dependent effective action that interpolates between microscopic and full effective descriptions. The full propagator isGκ,A​B​(q)=(Γk(2)+Rk)−1=(Dκ,i​j​(q)Mκ,j∣k​l​(−q)Mκ,i∣l​m​(q)Cκ,i​j∣l​m​(q)).G_{\kappa,AB}(q)=\bigg(\Gamma_{k}^{(2)}+R_{k}\bigg)^{-1}=\begin{pmatrix}D_{\kappa,ij}(q)&M_{\kappa,j\mid kl}(-q)\\[6.0pt]
M_{\kappa,i\mid lm}(q)&C_{\kappa,ij\mid lm}(q)\end{pmatrix}.(14)

whereκ\kappais the running scale. As incompressibility is a macroscopic limit, not a fundamental microscopic identity.Γk⟶{Γinc,NR,for​k​in the incompressible non-relativistic regime,Γrel,for​k​in the compressible relativistic regime.\Gamma_{k}\longrightarrow\begin{cases}\Gamma_{\mathrm{inc,NR}},&\text{for }k\text{ in the incompressible non-relativistic regime},\\[4.0pt]
\Gamma_{\mathrm{rel}},&\text{for }k\text{ in the compressible relativistic regime}.\end{cases}(15)

This is the complete formal FRG skeleton:Γrel→k:Λ→0Wetterich equationΓinc,NR.\Gamma_{\mathrm{rel}}\;\xrightarrow[\;k:\,\Lambda\rightarrow 0\;]{\text{Wetterich equation}}\;\Gamma_{\mathrm{inc,NR}}.(16)

Write the effective action asΓκ=Γκ,inc+Γκ,comp+Γκ,E,\Gamma_{\kappa}=\Gamma_{\kappa,\mathrm{inc}}+\Gamma_{\kappa,\mathrm{comp}}+\Gamma_{\kappa,E},(17)

where the sectors are selected in (8) by the appropriate step functions and the boundary conditions are in (52). Following the standard Wetterich construction, the infrared effective average action is obtained through the modified Legendre transform,Γκinc​[Φ>]=Φ>⋅(JT)−Wκinc​[JT]−Δ​Sκ​[Φ>],\Gamma_{\kappa}^{\mathrm{inc}}[\Phi_{>}]=\Phi_{>}\cdot\left(\begin{smallmatrix}J\\
T\end{smallmatrix}\right)-W_{\kappa}^{\mathrm{inc}}[J_{T}]-\Delta S_{\kappa}[\Phi_{>}],(18)

The effective average action can be decomposed asΓκcomp​[Φ<]=ΓNS​[Φ>]+Δ​Γκ​[Φ>,Φ<],\Gamma_{\kappa}^{\mathrm{comp}}[\Phi_{<}]=\Gamma_{\mathrm{NS}}[\Phi_{>}]+\Delta\Gamma_{\kappa}[\Phi_{>},\Phi_{<}],(19)

whereΓNS\Gamma_{\mathrm{NS}}is the classical incompressible Navier–Stokes action, andΔ​Γκ\Delta\Gamma_{\kappa}contains renormalizations of the transport coefficients, nonlocal interactions, higher-order transverse vertices, noise corrections, and every operator compatible with the symmetries of the incompressible effective theory. Consequently, the infrared dynamics is entirely described on the transverse field manifold,Γκ≪k0inc​[Φ>]=Γκ≪k0​[Φ],\Gamma_{\kappa\ll k_{0}}^{\mathrm{inc}}[\Phi_{>}]=\Gamma_{\kappa\ll k_{0}}[\Phi],(20)

although the underlying microscopic theory remains fully compressible. The transverse one-particle-irreducible two-point function obtained from the compressible theory must reproduce the incompressible effective theory at momenta much smaller than the crossover scale,ΓT​T(2),comp​(κ)=Γ(2),inc​(κ)+𝒪​[(|κ|k0)n],|κ|≪k0,\Gamma^{(2),\mathrm{comp}}_{TT}(\kappa)=\Gamma^{(2),\mathrm{inc}}(\kappa)+\mathcal{O}\!\left[\left(\frac{|\kappa|}{k_{0}}\right)^{n}\right],\qquad|\kappa|\ll k_{0},(21)

wheren>0n>0is determined by the leading irrelevant operator generated during the elimination of the compressible sector333We present the matching condition in (52).. The terms suppressed by powers ofnncorrespond to the compressible microscopic theory and the incompressible effective theory described by the same low-energy physics. Equivalently, the transverse propagators satisfyGe​f​f|i​jcomp​(κ)=Gi​jinc​(κ),|κ|≪k0.G_{eff|ij}^{\mathrm{comp}}(\kappa)=G_{ij}^{\mathrm{inc}}(\kappa),\qquad|\kappa|\ll k_{0}.(22)

whereGe​f​f|i​jcompG_{eff|ij}^{\mathrm{comp}}is the effective propagator after integrating out the compressible fields. These matching conditions guarantee that the low-energy transverse observables are independent of whether they are computed directly in the compressible microscopic theory or in the incompressible effective
theory, up to corrections suppressed by powers of|κ|/k0|\kappa|/k_{0}.

## II.3  Compressible Fluids

The scale-dependent effective average action is written asΓκ=Γκcontinuity+Γκmomentum+Γκnoise.\Gamma_{\kappa}=\Gamma_{\kappa}^{\mathrm{continuity}}+\Gamma_{\kappa}^{\mathrm{momentum}}+\Gamma_{\kappa}^{\mathrm{noise}}.(23)

For the shear viscosity∂tηκ=ρ0​∂∂p2​∂tΓκ,π¯a​πa(2)​(ω,𝐩)|ω=0,𝐩=0.\partial_{t}\eta_{\kappa}=\rho_{0}\left.\frac{\partial}{\partial p^{2}}\,\partial_{t}\Gamma_{\kappa,\bar{\pi}_{a}\pi_{a}}^{(2)}(\omega,\mathbf{p})\right|_{\omega=0,\mathbf{p}=0}.(24)

Hereπi=ρ​ui\pi_{i}=\rho u_{i}denotes the momentum density, andπ¯i\bar{\pi}_{i}is the corresponding response field444π¯\bar{\pi}is introduced to formulate the stochastic dynamics and generate response functions, rather than an independently measurable hydrodynamic variable, so that the stochastic equation of motion can be written as an action.. For the sound speed∂tcs,κ2=1i​∂∂p​∂tΓκ,π¯1​ϱ(2)​(0,𝐩)|𝐩=0.\partial_{t}c_{s,\kappa}^{\,2}=\frac{1}{i}\left.\frac{\partial}{\partial p}\,\partial_{t}\Gamma_{\kappa,\bar{\pi}_{1}\varrho}^{(2)}(0,\mathbf{p})\right|_{\mathbf{p}=0}.(25)

Herecs,κ2=∂pκ/∂ρ|ρ0,κc_{s,\kappa}^{\,2}=\left.\partial p_{\kappa}/\partial\rho\right|_{\rho_{0,\kappa}}is the running adiabatic pressure response, i.e the speed of sound.

Usually the speed of sound is thought to be inherently related to the equation of state, via[44]through the Gibbs-Duhem relationsln⁡(TT0)=∫μ0μρ′​d​μcs2ρ′​(d​ρ′d​p)s−μ​ρ′\ln\left(\frac{T}{T_{0}}\right)=\int_{\mu_{0}}^{\mu}\frac{\rho^{\prime}d\mu}{\frac{c_{s}^{2}}{\rho^{\prime}}\left(\frac{d\rho^{\prime}}{dp}\right)_{s}-\mu\rho^{\prime}}(26)

Eq. (25) can be thought of as a correction to this due to hydrodynamic response to thermal fluctuations looking like a compressible sound wave. In the long-wavelength incompressible regime, this integral diverges so these perturbations would be indetectable at the bulk (they would correspond to “fluctuations of the boundary“, by definition undetectable). But a microscopic compressible scale means that Eq. (26) will receive contributions from the counter-term Eq. (25).

Similarly For the bulk (breathing mode) component,∂tζκ=ρ0​∂∂p2​∂tΓκ,π¯1​π1(2)​(ω,𝐩)|ω=0,𝐩=0−34​∂tηκ.\partial_{t}\zeta_{\kappa}=\rho_{0}\left.\frac{\partial}{\partial p^{2}}\,\partial_{t}\Gamma_{\kappa,\bar{\pi}_{1}\pi_{1}}^{(2)}(\omega,\mathbf{p})\right|_{\omega=0,\mathbf{p}=0}-\frac{3}{4}\partial_{t}\eta_{\kappa}.(27)

Once again, an incompressible limit would make Eq. (27) undetectable, but if incompressibility is cutoff at a critical scale this mode will appear.
As we argued earlier, for non-relativistic fluids these modes are themselves considered fluctuations, since the breakdown of compressibility (where such sound and bulk modes are possible) only appear on microscopic scales.
Thus, these modes will be associated to counterterms to the fluctuation operator.

## II.4  Incompressible Fluids

The incompressible effective average action isΓκ​[u,u¯]=Γκ,2+Γκ,3,\Gamma_{\kappa}[u,\bar{u}]=\Gamma_{\kappa,2}+\Gamma_{\kappa,3},(28)

The evaluation of the Wetterich trace in appendix∂tΓκ=12​Tr⁡[Gκ​∂tRκ]=νκ​κ53​π​Zκ.\partial_{t}\Gamma_{\kappa}=\frac{1}{2}\operatorname{Tr}\left[G_{\kappa}\,\partial_{t}R_{\kappa}\right]=\frac{\nu_{\kappa}\kappa^{5}}{3\pi Z_{\kappa}}\,.(29)

whereνκ\nu_{\kappa}is the running kinematic viscosity, andZκZ_{\kappa}is the wave-function renormalization (ui=Zκ−1/2​ui(R)u_{i}=Z_{\kappa}^{-1/2}u_{i}^{(\mathrm{R})}),κ\kappacomes entirely from dimensional analysis.∂tΓκ,u¯i​uj(2)​(p)|3×3\displaystyle\left.\partial_{t}\Gamma^{(2)}_{\kappa,\bar{u}_{i}u_{j}}(p)\right|_{3\times 3}=∂~t​∫qVi​a​b​(p,q)​Cκ,a​a′inc​(q)​Gκ,b​b′R​(p−q)​Vj​a′​b′​(−p,q−p)\displaystyle=\widetilde{\partial}_{t}\int_{q}V_{iab}(p,q)\,C^{\mathrm{inc}}_{\kappa,aa^{\prime}}(q)\,G^{R}_{\kappa,bb^{\prime}}(p-q)\,V_{ja^{\prime}b^{\prime}}(-p,q-p)=∂~t​∫ω′,𝐪2​Dκ​(𝐪)Zκ2​ω′⁣2+Aκ2​(𝐪)​Vi​a​b​(𝐩,𝐪)​Pa​a′T​(𝐪)​Pb​b′T​(𝐩−𝐪)​Vj​a′​b′​(−𝐩,𝐪−𝐩)−i​Zκ​(ω−ω′)+Aκ​(𝐩−𝐪),\displaystyle=\widetilde{\partial}_{t}\int_{\omega^{\prime},\mathbf{q}}\frac{2D_{\kappa}(\mathbf{q})}{Z_{\kappa}^{2}\omega^{\prime 2}+A_{\kappa}^{2}(\mathbf{q})}\,\frac{V_{iab}(\mathbf{p},\mathbf{q})\,P^{T}_{aa^{\prime}}(\mathbf{q})\,P^{T}_{bb^{\prime}}(\mathbf{p}-\mathbf{q})\,V_{ja^{\prime}b^{\prime}}(-\mathbf{p},\mathbf{q}-\mathbf{p})}{-iZ_{\kappa}(\omega-\omega^{\prime})+A_{\kappa}(\mathbf{p}-\mathbf{q})},(30)

withq=(ω,p)q=(\omega,p)and the∂~t\widetilde{\partial}_{t}denotes the scale derivative acting only on the regulator as it is standard in the Wetterich formalism.∂tηκ=12​∂∂p2​Pi​jT​(𝐩)​∂tΓκ,u¯i​uj(2)​(0,𝐩)|𝐩=0.\partial_{t}\eta_{\kappa}=\left.\frac{1}{2}\frac{\partial}{\partial p^{2}}\,P_{ij}^{T}(\mathbf{p})\,\partial_{t}\Gamma^{(2)}_{\kappa,\bar{u}_{i}u_{j}}(0,\mathbf{p})\right|_{\mathbf{p}=0}.(31)

Comparing with Eq. (24) of the previous section and
Matching symmetries, it is clear that Eq. (31) can be thought of as the anomalous dissipation correction
to the shear viscosity. The Eq. (24) on the other hand should be thought as a microscopic statistical fluctuation (as it occurs in the compressible regime) corresponding to the quantum numbers of a shear.

## III  Average evolution via linear response

The Ward identities described in the previous section prove one constraint relating the average and the fluctuation of the distribution. The second constraint is the linear response equation⟨Ji​(x,t+Δ​t)⟩=∫tt+Δ​t𝑑x′​𝑑t′​[𝒟i​k​(x−x′,t−t′)​⟨Jk​(x′,t′)⟩+ℳi​k​l​(x−x′,t−t′)​⟨Tk​l​(x′,t′)⟩]\left\langle J_{i}(x,t+\Delta t)\right\rangle=\int_{t}^{t+\Delta t}dx^{\prime}dt^{\prime}\left[\mathcal{D}_{ik}(x-x^{\prime},t-t^{\prime})\left\langle J_{k}(x^{\prime},t^{\prime})\right\rangle+\mathcal{M}_{ikl}(x-x^{\prime},t-t^{\prime})\left\langle T^{kl}(x^{\prime},t^{\prime})\right\rangle\right](32)⟨Ti​k​(x,t+Δ​t)⟩=∫tt+Δ​t𝑑x′​𝑑t′​[𝒞i​k​l​m​(x−x′,t−t′)​⟨Tl​m​(x′,t′)⟩+ℳi​k​mT​(x−x′,t−t′)​⟨Jm​(x′,t′)⟩]\left\langle T_{ik}(x,t+\Delta t)\right\rangle=\int_{t}^{t+\Delta t}dx^{\prime}dt^{\prime}\left[\mathcal{C}_{iklm}(x-x^{\prime},t-t^{\prime})\left\langle T_{lm}(x^{\prime},t^{\prime})\right\rangle+\mathcal{M}^{T}_{ikm}(x-x^{\prime},t-t^{\prime})\left\langle J^{m}(x^{\prime},t^{\prime})\right\rangle\right](33)

where theℱ\mathcal{F}(representing𝒞,𝒟,ℳ\mathcal{C},\mathcal{D},\mathcal{M}) is, in analogous notation[1,30], obtained from the fourier transforms of their correspondingFF(representingC,M,DC,M,Dof Eq. (1)) via Eq. (3). Here we note that equations Eq. (33) and Eq. (32)
are convolutions in configuration space, so their Fourier transforms are multiplications⟨J~i​(k,t+Δ​t)⟩\displaystyle\left\langle\tilde{J}_{i}(k,t+\Delta t)\right\rangle=∫tt+Δ​t𝑑t′​[𝒟~i​k​(k′,t−t′)​⟨J~k​(k,t′)⟩+ℳ~i​k​l​(k,t−t′)​⟨T~k​l​(k,t′)⟩]\displaystyle=\int_{t}^{t+\Delta t}dt^{\prime}\left[\tilde{\mathcal{D}}_{ik}(k^{\prime},t-t^{\prime})\left\langle\tilde{J}_{k}(k,t^{\prime})\right\rangle+\tilde{\mathcal{M}}_{ikl}(k,t-t^{\prime})\left\langle\tilde{T}^{kl}(k,t^{\prime})\right\rangle\right](34)⟨T~i​k​(x,t+Δ​t)⟩\displaystyle\left\langle\tilde{T}_{ik}(x,t+\Delta t)\right\rangle=∫tt+Δ​t𝑑t′​[𝒞~i​k​l​m​(k,t−t′)​⟨T~l​m​(k,t′)⟩+ℳ~i​k​mT​(k,t−t′)​⟨J~m​(k,t′)⟩]\displaystyle=\int_{t}^{t+\Delta t}dt^{\prime}\left[\tilde{\mathcal{C}}_{iklm}(k,t-t^{\prime})\left\langle\tilde{T}^{lm}(k,t^{\prime})\right\rangle+\tilde{\mathcal{M}}^{T}_{ikm}(k,t-t^{\prime})\left\langle\tilde{J}^{m}(k,t^{\prime})\right\rangle\right](35)

And, as explained in the previous section, the correlation functions above and belowk0k_{0}are very different, with the microscopic ones being compressible and macroscopic ones being incompressible.⟨J~i​(k,t)⟩={ρ0​uiT+⟨Δ​Jicomp→inc⟩k≤k0ρ0​(δi​j−ki​kjk2)​uj​(k,t),k≥k0\left\langle\tilde{J}_{i}(k,t)\right\rangle=\left\{\begin{array}[]{cc}\rho_{0}\,u_{i}^{T}+\left\langle\Delta J_{i}^{\mathrm{comp}\rightarrow\mathrm{inc}}\right\rangle&k\leq k_{0}\\
\rho_{0}\left(\delta_{ij}-\frac{k_{i}k_{j}}{k^{2}}\right)u_{j}(k,t),&k\geq k_{0}\end{array}\right.(36)

where⟨Δ​Jicomp→inc​(p)⟩≃lim|p|/k0→0|ω|/(cs​k0)→0Pi​jT​(p)​∫q∈compVκ,j​A​B​(p,q,−p−q)​Gκ,compA​B​(q)​Φmacro​(p)+𝒪​(Φmacro2)\left\langle\Delta J_{i}^{\mathrm{comp}\rightarrow\mathrm{inc}}(p)\right\rangle\simeq\lim_{\begin{subarray}{c}|p|/k_{0}\rightarrow 0\\[2.0pt]
|\omega|/(c_{s}k_{0})\rightarrow 0\end{subarray}}P_{ij}^{T}(p)\int_{q\in\mathrm{comp}}V_{\kappa,jAB}(p,q,-p-q)\,G_{\kappa,\mathrm{comp}}^{AB}(q)\,\Phi_{\mathrm{macro}}(p)+\mathcal{O}\!\left(\Phi_{\mathrm{macro}}^{2}\right)(37)

whereVκ,j​A​BV_{\kappa,jAB}is the one-particle-irreducible three-point of full compressible vertex555A,B run over all compressible microscopic degrees of freedom of the FRG field multiplet.. This “compressible current“Jicomp→incJ_{i}^{\mathrm{comp}\rightarrow\mathrm{inc}}arising from the counterterm can be thought of as the anomalous dissipation diffusive current, creating a turbulent flow of molecules from the chaotic microscopic molecular motion, at the scale, comparable with molecular distance, where dynamics is also compressible. The energy-momentum tensor is more complicated but follows the same pattern⟨T~k​i​(k,t)⟩={⟨ρ0∫qukT(q,t)uiT(k−q,t)−iη(kkuiT+kiukT)−ρ0δk​ikmkn/k2∫qumT(q,t)unT(k−q,t)⟩+⟨ΔTk​icomp→inc⟩k≤k0ρ​uk​ui+p​(ρ,s)​δk​i−η​(∂kui+∂iuk−23​δk​i​∂ℓuℓ)−ζ​δk​i​∂ℓuℓk≥k0\left\langle\tilde{T}_{ki}(k,t)\right\rangle=\left\{\begin{array}[]{cc}\langle\rho_{0}\int_{q}u_{k}^{T}(q,t)\,u_{i}^{T}(k-q,t)-i\eta\left(k_{k}u_{i}^{T}+k_{i}u_{k}^{T}\right)-\\
\rho_{0}\,\delta_{ki}\,k_{m}k_{n}/k^{2}\int_{q}u_{m}^{T}(q,t)\,u_{n}^{T}(k-q,t)\rangle+\left\langle\Delta T_{ki}^{\mathrm{comp}\rightarrow\mathrm{inc}}\right\rangle&k\leq k_{0}\\
\rho\,u_{k}u_{i}+p(\rho,s)\,\delta_{ki}-\eta\left(\partial_{k}u_{i}+\partial_{i}u_{k}-\frac{2}{3}\,\delta_{ki}\,\partial_{\ell}u_{\ell}\right)-\zeta\,\delta_{ki}\,\partial_{\ell}u_{\ell}&k\geq k_{0}\end{array}\right.(38)

The anomalously dissipative energy momentum tensor, therefore, should generally be expanded as⟨Δ​Tk​icomp→inc​(p)⟩≃∫qVκ,k​i;A​B(1)​(p,q,−p−q)​Gκ,compA​B​(q)​Φmacro​(p)+12​∫p1∫q∈compΦmacro,C​(p1)\displaystyle\left\langle\Delta T_{ki}^{\mathrm{comp}\rightarrow\mathrm{inc}}(p)\right\rangle\simeq\int_{q}V_{\kappa,ki;AB}^{(1)}(p,q,-p-q)\,G_{\kappa,\mathrm{comp}}^{AB}(q)\,\Phi_{\mathrm{macro}}(p)+\frac{1}{2}\int_{p_{1}}\int_{q\in\mathrm{comp}}\Phi_{\mathrm{macro},C}(p_{1})×Gκ,compA​B​(q)​Vκ,k​i;A​B;C​D(2)​(p,q,−q−p;p1,p−p1)​Φmacro,D​(p−p1)+𝒪​(Φmacro3)\displaystyle\times G_{\kappa,\mathrm{comp}}^{AB}(q)V_{\kappa,ki;AB;CD}^{(2)}\left(p,q,-q-p;p_{1},p-p_{1}\right)\,\Phi_{\mathrm{macro},D}(p-p_{1})+\mathcal{O}\!\left(\Phi_{\mathrm{macro}}^{3}\right)(39)

whereVκ,k​i;A​B(1)​(p,q,−p−q)V_{\kappa,ki;AB}^{(1)}(p,q,-p-q)connects one external incompressible stress insertion, one external macroscopic field, and
two internal compressible fields. TheGκ,comp​V(2)G_{\kappa,\mathrm{comp}}V^{(2)}carries the memory of the eliminated compressible physics into the effective incompressible stress tensor. It measures how the eliminated compressible microscopic sector modifies the quadratic constitutive relation between two macroscopic incompressible fields. The first line modifies the stress terms linear in the macroscopic field, for example the effective shear response. The second line modifies the quadratic convective and pressure structures.
as well as the correlators

We now proceed to find the anomalous contribution to the fluctuations, which very roughly corresponds to “the wildness“ ([8]),the backreaction of the macroscopic turbulence on microscopic fluctuations and in general microstate distributions.D~i​j​k​l​(k,t)={Pi​kT​DTinc−Dκresk≤k0Pi​k​DT+ki​kk​DLk≥k0\tilde{D}_{ijkl}(k,t)=\left\{\begin{array}[]{cc}P_{ik}^{T}\,D_{T}^{\mathrm{inc}}-D_{\kappa}^{\mathrm{res}}&k\leq k_{0}\\
P_{ik}\,D_{T}+k_{i}k_{k}\,D_{L}&k\geq k_{0}\end{array}\right.(40)

whereDT=2​T​Pi​kT​(δi​j−ki​kj)​ηω2+(η​k2/ρ)2D_{T}=\frac{2T\,P^{T}_{ik}(\delta^{ij}-k^{i}k^{j})\eta\,}{\omega^{2}+\left(\eta k^{2}/\rho\right)^{2}}, andDL=2​T​ki​kj​ω2​[ζ+43​η](cs2​k2−ω2)2+γL2​ω2​k4D_{L}=\frac{2Tk^{i}k^{j}\omega^{2}\left[\zeta+\frac{4}{3}\,\eta\right]}{\left(c_{s}^{2}k^{2}-\omega^{2}\right)^{2}+\gamma_{L}^{2}\omega^{2}k^{4}}.M~k​i​m​(k,t)={Mi​j∣kinc−Mκresk≤k0ωk2​[ki​Pj​kT+kj​Pi​kT]​DT+Hi​j​kkk​DLk≥k0\tilde{M}_{kim}(k,t)=\left\{\begin{array}[]{cc}M_{ij\mid k}^{\mathrm{inc}}-M_{\kappa}^{\mathrm{res}}&k\leq k_{0}\\
\frac{\omega}{k^{2}}\left[k_{i}P_{jk}^{T}+k_{j}P_{ik}^{T}\right]D_{T}+H_{ij}\frac{k_{k}}{k}\,D_{L}&k\geq k_{0}\end{array}\right.(41)

whereHi​j=[ωk2​ki​kj+r​Pi​jT]H_{ij}=\left[\frac{\omega}{k^{2}}k_{i}k_{j}+rP_{ij}^{T}\right]andr=3​ζ+4​η3​ζ−2​η​kω+3​ζ+4​η2​η​ω3​cs2​kr=\frac{3\zeta+4\eta}{3\zeta-2\eta}\,\frac{k}{\omega}+\frac{3\zeta+4\eta}{2\eta}\,\frac{\omega}{3c_{s}^{2}k}. Equivalently, defining the pressure-projected tensorQi​j∣m​n​(k)=12​(δi​m​δj​n+δi​n​δj​m)−δi​j​km​knk2Q_{ij\mid mn}(k)=\frac{1}{2}\left(\delta_{im}\delta_{jn}+\delta_{in}\delta_{jm}\right)-\delta_{ij}\,\frac{k_{m}k_{n}}{k^{2}}, the nonlinear terms can be combined asMi​j∣kinc​(p)=−i​ηρ0​[ki​Dj​kinc​(p)+kj​Di​kinc​(p)]+ρ02​Qi​j∣m​n​(k)​∫q⟨vm​(q)​vn​(p−q)​vk​(−p)⟩c.M_{ij\mid k}^{\mathrm{inc}}(p)=-\frac{i\eta}{\rho_{0}}\left[k_{i}\,D_{jk}^{\mathrm{inc}}(p)+k_{j}\,D_{ik}^{\mathrm{inc}}(p)\right]+\rho_{0}^{2}\,Q_{ij\mid mn}(k)\int_{q}\left\langle v_{m}(q)\,v_{n}(p-q)\,v_{k}(-p)\right\rangle_{c}.(42)

At a centered Gaussian level,⟨vm​vn​vk⟩c=0\left\langle v_{m}\,v_{n}\,v_{k}\right\rangle_{c}=0, so only at that approximation,Mi​j∣kinc,G​(p)=−i​ηρ0​[ki​Pj​kT+kj​Pi​kT]​DTinc​(p).M_{ij\mid k}^{\mathrm{inc},G}(p)=-\frac{i\eta}{\rho_{0}}\left[k_{i}\,P_{jk}^{T}+k_{j}\,P_{ik}^{T}\right]D_{T}^{\mathrm{inc}}(p).(43)

Beyond the Gaussian approximation, the convective and nonlocal-pressure terms are both controlled by the full connected three-velocity correlator.C~k​i​m​(k,t)={Ci​j​l​k−Cκ,i​j​l​kresk≤k0ω2k4​DT​(ki​kk​Pj​lT+ki​kl​Pj​kT+kj​kk​Pi​lT+kj​kl​Pi​kT)+k2​DL​Hi​j​Hk​l+Ni​j∣k​l⟂k≥k0\tilde{C}_{kim}(k,t)=\left\{\begin{array}[]{cc}C_{ijlk}-C_{\kappa,ijlk}^{\mathrm{res}}&k\leq k_{0}\\
\frac{\omega^{2}}{k^{4}}D_{T}\left(k_{i}k_{k}P_{jl}^{T}+k_{i}k_{l}P_{jk}^{T}+k_{j}k_{k}P_{il}^{T}+k_{j}k_{l}P_{ik}^{T}\right)+k^{2}D_{L}H_{ij}H_{kl}+N_{ij\mid kl}^{\perp}&k\geq k_{0}\end{array}\right.(44)

whereNi​j∣k​l⟂=2​T​[η​(Pi​kT​Pj​lT+Pi​lT​Pj​kT)+A2​η​λ​Pi​jT​Pk​lT]N_{ij\mid kl}^{\perp}=2T\left[\eta\left(P_{ik}^{T}P_{jl}^{T}+P_{il}^{T}P_{jk}^{T}\right)+A_{2\eta\lambda}\,P_{ij}^{T}P_{kl}^{T}\right]andTi​j​[v]​(p)=−i​η​(ki​vj+kj​vi)+ρ0​∫q(δi​m​δj​n−δi​j​km​knk2)​vm​(q)​vn​(p−q)T_{ij}[v](p)=-i\eta\left(k_{i}v_{j}+k_{j}v_{i}\right)+\rho_{0}\int_{q}\left(\delta_{im}\delta_{jn}-\delta_{ij}\frac{k_{m}k_{n}}{k^{2}}\right)v_{m}(q)\,v_{n}(p-q).(DκresMκres​TMκresCκres)=(DκMκTMκCκ)​(ΣκJ​JΣκJ​TΣκT​JΣκT​T)​(DκMκTMκCκ)+𝒪​(Σ2).\begin{pmatrix}D_{\kappa}^{\mathrm{res}}&M_{\kappa}^{\mathrm{res}\,T}\\[5.69054pt]
M_{\kappa}^{\mathrm{res}}&C_{\kappa}^{\mathrm{res}}\end{pmatrix}=\begin{pmatrix}D_{\kappa}&M_{\kappa}^{T}\\[5.69054pt]
M_{\kappa}&C_{\kappa}\end{pmatrix}\begin{pmatrix}\Sigma_{\kappa}^{JJ}&\Sigma_{\kappa}^{JT}\\[5.69054pt]
\Sigma_{\kappa}^{TJ}&\Sigma_{\kappa}^{TT}\end{pmatrix}\begin{pmatrix}D_{\kappa}&M_{\kappa}^{T}\\[5.69054pt]
M_{\kappa}&C_{\kappa}\end{pmatrix}+\mathcal{O}(\Sigma^{2}).(45)

Compressible propagators therefore remain present in internal loops even though the external correlation functions carry only transverse hydrodynamic indices.

This makes the convolution integrals evolve slow and fast perturbations in very different ways. The microscopic compressible correlators do not appear as separate additive correlators in the infrared theory, but integrating them out generally changes the effective incompressible action and therefore changes the incompressible correlation functions indirectly. In general,{DLcomp,Mi​j∣kcomp,Ci​j∣k​lcomp}≠0\{D_{L}^{\mathrm{comp}},M_{ij\mid k}^{\mathrm{comp}},C_{ij\mid kl}^{\mathrm{comp}}\}\neq 0. The density, longitudinal current and isotropic stress are coupled through the continuity equation and the equation of state. This longitudinal compressible sector is precisely what disappears as a propagating macroscopic degree of freedom belowk0k_{0}. The residue must not be evaluated simply by putting the microscopic fields equal to zero. It is obtained by first retaining their coupling to the macroscopic sector and then taking the external low-energy limit:|p|k0→0,|ω|cs​k0→0.\frac{|p|}{k_{0}}\rightarrow 0,\qquad\frac{|\omega|}{c_{s}k_{0}}\rightarrow 0.(46)

The internal microscopic fluctuations remain at momenta and frequencies characteristic of the compressible sectorGκinc≠GNSG_{\kappa}^{\mathrm{inc}}\neq G_{\mathrm{NS}}but it is also wrong to writeGκinc=GNS+GmicroG_{\kappa}^{\mathrm{inc}}=G_{\mathrm{NS}}+G_{\mathrm{micro}}. Integrating out the microscopic sector producesGeff,κinc=[Gκinc−Σcomp→inc].G_{\mathrm{eff},\kappa}^{\mathrm{inc}}=\left[G_{\kappa}^{\mathrm{inc}}-\Sigma_{\mathrm{comp}\rightarrow\mathrm{inc}}\right].(47)

The microscopic sector modifies the equation of motion rather than the observed fluctuations directly. The observed fluctuations are computed afterwards from the modified equation of motion. This is the mathematically precise place where the compressible microscopic sector manifests itself.Σcomp→inc​(p;k0)=lim|p|/k0→0|ω|/(cs​k0)→0∫compVinc−comp​Gcomp​(q)​Gcomp​(q−p)​Vcomp−inc.\Sigma_{\mathrm{comp}\rightarrow\mathrm{inc}}(p;k_{0})=\lim_{\begin{subarray}{c}|p|/k_{0}\rightarrow 0\\[2.0pt]
|\omega|/(c_{s}k_{0})\rightarrow 0\end{subarray}}\int_{\mathrm{comp}}V_{\mathrm{inc-comp}}\,G_{\mathrm{comp}}(q)\,G_{\mathrm{comp}}(q-p)\,V_{\mathrm{comp-inc}}.(48)

The complete decoupling iflim|p|/k0→0Σκcomp​(p)=0\lim_{|p|/k_{0}\rightarrow 0}\Sigma_{\kappa}^{\mathrm{comp}}(p)=0then the compressible sector leaves no infrared residueGeff,κinc→GκincG_{\mathrm{eff,\kappa}}^{\mathrm{inc}}\rightarrow G_{\kappa}^{\mathrm{inc}}. The convolution integrals treat slow incompressible perturbations and fast compressible perturbations very differently because they occupy different positions in the FRG loop. Instead of being governed by two unrelated RG evolutions, they participate in the same flow equation with different propagator blocks, different dispersion relations, and different momentum-frequency regions.

## IV  Discussion and outlook

While this work is a highly incomplete first effort, it lays out the ingredients required for an inherently generally stochastic hydrodynamics, implementing both Galilean symmetry and fluctuations non-perturbatively. The fundamental object is the Gaussian partition function Eq. (1) evolves via the Galilean Ward identity,eqs.˜6,7and8.
Together with the linear response equation,eqs.˜32and33, an initial ensemble of initial values for currents from which⟨Ti​j⟩,⟨Ji⟩,Di​k,Mi​j​k,Ci​j​k​l\left\langle T_{ij}\right\rangle,\left\langle J_{i}\right\rangle,D_{ik},M_{ijk},C_{ijkl}can be calculated and a thermostatic partition functionln⁡𝒵​(T,μ)\ln\mathcal{Z}(T,\mu)to Gaussian order (basically the energy and molecular density, heat capacity and susceptibility), one could evolve the whole ensemble in a way that respects Galilean symmetries, via a lattice algorithm shown in Fig 2,3 of[1].

The non-relativistic limit is more complicated than[1]as necessitates a current and a chemical potential, which triples the number of correlators and doubles the number of currents, but the equations remain closed as before.

The issue is that a Gaussianln⁡𝒵​(T,μ)\ln\mathcal{Z}(T,\mu)can not be defined for an incompressible fluid, since it would be non-analytic. However this can be resolved by a functional renormalization group calculation, where macroscopic correlation functions look incompressible while hiding, in counterterms, the microscopic compressible structure. Since linear response is non-local in frequency and wavenumber, such microscopic terms will generate fluctuations at the scale of the non-locality of pressure, cascading statistical fluctuations up to the macroscopic turbulence scale. This has the potential of explaining spontaneous stochasticity, which would indeed be the molecular noise given by statistical mechanics amplified to macroscopic scales by a regime where the microscopic chaos of statistical mechanics and the macroscopic incompressible turbulence scale talk to each other.

Incompressibility ensures that the volume preserving diffeomorphism invariance works in the same way in relativistic[38]as in non-relativistic[39]regimes: It ensures local conservation of entropy, in that while dissipation and entropy creation of course do occur, they can not be measured locally (on a scale set by the incompressibility scale) because it can not be locally distinguished from a fluctuation within a microstate distribution.
This ensures the turbulence scale and the the microscopic fluctuation scale, while different by orders of magnitude, are ultimately related, making spontaneous stochasticity natural.

Diffeomorphism invariance together with the inherently probabilistic nature of Eq. (1) and Stochastic calculus gives a natural setting which includes spontaneous stochasticity[21,22]automatically. Anomalous dissipation[7](in this picture, irregular turbulent structures become features of a microstate distribution) and Wild/nightmare solutions[8](in this picture, ”tails” of statistical microstate distributions which become features of the turbulent flow) are then not mathematical abstractions but potentially observable phenomena to be incorporated into our understanding of statistical physics.

In this regard, we note that the concept of “weak solutions”[7,25]around which anomalous transport and Wild solutions[8]are defined, is somewhat analogous to the renormalization group (with the test function paralleling renormalization group coarse-graining, and notions of universality of coarse-graining vs universality w.r.t. test functions used the same way).
Thus, the renormalization group treatment of the compressibility issue has important consequences on the evolution of the average quantities⟨Ti​j​(x)⟩,⟨Ji​(x)⟩\left\langle T_{ij}(x)\right\rangle,\left\langle J_{i}(x)\right\rangle, which will survive any coarse-graining.
While distances of the order of the compressibility scale are unobservable (even in principle, as probing them generally destroys the fluid), their effect survives, via the residual, in macroscopic dynamics. This should give visible effects, for it is expected spontaneous stochasticity is set around the compressibility scale, and the residual might be crucial in determining the interaction of this scale with the turbulence scale, as seen in[22].

The breaking of incompressibility at the UV cutoff means that the counterterm should be treated as an anomaly (breaking the volume-preserving diffeomorphisms of[39]), which might alter the fluctuation distribution worked out via topology from macroscopic statistical mechanics alone[49], something familiar within quantum field theory[23]. The incorporation of anomalies in the topological derivation of[49]is therefore a promising further investigation.

It remains to be seen whether such an approach, and in general a non-perturbative treatment of fluctuations,is really needed to understand experimental data. Calculating anomalous diffusion from first principles would be a possible but long-winded project, necessitating inputs from both hydrodynamics and microscopic statistical mechanics. Hence, a more qualitative experimental signature for such dynamics would be useful.

The experimental-driven question which prompted[1]is the question of the existence of what appears to be a fluid with very few degrees of freedom[18]. In parallel, it was found that systems with very few strongly interacting ultracold atoms appear to be surprisingly fluid-like[19]666Note that it is a fluid rather than a super-fluid, since no evidence was found for energy gaps of fluidic excitations, and even every-day systems with a surprisingly small number of particles behave as a fluid[20]. It is clear that concepts such as spontaneous stochasticity are related to the experimentally investigable question of ”what is the smallest fluid”.

If turbulence and spontaneous stochasticity are found in such small systems, their scales will be much closer to each other than in ordinary turbulent fluids. Perturbative fluctuating hydrodynamics will fail by a simple order of magnitude estimate, but our approach might not. From there, one might check if the corrections from inserting an inherent stochasticity into the fluids evolution rather than treating it as a perturbation on a deterministic equation is worthwhile, also for more fundamental and mathematical questions such as Onsager’s conjecture and the existence of a low viscosity limit from anomalous dissipation.

This brings us back to the ”philosophical” issues discussed in the introduction. Some of the deepest questions usually associated with fluid dynamics are thought to lie within the realm of mathematics, but fluids are very much physical objects, depending on such ingredients as statistical mechanics for their definition.
A proper treatment of how statistical mechanics and fluid dynamics meet when viscosity is so low that backreaction to thermal fluctuations is non-negligible might be necessary to better understand phenomena such as turbulence and anomalous dissipation, also from a mathematical point of view.

AcknowledgementsGT thanks Bolsa de produtividade CNPQ 305731/2023-8 and FAPESP 2023/06278-2 as well as participation in the tematico 2023/13749-1 for support.

## Appendix

## Appendix AFunctional construction of the incompressible effective theory

This appendix develops the functional construction used to connect the compressible microscopic description with the effective incompressible theory. The density and longitudinal-velocity
fluctuations are integrated out and their effect consequently remains encoded in the correlation functions of incompressible sectorZκcomp​[J,T]=∫𝒟​δ​ρ​𝒟​vL​𝒟​vT​exp⁡[−Sκcomp​[δ​ρ,vL,vT]+Jρ​δ​ρ+JL​vL+JT​vT].Z_{\kappa}^{\mathrm{comp}}[J,T]=\int\mathcal{D}\delta\rho\,\mathcal{D}v^{L}\,\mathcal{D}v^{T}\,\exp\!\left[-S_{\kappa}^{\mathrm{comp}}[\delta\rho,v^{L},v^{T}]+J_{\rho}\delta\rho+J_{L}v^{L}+J_{T}v^{T}\right].(49)

The transverse field is kept as an explicit infrared variable. It only means that the infrared observer does not probe them directly.
Their contribution is absorbed into an effective generating functional
for the transverse velocity by integrating over the compressible sector,Zκinc​[JT]=∫𝒟​δ​ρ​𝒟​vL​Zκcomp​[Jρ=0,JL=0,JT].Z_{\kappa}^{\mathrm{inc}}[J_{T}]=\int\mathcal{D}\delta\rho\,\mathcal{D}v^{L}\,Z_{\kappa}^{\mathrm{comp}}[J_{\rho}=0,J_{L}=0,J_{T}].(50)

Equation (50) defines the incompressible theory as an effective theory. The boundary conditions in the notation of Eq. (2) and using the renormalization group prescription of Eq. (4) are∂ln⁡𝒵∂k0=Θ​(k0−|𝐤|)​Θ​(k0c−|ω|)​∂M∂k0+Θ​(|𝐤|−k0)​Θ​(k0c−|ω|)​∂N∂k0+Θ​(|ω|−k0c)​∂W∂k0\displaystyle\frac{\partial\ln\mathcal{Z}}{\partial k_{0}}={}\Theta(k_{0}-|\mathbf{k}|)\Theta\!\left(\frac{k_{0}}{c}-|\omega|\right)\frac{\partial M}{\partial k_{0}}+\Theta(|\mathbf{k}|-k_{0})\Theta\!\left(\frac{k_{0}}{c}-|\omega|\right)\frac{\partial N}{\partial k_{0}}+\Theta\!\left(|\omega|-\frac{k_{0}}{c}\right)\frac{\partial W}{\partial k_{0}}+δ​(k0−|𝐤|)​Θ​(k0c−|ω|)​(M−N)+1c​δ​(k0c−|ω|)​[Θ​(k0−|𝐤|)​M+Θ​(|𝐤|−k0)​N−W].\displaystyle+\delta(k_{0}-|\mathbf{k}|)\Theta\!\left(\frac{k_{0}}{c}-|\omega|\right)(M-N)+\frac{1}{c}\delta\!\left(\frac{k_{0}}{c}-|\omega|\right)\left[\Theta(k_{0}-|\mathbf{k}|)M+\Theta(|\mathbf{k}|-k_{0})N-W\right].(51)

The region where the descriptions meeting are at|𝐤|=k0,|\mathbf{k}|=k_{0},one requiresM​(ω,k0)=N​(ω,k0).M(\omega,k_{0})=N(\omega,k_{0}).At|ω|=k0c,|\omega|=\frac{k_{0}}{c},one requiresN​(k,k0c)=W​(k,k0c)N\!\left(k,\frac{k_{0}}{c}\right)=W\!\left(k,\frac{k_{0}}{c}\right). However, the derivatives need not match:∂M∂|𝐤||k0−≠∂N∂|𝐤||k0+\left.\frac{\partial M}{\partial|\mathbf{k}|}\right|_{k_{0}^{-}}\neq\left.\frac{\partial N}{\partial|\mathbf{k}|}\right|_{k_{0}^{+}}since their discontinuity reflects a nonanalytic change in its scale derivative.

The boundary conditions of (17)Γκ=Θ​(k0−|𝐩|)​Θ​(k0c−|ω|)​Γκ,inc+Θ​(|𝐩|−k0)​Θ​(k0c−|ω|)​Γκ,comp+Θ​(|ω|−k0c)​Γκ,E.\Gamma_{\kappa}=\Theta(k_{0}-|\mathbf{p}|)\Theta\!\left(\frac{k_{0}}{c}-|\omega|\right)\Gamma_{\kappa,\mathrm{inc}}+\Theta(|\mathbf{p}|-k_{0})\Theta\!\left(\frac{k_{0}}{c}-|\omega|\right)\Gamma_{\kappa,\mathrm{comp}}+\Theta\!\left(|\omega|-\frac{k_{0}}{c}\right)\Gamma_{\kappa,E}.(52)

It must not be interpreted as a sum of three independent theories. The same scale-dependent functional is evaluated with different active degrees of freedom in the corresponding momentum-frequency domains. The effective actions are matched continuously at the crossover scale,Γκinc|k0−=Γκcomp|k0+\Gamma_{\kappa}^{\mathrm{inc}}\Big|_{k_{0}^{-}}=\Gamma_{\kappa}^{\mathrm{comp}}\Big|_{k_{0}^{+}}. The discontinuity∂κΓκinc|k0−≠∂κΓκcomp|k0+\partial_{\kappa}\Gamma_{\kappa}^{\mathrm{inc}}\Big|_{k_{0}^{-}}\neq\partial_{\kappa}\Gamma_{\kappa}^{\mathrm{comp}}\Big|_{k_{0}^{+}}is because the sets of active degrees of freedom are different.

## A.1  Compressible

The continuity part constructed with scale-dependent coefficientsΓκcontinuity+Γκmomentum=∫{ρ¯[Zρ,κ∂tρ+λρ,κ∂i(ρui)]+u¯i[Zu,κρ(∂tui+λu,κuj∂jui)\displaystyle\Gamma_{\kappa}^{\mathrm{continuity}}+\Gamma_{\kappa}^{\mathrm{momentum}}=\int\bigg\{\bar{\rho}[Z_{\rho,\kappa}\,\partial_{t}\rho+\lambda_{\rho,\kappa}\,\partial_{i}(\rho u_{i})]+\bar{u}_{i}[Z_{u,\kappa}\,\rho(\partial_{t}u_{i}+\lambda_{u,\kappa}\,u_{j}\partial_{j}u_{i})+∂ipκ(ρ)−ηκ∇2ui−(ζκ+3ηκ)∂i∂juj]}.\displaystyle+\partial_{i}p_{\kappa}(\rho)-\eta_{\kappa}\nabla^{2}u_{i}-(\zeta_{\kappa}+3\eta_{\kappa})\partial_{i}\partial_{j}u_{j}]\bigg\}.(53)

The coefficients are kept scale dependentκ\kappabecause the effective equations change as fluctuations are integrated out. TheΓκcontinuity\Gamma_{\kappa}^{\mathrm{continuity}}andΓκmomentum\Gamma_{\kappa}^{\mathrm{momentum}}enforce local mass conservation and momentum balance, respectively. We expand around a homogeneous configurationρ=ρ0,κ+δ​ρ\rho=\rho_{0,\kappa}+\delta\rhoandui=0u_{i}=0. The quadratic continuity contribution isΓκ,continuity(2)+Γκ,momentum(2)=∫qρ¯​(−q)​[−i​Zρ,κ​ω​δ​ρ​(q)+i​λρ,κ​ρ0,κ​pi​ui​(q)]\displaystyle\Gamma_{\kappa,\mathrm{continuity}}^{(2)}+\Gamma_{\kappa,\mathrm{momentum}}^{(2)}=\int_{q}\bar{\rho}(-q)\left[-iZ_{\rho,\kappa}\,\omega\,\delta\rho(q)+i\lambda_{\rho,\kappa}\,\rho_{0,\kappa}\,p_{i}u_{i}(q)\right]u¯​(−q)​[−i​Zu,κ​ρ0,κ​ω​ui​(q)+i​cs,κ2​pi​δ​ρ​(q)+ηκ​p2​ui​(q)+[ζκ+d−2d​ηκ]​pi​pj​uj​(q)],\displaystyle\bar{u}(-q)[-iZ_{u,\kappa}\,\rho_{0,\kappa}\,\omega\,u_{i}(q)+ic_{s,\kappa}^{\,2}\,p_{i}\,\delta\rho(q)+\eta_{\kappa}p^{2}u_{i}(q)+\left[\zeta_{\kappa}+\frac{d-2}{d}\eta_{\kappa}\right]p_{i}p_{j}u_{j}(q)],(54)

where the coefficientsZρ,κZ_{\rho,\kappa},Zc,κZ_{c,\kappa}, andZg,κZ_{g,\kappa}are initially retained so that the renormalization of the density, velocity, and response fields can be tracked independently throughout the renormalization-group flow. The stochastic force, represented byΓκ(2)=−∫qΦa>​(−q)​Pκ,a​b​(q)​Φb>​(q),Pκ​(q)=(−i​Zρ,κ​ωi​cs,κ2​pii​Zc,κ​pjAκ,i​j​(q))\Gamma_{\kappa}^{(2)}=-\int_{q}\Phi^{>}_{a}(-q)\,P_{\kappa,ab}(q)\,\Phi^{>}_{b}(q),\qquad P_{\kappa}(q)=\begin{pmatrix}-iZ_{\rho,\kappa}\,\omega&ic_{s,\kappa}^{\,2}\,p_{i}\\[6.0pt]
iZ_{c,\kappa}\,p_{j}&A_{\kappa,ij}(q)\end{pmatrix}(55)

specifies the covariance driven
of the microscopic fluctuations that drive, but not
replace the deterministic compressible dynamics. The matrixPκP_{\kappa}is the quadratic response operator for the coupled compressible variables. TheAκ,i​j​(q)=(−i​Zg,κ​ω+ρ0​ηκ​p2)​δi​j+ρ0​(ζκ+32​ηκ)​pi​pjA_{\kappa,ij}(q)=\left(-iZ_{g,\kappa}\omega+\rho_{0}\eta_{\kappa}\,p^{2}\right)\delta_{ij}+\rho_{0}\left(\zeta_{\kappa}+\frac{3}{2}\eta_{\kappa}\right)p_{i}p_{j}.
The regulator must preserve the response-field structureRκ,i​jg​(𝐩)=κ2−p2ρ0​Θ​(κ2−p2)​[ηκ​δi​j+(ζκ+13​ηκ)​pi​pjp2]R_{\kappa,ij}^{g}(\mathbf{p})=\frac{\kappa^{2}-p^{2}}{\rho_{0}}\,\Theta(\kappa^{2}-p^{2})\left[\eta_{\kappa}\delta_{ij}+\left(\zeta_{\kappa}+\frac{1}{3}\eta_{\kappa}\right)\frac{p_{i}p_{j}}{p^{2}}\right](56)

and is responsible to define which fluctuations are allowed to participate in the effective theory at a given RG scale. In other words, this regulator suppresses the low-momentum response modes without changing their transverse and longitudinal tensor decomposition. The density fluctuations are coupled to the regulated momentum fluctuations through the continuity equation. The green function from (14) isGκ​(q)=(2​Pκ−1​(q)​Nκ​(q)​Pκ−T​(q)Pκ−T​(q)Pκ−1​(q)0).G_{\kappa}(q)=\begin{pmatrix}2\,P_{\kappa}^{-1}(q)\,N_{\kappa}(q)\,P_{\kappa}^{-T}(q)&P_{\kappa}^{-T}(q)\\[8.0pt]
P_{\kappa}^{-1}(q)&0\end{pmatrix}.(57)

The exact flow equation is∂tΓκ=12​Tr⁡[Gκ​∂tRκ],t=ln⁡(κΛ).\partial_{t}\Gamma_{\kappa}=\frac{1}{2}\,\operatorname{Tr}\left[G_{\kappa}\,\partial_{t}R_{\kappa}\right],\qquad t=\ln\!\left(\frac{\kappa}{\Lambda}\right).(58)

The trace contains the full regularized propagator. Functional derivatives of this equation generate the flow equations for the scale-dependent
vertices. Taking two functional derivatives of the Wetterich equation yields∂tΓκ,A​B(2)​(p)=Tr⁡[Gκ​Γκ,A(3)​Gκ​Γκ,B(3)​Gκ​∂tRκ]−12​Tr⁡[Gκ​Γκ,A​B(4)​Gκ​∂tRκ].\partial_{t}\Gamma_{\kappa,AB}^{(2)}(p)=\operatorname{Tr}\!\left[G_{\kappa}\,\Gamma_{\kappa,A}^{(3)}G_{\kappa}\,\Gamma_{\kappa,B}^{(3)}G_{\kappa}\,\partial_{t}R_{\kappa}\right]-\frac{1}{2}\operatorname{Tr}\!\left[G_{\kappa}\,\Gamma_{\kappa,AB}^{(4)}G_{\kappa}\,\partial_{t}R_{\kappa}\right].(59)

he first contribution contains two three-point vertices, while the second
contains one four-point vertex.

## A.2  Incompressible

The incompressible theory is defined on the transverse velocity sector.Γκ,2=∫qu¯i​(−q)​Pi​jT​(𝐪)​[−i​Zκ​ω+νκ​p2]​uj​(q)−Dκ​(𝐪)​u¯i​(−q)​Pi​jT​(𝐪)​u¯j​(q),\Gamma_{\kappa,2}=\int_{q}\bar{u}_{i}(-q)P_{ij}^{T}(\mathbf{q})\left[-iZ_{\kappa}\omega+\nu_{\kappa}p^{2}\right]u_{j}(q)-D_{\kappa}(\mathbf{q})\bar{u}_{i}(-q)P_{ij}^{T}(\mathbf{q})\bar{u}_{j}(q),(60)

The coefficientZκZ_{\kappa}controls the temporal response, whileνκ\nu_{\kappa}is the running kinematic viscosity. The kernelDκ​(𝐩)D_{\kappa}(\mathbf{p})determines the covariance of the transverse stochastic force. The nonlinear Navier–Stokes interaction isΓκ,3=12​∫q1∫q2∫q3(2​π)d+1​δ​(q1+q2+q3)​u¯i​(q1)​Vκ,i​j​l​(𝐪1)​uj​(q2)​ul​(q3),\Gamma_{\kappa,3}=\frac{1}{2}\int_{q_{1}}\int_{q_{2}}\int_{q_{3}}(2\pi)^{d+1}\delta(q_{1}+q_{2}+q_{3})\,\bar{u}_{i}(q_{1})V_{\kappa,ijl}(\mathbf{q}_{1})u_{j}(q_{2})u_{l}(q_{3}),(61)

whereVκ,i​j​l​(𝐩)=i​λκ2​[pj​Pi​lT​(𝐩)+pl​Pi​jT​(𝐩)]V_{\kappa,ijl}(\mathbf{p})=\frac{i\lambda_{\kappa}}{2}\left[p_{j}P_{il}^{T}(\mathbf{p})+p_{l}P_{ij}^{T}(\mathbf{p})\right]determines the nonlinear mode coupling and it is the incompressible Navier–Stokes cubic vertex, which removes the longitudinal component generated by the quadratic velocity product. The transverse projector contained in the vertex is the explicit remnant of the eliminated pressure. At zero background field, the HessianΓκ(2)​(q)=Pi​jT​(𝐩)​(0−i​Zκ​ω+νκ​p2i​Zκ​ω+νκ​p2−2​Dκ​(𝐩)).\Gamma_{\kappa}^{(2)}(q)=P_{ij}^{T}(\mathbf{p})\begin{pmatrix}0&-iZ_{\kappa}\omega+\nu_{\kappa}p^{2}\\[4.0pt]
iZ_{\kappa}\omega+\nu_{\kappa}p^{2}&-2D_{\kappa}(\mathbf{p})\end{pmatrix}.(62)

The regulator of (13) acts only in the response sector and generates a transverse external propagator in the incompressible sector∂tRκ=νκ​[(2−ην)​κ2+ην​p2]​Θ​(κ2−p2)\partial_{t}R_{\kappa}=\nu_{\kappa}\left[(2-\eta_{\nu})\kappa^{2}+\eta_{\nu}p^{2}\right]\Theta(\kappa^{2}-p^{2})(63)

Define the viscosity anomalous dimension byην=−∂tln⁡νκ,t=ln⁡κ\eta_{\nu}=-\partial_{t}\ln\nu_{\kappa},\ t=\ln\kappa. The green function from (14) isGκ,i​j​(q)=Pi​jT​(𝐩)​(2​Dκ​(𝐩)Zκ2​ω2+Aκ2​(𝐩)1−i​Zκ​ω+Aκ​(𝐩)1i​Zκ​ω+Aκ​(𝐩)0).G_{\kappa,ij}(q)=P_{ij}^{T}(\mathbf{p})\begin{pmatrix}\dfrac{2D_{\kappa}(\mathbf{p})}{Z_{\kappa}^{2}\omega^{2}+A_{\kappa}^{2}(\mathbf{p})}&\dfrac{1}{-iZ_{\kappa}\omega+A_{\kappa}(\mathbf{p})}\\[12.0pt]
\dfrac{1}{iZ_{\kappa}\omega+A_{\kappa}(\mathbf{p})}&0\end{pmatrix}.(64)

The current covariance isDi​jmacro​(q)=ρ02​Gκ,i​ju​u​(q)D^{\mathrm{macro}}_{ij}(q)=\rho_{0}^{2}G^{uu}_{\kappa,ij}(q). We start from (29)∂tΓκ​[Φ]=12​Tr⁡[Gκ​[Φ]​∂tRκ]=∫qAκ​(p)​∂tRκ​(p)Zκ2​ω2+Aκ2​(p)=νκ​κ53​π​Zκ,\partial_{t}\Gamma_{\kappa}[\Phi]=\frac{1}{2}\operatorname{Tr}\left[G_{\kappa}[\Phi]\,\partial_{t}R_{\kappa}\right]=\int_{q}\frac{A_{\kappa}(p)\,\partial_{t}R_{\kappa}(p)}{Z_{\kappa}^{2}\omega^{2}+A_{\kappa}^{2}(p)}=\frac{\nu_{\kappa}\kappa^{5}}{3\pi Z_{\kappa}}\,,(65)

The (65) is the flow of the effective average action evaluated at vanishing field, i.e., the vacuum contribution to the Wetterich equation. It is the simplest projection of the FRG flow. this expression alone cannot produce the running of the couplings. The first nontrivial physical flow is the flow of the two-point vertex,∂tΓκ(2)\displaystyle\partial_{t}\Gamma_{\kappa}^{(2)}=−12​Tr⁡[Gκ​(Γκ(4)−2​Γκ(3)​Gκ​Γκ(3))​Gκ​∂tRκ].\displaystyle=-\frac{1}{2}\operatorname{Tr}\left[G_{\kappa}\left(\Gamma_{\kappa}^{(4)}-2\Gamma_{\kappa}^{(3)}G_{\kappa}\Gamma_{\kappa}^{(3)}\right)G_{\kappa}\,\partial_{t}R_{\kappa}\right].(66)=two-cubic-vertex diagram−12​quartic-vertex diagram.\displaystyle=\text{two-cubic-vertex diagram}-\frac{1}{2}\,\text{quartic-vertex diagram}.(67)

The effective actions are matched continuously at the crossover scale,Γκinc|k0−=Γκcomp|k0+\Gamma_{\kappa}^{\mathrm{inc}}\Big|_{k_{0}^{-}}=\Gamma_{\kappa}^{\mathrm{comp}}\Big|_{k_{0}^{+}}the continuity condition guarantees that the same observable physics is described on the matching surface.∂κΓκinc|k0−≠∂κΓκcomp|k0+\partial_{\kappa}\Gamma_{\kappa}^{\mathrm{inc}}\Big|_{k_{0}^{-}}\neq\partial_{\kappa}\Gamma_{\kappa}^{\mathrm{comp}}\Big|_{k_{0}^{+}}. This discontinuity of the scale derivative records the abrupt change in the set of active degrees of freedom. It is not enough to determine the residue without the macro-micro coupling.∂tΓκ(2)=Tr⁡[Gκ​Γκ(3)​Gκ​Γκ(3)​Gκ​∂tRκ].\partial_{t}\Gamma_{\kappa}^{(2)}=\operatorname{Tr}\left[G_{\kappa}\Gamma_{\kappa}^{(3)}G_{\kappa}\Gamma_{\kappa}^{(3)}G_{\kappa}\,\partial_{t}R_{\kappa}\right].(68)

This is the two-cubic-vertex contribution to the incompressible two-point flow and It should not be identified directly with the compressible residue.

## Appendix BCompressible residue kernels

Then,Σκ,i​kJ​J(p)=∫q∈𝒞​(k0)[\displaystyle\Sigma_{\kappa,ik}^{JJ}(p)=\int_{q\in\mathcal{C}(k_{0})}\Big[∂tGκ,ρ​ρ>​(q)​Gκ,i​k>​(r)+Gκ,ρ​k>​(q)​∂tGκ,i​ρ>​(r)+Gκ,i​ρ>​(q)​∂tGκ,ρ​k>​(r)+\displaystyle\partial_{t}G_{\kappa,\rho\rho}^{>}(q)\,G_{\kappa,ik}^{>}(r)+G_{\kappa,\rho k}^{>}(q)\,\partial_{t}G_{\kappa,i\rho}^{>}(r)+G_{\kappa,i\rho}^{>}(q)\,\partial_{t}G_{\kappa,\rho k}^{>}(r)\ +Gκ,i​k>(q)∂tGκ,ρ​ρ>(r)],r=p−q.\displaystyle G_{\kappa,ik}^{>}(q)\,\partial_{t}G_{\kappa,\rho\rho}^{>}(r)\Big],\qquad r=p-q.(69)

Then,Σκ,i∣k​lJ​T​(p;k0)=∂t∫q∈𝒞​(k0)Vκ,Ji;a​b​(p;q,p−q)​Gκ,a​c>​(q)​Gκ,b​d>​(p−q)​Vκ,Tk​l;c​d​(−p;q−p,−q).\Sigma_{\kappa,i\mid kl}^{JT}(p;k_{0})=\partial_{t}\int_{q\in\mathcal{C}(k_{0})}V_{\kappa,J_{i};ab}\bigl(p;q,p-q\bigr)\,G_{\kappa,ac}^{>}(q)\,G_{\kappa,bd}^{>}(p-q)\,V_{\kappa,T_{kl};cd}\bigl(-p;q-p,-q\bigr).(70)

This is not generally an independent kernel. For a real Gaussian theory with the usual exchange properties,Σκ,i​j∣kT​J​(p)=Σκ,k∣i​jJ​T​(−p)\Sigma_{\kappa,ij\mid k}^{TJ}(p)=\Sigma_{\kappa,k\mid ij}^{JT}(-p). In matrix notationΣκT​J​(p)=[ΣκJ​T​(−p)]T\Sigma_{\kappa}^{TJ}(p)=\left[\Sigma_{\kappa}^{JT}(-p)\right]^{T}. Then,Σκ,i​j∣kT​J​(p;k0)=∂t∫q∈𝒞​(k0)Vκ,Ti​j;a​b​(p;q,p−q)​Gκ,a​c>​(q)​Gκ,b​d>​(p−q)​Vκ,Jk;c​d​(−p;q−p,−q).\Sigma_{\kappa,ij\mid k}^{TJ}(p;k_{0})=\partial_{t}\int_{q\in\mathcal{C}(k_{0})}V_{\kappa,T_{ij};ab}\bigl(p;q,p-q\bigr)\,G_{\kappa,ac}^{>}(q)\,G_{\kappa,bd}^{>}(p-q)\,V_{\kappa,J_{k};cd}\bigl(-p;q-p,-q\bigr).(71)Σκ,i​j∣k​lT​T​(p;k0)\displaystyle\Sigma_{\kappa,ij\mid kl}^{TT}(p;k_{0})=lim|p|/k0→0|ω|/(cs​k0)→0∫q∈𝒞​(k0)∂⋅Vκ,Ti​j;A​Binc​-​comp(p;q,p−q)Gκ,A​C>(q)Gκ,B​D<(p−q)×\displaystyle=\lim_{\begin{subarray}{c}|p|/k_{0}\rightarrow 0\\[2.0pt]
|\omega|/(c_{s}k_{0})\rightarrow 0\end{subarray}}\,\int_{q\in\mathcal{C}(k_{0})}\partial\cdot V_{\kappa,T_{ij};AB}^{\mathrm{inc\text{-}comp}}\bigl(p;q,p-q\bigr)\,G_{\kappa,AC}^{\mathrm{>}}(q)\,G_{\kappa,BD}^{\mathrm{<}}(p-q)\timesVκ,Tk​l;C​Dcomp​-​inc​(−p;q−p,−q)+Gκ,A​C<​(q)​∂⋅Vκ,Ti​j;A​Binc​-​comp​(p;q,p−q)​Gκ,B​D<​(p−q)\displaystyle V_{\kappa,T_{kl};CD}^{\mathrm{comp\text{-}inc}}\bigl(-p;q-p,-q\bigr)+G_{\kappa,AC}^{\mathrm{<}}(q)\,\partial\cdot V_{\kappa,T_{ij};AB}^{\mathrm{inc\text{-}comp}}\bigl(p;q,p-q\bigr)\ G_{\kappa,BD}^{\mathrm{<}}(p-q)(72)

## References
- [1]G. M. Sampaio, G. Rabelo-Soares and G. Torrieri,
Phys. Rev. D112(2025) no.5, 056002
doi:10.1103/67x1-knzr
[arXiv:2504.17152 [hep-th]].
- [2]M.J. Lighthill , "Physics of gas flow at very high speeds", Nature,178(4529): 343, Bibcode:1956Natur.178..343., doi:10.1038/178343a0 (1956)
- [3]L. V. Delacretaz,
[arXiv:2606.02391 [hep-th]].
- [4]Tsutomu Kambe, elementary fluid mechanics, World Scientific (2007)
- [5]P. Constantin "Some Open Problems and Research Directions in the Mathematical Study of Fluid Dynamics". Mathematics Unlimited — 2001 and Beyond. Berlin: Springer. pp. 353–360. doi:10.1007/978-3-642-56478-9_\_15. ISBN 3-642-63114-2.
- [6]Yu Deng, Zaher Hani, Xiao Ma,
”Hilbert’s sixth problem: derivation of fluid equations via Boltzmann’s kinetic theory”
[arXiv:2503.01800 [cond-mat.quant-gas]].
- [7]T. Drivas,
”Anomalous Dissipation,
Spontaneous Stochasticity
and Onsager’s Conjecture”, PhD thesis, Stony Brook University
https://www.math.stonybrook.edu/˜tdrivas/notes/DrivasPhDThesis.pdf
- [8]C. De Lellis and L. Szekelyhidi, ”The Euler equation as a differential inclusion”, Ann. of Math.
(2)170, no. 3, 1417–1436, 2009.
- [9]M. M. Disconzi,
Living Rev. Rel.27(2024) no.1, 6
doi:10.1007/s41114-024-00052-x
[arXiv:2308.09844 [math.AP]].
- [10]G. S. Rocha, D. Wagner, G. S. Denicol, J. Noronha and D. H. Rischke,
Entropy26(2024) no.3, 189
doi:10.3390/e26030189
[arXiv:2311.15063 [nucl-th]].
- [11]K.Huang, ”Statistical Mechanics”, Wiley (1987)
- [12]E. T. Jaynes,
Phys. Rev.108(1957), 171-190
doi:10.1103/PhysRev.108.171
- [13]D. Tong, Linear Response, lectures on kinetic theory
- [14]L. P. Kadanoff and P. C. Martin,
Annals Phys.24(1963), 419-469
doi:10.1016/0003-4916(63)90078-2
- [15]D. Forster, ”hydrodynamic fluctuations, broken symmetry and correlation functions”, Addison-Wesley (1990)
- [16]P. Kovtun,
J. Phys. A45(2012), 473001
doi:10.1088/1751-8113/45/47/473001
[arXiv:1205.5040 [hep-th]].
- [17]A. Jain and P. Kovtun,
Phys. Rev. Lett.128(2022) no.7, 7
doi:10.1103/PhysRevLett.128.071601
[arXiv:2009.01356 [hep-th]].
- [18]J. L. Nagle and W. A. Zajc,
Ann. Rev. Nucl. Part. Sci.68(2018), 211-235
doi:10.1146/annurev-nucl-101916-123209
[arXiv:1801.03477 [nucl-ex]].
- [19]S. Brandstetter, P. Lunt, C. Heintze, G. Giacalone, L. H. Heyen, M. Gałka, K. Subramanian, M. Holten, P. M. Preiss and S. Floerchinger,et al.Nature Phys.21(2025) no.1, 52-56
doi:10.1038/s41567-024-02705-8
[arXiv:2308.09699 [cond-mat.quant-gas]].
- [20]C. Güttler, I. von Borstel, R. Schräpler and J. Blum,
Phys. Rev. E87(2013), 044201
doi:10.1103/PhysRevE.87.044201
[arXiv:1304.0569 [cond-mat.soft]].
- [21]D. Bernard, K. Gawedzki and A. Kupiainen,
J. Statist. Phys.90(1998), 519
doi:10.1023/A:1023212600779
[arXiv:cond-mat/9706035 [cond-mat]].
- [22]Dmytro Bandak, Alexei Mailybaev, Gregory L. Eyink, Nigel Goldenfeld
[arXiv:2401.13881 [hep-th]]
- [23]J. Zinn-Justin,
Int. Ser. Monogr. Phys.113(2002), 1-1054
- [24]E. Calzetta,
[arXiv:2605.25329 [physics.flu-dyn]].
- [25]G. L. Eyink and K. R. Sreenivasan,
Rev. Mod. Phys.78(2006), 87-135
doi:10.1103/RevModPhys.78.87
- [26]M. Hnatič, J. Honkonen and T. Lučivjanský,
Symmetry11(2019) no.10, 1193
doi:10.3390/sym11101193
- [27]W. D. McComb, Phys Rev E71037301 (2005)
- [28]C. Wetterich,
Phys. Lett. B301, 90-94 (1993)
doi:10.1016/0370-2693(93)90726-X
[arXiv:1710.05815 [hep-th]].
- [29]J. Polchinski,
Nucl. Phys. B231, 269-295 (1984)
doi:10.1016/0550-3213(84)90287-6
- [30]G. Torrieri,
[arXiv:2601.01656 [hep-th]].
- [31]G. Torrieri,
JHEP02(2021), 175
doi:10.1007/JHEP02(2021)175
[arXiv:2007.09224 [hep-th]].
- [32]G. Torrieri,
Phys. Rev. D109(2024) no.5, L051903
doi:10.1103/PhysRevD.109.L051903
[arXiv:2307.07021 [hep-th]].
- [33]T. Dore, L. Gavassino, D. Montenegro, M. Shokri and G. Torrieri,
Annals Phys.442(2022), 168902
doi:10.1016/j.aop.2022.168902
[arXiv:2109.06389 [hep-th]].
- [34]TA De Pirey, LF Cugliandolo, V Lecomte, F Van Wijland,
Advances in Physics, Volume 71, Issue 1-2, pp. 1-85, 85 pp.
2211.09470
- [35]Alexei Mailybaev
[arXiv:2010.13089 [hep-th]]
- [36]K. Jensen and A. Karch,
JHEP04, 155 (2015)
doi:10.1007/JHEP04(2015)155
[arXiv:1412.2738 [hep-th]].
- [37]J. Liao and V. Koch,
Phys. Rev. C81, 014902 (2010)
doi:10.1103/PhysRevC.81.014902
[arXiv:0909.3105 [hep-ph]].
- [38]S. Dubovsky, L. Hui, A. Nicolis and D. T. Son,
Phys. Rev. D85(2012), 085029
doi:10.1103/PhysRevD.85.085029
[arXiv:1107.0731 [hep-th]].
- [39]Mohammad Farazmand, Mattia Serra
[arXiv:1807.02726 [hep-th]]
and references therein
- [40]George, William K. "Lectures in Turbulence for the 21st Century." Department of Thermo and Fluid Engineering, Chalmers University of Technology, Göteborg, Sweden (2005).p 64http://www.turbulence-online.com/Publications/Lecture_Notes/Turbulence_Lille/TB_16January2013.pdf
- [41]J.Y Chemin and I.Ghallager, [arxiv:0508374]
- [42]J.Y Chemin and I.Ghallager, [arxiv:0710.5408]
- [43]R. K. Pathria,
Butterworth-Heinemann, 1996,
ISBN 978-0-08-054171-6
- [44]A. Sorensen, D. Oliinychenko, V. Koch and L. McLerran,
Phys. Rev. Lett.127(2021) no.4, 042303
doi:10.1103/PhysRevLett.127.042303
[arXiv:2103.07365 [nucl-th]].
- [45]W. b. He, G. y. Shao and C. l. Xie,
Phys. Rev. C107(2023) no.1, 014903
doi:10.1103/PhysRevC.107.014903
[arXiv:2212.08263 [nucl-th]].
- [46]Francoice Golse, ”the Boltzmann equation and its hydrodynamic limits”,
10.1016/S1874-5717(06)80006-X
- [47]C. Cercignani and G. M. Kremer, “The relativistic Boltzmann equation, Progress in mathematical physics“ No. 22 (Birkhauser,
Basel, 2002).
- [48]G. L. Eyink and T. D. Drivas,
Phys. Rev. X8(2018) no.1, 011023
doi:10.1103/PhysRevX.8.011023
[arXiv:1704.03541 [physics.flu-dyn]].
- [49]S. L. Braunstein,
[arXiv:2605.21357v1 [cond-mat2]].
- [50]G. Jona-Lasinio,
Phys. Rept.352, 439-458 (2001)
doi:10.1016/S0370-1573(01)00042-4
[arXiv:cond-mat/0009219 [cond-mat]].
- [51]K. Jensen,
SciPost Phys.5(2018) no.1, 011
doi:10.21468/SciPostPhys.5.1.011
[arXiv:1408.6855 [hep-th]].
- [52]M. Geracie,
[arXiv:1611.01198 [hep-th]].
- [53]T. Brauner, S. Endlich, A. Monin and R. Penco,
Phys. Rev. D90(2014) no.10, 105016
doi:10.1103/PhysRevD.90.105016
[arXiv:1407.7730 [hep-th]].

## 


- 


Major funding support from
