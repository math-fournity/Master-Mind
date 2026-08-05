# Solving the Dissipation Inequality not as a constitutive restriction

**arXiv ID**: 2608.02215v1
**Authors**: Maximiliano Larrain Silva, Amit Acharya
**Published**: 2026-08-03
**Categories**: physics.class-ph, cond-mat.mtrl-sci, math.OC
**Comments**: 16 pages, 10 figures
**HTML URL**: https://arxiv.org/html/2608.02215v1

## Abstract

A solution procedure is formulated and solved for treating the nonlinear Dissipation Inequality as a constraint equation within continuum mechanics, and allowing for incomplete knowledge of constitutive behavior. The scheme is demonstrated in the context of the rate-dependent, elastoplastic response of a bar, resulting in a nonlinear problem of constrained optimization. Both closed form and computational results are developed. The computational solutions utilize a sequence of convex optimization problems, and are shown to be accurate. In the example considered, the approach is shown to automatically correct an (intentionally) faulty constitutive specification, resulting in the solution to be in accord with the fundamental postulates of continuum mechanics.

## Full Text

Solving the Dissipation Inequality not as a constitutive restriction

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2608.02215v1 [physics.class-ph] 03 Aug 2026

## Solving the Dissipation Inequality not as a constitutive restrictionMaximiliano Larrain Silva    Amit AcharyaDepartment of Civil & Environmental Engineering, Carnegie Mellon University, Pittsburgh, PA 15213, email: maximill@andrew.cmu.edu.Department of Civil & Environmental Engineering, and Center for Nonlinear Analysis, Carnegie Mellon University, Pittsburgh, PA 15213, email: acharyaamit@cmu.edu.

## Abstract

A solution procedure is formulated and solved for treating the nonlinear Dissipation Inequality as a constraint equation within continuum mechanics, and allowing for incomplete knowledge of constitutive behavior. The scheme is demonstrated in the context of the rate-dependent, elastoplastic response of a bar, resulting in a nonlinear problem of constrained optimization. Both closed form and computational results are developed. The computational solutions utilize a sequence of convex optimization problems, and are shown to be accurate. In the example considered, the approach is shown to automatically correct an (intentionally) faulty constitutive specification, resulting in the solution to be in accord with the fundamental postulates of continuum mechanics.

## 1Introduction

In solving problems of continuum mechanics, the Second Law of thermodynamics or the Dissipation Inequality is difficult to accommodate as a constraint. It is also a fact that it is never possible to prescribe a model for material behavior with absolute certainty. In this communication, we study a simple model problem intentionally designed to embody these questions, and solve it using the ideas and scheme initiated in[acharya2025second]. The model problem concerns the quasi-static response of a rate-dependent elastic-plastic bar whose specified constitutive equation is intentionally chosen to violate the Dissipation Inequality over an interval of time, in the spirit of[needleman2023discrete, Sec 7.1]. We seek a self-consistent procedure that takes as input such a specification and nevertheless produces a solution that does not violate the Second Law, with ‘minimal’ deviation from the specified constitutive response. An exact as well as a computational formulation is developed for the problem. It is shown how the ingredients of the proposed scheme attains its goal, allowing the solution of the problem in a well-set manner.

## 2A simple model problem

Consider a 1-d bar made of an elastic-plastic material occupying the regionx∈[0,1]x\in[0,1]in the reference configuration, undergoing quasi-static stretching under a prescribed force (per unit cross-section area)t↦l​(t)t\mapsto l(t)at the right end as a function of time. The left end is assumed to be fixed, i.e.,u​(0,t)=0u(0,t)=0, where(x,t)↦u​(x,t)(x,t)\mapsto u(x,t)is the displacement of the bar (see Fig.1). With notation that subscriptt,xt,xrepresent partial derivatives w.r.t.t,xt,x, respectively, if(x,t)↦σ​(x,t)(x,t)\mapsto\sigma(x,t)represents the axial stress in the bar, equilibriumFigure 1:Schematic of the physical problem.σx=0\sigma_{x}=0(1)

implies that the stress is only a function time in the bar given byσ​(x,t)=σ​(1,t)=l​(t).\sigma(x,t)=\sigma(1,t)=l(t).(2)

Letψ\psibe the stored energy density for the material. Then the Second Law/Dissipation Inequality is given byσ​ut|x=1−σ​ut|x=0−ψt≥0.\sigma u_{t}\big|_{x=1}-\sigma u_{t}\big|_{x=0}-\psi_{t}\geq 0.(3)

Assuming a specified constitutive equation for stress and stored energy of the formσ=σc\displaystyle\sigma=\sigma^{c}=E​(ux−p)\displaystyle=E(u_{x}-p)(4)ψc\displaystyle\psi^{c}=12​E​(ux−p)2\displaystyle=\frac{1}{2}E(u_{x}-p)^{2}

whereEEis the Young’s modulus, and(x,t)↦p​(x,t)(x,t)\mapsto p(x,t)is the plastic strain in the bar. Using (1), (4) and the boundary condition on the displacement at the left end of the bar, (3) takes the formσ​pt≥0.\sigma p_{t}\geq 0.(5)

Suppose the specified constitutive equation for the evolution ofppwere to be given bypt=fc​(σ,t).p_{t}=f^{c}(\sigma,t).(6)

For simplicity let us assume that the loadingt↦l​(t)≥0t\mapsto l(t)\geq 0. Given an initial conditionp​(0)=p0p(0)=p_{0}the plastic strain evolution is completely determined from solving (6) in the formpt=fc​(l​(t),t);p​(0)=p0,p_{t}=f^{c}(l(t),t);\qquad p(0)=p_{0},

and, therefore, iffcf^{c}were to be an ‘arbitrarily’ chosen physically motivated function, satisfaction of the Dissipation Inequality (5)l​(t)​fc​(l​(t),t)≥0l(t)f^{c}(l(t),t)\geq 0

cannot be guaranteed, unless the constitutive restrictionσc​fc≥0\sigma^{c}f^{c}\geq 0(7)

is imposed on the choice of the constitutive equation for the plastic strain rate.

We would now like to consider a formulation of the problem where the best possible physical choices of constitutive assumptions, i.e., estimates of material behavior, as deemed by a practitioner can be made and the Second Law satisfied without viewing it as a restriction on constitutive response as in (7). Noting that a constitutive response can never be claimed to be known with certainty, we assume that the evolution of the plastic strain is given bypt​(x,t)=fc​(σ​(x,t),t)+a​(x,t)p_{t}(x,t)=f^{c}(\sigma(x,t),t)+a(x,t)(8)

where the fields(x,t)↦(u​(x,t),p​(x,t),a​(x,t),s​(x,t))(x,t)\mapsto(u(x,t),p(x,t),a(x,t),s(x,t))are to be determined by solving (1)-(5) in the forml​(fc​(l,t)+a)−12​s2\displaystyle l\big(f^{c}(l,t)+a\big)-\frac{1}{2}s^{2}=0\displaystyle=0(9)pt−fc​(l,t)−a\displaystyle p_{t}-f^{c}(l,t)-a=0\displaystyle=0p​(0)\displaystyle p(0)=p0,\displaystyle=p_{0},

wherep0p_{0}is a specified initial condition on the plastic strain.

The function(1/2)​s2(1/2)s^{2}represents the dissipation density, and in this formulation,ssis a field we solve for as well. Given (1), it suffices to solve the problem withxx-independent fields, which is an ansatz we adopt. Once a solution fort↦p​(t)t\mapsto p(t)is obtained, (4) is solved in the formux​(x,t)=E−1​l​(t)+p​(t)u_{x}(x,t)=E^{-1}l(t)+p(t)and integrated w.r.t.xxwith b.c.u​(0,t)=0u(0,t)=0to obtain the displacement of the bar.

Thus the problem becomes a question of obtaining, in a well-set manner, the functionst↦(p​(t),s​(t),a​(t))t\mapsto(p(t),s(t),a(t))which satisfy (9). It is clear that we have two equations in three functions and, in general, this is going to be a practical impediment even if conceptually the non-uniqueness is accepted.

To have a physically reasonable and practically tractable problem, we follow[acharya2025second]and require thataabe as small as possible, reflecting faith in the constitutive specification deployed, but allowing, at the same time, for non-negative dissipation and the impossibility of knowing material response with infinite precision. Since we have employed a constitutive response functionfcf^{c}and would like the dissipation in the system to be dictated solely by that modeling knowledge to the extent possible without violating the fundamental constraints embodied in (9), we also require(1/2)​s2(1/2)s^{2}to be as small as possible without violating the constraints (9).

Thus, we consider the minimization problem on the time interval[0,T][0,T]given bymina,s​∫0Tℋ​(a,s)​𝑑t;ℋ​(a,s):=12​ca​a2+12​cs​s2\min_{a,s}\int_{0}^{T}{\cal H}(a,s)\,dt;\qquad{\cal H}(a,s):=\frac{1}{2}c_{a}a^{2}+\frac{1}{2}c_{s}s^{2}(10)

subject to the constraints (9) written in the forma​(s)\displaystyle a(s)=12​l​s2−fc\displaystyle=\frac{1}{2l}s^{2}-f^{c}(11a)pt\displaystyle p_{t}=12​l​s2;p​(0)=p0.\displaystyle=\frac{1}{2l}s^{2};\qquad p(0)=p_{0}.(11b)

Noticing the form of the constrained minimization problem, the optimization can be considered pointwise in time without any differential constraints for the objectiveh​(s)=12​ca​(a​(s))2+12​cs​s2,h(s)=\frac{1}{2}c_{a}(a(s))^{2}+\frac{1}{2}c_{s}s^{2},

witha​(s)a(s)given by (11a), andcsc_{s}andcac_{a}being positive material constants with the physical dimension of the ratiocs/cac_{s}/c_{a}being(Time.stress)−1(Time.stress)^{-1}.

It is easily checked that the minimum is attained ats2​(t)={0forfc​(l​(t),t)−csca​l​(t)<02​l​(t)​(fc​(l​(t),t)−csca​l​(t))forfc​(l​(t),t)−csca​l​(t)≥0,s^{2}(t)=\begin{cases}0\qquad\mbox{for}\qquad f^{c}(l(t),t)-\frac{c_{s}}{c_{a}}l(t)<0\\
\\
2l(t)\left(f^{c}(l(t),t)-\frac{c_{s}}{c_{a}}l(t)\right)\qquad\mbox{for}\qquad f^{c}(l(t),t)-\frac{c_{s}}{c_{a}}l(t)\geq 0,\end{cases}(12)

with (11b) evolved according to the above specification ofs2s^{2}.

Forσ0,γ^\sigma_{0},\hat{\gamma}being typical stress and strain rate scales for the problem entering through the specified constitutive equationfcf^{c}, e.g., the yield stress and reference plastic strain rate, it is interesting to note the solution of the problem in the limitcs​σ0ca​γ^→0\frac{c_{s}\sigma_{0}}{c_{a}\hat{\gamma}}\to 0

is given bys2​(t)={0forfc​(l​(t),t)<02​l​(t)​fc​(l​(t),t)forfc​(l​(t),t)≥0;pt=s22​l={0forfc<0fcforfc≥0.s^{2}(t)=\begin{cases}0\quad\mbox{for}\quad f^{c}(l(t),t)<0\\
\\
2l(t)\,f^{c}(l(t),t)\quad\mbox{for}\quad f^{c}(l(t),t)\geq 0\end{cases};\qquad p_{t}=\frac{s^{2}}{2l}=\begin{cases}0\quad\mbox{for}\quad f^{c}<0\\
f^{c}\quad\mbox{for}\quad f^{c}\geq 0.\end{cases}(13)

This is the naturally expected result selected by our scheme out of the infinite family of solutions to the system (9) consisting of force equilibrium, constitutive equation, and the Second Law. The infinite family is parametrized by any choice of the dissipation functiont↦(1/2)​s2​(t)t\mapsto(1/2)s^{2}(t), as evident from (11). The approach above selects a solution of this family.

In what follows we evaluate a computational scheme, originally designed for solving systems of partial differential equations (which obviously includes ordinary differential and algebraic equations) using methods of the calculus of variations[ka1,ka2,kpa,sga,suku_ach,AV_nash]. It tries to obtain the desired solution obtained above of the constrained minimization problem in a stable fashion without exploiting special simplifying features, e.g., not eliminating differential constraints as done above.

## 3Approximation based on a convex dual variational principle

This section presents the variational dual formulation of the governing equations (10)-(11), following the general theory proposed in[ach3]-[AV_nash, Sec. 3].

We use the notationU:=(p,s,a)U:=(p,s,a)denoting the primal fields andD:=(α,β)D:=(\alpha,\beta)the dual fields. A pre-dual functionalS^H​[U,D]\widehat{S}_{H}[U,D]is formed by taking the scalar product of equations (11) with the dual fieldsDD, integrating by parts, substituting the prescribed initial condition forpp(ignoring for now the final-time boundary condition that arises on integration by parts but is not specified as part of the primal physical problem (11)) and subtracting an auxiliary potentialHH, resulting inS^H​[U,D]=∫0T(l​(fc+a)−12​s2)​α−p​βt−fc​β−a​β−H​(U,U¯)​d​t−p0​β​(0).\widehat{S}_{H}[U,D]=\int_{0}^{T}\Big(l\big(f^{c}+a\big)-\frac{1}{2}s^{2}\Big)\alpha-p\beta_{t}-f^{c}\beta-a\beta-H(U,\bar{U})\,dt\ -\ p_{0}\beta(0).(14)

In the above,U¯:=(p¯,s¯,a¯)\bar{U}:=(\bar{p},\bar{s},\bar{a})are prescribed functions of time called ‘base states’ andH​(U,U¯)H(U,\bar{U})is specified asH​(U,U¯)=cp2​(p−p¯)2+cs2​(s−s¯)2+ca2​(a−a¯)2;cp,cs,ca>0.H(U,\bar{U})=\frac{c_{p}}{2}(p-\bar{p})^{2}+\frac{c_{s}}{2}(s-\bar{s})^{2}+\frac{c_{a}}{2}(a-\bar{a})^{2};\qquad c_{p},c_{s},c_{a}>0.(15)

A part of the auxiliary potentialHHis chosen to resemble the physical objective functionℋ\mathcal{H}(10) from Section2; the weightscsc_{s}andcac_{a}inℋ\mathcal{H}match those inHH. This is natural and aids in the selection of the solution representing a minimal controlaaand dissipations2/2s^{2}/2. This design of the auxiliary functionHHis slightly different from the case when the question is solely to solve a system of equations without involving a physical functional/objective to be optimized, as in[ka1,ka2,sga,kpa,AV_nash]. In that case, the design of the auxiliary function is entirely governed by considerations of mathematical convenience for obtaining a solution to the system.

For simplicity, we refer to the compositiont↦fc∘l​(t)t\mapsto f^{c}\circ l(t)ast↦fc​(t)t\mapsto f^{c}(t). In this specific problem,fcf^{c}becomes a specified function of time due to the simplification (2).

Define𝒟:=(D,Dt)\mathcal{D}:=(D,D_{t})and the LagrangianℒH​(U,𝒟,U¯)\mathcal{L}_{H}(U,\mathcal{D},\bar{U})asℒH​(U,𝒟,t)=(l​(fc+a)−12​s2)​α−p​βt−fc​β−a​β−H​(U,U¯).\mathcal{L}_{H}(U,\mathcal{D},t)=\Big(l\big(f^{c}+a\big)-\frac{1}{2}s^{2}\Big)\alpha-p\beta_{t}-f^{c}\beta-a\beta-H(U,\bar{U}).(16)

Then, the ‘dual-to-primal’ (DtP) map, denotedU(H)​(𝒟,U¯,t)U^{(H)}(\mathcal{D},\bar{U},t), is obtained by solving∂UℒH​(U,𝒟,U¯,t)=0\partial_{U}\mathcal{L}_{H}(U,\mathcal{D},\bar{U},t)=0forUUas(𝒟,U¯,t)↦U(H)​(𝒟,U¯,t)(\mathcal{D},\bar{U},t)\mapsto U^{(H)}(\mathcal{D},\bar{U},t)satisfying∂ℒH∂U​(U(H)​(𝒟,U¯),𝒟,t)=0.\frac{\partial\mathcal{L}_{H}}{\partial U}\left(U^{(H)}(\mathcal{D},\bar{U}),\mathcal{D},t\right)=0.(17)

In this particular case,U(H)​(𝒟,U¯,t)U^{(H)}(\mathcal{D},\bar{U},t)is obtained aspH​(𝒟,U¯,t)\displaystyle p_{H}(\mathcal{D},\bar{U},t)=p¯−βtcp\displaystyle=\bar{p}-\frac{\beta_{t}}{c_{p}}(18)sH​(𝒟,U¯,t)\displaystyle s_{H}(\mathcal{D},\bar{U},t)=cs​s¯α+cs\displaystyle=\frac{c_{s}\bar{s}}{\alpha+c_{s}}aH​(𝒟,U¯,t)\displaystyle a_{H}(\mathcal{D},\bar{U},t)=a¯+l​α−βca.\displaystyle=\bar{a}+\frac{l\alpha-\beta}{c_{a}}.

ThedualfunctionalSH​[D]S_{H}[D]is then obtained by substituting the DtP map (18) into the pre-dual functional (14) asSH​[D]\displaystyle S_{H}[D]=S^H​[U(H)​(𝒟,U¯,t),D]=∫0TℒH​(U(H)​(𝒟,U¯,t),𝒟,t)​𝑑t−p0​β​(0)\displaystyle=\widehat{S}_{H}\left[U^{(H)}(\mathcal{D},\bar{U},t),D\right]=\int_{0}^{T}\mathcal{L}_{H}\Bigl(U^{(H)}(\mathcal{D},\bar{U},t),\mathcal{D},t\Bigr)\hskip 5.69054ptdt\hskip 5.69054pt-p_{0}\beta(0)(19)=∫0T(l​(fc+aH)−12​sH2)​α−pH​βt−fc​β−aH​β−H​(U(H),U¯)​d​t−p0​β​(0).\displaystyle=\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)\alpha-p_{H}\beta_{t}-f^{c}\beta-a_{H}\beta-H(U^{(H)},\bar{U})\hskip 5.69054ptdt\hskip 5.69054pt-p_{0}\beta(0).

Its first variation about a stateDDin the directionδ​D\delta Dis given byδ​SH|δ​D​[D;U¯]=∫0T∂ℒH∂𝒟​(U(H)​(𝒟,t),𝒟,t)⋅δ​𝒟​𝑑t−p0​δ​β​(0)=∫0T(l​(fc+aH)−12​sH2)​δ​α−pH​δ​βt−fc​δ​β−aH​δ​β​d​t−p0​δ​β​(0).\delta S_{H}\Big|_{\delta D}[D;\bar{U}]=\int_{0}^{T}\frac{\partial\mathcal{L}_{H}}{\partial\mathcal{D}}\left(U^{(H)}(\mathcal{D},t),\mathcal{D},t\right)\cdot\delta\mathcal{D}\hskip 5.69054ptdt\hskip 5.69054pt-p_{0}\delta\beta(0)\\
=\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)\delta\alpha-p_{H}\delta\beta_{t}-f^{c}\delta\beta-a_{H}\delta\beta\hskip 5.69054ptdt\hskip 5.69054pt-p_{0}\delta\beta(0).(20)

SinceℒH\mathcal{L}_{H}is affine in its argument𝒟\mathcal{D}, and using (17) as well as the fact thatβ​(t)\beta(t)has a Dirichlet boundary condition specified att=Tt=Tso thatδ​β​(T)=0\delta\beta(T)=0, the Euler-Lagrange equations and natural boundary conditions of the dual functionalSHS_{H}are exactly the primal equations shown in (11) with the primal variablesUUsubstituted by the DtP map,U(H)U^{(H)}. Indeed, in this specific case we haveδ​SH|δ​D​[D]=∫0T(l​(fc+aH)−12​sH2)​δ​α+((pH)t−fc−aH)​δ​β​d​t+(pH​(0)−p0)​δ​β​(0),\delta S_{H}\Big|_{\delta D}[D]=\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)\delta\alpha+\Big((p_{H})_{t}-f^{c}-a_{H}\Big)\delta\beta\hskip 5.69054ptdt+\big(p_{H}(0)-p_{0}\big)\delta\beta(0),(21)

from which the E-L equations and the initial condition can be read off.

An important feature of the formulation which makes the dual functionalconvex, with its associated variational principle a minimum (as opposed to an extremum) principle, is ensured by requiring that the Dual functionalSHS_{H}is restricted to the domain inDD-space for which−∂U​UℒH​(U^​(t),𝒟​(t),U¯​(t),t)>0for each​t∈(0,T);U^​(t):=U(H)​(𝒟​(t),U¯​(t),t),-\partial_{UU}\mathcal{L}_{H}\left(\hat{U}(t),\mathcal{D}(t),\bar{U}(t),t\right)>0\quad\mbox{ for each }t\in(0,T);\qquad\hat{U}(t):=U^{(H)}\left(\mathcal{D}(t),\bar{U}(t),t\right),(22)

see[AG_control, Sec. 3],[AV_nash, Sec. 3]. We employ this restriction in all that follows by utilizing appropriate changes of base states. We refer to this restricted domain of the dual functionalSHS_{H}as the DtP zone.

In this example, the Hessian of the Lagrangian,∂U​UℒH​(U,𝒟,U¯,t)\partial_{UU}\mathcal{L}_{H}(U,\mathcal{D},\bar{U},t), is diagonal, so the condition reduces to requiring that each diagonal entry (i.e., each eigenvalue) be strictly negative:−∂2∂p2​ℒH=cp>0;−∂2∂s2​ℒH=α+cs>0;−∂2∂a2​ℒH=ca>0.-\frac{\partial^{2}}{\partial p^{2}}\mathcal{L}_{H}=c_{p}>0;\qquad-\frac{\partial^{2}}{\partial s^{2}}\mathcal{L}_{H}=\alpha+c_{s}>0;\qquad-\frac{\partial^{2}}{\partial a^{2}}\mathcal{L}_{H}=c_{a}>0.(23)

Sincecpc_{p},cac_{a}>0>0, the only non trivial restriction defining the DtP zone isα​(t)>−cs∀t∈(0,T).\alpha(t)>-c_{s}\hskip 28.45274pt\forall t\in(0,T).(24)

Having derived the dual functionalSH​[D]S_{H}[D]and its first variation, our goal is to find a stationary point ofSH​[D]S_{H}[D]. This is achieved in two consecutive phases: first, the gradient flow scheme presented in[AV_nash, Sec. 3]drives the initial approach to the solution; second, this solution is refined using the Newton Raphson scheme with step size control presented in[kpa]. Here, the Newton Raphson phase is modified to also include a restriction on theL2L^{2}norm of the gradient ofSHS_{H}, which must not increase throughout this phase, sinceSHS_{H}is convex with the restriction of its domain discussed surrounding (22). In both phases, the finite element method is used to discretize and approximately solve the problem.

For the gradient flow, we follow[AV_nash, Section 3.2], and think of a (fake, time-like) variable𝗌\mathsf{s}along which a gradient descent of the functionalSHkS_{H_{k}}is executed. Here,HkH_{k}represents the auxiliary potential used in stagekkof the gradient flow, parametrized by the base stateUk¯\bar{U^{k}}, which is held fixed throughout that stage. Each stage comprises the interval[0,𝗌~k∗)[0,\tilde{\mathsf{s}}^{*}_{k}), with𝗌~k∗\tilde{\mathsf{s}}^{*}_{k}being the (fake)time instant at which the gradient flow achieves convergence, or one of the stopping criteria for stagekkis met (see Table1). We consider dual unknown fields defined by(t,𝗌)↦Dk​(t,𝗌)(t,\mathsf{s})\mapsto D^{k}(t,\mathsf{s}), and corresponding variationsδ​D\delta Dto execute the following gradient flow:∫0Tδ​D​(t)⋅∂Dk∂s​(t,𝗌)​𝑑t=−∫0Tδ​SHkδ​D​[Dk;U¯k]​(t,𝗌)⋅δ​D​(t)​𝑑t.\int_{0}^{T}\delta D(t)\cdot\frac{\partial D^{k}}{\partial s}(t,\mathsf{s})dt=-\int_{0}^{T}\frac{\delta S_{H_{k}}}{\delta D}[D^{k};\bar{U}^{k}](t,\mathsf{s})\cdot\delta D(t)\,dt.(25)

LetΩ={t:t∈(0,T)}\Omega=\{t:t\in(0,T)\}denote the physical time domain, which we discretize using a uniform finite element mesh. The trial and test functions are chosen to be piecewise linear and globally continuous, dependent solely ontt. These shape functions are denoted byN(⋅)N^{(\cdot)}, where(⋅)(\cdot)denotes the index of the node associated with that function.
Using this discretization, the dual fields and their respective variations are approximated by the expressions shown in (26) and (27), where the summation convention is used. Throughout, the uppercase indexBBdenotes the node associated with the trial function, while the uppercase indexAAdenotes the node associated with the test (variation) function.α​(t,𝗌)=αB​(𝗌)​NB​(t)β​(t,𝗌)=βB​(𝗌)​NB​(t)\alpha(t,\mathsf{s})=\alpha^{B}(\mathsf{s})N^{B}(t)\hskip 28.45274pt\beta(t,\mathsf{s})=\beta^{B}(\mathsf{s})N^{B}(t)(26)δ​α​(t)=δ​αA​NA​(t)δ​β​(t)=δ​βA​NA​(t).\delta\alpha(t)=\delta\alpha^{A}N^{A}(t)\hskip 28.45274pt\delta\beta(t)=\delta\beta^{A}N^{A}(t).(27)

As shown in (26), the dual fieldsα​(t,𝗌)\alpha(t,\mathsf{s})andβ​(t,𝗌)\beta(t,\mathsf{s})depend on the variable𝗌\mathsf{s}only through the coefficients that multiply the shape functions, not through the shape functions themselves (which depend only on physical timett). Expanding (25) using (20), we have∫0Tδ​α​(t)​∂α∂s​(t,𝗌)​𝑑t+∫0Tδ​β​(t)​∂β∂𝗌​(t,𝗌)​𝑑t=−∫0T(l​(fc+aH)−12​sH2)​δ​α​(t)−pH​δ​βt​(t)−fc​δ​β​(t)−aH​δ​β​(t)​d​t−p0​δ​β​(0).\int_{0}^{T}\delta\alpha(t)\frac{\partial\alpha}{\partial\mathrm{s}}(t,\mathsf{s})dt+\int_{0}^{T}\delta\beta(t)\frac{\partial\beta}{\partial\mathsf{s}}(t,\mathsf{s})dt=\\
-\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)\delta\alpha(t)-p_{H}\delta\beta_{t}(t)-f^{c}\delta\beta(t)-a_{H}\delta\beta(t)\hskip 5.69054ptdt\hskip 5.69054pt-p_{0}\delta\beta(0).(28)

Note that∂/∂s\partial/\partial\mathrm{s}denotes differentiation with respect to the fictitious gradient flow time, whereas the subscriptttappearing inδ​βt\delta\beta_{t}denotes differentiation with respect to physical time, consistent with (20). Substituting (26) and (27) in (28), we obtainδ​αA​(∫0TNA​(t)​∂αB∂𝗌​(𝗌)​NB​(t)​𝑑t)+δ​βA​(∫0TNA​(t)​∂βB∂𝗌​(𝗌)​NB​(t)​𝑑t)=−δαA(∫0T(l(fc+aH)−12sH2)NA(t)dt)−δβA(∫0T−pHNtA(t)−fcNA(t)−aHNA(t)dt−p0NA(0)).\delta\alpha^{A}\Big(\int_{0}^{T}N^{A}(t)\frac{\partial\alpha^{B}}{\partial\mathsf{s}}(\mathsf{s})N^{B}(t)dt\Big)+\delta\beta^{A}\Big(\int_{0}^{T}N^{A}(t)\frac{\partial\beta^{B}}{\partial\mathsf{s}}(\mathsf{s})N^{B}(t)dt\Big)=\\
-\delta\alpha^{A}\Big(\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)N^{A}(t)dt\Big)-\delta\beta^{A}\Big(\int_{0}^{T}-p_{H}N_{t}^{A}(t)\\
-f^{c}N^{A}(t)-a_{H}N^{A}(t)dt\hskip 5.69054pt-p_{0}N^{A}(0)\Big).(29)

Factoring outδ​αA\delta\alpha^{A}andδ​βA\delta\beta^{A}, (29) becomes:δ​αA​(MA​B​∂αB∂𝗌​(𝗌)+R(α)A)+δ​βA​(MA​B​∂βB∂𝗌​(𝗌)+R(β)A)=0,\delta\alpha^{A}\Big(M^{AB}\frac{\partial\alpha^{B}}{\partial\mathsf{s}}(\mathsf{s})+R_{(\alpha)}^{A}\Big)+\delta\beta^{A}\Big(M^{AB}\frac{\partial\beta^{B}}{\partial\mathsf{s}}(\mathsf{s})+R_{(\beta)}^{A}\Big)=0,(30)

where the mass matrixMA​BM^{AB}and the residual vectorsR(α)AR_{(\alpha)}^{A}andR(β)AR_{(\beta)}^{A}are defined asMA​B:=∫0TNA​(t)​NB​(t)​𝑑t,M^{AB}:=\int_{0}^{T}N^{A}(t)N^{B}(t)\ dt,(31)R(α)A​(t):=∫0T(l​(fc+aH)−12​sH2)​NA​(t)​𝑑t,R_{(\alpha)}^{A}(t):=\int_{0}^{T}\Big(l\big(f^{c}+a_{H}\big)-\frac{1}{2}s_{H}^{2}\Big)N^{A}(t)\ dt,(32)R(β)A​(t):=∫0T−pH​NtA​(t)−fc​NA​(t)−aH​NA​(t)​d​t−p0​NA​(0).R_{(\beta)}^{A}(t):=\int_{0}^{T}-p_{H}N_{t}^{A}(t)-f^{c}N^{A}(t)-a_{H}N^{A}(t)\ dt-p_{0}N^{A}(0).(33)

Since (30) must hold for allδ​αA\delta\alpha^{A}andδ​βA\delta\beta^{A}, we obtain the following system of equations:MA​B​∂αB∂𝗌​(𝗌)=−R(α)A;MA​B​∂βB∂𝗌​(𝗌)=−R(β)A∀A.M^{AB}\frac{\partial\alpha^{B}}{\partial\mathsf{s}}(\mathsf{s})=-R_{(\alpha)}^{A};\qquad M^{AB}\frac{\partial\beta^{B}}{\partial\mathsf{s}}(\mathsf{s})=-R_{(\beta)}^{A}\hskip 28.45274pt\forall A.(34)

Finally, to integrate the system (34) in the fictitious time𝗌\mathsf{s}, we partition the interval[0,𝗌~k∗)[0,\tilde{\mathsf{s}}^{*}_{k})into discrete instants𝗌0:=0<𝗌1<𝗌2<…\mathsf{s}_{0}:=0<\mathsf{s}_{1}<\mathsf{s}_{2}<\ldots, with a step sizeΔ​𝗌n\Delta\mathsf{s}_{n}(not necessarily constant and determined by satisfying both (24) and having theL2L^{2}norm of the residual non increasing from instant𝐬n\mathbf{s}_{n}to𝐬n+1\mathbf{s}_{n+1}(see Table1)), and denote byαB​(𝗌n)\alpha^{B}(\mathsf{s}_{n}),βB​(𝗌n)\beta^{B}(\mathsf{s}_{n})the nodal coefficients of the dual functions at time𝗌n\mathsf{s}_{n}. Approximating the derivatives ofαB\alpha^{B}andβB\beta^{B}with respect to𝗌\mathsf{s}using a forward difference scheme (forward Euler), and evaluating the residualR(α)AR_{(\alpha)}^{A}andR(β)AR_{(\beta)}^{A}using the known valuesαB​(𝗌n)\alpha^{B}(\mathsf{s}_{n}),βB​(𝗌n)\beta^{B}(\mathsf{s}_{n})(through the DtP mappHp_{H},sHs_{H}andaHa_{H}), we obtain the linear system of equations shown in (35) to be solved to obtainαB​(𝗌n+1)\alpha^{B}(\mathsf{s}_{n+1}),βB​(𝗌n+1)\beta^{B}(\mathsf{s}_{n+1}), thus advancing from time𝗌n\mathsf{s}_{n}to𝗌n+1\mathsf{s}_{n+1}:MA​B​αB​(sn+1)−αB​(sn)Δ​sn=−RαAMA​B​βB​(sn+1)−βB​(sn)Δ​sn=−RβA∀A.M^{AB}\frac{\alpha^{B}(\mathrm{s}_{n+1})-\alpha^{B}(\mathrm{s}_{n})}{\Delta\mathrm{s}_{n}}=-R_{\alpha}^{A}\hskip 28.45274ptM^{AB}\frac{\beta^{B}(\mathrm{s}_{n+1})-\beta^{B}(\mathrm{s}_{n})}{\Delta\mathrm{s}_{n}}=-R_{\beta}^{A}\hskip 28.45274pt\forall A.(35)

For the second phase consisting of the Newton-Raphson scheme with step size control, we follow the algorithm presented in[kpa]. The system Jacobian is computed by taking the variation of the residual (20), given byJ|δ​D,d​D​[D]=∫0T((l​∂aH∂α−sH​∂sH∂α)​d​α+l​∂aH∂β​d​β)​δ​α​𝑑t+∫0T(−∂aH∂α​d​α​δ​β−∂pH∂βt​d​βt​δ​βt−∂aH∂β​d​β​δ​β)​𝑑t.J\Big|_{\delta D,dD}[D]=\int_{0}^{T}\Big(\big(l\frac{\partial a_{H}}{\partial\alpha}-s_{H}\frac{\partial s_{H}}{\partial\alpha}\big)d\alpha+l\frac{\partial a_{H}}{\partial\beta}d\beta\Big)\delta\alpha\,dt\\
+\int_{0}^{T}\Big(-\frac{\partial a_{H}}{\partial\alpha}d\alpha\delta\beta-\frac{\partial p_{H}}{\partial\beta_{t}}d\beta_{t}\delta\beta_{t}-\frac{\partial a_{H}}{\partial\beta}d\beta\delta\beta\Big)\,dt.(36)

Recalling the approximations forδ​α\delta\alphaandδ​β\delta\betagiven in (27) and introducing analogous approximations for the linearization directionsd​αd\alphaandd​βd\betad​α​(t)=d​αC​NC​(t),d​β​(t)=d​βD​ND​(t),d\alpha(t)=d\alpha^{C}N^{C}(t),\hskip 28.45274ptd\beta(t)=d\beta^{D}N^{D}(t),(37)

the Jacobian in (36) can be expressed asJ|δ​D,d​D​[D]=δ​αA​[∫0T(l​∂aH∂α−sH​∂sH∂α)​NA​(t)​NC​(t)​𝑑t]​d​αC+δ​αA​[∫0Tl​∂aH∂β​NA​(t)​ND​(t)​𝑑t]​d​βD+δ​βA​[∫0T−∂aH∂α​NA​(t)​NC​(t)​d​t]​d​αC+δ​βA​[∫0T−∂pH∂βt​NtA​(t)​NtD​(t)−∂aH∂β​NA​(t)​ND​(t)​d​t]​d​βD.J\Big|_{\delta D,dD}[D]=\\
\delta\alpha^{A}\ \left[\int_{0}^{T}\big(l\frac{\partial a_{H}}{\partial\alpha}-s_{H}\frac{\partial s_{H}}{\partial\alpha}\big)N^{A}(t)N^{C}(t)\,dt\right]\ d\alpha^{C}\ +\ \delta\alpha^{A}\ \left[\int_{0}^{T}l\frac{\partial a_{H}}{\partial\beta}N^{A}(t)N^{D}(t)\,dt\right]\ d\beta^{D}\\
+\ \delta\beta^{A}\ \left[\int_{0}^{T}-\frac{\partial a_{H}}{\partial\alpha}N^{A}(t)N^{C}(t)\,dt\right]\ d\alpha^{C}\ +\ \delta\beta^{A}\ \left[\int_{0}^{T}-\frac{\partial p_{H}}{\partial\beta_{t}}N^{A}_{t}(t)N^{D}_{t}(t)-\frac{\partial a_{H}}{\partial\beta}N^{A}(t)N^{D}(t)\,dt\right]\ d\beta^{D}.(38)

Denoting the main blocks of the system Jacobian asJ(α​α)A​C=∫0T(l​∂aH∂α−sH​∂sH∂α)​NA​(t)​NC​(t)​𝑑t;J(α​β)A​D=∫0Tl​∂aH∂β​NA​(t)​ND​(t)​𝑑tJ_{(\alpha\alpha)}^{AC}=\int_{0}^{T}\big(l\frac{\partial a_{H}}{\partial\alpha}-s_{H}\frac{\partial s_{H}}{\partial\alpha}\big)N^{A}(t)N^{C}(t)dt;\qquad J_{(\alpha\beta)}^{AD}=\int_{0}^{T}l\frac{\partial a_{H}}{\partial\beta}N^{A}(t)N^{D}(t)dt\\J(β​α)A​C=∫0T−∂aH∂α​NA​(t)​NC​(t)​d​t;J(β​β)A​D=∫0T−∂pH∂βt​NtA​(t)​NtD​(t)+∂aH∂β​NA​(t)​ND​(t)​d​t,J_{(\beta\alpha)}^{AC}=\int_{0}^{T}-\frac{\partial a_{H}}{\partial\alpha}N^{A}(t)N^{C}(t)dt;\qquad J_{(\beta\beta)}^{AD}=\int_{0}^{T}-\frac{\partial p_{H}}{\partial\beta_{t}}N^{A}_{t}(t)N^{D}_{t}(t)+\frac{\partial a_{H}}{\partial\beta}N^{A}(t)N^{D}(t)dt,(39)

the Newton-Raphson system, with unknown coefficientsd​αCd\alpha^{C}andd​βDd\beta^{D}, is given by(J(α​α)A​CJ(α​β)A​DJ(β​α)A​CJ(β​β)A​D)​(d​αCd​βD)=−(R(α)AR(β)A),\begin{pmatrix}J_{(\alpha\alpha)}^{AC}&J_{(\alpha\beta)}^{AD}\\
&\\
J_{(\beta\alpha)}^{AC}&J_{(\beta\beta)}^{AD}\end{pmatrix}\begin{pmatrix}d\alpha^{C}\\
\\
d\beta^{D}\end{pmatrix}=-\begin{pmatrix}R_{(\alpha)}^{A}\\
\\
R_{(\beta)}^{A}\end{pmatrix},(40)

whereR(α)AR_{(\alpha)}^{A}andR(β)AR_{(\beta)}^{A}are defined by (32) and (33), respectively.
Finally, after each Newton-Raphson iteration, the dual unknown coefficients are updated according toαC​(𝗌n+1)=αC​(𝗌n)+Δ​𝗌n​d​αC\displaystyle\alpha^{C}(\mathsf{s}_{n+1})=\alpha^{C}(\mathsf{s}_{n})+{\Delta\mathrm{\mathsf{s}}_{n}}d\alpha^{C}(41)βD​(𝗌n+1)=βD​(𝗌n)+Δ​𝗌n​d​βD,\displaystyle\beta^{D}(\mathsf{s}_{n+1})=\beta^{D}(\mathsf{s}_{n})+{\Delta\mathrm{\mathsf{s}}_{n}}d\beta^{D},

whereΔ​𝗌n\Delta\mathsf{s}_{n}is the step size determined (as in the gradient flow phase) by satisfying the DtP zone condition (24) and having a non increasingL2L^{2}norm of the residual moving from instant𝗌n\mathsf{s}_{n}to𝗌n+1\mathsf{s}_{n+1}. The implementation details of the computational scheme are shown in the algorithm presented in Table1.Algorithm: Gradient Flow & Newton-Raphson IterationsInitialization:Setcpc_{p},csc_{s},cac_{a},t​o​lD​t​Ptol_{DtP},t​o​lN​Rtol_{NR},t​o​ltol,Δ​𝗌m​i​n\Delta\mathsf{s}_{min},Δ​𝗌i​n​i​t\Delta\mathsf{s}_{init}Set initial base states (k=1k=1):p¯1=P0¯\bar{p}_{1}=\bar{P_{0}},s¯1=S0¯\bar{s}_{1}=\bar{S_{0}},a¯1=A0¯\bar{a}_{1}=\bar{A_{0}}SetNe​l​e​mN_{elem}, assemble mass matrixMM1)kthk_{\text{th}}stage:1a.Set𝗌0=0\mathsf{s}_{0}=01b.SetαkB​(𝗌0)=0\alpha_{k}^{B}(\mathsf{s}_{0})=0andβkB​(𝗌0)=0\beta_{k}^{B}(\mathsf{s}_{0})=0∀B\forall B(i.e.,Dk​(𝗌0)=0D^{k}(\mathsf{s}_{0})=0)1c.Setp¯kB​(𝗌0)=pHk−1B​(𝗌~k−1∗)\bar{p}_{k}^{B}(\mathsf{s}_{0})=p^{B}_{H_{k-1}}(\tilde{\mathsf{s}}^{*}_{k-1}),s¯kB​(𝗌0)=sHk−1B​(𝗌~k−1∗)\bar{s}_{k}^{B}(\mathsf{s}_{0})=s^{B}_{H_{k-1}}(\tilde{\mathsf{s}}^{*}_{k-1})anda¯kB​(𝗌0)=aHk−1B​(𝗌~k−1∗)\bar{a}_{k}^{B}(\mathsf{s}_{0})=a^{B}_{H_{k-1}}(\tilde{\mathsf{s}}^{*}_{k-1})∀B\forall B(i.e.,U¯k​(𝗌0)=UHk−1​(𝗌~k−1∗)\bar{U}^{k}(\mathsf{s}_{0})=U^{H_{k-1}}(\tilde{\mathsf{s}}^{*}_{k-1}))1d.SetΔ𝗌k=Δ​𝗌i​n​i​t\Delta_{\mathsf{s}_{k}}=\Delta\mathsf{s}_{init}1e.Solve DtPmapusing (1b) and (1c) to obtainpHk​(𝗌0)p_{H_{k}}(\mathsf{s}_{0}),sHk​(𝗌0)s_{H_{k}}(\mathsf{s}_{0})andaHk​(𝗌0)a_{H_{k}}(\mathsf{s}_{0})1f.Compute residual (32)-(33), evaluate itsL2L_{2}norm, define it as|r​h​s|k​(𝗌0)|rhs|_{k}(\mathsf{s}_{0})2) Gradient Flow/Newton-Raphson Iterations:2a.Forn≥0n\geq 0:i.if|r​h​s|k​(𝗌n)≥t​o​lN​R|rhs|_{k}(\mathsf{s}_{n})\geq tol_{NR}:Gradient Flow: Solve Eq.35→\rightarrowdual guess:α∗B​(𝗌n+1)\alpha_{*}^{B}(\mathsf{s}_{n+1}),β∗B​(𝗌n+1)\beta_{*}^{B}(\mathsf{s}_{n+1})else: Newton-Raphson: Solve Eq.40→\rightarrowdual guess:α∗B​(𝗌n+1)\alpha_{*}^{B}(\mathsf{s}_{n+1}),β∗B​(𝗌n+1)\beta_{*}^{B}(\mathsf{s}_{n+1})ii.Solve DtPmapusingα∗B​(𝗌n+1)\alpha_{*}^{B}(\mathsf{s}_{n+1}),β∗B​(𝗌n+1)\beta_{*}^{B}(\mathsf{s}_{n+1})→\rightarrowobtainpHk​(𝗌n+1)p_{H_{k}}(\mathsf{s}_{n+1}),sHk​(𝗌n+1)s_{H_{k}}(\mathsf{s}_{n+1}),aHk​(𝗌n+1)a_{H_{k}}(\mathsf{s}_{n+1})iii.ifaHk​(𝗌n+1)>−ca+t​o​lD​t​Pa_{H_{k}}(\mathsf{s}_{n+1})>-c_{a}+tol_{DtP}(DtP zone check):Compute|r​h​s|k​(𝗌n+1)|rhs|_{k}(\mathsf{s}_{n+1})if|r​h​s|k​(𝗌n+1)≤|r​h​s|k​(𝗌n)|rhs|_{k}(\mathsf{s}_{n+1})\leq|rhs|_{k}(\mathsf{s}_{n})(descent condition check):Accept and save dual guess:αB​(𝗌n+1)=α∗B​(𝗌n+1)\alpha^{B}(\mathsf{s}_{n+1})=\alpha_{*}^{B}(\mathsf{s}_{n+1}),βB​(𝗌n+1)=β∗B​(𝗌n+1)\beta^{B}(\mathsf{s}_{n+1})=\beta_{*}^{B}(\mathsf{s}_{n+1})Save|r​h​s|k​(𝗌n+1)|rhs|_{k}(\mathsf{s}_{n+1})Save time:𝗌n+1=𝗌n+Δ​𝗌n\mathsf{s}_{n+1}=\mathsf{s}_{n}+\Delta\mathsf{s}_{n}if|r​h​s|k​(sn+1)≤t​o​l|rhs|_{k}(s_{n+1})\leq tol:returnpHk​(𝗌n+1)p_{H_{k}}(\mathsf{s}_{n+1}),sHk​(𝗌n+1)s_{H_{k}}(\mathsf{s}_{n+1}),aHk​(𝗌n+1)a_{H_{k}}(\mathsf{s}_{n+1})—Convergence Achievedelse: SetΔ​𝗌n+1=Δ​𝗌n\Delta\mathsf{s}_{n+1}=\Delta\mathsf{s}_{n},n=n+1n=n+1, go to2a.ielse(descent fails): SetΔ​𝗌n=Δ​𝗌n/2\Delta\mathsf{s}_{n}=\Delta\mathsf{s}_{n}/2ifΔ​𝗌n≤Δ​𝗌m​i​n\Delta\mathsf{s}_{n}\leq\Delta\mathsf{s}_{min}: Set𝗌~k∗=𝗌n\tilde{\mathsf{s}}^{*}_{k}=\mathsf{s}_{n},p¯kB​(𝗌~k∗)=pHkB​(sn)\bar{p}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=p^{B}_{H_{k}}(s_{n}),
s¯kB​(𝗌~k∗)=sHkB​(𝗌n)\bar{s}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=s^{B}_{H_{k}}(\mathsf{s}_{n})anda¯kB​(𝗌~k∗)=aHkB​(𝗌n)\bar{a}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=a^{B}_{H_{k}}(\mathsf{s}_{n}), setk=k+1k=k+1, go to1else: Keepn=nn=n, go to2a.ielse(outside DtP zone): SetΔ​𝗌n=Δ​sn/2\Delta\mathsf{s}_{n}=\Delta s_{n}/2ifΔ​𝗌n≤Δ​𝗌m​i​n\Delta\mathsf{\mathsf{s}}_{n}\leq\Delta\mathsf{\mathsf{s}}_{min}: Set𝗌~k∗=𝗌n\tilde{\mathsf{s}}^{*}_{k}=\mathsf{\mathsf{s}}_{n},p¯kB​(𝗌~k∗)=pHkB​(𝗌n)\bar{p}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=p^{B}_{H_{k}}(\mathsf{s}_{n}),
s¯kB​(𝗌~k∗)=sHkB​(𝗌n)\bar{s}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=s^{B}_{H_{k}}(\mathsf{s}_{n})anda¯kB​(𝗌~k∗)=aHkB​(𝗌n)\bar{a}_{k}^{B}(\tilde{\mathsf{s}}^{*}_{k})=a^{B}_{H_{k}}(\mathsf{s}_{n}), setk=k+1k=k+1, go to1else: Keepn=nn=n, go to2a.iTable 1:Algorithm: Gradient Flow & Newton-Raphson Iterations

## 3.1Results

This Section presents numerical results for two examples, both involving the monotonically increasing external loadl​(t)=l0​t,l(t)=l_{0}\,t,(42)

wherel0l_{0}corresponds to the loading rate applied to the bar. The prescribed part of the plastic constitutive evolution is characterized by the response functionfc​(t)=(σ​(t)σ0)m​c​(t),f^{c}(t)=\left(\frac{\sigma(t)}{\sigma_{0}}\right)^{m}c(t),(43)

whereσ0\sigma_{0}is the initial yield stress of the material. We consider the casesm=1m=1corresponding to a rate-sensitive material, andm=0.1m=0.1to a rate insensitive material.
In (43),ccis a modulating function defined asc​(t)=γ^​g​(t),c(t)=\hat{\gamma}\,g(t),(44)

withγ^\hat{\gamma}being a dimensional constant (cf., Sec.2) andt↦g​(t)t\mapsto g(t)taking non-dimensional values. Here, the functiongg, shown in Fig.2(a), is intentionally chosen to be strictly negative over a part of the time domain, thereby specifying a plastic behavior that would violate the Second Law (5) if the evolution of plastic strain were given bypt=fcp_{t}=f^{c}(notingl​(t)l(t)is positive in the same domain and (2)). Of course, prescribing part of the plastic strain evolution as an explicit function of time is somewhat physically unrealistic. We adopt this simplification here in order to deliberately trigger a violation on the Second Law, so as to test whether our theoretical formalism and its computational implementation are able to correct such a violation.

Given the response function of the form (43) and noting (2),fcf^{c}becomes a specified function of time. In a more general problem,fcf^{c}would instead be determined implicitly by the solution and cannot be directly prescribed.
Using this constitutive set up, numerical solutions for the functionspp,ssandaawere obtained, and the total strainuxu_{x}was computed from (4) asux=l0​tE+pu_{x}=\frac{l_{0}t}{E}+p, whereEEis the Young’s modulus of the bar material.

We choose a time scaleT0T_{0}such thatT0​l0/σ0=1T_{0}l_{0}/\sigma_{0}=1, which suffices to show the main events of interest in the simulations. The numerical solutions presented in this Section were computed with the parameter values listed in Table2.Table 2:Parameter combinations used in the simulations.RatioValueEσ0\frac{E}{\sigma_{0}}1×1031\times 10^{3}γ^1/T0\frac{\hat{\gamma}}{1/T_{0}}1×10−31\times 10^{-3}cpσ0\frac{c_{p}}{\sigma_{0}}1×1031\times 10^{3}csT0\frac{c_{s}}{T_{0}}1×1031\times 10^{3}ca(σ0​T02)\frac{c_{a}}{(\sigma_{0}T_{0}^{2})}1×10151\times 10^{15}\begin{overpic}[width=345.0pt]{ccurve.pdf}
\put(11.0,35.0){ \scalebox{0.64}{
\begin{minipage}{172.5pt}\begin{equation*}g(t/T_{0})=\begin{cases}1&t/T_{0}\leq 1.75\\[4.0pt]
1-1.1\,S_{step}\!\left(\dfrac{t/T_{0}-1.75}{0.125}\right)&1.75<t/T_{0}\leq 1.875\\[8.0pt]
-0.1&1.875<t/T_{0}\leq 2.125\\[4.0pt]
-0.1+1.1\,S_{step}\!\left(\dfrac{t/T_{0}-2.125}{0.125}\right)&2.125<t/T_{0}\leq 2.25\\[4.0pt]
1&t/T_{0}>2.25\end{cases}\end{equation*}\begin{equation*}S_{step}(t)=3t^{2}-2t^{3}\end{equation*}\end{minipage}
}
}
\end{overpic}(a)Curveg​(t)g(t).(b)External load.Figure 2:Curveg​(t)g(t)and external load applied.

For each case, the approximate solutions obtained with the scheme, sayt↦v​(t)t\mapsto v(t), is compared with the analytical solution, sayt↦vr​(t)t\mapsto v^{r}(t), computed using (11a), (11b) and (12). The percent errorve​(t)v_{e}(t)(45) betweenvvandvrv^{r}is also shown, wherem​(vr​(t))m(v^{r}(t))is the mean ofvr​(t)v^{r}(t)in the physical time domain and|vr​(t)||v^{r}(t)|is the absolute value ofvrv^{r}at the time instanttt.ve​(t)={v​(t)−vr​(t)m​(vr​(t))×100[%],|vr​(t)|≤1×10−3v​(t)−vr​(t)vr​(t)×100[%],|vr​(t)|>1×10−3.v_{e}(t)=\begin{cases}\frac{v(t)-v^{r}(t)}{m(v^{r}(t))}\times 100\ [\%],&\qquad|v^{r}(t)|\leq 1\times 10^{-3}\\[4.0pt]
\frac{v(t)-v^{r}(t)}{v^{r}(t)}\times 100\ [\%],&\qquad|v^{r}(t)|>1\times 10^{-3}.\\
\end{cases}(45)

An important point to note about our numerical solution procedure relying on a sequence of convex optimization problems is as follows. Strictly speaking, the numerical scheme does not attempt to discretize the problem defined by (10)-(11), where the solution follows from minimizingℋ\mathcal{H}with the base stateU¯=(0,0,0)\bar{U}=(0,0,0). The scheme instead works with a sequence of functionalsSHS_{H}, parametrized by a corresponding sequence of base states defined by the algorithm. The initial base states for all simulations presented were chosen asU¯=[0,0.1,0]\bar{U}=[0,0.1,0]. The base states¯=0\bar{s}=0is a natural choice to guide the solution to that of (10)-(11). However, since the DtP map forssissH=cs​s¯/(α+cs)s_{H}=c_{s}\bar{s}/(\alpha+c_{s}), settings¯=0\bar{s}=0would forcesH=0s_{H}=0throughout the discrete algorithm, trapping it at this starting value. Consequently, a small non-zero startings¯\bar{s}is used, while remaining close to desired guess. The effect of larger initial values ofs¯\bar{s}is discussed further in this Section. Our numerical experiments, thus, also test if the scheme is able to reproduce the analytical result for the problem (10)-(11), despite this difference in the formulation.

The stress-strain curves obtained for the casesm=1m=1case andm=0.1m=0.1are presented in Figs.3(a)and3(b), with the corresponding error foruxu_{x}shown in Figs.4(a)and4(b). Both curves exhibit an apparent ‘elastic gap,’ where, despite the external load increasing monotonically, the stiffness reverts to a purely elastic valueEE. This behavior is not prescribed, but emerges naturally from the scheme through the activation of the corrective variableaawhich enforces the Second Law (5), as discussed next.(a)Stress-strain curve form=1m=1.(b)Stress-strain curve form=0.1m=0.1.Figure 3:Stress-strain relations.(a)Error form=1m=1.(b)Error form=0.1m=0.1.Figure 4:Error percentage for total strain.

The solution fora​(t)a(t)is shown in Figs.5(a)to6(b). Recall that the constitutive response for the plastic strain rate in this problem is composed of two parts, a completely determined partt↦fc​(t)t\mapsto f^{c}(t)from the boundary condition and (43) defined through a power law and modulated with the functiongg(shown in2(a)), and a corrective partaa, which is instead determined by the scheme. In the time interval whereggbecomes negative, the prescribed partfcf^{c}would drive the dissipation negative, directly violating the Second Law constraint (5), were it to operate in isolation. To correct this, the scheme activatesa​(t)>0a(t)>0within that interval, modifying the constitutive response so as to satisfy the Second Law.(a)a​(t)a(t)form=1m=1.(b)a​(t)a(t)form=0.1m=0.1.Figure 5:Functiona​(t)a(t).(a)Error form=1m=1.(b)Error form=0.1m=0.1.Figure 6:Error percentage fora​(t)a(t).

The effect of this correction is that the constitutive response (8) becomespt=0p_{t}=0in the activation interval. This is shown in Figs.7(a)to8(b), whereppremains constant over the interval wherea​(t)>0a(t)>0andfc<cs​lcaf^{c}<\frac{c_{s}l}{c_{a}}. Thus,d​σd​t=E​d​uxd​t\frac{d\sigma}{dt}=E\frac{du_{x}}{dt}in this interval, and sinceuuis a monotonically increasing function oftthere, we recover the elastic sloped​σd​ux=E\frac{d\sigma}{du_{x}}=Ein the regions with the elastic gaps of Figs.3(a)and3(b). Note that the thresholdcs​lca\frac{c_{s}l}{c_{a}}forfcf^{c}(12) is small but positive in the present simulations sincecs​σ0ca​γ^=1×10−9\frac{c_{s}\sigma_{0}}{c_{a}\hat{\gamma}}=1\times 10^{-9}(see Table2), so the activation interval foraa, shown in Fig.5(a), closely resembles the limit case forfc<0f^{c}<0in (13).(a)Plastic strain form=1m=1.(b)Plastic strain form=0.1m=0.1.Figure 7:Plastic strain.(a)Error form=1m=1.(b)Error form=0.1m=0.1.Figure 8:Error percentage for the plastic strain.

Looking at the dissipated energy,Ed​i​s​s:=s2/2E_{diss}:=s^{2}/2, shown in Figs.9(a)to10(b), it is confirmed that the dissipation remains strictly non-negative throughout the entire time domain for both cases, vanishing only whenpt=0p_{t}=0and recovering positive values once plasticity resumes.

It is also worth noting that, in the interval where the response function is deliberately modified to violate the Second Law, the scheme corrects it throughaaby a minimal amount required to satisfy (5), i.e., to drive the dissipation to precisely zero, rather than to any positive value. This behavior is explained by the large cost that any value ofa≠0a\neq 0incurs in the dual functionalSH​[D]S_{H}[D], through the potentialHHand the corresponding weightcac_{a}, which was chosen to be large in this simulations.(a)Dissipated energy form=1m=1.(b)Dissipated energy form=1m=1case.Figure 9:Dissipated energy.(a)Error form=1m=1.(b)Error form=0.1m=0.1.Figure 10:Error percentage for the dissipated energy.

Regarding numerical accuracy, as shown in Fig.4, the scheme achieves a percent error below0.05%0.05\%for the stress-strain relation in them=1m=1case, and below0.8%0.8\%in them=0.1m=0.1case. The errors forpp, shown in Fig.8, follow the same trend, staying below0.1%0.1\%and1%1\%for both respective cases. As shown in Fig.6, the error foraaremains under0.1%0.1\%over most of the domain, with two localized spikes of up to6%6\%occurring whereggrapidly transitions between its plateau values (see Fig.2(a)). A similar pattern is observed in the dissipated energy curves, where the error is below0.1%0.1\%except for two spikes reaching values up to40%40\%in them=0.1m=0.1case. In both cases, the largest error is localized precisely at those rapid transitions, suggesting that they originate from mesh resolution in that region of the time domain, rather than a cumulative numerical error from the scheme. It is expected that using a finer mesh, or a smoother transition ingg, would help reduce the error in these regions. Of course, a more adapted discretization like a Discontinuous Galerkin scheme for the dual fields would also be appropriate, at higher cost.

It is important to clarify that the numerical scheme recovers a solution that resembles the one analytically obtained in Sec.2which follows from minimizingℋ\mathcal{H}, withU¯=(0,0,0)\bar{U}=(0,0,0)even though the numerical scheme instead minimizesHkH_{k}parametrized by a sequence of base states and, as explained above, requires a non-zero initial value fors¯\bar{s}. The correspondence observed in the solutions is not a coincidence, and is in fact due to the small value used for the initials¯\bar{s}. Numerical experiments (not shown) with initial values ofs¯\bar{s}of the order of1×1061\times 10^{6}converge to a different solution of the primal system, still satisfying force equilibrium, the constitutive equation, and the Second Law, but does not resemble the analytical solution obtained by minimizingℋ\mathcal{H}. This confirms that the initial value of the base state is acting as a selection parameter among infinite possible solutions, and that the small value ofs¯\bar{s}used here guides the scheme toward the desired closed-form solution, within the errors reported above.

## 4Conclusion

In this work we demonstrate the scheme presented in[ach3,acharya2025second,AV_nash]through a specific example: the quasi static response of a rate-dependent elastic-plastic bar whose prescribed constitutive equation was intentionally chosen to violate the Dissipation Inequality. Closed-form and numerical solutions were developed for this problem.

The results show that the proposed scheme is capable of correcting the prescribed constitutive response, through the activation of the variableaa, to satisfy the Second Law (Dissipation Inequality) at every instant, while solving for the plastic strainppand the dissipated energys2/2s^{2}/2in a well-set manner. This correction is achieved by using only the minimum amount of thecontrolvariableaanecessary to restore non-negative dissipation which, in this case, drives the dissipation to exactly zero. The resulting stress-strain relations exhibit an elastic gap, which emerges as a direct consequence of the plastic strain remaining constant whileaais active.

The close resemblance between the numerical and closed-form solutions is a consequence of the small initial value ofs¯\bar{s}used. As mentioned in Section3.1, the initial base state value acts as a selection parameter among the infinite family of solutions of the primal system, and larger initial values ofs¯\bar{s}converged instead to different solutions, compared to the analytical case. The numerical solutions obtained with the gradient flow cum Newton-Raphson scheme, for bothm=1m=1andm=0.1m=0.1cases, closely reproduce the analytical answer, achieving errors below0.1%0.1\%throughout the domain, and only locally increasing where the modulating functionggrapidly transitions between positive and negative values.

These results provide a first numerical confirmation that the dual variational principle proposed in[acharya2025second], and the scheme proposed in[AV_nash]are capable of enforcing the Second Law of Thermodynamics in a problem where the Second Law may not be satisfied in some process, using the constitutive model deemed adequate for the purpose. Short of improving the physics of the specification, say due to the absence of more reliable information and to avoid further ad-hoc phenomenology, one remedy involves the approach adopted herein. In the specific problem considered, the scheme results in the occurrence of ‘elastic gaps’ in stress-strain response, reminiscent of behavior in some strain-gradient plasticity theories[FHW]. However, the main applications of the technique are expected to be where the restrictions arising from the Second Law on constitutive functions become extremely complex due to the intricate nature of the mechanics of the model, or in the coupling of established models for disparate phenomena, or in implementing postulates like maximum dissipation as a selection criterion in the analysis of nonlinear transport phenomena.

## References

## 


- 


Major funding support from
