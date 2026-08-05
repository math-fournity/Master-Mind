# Quantum resetting with memory

**arXiv ID**: 2608.02297v1
**Authors**: Gabriele de Mauro, Manas Kulkarni, Satya N. Majumdar
**Published**: 2026-08-03
**Categories**: cond-mat.stat-mech, quant-ph
**HTML URL**: https://arxiv.org/html/2608.02297v1

## Abstract

We introduce a quantum stochastic resetting protocol with uniform memory, in which each resetting event returns the system to a state visited at a time chosen uniformly from its entire history. The resulting dynamics is nonunitary, non-Markovian and a direct quantum generalization of the classical preferential relocation model. Working in the energy eigenbasis, we derive the exact evolution of every density-matrix element for an arbitrary time-independent Hamiltonian and show that the Hamiltonian enters the dynamics only through the corresponding Bohr frequencies. This leads to a natural distinction between two classes of quantum systems: gapped and gapless. In \emph{gapped systems} (systems with a discrete energy spectrum), while the diagonal elements remain unchanged, the off-diagonal elements of the density matrix in the energy eigenbasis decay algebraically with a continuously varying exponent and with an amplitude that oscillates periodically in $\log t$. The system therefore approaches a stationary state that is independent of the resetting rate and retains a strong memory of the initial state. In \emph{gapless systems} (systems with a continuous energy spectrum), arbitrarily small Bohr frequencies prevent stationarity. Instead, the position distribution spreads on the universal (ultra-slow) scale $\log(rt)/r$, independently of the initial state and of the details of the Hamiltonian. We illustrate these results with a two-level system, a harmonic oscillator, and a free quantum particle, and contrast them with their classical counterparts.

## Full Text

Quantum resetting with memory

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.02297v1 [cond-mat.stat-mech] 03 Aug 2026

## Quantum resetting with memoryGabriele de MauroLPTMS, CNRS, Univ. Paris-Sud, Université Paris-Saclay, 91405 Orsay, France
gabriele.de-mauro@universite-paris-saclay.frManas KulkarniInternational Centre for Theoretical Sciences, Tata Institute of Fundamental Research,
Bengaluru 560089, India
manas.kulkarni@icts.res.inSatya N. MajumdarLPTMS, CNRS, Univ. Paris-Sud, Université Paris-Saclay, 91405 Orsay, France
satyanarayan.majumdar@cnrs.fr

## Abstract

We introduce a quantum stochastic resetting protocol with uniform memory, in which each resetting event returns the system to a state visited at a time chosen uniformly from its entire history. The resulting dynamics is nonunitary, non-Markovian and a direct quantum generalization of the classical preferential relocation model. Working in the energy eigenbasis, we derive the exact evolution of every density-matrix element for an arbitrary time-independent Hamiltonian and show that the Hamiltonian enters the dynamics only through the corresponding Bohr frequencies. This leads to a natural distinction between two classes of quantum systems: gapped and gapless. Ingapped systems(systems with a discrete energy spectrum), while the diagonal elements remain unchanged, the off-diagonal elements of the density matrix in the energy eigenbasis decay algebraically with a continuously varying exponent and with an amplitude that oscillates periodically inlog⁡t\log t. The system therefore approaches a stationary state that is independent of the resetting rate and retains a strong memory of the initial state. Ingapless systems(systems with a continuous energy spectrum), arbitrarily small Bohr frequencies prevent stationarity.
Instead, the position distribution spreads on the universal (ultra-slow) scalelog⁡(r​t)/r\log(rt)/r, independently of the initial state and of the details of the Hamiltonian.
We illustrate these results with a two-level system, a harmonic oscillator, and a free quantum particle, and contrast them with their classical counterparts.

## 1Introduction

Stochastic resetting[1,2,3,4,5,6]consists of interrupting a dynamical process at random times and returning the system to a prescribed state. By introducing an additional time scale, it can qualitatively reshape the underlying dynamics, with important consequences for first-passage and search properties. These effects have been studied in diffusive target-search problems[1,2,7,8,9,10,11], under time-dependent resetting[12], in spatially dependent or heterogeneous environments[13,14,15], and in the presence of partially absorbing targets[16,17].
Another important protocol is threshold resetting[18,19], in which a reset is triggered when the process reaches a prescribed threshold rather than by an external Poisson clock. Related developments include collective searches[20,21], lattice systems[22,23,24], and adaptive navigation strategies[25,26,27].
Besides providing an efficient search strategy, stochastic resetting also has another important aspect, namely that it drives a system to a nonequilibrium stationary state (NESS)[1,2,28,29,30,31,32,33,34]. Moreover, a common stochastic driving can induce strong correlations between otherwise independent degrees of freedom. Such dynamically emergent correlations (DEC) have been investigated in Brownian gases under different resetting protocols[35,36,37,38,39,40,41,42,43], in systems driven by fluctuating common environments[44,45,46], and within more general theoretical frameworks[47,48,49]. The same mechanism has also been extended to batch resetting events, where only a fraction of the particles is reset while the others continue to evolve via their reset-free dynamics[50].
Experimental realizations have been achieved in colloidal systems using optical trapping techniques, both for single particles[51,52,53,54]and for many-particle systems[55,56]. For a recent perspective article on DEC see Ref.[57].

More recently, stochastic resetting has been extended to quantum systems, with studies focusing on the resulting dynamics and stationary states[58,59,60,61,62,63,64,65,66,67], open quantum systems[68,69,70], first-detection and quantum-search problems[71,72,73,74,75], and many-body correlations and entanglement[78,79,80,76,77,81,82,83].

In most of the models mentioned above, classical or quantum, the reset is memory-less and the system is returned to a fixed initial configuration or state. In these resetting protocols the process does not retain the memory of the history of the trajectory in the past. A class of classical models where the resetting involves memory has been recently studied, leading to rather interesting and nontrivial memory effects. These includes, in particular, the “preferential relocation” model of a random walk, in which the walker is relocated at a constant raterrto
a position visited at a past time chosen uniformly from its entire history[84]. This is also known as the “monkey walk”, since certain species of rhesus monkeys follow this resetting pattern during their foraging period[84]. This model has also been studied in the mathematical literature, where several rigorous results were obtained[85].
These studies were extended further to more general memory kernels[86]and to
generic random-walk settings[87], including Lévy processes.
The preferential relocation model in the presence of a spatial impurity was
studied in Refs.[88,89], where the interplay between
memory and spatial heterogeneity was shown to produce an Anderson-like
localization transition. A mini-review of random walks with memory-induced
relocations can be found in Ref.[90].
A continuous-space formulation for Brownian
diffusion was introduced in Ref.[91], together with a general
memory kernelK​(τ,t)K(\tau,t)that interpolates between Poissonian resetting to
the initial position and the preferential relocation protocol. Related
models have also been studied for active particles[92], sluggish
random walkers[93], confined diffusion[94,95],
and many-particle systems[39]. Depending on the temporal bias of
the memory kernel, the dynamics can exhibit conventional diffusion,
anomalous diffusion, or ultraslow spreading[91].

This naturally raises the question: what is the effect of memory on the resetting protocol for quantum systems?
Incorporating these memory effects in quantum systems is nontrivial. Unlike a classical trajectory, a quantum system is described by a density matrix that contains populations (diagonal elements of the density matrix) and coherences (off-diagonal elements), and a reset to a previously visited state must retain the corresponding quantum information. The resulting evolution combines coherent dynamics, stochastic resets, and temporal nonlocality, and is therefore generally nonunitary and non-Markovian[96]. Moreover, because the reset state depends explicitly on the preceding evolution, the conventional renewal formulation used for fixed-state quantum resetting[58]is no longer directly applicable.

In this work, we introduce a quantum resetting protocol with memory in which, at every resetting event, the system is returned to a state visited at an earlier time selected uniformly from its entire history. Thus, all previous times are chosen with equal probability. This is the quantum analog of the classical preferential relocation model. We formulate the corresponding evolution equation and develop a general analytical framework to study the resulting nonunitary and non-Markovian dynamics, contrasting it with conventional quantum resetting to the initial state[1,2,58].
Working in the energy eigenbasis, we derive the exact evolution of each density-matrix element for an arbitrary time-independent Hamiltonian and show that the microscopic details of the Hamiltonian enter only through the corresponding Bohr frequencies. We then investigate the consequences of this very general result for two broad classes of quantum systems. Forgapped quantum systems, more specifically, systems with a discrete energy spectrum, the relevant nonzero Bohr frequencies are bounded away from zero, leading to the algebraic suppression of coherences and relaxation towards a stationary state. We then illustrate this behavior using two concrete examples: a quantum two-level system and a quantum harmonic oscillator. Forgapless quantum systems, specifically systems with a continuous energy spectrum, arbitrarily small Bohr frequencies are instead present, producing qualitatively different long-time dynamics. We illustrate this regime using a freely propagating quantum particle with a general dispersion relation, whose reset-free evolution exhibits unbounded dispersive spreading.

This classification exposes a qualitative distinction in the long-time behavior. For gapped systems, uniform memory resetting drives the system towards a stationary state through an ultraslow power-law relaxation, in sharp contrast with the exponential approach typically observed. This algebraic decay is further accompanied by very slow oscillations, whose phase grows only logarithmically in time. Remarkably, the stationary state reached at long times coincides with the time average of the reset-free unitary dynamics and is therefore completely independent of the resetting raterr, while retaining a very strong memory of the initial condition. For gapless systems, by contrast, no stationary state is reached. Instead, the spatial extent continues to grow logarithmically in time. Thislog⁡t\log tgrowth is universal and determined solely by the presence of memory, whereas the asymptotic shape of the spreading distribution depends on both the initial state and the specific dispersion relation, and therefore also retains a very strong memory of the initial condition. Thus, in both cases, the dynamics preserves a strong memory of the initial state, while the existence of a spectral gap determines whether the memory-induced ultraslow dynamics culminates in stationarity or in persistent spreading.

Despite this sharp distinction, both categories exhibit a common suppression of the intrinsic quantum dynamics. Under stochastic resetting with uniform memory, the continually expanding history progressively reduces the relative weight of newly generated states, leading to ultraslow evolution governed primarily by the temporal structure of the memory kernel rather than by the microscopic details of the Hamiltonian. This behavior contrasts sharply with conventional resetting, which typically produces an exponentially fast approach to a NESS. Quantum resetting with memory therefore provides a general framework for generating and controlling slow, non-Markovian dynamical regimes in both gapped and gapless quantum systems.

The paper is organized as follows. In Sec.2, we formulate the general protocol for quantum resetting with memory. We then discuss gapped quantum systems in Sec.3, using the two-level system and the quantum harmonic oscillator as representative examples. In Sec.4, we discuss gapless quantum systems, illustrated by the free quantum particle. Conclusions and an outlook are presented in Sec.5, while technical details are relegated to the appendices.

## 2Quantum resetting protocol with memory

In this section, we formulate a general framework for quantum stochastic
resetting with memory. We first review the reset-free unitary dynamics and
conventional Poissonian resetting to a fixed state, and then extend the
corresponding evolution equation to a protocol in which the reset state is
sampled from the system’s own history.

We consider a closed quantum system governed by a time-independent
HamiltonianH^\hat{H}. Att=0t=0, the system is prepared in a general density
matrixρ^0​(0)\hat{\rho}_{0}(0), which may describe either a pure or a mixed state.
Throughout this work, we setℏ=1\hbar=1. In the absence of resetting, the
density matrixρ^0​(t)\hat{\rho}_{0}(t)evolves unitarily as[97]ρ^0​(t)=e−i​H^​t​ρ^0​(0)​ei​H^​t.\hat{\rho}_{0}(t)=\mathrm{e}^{-\mathrm{i}\hat{H}t}\hat{\rho}_{0}(0)\mathrm{e}^{\mathrm{i}\hat{H}t}.(1)

Throughout the paper, the subscript0denotes the absence of resetting.
Equivalently, Eq. (1) satisfies the von Neumann equationd​ρ^0​(t)d​t=−i​[H^,ρ^0​(t)],\frac{\mathrm{d}\hat{\rho}_{0}(t)}{\mathrm{d}t}=-\mathrm{i}\left[\hat{H},\hat{\rho}_{0}(t)\right],(2)

with initial conditionρ^0​(0)\hat{\rho}_{0}(0).

We now introduce stochastic resetting events occurring according to a Poisson
process with constant raterr. The probability that no reset occurs during
a time interval of durationttise−r​t\mathrm{e}^{-rt}, while the waiting timeτ\taubetween consecutive resets is distributed asR​(τ)=r​e−r​τR(\tau)=r\,\mathrm{e}^{-r\tau}. Starting fromρ^0​(0)\hat{\rho}_{0}(0), the dynamics is
defined by the following protocol:
- (i)

A waiting time (sayτ1\tau_{1}) is drawn from the exponential distributionR​(τ)=r​e−r​τR(\tau)=r\,\mathrm{e}^{-r\tau}. During this interval, the system evolves
unitarily according to Eq. (1).
- (ii)

At timeτ1\tau_{1}, a resetting event occurs and the system is
instantaneously returned to its initial stateρ^0​(0)\hat{\rho}_{0}(0).

After the reset, a new waiting time (sayτ2\tau_{2}) is independently drawn from the
same distributionR​(τ)R(\tau). The system then evolves unitarily for a durationτ2\tau_{2}before being reset again toρ^0​(0)\hat{\rho}_{0}(0). This sequence of unitary
evolution intervals and instantaneous resetting events is repeated
indefinitely.

We denote byρ^r​(t)\hat{\rho}_{r}(t)the density matrix averaged over all possible
realizations of the resetting process, where the subscriptrrindicates a resetting raterr.
The expectation value of a generic observableO^\hat{O}is then given by⟨O^​(t)⟩r=Tr⁡[ρ^r​(t)​O^]\left\langle\hat{O}(t)\right\rangle_{r}=\operatorname{Tr}\left[\hat{\rho}_{r}(t)\hat{O}\right].
Since the previous history of the process becomes irrelevant once a reset event occurs, the density matrixρ^r​(t)\hat{\rho}_{r}(t)satisfies the renewal equation[3,58]ρ^r​(t)=e−r​t​ρ^0​(t)+r​∫0tdτ​e−r​τ​ρ^0​(τ).\hat{\rho}_{r}(t)=\mathrm{e}^{-rt}\hat{\rho}_{0}(t)+r\int_{0}^{t}\mathrm{d}\tau\,\mathrm{e}^{-r\tau}\hat{\rho}_{0}(\tau).(3)

The first term accounts for realizations in which no resetting event occurs up to timett. This happens with probabilitye−r​t\mathrm{e}^{-rt}, and the system therefore evolves unitarily from its initial state for the entire time intervaltt, resulting in the reset-free density matrixρ^0​(t)\hat{\rho}_{0}(t). The second term accounts for realizations in which at least one resetting event has occurred. In this term,τ\taudenotes the time elapsed since the most recent reset. Because that reset returns the system exactly to its initial state, the evolution before the most recent reset is irrelevant. The system subsequently evolves freely for a timeτ\tau, reaching the stateρ^0​(τ)\hat{\rho}_{0}(\tau). The factorr​e−r​τ​d​τr\,\mathrm{e}^{-r\tau}\mathrm{d}\taugives the probability that the most recent reset occurred betweent−τt-\tauandt−τ+d​τt-\tau+\mathrm{d}\tau, with no further resets during the following interval of durationτ\tau. Integrating overτ∈[0,t]\tau\in[0,t]therefore averages over all possible times elapsed since the most recent resetting event.

Equation (3) is equivalent to the following “Master equation” [seeA]:d​ρ^r​(t)d​t=−i​[H^,ρ^r​(t)]−r​ρ^r​(t)+r​ρ^0​(0).\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-\mathrm{i}\left[\hat{H},\hat{\rho}_{r}(t)\right]-r\hat{\rho}_{r}(t)+r\hat{\rho}_{0}(0).(4)

The first term describes the unitary evolution generated byH^\hat{H}, the second term accounts for the loss of probability from the current state due to resetting, and the last term reinjects this probability into the fixed reset stateρ^0​(0)\hat{\rho}_{0}(0).
Equation (3) provides the explicit solution to Eq. (4) and is generally the most convenient formulation whenever a renewal description is available. For this reason, previous studies of quantum stochastic resetting have typically relied directly on the renewal equation (3). In the present work, however, it is useful to introduce the equivalent differential formulation in Eq. (4). As we will see below, this formulation can be generalized more naturally to situations in which a simple renewal decomposition is no longer available, as occurs when memory effects are introduced.

We now use the differential formulation given in Eq. (4) to generalize the resetting protocol to the case in which the reset state depends on the system’s previous evolution. The protocol again begins with step(i), while step(ii)is slightly modified: the system is no longer returned to a fixed state. Instead, when a resetting event occurs at timett, a past timeτ\tauis selected uniformly in[0,t][0,t]. The corresponding equation readsd​ρ^r​(t)d​t=−i​[H^,ρ^r​(t)]−r​ρ^r​(t)+rt​∫0tdτ​ρ^r​(τ).\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-\mathrm{i}\left[\hat{H},\hat{\rho}_{r}(t)\right]-r\hat{\rho}_{r}(t)+\frac{r}{t}\int_{0}^{t}\mathrm{d}\tau\,\hat{\rho}_{r}(\tau).(5)

The first two terms in Eq. (5) are identical to those in Eq. (4) and retain the same physical
interpretation. The first term describes the unitary evolution generated by
the HamiltonianH^\hat{H}, while the second accounts for the loss of
probability from the state occupied at timettdue to resetting events.
The last term generalizes the reinjection termr​ρ^0​(0)r\hat{\rho}_{0}(0)appearing in
Eq. (4). In conventional resetting, the system is always returned to the fixed initial stateρ^0​(0)\hat{\rho}_{0}(0). In the
uniform memory protocol, instead, a past timeτ\tauis sampled uniformly in[0,t][0,t], and the system is reset to
the state previously occupied at that time, described byρ^r​(τ)\hat{\rho}_{r}(\tau). The
quantityd​τ/t\mathrm{d}\tau/tin the last term of Eq. (5) is the probability of selecting a past time in the interval[τ,τ+d​τ][\tau,\tau+\mathrm{d}\tau]. The integral therefore averages the reset state over all possible past times, while the prefactorrraccounts for the rate at which resetting events occur.
Since the reinjection term depends on the density matrix at all previous timesτ≤t\tau\leq t, the resulting evolution is nonlocal in time. Consequently, the dynamics is generally non-Markovian and does not admit the simple renewal representation of Eq. (3). The main goal of this work is to study Eq. (5) for two very general classes of quantum systems:gapped systems, namely systems whose Hamiltonian has a discrete spectrum, andgapless systems, namely systems whose Hamiltonian has a continuous spectrum.

Equation (5) is the quantum counterpart of the
Fokker–Planck equation for the classical position distributionPr​(x,t)P_{r}(x,t)under uniform memory resetting[84,86,87,91,88,89,90,85,92,94,95,39,93], with the density matrixρ^r​(t)\hat{\rho}_{r}(t)playing the role of the
classical probability distribution and the reset-free classical dynamics
replaced by the unitary evolution generated byH^\hat{H}. Classical resetting
with memory has been extensively studied because the repeated sampling of
past configurations can strongly modify the long-time dynamics, producing
anomalous diffusion, ultraslow spreading, and unusually slow relaxation
towards stationary states. In particular, a Brownian particle diffusing on
the infinite line under uniform memory resetting was studied in
Ref.[91]. In this case, no stationary state is reached and the
position distribution remains asymptotically Gaussian, but with a characteristic width growing aslog⁡t\sqrt{\log t}. This system can be regarded as the
classical analogue of the gapless quantum systems considered here, since the
corresponding Fokker–Planck operator has a continuous spectrum extending
down to zero. By contrast, classical Brownian particles evolving in a
confining potentialV​(x)V(x)were studied in
Refs.[94]with the same uniform memory kernel. Remarkably, despite the history-dependent
resetting dynamics, the probability distribution approaches the equilibrium
Gibbs–Boltzmann state at long times, independently of the initial condition.
The relaxation towards this stationary state is, however, extremely slow
and occurs algebraically rather than exponentially, with an exponent that depends on the resetting raterrand the smallest nonzero eigenvalue of the Fokker–Planck operator. These confined systems
provide the natural classical counterparts of the gapped quantum systems
studied here, since their Fokker–Planck operator has a discrete spectrum
with a finite gap above its stationary mode. More generally, Ref.[91]studied the unconfined Brownian particle for a generic memory kernelK​(τ,t)K(\tau,t), with uniform memory corresponding to the particular choiceK​(τ,t)=1/tK(\tau,t)=1/t. Similarly, Ref.[95]extended the analysis of confined diffusion to a broad class of memory kernels, showing how the sampling of the past affects both the stationary state and the relaxation towards it. In the present work, however, we focus exclusively on the uniform memory kernel and leave the extension to more general memory kernels as an interesting open problem.

As we will see, the classical and quantum problems share the same basic
spectral distinction. In both cases, a discrete spectrum with a finite gap
leads to an ultraslow power-law relaxation towards a stationary state,
whereas a continuous spectrum extending down to zero prevents stationarity
and produces persistent ultraslow spreading. The long-time behavior,
however, differs in crucial ways. For confined classical systems, the
stationary state is always the equilibrium Gibbs–Boltzmann distribution[94]and it
is therefore independent of the initial condition, while in the gapped quantum case it
retains a strong memory of the initial state. In particular, for a nondegenerate spectrum, the stationary density matrix is given by the initial populations in the energy eigenbasis,ρ^rst=∑nρn​n​(0)​|n⟩​⟨n|.\hat{\rho}_{r}^{\rm st}=\sum_{n}\rho_{nn}(0)\ket{n}\bra{n}.(6)

Similarly, for an unconfined classical particle, the distribution remains
asymptotically Gaussian and its width grows aslog⁡t\sqrt{\log t}[91], whereas in
the gapless quantum case the width grows aslog⁡t\log t. Moreover, the
asymptotic quantum distribution again retains a strong memory of the
microscopic dynamics, since its shape depends on both the initial state and
the specific dispersion relation. These differences originate from the
coherent unitary dynamics and therefore represent genuinely quantum effects.

Having established the classical–quantum correspondence and anticipated the
central role played by the spectral properties of the underlying dynamics, we
now turn to the exact solution of Eq. (5). The energy
eigenbasis provides the natural framework for this analysis, since it
diagonalizes the unitary part of the evolution and makes the dependence on
the energy spectrum explicit. Without yet assuming whether the spectrum is discrete or continuous, we denote its energy eigenstates generically byH^​|m⟩=Em​|m⟩\hat{H}\ket{m}=E_{m}\ket{m}and defineρr,m​n​(t)=⟨m|​ρ^r​(t)​|n⟩\rho_{r,mn}(t)=\bra{m}\hat{\rho}_{r}(t)\ket{n}. Projecting
Eq. (5) between⟨m|\bra{m}and|n⟩\ket{n}, we obtaind​ρr,m​n​(t)d​t=−[r+i​(Em−En)]​ρr,m​n​(t)+rt​∫0tdτ​ρr,m​n​(τ).\frac{\mathrm{d}\rho_{r,mn}(t)}{\mathrm{d}t}=-\left[r+\mathrm{i}(E_{m}-E_{n})\right]\rho_{r,mn}(t)+\frac{r}{t}\int_{0}^{t}\mathrm{d}\tau\,\rho_{r,mn}(\tau).(7)

Equation (7) shows that the different
matrix elements ofρ^r​(t)\hat{\rho}_{r}(t)evolve independently in the energy
basis. The Hamiltonian enters their evolution only through the corresponding
Bohr frequencyωm​n≡Em−En\omega_{mn}\equiv E_{m}-E_{n}. More precisely, the evolution of
every matrix element can be written asρr,m​n​(t)=ρr,m​n​(0)​f​(ωm​n,t),\rho_{r,mn}(t)=\rho_{r,mn}(0)f\left(\omega_{mn},t\right),(8)

where the same scalar functionf​(ω,t)f(\omega,t), evaluated at the corresponding Bohr frequency, governs the time dependence of every matrix element. It therefore remains to determinef​(ω,t)f(\omega,t).
Substituting Eq. (8) into Eq. (7), we obtaind​f​(ω,t)d​t=−(r+i​ω)​f​(ω,t)+rt​∫0tdτ​f​(ω,τ).\frac{\mathrm{d}f(\omega,t)}{\mathrm{d}t}=-\left(r+\mathrm{i}\omega\right)f(\omega,t)+\frac{r}{t}\int_{0}^{t}\mathrm{d}\tau\,f(\omega,\tau).(9)

Multiplying Eq. (9) byttand differentiating with respect to time eliminates the memory integral and yieldst​f′′​(ω,t)+[1+(r+i​ω)​t]​f′​(ω,t)+i​ω​f​(ω,t)=0.tf^{\prime\prime}(\omega,t)+\left[1+\left(r+\mathrm{i}\omega\right)t\right]f^{\prime}(\omega,t)+\mathrm{i}\omega f(\omega,t)=0.(10)

Because this is a second-order equation, it requires two initial conditions. The first follows directly from Eq. (8), namelyf​(ω,0)=1f(\omega,0)=1. The second is obtained by taking the limitt→0t\to 0in Eq. (9). Sincelimt→0t−1​∫0tdτ​f​(ω,τ)=f​(ω,0)\lim_{t\to 0}t^{-1}\int_{0}^{t}\mathrm{d}\tau\,f(\omega,\tau)=f(\omega,0), one findsf′​(ω,0)=−i​ωf^{\prime}(\omega,0)=-\mathrm{i}\omega.
Introducingu=−(r+i​ω)​tu=-(r+\mathrm{i}\omega)tandχ​(ω)=i​ω/(r+i​ω)\chi(\omega)=\mathrm{i}\omega/(r+\mathrm{i}\omega), and usingd/d​t=−(r+i​ω)​d/d​u\mathrm{d}/\mathrm{d}t=-(r+\mathrm{i}\omega)\mathrm{d}/\mathrm{d}u,
Eq. (10) becomesu​d2​fd​u2+(1−u)​d​fd​u−χ​(ω)​f=0.u\frac{\mathrm{d}^{2}f}{\mathrm{d}u^{2}}+(1-u)\frac{\mathrm{d}f}{\mathrm{d}u}-\chi(\omega)f=0.(11)

Eq. (11) is Kummer’s confluent hypergeometric equation (see Eq. 13.2.1 of
Ref.[98]).
The general solution is a linear combination ofM​(χ;1;u)M(\chi;1;u)andU​(χ;1;u)U(\chi;1;u), respectively known as Kummer’s confluent hypergeometric function of the first kind and Tricomi’s confluent hypergeometric function of the second kind.
SinceU​(χ,1,u)U(\chi,1,u)is singular atu=0u=0for genericχ\chi, regularity at the initial time excludes this solution. UsingM​(χ,1,0)=1M(\chi,1,0)=1, the conditionf​(ω,0)=1f(\omega,0)=1then givesf​(ω,t)=M​(i​ωr+i​ω;1;−(r+i​ω)​t).f(\omega,t)=M\left(\frac{\mathrm{i}\omega}{r+\mathrm{i}\omega};1;-\left(r+\mathrm{i}\omega\right)t\right).(12)

Since∂uM​(a,b,u)|u=0=a/b\left.\partial_{u}M(a,b,u)\right|_{u=0}=a/b, this solution also satisfiesf′​(ω,0)=−(r+i​ω)​χ​(ω)=−i​ωf^{\prime}(\omega,0)=-(r+\mathrm{i}\omega)\chi(\omega)=-\mathrm{i}\omega.
Forω=0\omega=0, Eq. (9) directly
gives the constant solutionf​(0,t)=1f(0,t)=1.
Consequently, the complete density matrix in the energy basis isρr,m​n​(t)=ρr,m​n​(0)​M​(i​ωm​nr+i​ωm​n;1;−(r+i​ωm​n)​t).\rho_{r,mn}(t)=\rho_{r,mn}(0)M\left(\frac{\mathrm{i}\omega_{mn}}{r+\mathrm{i}\omega_{mn}};1;-\left(r+\mathrm{i}\omega_{mn}\right)t\right).(13)

For the diagonal elements,ωm​m=0\omega_{mm}=0, and thereforeρr,m​m​(t)=ρr,m​m​(0)\rho_{r,mm}(t)=\rho_{r,mm}(0).
Hence, the populations in the energy eigenbasis remain equal to their
initial values at all times. More generally, whenever two energy eigenstates
are degenerate,Em=EnE_{m}=E_{n}, one hasωm​n=0\omega_{mn}=0and thereforeρr,m​n​(t)=ρr,m​n​(0)\rho_{r,mn}(t)=\rho_{r,mn}(0).
Thus, uniform memory resetting preserves both the energy populations and
the coherences within each degenerate energy eigenspace. The nontrivial
dynamics is entirely carried by matrix elements connecting states with
different energies.
Equation (13) is the central result of this work. It is completely
general and it applies to any time-independent Hamiltonian, irrespective of
whether its spectrum is gapped or gapless. Remarkably, the details of the reset-free unitary dynamics enter only through the Bohr frequenciesωm​n\omega_{mn}.

We now analyze the general long-time behavior of Eq. (13). For a fixed nonzeroω\omega, the large-argument asymptotic expansion of Kummer’s function gives
[see Eq. (13.7.2) of Ref.[98]]f​(ω,t)≈[(r+i​ω)​t]−χ​(ω)Γ​(1−χ​(ω)),t→∞,f(\omega,t)\approx\frac{\left[\left(r+\mathrm{i}\omega\right)t\right]^{-\chi(\omega)}}{\Gamma\left(1-\chi(\omega)\right)},\qquad t\to\infty,(14)

whereχ​(ω)=i​ω/(r+i​ω)\chi(\omega)=\mathrm{i}\omega/(r+\mathrm{i}\omega). Separating its real and
imaginary parts asχ​(ω)=χR​(ω)+i​χI​(ω)\chi(\omega)=\chi_{\rm R}(\omega)+\mathrm{i}\chi_{\rm I}(\omega), we haveχR​(ω)=ω2r2+ω2\chi_{\rm R}(\omega)=\frac{\omega^{2}}{r^{2}+\omega^{2}}andχI​(ω)=r​ωr2+ω2\chi_{\rm I}(\omega)=\frac{r\omega}{r^{2}+\omega^{2}}.
We also writer+i​ω=r2+ω2​ei​θ​(ω)r+\mathrm{i}\omega=\sqrt{r^{2}+\omega^{2}}\,\mathrm{e}^{\mathrm{i}\theta(\omega)}, whereθ​(ω)=arctan⁡(ω/r)\theta(\omega)=\arctan(\omega/r). Equation (14)
can then be expressed asf​(ω,t)≈C​(ω)​[r2+ω2​t]−χR​(ω)​e−i​[χI​(ω)​log⁡(r2+ω2​t)+φ​(ω)],f(\omega,t)\approx C(\omega)\left[\sqrt{r^{2}+\omega^{2}}\,t\right]^{-\chi_{\rm R}(\omega)}\mathrm{e}^{-\mathrm{i}\left[\chi_{\rm I}(\omega)\log\left(\sqrt{r^{2}+\omega^{2}}\,t\right)+\varphi(\omega)\right]},(15)

whereC​(ω)=eχI​(ω)​θ​(ω)|Γ​(1−χR​(ω)−i​χI​(ω))|C(\omega)=\frac{\mathrm{e}^{\chi_{\rm I}(\omega)\theta(\omega)}}{\left|\Gamma\left(1-\chi_{\rm R}(\omega)-\mathrm{i}\chi_{\rm I}(\omega)\right)\right|}(16)

andφ​(ω)=χR​(ω)​θ​(ω)+arg⁡Γ​(1−χR​(ω)−i​χI​(ω)).\varphi(\omega)=\chi_{\rm R}(\omega)\theta(\omega)+\arg\Gamma\left(1-\chi_{\rm R}(\omega)-\mathrm{i}\chi_{\rm I}(\omega)\right).(17)

Consequently, the modulus off​(ω,t)f(\omega,t)decays algebraically as|f​(ω,t)|=O​(t−ω2r2+ω2)\left|f(\omega,t)\right|=O\left(t^{-\frac{\omega^{2}}{r^{2}+\omega^{2}}}\right),
while its phase oscillates periodically as a function oflog⁡t\log t, with logarithmic angular frequencyχI​(ω)=r​ω/(r2+ω2)\chi_{\rm I}(\omega)=r\omega/(r^{2}+\omega^{2}).
In particular,f​(ω,t)→0f(\omega,t)\to 0ast→∞t\to\inftyfor every fixedω≠0\omega\neq 0, since0<χR​(ω)=ω2/(r2+ω2)<10<\chi_{\rm R}(\omega)=\omega^{2}/(r^{2}+\omega^{2})<1. Therefore, every
density-matrix element connecting states with different energies vanishes
algebraically at long times:ρr,m​n​(t)≈ρr,m​n​(0)​C​(ωm​n)​[r2+ωm​n2​t]−χR​(ωm​n)​e−i​[χI​(ωm​n)​log⁡(r2+ωm​n2​t)+φ​(ωm​n)],\rho_{r,mn}(t)\approx\rho_{r,mn}(0)\,C(\omega_{mn})\left[\sqrt{r^{2}+\omega_{mn}^{2}}\,t\right]^{-\chi_{\rm R}(\omega_{mn})}\mathrm{e}^{-\mathrm{i}\left[\chi_{\rm I}(\omega_{mn})\log\left(\sqrt{r^{2}+\omega_{mn}^{2}}\,t\right)+\varphi(\omega_{mn})\right]},(18)

forEm≠EnE_{m}\neq E_{n}. The last term in Eq. (18) has unit modulus and a phase that grows only logarithmically in time, giving rise to extremely slow oscillations that are periodic inlog⁡t\log t.
For the diagonal elements, instead, the Bohr frequency vanishes,ωm​m=0\omega_{mm}=0.
The exact solutionf​(0,t)=1f(0,t)=1therefore givesρr,m​m​(t)=ρr,m​m​(0),\rho_{r,mm}(t)=\rho_{r,mm}(0),(19)

for all timestt. Hence, the populations (diagonal elements) in the energy eigenbasis remain unchanged throughout the evolution. Together with
Eq. (18), Eq. (19) shows that, whenever
the relevant nonzero Bohr frequencies are bounded away from zero, all
coherences between states with different energies vanish algebraically at
long times, while the populations remain fixed. The system consequently approaches the stationary state given in Eq. (6).

This dephasing (loss of coherence) mechanism is reminiscent of dephasing Linbladian terms in an open quantum system[99,100,101,102]. However, the crucial differnce is that the Lindbaldian terms arise out of environmental effects and usually cause dephasing at an exponentially fast rate. In our case, the dephasing is caused because the system revisits its own history and it occurs algebraically slowly.

## 3Gapped Quantum Systems

In this section, we discuss the implications of the general solution in
Eq. (13) for a gapped quantum
system. We consider a system described by a time-independent Hamiltonian with
a discrete and nondegenerate energy spectrum,H^​|n⟩=En​|n⟩,\hat{H}\ket{n}=E_{n}\ket{n},withEm≠EnE_{m}\neq E_{n}form≠n.m\neq n.We further assume that the nonzero Bohr frequenciesωm​n≡Em−En\omega_{mn}\equiv E_{m}-E_{n}relevant to the dynamics are bounded away from zero. Namely, there exists a finite frequency gapΔ=minm≠n⁡|ωm​n|>0.\Delta=\min_{m\neq n}|\omega_{mn}|>0.(20)

As shown in
Sec.2, the different matrix elementsρr,m​n​(t)=⟨m|​ρ^r​(t)​|n⟩\rho_{r,mn}(t)=\bra{m}\hat{\rho}_{r}(t)\ket{n}evolve independently according to Eq. (7). Their exact time-dependent solution is given in
Eq. (13), while their long-time
behavior follows from Eq. (18).
For every pair of distinct states, one has|ωm​n|≥Δ>0|\omega_{mn}|\geq\Delta>0. Therefore, all off-diagonal matrix elements
vanish algebraically at long times. In particular, whenm≠nm\neq n, their modulus behaves as|ρr,m​n​(t)|∼t−ωm​n2r2+ωm​n2\left|\rho_{r,mn}(t)\right|\sim t^{-\frac{\omega_{mn}^{2}}{r^{2}+\omega_{mn}^{2}}},
while their phase oscillates periodically as a function oflog⁡t\log t, with logarithmic angular frequencyr​ωm​n/(r2+ωm​n2)r\omega_{mn}/(r^{2}+\omega_{mn}^{2}).
Since the decay exponentωm​n2/(r2+ωm​n2)\omega_{mn}^{2}/(r^{2}+\omega_{mn}^{2})increases monotonically with|ωm​n||\omega_{mn}|, the slowest-decaying contribution is associated with the
smallest nonzero Bohr frequencyΔ\Delta. Therefore, the asymptotic approach of the full density matrix to the stationary state is controlled only byΔ\Deltaand the resetting raterr:ρ^r​(t)−ρ^rst=O​(t−θ),θ=Δ2r2+Δ2,\hat{\rho}_{r}(t)-\hat{\rho}_{r}^{\rm st}=O\left(t^{-\theta}\right),\qquad\theta=\frac{\Delta^{2}}{r^{2}+\Delta^{2}},(21)

where0<θ<10<\theta<1. A similar algebraic relaxation occurs for a classical diffusing particle
confined by a potential and subject to uniform memory resetting[94].
In that case, the probability distribution approaches the Gibbs–Boltzmann
stationary state algebraically, with the slowest decay exponentθcl=λr+λ,\theta_{\rm cl}=\frac{\lambda}{r+\lambda},whereλ\lambdais the spectral gap between the stationary mode and the first
excited mode of the Fokker–Planck operator.
This is different from the quantum case, where the exponentθ\thetain Eq. (21) depends on the global minimum of all spectral gapsΔ\Delta.
The approach to the stationary state given in Eq. (21) is therefore anomalously slow
and algebraic, in sharp contrast with the exponential relaxation typically
observed under conventional resetting.
By contrast, the diagonal matrix elements correspond toωn​n=0\omega_{nn}=0and therefore remain equal to their initial values at all
times,ρr,n​n​(t)=ρr,n​n​(0).\rho_{r,nn}(t)=\rho_{r,nn}(0).The system consequently approaches the stationary density matrixρ^rst=∑nρr,n​n​(0)​|n⟩​⟨n|.\hat{\rho}_{r}^{\rm st}=\sum_{n}\rho_{r,nn}(0)\ket{n}\bra{n}.(22)

In other words, for a nondegenerate spectrum the long-time dynamics
suppresses all coherences between different energy eigenstates, while
preserving the initial populations. This can be represented schematically asρ^r​(0)=(ρ11​(0)ρ12​(0)⋯ρ1​N​(0)ρ21​(0)ρ22​(0)⋯ρ2​N​(0)⋮⋮⋱⋮ρN​1​(0)ρN​2​(0)⋯ρN​N​(0))→t→∞ρ^rst=(ρ11​(0)0⋯00ρ22​(0)⋯0⋮⋮⋱⋮00⋯ρN​N​(0)).\hat{\rho}_{r}(0)=\begin{pmatrix}\rho_{11}(0)&\rho_{12}(0)&\cdots&\rho_{1N}(0)\\
\rho_{21}(0)&\rho_{22}(0)&\cdots&\rho_{2N}(0)\\
\vdots&\vdots&\ddots&\vdots\\
\rho_{N1}(0)&\rho_{N2}(0)&\cdots&\rho_{NN}(0)\end{pmatrix}\;\xrightarrow{\,t\to\infty\,}\;\hat{\rho}_{r}^{\rm st}=\begin{pmatrix}\rho_{11}(0)&0&\cdots&0\\
0&\rho_{22}(0)&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&\rho_{NN}(0)\end{pmatrix}.(23)

The stationary state is therefore completely determined by the initial
populations and is remarkably independent of the resetting raterr. In this sense, a strong memory of the initial condition is retained.
This stationary state can also be identified with the infinite-time average
of the corresponding reset-free unitary evolution. Indeed, in the energy
eigenbasis the reset-free density matrix follows from Eq. (1) and reads[97]ρ^0​(t)=∑m,nρm​n​(0)​e−i​ωm​n​t​|m⟩​⟨n|.\hat{\rho}_{0}(t)=\sum_{m,n}\rho_{mn}(0)\mathrm{e}^{-\mathrm{i}\omega_{mn}t}\ket{m}\bra{n}.(24)

Averaging this expression over a time interval of durationTTgives1T​∫0Tdt​ρ^0​(t)=∑m,nρm​n​(0)​[1T​∫0Tdt​e−i​ωm​n​t]​|m⟩​⟨n|.\displaystyle\frac{1}{T}\int_{0}^{T}\mathrm{d}t\,\hat{\rho}_{0}(t)=\sum_{m,n}\rho_{mn}(0)\left[\frac{1}{T}\int_{0}^{T}\mathrm{d}t\,\mathrm{e}^{-\mathrm{i}\omega_{mn}t}\right]\ket{m}\bra{n}.(25)

For a nondegenerate spectrum and for largeTT, we can use the identitylimT→∞1T​∫0Tdt​e−i​ωm​n​t=δm​n\lim_{T\to\infty}\frac{1}{T}\int_{0}^{T}\mathrm{d}t\,\mathrm{e}^{-\mathrm{i}\omega_{mn}t}=\delta_{mn}.
Hence,ρ^rst=limT→∞1T​∫0Tdt​ρ^0​(t)=∑nρn​n​(0)​|n⟩​⟨n|,\hat{\rho}_{r}^{\rm st}=\lim_{T\to\infty}\frac{1}{T}\int_{0}^{T}\mathrm{d}t\,\hat{\rho}_{0}(t)=\sum_{n}\rho_{nn}(0)\ket{n}\bra{n},(26)

which coincides with
Eq. (22).
Here, the limitT→∞T\to\inftymeans that the averaging interval is much longer than the longest relevant oscillation period, namelyT≫2​π/ΔT\gg 2\pi/\Delta. In this regime, all off-diagonal contributions undergo many oscillations and average to zero.
Uniform-memory resetting therefore progressively suppresses the oscillatory
contributions associated with nonzero Bohr frequencies, while preserving the time-independent component of the reset-free dynamics.
As anticipated in Sec.2, this marks a crucial difference from the classical confined case[94]: although the approach to the stationary state is algebraic in both settings, the classical stationary state is always the Gibbs–Boltzmann distribution, independently of the initial condition, whereas in the quantum case the stationary state is entirely determined by the initial energy populations. In this sense, the quantum case has a stronger memory.

The extension to degenerate spectra is immediate: matrix elements connecting states with the same energy have zero Bohr frequency and therefore remain equal to their initial values, while those connecting different energies decay as above. We therefore do not discuss the degenerate case further.

In the following, we illustrate these general results through two concrete systems with a discrete energy spectrum: a quantum two-level system and a quantum harmonic oscillator.

## 3.1Quantum two-level system

We first illustrate the general results derived above using the simplest nontrivial gapped quantum system: a two-level system governed by the HamiltonianH^=Ω​σ^x\hat{H}=\Omega\hat{\sigma}_{x}, whereσ^x\hat{\sigma}_{x}is the Pauli matrix along thexxdirection. The corresponding energy eigenstates are|↑x⟩\ket{\uparrow_{x}}and|↓x⟩\ket{\downarrow_{x}}, with eigenenergiesE↑=+ΩE_{\uparrow}=+\OmegaandE↓=−ΩE_{\downarrow}=-\Omega, respectively.
The only nonzero Bohr frequencies are thereforeω↑↓=2​Ω\omega_{\uparrow\downarrow}=2\Omegaandω↓↑=−2​Ω\omega_{\downarrow\uparrow}=-2\Omega.
We consider a general initial density matrix in the energy basis,ρ^r​(0)=(ρ↑↑​(0)ρ↑↓​(0)ρ↓↑​(0)ρ↓↓​(0)),\hat{\rho}_{r}(0)=\begin{pmatrix}\rho_{\uparrow\uparrow}(0)&\rho_{\uparrow\downarrow}(0)\\
\rho_{\downarrow\uparrow}(0)&\rho_{\downarrow\downarrow}(0)\end{pmatrix},(27)

whereρ↑↑​(0)+ρ↓↓​(0)=1\rho_{\uparrow\uparrow}(0)+\rho_{\downarrow\downarrow}(0)=1andρ↓↑​(0)=ρ↑↓∗​(0)\rho_{\downarrow\uparrow}(0)=\rho_{\uparrow\downarrow}^{*}(0).
In the absence of resetting, the density matrix evolves unitarily according
to Eq. (1). Since the Hamiltonian is diagonal in theσ^x\hat{\sigma}_{x}basis, one obtains[97]ρ^0​(t)=(ρ↑↑​(0)ρ↑↓​(0)​e−2​i​Ω​tρ↓↑​(0)​e2​i​Ω​tρ↓↓​(0)).\hat{\rho}_{0}(t)=\begin{pmatrix}\rho_{\uparrow\uparrow}(0)&\rho_{\uparrow\downarrow}(0)\mathrm{e}^{-2\mathrm{i}\Omega t}\\
\rho_{\downarrow\uparrow}(0)\mathrm{e}^{2\mathrm{i}\Omega t}&\rho_{\downarrow\downarrow}(0)\end{pmatrix}.(28)

Thus, the energy populations remain constant, while the coherences oscillate
indefinitely with Bohr frequencies±2​Ω\pm 2\Omega.

We now consider stochastic resetting at a raterrwith uniform memory.
Using the general solution given by Eq. (8), we obtainρ^r​(t)=(ρ↑↑​(0)ρ↑↓​(0)​f​(2​Ω,t)ρ↓↑​(0)​f​(−2​Ω,t)ρ↓↓​(0)),\hat{\rho}_{r}(t)=\begin{pmatrix}\rho_{\uparrow\uparrow}(0)&\rho_{\uparrow\downarrow}(0)f(2\Omega,t)\\
\rho_{\downarrow\uparrow}(0)f(-2\Omega,t)&\rho_{\downarrow\downarrow}(0)\end{pmatrix},(29)

wheref​(ω,t)f(\omega,t)is given in Eq. (12).
Equation (29) directly illustrates the
general results derived above.Figure 1:Reset-averaged polarization⟨σ^z​(t)⟩r\langle\hat{\sigma}_{z}(t)\rangle_{r}for a two-level system withH^=Ω​σ^x\hat{H}=\Omega\hat{\sigma}_{x}, initially prepared in|↑z⟩\ket{\uparrow_{z}}.
(Left) Exact analytical result in Eq. (32)
(solid lines) and numerical simulations (circles) for different resetting
ratesrr. The polarization approaches zero through algebraically damped
oscillations.
(Right) Long-time behavior forr=5r=5, after the polarization has been multipliedtθt^{\theta}, withθ=4​Ω2/(r2+4​Ω2)\theta=4\Omega^{2}/(r^{2}+4\Omega^{2}).
This rescaling removes the algebraically decaying envelope [see Eq. (33)] and makes the slow
oscillations, which are periodic inlog⁡t\log t, clearly visible.
In both panels,Ω=1\Omega=1.

The diagonal elements, corresponding to zero
Bohr frequency, remain equal to their initial values:ρr,↑↑​(t)=ρ↑↑​(0)\rho_{r,\uparrow\uparrow}(t)=\rho_{\uparrow\uparrow}(0)andρr,↓↓​(t)=ρ↓↓​(0)\rho_{r,\downarrow\downarrow}(t)=\rho_{\downarrow\downarrow}(0).
By contrast, the off-diagonal elements evolve according to
Eq. (13). In this two-level
system, the frequency gap defined in Eq. (20) isΔ=2​Ω\Delta=2\Omega. Therefore, at large times, the modulus of the coherences
decays algebraically as|ρr,↑↓​(t)|∼t−θ,θ=Δ2r2+Δ2=4​Ω2r2+4​Ω2,\left|\rho_{r,\uparrow\downarrow}(t)\right|\sim t^{-\theta},\qquad\theta=\frac{\Delta^{2}}{r^{2}+\Delta^{2}}=\frac{4\Omega^{2}}{r^{2}+4\Omega^{2}},(30)

while their phase oscillates periodically as a function oflog⁡t\log t, with
logarithmic angular frequency2​r​Ω/(r2+4​Ω2)2r\Omega/(r^{2}+4\Omega^{2}). Consequently, the
spin approaches the stationary density matrix predicted by
Eq. (23),ρ^rst=(ρ↑↑​(0)00ρ↓↓​(0)).\hat{\rho}_{r}^{\rm st}=\begin{pmatrix}\rho_{\uparrow\uparrow}(0)&0\\
0&\rho_{\downarrow\downarrow}(0)\end{pmatrix}.(31)

This stationary state is independent of the resetting raterrand coincides with the infinite-time average of the reset-free density matrix in Eq. (28).

To illustrate these results and enable a direct comparison with numerical
simulations, we now consider the polarization along thezzdirection. It is obtained from⟨σ^z​(t)⟩r=Tr⁡[σ^z​ρ^r​(t)].\left\langle\hat{\sigma}_{z}(t)\right\rangle_{r}=\operatorname{Tr}\left[\hat{\sigma}_{z}\hat{\rho}_{r}(t)\right].Since, in theσ^x\hat{\sigma}_{x}basis,σ^z=|↑x⟩​⟨↓x|+|↓x⟩​⟨↑x|\hat{\sigma}_{z}=\ket{\uparrow_{x}}\bra{\downarrow_{x}}+\ket{\downarrow_{x}}\bra{\uparrow_{x}}[97],
we find, for the general initial condition in
Eq. (27),⟨σ^z​(t)⟩r=2​Re⁡[ρ↑↓​(0)​f​(2​Ω,t)].\left\langle\hat{\sigma}_{z}(t)\right\rangle_{r}=2\operatorname{Re}\left[\rho_{\uparrow\downarrow}(0)f(2\Omega,t)\right].In Fig.1, we specialize to the initial state|↑z⟩\ket{\uparrow_{z}}, for whichρ↑↓​(0)=1/2\rho_{\uparrow\downarrow}(0)=1/2in theσ^x\hat{\sigma}_{x}basis. Therefore,⟨σ^z​(t)⟩r=Re⁡[f​(2​Ω,t)]=Re⁡[M​(2​i​Ωr+2​i​Ω;1;−(r+2​i​Ω)​t)].\displaystyle\left\langle\hat{\sigma}_{z}(t)\right\rangle_{r}=\operatorname{Re}\left[f(2\Omega,t)\right]=\operatorname{Re}\left[M\left(\frac{2\mathrm{i}\Omega}{r+2\mathrm{i}\Omega};1;-\left(r+2\mathrm{i}\Omega\right)t\right)\right].(32)

Using Eq.(15), we find that at large times Eq. (32) behaves as⟨σ^z​(t)⟩r≈C​(2​Ω)​[r2+4​Ω2​t]−θ​cos⁡[2​r​Ωr2+4​Ω2​log⁡(r2+4​Ω2​t)+φ​(2​Ω)],\displaystyle\left\langle\hat{\sigma}_{z}(t)\right\rangle_{r}\approx C(2\Omega)\left[\sqrt{r^{2}+4\Omega^{2}}\,t\right]^{-\theta}\cos\left[\frac{2r\Omega}{r^{2}+4\Omega^{2}}\log\left(\sqrt{r^{2}+4\Omega^{2}}\,t\right)+\varphi(2\Omega)\right],(33)

where we recallθ=4​Ω2r2+4​Ω2\theta=\frac{4\Omega^{2}}{r^{2}+4\Omega^{2}},C​(ω)C(\omega)andφ​(ω)\varphi(\omega)are given in Eqs. (16) and (17), respectively.
Thus, the polarization approaches zero through oscillations (with an algebraically decaying envelope), which are periodic as a function oflog⁡t\log t.

## 3.2Quantum harmonic oscillator

As a second example, we consider a quantum harmonic oscillator of massmmand angular frequencyΩho\Omega_{\rm ho}, described byH^=p^22​m+12​m​Ωho2​x^2.\hat{H}=\frac{\hat{p}^{2}}{2m}+\frac{1}{2}m\Omega_{\rm ho}^{2}\hat{x}^{2}.(34)

Its energy eigenstates satisfyH^​|n⟩=En​|n⟩\hat{H}\ket{n}=E_{n}\ket{n}, withEn=Ωho​(n+1/2)E_{n}=\Omega_{\rm ho}(n+1/2)and Bohr frequenciesωn​ℓ=(n−ℓ)​Ωho\omega_{n\ell}=(n-\ell)\Omega_{\rm ho}. In the position representation,φn​(x)=⟨x|n⟩=(m​Ωhoπ)1/4​Hn​(m​Ωho​x)2n​n!​exp⁡(−m​Ωho​x22),\varphi_{n}(x)=\braket{x|n}=\left(\frac{m\Omega_{\rm ho}}{\pi}\right)^{1/4}\frac{H_{n}\left(\sqrt{m\Omega_{\rm ho}}\,x\right)}{\sqrt{2^{n}n!}}\exp\left(-\frac{m\Omega_{\rm ho}x^{2}}{2}\right),(35)

whereHnH_{n}is thenn-th Hermite polynomial[97].
We choose the normalized Gaussian initial stateψ0​(x,0)=(2​απ)1/4​e−α​x2,\psi_{0}(x,0)=\left(\frac{2\alpha}{\pi}\right)^{1/4}\mathrm{e}^{-\alpha x^{2}},(36)

and introduce the dimensionless width parameterη=2​αm​Ωho,\eta=\frac{2\alpha}{m\Omega_{\rm ho}},(37)

whereη=1\eta=1corresponds to the ground state of the harmonic oscillator. Sinceψ0​(x,0)\psi_{0}(x,0)is even, only even energy levels are populated, so that|ψ0​(0)⟩=∑n=0∞c2​n​|2​n⟩\ket{\psi_{0}(0)}=\sum_{n=0}^{\infty}c_{2n}\ket{2n}[97], withc2​n=(2​η1+η)1/2​(2​n)!2n​n!​(1−η1+η)n,c2​n+1=0.c_{2n}=\left(\frac{2\sqrt{\eta}}{1+\eta}\right)^{1/2}\frac{\sqrt{(2n)!}}{2^{n}n!}\left(\frac{1-\eta}{1+\eta}\right)^{n},\qquad c_{2n+1}=0.(38)

Forη=1\eta=1, one hasc0=1c_{0}=1andc2​n=0c_{2n}=0for alln≥1n\geq 1.
The reset-free and reset-averaged density matrices follow directly from Eqs. (1) and (8):ρ^0​(t)\displaystyle\hat{\rho}_{0}(t)=∑n,ℓ=0∞c2​n​c2​ℓ∗​e−2​i​(n−ℓ)​Ωho​t​|2​n⟩​⟨2​ℓ|,\displaystyle=\sum_{n,\ell=0}^{\infty}c_{2n}c_{2\ell}^{*}\mathrm{e}^{-2\mathrm{i}(n-\ell)\Omega_{\rm ho}t}\ket{2n}\bra{2\ell},(39)ρ^r​(t)\displaystyle\hat{\rho}_{r}(t)=∑n,ℓ=0∞c2​n​c2​ℓ∗​f​(2​(n−ℓ)​Ωho,t)​|2​n⟩​⟨2​ℓ|,\displaystyle=\sum_{n,\ell=0}^{\infty}c_{2n}c_{2\ell}^{*}f\left(2(n-\ell)\Omega_{\rm ho},t\right)\ket{2n}\bra{2\ell},(40)

wheref​(ω,t)f(\omega,t)is given in Eq. (12). Since only even levels are populated, the smallest nonzero Bohr frequency contributing to the dynamics isΔ=2​Ωho\Delta=2\Omega_{\rm ho}. Thus, forη≠1\eta\neq 1, Eq. (21) givesρ^r​(t)−ρ^rst=O​(t−θ)\hat{\rho}_{r}(t)-\hat{\rho}_{r}^{\rm st}=O(t^{-\theta}), withθ=4​Ωho2/(r2+4​Ωho2)\theta=4\Omega_{\rm ho}^{2}/(r^{2}+4\Omega_{\rm ho}^{2}), up to oscillations periodic inlog⁡t\log twith logarithmic angular frequency2​r​Ωho/(r2+4​Ωho2)2r\Omega_{\rm ho}/(r^{2}+4\Omega_{\rm ho}^{2}). For the special caseη=1\eta=1, Eqs. (39) and (40) reduce, respectively, toρ^0​(t)=|0⟩​⟨0|\hat{\rho}_{0}(t)=\ket{0}\bra{0}andρ^r​(t)=|0⟩​⟨0|\hat{\rho}_{r}(t)=\ket{0}\bra{0}at alltt.

At long times, all coherences between different energy levels vanish (see Eq. (23)) and the stationary density matrix isρ^rst=∑n=0∞|c2​n|2​|2​n⟩​⟨2​n|.\hat{\rho}_{r}^{\rm st}=\sum_{n=0}^{\infty}|c_{2n}|^{2}\ket{2n}\bra{2n}.(41)

As predicted by the general result in Eq. (26), this state is independent ofrrand coincides with the infinite-time average of the reset-free evolution. In the position representation,P0​(x,t)=⟨x|​ρ^0​(t)​|x⟩=∑n,ℓ=0∞c2​n​c2​ℓ∗​e−2​i​(n−ℓ)​Ωho​t​φ2​n​(x)​φ2​ℓ∗​(x),P_{0}(x,t)=\bra{x}\hat{\rho}_{0}(t)\ket{x}=\sum_{n,\ell=0}^{\infty}c_{2n}c_{2\ell}^{*}\mathrm{e}^{-2\mathrm{i}(n-\ell)\Omega_{\rm ho}t}\varphi_{2n}(x)\varphi_{2\ell}^{*}(x),(42)

whereP0​(x,t)P_{0}(x,t)is periodic with periodπ/Ωho\pi/\Omega_{\rm ho}. Averaging Eq. (42) over one period and usingΩhoπ​∫0π/Ωhodt​e−2​i​(n−ℓ)​Ωho​t=δn​ℓ\frac{\Omega_{\rm ho}}{\pi}\int_{0}^{\pi/\Omega_{\rm ho}}\mathrm{d}t\,\mathrm{e}^{-2\mathrm{i}(n-\ell)\Omega_{\rm ho}t}=\delta_{n\ell}yieldsPrst​(x)=∑n=0∞|c2​n|2​|φ2​n​(x)|2=Ωhoπ​∫0π/Ωhodt​P0​(x,t).P_{r}^{\rm st}(x)=\sum_{n=0}^{\infty}|c_{2n}|^{2}|\varphi_{2n}(x)|^{2}=\frac{\Omega_{\rm ho}}{\pi}\int_{0}^{\pi/\Omega_{\rm ho}}\mathrm{d}t\,P_{0}(x,t).(43)

For the initial condition in Eq. (36), we have[97]P0​(x,t)=2​απ​Dη​(t)​exp⁡[−2​α​x2Dη​(t)],Dη​(t)=cos2⁡(Ωho​t)+η2​sin2⁡(Ωho​t),P_{0}(x,t)=\sqrt{\frac{2\alpha}{\pi D_{\eta}(t)}}\exp\left[-\frac{2\alpha x^{2}}{D_{\eta}(t)}\right],\qquad D_{\eta}(t)=\cos^{2}(\Omega_{\rm ho}t)+\eta^{2}\sin^{2}(\Omega_{\rm ho}t),(44)

and thereforePrst​(x)=Ωhoπ​∫0π/Ωhodt​2​απ​Dη​(t)​exp⁡[−2​α​x2Dη​(t)].P_{r}^{\rm st}(x)=\frac{\Omega_{\rm ho}}{\pi}\int_{0}^{\pi/\Omega_{\rm ho}}\mathrm{d}t\,\sqrt{\frac{2\alpha}{\pi D_{\eta}(t)}}\exp\left[-\frac{2\alpha x^{2}}{D_{\eta}(t)}\right].(45)

## 4Gapless Quantum Systems

We now consider quantum systems with a continuous, gapless energy spectrum. We denote
the energy eigenstates by|p⟩\ket{p}, satisfyingH^​|p⟩=ε​(p)​|p⟩,⟨p|p′⟩=δ​(p−p′).\hat{H}\ket{p}=\varepsilon(p)\ket{p},\qquad\braket{p|p^{\prime}}=\delta(p-p^{\prime}).(46)

The matrix elements ofρ^r​(t)\hat{\rho}_{r}(t)in this basis areρr​(p,p′,t)=⟨p|​ρ^r​(t)​|p′⟩\rho_{r}(p,p^{\prime},t)=\bra{p}\hat{\rho}_{r}(t)\ket{p^{\prime}}, while the corresponding Bohr frequencies readωp​p′=ε​(p)−ε​(p′).\omega_{pp^{\prime}}=\varepsilon(p)-\varepsilon(p^{\prime}).We also define the group velocity asv​(p)=d​ε​(p)d​pv(p)=\frac{\mathrm{d}\varepsilon(p)}{\mathrm{d}p}.
As a representative class, we consider translationally invariant systems with the power-law dispersionεν​(p)=κν​|p|ν,κν>0,ν>1.\varepsilon_{\nu}(p)=\kappa_{\nu}|p|^{\nu},\qquad\kappa_{\nu}>0,\qquad\nu>1.(47)

The restrictionν>1\nu>1ensures that the dispersion is differentiable atp=0p=0and that the group velocity is a continuous function of momentum.

As in the gapped case, the different energy-basis matrix elements evolve
independently, and the Hamiltonian enters their dynamics only through the
corresponding Bohr frequency. Their exact time evolution is again given by Eq. (13), namelyρr​(p,p′,t)=ρ0​(p,p′,0)​f​(ωp​p′,t)\rho_{r}(p,p^{\prime},t)=\rho_{0}(p,p^{\prime},0)f\left(\omega_{pp^{\prime}},t\right),
wheref​(ω,t)f(\omega,t)is given in
Eq. (12). For every fixed pair(p,p′)(p,p^{\prime})withωp​p′≠0\omega_{pp^{\prime}}\neq 0, it follows directly from Eq. (18) that the corresponding matrix element vanishes algebraically at long times as|ρr​(p,p′,t)|∼t−ωp​p′2r2+ωp​p′2.\left|\rho_{r}(p,p^{\prime},t)\right|\sim t^{-\frac{\omega_{pp^{\prime}}^{2}}{r^{2}+\omega_{pp^{\prime}}^{2}}}.(48)

The crucial difference from the gapped case is that the zero-frequency sector is not separated from the nonzero Bohr frequencies by a finite gap. Instead, arbitrarily small nonzero frequencies are present, and the corresponding density-matrix elements decay increasingly slowly asω→0\omega\to 0[see Eq. (48)]. Consequently, the density matrix cannot be decomposed into a time-independent contribution plus a term that vanishes uniformly at long times, as in the gapped case. Although every fixed matrix element withω≠0\omega\neq 0eventually decays, matrix elements associated with frequencies increasingly close to zero continue to contribute to observables, thereby preventing convergence to a stationary state.

As shown inC, for a sufficiently
regular initial density matrix the long-time position distribution takes the
scaling formPr​(x,t)≈rlog⁡(r​t)​𝒱0​(r​xlog⁡(r​t)).P_{r}(x,t)\approx\frac{r}{\log(rt)}\mathcal{V}_{0}\left(\frac{rx}{\log(rt)}\right).(49)

where the function𝒱0​(v)\mathcal{V}_{0}(v)is given by𝒱0​(v)=∫−∞∞dp​ρ0​(p,p,0)​δ​(v−d​ε​(p)d​p).\mathcal{V}_{0}(v)=\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\delta\left(v-\frac{\mathrm{d}\varepsilon(p)}{\mathrm{d}p}\right).(50)

Equation (49) shows that there is a characteristic spatial scale that
grows in time aslog⁡(r​t)/r\log(rt)/r, independently of the specific dispersion relation and
of the initial state. This logarithmic growth is therefore a universal
consequence of the continuous spectrum and of the uniform memory protocol.
By contrast, the shape of the spreading distribution is nonuniversal: it
depends strongly on the details of the Hamiltonian through the group velocityv​(p)=d​ε​(p)d​pv(p)=\frac{\mathrm{d}\varepsilon(p)}{\mathrm{d}p}and retains a strong memory of the initial condition throughρ0​(p,p,0)\rho_{0}(p,p,0). This behavior differs qualitatively from that of an
unconfined classical Brownian particle under uniform memory resetting[91], whose
long-time position distribution is universally Gaussian, independently of
the initial condition, with a width growing aslog⁡t\sqrt{\log t}. In the
quantum case, instead, the width grows aslog⁡t\log t, while the asymptotic
distribution is generally non-Gaussian, system dependent, and strongly
sensitive to the initial condition.

For the power-law dispersion in
Eq. (47), the group velocity isvν​(p)=d​εν​(p)d​p=κν​ν​sgn⁡(p)​|p|ν−1.v_{\nu}(p)=\frac{d\varepsilon_{\nu}(p)}{dp}=\kappa_{\nu}\nu\,\operatorname{sgn}(p)|p|^{\nu-1}.Forν>1\nu>1, this relation is monotonic and can be inverted asp​(v)=sgn⁡(v)​(|v|κν​ν)1ν−1p(v)=\operatorname{sgn}(v)\left(\frac{|v|}{\kappa_{\nu}\nu}\right)^{\frac{1}{\nu-1}}(51)

with Jacobian|d​pd​v|=|v|2−νν−1(ν−1)​(κν​ν)1ν−1\left|\frac{\mathrm{d}p}{\mathrm{d}v}\right|=\frac{|v|^{\frac{2-\nu}{\nu-1}}}{(\nu-1)(\kappa_{\nu}\nu)^{\frac{1}{\nu-1}}}.
The initial velocity distribution defined in
Eq. (50) therefore becomes𝒱0​(v)=|v|2−νν−1(ν−1)​(κν​ν)1ν−1​ρ0​(p​(v),p​(v),0).\displaystyle\mathcal{V}_{0}(v)=\frac{|v|^{\frac{2-\nu}{\nu-1}}}{(\nu-1)(\kappa_{\nu}\nu)^{\frac{1}{\nu-1}}}\rho_{0}\!\big(p(v),p(v),0\big).(52)

Substituting this expression into
Eq. (49), we obtain the explicit long-time
position distributionPr​(x,t)≈rlog⁡(r​t)​|r​xlog⁡(r​t)|2−νν−1(ν−1)​(κν​ν)1ν−1​ρ0​(p​(r​xlog⁡(r​t)),p​(r​xlog⁡(r​t)),0),\displaystyle P_{r}(x,t)\approx\frac{r}{\log(rt)}\frac{\left|\frac{rx}{\log(rt)}\right|^{\frac{2-\nu}{\nu-1}}}{(\nu-1)(\kappa_{\nu}\nu)^{\frac{1}{\nu-1}}}\rho_{0}\left(p\left(\frac{rx}{\log(rt)}\right),p\left(\frac{rx}{\log(rt)}\right),0\right),(53)

wherep​(v)p(v)is given in Eq. (51) and we recallρ0​(p,p,0)=⟨p|​ρ^0​(0)​|p⟩\rho_{0}(p,p,0)=\bra{p}\hat{\rho}_{0}(0)\ket{p}is the momentum distribution at timet=0t=0.

## 4.1Quantum free particle

As a representative example of a gapless quantum system, we consider a quantum free
particle of massmmmoving on the infinite line. This corresponds to the quadratic dispersion relationε2​(p)=p22​m\varepsilon_{2}(p)=\frac{p^{2}}{2m},
obtained by settingν=2\nu=2andκ2=12​m\kappa_{2}=\frac{1}{2m}into Eq. (47).
The associated group velocity is thereforev2​(p)=d​ε2​(p)d​p=pm.v_{2}(p)=\frac{\mathrm{d}\varepsilon_{2}(p)}{\mathrm{d}p}=\frac{p}{m}.We again choose the normalized Gaussian initial state in Eq. (36), whose initial momentum distribution isρ0​(p,p,0)=12​π​α​exp⁡(−p22​α)\rho_{0}(p,p,0)=\frac{1}{\sqrt{2\pi\alpha}}\exp\left(-\frac{p^{2}}{2\alpha}\right)[97].
Usingν=2\nu=2andκ2=12​m\kappa_{2}=\frac{1}{2m}, the initial velocity distribution in Eq. (52) becomes Gaussian:𝒱0​(v)=m​ρ0​(m​v,m​v,0)=m2​π​α​exp⁡(−m2​v22​α).\mathcal{V}_{0}(v)=m\,\rho_{0}(mv,mv,0)=\frac{m}{\sqrt{2\pi\alpha}}\exp\left(-\frac{m^{2}v^{2}}{2\alpha}\right).(54)

Substituting this expression into
Eq. (49), we obtain the long-time position
probability densityPr​(x,t)≈m​r2​π​α​log⁡(r​t)​exp⁡[−m2​r2​x22​α​[log⁡(r​t)]2],t→∞.P_{r}(x,t)\approx\frac{mr}{\sqrt{2\pi\alpha}\,\log(rt)}\exp\left[-\frac{m^{2}r^{2}x^{2}}{2\alpha[\log(rt)]^{2}}\right],\qquad t\to\infty.(55)

The position distribution is therefore asymptotically Gaussian, with zero mean and variance⟨x^2​(t)⟩r≈αm2​r2​[log⁡(r​t)]2.\left\langle\hat{x}^{2}(t)\right\rangle_{r}\approx\frac{\alpha}{m^{2}r^{2}}[\log(rt)]^{2}.Consequently, its characteristic width grows as⟨x^2​(t)⟩r∼log⁡(r​t).\sqrt{\left\langle\hat{x}^{2}(t)\right\rangle_{r}}\sim\log(rt).

Thus, the particle does not approach a stationary position distribution but continues to spread logarithmically slowly. Uniform-memory resetting strongly suppresses the ballistic spreading of the reset-free particle, whose width grows linearly in time. As discussed above, thislog⁡t\log tgrowth is faster than thelog⁡t\sqrt{\log t}spreading found for the classical Brownian particle under uniform memory resetting[91]. Moreover, while the classical asymptotic distribution is universally Gaussian, the Gaussian form obtained here results specifically from the quadratic dispersion and the Gaussian initial momentum distribution.

## 5Conclusions and Outlook

In this work, we introduced a quantum stochastic resetting protocol with memory in which, at each resetting event, the system is returned to a state visited at an earlier time selected uniformly from its entire history. This construction provides a quantum counterpart of the classical preferential relocation model[84,91], while combining coherent evolution, stochastic resetting, and temporal nonlocality. The resulting dynamics is therefore both nonunitary and non-Markovian.

Working in the energy eigenbasis, we obtained an exact solution for any density-matrix element of a general time-independent Hamiltonian and showed that the details of such Hamiltonian enter the dynamics only through the corresponding Bohr frequencies. This naturally leads to a classification into gapped and gapless quantum systems.
Forgapped systems, the relevant nonzero Bohr frequencies are bounded away from zero. Consequently, coherences between states with different energies vanish algebraically while oscillating periodically as functions oflog⁡t\log t. The slowest relaxation is controlled by the smallest relevant Bohr frequencyΔ\Delta, with decay exponentθ=Δ2/(r2+Δ2)\theta=\Delta^{2}/(r^{2}+\Delta^{2}). The populations in the energy basis remain equal to their initial values, as do coherences within degenerate energy eigenspaces. The stationary state is therefore obtained by projecting the initial density matrix onto the eigenspaces of the Hamiltonian. For a nondegenerate spectrum, it is simply its diagonal part in the energy basis. Remarkably, this stationary state is independent of the resetting raterrand coincides with the infinite-time average of the reset-free unitary evolution. These results were illustrated concretely using a quantum two-level system and a quantum harmonic oscillator.
The dependence of the stationary state on the initial energy populations reveals a strong memory of the initial condition. This marks a crucial difference from confined classical systems under uniform memory resetting[94]. Although both classical and quantum systems relax algebraically, the classical stationary state is the equilibrium Gibbs–Boltzmann distribution and is independent of the initial condition, whereas the quantum stationary state has a very strong memory of the initial condition.

Forgapless systems, the continuous spectrum contains arbitrarily small nonzero Bohr frequencies. In this case, the system does not generally reach a stationary position distribution. For translationally invariant systems, the long-time distribution universally spreads on the extremely slow scalelog⁡(r​t)/r\log(rt)/r. The complete large-time scaling function is instead non-universal. It depends on the specific dispersion relation and on the initial group-velocity distribution. It therefore retains a strong memory of the initial condition.
For a free quantum particle with a quadratic dispersion relation and a Gaussian initial state, the long-time position distribution is Gaussian, with standard deviation growing extremely slowly aslog⁡t\log t. This differs from the classical unconfined Brownian particle, whose asymptotic distribution is Gaussian independently of the initial condition and with a width growing aslog⁡t\sqrt{\log t}[91].

The spectral distinction therefore determines the qualitative long-time behavior: a finite frequency gap leads to a stationary state approached algebraically, whereas an accumulation of frequencies near zero produces persistent logarithmic spreading. In both cases, however, the repeated sampling of an expanding history strongly suppresses the underlying quantum dynamics. This contrasts with conventional quantum resetting to a fixed state[58,59], which has a renewal structure and typically produces an exponentially fast approach to anrr-dependent nonequilibrium stationary state.

Several interesting extensions follow naturally from the present work. It would be interesting to investigate nonuniform memory kernels that favor either recent or remote portions of the history (such as those proposed in the classical setting in Ref.[91]). A particularly interesting direction is to replace the uniform kernel by a general normalized memory kernel,K​(τ,t)=ϕ​(τ)∫0tds​ϕ​(s)K(\tau,t)=\frac{\phi(\tau)}{\int_{0}^{t}\mathrm{d}s\,\phi(s)}with∫0tdτ​K​(τ,t)=1\int_{0}^{t}\mathrm{d}\tau\,K(\tau,t)=1in Eq. (5). The last term in Eq. (5) generalizes tor​∫0tdτ​K​(τ,t)​ρ^r​(τ)r\int_{0}^{t}\mathrm{d}\tau\,K(\tau,t)\hat{\rho}_{r}(\tau).
Depending on the choice ofϕ​(τ)\phi(\tau), the resetting protocol can preferentially sample either remote or recent portions of the history. In the classical diffusive problem, Ref.[91]showed that this temporal bias produces a remarkably broad range of long-time behaviors. It would be interesting to determine how this hierarchy is modified in the quantum setting, where the kernel affects not only populations but also coherences.

It will be interesting to study interacting many-body systems, where memory may affect correlations and entanglement. Further directions include time-dependent Hamiltonians, open quantum systems, and state- or observable-dependent memory kernels. Quantum resetting with memory thus provides a simple framework in which coherent evolution, stochastic control, and temporal nonlocality coexist, offering a route to generate ultraslow dynamics while preserving information about the initial quantum state.

## Acknowledgments

We acknowledge support from ANR Grant No. ANR-23-CE30-0020-01 EDIPS. M.K. acknowledges support from the Department of Atomic Energy, Government of India, under Project No. RTI4001. M. K. thanks the hospitality of Laboratoire de Physique Théorique et Modèles Statistiques (LPTMS), University Paris-Saclay and Collège de France, PSL Research University where a major part of the work took place.

## Appendix AEquivalence between the renewal equation and a the “Master equation”

This appendix relates the renewal description of quantum resetting in Ref.[58]to a “Master equation”[59], i.e., we derive the equivalence between Eq. (3) and Eq. (4) of the main text. We writeρ^0​(t)\hat{\rho}_{0}(t)for the density matrix evolvingwithoutresetting, andρ^r​(t)\hat{\rho}_{r}(t)for the density matrix averaged over the resetting process. The renewal equation is given in Eq. (3).
Using the change of variableτ↦t−τ\tau\mapsto t-\tauin Eq. (3) givesρ^r​(t)=e−r​t​ρ^0​(t)+r​∫0tdτ​e−r​(t−τ)​ρ^0​(t−τ).\hat{\rho}_{r}(t)=e^{-rt}\hat{\rho}_{0}(t)+r\int_{0}^{t}\mathrm{d}\tau\,e^{-r(t-\tau)}\hat{\rho}_{0}(t-\tau).(56)

The reset-free density matrix obeys the von Neumann equationd​ρ^0​(t)d​t=−i​[H^,ρ^0​(t)].\frac{\mathrm{d}\hat{\rho}_{0}(t)}{\mathrm{d}t}=-\mathrm{i}\left[\hat{H},\hat{\rho}_{0}(t)\right].(57)

We now differentiate Eq. (56). Applying the product rule and the Leibniz rule givesd​ρ^r​(t)d​t=−r​e−r​t​ρ^0​(t)+e−r​t​d​ρ^0​(t)d​t+r​ρ^0​(0)−r2​∫0tdτ​e−r​(t−τ)​ρ^0​(t−τ)+r​∫0tdτ​e−r​(t−τ)​d​ρ^0​(t−τ)d​t.\begin{split}\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}={}&-r\mathrm{e}^{-rt}\hat{\rho}_{0}(t)+\mathrm{e}^{-rt}\frac{\mathrm{d}\hat{\rho}_{0}(t)}{\mathrm{d}t}+r\hat{\rho}_{0}(0)\\
&-r^{2}\int_{0}^{t}\mathrm{d}\tau\,\mathrm{e}^{-r(t-\tau)}\hat{\rho}_{0}(t-\tau)+r\int_{0}^{t}\mathrm{d}\tau\,\mathrm{e}^{-r(t-\tau)}\frac{\mathrm{d}\hat{\rho}_{0}(t-\tau)}{\mathrm{d}t}.\end{split}(58)

The first and the fourth term in Eq. (58) combine to give−r​ρ^r​(t)-r\hat{\rho}_{r}(t)by Eq. (56). Therefored​ρ^r​(t)d​t=−r​ρ^r​(t)+e−r​t​d​ρ^0​(t)d​t+r​ρ^0​(0)+r​∫0tdτ​e−r​(t−τ)​d​ρ^0​(t−τ)d​t,\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-r\hat{\rho}_{r}(t)+e^{-rt}\frac{\mathrm{d}\hat{\rho}_{0}(t)}{\mathrm{d}t}+r\hat{\rho}_{0}(0)+r\int_{0}^{t}\mathrm{d}\tau\,e^{-r(t-\tau)}\frac{\mathrm{d}\hat{\rho}_{0}(t-\tau)}{\mathrm{d}t},(59)

where we recall thatρ^0​(0)\hat{\rho}_{0}(0)is the general initial density matrix to which the
system is returned at each resetting event.
Substituting Eq. (57) into Eq. (59), we obtaind​ρ^r​(t)d​t=−r​ρ^r​(t)+e−r​t​(−i​[H^,ρ^0​(t)])+r​ρ^0​(0)+r​∫0tdτ​e−r​(t−τ)​(−i​[H^,ρ^0​(t−τ)]).\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-r\hat{\rho}_{r}(t)+e^{-rt}\Big(-\mathrm{i}\left[\hat{H},\hat{\rho}_{0}(t)\right]\Big)+r\hat{\rho}_{0}(0)+r\int_{0}^{t}\mathrm{d}\tau\,e^{-r(t-\tau)}\Big(-\mathrm{i}\left[\hat{H},\hat{\rho}_{0}(t-\tau)\right]\Big).(60)

By linearity of the commutator, the Hamiltonian terms in Eq. (60) can be collected asd​ρ^r​(t)d​t=−r​ρ^r​(t)+r​ρ^0​(0)−i​[H^,e−r​t​ρ^0​(t)+r​∫0tdτ​e−r​(t−τ)​ρ^0​(t−τ)].\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-r\hat{\rho}_{r}(t)+r\hat{\rho}_{0}(0)-\mathrm{i}\left[\hat{H},e^{-rt}\hat{\rho}_{0}(t)+r\int_{0}^{t}\mathrm{d}\tau\,e^{-r(t-\tau)}\hat{\rho}_{0}(t-\tau)\right].(61)

The expression inside the right argument of the commutator is exactlyρ^r​(t)\hat{\rho}_{r}(t)by Eq. (56). Hence, we finally getd​ρ^r​(t)d​t=−i​[H^,ρ^r​(t)]−r​ρ^r​(t)+r​ρ^0​(0).\frac{\mathrm{d}\hat{\rho}_{r}(t)}{\mathrm{d}t}=-\mathrm{i}\left[\hat{H},\hat{\rho}_{r}(t)\right]-r\hat{\rho}_{r}(t)+r\hat{\rho}_{0}(0).(62)

## Appendix BEvent-driven Monte Carlo simulation of the uniform memory protocol

In this appendix, we describe the event-driven Monte Carlo procedure used to verify the analytical result in Eq. (32) for the quantum two-level system under Poissonian resetting with uniform memory. We denote the density matrix along thekk-th realization of the dynamics byρ^r(k)​(t)\hat{\rho}_{r}^{(k)}(t). Each realization is specified by a sequence of resetting times{T1,T2,…}\{T_{1},T_{2},\ldots\}and selected past times{τ1,τ2,…}\{\tau_{1},\tau_{2},\ldots\}, whereτj\tau_{j}is sampled uniformly in[0,Tj][0,T_{j}]at thejj-th reset. The density matrix considered in the analytical treatment is the ensemble averageρ^r​(t)=𝔼​[ρ^r(k)​(t)]\hat{\rho}_{r}(t)=\mathbb{E}\left[\hat{\rho}_{r}^{(k)}(t)\right],
where the expectation is taken over both the Poissonian resetting times and the past times selected at each event.

For the two-level system in Sec.3.1, the Hamiltonian isH^=Ω​σ^x\hat{H}=\Omega\hat{\sigma}_{x}. In the absence of resetting, the density matrix evolves along the unitary orbit according to Eq. (28), namelyρ^0​(s)=e−i​H^​s​ρ^0​(0)​ei​H^​s=(ρ↑↑​(0)ρ↑↓​(0)​e−2​i​Ω​sρ↓↑​(0)​e2​i​Ω​sρ↓↓​(0)),\hat{\rho}_{0}(s)=\mathrm{e}^{-\mathrm{i}\hat{H}s}\hat{\rho}_{0}(0)\mathrm{e}^{\mathrm{i}\hat{H}s}=\begin{pmatrix}\rho_{\uparrow\uparrow}(0)&\rho_{\uparrow\downarrow}(0)\mathrm{e}^{-2\mathrm{i}\Omega s}\\
\rho_{\downarrow\uparrow}(0)\mathrm{e}^{2\mathrm{i}\Omega s}&\rho_{\downarrow\downarrow}(0)\end{pmatrix},(63)

wheressis the time elapsed along the reset-free evolution.

We now consider a single stochastic realization of the resetting process with memory. In this case, the state no longer follows the reset-free evolution in Eq. (63) as a function of the physical timett. However, by construction, each reset returns the system to a state that was previously occupied and that therefore belongs to the same unitary orbit generated from the initial condition. We may thus introduce an effective timeq(k)​(t)q^{(k)}(t)such that the state at timettalong thekk-th realization can always be written asρ^r(k)​(t)=ρ^0​(q(k)​(t)).\hat{\rho}_{r}^{(k)}(t)=\hat{\rho}_{0}\left(q^{(k)}(t)\right).(64)

The quantityq(k)​(t)q^{(k)}(t)therefore identifies the point of the reset-free unitary orbit occupied by the system at physical timettand should not be interpreted as an additional physical time. In the following, we consider a fixed realization and suppress the indexkk.

LetT1<T2<⋯T_{1}<T_{2}<\cdotsbe the resetting times, withT0=0T_{0}=0, and defineq¯j=q​(Tj+)\bar{q}_{j}=q(T_{j}^{+})as the effective time immediately after thejj-th reset, withq¯0=0\bar{q}_{0}=0. Between two consecutive resetting events, the effective time increases linearly. In particular, if the system is at effective timeq¯j\bar{q}_{j}immediately after the reset atTjT_{j}, thenq​(t)=q¯j+t−Tjq(t)=\bar{q}_{j}+t-T_{j}forTj≤t<Tj+1T_{j}\leq t<T_{j+1}. This follows directly from the property of the unitary evolution, since fors=t−Tjs=t-T_{j}one hasρ^r​(Tj+s)=e−i​H^​s​ρ^0​(q¯j)​ei​H^​s=ρ^0​(q¯j+s).\hat{\rho}_{r}(T_{j}+s)=\mathrm{e}^{-\mathrm{i}\hat{H}s}\hat{\rho}_{0}(\bar{q}_{j})\mathrm{e}^{\mathrm{i}\hat{H}s}=\hat{\rho}_{0}(\bar{q}_{j}+s).At thejj-th resetting event, a past physical timeτj\tau_{j}is sampled uniformly in[0,Tj][0,T_{j}]. To determine the state occupied at that time, we identify the interval containingτj\tau_{j}. Letℓ\ellsatisfyTℓ≤τj<Tℓ+1T_{\ell}\leq\tau_{j}<T_{\ell+1}, with0≤ℓ≤j−10\leq\ell\leq j-1. Since the system started from the effective timeq¯ℓ\bar{q}_{\ell}immediately after the reset atTℓT_{\ell}and subsequently evolved unitarily for a durationτj−Tℓ\tau_{j}-T_{\ell}, the effective time immediately after thejj-th reset isq¯j=q​(Tj+)=q​(τj)=q¯ℓ+τj−Tℓ.\bar{q}_{j}=q(T_{j}^{+})=q(\tau_{j})=\bar{q}_{\ell}+\tau_{j}-T_{\ell}.(65)

For the first reset,ℓ=0\ell=0, and Eq. (65) simply givesq¯1=τ1\bar{q}_{1}=\tau_{1}. For later resets, one generally hasq​(τj)≠τjq(\tau_{j})\neq\tau_{j}, because the state occupied at the selected physical time may already contain the effects of previous resetting events. All resets precedingTℓT_{\ell}are encoded inq¯ℓ\bar{q}_{\ell}. Therefore, the complete memory of a realization is contained in the stored pairs{Tj,q¯j}\{T_{j},\bar{q}_{j}\}for alljj.

The resetting times are generated by a Poisson process of raterr. Hence, the waiting timesΔ​Tj=Tj−Tj−1\Delta T_{j}=T_{j}-T_{j-1}are independent random variables distributed according top​(Δ​T)=r​e−r​Δ​Tp(\Delta T)=r\mathrm{e}^{-r\Delta T}. For each realization, the event-driven algorithm proceeds as follows:
- 1.

SetT0=0T_{0}=0andq¯0=0\bar{q}_{0}=0.
- 2.

Draw a waiting timeΔ​Tj\Delta T_{j}fromp​(Δ​T)=r​e−r​Δ​Tp(\Delta T)=r\mathrm{e}^{-r\Delta T}and setTj=Tj−1+Δ​TjT_{j}=T_{j-1}+\Delta T_{j}.
- 3.

Evolve the system unitarily fromTj−1+T_{j-1}^{+}toTj−T_{j}^{-}. Since the effective time immediately after the previous reset isq¯j−1\bar{q}_{j-1}, one hasq​(Tj−)=q¯j−1+Δ​Tj,q(T_{j}^{-})=\bar{q}_{j-1}+\Delta T_{j},and thereforeρ^r​(Tj−)=e−i​H^​Δ​Tj​ρ^r​(Tj−1+)​ei​H^​Δ​Tj=ρ^0​(q¯j−1+Δ​Tj)\hat{\rho}_{r}(T_{j}^{-})=\mathrm{e}^{-\mathrm{i}\hat{H}\Delta T_{j}}\hat{\rho}_{r}(T_{j-1}^{+})\mathrm{e}^{\mathrm{i}\hat{H}\Delta T_{j}}=\hat{\rho}_{0}\left(\bar{q}_{j-1}+\Delta T_{j}\right), withρ^0​(s)\hat{\rho}_{0}(s)given in Eq. (63)
- 4.

Draw a past timeτj\tau_{j}uniformly in[0,Tj][0,T_{j}]and find the indexℓ\ellsuch thatTℓ≤τj<Tℓ+1T_{\ell}\leq\tau_{j}<T_{\ell+1}.
- 5.

Update the effective time according toq¯j=q¯ℓ+τj−Tℓ,\bar{q}_{j}=\bar{q}_{\ell}+\tau_{j}-T_{\ell},and reset the system toρ^r​(Tj+)=ρ^0​(q¯j)\hat{\rho}_{r}(T_{j}^{+})=\hat{\rho}_{0}(\bar{q}_{j}).
- 6.

Store the pair(Tj,q¯j)(T_{j},\bar{q}_{j})and repeat the procedure until the final observation time is reached.

Once the reset history has been generated, the trajectory is evaluated at a prescribed set of observation timestnt_{n}. For eachtnt_{n}, the algorithm finds the most recent reset timeTjT_{j}such thatTj≤tn<Tj+1T_{j}\leq t_{n}<T_{j+1}and reconstructs the effective time asq​(tn)=q¯j+tn−Tjq(t_{n})=\bar{q}_{j}+t_{n}-T_{j}. The density matrix is then obtained directly from the reset-free solution asρ^r(k)​(tn)=ρ^0​(q​(tn))\hat{\rho}_{r}^{(k)}(t_{n})=\hat{\rho}_{0}(q(t_{n})). Finally, the observable of interest is evaluated for each realization and averaged over the ensemble. The resulting numerical averages are shown as dots in Fig.1.

## Appendix CLong-time position distribution for a generic dispersion relation

In this Appendix, we derive the long-time position distribution of a
translationally invariant quantum particle with a generic dispersion
relationε​(p)\varepsilon(p)and an arbitrary initial stateρ^0​(0)\hat{\rho}_{0}(0). We consider a Hamiltonian of the
form introduced in Eq. (46), whose momentum
eigenstates satisfyH^​|p⟩=ε​(p)​|p⟩\hat{H}\ket{p}=\varepsilon(p)\ket{p}and⟨p|p′⟩=δ​(p−p′)\braket{p|p^{\prime}}=\delta(p-p^{\prime}). We assume thatε​(p)\varepsilon(p)is
differentiable in the region of momentum space explored by the initial
state.
We denote the momentum-space matrix elements of the reset-averaged density
matrix byρr​(p,p′,t)=⟨p|​ρ^r​(t)​|p′⟩\rho_{r}(p,p^{\prime},t)=\bra{p}\hat{\rho}_{r}(t)\ket{p^{\prime}}and those of the
initial density matrix byρ0​(p,p′,0)=⟨p|​ρ^0​(0)​|p′⟩\rho_{0}(p,p^{\prime},0)=\bra{p}\hat{\rho}_{0}(0)\ket{p^{\prime}}. Using the general
factorization in Eq. (8), their time
evolution isρr​(p,p′,t)=ρ0​(p,p′,0)​f​(ε​(p)−ε​(p′),t),\rho_{r}(p,p^{\prime},t)=\rho_{0}(p,p^{\prime},0)f\left(\varepsilon(p)-\varepsilon(p^{\prime}),t\right),(66)

where the corresponding Bohr frequency isωp​p′=ε​(p)−ε​(p′)\omega_{pp^{\prime}}=\varepsilon(p)-\varepsilon(p^{\prime})andf​(ω,t)f(\omega,t)is given in
Eq. (12).

We first express the position probability densityPr​(x,t)=⟨x|​ρ^r​(t)​|x⟩P_{r}(x,t)=\bra{x}\hat{\rho}_{r}(t)\ket{x}in terms of the momentum-space density
matrix. Using⟨x|p⟩=(2​π)−1/2​ei​p​x\braket{x|p}=(2\pi)^{-1/2}\mathrm{e}^{\mathrm{i}px}, we
obtainPr​(x,t)=12​π​∫−∞∞dp​∫−∞∞dp′​ei​(p−p′)​x​ρr​(p,p′,t).P_{r}(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{d}p\int_{-\infty}^{\infty}\mathrm{d}p^{\prime}\,\mathrm{e}^{\mathrm{i}(p-p^{\prime})x}\rho_{r}(p,p^{\prime},t).(67)

We now introduce the Fourier transformP~r​(q,t)=∫−∞∞dx​e−i​q​x​Pr​(x,t)\widetilde{P}_{r}(q,t)=\int_{-\infty}^{\infty}\mathrm{d}x\,\mathrm{e}^{-\mathrm{i}qx}P_{r}(x,t), with inverse transformPr​(x,t)=12​π​∫−∞∞dq​ei​q​x​P~r​(q,t)P_{r}(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{d}q\,\mathrm{e}^{\mathrm{i}qx}\widetilde{P}_{r}(q,t). Taking the Fourier transform
of Eq. (67) and using the identityδ​(k)=12​π​∫−∞∞dx​ei​k​x\delta(k)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{d}x\,\mathrm{e}^{\mathrm{i}kx}, we findP~r​(q,t)=∫−∞∞dp​∫−∞∞dp′​ρr​(p,p′,t)​δ​(p−p′−q).\widetilde{P}_{r}(q,t)=\int_{-\infty}^{\infty}\mathrm{d}p\int_{-\infty}^{\infty}\mathrm{d}p^{\prime}\,\rho_{r}(p,p^{\prime},t)\delta(p-p^{\prime}-q).(68)

To evaluate the delta function, we introduce the central and relative
momentaP=(p+p′)/2P=(p+p^{\prime})/2andQ=p−p′Q=p-p^{\prime}. The inverse relations arep=P+Q/2p=P+Q/2andp′=P−Q/2p^{\prime}=P-Q/2. Performing the change of variables(p,p′)→(P,Q)(p,p^{\prime})\to(P,Q), whose Jacobian has absolute value one,
Eq. (68) becomesP~r​(q,t)=∫−∞∞dP​∫−∞∞dQ​ρr​(P+Q2,P−Q2,t)​δ​(Q−q).\displaystyle\widetilde{P}_{r}(q,t)=\int_{-\infty}^{\infty}\mathrm{d}P\int_{-\infty}^{\infty}\mathrm{d}Q\,\rho_{r}\left(P+\frac{Q}{2},P-\frac{Q}{2},t\right)\delta(Q-q).(69)

Performing the integral overQQ, renaming the remaining integration
variablePPaspp, and using
Eq. (66), we obtainP~r​(q,t)=∫−∞∞dp​ρ0​(p+q2,p−q2,0)​f​(ε​(p+q2)−ε​(p−q2),t).\widetilde{P}_{r}(q,t)=\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}\left(p+\frac{q}{2},p-\frac{q}{2},0\right)f\left(\varepsilon\left(p+\frac{q}{2}\right)-\varepsilon\left(p-\frac{q}{2}\right),t\right).(70)

Equation (70) is exact at all times. We now
analyze its long-time behavior. Since the large-scale behavior of the
position distribution is controlled by the small-qqbehavior of its
Fourier transform, we expand the energy difference appearing in the first
argument offffor smallqq. This givesε​(p+q2)−ε​(p−q2)≈q​v​(p),v​(p)=d​ε​(p)d​p.\varepsilon\left(p+\frac{q}{2}\right)-\varepsilon\left(p-\frac{q}{2}\right)\approx qv(p),\qquad v(p)=\frac{\mathrm{d}\varepsilon(p)}{\mathrm{d}p}.(71)

Herev​(p)v(p)is the group velocity associated with momentumpp.

We next determine the large-time behavior off​(ω,t)f(\omega,t). From
Eq. (14), the leading asymptotic form of the
Kummer function isf​(ω,t)≈[(r+i​ω)​t]−χ​(ω)Γ​(1−χ​(ω))=exp⁡{−χ​(ω)​log⁡[(r+i​ω)​t]−log⁡Γ​(1−χ​(ω))},f(\omega,t)\approx\frac{\left[\left(r+\mathrm{i}\omega\right)t\right]^{-\chi(\omega)}}{\Gamma\left(1-\chi(\omega)\right)}=\exp\left\{-\chi(\omega)\log\left[\left(r+\mathrm{i}\omega\right)t\right]-\log\Gamma\left(1-\chi(\omega)\right)\right\},(72)

whereχ​(ω)=i​ωr+i​ω\chi(\omega)=\frac{\mathrm{i}\omega}{r+\mathrm{i}\omega}. At long
times, the dominant contribution comes from increasingly small frequencies.
We therefore consider the joint limit of largettand smallω\omegawhile
keepingω​log⁡(r​t)\omega\log(rt)fixed. Sinceχ​(ω)≈i​ω/r\chi(\omega)\approx\mathrm{i}\omega/r,log⁡[(r+i​ω)​t]≈log⁡(r​t)\log[(r+\mathrm{i}\omega)t]\approx\log(rt), andΓ​(1−χ​(ω))≈1\Gamma(1-\chi(\omega))\approx 1in this limit, the leading contribution isf​(ω,t)≈exp⁡[−i​ωr​log⁡(r​t)]=e−i​ω​teff​(t),teff​(t)=log⁡(r​t)r.f(\omega,t)\approx\exp\left[-\frac{\mathrm{i}\omega}{r}\log(rt)\right]=\mathrm{e}^{-\mathrm{i}\omega t_{\mathrm{eff}}(t)},\qquad t_{\mathrm{eff}}(t)=\frac{\log(rt)}{r}.(73)

Combining Eqs. (71) and
(73), we findf​(ε​(p+q2)−ε​(p−q2),t)≈e−i​q​teff​(t)​v​(p).f\left(\varepsilon\left(p+\frac{q}{2}\right)-\varepsilon\left(p-\frac{q}{2}\right),t\right)\approx\mathrm{e}^{-\mathrm{i}qt_{\mathrm{eff}}(t)v(p)}.(74)

Moreover, since the relevant values ofqqvanish at long times, we may useρ0​(p+q2,p−q2,0)→ρ0​(p,p,0)\rho_{0}\left(p+\frac{q}{2},p-\frac{q}{2},0\right)\to\rho_{0}(p,p,0)asq→0q\to 0. Inserting Eq. (74) into
Eq. (70), we then obtainP~r​(q,t)≈∫−∞∞dp​ρ0​(p,p,0)​e−i​q​teff​(t)​v​(p).\widetilde{P}_{r}(q,t)\approx\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\mathrm{e}^{-\mathrm{i}qt_{\mathrm{eff}}(t)v(p)}.(75)

We now invert the Fourier transform in
Eq. (75). This givesPr​(x,t)\displaystyle P_{r}(x,t)≈12​π​∫−∞∞dq​ei​q​x​∫−∞∞dp​ρ0​(p,p,0)​e−i​q​teff​(t)​v​(p)\displaystyle\approx\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{d}q\,\mathrm{e}^{\mathrm{i}qx}\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\mathrm{e}^{-\mathrm{i}qt_{\mathrm{eff}}(t)v(p)}=∫−∞∞dp​ρ0​(p,p,0)​12​π​∫−∞∞dq​ei​q​[x−teff​(t)​v​(p)]\displaystyle=\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{d}q\,\mathrm{e}^{\mathrm{i}q[x-t_{\mathrm{eff}}(t)v(p)]}=∫−∞∞dp​ρ0​(p,p,0)​δ​(x−teff​(t)​v​(p)).\displaystyle=\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\delta\left(x-t_{\mathrm{eff}}(t)v(p)\right).(76)

Using the identityδ​(x−teff​v​(p))=1teff​δ​(xteff−v​(p))\delta\left(x-t_{\mathrm{eff}}v(p)\right)=\frac{1}{t_{\mathrm{eff}}}\delta\left(\frac{x}{t_{\mathrm{eff}}}-v(p)\right),
Eq. (76) becomesPr​(x,t)≈1teff​(t)​∫−∞∞dp​ρ0​(p,p,0)​δ​(xteff​(t)−v​(p)).P_{r}(x,t)\approx\frac{1}{t_{\mathrm{eff}}(t)}\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\delta\left(\frac{x}{t_{\mathrm{eff}}(t)}-v(p)\right).(77)

We now define the group-velocity distribution induced by the diagonal
momentum distribution of the initial stateρ0​(p,p,0)\rho_{0}(p,p,0)as𝒱0​(v)=∫−∞∞dp​ρ0​(p,p,0)​δ​(v−ε′​(p)),\mathcal{V}_{0}(v)=\int_{-\infty}^{\infty}\mathrm{d}p\,\rho_{0}(p,p,0)\delta\left(v-\varepsilon^{\prime}(p)\right)\,,(78)

whereε′​(p)=d​ε​(p)d​p\varepsilon^{\prime}(p)=\frac{d\varepsilon(p)}{dp}. Using Eq. (78), we finally
obtainPr​(x,t)≈1teff​(t)​𝒱0​(xteff​(t)).P_{r}(x,t)\approx\frac{1}{t_{\mathrm{eff}}(t)}\mathcal{V}_{0}\left(\frac{x}{t_{\mathrm{eff}}(t)}\right).(79)

Sinceteff​(t)=log⁡(r​t)/rt_{\mathrm{eff}}(t)=\log(rt)/r, this result can equivalently be
written asPr​(x,t)≈rlog⁡(r​t)​𝒱0​(r​xlog⁡(r​t)).P_{r}(x,t)\approx\frac{r}{\log(rt)}\mathcal{V}_{0}\left(\frac{rx}{\log(rt)}\right).(80)

Thus, the characteristic spatial scale is completely universal and it grows logarithmically aslog⁡(r​t)/r\log(rt)/r, while the shape of the asymptotic distribution is non-universal and given
by the initial group-velocity distribution in Eq. (78).

## References
- [1]M. R. Evans, S. N. Majumdar,Diffusion with Stochastic Resetting,
Phys. Rev. Lett.106, 160601 (2011).
- [2]M. R. Evans, S. N. Majumdar,Diffusion with optimal resetting,
J. Phys. A: Math. Theor.44, 435001 (2011).
- [3]M. R. Evans, S. N. Majumdar, G. Schehr,Stochastic resetting and applications,
J. Phys. A: Math. Theor.53, 193001 (2020).
- [4]S. Gupta, A. M. Jayannavar,Stochastic resetting: A (very) brief review,
Front. Phys.10, 789097 (2022).
- [5]A. Kundu, S. Reuveni,Preface: stochastic resetting—theory and applications,
J. Phys. A: Math. Theor.57, 060301 (2024).
- [6]T. D. Keidar, S. Meir, N. Sherf, R. Goerlich, S. Reuveni, Y. Roichman, and B. Hirshberg,Stochastic Resetting: A Non-Equilibrium Framework for Prediction, Inference and Design,
arXiv:2607.16474 (2026).
- [7]S. Reuveni,Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal,
Phys. Rev. Lett.116, 170601 (2016).
- [8]A. Nagar and S. Gupta,Diffusion with stochastic resetting at power-law times,
Phys. Rev. E93, 060102(R) (2016).
- [9]A. Pal, S. Reuveni,First Passage under Restart,
Phys. Rev. Lett.118, 030603 (2017).
- [10]A. Chechkin, I. M. Sokolov,Random Search with Resetting: A Unified Renewal Approach,
Phys. Rev. Lett.121, 050601 (2018).
- [11]B. De Bruyne, S. N. Majumdar, and G. Schehr,Optimal Resetting Brownian Bridges via Enhanced Fluctuations,
Phys. Rev. Lett.128, 200603 (2022).
- [12]A. Pal, A. Kundu, M. R. Evans,Diffusion under time-dependent resetting,
J. Phys. A: Math. Theor.49, 225001 (2016).
- [13]R. G. Pinsky,Diffusive Search with spatially dependent Resetting,
arXiv:1805.00320 (2018).
- [14]G. García-Valladares, C. A. Plata, A. Prados and A. Manacorda,Optimal resetting strategies for search processes in heterogeneous environments,
New J. Phys.25, 113031 (2023).
- [15]R. Verma, B. Banerjee, S. Gupta, S. K. NandiResetting dynamics in a system with quenched disorder,
arXiv:2604.02950 (2026).
- [16]J. Whitehouse, M. R. Evans, and S. N. Majumdar,Effect of partial absorption on diffusion with resetting,
Phys. Rev. E87, 022118 (2013).
- [17]R. D. Schumm, P. C. Bressloff,Search processes with stochastic resetting and partially absorbing targets,
J. Phys. A: Math. Theor.54, 404004 (2021).
- [18]B. De Bruyne, J. Randon-Furling, and S. Redner,Optimization in first-passage resetting,
Phys. Rev. Lett.125, 050602 (2020).
- [19]A. Biswas, S. N. Majumdar, A. Pal,Target Search Optimization by Threshold Resetting,
Phys. Rev. Lett.135, 227101 (2025).
- [20]U. Bhat, C. De Bacco and S. Redner,Stochastic search with Poisson and deterministic resetting,
J. Stat. Mech. (2016) 083401.
- [21]M. Biroli, S. N. Majumdar, G. Schehr,Critical number of walkers for diffusive search processes with resetting,
Phys. Rev. E107, 064141 (2023).
- [22]L. N. Christophorov,Peculiarities of random walks with resetting in a one-dimensional chain,
J. Phys. A: Math. Theor. 54 (2021) 015001.
- [23]A. Barbini, L. Giuggioli,Lattice random walk dynamics
with stochastic resetting in heterogeneous space,
J. Phys. A: Math. Theor. 57, 425001 (2024).
- [24]A. K. Hartmann, S. N. Majumdar,Diffusion with stochastic resetting on a lattice,
Phys. Rev. E112, 034102 (2025).
- [25]B. De Bruyne and F. Mori,Resetting in stochastic optimal control,
Phys. Rev. Research5, 013122.
- [26]F. Mori, L. Mahadevan,Optimal switching strategies for navigation in stochastic settings,
J. R. Soc. Interface22, 20240677 (2025).
- [27]G. Del Vecchio Del Vecchio, M. Kulkarni, S. N. Majumdar, S. Sabhapandit,Proxitaxis: An adaptive search strategy based on proximity and stochastic resetting,
Phys. Rev. E113, L042101 (2026).
- [28]A. Pal, S. Kostinski, and S. Reuveni,The inspection paradox in stochastic resetting,
J. Phys. A: Math. Theor.55, 021001 (2022).
- [29]S. Gupta, S. N. Majumdar, and G. Schehr,Fluctuating Interfaces Subject to Stochastic Resetting,
Phys. Rev. Lett.112, 220601 (2014).
- [30]U. Basu, A. Kundu, and A. Pal,Symmetric exclusion process under stochastic resetting,
Phys. Rev. E100, 032136 (2019).
- [31]M. Magoni, S. N. Majumdar, and G. Schehr,Ising model with stochastic resetting,
Phys. Rev. Res.2, 033182 (2020).
- [32]Y. Chen and W. Zhong,Crossover from anomalous to normal diffusion: Ising model with stochastic resetting,
Phys. Rev. Res.6, 033189 (2024).
- [33]A. Acharya, R. Majumder, and S. Gupta,Manipulating phases in many-body interacting systems with subsystem resetting,
Phys. Rev. Lett.135, 127103 (2025).
- [34]Anagha V. K. and A. Nagar,Stochastic resetting in the infinite range Ising model,
J. Phys. A: Math. Theor.59, 215001 (2026).
- [35]M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr,Extreme statistics and spacing distribution in a Brownian gas correlated by resetting,
Phys. Rev. Lett.130, 207101 (2023).
- [36]G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr,Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols,
Phys. Rev. E113, 014120 (2026).
- [37]M. Biroli, S. N. Majumdar, G. Schehr,First-passage resetting gas,
EPL153, 31002 (2026).
- [38]G. de Mauro, S. N. Majumdar, G. Schehr,Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations,
arXiv:2606.31634 (2026).
- [39]D. Boyer, S. N. Majumdar,Emerging correlations between diffusing particles evolving via simultaneous resetting with memory,
J. Phys. A: Math. Theor.59, 125001 (2026).
- [40]M. Biroli, S. N. Majumdar, G. Schehr,Resetting Dyson Brownian motion,
Phys. Rev. E112, 014101 (2025).
- [41]O. Vilk, M. Assaf, and B. Meerson,Fluctuations and first-passage properties of systems of Brownian particles with reset,
Phys. Rev. E106, 024117 (2022).
- [42]B. Meerson and O. Vilk,Age-structured hydrodynamics of ensembles of anomalously diffusing particles with renewal resetting,
Phys. Rev. Res.8, 023103 (2026).
- [43]O. Vilk,Macroscopic localization and collective memory in Poisson renewal resetting,
Phys. Rev. Res.8, 023305 (2026).
- [44]M. Biroli, M. Kulkarni, S. N. Majumdar, and G. Schehr,Dynamically emergent correlations between particles in a switching harmonic trap,
Phys. Rev. E109, L032106 (2024).
- [45]S. Sabhapandit, S. N. Majumdar,Noninteracting particles in a harmonic trap with a stochastically driven center,
J. Phys. A: Math. Theor.57, 335003 (2024).
- [46]N. Mesquita, S. N. Majumdar, S. Sabhapandit,Dynamically emergent correlations in a Brownian gas with diffusing diffusivity,
J. Stat. Mech.2025, 103207 (2025).
- [47]M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr,Exact extreme, order, and sum statistics in a class of strongly correlated systems,
Phys. Rev. E109, 014101 (2024).
- [48]T. Galla,A diffusion approximation for systems with frequent weak resetting,
arXiv:2602.21635 (2026).
- [49]K. S. Olsen,Information-fluctuation inequalities for collective response,
arXiv:2603.01852 (2026).
- [50]G. de Mauro, S. N. Majumdar, and G. Schehr,Tuning the strength of emergent correlations in a Brownian gas via batch resetting,
arXiv:2601.20077 (2026).
- [51]B. Besga, A. Bovon, A. Petrosyan, S. N. Majumdar, and S. Ciliberto,Optimal mean first-passage time for a Brownian searcher subjected to resetting: Experimental and theoretical results,
Phys. Rev. Res.2, 032029(R) (2020).
- [52]F. Faisant, B. Besga, A. Petrosyan, S. Ciliberto, and S. N. Majumdar,Optimal mean first-passage time of a Brownian searcher with resetting in one and two dimensions: experiments, theory and numerical tests,
J. Stat. Mech.2021, 113203 (2021).
- [53]O. Tal-Friedman, A. Pal, A. Sekhon, S. Reuveni, and Y. Roichman,Experimental realization of diffusion with stochastic resetting,
J. Phys. Chem. Lett.11, 7350–7355 (2020).
- [54]F. Ginot and C. Bechinger,Experimental investigation of stochastic resetting in a non-Markovian environment,
New J. Phys.28, 015001 (2026).
- [55]R. Vatash and Y. Roichman,Many-body colloidal dynamics under stochastic resetting: Competing effects of particle interactions on the steady-state distribution,
Phys. Rev. Res.7, L032020 (2025).
- [56]M. Biroli, S. Ciliberto, M. Kulkarni,
S. N. Majumdar, A. Petrosyan, and G. Schehr,Experimental evidence for strong emergent correlations between particles in a switching trap,
Phys. Rev. Lett.137, 037102 (2026).
- [57]S. N. Majumdar and G. Schehr,Dynamically Emergent Correlations,
EPL155, 11001 (2026).
- [58]B. Mukherjee, K. Sengupta, S. N. Majumdar,Quantum dynamics with stochastic reset,
Phys. Rev. B98, 104309 (2018).
- [59]D. C. Rose, H. Touchette, I. Lesanovsky, J. P. Garrahan,Spectral properties of simple classical and quantum reset processes,
Phys. Rev. E98, 022129 (2018).
- [60]G. Perfetto, F. Carollo, M. Magoni, I. Lesanovsky,Designing nonequilibrium states of quantum matter through stochastic resetting,
Phys. Rev. B104, L180302 (2021).
- [61]M. Navascués,Resetting uncontrolled quantum systems,
Phys. Rev. X8, 031008 (2018).
- [62]S. Wald and L. Böttcher,From classical to quantum walks with stochastic resetting on networks,
Phys. Rev. E103, 012122 (2021).
- [63]D. Das, S. Dattagupta, and S. Gupta,Quantum unitary evolution interspersed with repeated non-unitary interactions at random times: The method of stochastic Liouville equation, and two examples of interactions in the context of a tight-binding chain,
J. Stat. Mech.2022, 053101 (2022).
- [64]A. Acharya and S. Gupta,Tight-binding model subject to conditional resets at random times,
Phys. Rev. E108, 064125 (2023).
- [65]F. J. Sevilla and A. Valdés-Hernández,Dynamics of closed quantum systems under stochastic resetting,
J. Phys. A: Math. Theor.56, 034001 (2023).
- [66]D. Alcalde Puente, F. Motzoi, T. Calarco, G. Morigi, M. Rizzi,Quantum state preparation via engineered ancilla resetting,
Quantum8, 1299 (2024).
- [67]S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo,Stochastic resetting in discrete-time quantum dynamics: Steady states and correlations in few-qubit systems,
Quantum9, 1742 (2025).
- [68]G. Perfetto, F. Carollo, and I. Lesanovsky,Thermodynamics of quantum-jump trajectories of open quantum systems subject to stochastic resetting,
SciPost Phys.13, 079 (2022).
- [69]F. Carollo, I. Lesanovsky, and J. P. Garrahan,Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes,
Phys. Rev. E109, 044129 (2024).
- [70]P. Solanki, I. Lesanovsky, and G. Perfetto,Universal relaxation speedup in open quantum systems through transient conditional and unconditional resetting,
arXiv:2512.10005 [quant-ph] (2025).
- [71]M. Kulkarni, S. N. Majumdar,First detection probability in quantum resetting via random projective measurements,
J. Phys. A: Math. Theor.56, 385003 (2023).
- [72]R. Yin, E. Barkai,Restart expedites quantum walk hitting times,
Phys. Rev. Lett.130, 050802 (2023).
- [73]R. Yin, Q. Wang, and E. Barkai,Instability in the quantum restart problem,
Phys. Rev. E109, 064150 (2024).
- [74]R. Yin, Q. Wang, S. Tornow, E. Barkai,Restart uncertainty relation for monitored quantum dynamics,
Proc. Natl. Acad. Sci.122, e2402912121 (2025).
- [75]E. C. King, S. Roy, F. Mattiotti,
M. Kiefer-Emmanouilidis, M. Bläser, G. Morigi,Time complexity of a monitored quantum search with resetting,
arXiv:2601.20560 [quant-ph] (2026).
- [76]M. Kulkarni, S. N. Majumdar, S. Sabhapandit,Dynamically emergent correlations in bosons via quantum resetting,
J. Phys. A: Math. Theor.58, 105003 (2025).
- [77]D. Soldner, I. Lesanovsky, G. Perfetto,Nonanaliticities and ergodicity breaking in noninteracting many-body dynamics via stochastic resetting and global measurements,
Phys. Rev. E114, 014105 (2026).
- [78]M. Magoni, F. Carollo, G. Perfetto, I. Lesanovsky,Emergent quantum correlations and collective behavior in noninteracting quantum systems subject to stochastic resetting,
Phys. Rev. A106, 052210 (2022).
- [79]M. Kulkarni, S. N. Majumdar,Generating entanglement by quantum resetting,
Phys. Rev. A108, 062210 (2023).
- [80]X. Turkeshi, M. Dalmonte, R. Fazio, and M. Schirò,Entanglement transitions from stochastic resetting of non-Hermitian quasiparticles,
Phys. Rev. B105, L241114 (2022).
- [81]L. Gotta, M. Kulkarni, G. Perfetto,Towers of quantum many-body scars under stochastic resetting,
arXiv:2603.13165 [cond-mat.stat-mech] (2026).
- [82]S. Ghosh, M. Kulkarni, K. Sengupta, S. N. Majumdar,Generating pairwise entanglement in periodically driven quantum spin chains with stochastic resetting,
arXiv:2604.19333 [quant-ph] (2026).
- [83]J. Murauer, S. Tornow, and G. Perfetto,Nonequilibrium steady states induced by stochastic mid-circuit measurements and resets on a quantum computer,
arXiv:2606.19027 [quant-ph] (2026).
- [84]D. Boyer, C. Solis-Salas,Random walks with preferential relocations to places visited in the past and their application to biology,
Phys. Rev. Lett.112, 240601 (2014).
- [85]C. Mailler, G. Uribe Bravo,Random walks with preferential relocations and fading memory: a study through random recursive trees,
J. Stat. Mech.2019, 093206 (2019).
- [86]D. Boyer, J. C. R. Romo-Cruz,Solvable random-walk model with memory and its relations with Markovian models of anomalous diffusion,
Phys. Rev. E90, 042136 (2014).
- [87]D. Boyer and I. Pineda,Slow Lévy flights,
Phys. Rev. E93, 022103 (2016).
- [88]A. Falcón-Cortés, D. Boyer, L. Giuggioli, S. N. Majumdar,Localization transition induced by learning in random searches,
Phys. Rev. Lett.119, 140603 (2017).
- [89]D. Boyer, A. Falcón-Cortés, L. Giuggioli, S. N. Majumdar,Anderson-like localization transition of random walks with resetting,
J. Stat. Mech.2019, 053204 (2019).
- [90]A. Masó-Puigdellosas, D. Campos, V. Méndez,Anomalous diffusion in random-walks with memory-induced relocations,
Front. Phys.7, 112 (2019).
- [91]D. Boyer, M. R. Evans, S. N. Majumdar,Long time scaling behaviour for diffusion with resetting and memory,
J. Stat. Mech.2017, 023208 (2017).
- [92]D. Boyer, S. N. Majumdar,Active particle in one dimension subjected to resetting with memory,
Phys. Rev. E109, 054105 (2024).
- [93]D. Boyer, S. N. Majumdar,Ultra slow sub-logarithmic diffusion of a sluggish random walker subject to resetting with memory,
J. Stat. Mech.2026, 063201 (2026).
- [94]D. Boyer, S. N. Majumdar,Power-law relaxation of a confined diffusing particle subject to resetting with memory,
J. Stat. Mech.2024, 073206 (2024).
- [95]D. Boyer, M. R. Evans, S. N. Majumdar,Diffusion with preferential relocation in a confining potential,
J. Stat. Mech.2025, 013209 (2025).
- [96]F. Carollo and S. Wald,Stochastic resetting induces quantum non-Markovianity,
arXiv:2601.13367 [quant-ph] (2026).
- [97]R. P. Feynman, A. R. Hibbs, D. F. Styer,Quantum Mechanics and Path Integrals,
Courier Corporation (2010).
- [98]NIST Digital Library of Mathematical Functions,
Release 1.2.7, National Institute of Standards and Technology
(15 June 2026),https://dlmf.nist.gov/.
- [99]V. Gorini, A. Kossakowski, E. C. G. Sudarshan,Completely positive dynamical semigroups ofNN-level systems,
J. Math. Phys.17, 821 (1976).
- [100]G. Lindblad,On the generators of quantum dynamical semigroups,
Commun. Math. Phys.48, 119 (1976).
- [101]H.-P. Breuer, F. Petruccione,The Theory of Open Quantum Systems(Oxford University Press, Oxford, 2006).
- [102]H. J. Carmichael,Statistical Methods in Quantum Optics 1:
Master Equations and Fokker–Planck Equations(Springer-Verlag, Berlin, Heidelberg, 2002).

## 


- 


Major funding support from
