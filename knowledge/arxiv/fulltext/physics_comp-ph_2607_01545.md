# Learning Effective Soliton Dynamics from Scattering Data

**arXiv ID**: 2607.01545v1
**Authors**: Seth Minor, Vanja Dukic, David M. Bortz
**Published**: 2026-07-01
**Categories**: physics.comp-ph, nlin.SI, stat.ML
**Comments**: 22 pages, 5 figures
**HTML URL**: https://arxiv.org/html/2607.01545v1

## Abstract

The inverse scattering transform (IST) provides the standard theoretical framework for deriving soliton dynamics. Traditionally, such derivations have been of an analytical, rather than data-driven, nature. In this paper, we combine the conceptual framework of the IST with weak-form system identification methods to discover effective soliton dynamics directly from observed scattering data, without assuming prior knowledge of the scattering equations. Our method avoids parameterizing solitary waves via ad hoc curve-fitting by working in the scattering domain, yielding interpretable low-dimensional models that remain valid in perturbed and near-integrable regimes. We demonstrate the performance of the proposed approach on synthetic and experimental data governed by shallow-water equations of Korteweg--de Vries-type and recover models that are consistent with canonical IST theory.

## Full Text

Learning Effective Soliton Dynamics from Scattering Data

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
- License: CC BY-NC-SA 4.0arXiv:2607.01545v1 [physics.comp-ph] 01 Jul 2026

## Learning Effective Soliton Dynamics from Scattering DataSeth MinorVanja DukicDavid M. Bortz\orgdivDepartment of Applied Mathematics,\orgnameUniversity of Colorado,\orgaddress\cityBoulder,\stateCO,\countryUSA

## Abstract

Theinverse scattering transform(IST) provides the standard theoretical framework for deriving soliton dynamics. Traditionally, such derivations have been of an analytical, rather than data-driven, nature. In this paper, we combine the conceptual framework of the IST with weak-form system identification methods to discover effective soliton dynamics directly from observed scattering data, without assuming prior knowledge of the scattering equations. Our method avoids parameterizing solitary waves via ad hoc curve-fitting by working in the scattering domain, yielding interpretable low-dimensional models that remain valid in perturbed and near-integrable regimes. We demonstrate the performance of the proposed approach on synthetic and experimental data governed by shallow-water equations of Korteweg–de Vries-type and recover models that are consistent with canonical IST theory.

## keywords:weak-form system identification, inverse scattering transform, solitons, Korteweg-de Vries equation\jyear

2026{Frontmatter}\authormark

Minoret al.\authormark

Minor et al.

## 1Introduction

A central mathematical problem in the study of nonlinear dispersive waves is the construction of effective, low-dimensional models for coherent solitary wave structures (solitons). In such settings, theinverse scattering transform(IST) of Ablowitz, Kaup, Newell, and Segur[Ablowitz.etal1974StudApplMath]has enjoyed a rich and successful history, and is now the standard theoretical framework for deriving reduced-order evolution equations for soliton dynamics. Although these derivations are traditionally of an analytical – rather than data-driven – nature, recent work has employed the IST formalism as a tool for experimental data analysis, using the technique to analyze soliton content from empirical measurements[Feng.etal2023FrontPhys,Lee.etal2024PLoSONE,Tikan.etal2022SciRep]. Moreover, recent approaches using alternative parameterization techniques have demonstrated that the learning of reduced-order, interpretable equations of motion for solitons is tenable in a data-driven setting[Chen.etal2025ChaosInterdiscipJNonlinearSci,Yang.etal2024FrontPhotonics,Yang.etal2025]. Despite the success of this recent work, however, little effort has been devoted to developing a data-driven modeling approach based on the IST itself, most likely due to the fact that the framework is fundamentally problem-specific.

In this paper, we address the question of whether effective soliton dynamics can be inferred directly from observed scattering data (as opposed to being derived or approximated analytically). We show that the conceptual framework of the IST can be combined with modern weak-form equation learning methods to identify interpretable models for the scattering dynamics, without assuming prior knowledge about the form of the equations. Our proposed method avoids parameterizing solitary waves via ad hoc curve-fitting by working in natural spectral domains, yielding interpretable low-dimensional models that remain valid in perturbed, near-integrable regimes. In this paper, we specifically focus on examples related to the canonical Korteweg–de Vries equation; however, we do briefly comment on the potential for extension to other integrable equations in Section5.

The paper is organized as follows. In Section2, we relate to previous work (§2.1), establish some notational conventions and background assumptions (§2.2), identify the specific class of models being considered (§2.3), and review background material on the IST (§2.4) as well as the paradigm of weak form modeling (§2.5). Later, in Section3, we outline our approach (§3.1) and numerical implementation (§3.2and §3.3). In Section4, we discuss validation metrics (§4.1) before presenting some preliminary numerical results obtained using simulated data (§4.2) and experimental water-wave data (§4.3), pausing briefly to comment on structural identifiability concerns (§4.4). Finally, we conclude with a summary and discussion in Section5. Supplemental information is given in the Appendix.

## 2Background Material

## 2.1Relation to Previous Work

It is important to note that there are many ways of parameterizing solitary waves, and different choices can lead to distinct effective models[Guo.etal2022PhysRevResearch,Zhang.etal2025ComputerMethodsinAppliedMechanicsandEngineering]. In the recent literature, Chen, Yang, Zhu, and Kevrekidis have explicitly fit parameterized waveforms (centers, widths, amplitudes, phases) to simulated data[Yang.etal2025], and have also considered parameterizing the statistical moments of physically relevant quantities[Chen.etal2025ChaosInterdiscipJNonlinearSci,Yang.etal2024FrontPhotonics], before then applying equation learning approaches to discover effective dynamic models governing the corresponding parameters. Here, we instead propose to usescattering data(formally defined in §2.4) directly as a parameterization of the soliton field. This choice has at least two advantages:
- •

it is natural in the context of nonlinear wave equations, inheriting a conceptual framework and set of known analytical results from existingdirect/inverse scattering transform(DST/IST) theory;
- •

it avoids fitting ad hoc, problem-specific waveforms to the data.

Unfortunately, there is no free lunch regarding the latter point – a significant caveat of using scattering data is that, while the IST framework of[Ablowitz.etal1974StudApplMath]does supply a fairly unified language across many integrable equations of interest, the definitions of both DST and IST are inherently problem-specific.

## 2.2Notation and Assumptions

Herein, we will letu=u​(x,t)u=u(x,t)denote a scalar-valued field which represents a solution to a perturbed, dispersive partial differential equation (PDE) of the formut+N​[u]=ϵ​F​[u],with{u​(x,0)=u0​(x),(x,t)∈(−∞,∞)×[0,T],\displaystyle u_{t}+N[u]=\epsilon F[u],\quad\text{with}\quad\begin{cases}u(x,0)=u_{0}(x),\\
(x,t)\in(-\infty,\infty)\times[0,T],\end{cases}(2.1)

whereNNandFFare (potentially nonlinear) differential operators and0≤ϵ≪10\leq\epsilon\ll 1is a small parameter representing a perturbation to the system. Of particular interest areintegrable systems,111For our purposes, it will suffice to define an ‘integrable system’ as a system of partial differential equations that admits a Lax pair representation.which forϵ=0\epsilon=0admit aLax pair– linear operatorsL=L​(u)L=L(u)andM=M​(u)M=M(u)which depend onuuand satisfy(Lt​(u)+[L,M]​(u))​ϕ=(ut+N​[u])⋅ϕ=0,\displaystyle\big(L_{t}(u)+[L,M](u)\big)\phi=\big(u_{t}+N[u]\big)\cdot\phi=0,(2.2)

for any test functionϕ=ϕ​(x,t)\phi=\phi(x,t)of appropriate smoothness, where[⋅,⋅][\cdot\,,\cdot]is the commutator operator andLt:=[∂t,L]L_{t}:=[\operatorname{\partial}_{t},L]denotes the operator-valued time derivative ofLL. This identity arises as a consistency condition for an associated overdetermined eigenvalue problem (EVP) given by{L​(u)​ϕ=λ​ϕ,ϕt=M​(u)​ϕ.\displaystyle\begin{cases}L(u)\phi=\lambda\phi,\\
\phi_{t}=M(u)\phi.\end{cases}(2.3)

To keep the exposition somewhat concise and self-contained, we have deferred a more detailed review of Lax pairs to Appendix §B. Throughout the paper, the following two assumptions are in play: (1) the field decays asymptotically (i.e.,|u|→0|u|\rightarrow 0asx→±∞x\rightarrow\pm\infty),222From an analytical perspective, the rate of decay must be sufficiently fast – a standard assumption is thatu∈L1u\in L^{1}and(1+|x|)⋅u0∈L1(1+|x|)\cdot u_{0}\in L^{1}.and (2) the underlying PDE and Lax pair are available in closed form. Regarding (2), we note that, e.g., the WSINDy[Messenger.etal2024SciRep]and SILO[Adriazola.etal2026SIAMJApplDynSyst]algorithms are respectively capable of identifying theNNandL,ML,Moperators from nonlinear wave equation data, indicating that an end-to-end data-driven extension of the current work is also tenable.

## 2.3Equations Considered

To illustrate our proposed method on a canonical and well-understood testbed, we focus on examples related to theKorteweg-de Vries(KdV)equation, a prototypical model of shallow water waves given byut+α​u​ux+β​ux​x​x=0,where{L​(u)=−(∂x2+α6​β​u),M​(u)=−(4​β​∂x3+α​u​∂x+α2​[∂x,u]).\displaystyle u_{t}+\alpha uu_{x}+\beta u_{xxx}=0,\quad\text{where}\quad\begin{cases}L(u)=-\big(\!\operatorname{\partial}^{2}_{\!x}+\,\frac{\alpha}{6\beta}u\big),\\
M(u)=-\big(4\beta\!\operatorname{\partial}^{3}_{\!x}+\,\alpha u\!\operatorname{\partial}_{\!x}+\,\frac{\alpha}{2}[\operatorname{\partial}_{\!x},u]\big).\end{cases}(2.4)

We also consider nontrivial perturbations of the KdV equation, leading to models of the formut+α​u​ux+β​ux​x​x=ϵ​F​[u].\displaystyle u_{t}+\alpha uu_{x}+\beta u_{xxx}=\epsilon F[u].(2.5)

In particular, for a fifth-order dispersive forcing termF​[u]:=∂x5⁡uF[u]:=\operatorname{\partial}^{5}_{\!x}u, the perturbed KdV model given above collapses to theKawahara equation,ut+α​u​ux+β​ux​x​x=ϵ​ux​x​x​x​x.\displaystyle u_{t}+\alpha uu_{x}+\beta u_{xxx}=\epsilon u_{xxxxx}.(2.6)

Our focus on this specific class of governing equations is partly motivated by the recent success of Heinrich et al.[Heinrich.etal2025]in applying data-driven equation-learning methods to experimental wave-tank data, in which a Kawahara-type model was identified.333In[Heinrich.etal2025], the identified model was equivalent to eq. (2.6) with coefficientsα≈1.36\alpha\approx 1.36,β≈0.62\beta\approx 0.62, andϵ≈0.06\epsilon\approx 0.06; see §4.3below.However, a near-identical pipeline extends to other integrable equations that admit a Lax pair representation; we return to this point in
Section5.

## 2.4The Inverse Scattering Transform

In standard acoustic scattering problems, one is often concerned with identifying the form of a spatially varying parameterv​(x)v(x)associated with a linear hyperbolic PDE such as the classical wave equation,v​(x)−2​ut​t−ux​x=0,\displaystyle v(x)^{-2}u_{tt}-u_{xx}=0,

in some inhomogeneous regionx∈Ωx\in\Omegawherev​(x)→v0v(x)\rightarrow v_{0}collapses to a background value asx→∞x\rightarrow\infty. Adopting a temporally-modulated ansatz of the formu​(x,t)=ϕ​(x)​e−i​ω​tu(x,t)=\phi(x)e^{-i\omega{t}}and heuristically introducing ascattering potentialV​(x):=k2​(1−η​(x)2)V(x):=k^{2}(1-\eta(x)^{2}), whereη​(x):=v0/v​(x)\eta(x):=v_{0}/v(x)is theindex of refractionandk:=ω/v0k:=\omega/v_{0}is an associated wavenumber, one obtains a Schrödinger-type EVP (cf. eq. (2.3)) given byL​ϕ=k2​ϕ,withL=−∂x2+V​(x).\displaystyle L\phi=k^{2}\phi,\quad\text{with}\quad L=-\operatorname{\partial}^{2}_{\!x}\,+\,V(x).(2.7)

For fixedV​(x)V(x), the self-adjoint operatorLLhas a point spectrum defined by a finite set of eigenvaluesλi=ki2<0\lambda_{i}=k^{2}_{i}<0fori=1,…,ni=1,\dots,n, and a continuous spectrum which consists of allλ=k2∈[0,∞)\lambda=k^{2}\in[0,\infty). Traditionally, the solutions to eq. (2.7) are decomposed linearly asϕ=ϕin+ϕout\phi=\phi_{\text{in}}+\phi_{\text{out}}, whereϕin​(x;k)=e𝒊​k​x\phi_{\text{in}}(x;k)=e^{\boldsymbol{i}kx}represents an incoming wave andϕout​(x;ki)∼ci​e𝒊​ki​x\phi_{\text{out}}(x;k_{i})\sim c_{i}e^{\boldsymbol{i}k_{i}x}orϕout​(x;k)∼R​(k)​e𝒊​k​x\phi_{\text{out}}(x;k)\sim R(k)e^{\boldsymbol{i}kx}represent bound or scattered waves corresponding to the point spectrum or the continuous spectrum, respectively.

It is often convenient to write the asymptotic weighting coefficientscic_{i}andR​(k)R(k), respectively referred to as thenorming constantsandreflection coefficient, in terms of the positiveJost solution,ϕ+\phi_{+}, of the Schrödinger EVP in eq. (2.7). Fork≠0k\neq 0, this eigenfunction can be uniquely defined as the solution of the EVP subject to the boundary conditionϕ+​(x;k)=ρ​(x;k)​ei​k​x∼e𝒊​k​x\phi_{+}(x;k)=\rho(x;k)e^{ikx}\sim e^{\boldsymbol{i}kx}asx→∞x\rightarrow\infty, or equivalently:L​ρ=2​𝒊​ki​ρ′,subject to{ρ​(∞)=1,ρ′​(∞)=0.\displaystyle L\rho=2\boldsymbol{i}k_{i}\rho^{\prime},\quad\text{subject to}\quad\begin{cases}\rho(\infty)=1,\\
\rho^{\prime}(\infty)=0.\end{cases}(2.8)

Following the Marchenko convention and definingκ:=−𝒊​k\kappa:=-\boldsymbol{i}kwithλi=−κi2<0\lambda_{i}=-\kappa^{2}_{i}<0, one typically expressesc​(κi):=[∫−∞∞ϕ+​(x,t;𝒊​κi)2​𝑑x]−1​andR​(k):=b​(k)a​(k),\displaystyle c(\kappa_{i}):=\left[\int_{-\infty}^{\infty}\phi_{+}(x,t;\boldsymbol{i}\kappa_{i})^{2}\,dx\right]^{-1}\!\quad\text{and}\ \quad R(k):=\frac{b(k)}{a(k)},(2.9)

given thatϕ+​(x;k)∼a​(k)​e𝒊​k​x+b​(k)​e−𝒊​k​x\phi_{+}(x;k)\sim a(k)e^{\boldsymbol{i}kx}+b(k)e^{-\boldsymbol{i}kx}asx→−∞x\rightarrow-\infty. We refer to the set ofnneigenvaluesλi:=−κi2\lambda_{i}:=-\kappa^{2}_{i}in the point spectrum ofLL, together with the corresponding constantsci:=c​(κi)c_{i}:=c(\kappa_{i})and reflection coefficientR​(k)R(k)for eachλ=k2\lambda=k^{2}in the continuous spectrum, as thescattering data,σ\sigma, corresponding to the EVP:σ​(L):={(κi,c​(κi)):i=1,…,n}∪{(k,R​(k)):k∈ℝ}.\displaystyle\sigma(L):=\big\{\big(\kappa_{i},c(\kappa_{i})\big)\,:\,i=1,\dots,n\big\}\,\cup\,\big\{\big(k,R(k)\big)\,:\,k\in\mathbb{R}\big\}.(2.10)

In aforward scattering problem, one aims to compute the scattering data for a known potentialV​(x)V(x), while in aninverse scattering problem, one instead aims to recoverV​(x)V(x)from observed scattering data.

At a high level, the IST formalism of[Ablowitz.etal1974StudApplMath]turns the standard scattering paradigm described above on its head by associating a nonlinear PDE of the form of eq. (2.1) with an equivalent linear EVP of the form of eq. (2.3), by way of a Lax pair representationLt+[L,M]=ut+N​[u]L_{t}+[L,M]=u_{t}+N[u]. For the shallow-wave models introduced in §2.3, this can be interpreted as solving a one-parameter family of Schrödinger EVPs (just as in eq. (2.7) above) defined by the scattering potentialsV​(x;t):=γ​u​(x,t),withγ:=−α6​β,\displaystyle V(x;t):=\gamma u(x,t),\quad\text{with}\quad\gamma:=-\frac{\alpha}{6\beta},

whereu=u​(x,t)u=u(x,t)denotes the solution to the nonlinear PDE andL​(u)=−∂x2+V​(x;t)L(u)=-\operatorname{\partial}^{2}_{\!x}\,+\,V(x;t)is now the Lax operator corresponding to the KdV equation. Here, the time derivative of the Lax operator isLt=γ​utL_{t}=\gamma u_{t}.

For a fixed timet≥0t\geq 0, thedirect scattering transform𝒮t:u↦σ​(L​(u)|t)\mathcal{S}_{t}:u\mapsto\sigma(L(u)|_{t})is defined as the nonlinear map which uniquely associates a fielduuto its scattering data,𝒮t​[u]:=σ​(L​(u)|t)={(κi​(t),ci​(t)):i=1,…,n}∪{(k,R​(k,t)):k∈ℝ}.\displaystyle\mathcal{S}_{t}[u]:=\sigma\big(L(u)|_{t}\big)=\big\{\big(\kappa_{i}(t),c_{i}(t)\big)\,:\,i=1,\dots,n\big\}\,\cup\,\big\{\big(k,R(k,t)\big)\,:\,k\in\mathbb{R}\big\}.(2.11)

Conversely, theinverse scattering transform𝒮t−1:σ​(L​(u))↦u​(⋅,t)\mathcal{S}^{-1}_{t}:\sigma(L(u))\mapsto u(\cdot,t)uses scattering data to reconstruct the field. In the context of the KdV-type models, the inverse transform𝒮t−1\mathcal{S}^{-1}_{t}can be implicitly defined for scattering dataσ\sigmaof the form of eq. (2.10) via𝒮t−1​[σ]​(x):=−2γ​∂x⁡Kσ​(x,x,t),with𝒮t−1​[σ​(L​(u))]​(x)=u​(x,t),\displaystyle\vskip-2.84526pt\mathcal{S}^{-1}_{t}[\sigma](x):=-\frac{2}{\gamma}\operatorname{\partial}_{\!x}K_{\sigma}(x,x,t),\quad\text{with}\quad\mathcal{S}^{-1}_{t}\big[\sigma\big(L(u)\big)\big](x)=u(x,t),(2.12)

whereKσK_{\sigma}is the unique interaction kernel satisfying theGelfand-Levitan-Marchenko(GLM)equation,Kσ​(x,y,t)+Gσ​(x+y,t)+∫x∞Kσ​(x,x′,t)​Gσ​(x′+y,t)​𝑑x′=0,fory≥x.\displaystyle K_{\sigma}(x,y,t)\,+\,G_{\!\sigma}(x+y,t)\,+\int_{x}^{\infty}K_{\sigma}(x,x^{\prime},t)\,G_{\!\sigma}(x^{\prime}+y,t)\,dx^{\prime}=0,\quad\text{for}\quad y\geq x.(2.13)

Here, the functionGσG_{\!\sigma}denotes the observed reflection response and is defined byGσ​(x;t):=∑i=1nci​(t)​ei​ki​x+12​π​∫−∞∞R​(k,t)​ei​k​x​𝑑k.\displaystyle G_{\!\sigma}(x;t):=\sum_{i=1}^{n}c_{i}(t)e^{ik_{i}x}+\frac{1}{2\pi}\int_{-\infty}^{\infty}R(k,t)e^{ikx}dk.

The GLM equation reconstructs a hidden 1D medium from its reflected waves, and thus can be thought of as a kind of deconvolution equation.

An important consequence of eq. (2.3) is that the spectrum ofLLis invariant in time; for any eigenpair(λ,ϕ)(\lambda,\phi)initially satisfyingL​ϕ=λ​ϕL\phi=\lambda\phiatt=0t=0, one hasϕt=M​ϕ\phi_{t}=M\phiandλ˙=0\dot{\lambda}=0for allt≥0t\geq 0(see AppendixB).
For unperturbed systems (i.e., forϵ=0\epsilon=0), the scattering data also evolve linearly according toR˙=𝒊​ω​(k)​R,with{κ˙i=0,c˙i=ω​(κi)​ci,​for eachi=1,…,n,\displaystyle\dot{R}=\boldsymbol{i}\omega(k)R,\quad\ \text{with}\ \quad\begin{cases}\dot{\kappa}_{i}=0,\\
\dot{c}_{i}=\omega(\kappa_{i})c_{i},\end{cases}\text{for each}\ \ i=1,\dots,n,(2.14)

whereω​(k):=8​β​k3\omega(k):=8\beta k^{3}is the dispersion relation of the KdV equation (2.4). The upshot is that the original nonlinear PDE can then be reduced to the system of linear ordinary differential equations (ODEs) in eq. (2.14) and solved via the following recipe:u0→DST𝒮0​[u]→integrate scattering ODEs𝒮t​[u]→ISTu.\displaystyle u_{0}\,\xrightarrow{\text{DST}}\,\mathcal{S}_{0}[u]\,\xrightarrow{\text{integrate scattering ODEs}}\,\mathcal{S}_{t}[u]\,\xrightarrow{\text{IST}}u.

In the case that0<ϵ≪10<\epsilon\ll 1, the adiabatic perturbation theory of Karpman and Solov’ev[Karpman.Solovev1981PhysicaDNonlinearPhenomena]confirms that the equations of motion continuously deform to the tune ofR˙=𝒊​ω​(k)​R+ϵ​fR​(k)+𝒪​(ϵ2),with{κ˙i=0+ϵ​fκi​(𝜿,𝐜,R)+𝒪​(ϵ2),c˙i=ω​(κi)​ci+ϵ​fci​(𝜿,𝐜,R)+𝒪​(ϵ2).\displaystyle\dot{R}=\boldsymbol{i}\omega(k)R+\epsilon f_{R}(k)+\mathcal{O}(\epsilon^{2}),\quad\ \text{with}\ \quad\begin{cases}\dot{\kappa}_{i}=0+\epsilon f_{\kappa_{i}}(\boldsymbol{\kappa},\mathbf{c},R)+\mathcal{O}(\epsilon^{2}),\\
\dot{c}_{i}=\omega(\kappa_{i})c_{i}+\epsilon f_{c_{i}}(\boldsymbol{\kappa},\mathbf{c},R)+\mathcal{O}(\epsilon^{2}).\end{cases}(2.15)

A natural connection between the scattering ODEs given above and the governing PDE is obtained by recognizing that the fielduucan be decomposed intonnlocalized waves parameterized in the fashionu​(x,t)=usol​(x;𝐱1​(t),…,𝐱n​(t))+urad​(x,t),\displaystyle u(x,t)=u_{\text{sol}}\big(x;\mathbf{x}_{1}(t),\dots,\mathbf{x}_{n}(t)\big)\,+\,u_{\text{rad}}(x,t),(2.16)

where𝐱i:=(κi,ci)\mathbf{x}_{i}:=(\kappa_{i},c_{i})represents the scattering data associated with theithi^{\rm{th}}soliton anduradu_{\text{rad}}represents any excessradiation. Importantly, for a pure-soliton solution (urad=0u_{\text{rad}}=0), the system isreflectionless(R=0R=0).

## 2.5Sparse Regression with WSINDy

Consider a state vector𝒙​(t)=(x1,…,xd)​(t)∈ℝd\boldsymbol{x}(t)=(x_{1},\dots,x_{d})(t)\in\mathbb{R}^{d}governed by a system of ODEs444In this paper, we will be concerned with ordinary differential equations. However, the SINDy[Brunton.etal2016ProcNatlAcadSciUSA]and WSINDy[Messenger.Bortz2021MultiscaleModelSimul]paradigms can also be extended to work with partial differential equations; see[Messenger.Bortz2021JournalofComputationalPhysics,Rudy.etal2017SciAdv,schaefferLearningPartialDifferential2017].of the form𝒙˙=𝚯​(𝒙)​𝐰,with{𝚯​(𝒙):=[f1​(𝒙),…,fJ​(𝒙)]∈ℝJ,𝐰=[𝐰1,…,𝐰d]∈ℝJ×d,\displaystyle\dot{\boldsymbol{x}}=\mathbf{\Theta}(\boldsymbol{x})\mathbf{w},\quad\text{with}\quad\begin{cases}\mathbf{\Theta}(\boldsymbol{x}):=[f_{1}(\boldsymbol{x}),\,\dots\,,\,f_{J}(\boldsymbol{x})]\in\mathbb{R}^{J},\\
\mathbf{w}=[\mathbf{w}_{1},\,\dots\,,\,\mathbf{w}_{d}]\in\mathbb{R}^{J\times d},\end{cases}(2.17)

where eachfj:ℝd→ℝf_{j}:\mathbb{R}^{d}\rightarrow\mathbb{R}represents a scalar-valued function of the state, given component-wise byx˙i=𝚯​(𝒙)​𝐰i,for eachi=1,…,d.\displaystyle\dot{x}_{i}=\mathbf{\Theta}(\boldsymbol{x})\mathbf{w}_{i},\quad\text{for each}\quad i=1,\dots,d.

Theweak-form sparse identification of nonlinear dynamics(WSINDy) algorithm[Messenger.Bortz2021JournalofComputationalPhysics]is a data-driven technique which attempts to infer dynamics of the form of eq. (2.17) above from noisy training data𝒳={𝒙​(tm)+𝜺​(tm):m=1,…,Nt},where, e.g.,𝜺​(t)∼𝒩​(0,σε2​𝐈).\displaystyle\mathcal{X}=\big\{\boldsymbol{x}(t_{m})+\boldsymbol{\varepsilon}(t_{m})\,:\,m=1,\dots,N_{t}\big\},\quad\text{where, e.g.,}\quad\boldsymbol{\varepsilon}(t)\sim\mathcal{N}\big(0,\sigma^{2}_{\!\varepsilon}\mathbf{I}\big).

This is accomplished by integrating the governing ODE against a collection of smooth and compactly supported test functions,φk​(t):=φ​(tmk−t),fork=1,…,K,\displaystyle\varphi_{k}(t):=\varphi(t_{m_{k}}-t),\quad\text{for}\ \ \ k=1,\dots,K,

whereφ∈Cc∞\varphi\in C^{\infty}_{c}is symmetric aboutt=0t=0and thequery points,tmk∈[0,T]t_{m_{k}}\in[0,T], are uniformly placed within the domain. Using integration by parts, models of the form of eq. (2.17) are then transformed into theirconvolutional weak formulations,555Note that the factor of ‘−1-1’ resulting from integration by parts is eliminated by adopting the sign convention(φ∗f)(tk)=⟨φ(tmk−⋅),f(⋅)⟩(\varphi*f)(t_{k})=\langle\varphi(t_{m_{k}}-\cdot),f(\cdot)\rangle.(φ˙∗𝒙)​(tmk)=(φ∗𝚯​(𝒙)​𝐰)​(tmk).\displaystyle\big(\dot{\varphi}*\boldsymbol{x}\big)(t_{m_{k}})=\big(\varphi*\mathbf{\Theta}(\boldsymbol{x})\mathbf{w}\big)(t_{m_{k}}).(2.18)

Accordingly, we investigate the linear system given by𝐛​(𝒙)=𝐆​(𝒙)​𝐰,where{𝐛​(𝒙)k,i:=(φ˙∗xi)​(tmk)=⟨φ˙k,xi⟩,𝐆​(𝒙)k,j:=(φ∗fj​(𝒙))​(tmk)=⟨φk,fj​(𝒙)⟩,\displaystyle\mathbf{b}(\boldsymbol{x})=\mathbf{G}(\boldsymbol{x})\mathbf{w},\quad\text{where}\quad\begin{cases}\mathbf{b}(\boldsymbol{x})_{k,i}:=\big(\dot{\varphi}*x_{i}\big)(t_{m_{k}})=\langle\dot{\varphi}_{k},x_{i}\rangle,\\
\mathbf{G}(\boldsymbol{x})_{k,j}:=\big(\varphi*f_{j}(\boldsymbol{x})\big)(t_{m_{k}})=\langle\varphi_{k},f_{j}(\boldsymbol{x})\rangle,\end{cases}(2.19)

where⟨⋅,⋅⟩\langle\cdot\,,\cdot\rangledenotes theL2L^{2}inner-product. Observe that in eqs. (2.18) and (2.19), no differential operators are applied directly to the state variable𝒙=𝒙​(t)\boldsymbol{x}=\boldsymbol{x}(t)– a property which increases the fidelity of the results in noisy regimes (that is, compared to the strong-form of SINDy[Brunton.etal2016ProcNatlAcadSciUSA]; see, e.g., Table 6 in[Messenger.Bortz2021JournalofComputationalPhysics]).

In contrast to standard parameter estimation problems, here the form of the governing equation isnotassumed to be known prima-facie. Instead, one typically assumes in the context of sparse regression that thelibraryof candidate terms𝚯​(𝒙)\mathbf{\Theta}(\boldsymbol{x})is substantially over-specified, and that only a small subset of its parameters are nonzero (i.e., the parameter matrix𝐰\mathbf{w}is sparse). In turn, WSINDy targets a regularized least-squares problem of the form𝐰^:=argmin𝐰∈ℝJ×dℒμ​(𝐰),whereℒμ​(𝐰):=‖𝐛​(𝒙)−𝐆​(𝒙)​𝐰‖F2+μ​‖𝐰‖0.\displaystyle\hat{\mathbf{w}}:=\operatorname*{argmin}_{\mathbf{w}\in\mathbb{R}^{J\times d}}\,\mathcal{L}_{\mu}(\mathbf{w}),\quad\text{where}\quad\mathcal{L}_{\mu}(\mathbf{w}):=\left\|\mathbf{b}(\boldsymbol{x})-\mathbf{G}(\boldsymbol{x})\mathbf{w}\right\|^{2}_{F}+\mu\|\mathbf{w}\|_{0}.(2.20)

The regularization termμ​‖𝐰‖0\mu\|\mathbf{w}\|_{0}in the loss function promotes the selection of a parsimonious model by penalizing the number of nonzero coefficients, where∥⋅∥0\|\cdot\|_{0}denotes theℓ0\ell_{0}pseudo-norm. Since theℓ0\ell_{0}penalty is non-differentiable, in practice the loss function in eq. (2.20) is approximately minimized via iterative thresholding schemes, e.g.,modified sequential thresholding least squares(MSTLS)[Brunton.etal2016ProcNatlAcadSciUSA,Messenger.Bortz2021JournalofComputationalPhysics], which progressively restricts the columns of𝚯​(𝒙)\boldsymbol{\Theta}(\boldsymbol{x})available to the model (see §Aof the Appendix).

## 3Methods

## 3.1High-Level Overview

As briefly mentioned in §2.1, Yang et al. have in recent work[Yang.etal2025]explored data-driven soliton dynamics (specifically, in the context of the nonlinear Schrödinger equation) by explicitly fitting parameterized waveforms to data. In particular, these authors developed a pipeline of the form{u​(x,t)}⏟measure data→{𝒙i=(ξi,ai,vi,θi)}i=1n⏟extract fit parameters→𝒙˙i≈𝚯​(𝒙)​𝐰^i,fori=1,…,n⏟infer effective ODEs with SINDy,\displaystyle\underbrace{\big\{u(x,t)\big\}}_{\text{measure data}}\quad\rightarrow\quad\underbrace{\big\{\boldsymbol{x}_{i}=(\xi_{i},a_{i},v_{i},\theta_{i})\big\}_{i=1}^{n}}_{\text{extract fit parameters}}\quad\rightarrow\quad\underbrace{\dot{\boldsymbol{x}}_{i}\approx\mathbf{\Theta}(\boldsymbol{x})\hat{\mathbf{w}}_{i},\ \ \text{for}\ \ i=1,\dots,n}_{\text{infer effective ODEs with SINDy}},

whereξi\xi_{i},aia_{i},viv_{i}, andθi\theta_{i}respectively denote the centers, amplitudes, velocities, and phases of modulatedsech-like profiles fit to theithi^{\rm{th}}soliton. For the reasons detailed in §2.1, we propose an alternative pipeline:{u​(x,t)}⏟measure data→{𝒙i=(κi,ci)}i=1n⏟compute scattering data→𝐛​(𝒙i)≈𝐆​(𝒙)​𝐰^i,fori=1,…,n⏟infer effective ODEs with WSINDy.\displaystyle\underbrace{\big\{u(x,t)\big\}}_{\text{measure data}}\quad\rightarrow\quad\underbrace{\big\{\boldsymbol{x}_{i}=(\kappa_{i},c_{i})\big\}_{i=1}^{n}}_{\text{compute scattering data}}\quad\rightarrow\quad\underbrace{\mathbf{b}(\boldsymbol{x}_{i})\approx\mathbf{G}(\boldsymbol{x})\hat{\mathbf{w}}_{i},\ \ \text{for}\ \ i=1,\dots,n}_{\text{infer effective ODEs with WSINDy}}.

Given our focus on effective models for solitons (and to simplify the core ideas of the paper), in this work we specifically address reflectionless settings withR=0R=0; however, in the regime of nonzero radiation, note that one can simply append additional components of the formR​(𝐤,t)∈ℝN𝐤R(\mathbf{k},t)\in\mathbb{R}^{N_{\mathbf{k}}}onto the state vector.

## 3.2Numerical Implementation

In our numerical implementation, we discretize the state vector𝒙​(t)∈ℝd\boldsymbol{x}(t)\in\mathbb{R}^{d}over a uniform temporal grid𝐭=[t1,…,tNt]T⊂[0,T]\mathbf{t}=[t_{1},\dots,t_{N_{t}}]^{T}\subset[0,T]with spacingΔ​t\Delta{t}, producing a data matrix𝐗:=𝐗∗+ϵ​(𝐭)∈ℝNt×d\mathbf{X}:=\mathbf{X}^{*}+\boldsymbol{\epsilon}(\mathbf{t})\in\mathbb{R}^{N_{t}\times\,d}given by𝐗=[x1​(t1)⋯xd​(t1)⋮⋮x1​(tNt)⋯xd​(tNt)]=[x1∗​(t1)⋯xd∗​(t1)⋮⋮x1∗​(tNt)⋯xd∗​(tNt)]+[ϵ1​(t1)⋯ϵd​(t1)⋮⋮ϵ1​(tNt)⋯ϵd​(tNt)],\displaystyle\mathbf{X}=\begin{bmatrix}x_{1}(t_{1})&\cdots&x_{d}(t_{1})\\
\vdots&&\vdots\\
x_{1}(t_{N_{t}})&\cdots&x_{d}(t_{N_{t}})\end{bmatrix}=\begin{bmatrix}x^{*}_{1}(t_{1})&\cdots&x^{*}_{d}(t_{1})\\
\vdots&&\vdots\\
x^{*}_{1}(t_{N_{t}})&\cdots&x^{*}_{d}(t_{N_{t}})\end{bmatrix}+\begin{bmatrix}\epsilon_{1}(t_{1})&\cdots&\epsilon_{d}(t_{1})\\
\vdots&&\vdots\\
\epsilon_{1}(t_{N_{t}})&\cdots&\epsilon_{d}(t_{N_{t}})\end{bmatrix},

where𝐗∗:=𝒙∗​(𝐭)\mathbf{X}^{*}:=\boldsymbol{x}^{*}(\mathbf{t})denotes the matrix of uncorrupted (i.e., non-noisy) data. The data matrix𝐗\mathbf{X}represents the scattering data computed from observations of a noisy scalar field𝐮​(t)∈ℝNx\mathbf{u}(t)\in\mathbb{R}^{N_{x}}of the form𝐮​(t):=𝐮∗​(t)+𝜺​(t),where𝐮​(t):=vec​{u​(n​Δ​x,t):n​Δ​x∈Ω},\displaystyle\mathbf{u}(t):=\mathbf{u}^{*}(t)+\boldsymbol{\varepsilon}(t),\quad\text{where}\quad\mathbf{u}(t):=\texttt{vec}\big\{u(n\Delta{x},t)\,:\,n\Delta{x}\in\Omega\big\},

and a discretized Lax operator𝐋​(𝐮)∈ℝNx×Nx\mathbf{L}(\mathbf{u})\in\mathbb{R}^{N_{x}\times N_{x}}defined by𝐋​(𝐮):=−𝐃x​x+γ​𝐮′=𝐐​𝚲​𝐐T,with(⋅)′:=diag​(⋅),\displaystyle\mathbf{L}(\mathbf{u}):=-\mathbf{D}_{xx}+\gamma\mathbf{u}^{\prime}=\mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{T}\!,\quad\text{with}\quad(\,\cdot\,)^{\prime}:=\texttt{diag}(\,\cdot\,),

where𝐃x​x\mathbf{D}_{xx}is a second-order centered finite difference operator and𝐐,𝚲\mathbf{Q},\mathbf{\Lambda}give a unitary diagonalization of𝐋​(𝐮)\mathbf{L}(\mathbf{u}). After ordering the entries of𝚲\mathbf{\Lambda}in ascending order, the firstnnnegative eigenvalues approximate the point spectrum ofL​(u)L(u), and we thus defineλi=−κi2:=Λi​i<0\lambda_{i}=-\kappa^{2}_{i}:=\Lambda_{ii}<0andϕi​(𝐱,t):=𝐪i​(t)\phi_{i}(\mathbf{x},t):=\mathbf{q}_{i}(t)fori=1,…,ni=1,\dots,n, where𝐐=[𝐪1,…,𝐪Nx]\mathbf{Q}=[\mathbf{q}_{1},\dots,\mathbf{q}_{N_{x}}]; see Figure1. The discrete scattering data then take the form𝒙​(t):=𝒮t​[𝐮]=[κ1​(t),…,κn​(t),c1​(t),…,cn​(t)]∈ℝd,whered:=2​n,\displaystyle\boldsymbol{x}(t):=\mathcal{S}_{t}[\mathbf{u}]=[\kappa_{1}(t),\dots,\kappa_{n}(t),c_{1}(t),\dots,c_{n}(t)]\in\mathbb{R}^{d},\quad\text{where}\quad d:=2n,

and where the norming constantscic_{i}are computed as per eq. (2.9) after numerically solving the boundary value problem in eq. (2.8) for the Jost solution.

​​​​
Figure 1:Illustrating the numerical computation of the scattering data, in this case using the noisy measurements from the two-soliton collision example of §4.2(see Figure2). [Top panel] Plotting the first few eigenvalues in the time-invariant spectrum of the discretized Lax operator𝐋​(𝐮∗)\mathbf{L}(\mathbf{u}^{*}), for reference; the ‘bound state’ eigenvaluesλi=−κi2<0\lambda_{i}=-\kappa^{2}_{i}<0in the point spectrum parameterize the soliton dynamics. [Middle panel] Plotting the numerically computedκi​(t)\kappa_{i}(t)andlog⁡(ci)​(t)\log(c_{i})(t)time-series; note that these quantities correlate with the soliton widths and locations, respectively. [Bottom panel] Comparing the true state𝐮∗​(t)\mathbf{u}^{*}(t)to the reconstructed state𝐮IST​(t)\mathbf{u}_{\text{IST}}(t)obtained by applying the IST to these scattering data

It is important to recognize that the DST mapu↦𝒮t​[u]u\mapsto\mathcal{S}_{t}[u]is highly nonlinear and, as such, can be sensitive to noisy perturbations of the formu=u∗+εu=u^{*}+\varepsilon. Although this presents limitations when working with experimental data, this sensitivity is partially alleviated by working within the noise-robust weak formulation described in §2.5. Letting𝐐∗,𝚲∗\mathbf{Q}^{*},\mathbf{\Lambda}^{*}provide a unitary diagonalization of𝐋​(𝐮∗)\mathbf{L}(\mathbf{u}^{*}), one finds that𝐋​(𝐮)=𝐋​(𝐮∗)+γ​𝜺′,or equivalently,𝐐​𝚲​𝐐T=𝐐∗​𝚲∗​𝐐∗T+γ​𝜺′.\displaystyle\mathbf{L}(\mathbf{u})=\mathbf{L}(\mathbf{u}^{*})+\gamma\boldsymbol{\varepsilon}^{\prime},\quad\text{or equivalently,}\quad\mathbf{Q\Lambda Q}^{T}=\mathbf{Q}^{*}\mathbf{\Lambda}^{*}{\mathbf{Q}^{*}}^{T}+\gamma\boldsymbol{\varepsilon}^{\prime}.

Applying first-order eigenvalue perturbation theory, one in turn finds that the eigenvalues are perturbed to the tune ofλi=λi∗+γ​‖𝐪i‖𝜺′2+𝒪​(‖𝐪i‖𝜺′4),\displaystyle\lambda_{i}=\lambda^{*}_{i}\,+\,\gamma\|\mathbf{q}_{i}\|^{2}_{\boldsymbol{\varepsilon}^{\prime}}+\,\mathcal{O}\big(\|\mathbf{q}_{i}\|^{4}_{\boldsymbol{\varepsilon}^{\prime}}\big),

meaning that, to first-order,λi=−κi2\lambda_{i}=-\kappa^{2}_{i}is approximately normally-distributed aboutλi=−(κi∗)2\lambda_{i}=-(\kappa^{*}_{i})^{2}with a standard deviation that is proportional to the weightedL2L^{2}norm‖𝐪i‖𝜺′2\|\mathbf{q}_{i}\|^{2}_{\boldsymbol{\varepsilon}^{\prime}}. Similar results also hold for the norming constantscic_{i}, which implicitly depend on the sensitivity of the Jost solutionϕ+\phi_{+}to measurement error. Adding noise can also result in the generation of spurious small negative eigenvalues, which in practice we find can be avoided by numerically enforcing a lower-bound of the formκmin∈[0.2,0.6]\kappa_{\min}\in[0.2,0.6].

We discretize the variational WSINDy problem posed in eq. (2.19) by reshaping the candidate library matrix to the tune of𝚯​(𝒙)∈ℝJ↦𝚯​(𝐗)∈ℝM×J\mathbf{\Theta}(\boldsymbol{x})\in\mathbb{R}^{J}\mapsto\mathbf{\Theta}(\mathbf{X})\in\mathbb{R}^{M\times J}, where𝚯​(𝐗):=[f1​(𝒙)​(t1)⋯fJ​(𝒙)​(t1)⋮⋮f1​(𝒙)​(tNt)⋯fJ​(𝒙)​(tNt)].\displaystyle\mathbf{\Theta}(\mathbf{X}):=\begin{bmatrix}f_{1}(\boldsymbol{x})(t_{1})&\cdots&f_{J}(\boldsymbol{x})(t_{1})\\
\vdots&&\vdots\\
f_{1}(\boldsymbol{x})(t_{N_{t}})&\cdots&f_{J}(\boldsymbol{x})(t_{N_{t}})\end{bmatrix}.

In turn, banded convolution matrices𝚽,𝚽˙∈ℝK×Nt\mathbf{\Phi},\dot{\mathbf{\Phi}}\in\mathbb{R}^{K\times{N_{t}}}can be defined via𝚽:=[φ1​(t1)⋯φ1​(tNt)⋱φK​(t1)⋯φK​(tNt)]and𝚽˙:=[φ˙1​(t1)⋯φ˙1​(tNt)⋱φ˙K​(t1)⋯φ˙K​(tNt)],with{𝐛​(𝐗):=𝚽˙​𝐗,𝐆​(𝐗):=𝚽​𝚯​(𝐗).\displaystyle\mathbf{\mathbf{\Phi}}:=\begin{bmatrix}\varphi_{1}(t_{1})&\cdots&\varphi_{1}(t_{N_{t}})\\
&\ddots&\\
\varphi_{K}(t_{1})&\cdots&\varphi_{K}(t_{N_{t}})\end{bmatrix}\quad\text{and}\quad\dot{\mathbf{\mathbf{\Phi}}}:=\begin{bmatrix}\dot{\varphi}_{1}(t_{1})&\cdots&\dot{\varphi}_{1}(t_{N_{t}})\\
&\ddots&\\
\dot{\varphi}_{K}(t_{1})&\cdots&\dot{\varphi}_{K}(t_{N_{t}})\end{bmatrix},\quad\text{with}\ \ \,\begin{cases}\mathbf{b}(\mathbf{X}):=\dot{\mathbf{\mathbf{\Phi}}}\mathbf{X},\\
\mathbf{G}(\mathbf{X}):=\mathbf{\mathbf{\Phi}}\mathbf{\Theta}(\mathbf{X}).\end{cases}

The discretized analogue of the weak convolutional formulation in eq. (2.18) is then given, up to a quadrature error‖𝐞int‖=𝒪​(Δ​tp+1)\|\mathbf{e}_{\text{int}}\|=\mathcal{O}(\Delta{t}^{p+1})with2​p2pbeing the polynomial order ofφ\varphi, by𝐛​(𝐗∗)≈𝐆​(𝐗∗)​𝐰∗\mathbf{b}(\mathbf{X}^{*})\approx\mathbf{G}(\mathbf{X}^{*})\mathbf{w}^{*}. Similarly, the discrete analogue of the sparse regression problem in eq. (2.20) takes the form𝐰^:=argmin𝐰∈ℝJ×dℒμ​(𝐰),whereℒμ​(𝐰):=‖𝐛​(𝐗)−𝐆​(𝐗)​𝐰‖F2+μ​‖𝐰‖0,\displaystyle\hat{\mathbf{w}}:=\operatorname*{argmin}_{\mathbf{w}\in\mathbb{R}^{J\times d}}\,\mathcal{L}_{\mu}(\mathbf{w}),\quad\text{where}\quad\mathcal{L}_{\mu}(\mathbf{w}):=\left\|\mathbf{b}(\mathbf{X})-\mathbf{G}(\mathbf{X})\mathbf{w}\right\|^{2}_{F}+\mu\|\mathbf{w}\|_{0},(3.1)

the solution of which we approximate via the MSTLS algorithm described in AppendixA.

## 3.3Test Functions and Candidate Library

Following[Messenger.Bortz2021JournalofComputationalPhysics], we use a rescaled Bernstein polynomial for the generating test functionφ\varphi, defined in a piecewise fashion byφ​(t;m,p):=(1−t2m2​Δ​t2)pwithint∈supp​(φ):=[−m​Δ​t,m​Δ​t],\displaystyle\varphi(t;m,p):=\left(1-\frac{t^{2}}{m^{2}\Delta{t}^{2}}\right)^{p}\quad\text{within}\quad t\in\text{supp}(\varphi):=\,[-m\Delta{t},\,m\Delta{t}],

where the degreeppis defined for a highest derivative orderα¯:=1\bar{\alpha}:=1and support toleranceτ0:=1​e−10\tau_{0}:=1\texttt{e}-10viap=max⁡{⌈ln⁡(τ0)ln⁡((2​m−1)/m2)⌉,α¯+1}≥2.\displaystyle p=\max\left\{\left\lceil\frac{\ln(\tau_{0})}{\ln((2m-1)/m^{2})}\right\rceil\!,\ \bar{\alpha}+1\right\}\geq 2.(3.2)

Convolving the scattering data against localized test function kernelsφk​(⋅;m,p)\varphi_{k}(\cdot;m,p)approximately projects these data onto the temporal scalest⪆m​Δ​tt\gtrapprox m\Delta{t}; in particular, as the support radiusm​Δ​t→0m\Delta{t}\rightarrow 0, the weak (WSINDy) formulation in eq. (2.18) collapses to the strong (SINDy) formulation in eq. (2.17). From a distributional perspective, the test functionsφk\varphi_{k}converge to Dirac delta distributionsδ​(tk)\delta(t_{k})while the derivativesφ˙k\dot{\varphi}_{k}converge to centered finite difference kernels. We provisionally setm:=20m:=20throughout. For additional information about our numerical implementation, we refer the reader to Appendix §A.

Our choice of library𝚯​(𝒙)\mathbf{\Theta}(\boldsymbol{x})is motivated by the analytic structure of the scattering ODEs in eq. (2.14). It is convenient to work in terms of(κi,log⁡(ci))(\kappa_{i},\log(c_{i}))rather than, e.g.,(κi,ci)(\kappa_{i},c_{i})or(λi,ci)(\lambda_{i},c_{i}), as the scattering dynamics of the KdV equation become polynomial in these coordinates:κ˙i=0\dot{\kappa}_{i}=0anddd​t​log⁡(ci)=8​β​κi3\tfrac{d}{dt}\log(c_{i})=8\beta\kappa_{i}^{3}. Accordingly, we use a library of low-order (i.e., cubic) monomials inκi\kappa_{i}and inlog⁡(ci)\log(c_{i}),𝚯(𝒙i)={κi,κi2,κi3,log(ci),log(ci)2,log(ci)3}.\mathbf{\Theta}(\boldsymbol{x}_{i})=\big\{\kappa_{i},\,\kappa^{2}_{i},\,\kappa^{3}_{i},\,\log(c_{i}),\,\log(c_{i})^{2},\,\log(c_{i})^{3}\big\}.(3.3)

In order to respect the index-invariant physical symmetry of the system – i.e., that each soliton follows the same physics – we enforce index-invariant ODEs of the formκ˙i=f𝜿​(κi,ci)\dot{\kappa}_{i}=f_{\boldsymbol{\kappa}}(\kappa_{i},c_{i})andc˙i=f𝐜​(κi,ci)\dot{c}_{i}=f_{\mathbf{c}}(\kappa_{i},c_{i}).

## 4Results

## 4.1Validation

To illustrate how the performance of our scheme scales with increasingly noisy data𝐮=𝐮∗+𝜺\mathbf{u}=\mathbf{u}^{*}+\boldsymbol{\varepsilon}, we run repeated trials on corrupted versions of the datasets and report the resulting metrics (see Figure3). Following[Messenger.Bortz2021JournalofComputationalPhysics], we add distinct realizations of artificial i.i.d. noiseε∈𝒩​(0,σε2)\varepsilon\in\mathcal{N}(0,\sigma^{2}_{\!\varepsilon})in a pointwise fashion to each element of𝐔:=𝐮​(𝐭)\mathbf{U}:=\mathbf{u}(\mathbf{t}), which are computed by enforcing a standard deviationσε=σnr​‖𝐔‖F\sigma_{\!\varepsilon}=\sigma_{\textsc{nr}}\|\mathbf{U}\|_{F}so thatσnr=‖𝜺​(𝐭)‖F/‖𝐔‖F\sigma_{\textsc{nr}}=\|\boldsymbol{\varepsilon}(\mathbf{t})\|_{F}/\|\mathbf{U}\|_{F}. We explore noise ratios in the range0≤σnr≤0.50\leq\sigma_{\textsc{nr}}\leq 0.5, i.e., up to50%50\%of the magnitude of the data. To give a sense of the symbolic form of the discovered equations, in Table1we explicitly compare the ground-truth and identified models at zero noise for the synthetically generated KdV data of §4.2. Metrics given below then track how the identified models deform asσnr\sigma_{\textsc{nr}}increases.

To help gauge the quality of the weak-form regression, we report the coefficient of determination corresponding to each identified WSINDy model, which is defined by666TheR2R^{2}metric is unstable for models with small or vanishing coeffs; therefore, we do not report anR2R^{2}value when𝐰^=0\hat{\mathbf{w}}=0(see Figure3).R2:=1−‖𝐛−𝐆​𝐰^‖22‖𝐛−𝐛¯‖22,where𝐛¯:=[1K​d​∑k,i𝐛k,i]​𝟏.\displaystyle R^{2}:=1-\frac{\|\mathbf{b}-\mathbf{G}\hat{\mathbf{w}}\|_{2}^{2}}{\|\mathbf{b}-\overline{\mathbf{b}}\,\|_{2}^{2}},\quad\text{where}\quad\overline{\mathbf{b}}:=\left[\frac{1}{Kd}\sum_{k,i}\mathbf{b}_{k,i}\right]\mathbf{1}.

This metric, which equals the proportion of the variance of𝐛\mathbf{b}that is explained by the identified model𝐆​𝐰^\mathbf{G}\hat{\mathbf{w}}, satisfiesR2≤1R^{2}\leq 1, with values near one indicating an accurate model. We additionally report the pointwise RMSE between the true state𝐔∗\mathbf{U}^{*}and the reconstructed field𝐔IST\mathbf{U}_{\text{IST}}obtained by applying the IST to a forward simulation of the discovered scattering dynamics (see the bottom panel of Figure1),RMSE​(𝐔IST):=1Nx​Nt​‖𝐔∗−𝐔IST‖F,\displaystyle\text{RMSE}(\mathbf{U}_{\text{IST}}):=\frac{1}{\sqrt{N_{\!x}N_{t}}}\big\|\mathbf{U}^{*}-\mathbf{U}_{\text{IST}}\big\|_{F},(4.1)

which quantifies how faithfully the recovered dynamics reproduce the original field. For reflectionless data, the IST admits a convenient closed-form "τ\tau-determinant" representation[Hirota1971PhysRevLett]given byu​(x,t)=−2γ​d2d​x2​log⁡|𝐀​(x;𝜿​(t),𝐜​(t))|,where𝐀i​j​(x;𝜿,𝐜):=δi​j+ci​cj​e−(κi+κj)​xκi+κj,\displaystyle u(x,t)=-\frac{2}{\gamma}\frac{d^{2}}{dx^{2}}\log|\mathbf{A}(x;\boldsymbol{\kappa}(t),\mathbf{c}(t))|,\quad\text{where}\quad\mathbf{A}_{ij}(x;\boldsymbol{\kappa},\mathbf{c}):=\delta_{ij}+\frac{\sqrt{c_{i}c_{\!j}}\,e^{-(\kappa_{i}+\kappa_{j})x}}{\kappa_{i}+\kappa_{j}},

which we use to recover𝐔IST\mathbf{U}_{\text{IST}}from the scattering data(κ^i,c^i)​(t)(\hat{\kappa}_{i},\hat{c}_{i})(t)forecast with the identified models.777Theτ\tau-determinant representation is more numerically convenient than the GLM equation of eq. (2.13), but only applies to reflectionless cases. When forecasting a WSINDy model forward in time, we use an adaptive RK-45 scheme instantiated with the exact initial condition; see Figure4.

The metrics above are model-agnostic and can be computed in every case, including the experimental setting of §4.3. In cases where underlying the model is available, i.e., the synthetic experiments of §4.2, we also compare the identified coefficients against a reference; for unperturbed synthetic data (ϵ=0\epsilon=0) the reference is the exact scattering ODEs of eq. (2.14), while for perturbed synthetic data (ϵ>0\epsilon>0) it is the perturbed scattering ODEs of eq. (2.15). In these cases, we follow[Messenger.Bortz2021JournalofComputationalPhysics]in reporting the normalizedℓ∞\ell^{\infty}coefficient error and the true positive ratio (TPR),888Here,TPdenotes the number of terms that were correctly identified as nonzero,FPdenotes the number of terms that were falsely identified as nonzero, andFNdenotes the number of terms that were falsely identified as zero.respectively defined byE∞:=maxj=1,…,J⁡|wj−wj∗||wj∗|,andTPR:=TPTP+FP+FN.\displaystyle E_{\infty}:=\max_{j=1,\dots,J}\frac{|w_{j}-w^{*}_{j}|}{|w^{*}_{j}|},\quad\text{and}\quad\text{TPR}:=\frac{\text{TP}}{\text{TP}+\text{FP}+\text{FN}}.(4.2)

TheE∞E_{\infty}coefficient error represents maximum element-wise relative error incurred by the discovered model, while the TPR assesses the extent to which the identified models recover the correct terms. Note that a TPR of 1 means that the true model has been discovered in its entirety while a TPR of 0 indicates that none of the correct terms were identified.\TBLTable 1:Results obtained using synthetic, noise-free (σnr=0\sigma_{\textsc{nr}}=0) data sourced from numerical simulations of the perturbed KdV model in eq. (2.5) with the canonical parameters(α,β)=(6,1)(\alpha,\beta)=(6,1). For each configuration, ground-truth reference dynamics are compared against the model identified by WSINDy. The reference equations are given by the exact scattering dynamics of eq. (2.14) for the unperturbed runs (ϵ=0\epsilon=0) and by the near-integrable scattering dynamics of eq. (2.15) for the perturbed runs (ϵ=0.2\epsilon=0.2). Forϵ=0.2\epsilon=0.2, note that13​ϵ≈0.0667\frac{1}{3}\epsilon\approx 0.0667and23​ϵ≈0.1333\frac{2}{3}\epsilon\approx 0.1333\TCHNumber ofsolitons(n)(n)\TCHPerturbation(ϵ)(\epsilon)\TCHForcing(F)(F)\TCHGround truth model\TCHIdentified model(0%(0\%noise)n=1n=1ϵ=0\epsilon=0N/A{κ˙=0,dd​t​log⁡(c)=8​κ3\begin{cases}\dot{\kappa}=0,\\
\frac{d}{dt}\log(c)=8\kappa^{3}\end{cases}{κ˙=0,dd​t​log⁡(c)=7.9981​κ3\begin{cases}\dot{\kappa}={\color[rgb]{.75,0,.25}0},\\
\frac{d}{dt}\log(c)={\color[rgb]{.75,0,.25}7.9981}\kappa^{3}\end{cases}n=2n=2ϵ=0\epsilon=0N/A{κ˙i=0,dd​t​log⁡(ci)=8​κi3\begin{cases}\dot{\kappa}_{i}=0,\\
\dfrac{d}{dt}\log(c_{i})=8\kappa_{i}^{3}\end{cases}{κ˙i=0,dd​t​log⁡(ci)=7.9984​κi3\begin{cases}\dot{\kappa}_{i}={\color[rgb]{.75,0,.25}0},\\
\frac{d}{dt}\log(c_{i})={\color[rgb]{.75,0,.25}7.9984}\kappa_{i}^{3}\end{cases}n=1n=1ϵ=0.2\epsilon=0.2F​[u]=(x​u)xF[u]=(xu)_{x}{κ˙=13​ϵ​κ+O​(ϵ2),dd​t​log⁡(c)=8​κ3−23​ϵ​log⁡(c)+O​(ϵ2)\begin{cases}\dot{\kappa}=\frac{1}{3}\epsilon\kappa+O(\epsilon^{2}),\\
\frac{d}{dt}\log(c)=8\kappa^{3}-\frac{2}{3}\epsilon\log(c)+O(\epsilon^{2})\end{cases}{κ˙=0.0666​κ,dd​t​log⁡(c)=8.0072​κ3−0.1336​log⁡(c)\begin{cases}\dot{\kappa}={\color[rgb]{.75,0,.25}0.0666}\kappa,\\
\frac{d}{dt}\log(c)={\color[rgb]{.75,0,.25}8.0072}\kappa^{3}{\color[rgb]{.75,0,.25}-0.1336}\log(c)\end{cases}n=2n=2ϵ=0.2\epsilon=0.2F​[u]=(x​u)xF[u]=(xu)_{x}{κ˙i=13​ϵ​κi+O​(ϵ2),dd​t​log⁡(ci)=8​κi3−23​ϵ​log⁡(ci)+O​(ϵ2)\begin{cases}\dot{\kappa}_{i}=\frac{1}{3}\epsilon\kappa_{i}+O(\epsilon^{2}),\\
\frac{d}{dt}\log(c_{i})=8\kappa^{3}_{i}-\frac{2}{3}\epsilon\log(c_{i})+O(\epsilon^{2})\end{cases}{κ˙i=0.0660​κi,dd​t​log⁡(ci)=8.0192​κi3−0.1364​log⁡(ci)\begin{cases}\dot{\kappa}_{i}={\color[rgb]{.75,0,.25}0.0660}\kappa_{i},\\
\frac{d}{dt}\log(c_{i})={\color[rgb]{.75,0,.25}8.0192}\kappa^{3}_{i}{\color[rgb]{.75,0,.25}-0.1364}\log(c_{i})\end{cases}\botruleFigure 2:[Top panel] Visualizing one of three sets of numerical simulations used to generate synthetic data, which each follow the evolution of one or two solitons evolving under the perturbed KdV equation in eq. (2.5), pictured at20%20\%noise withκ=2\kappa=2and(κ1,κ2)=(2.4,1.2)(\kappa_{1},\kappa_{2})=(2.4,1.2)in the left and right panels, respectively. [Bottom panel] Snapshots of the double-soliton simulations evolving in time

## 4.2Synthetic Data

We consider several examples using synthetic data sourced from numerical simulations of the perturbed KdV equation given in eq. (2.5). In particular, we explore configurations featuring either one or two solitons (see Figure2) and investigate both the unperturbed (ϵ=0\epsilon=0) and perturbed cases (ϵ=0.2\epsilon=0.2) subject to a mass-conserving forcing function,F​[u]=(x​u)xF[u]=(xu)_{x}, for which the reference ODEs in eq. (2.15) can be explicitly computed (see Table1). In each instance, we use the canonical KdV parametersα=6\alpha=6andβ=1\beta=1. The numerical simulations are computed on the domainx∈Ω=[−25,25]x\in\Omega=[-25,25]usingN=210N=2^{10}uniformly-spaced nodes and adaptively integrated fort∈[0,1.5]t\in[0,1.5]using a pseudo-spectral solver from the open-sourcesangkuriang-ideal[Irawan.etal2026]Python package withM=200M=200saved snapshots.999This package does not natively support perturbations, so for the perturbed cases we use a slightly hand-modified version of the original code.Figure 3:Illustrating how the validation metrics of §4.1scale with increasing noise for each of the four configurations of synthetic data. The noise ratioσnr\sigma_{\textsc{nr}}is swept from0to0.50.5in increments ofΔ​σnr=0.0125\Delta\sigma_{\textsc{nr}}=0.0125using1515distinct realizations per nonzero noise level; solid lines denote sample means while the shaded bands denote±1\pm 1standard deviation. [Top-left]R2R^{2}values for the identified norming constant models, with an inset corresponding to the scattering parameter models; as per §4.1, we omitR2R^{2}values for runs in which the zero model𝐰^=0\hat{\mathbf{w}}=0was selected. The TPR [top-right], coefficient error [bottom-right], and IST reconstruction error [bottom-left] are computed via eqns. (4.2) and (4.1)

In the unperturbed case, the scattering parametersκi\kappa_{i}are conserved quantities (i.e.,κ˙i=0\dot{\kappa}_{i}=0), meaning that any single simulation samples only a constant value for each parameter. Consequently, the candidate monomialsκi,κi2,κi3\kappa_{i},\,\kappa_{i}^{2},\,\kappa_{i}^{3}in the WSINDy library of eq. (3.3) are linearly dependent along the trajectory, and the regression problem in eq. (3.1) becomes ill-posed. To account for this degeneracy, we stack scattering data𝐗r\mathbf{X}_{r}from three distinct simulationsr=1,2,3r=1,2,3(the minimum number required for well-posedness) and concatenate each respective weak-form linear system from eq. (2.19) into a single block-regression. This is motivated by the nature of the experimental dataset of[Heinrich.etal2025]investigated in §4.3below, which includes several (25) distinct experimental runs. Each simulation is initialized using sech-squared profilesu0​(x)=∑i=1n2​κi2​sech2​(κi​(x−xi))u_{0}(x)=\sum_{i=1}^{n}2\kappa^{2}_{i}\text{sech}^{2}(\kappa_{i}(x-x_{i}))parameterized by a distinct set of scattering parametersκi\kappa_{i}and initial positionsxj:=5​(j−5)x_{j}:=5(j-5). For the single soliton examples in whichn=1n=1, we varyκ∈{2,2.2,2.4},\kappa\in\{2,2.2,2.4\},while for the two-soliton cases withn=2n=2, we instead use(κ1,κ2)∈{(2,1.8),(2.2,1.4),(2.4,1.2)}(\kappa_{1},\kappa_{2})\in\{(2,1.8),(2.2,1.4),(2.4,1.2)\}; theκ=2\kappa=2and(κ1,κ2)=(2.4,1.2)(\kappa_{1},\kappa_{2})=(2.4,1.2)cases are shown in Figure2. Finally, because the unperturbed dynamics obey a trivial conservation law of the form𝜿˙=0\dot{\boldsymbol{\kappa}}=0, we extend the standard MSTLS of Algorithm1to the zero-admissible formulation given in Algorithm2, which uses BIC-based hypothesis testing to allow WSINDy to select model coefficients with empty support.

As reported in Table1, the recovered coefficients agree with both the exact scattering ODEs and the leading-order perturbation theory to within a fraction of a percent at zero noise; e.g., in the perturbed single soliton example, WSINDy estimatesκ˙≈0.0667​κ\dot{\kappa}\approx 0.0667\kappaversus the ground-truth ofκ˙=13​ϵ​κ≈0.0666​κ\dot{\kappa}=\tfrac{1}{3}\epsilon\kappa\approx 0.0666\kappa. In turn, Figure3tracks how the model identification results deform as the noise ratioσnr\sigma_{\textsc{nr}}increases, revealing a few consistent trends. In particular, the weak-form regression for thelog⁡(𝐜)\log(\mathbf{c})models stays robust across the entire noise range – theR2R^{2}for these ODEs remains above∼0.96\sim\!0.96for three of the four configurations and declines only mildly to∼0.88\sim\!0.88for the weakest (i.e., unperturbed single-soliton) case at50%50\%noise. By contrast, theR2R^{2}values decay rapidly for the perturbed𝜿˙\dot{\boldsymbol{\kappa}}equations, which feature small𝒪​(ϵ)\mathcal{O}(\epsilon)coefficients. Mechanistically, beyond∼15%\sim\!15\%background noise this perturbation becomes indistinguishable from a conservation law of the formκ˙=0\dot{\kappa}=0, at which point the BIC test in Algorithm2selects the zero model𝐰^=0\hat{\mathbf{w}}=0and a correspondingR2R^{2}value is no longer reported.

Although theR2R^{2}eventually becomes unstable for the perturbed cases featuring small coefficients, the correct model terms are nonetheless reliably recovered: the mean TPR stays above∼0.7\sim\!0.7at all noise levels for each of the four configurations, while the unperturbed two-soliton example in particular retains a TPR of exactly one until∼45%\sim\!45\%noise. In a similar vein, theE∞E_{\infty}coefficient error remains𝒪​(1e-3)\mathcal{O}(\texttt{1e-3})across nearly the entire noise range in the unperturbed two-soliton case, rising only beyondσnr≈0.45\sigma_{\textsc{nr}}\approx 0.45. By contrast, in the single-soliton and perturbed cases, theE∞E_{\infty}coefficient error plateaus near𝒪​(1e-1)\mathcal{O}(\texttt{1e-1}), again reflecting the difficulty of resolving the small perturbative coefficients. Moreover, occasional sharp oscillatory peaks are present in several cases – features which we predominantly attribute to sampling error. Lastly, we observe that the reconstruction RMSE, a proxy for the predictive fidelity of the identified models, grows monotonically withσnr\sigma_{\textsc{nr}}in every case. Unsurprisingly, the most dynamically complex configuration (i.e., the perturbed two-soliton collision) tends to incur the largest reconstruction error.

## 4.3Empirical Data

In this section, we illustrate the discovery of effective soliton dynamics using real experimental data. Specifically, we consider data from a recent study by Heinrich et al.[Heinrich.etal2025,Heinrich.etal2026]in which a Kawahara-type PDE was identified from video recordings of solitary shallow-water waves propagating down a flume apparatus (see Figure4). In this study, the edge-detection algorithm of[Canny1986IEEETransPatternAnalMachIntell]was used to extract a nondimensionalized101010The rescaling isu∗,x∗,t∗↦h​u,h​x,h/g​tu^{*}\!,x^{*}\!,t^{*}\mapsto hu,hx,\sqrt{h/g}t, whereu∗,x∗,t∗u^{*}\!,x^{*}\!,t^{*}are the measured dimensional quantities andh≈32h\approx 32mm is the water depth.surface fielduk​(x,t)u_{k}(x,t)for each ofk=1,…,25k=1,\dots,25distinct experimental trials,1818of which were subsequently concatenated into a single data-matrix𝐔\mathbf{U}(cf. §4.2above). The authors then applied two distinct equation-learning methodologies to the data – WSINDy and a novel "Fourier multiplier" method[Heinrich.etal2025]– both of which independently selected a sparse model of the formut+v0​ux+α​u​ux+β​ux​x​x=ϵ​ux​x​x​x​x.u_{t}+v_{0}u_{x}+\alpha uu_{x}+\beta u_{xxx}=\epsilon u_{xxxxx}.(4.3)

Moreover, similar coefficient values were estimated by each method (e.g.,ϵ≈−0.06\epsilon\approx-0.06from both methods). In a moving frame of referenceξ=x−v0​t\xi=x-v_{0}t, this model is equivalent to the Kawahara model in eq. (2.6),ut+α​u​uξ+β​uξ​ξ​ξ=ϵ​uξ​ξ​ξ​ξ​ξ.\displaystyle u_{t}+\alpha uu_{\xi}+\beta u_{\xi\xi\xi}=\epsilon u_{\xi\xi\xi\xi\xi}.

To validate the discovered model, the authors of[Heinrich.etal2025]numerically integrated eq. (4.3) forward in time and compared the predicted field to the measured soliton surface heights from each of the seven held-out experimental trials, achieving errors of just44-6%6\%relative to the wave amplitudes.

Note that, for our purposes here, we apply two additional lightweight preprocessing steps to the data: (1) a small number of spike artifacts were repaired via local temporal averaging; (2) we subtracted a small offset from the water levelu↦u−u¯u\mapsto u-\bar{u}, whereu¯∼0.02\bar{u}\sim 0.02–0.130.13mm, so thatu→0u\rightarrow 0asx→∂⁡Ωx\rightarrow\operatorname{\partial}\!\Omega. Just as in[Heinrich.etal2026], each run is sampled overNx=1200N_{x}=1200points in space (Δ​x≈0.29\Delta{x}\approx 0.29mm) andNt=151N_{t}=151frames in time (Δ​t=0.02\Delta{t}=0.02s). In each case, we isolate a specific temporal window in which the soliton stays solidly in-frame, which we then temporally super-sample via cubic-spline interpolation before computing the scattering data (see Figure4). We estimate that the experimental noise level is roughlyσnr≈1.4%\sigma_{\textsc{nr}}\approx 1.4\%, comfortably within the regime in which WSINDy provides reliable model estimates (cf. §4.2).\TBLTable 2:The models identified from the experimental data of[Heinrich.etal2025,Heinrich.etal2026]. Here, we report the RMSE of eq. (4.1) normalized to the peak amplitudeA:=max⁡|u|A:=\max|u|and averaged over the seven validation trials\TCHIdentified model\TCHLibrary\TCHRMSE\TCHR2R^{2}{κ˙=0,dd​t​log⁡(c)=3.46​κ+2.60​κ3+0.20​log⁡(c)\begin{cases}\dot{\kappa}={\color[rgb]{.75,0,.25}0},\\
\tfrac{d}{dt}\log(c)={\color[rgb]{.75,0,.25}3.46}\kappa+{\color[rgb]{.75,0,.25}2.60}\kappa^{3}+{\color[rgb]{.75,0,.25}0.20}\log(c)\end{cases}{{1}∪{κp,log(c)p}1≤p≤3,{1,κ,κ3}∪{log(c)p}1≤p≤3,\begin{cases}\{1\}\cup\{\kappa^{p},\log(c)^{p}\}_{1\leq p\leq 3},\\
\{1,\kappa,\kappa^{3}\}\cup\{\log(c)^{p}\}_{1\leq p\leq 3},\end{cases}17.6%0.803\botrule

Figure 4:[Top-left] Example snapshots from the experimental dataset of[Heinrich.etal2025,Heinrich.etal2026]. [Top-right] The selected temporal window for one trial in which the soliton sits solidly in-frame, showing the extracted profiles (red) overlaid on the measured fieldu=u​(x,t)u=u(x,t). [Bottom] Visualizing, for one held-out validation trial, the measured field, the reconstruction obtained by forward-integrating the WSINDy-discovered scattering dynamics and applying the IST, and the corresponding pointwise error

For each equation listed in Table2, we use a candidate library inspired both by the identified PDE model in eq. (4.3) and by the empirical amplitude–phase-velocity relationv2≈1+Av^{2}\approx 1+Areported in[Heinrich.etal2025],111111See Figure 9 therein.whereA:=max⁡|u​(x,t)|A:=\max|u(x,t)|andv:=|x˙|v:=|\dot{x}|respectively denote the nondimensionalized amplitude and phase velocity of the traveling water wave (see Figure5). In particular, a single exact KdV soliton satisfieslog⁡(c)=2​κ​ξ+log⁡(2​κ)\log(c)=2\kappa\xi+\log(2\kappa)in a co-moving frame of referenceξ​(t)=ξ0+4​β​κ2​t\xi(t)=\xi_{0}+4\beta\kappa^{2}t(cf. eq. (2.14)); however, a stationary observer (i.e., in the lab framex=ξ+v0​tx=\xi+v_{0}t) would measure an additional advective force,dd​t​log⁡(c)=2​κ​v=2​v0​κ+8​β​κ3.\displaystyle\tfrac{d}{dt}\log(c)=2\kappa{v}=2v_{0}\kappa+8\beta\kappa^{3}.(4.4)

Inserting an expansion of the empirical relationv≈1+A=1+(1/2)​A+𝒪​(A2)v\approx\sqrt{1+A}=1+(1/2)A+\mathcal{O}(A^{2})into eq. (4.4) and using the exact soliton amplitudeA​(κ)=−(2/γ)​κ2=12​(β/α)​κ2A(\kappa)=-(2/\gamma)\kappa^{2}=12(\beta/\alpha)\kappa^{2}independently yieldsdd​t​log⁡(c)=2​v​κ≈2​κ​(1+6​βα​κ2+𝒪​(κ4))=2​κ+12​βα​κ3+𝒪​(κ5).\displaystyle\tfrac{d}{dt}\log(c)=2v\kappa\approx 2\kappa\left(1+\tfrac{6\beta}{\alpha}\kappa^{2}+\mathcal{O}(\kappa^{4})\right)=2\kappa+\tfrac{12\beta}{\alpha}\kappa^{3}+\mathcal{O}\big(\kappa^{5}\big).(4.5)

Consistency between the idealized and empirical ODEs in eqs. (4.4) and (4.5) requires that bothv0=1v_{0}=1(empirically,v0≈1.2v_{0}\approx 1.2) and8​β=12​(β/α)8\beta=12(\beta/\alpha), which occurs if and only ifα=3/2\alpha=3/2(α≈1.4\alpha\approx 1.4and8​β≈58\beta\approx 5). Therefore, the observedv2≈1+Av^{2}\approx 1+Arelationship may be viewed as a restatement of the ODE in eq. (4.5). Guided by this structure, we use a candidate library based on the odd powers{κ,κ3}\{\kappa,\kappa^{3}\}, where we interpret the linear term as capturing advection and the cubic term as capturing the soliton’s nonlinear evolution, together with low-order powers oflog⁡(c)\log(c)(see Table2). Although the identified Kawahara-type PDE is translation-invariant, our hope is that the latter terms allow us to absorb any residual position-dependence introduced by the experimental or numerical setup rather than by the physical dynamics.121212Recall thatlog⁡(c)\log(c)is highly correlated with the soliton positionξ\xi.Figure 5:A reproduction of Figure 9 from Ref.[Heinrich.etal2025], which illustrates an empirical amplitude–phase velocity relation obeyed by the shallow-water waves. Here, the dimensional amplitudesA∗:=max⁡|h​u∗|A^{*}:=\max|hu^{*}|are plotted against the phase-velocityv∗:=|x˙|/g​hv^{*}:=|\dot{x}|/\sqrt{gh}for the1818training and77validation trials, showing the validity of the empirical relation. Note that the first two terms in the identifieddd​t​log⁡(c)\tfrac{d}{dt}\log(c)model listed in Table2are consistent with first two terms of a Taylor series expansion of the nondimensionalizedv≈1+Av\approx\sqrt{1+A}relationship; see §4.3

Using the setup described above, WSINDy selects the conservation lawκ˙=0\dot{\kappa}=0together with a model fordd​t​log⁡(c)\tfrac{d}{dt}\log(c)that is consistent with the form of the cubic expansion given in eq. (4.4), with the exception of an additional smalllog⁡(c)\log(c)term reminiscent of the perturbed scattering ODEs from Table1above. We emphasize, however, that we do not realistically expect the additionallog⁡(c)\log(c)term to play an active role in the physical dynamics – instead, we attribute its existence to experimental and numerical artifacts, and note that it likely skews the relative magnitudes of the identified coefficients (cf. eq. (4.4)). Forward integration of the discovered scattering dynamics and subsequent reconstruction of the water-line via the IST yields an amplitude-normalized RMSE of88–27%27\%(or∼18%\sim\!18\%on average; see Table2) across the seven held-out trials (cf. Figure4). In each case exhibiting large RMSE, the reconstruction errors are predominantly caused by a secondary wave trailing behind the main soliton (i.e., additional radiation), which the reflectionless IST is not capable of representing.

## 4.4A Note on Identifiability

We conclude the results section with a few brief remarks on the identifiability of nonlinear dynamics from solitary wave trajectories. Rudy et al.[Rudy.etal2017SciAdv]observed that when SINDy-based methods are applied to measurements of a single soliton evolving along a single trajectory, they tend to recover trivial linear transport equations in place of any underlying nonlinear wave dynamics.131313As in §4.2, this problem can be avoided by stacking trajectories – for example, Heinrich et al.[Heinrich.etal2025]use 18 distinct single soliton trajectories.Interestingly, this behavior represents an inherent feature of the data, rather than a deficiency of the SINDy architecture; i.e., every lone KdV solitonexactlysolves a corresponding linear transport equation,u​(x,t)=2​κ2​sech2​(κ​(x−x0−4​κ2​t))solves both:{ut+4​κ2​ux=0,ut+6​u​ux+ux​x​x=0.\displaystyle u(x,t)=2\kappa^{2}\,\text{sech}^{2}\!\big(\kappa\big(x-x_{0}-4\kappa^{2}t\big)\big)\quad\text{solves both:}\quad\begin{cases}u_{t}+4\kappa^{2}u_{x}=0,\\
u_{t}+6uu_{x}+u_{xxx}=0.\end{cases}(4.6)

Since both candidate models in eq. (4.6) reproduce the data exactly, a sparse-regression architecture naturally selects the simpler one – in this case, the transport equation is a more parsimonious model than the KdV equation. Physically speaking, nonlinearity manifests itself in the KdV equation via the dependence of wave-speeds on wave-amplitudes, and no such dependence can be observed from a soliton in isolation. Conversely, nonlinearities can be identified by, e.g., observing a two-soliton interaction or, more generally, a collection of solitons of differing amplitudes[Rudy.etal2017SciAdv]. A closely-related identifiability issue was subsequently reported by Vasey et al.[Vasey.etal2025JournalofComputationalPhysics]in the setting of magnetohydrodynamic blast waves.

Working with scattering data(κi,ci)​(t)(\kappa_{i},c_{i})(t)instead of field datau​(x,t)u(x,t)does not fundamentally remove the degeneracy described above, although it does change the nature of the identifiability problem in an interesting and potentially useful way – in particular, the scattering ODEs in eqs. (2.14) and (2.15) are nonlinear inκi\kappa_{i}, regardless of the number of solitons present in the data. However, in analogy with eq. (4.6), eachκi​(t)=κi​(0)\kappa_{i}(t)=\kappa_{i}(0)is conserved and thus constant in the absence of an external perturbation; consequently, the candidate monomials{κi,κi2,κi3}\{\kappa_{i},\,\kappa^{2}_{i},\,\kappa^{3}_{i}\}in the library of eq. (3.3) are nearly collinear along a single trajectory, and linear regression cannot uniquely determine which monomial governs the evolution oflog⁡(ci)\log(c_{i}). It is important to recognize that the collinearity of theκip\kappa^{p}_{i}is the manifestation, observed at the level of the scattering data, of the very same mechanism responsible for the spurious transport equation observed at the PDE level. That being said, the nature of this degeneracy does become more benign in the scattering coordinates – the recovered model never collapses onto a structurally distinct equation. The conservation lawsκ˙i=0\dot{\kappa}_{i}=0and the linear-in-time growth oflog⁡(ci)\log(c_{i})can still be identified, and only the exponents of thedd​t​log⁡(ci)=κip\tfrac{d}{dt}\log(c_{i})=\kappa^{p}_{i}models remain unknown. As noted above, the identifiability problem dissolves as the data either begin to feature either more than one soliton or more than one trajectory, the latter of which is a phenomenon that has been observed in settings as diverse as network dynamics[Tian.etal2026].

To concretely illustrate the above points, we observe that applying WSINDy for PDEs[Messenger.Bortz2021JournalofComputationalPhysics]to just the first experimental training dataset from[Heinrich.etal2026]yields the transport equationut≈1.2​uxu_{t}\approx 1.2u_{x}withR2≈0.99R^{2}\approx 0.99. Interestingly, when using the scale-invariant preconditioning method described in[Messenger.etal2024SciRep], WSINDy instead identifies a nonlinear PDE of the formut≈−0.0​u+0.1​u2+0.9​ux+0.8​(u2)xu_{t}\approx-0.0u+0.1u^{2}+0.9u_{x}+0.8(u^{2})_{x}where againR2≈0.99R^{2}\approx 0.99, indicating that scaling becomes particularly important when attempting to recover such nonlinearities.141414We note that additional radiation content in the experimental data may also have aided in the identification of the nonlinear(u2)x(u^{2})_{x}term.In a similar vein, regressing the scattering data against a simple polynomial library of the form{κ,κ2,κ3}\{\kappa,\kappa^{2},\kappa^{3}\}(evaluated over the same experimental trial data) yields an advective law of the formdd​t​log⁡(c)≈−2​κ,\tfrac{d}{dt}\log(c)\approx-2\kappa,irrespective of whether the library columns are rescaled. In this case,κ​(t)≈2/3\kappa(t)\approx 2/3is nearly constant along the trajectory, and the identified model is almost indistinguishable from both−3​κ2-3\kappa^{2}and−5​κ3-5\kappa^{3}.

## 5Discussion

In this paper, we have proposed and investigated a data-driven method for modeling effective soliton dynamics that works directly with scattering data. In particular, this technique combines the conceptual framework of the IST[Ablowitz.etal1974StudApplMath]with the weak-form equation-learning paradigm of WSINDy[Messenger.Bortz2021MultiscaleModelSimul]to identify interpretable symbolic models without requiring prior knowledge of the form of the scattering equations. Parameterizing a scalar fielduuvia its scattering data(κi,ci)(\kappa_{i},c_{i})is natural in the context of near-integrable wave equations and inherits a large body of analytical structure from existing theory, e.g., the fact that unperturbed KdV scattering dynamics take a convenient polynomial form in(κi,log⁡(ci))(\kappa_{i},\log(c_{i}))coordinates. We have focused on shallow-water models of KdV-type and demonstrated that for this class of governing equations, the technique reliably recovers both the exact unperturbed scattering ODEs as well as the leading-order corrections predicted by the perturbation theory[Karpman.Solovev1981PhysicaDNonlinearPhenomena].

Our numerical experiments indicate that the inferred scattering dynamics are robust to low amounts of additive i.i.d. Gaussian measurement noise, both in unperturbed and perturbed regimes. On synthetic data, the recovered coefficients agree with the exact and perturbed scattering ODEs to within a fraction of a percent at0%0\%noise, and thedd​t​log⁡(𝐜)\tfrac{d}{dt}\log(\mathbf{c})models remain accurate (i.e.,R2≳0.96R^{2}\gtrsim 0.96in three of four cases)
across the entire0–50%50\%noise range tested. Unsurprisingly, the small𝒪​(ϵ)\mathcal{O}(\epsilon)corrections to the𝜿˙\dot{\boldsymbol{\kappa}}equations are harder to resolve in the presence of measurement noise; beyondσnr≳0.15\sigma_{\textsc{nr}}\gtrsim 0.15, these data become statistically indistinguishable from the conservation law𝜿˙=0\dot{\boldsymbol{\kappa}}=0and the BIC test of Algorithm2defaults to the zero model. When applied to the experimental shallow-water wave dataset of Heinrich et al.[Heinrich.etal2025,Heinrich.etal2026], the method recoversκ˙=0\dot{\kappa}=0together with add​t​log⁡(c)\tfrac{d}{dt}\log(c)model consistent with a cubic expansion of the empirical amplitude–phase-velocity relationship reported therein; forward-integration of the recovered dynamics and a subsequent IST reconstruction(κ,log⁡(c))↦u(\kappa,\log(c))\mapsto uyields an amplitude-normalized RMSE of∼18%\sim\!18\%, with the largest errors stemming from the existence of excess radiation trailing the main wave.

Notably, numerical experiments that featured a single, unperturbed soliton consistently saw worse performance than their two-soliton counterparts across each validation metric (R2R^{2},E∞E_{\infty}, RMSE, TPR), despite the fact that these cases are significantly simpler from a dynamical perspective. We attribute this somewhat counterintuitive result to a structural identifiability mechanism similar to that observed in both the KdV and magnetohydrodynamic settings of[Rudy.etal2017SciAdv]and[Vasey.etal2025JournalofComputationalPhysics], in which solitary waves measured along a single trajectory were found to obey advection equations that were much simpler than the expected underlying nonlinear dynamics. Although working with scattering data does not fundamentally remove this degeneracy, it does change the nature of the identifiability problem in a convenient way – while lone solitons exactly obey linear dynamics at the PDE level, the ODEs governing their scattering data are, by contrast, inherently nonlinear inκi\kappa_{i}regardless of the number of solitons present. In the scattering formulation, this degeneracy enters only at a more benign numerical conditioning level, with constantκi\kappa_{i}values rendering the candidate monomialsκip\kappa^{p}_{i}collinear. Moreover, this ill-conditioning is avoided in perturbed regimes where theκi\kappa_{i}are non-constant, and in these cases the identified𝒪​(ϵ)\mathcal{O}(\epsilon)corrections conceivably allow one to back out a set of consistent forms for the forcing termF​[u]F[u].

Although we have focused here on shallow-water equations of KdV-type, a similar pipeline applies, in principle, to any PDE admitting a Lax-pair representation (e.g., any integrable wave equation from[Ablowitz.etal1974StudApplMath]).
Practically speaking, extending the framework discussed here to a new integrable system would require three main ingredients:
- 1.

the Lax operator corresponding to the PDE in question;
- 2.

a numerical DST scheme for the associated EVP;
- 3.

a choice of coordinates in which the scattering dynamics can be reasonably well-approximated by a low-order library of candidate terms.

Applying this pipeline to the focusing nonlinear Schrödinger equation would be a natural next step, subject to the caveat that a treatment of this equation would introduce additional difficulties that haven’t been considered herein. In particular, rather than the self-adjoint EVP considered above, its scattering data are defined in terms of a non-self-adjoint EVP (i.e., the2×22\!\times\!2Zakharov-Shabat system) that has a fundamentally complex-valued point spectrum featuring non-trivial realandimaginary components. Additionally, addressing the defocusing regime (in which dark solitons sit atop a nonzero background), would require developing a strategy for relaxing the assumption of decay asx→∞x\rightarrow\infty.

We conclude by considering a few natural extensions of the current work. In addition to addressing other integrable PDEs and more straightforward methodological improvements such as an end-to-end data-driven pipeline utilizing WSINDy[Messenger.Bortz2021JournalofComputationalPhysics]and SILO[Adriazola.etal2026SIAMJApplDynSyst], one could consider accommodating nonzero radiation (i.e.,R≠0R\neq 0) by appending reflection coefficients to the state vector as outlined in §3.1. This would generalize the modeling technique to non-solitonic settings and, seeing as how excess radiation was the dominant source of reconstruction error in our experimental results, would likely increase the predictive capacity of the discovered models. From a more theoretical perspective, the inclusion of radiation might also lead one to considerpurely dispersiveregimes in which𝐜=0\mathbf{c}=0whileR≠0R\neq 0, including connecting the long-time asymptotics of such systems to Painlevé-type equations[ablowitzSolitonsNonlinearEvolution1991]. Lastly, we expect that it would be interesting and potentially fruitful to explore geophysical modeling applications related to, e.g., internal ocean waves, coastal shoaling waves, and morning-glory waves – settings where coherent nonlinear wave phenomena are ubiquitous and high-resolution field data are becoming increasingly available[elDispersiveShockWaves2016,Lee.etal2024PLoSONE].Algorithm 1Modified Sequential Thresholding Least Squares (MSTLS)

Inputs:response vector𝐛\mathbf{b}(sizeKK), library matrix𝐆\mathbf{G}(sizeK×JK\times J), thresholding parameterλ∈(0,1)\lambda\in(0,1).

Outputs:thresholded weights𝐰λ\mathbf{w}^{\lambda}(sizeJJ).


- 1.

n←0n\leftarrow 0
- 2.

𝐰0←𝐰ls\mathbf{w}^{0}\leftarrow\mathbf{w}_{\textsc{ls}}
- 3.

stopping_criterion←false\texttt{stopping\_criterion}\leftarrow\texttt{false}
- 4.

forj=1,…,Jj=1,\dots,Jdo:
- •

Lj←max⁡(1,‖𝐛‖2/‖𝐆j‖2)L_{j}\leftarrow\max\big(1,\,\|\mathbf{b}\|_{2}/\|\mathbf{G}_{j}\|_{2}\big)
- •

Uj←min⁡(1,‖𝐛‖2/‖𝐆j‖2)U_{j}\leftarrow\min\big(1,\,\|\mathbf{b}\|_{2}/\|\mathbf{G}_{j}\|_{2}\big)
- 5.

whilestopping_criterion == falsedo:
- •

ℐn←{1≤j≤J:|𝐰jn|∈[λ​Lj,λ−1​Uj]}\mathcal{I}_{n}\leftarrow\big\{1\leq j\leq J\,:\,|\mathbf{w}^{n}_{j}|\in[\lambda L_{j},\,\lambda^{-1}U_{j}]\big\}
- •

𝐰n+1←arg​minsupp​(𝐰)⊆ℐn⁡‖𝐛−𝐆𝐰‖22\mathbf{w}_{n+1}\,\leftarrow\ \text{arg}\!\min_{\text{supp}(\mathbf{w})\subseteq\mathcal{I}_{n}}\|\mathbf{b}-\mathbf{Gw}\|^{2}_{2}
- •

ifn≥1n\geq 1andℐn=ℐn−1\mathcal{I}_{n}=\mathcal{I}_{n-1}:
- ∘\circ

stopping_criterion←true\texttt{stopping\_criterion}\leftarrow\texttt{true}
- ∘\circ

𝐰λ←𝐰n+1\mathbf{w}^{\lambda}\leftarrow\mathbf{w}_{n+1}
- •

n←n+1n\leftarrow n+1

## Appendix AThe MSTLS Algorithm

We use a zero-admissible extension of the Modified Sequential Thresholding Least Squares (MSTLS) algorithm developed in[Messenger.Bortz2021JournalofComputationalPhysics]to approximately solve the sparse regression problem posed in eq. (2.20).In MSTLS, a sparse vector of model weights𝐰^i∈ℝJ\hat{\mathbf{w}}_{i}\in\mathbb{R}^{J}with‖𝐰^i‖0≪J\|\hat{\mathbf{w}}_{i}\|_{0}\ll Jfor eachi=1,…,di=1,\dots,dis obtained by minimizing a normalized version of the loss function given in eq. (2.20) over a finite set ofthresholding parameters𝝀:={λl:l=1,…,Nλ}⊂(0,1)\boldsymbol{\lambda}:=\{\lambda_{l}:l=1,\dots,N_{\lambda}\}\subset(0,1).In particular, the model weights are explicitly given by𝐰^imstls:=MSTLS​(𝐛i,𝐆,λ⋆),withλ∗:=min⁡[argminλ∈𝝀ℒmstls​(λ)],\displaystyle\hat{\mathbf{w}}^{\textsc{mstls}}_{i}:=\texttt{MSTLS}\big(\mathbf{b}_{i},\,\mathbf{G},\,\lambda^{\star}\big),\quad\text{with}\quad\lambda^{*}:=\min\left[\operatorname*{argmin}_{\lambda\in\boldsymbol{\lambda}}\,\mathcal{L}_{\textsc{mstls}}(\lambda)\right],(A.1)

whereMSTLSdenotes the output of Algorithm1. For a given thresholding parameterλ∈(0,1)\lambda\in(0,1), the loss functionℒmstls\mathcal{L}_{\textsc{mstls}}is defined asℒmstls​(λ):=ℒμ​(𝐰iλ;𝐛ils‖𝐛ils‖2,𝐆‖𝐛ils‖2),withμ:=1J,\displaystyle\mathcal{L}_{\textsc{mstls}}(\lambda):=\mathcal{L}_{\mu}\!\left(\mathbf{w}^{\lambda}_{i};\,\frac{\mathbf{b}_{i}^{\textsc{ls}}}{\|\mathbf{b}_{i}^{\textsc{ls}}\|_{2}},\,\frac{\mathbf{G}}{\|\mathbf{b}_{i}^{\textsc{ls}}\|_{2}}\right),\quad\text{with}\quad\mu:=\frac{1}{J},

where𝐛ils:=𝐆𝐰ils\mathbf{b}^{\textsc{ls}}_{i}:=\mathbf{G}\mathbf{w}^{\textsc{ls}}_{i}is the projection of the ordinary least-squares estimate given by𝐰ils:=(𝐆T​𝐆)−1​𝐆T​𝐛i.\displaystyle\mathbf{w}^{\textsc{ls}}_{i}:=\big(\mathbf{G}^{T}\mathbf{G}\big)^{-1}\mathbf{G}^{T}\mathbf{b}_{i}.

Here, the quantity𝐰iλ:=MSTLS​(𝐛i,𝐆,λ)\mathbf{w}^{\lambda}_{i}:=\texttt{MSTLS}(\mathbf{b}_{i},\mathbf{G},\lambda)denotes the vector ofλ\lambda-thresholded weights, which at every iteration satisfies the following dominant balance relationship:‖wj​iλ​𝐆j‖2‖𝐛i‖2∈[λ,λ−1],for eachj=1,…,J.\displaystyle\frac{\|w^{\lambda}_{\!ji}\mathbf{G}_{j}\|_{2}}{\|\mathbf{b}_{i}\|_{2}}\in\big[\lambda,\,\lambda^{-1}\big],\quad\text{for each}\quad j=1,\dots,J.

We follow[Messenger.Bortz2021JournalofComputationalPhysics]in scanning over a set ofNλ=50N_{\lambda}=50candidate values𝝀:={λl}l=150\boldsymbol{\lambda}:=\{\lambda_{l}\}^{50}_{l=1}defined by uniformly log-spaced incrementslog10⁡(λl)∈(−4,0)\log_{10}(\lambda_{l})\in(-4,0)with the exception of the perturbedlog⁡(c)\log(c)cases in §4.2and §4.3, for which we found it helpful to hand-tune theλ∗\lambda^{*}parameter to4e-2and1e-1, respectively.Algorithm 2MSTLS with BIC Testing for Trivial Dynamics

Inputs:response vector𝐛\mathbf{b}(sizeKK), library matrix𝐆\mathbf{G}(sizeK×JK\times J), thresholding parameters𝝀={λl}l=1Nλ\boldsymbol{\lambda}=\{\lambda_{l}\}_{l=1}^{N_{\lambda}}.

Outputs:BIC-tested weights𝐰^\hat{\mathbf{w}}(sizeJJ).


- 1.

λ∗←min⁡[argminλ∈𝝀ℒmstls​(λ)]\lambda^{*}\leftarrow\min\left[\operatorname*{argmin}_{\lambda\in\boldsymbol{\lambda}}\,\mathcal{L}_{\textsc{mstls}}(\lambda)\right]
- 2.

𝐰^mstls←MSTLS​(𝐛,𝐆,λ∗)\hat{\mathbf{w}}^{\textsc{mstls}}\leftarrow\texttt{MSTLS}\big(\mathbf{b},\,\mathbf{G},\,\lambda^{*}\big)
- 3.

Δ←γ2​log⁡(‖𝐛−𝐆​𝐰^mstls‖22/‖𝐛‖22)+2​log⁡(γ)​r​(𝐰^mstls)\Delta\leftarrow\gamma^{2}\log\left(\|\mathbf{b}-\mathbf{G}\hat{\mathbf{w}}^{\textsc{mstls}}\|^{2}_{2}/\|\mathbf{b}\|^{2}_{2}\right)+2\log(\gamma)r(\hat{\mathbf{w}}^{\textsc{mstls}})
- 4.

ifΔ≥0\Delta\geq 0:𝐰^←𝟎\hat{\mathbf{w}}\leftarrow\mathbf{0}
- 

else:𝐰^←𝐰^mstls\hat{\mathbf{w}}\leftarrow\hat{\mathbf{w}}^{\textsc{mstls}}
- 5.

return𝐰^\hat{\mathbf{w}}

It is important to note that the standard MSTLS algorithm does not natively allow for weight vectors with empty support (i.e., withsupp​(𝐰^i)=∅\text{supp}(\hat{\mathbf{w}}_{i})=\varnothing), and thus does not allow for trivial righthand-side models of the formx˙i≈𝚯​(𝒙)​𝐰^i=0.\displaystyle\dot{x}_{i}\approx\mathbf{\Theta}(\boldsymbol{x})\hat{\mathbf{w}}_{i}=0.

To resolve this behavior in the context of the scattering ODEs of eq. (2.14), where indeedκ˙i=0\dot{\kappa}_{i}=0, we develop a ‘zero-admissible’ extension of Algorithm1inspired by the model selection work of[Mangan.etal2017ProcRSocA]and[Messenger.etal2024JRSocInterfacea]. In particular, we use aBayesian information criterion(BIC) of the formℬ​(𝐰^i;𝐛i,𝐆):=γ2​log⁡(‖𝐛i−𝐆​𝐰^i‖22γ2)+2​log⁡(γ)​r​(𝐰^i),\displaystyle\mathcal{B}(\hat{\mathbf{w}}_{i};\mathbf{b}_{i},\mathbf{G}):=\gamma^{2}\log\left(\frac{\|\mathbf{b}_{i}-\mathbf{G}\hat{\mathbf{w}}_{i}\|^{2}_{2}}{\gamma^{2}}\right)\,+\,2\log(\gamma)r(\hat{\mathbf{w}}_{i}),(A.2)

wherer​(𝐰^i):=rank​(𝐆|supp​(𝐰^i))r(\hat{\mathbf{w}}_{i}):=\text{rank}(\mathbf{G}|_{\text{supp}(\hat{\mathbf{w}}_{i})})denotes the number of uniquely estimated parameters andγ2>0\gamma^{2}>0is a ‘soft rank’ heuristic for the number of statistically independent weak-form equations in eq. (2.19),γ:=‖𝚽˙‖F2‖𝚽˙​𝚽˙T‖F≈K​‖φ˙​(𝐭)‖22‖φ˙​(𝐭)⋆φ˙​(𝐭)‖2,whereγ2∼Km,asK→∞.\displaystyle\gamma:=\frac{\|\dot{\mathbf{\Phi}}\|^{2}_{F}}{\|\dot{\mathbf{\Phi}}\dot{\mathbf{\Phi}}^{T}\|_{F}}\approx\sqrt{K}\frac{\|\dot{\varphi}(\mathbf{t})\|^{2}_{2}}{\|\dot{\varphi}(\mathbf{t})\star\dot{\varphi}(\mathbf{t})\|_{2}},\quad\text{where}\quad\gamma^{2}\sim\frac{K}{m},\ \ \text{as}\ \ K\rightarrow\infty.

For the zero model𝐰^i=𝟎\hat{\mathbf{w}}_{i}=\mathbf{0}(representing conserved quantities), the corresponding BIC value is given byℬ​(𝟎;𝐛i,𝐆)=γ2​log⁡(‖𝐛i‖22γ2),\displaystyle\mathcal{B}(\mathbf{0};\mathbf{b}_{i},\mathbf{G})=\gamma^{2}\log\left(\frac{\|\mathbf{b}_{i}\|^{2}_{2}}{\gamma^{2}}\right),

meaning thatΔi:=ℬ​(𝐰^i;𝐛i,𝐆)−ℬ​(𝟎;𝐛i,𝐆)=γ2​log⁡(‖𝐛i−𝐆​𝐰^i‖22‖𝐛i‖22)+2​log⁡(γ)​r​(𝐰^i).\displaystyle\Delta_{i}:=\mathcal{B}(\hat{\mathbf{w}}_{i};\mathbf{b}_{i},\mathbf{G})-\mathcal{B}(\mathbf{0};\mathbf{b}_{i},\mathbf{G})=\gamma^{2}\log\left(\frac{\|\mathbf{b}_{i}-\mathbf{G}\hat{\mathbf{w}}_{i}\|^{2}_{2}}{\|\mathbf{b}_{i}\|^{2}_{2}}\right)\,+\,2\log(\gamma)r(\hat{\mathbf{w}}_{i}).

In principle, forΔi≥0\Delta_{i}\geq 0, trivial dynamics are preferred from an information-theoretic point of view; conversely, the non-zero MSTLS estimate is preferred wheneverΔi<0\Delta_{i}<0. With this in mind, our final model weights𝐰^i\hat{\mathbf{w}}_{i}are determined using Algorithm2given above. Numerically, we guard against degenerate weak dynamics‖𝐛i‖2≈0\|\mathbf{b}_{i}\|_{2}\approx 0by defaulting to the zero model whenever‖𝐛i‖2≤τ𝐛:=1e-8\|\mathbf{b}_{i}\|_{2}\leq\tau_{\mathbf{b}}:=\texttt{1e-8}. Otherwise, we trigger the BIC test of Algorithm2whenever the MSTLS fit is poor – in particular, when the relative residual‖𝐛i−𝐆​𝐰^imstls‖2/‖𝐛i‖2\|\mathbf{b}_{i}-\mathbf{G}\hat{\mathbf{w}}_{i}^{\textsc{mstls}}\|_{2}/\|\mathbf{b}_{i}\|_{2}exceeds a default cutoff of0.50.5.

## Appendix BProperties of Lax Pairs

Two linear differential operatorsLLandMM, acting on test functionsϕ=ϕ​(x;t)\phi=\phi(x;t)and potentially depending on a one-parameter family of functionsu=u​(x;t)u=u(x;t), are called aLax pairif they satisfyLax’s equation,Lt=[M,L],or equivalently,Lt+[L,M]=0,\displaystyle L_{t}=[M,L],\quad\text{or equivalently,}\quad L_{t}+[L,M]=0,

just as in eq. (2.2) above. In many cases of interest,LLis self-adjoint whileMMis skew-adjoint, in which case the point spectrum ofLLis invariant in time (i.e.,L​(u)∼L​(u0)L(u)\sim L(u_{0})for everytt). This can be explicitly shown by considering the EVP given byL​ϕ=λ​ϕL\phi=\lambda\phiwith normalized eigenfunctions‖ϕ‖2=1\|\phi\|_{2}=1, so thatλ=⟨ϕ,L​ϕ⟩\lambda=\langle\phi,L\phi\rangle. Differentiating with respect to time then yieldsλ˙=⟨ϕ,Lt​ϕ⟩=⟨ϕ,[M,L]​ϕ⟩=λ​⟨ϕ,M​ϕ⟩−λ​⟨ϕ,M​ϕ⟩=0,\displaystyle\dot{\lambda}=\langle\phi,L_{t}\phi\rangle=\langle\phi,[M,L]\phi\rangle=\lambda\langle\phi,M\phi\rangle-\lambda\langle\phi,M\phi\rangle=0,

where the second equality above follows from Lax’s equation and the third uses⟨ϕ,M​L​ϕ⟩=λ​⟨ϕ,M​ϕ⟩\langle\phi,ML\phi\rangle=\lambda\langle\phi,M\phi\rangletogether with⟨ϕ,L​M​ϕ⟩=λ​⟨ϕ,M​ϕ⟩\langle\phi,LM\phi\rangle=\lambda\langle\phi,M\phi\rangle. Moreover, for any eigenpair(λ,ϕ)(\lambda,\phi)satisfyingL​(u0)​ϕ0=λ​ϕ0L(u_{0})\phi_{0}=\lambda\phi_{0}at the initial timet=0t=0, the transported eigenfunctionϕ:=P​(t)​ϕ0\phi:=P(t)\phi_{0}satisfies the linear system of eq. (2.3), whereP​(t)P(t)is a unitary operator representing a solution toP˙=M​(u)​P\dot{P}=M(u)PwithP0=IP_{0}=I.{Backmatter}

## Acknowledgments

The authors would like to thank Mark Ablowitz for his helpful insights, especially concerning future work with Painlevé equations. This work utilized the Blanca condo computing resource at the University of Colorado Boulder. Blanca is jointly funded by computing users and the University of Colorado Boulder.

## Funding Statement

This work is supported in part by National Science Foundation Grants 2054085 and 2109774, National Institute of Food and Agriculture Grant 2019-67014-29919, and Department of Energy Grant DE-SC0023346.

## Competing Interests

The authors declare no competing interests.

## Data Availability Statement

Replication data and code are publicly available:https://github.com/MathBioCU/Scattering

## Ethical Standards

The research meets all ethical guidelines, including adherence to the legal requirements of the study country.

## Author Contributions

Conceptualization: S.M; V.D.; D.M.B. Methodology: S.M; V.D.; D.M.B. Data curation: S.M. Data visualization: S.M. Writing original draft: S.M. All authors approved the final submitted draft.

## 


- 


Major funding support from
