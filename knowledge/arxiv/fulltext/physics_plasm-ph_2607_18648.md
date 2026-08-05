# Current-Sheet Formation in Electron Magnetohydrodynamics with Split Fractional Dissipation

**arXiv ID**: 2607.18648v1
**Authors**: Ruimeng Hu, Qirui Peng, Xu Yang
**Published**: 2026-07-21
**Categories**: physics.plasm-ph, math.NA
**HTML URL**: https://arxiv.org/html/2607.18648v1

## Abstract

Thin current sheets are central small-scale structures in electron magnetohydrodynamics (EMHD), closely associated with energy dissipation and fast magnetic reconnection at electron scales. We study their formation numerically in a $2\frac{1}{2}$-dimensional EMHD system on a periodic domain with split fractional dissipation, where the magnetic potential and the vertical magnetic component are damped separately. The local theory is governed by a symmetric combined damping balance, but the numerical onset of small-scale growth need not follow this symmetry. A scaling analysis identifies the out-of-plane current as the primary concentration observable, since it is regularized only through the magnetic-potential equation. Using a validated Fourier pseudospectral exponential time-differencing solver with resolution-controlled diagnostics, we find a clear decay/concentration dichotomy. The onset boundary is markedly asymmetric: current-sheet formation appears to be controlled mainly by damping of the magnetic potential, rather than by the combined damping strength. The analyticity strip collapses to the grid scale, the concentration sharpens under grid refinement, and the observed growth is consistent with an energy-critical self-similar rate, with exponent near three. These experiments indicate that magnetic-potential damping is the apparent binding constraint for current-sheet concentration, refining the symmetric sum picture.

## Full Text

Current-Sheet Formation in Electron Magnetohydrodynamics with Split Fractional Dissipation

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18648v1 [physics.plasm-ph] 21 Jul 2026

## Current-Sheet Formation in Electron Magnetohydrodynamics
with Split Fractional DissipationRuimeng HuDepartment of Mathematics and
Department of Statistics and Applied Probability,
University of California, Santa Barbara, CA 93106, USA.rhu@ucsb.eduQirui PengDepartment of Mathematics,
University of California, Santa Barbara, CA 93106, USA.qpeng9@ucsb.eduXu YangDepartment of Mathematics,
University of California, Santa Barbara, CA 93106, USA.xy6@ucsb.edu

## Abstract

Thin current sheets are central small-scale structures in electron magnetohydrodynamics (EMHD), closely associated with energy dissipation and fast magnetic reconnection at electron scales. We study their formation numerically in a2⁤122\frac{1}{2}-dimensional EMHD system on a periodic domain with split fractional dissipation, where the magnetic potential and the vertical magnetic component are damped separately. The local theory is governed by a symmetric combined damping balance, but the numerical onset of small-scale growth need not follow this symmetry. A scaling analysis identifies the out-of-plane current as the primary concentration observable, since it is regularized only through the magnetic-potential equation. Using a validated Fourier pseudospectral exponential time-differencing solver with resolution-controlled diagnostics, we find a clear decay/concentration dichotomy. The onset boundary is markedly asymmetric: current-sheet formation appears to be controlled mainly by damping of the magnetic potential, rather than by the combined damping strength. The analyticity strip collapses to the grid scale, the concentration sharpens under grid refinement, and the observed growth is consistent with an energy-critical self-similar rate, with exponent near three. These experiments indicate that magnetic-potential damping is the apparent binding constraint for current-sheet concentration, refining the symmetric sum picture.

Keywords:Electron magnetohydrodynamics; Hall effect; fractional dissipation; current-sheet formation; self-similar scaling.

Mathematics Subject Classification:76W05, 35Q35, 65M70, 35R11.

## 1Introduction

Thin current sheets are the central coherent structures of electron magnetohydrodynamics (EMHD), the fluid model of plasma dynamics at scales below the ion inertial length, where the magnetic field is frozen into the electron flow[14]. Their formation is closely associated with energy dissipation and fast magnetic reconnection at electron scales, and simulations of electron-MHD turbulence show the current density organizing into sheet-like structures across scales[3,4]. This paper asks a quantitative question about the gate to this process: when the two magnetic degrees of freedom of the2⁤122\frac{1}{2}-dimensional model are damped through separate dissipation channels, which channel controls the onset of current-sheet formation? The split-dissipation system itself is a recently introduced model: its local well-posedness was established only in[25]. The experiments below show that it already exhibits a distinctive nonlinear phenomenology, including an asymmetric onset boundary, amplitude-dependent thresholds, and self-similar concentration at an energy-critical rate. It therefore provides a minimal setting in which the role of damping structure in small-scale formation can be isolated and quantified.

The mathematical difficulty is set by the Hall term. The parent Hall–magnetohydrodynamics (Hall–MHD) system models plasma dynamics in regimes where the Hall effect becomes relevant at small length scales; relative to classical magnetohydrodynamics, the Hall term carries one additional spatial derivative of the magnetic field, producing a genuinely quasilinear difficulty that dominates both the analysis and the numerics of these equations[1,5]. EMHD is the fluid-free subsystem obtained by retaining the Hall dynamics while neglecting the ion velocity; it serves as a standard model for small-scale plasma motion and whistler-type phenomena[3,4].

We study a2⁤122\frac{1}{2}-dimensional (2.5D) reduction in which the magnetic field is independent of the vertical coordinate and is written as𝑩=∇×(a​𝒆z)+b​𝒆z=(ay,−ax,b),\bm{B}\;=\;\nabla\times(a\,\bm{e}_{z})+b\,\bm{e}_{z}\;=\;(a_{y},\,-a_{x},\,b),(1.1)

witha=a​(x,y,t)a=a(x,y,t)the magnetic potential andb=b​(x,y,t)b=b(x,y,t)the vertical magnetic component. Allowing distinct fractional dissipation on the two scalar components yields the system∂ta+ay​bx−ax​by\displaystyle\partial_{t}a+a_{y}b_{x}-a_{x}b_{y}=−Λα​a,\displaystyle=-\Lambda^{\alpha}a,(1.2a)∂tb−ay​Δ​ax+ax​Δ​ay\displaystyle\partial_{t}b-a_{y}\Delta a_{x}+a_{x}\Delta a_{y}=−Λβ​b,\displaystyle=-\Lambda^{\beta}b,(1.2b)

on(0,∞)×𝕋2(0,\infty)\times\mathbb{T}^{2}, whereΛs:=(−Δ)s/2\Lambda^{s}:=(-\Delta)^{s/2}is the Fourier multiplier with symbol|k|s|k|^{s},k∈ℤ2k\in\mathbb{Z}^{2}, and throughout0<α,β<20<\alpha,\beta<2. Fractional orders below two interpolate between the undamped and fully resistive regimes and serve as a standard mathematical proxy for weakened or anomalous damping; assigning distinct orders to the two components turns the question of which damping channel binds into a quantitative one.

## Related literature.

A systematic local well-posedness theory for three-dimensional Hall–MHD was developed by[5], with blow-up criteria and small-data results in[6]; lower-regularity and critical-space theories followed in[12,13,21,10]. The role of weakened, fractional magnetic diffusion was clarified by[7], whose Littlewood–Paley and Besov estimates show that the full Laplacian dissipation can be relaxed to a fractional one. For the fluid-free EMHD subsystem, the Hall nonlinearity carries a derivative falling on the current∇×𝑩\nabla\times\bm{B}, and the behavior is especially delicate without resistivity:[18]proved ill-posedness near degenerate stationary states, while[19]established well-posedness around nonzero uniform fields;[11]studied a resistive22D EMHD setting near a steady state. Recently,[9]proved local well-posedness of the2.52.5D EMHD system (1.2) when one of the two equations carries a full Laplacian dissipation. In[25], the second author established the local-well-posedness under a split fractional condition0<α,β<2,α+β>2,0<\alpha,\beta<2,\qquad\alpha+\beta>2,(1.3)

in which case neither component need carry a full derivative of dissipation: the combined smoothing of the two fractional operators suffices to control the Hall nonlinearity. The mechanism is an exact cancellation between the leading low–high frequency interactions of the two equations, after which the residual terms close in an asymmetric energy in whichaais estimated one derivative abovebb. Beyond the deterministic setting, the well-posedness theory has recently been extended to a relaxed EMHD model with random diffusion[16]and to the three-dimensional stochastic EMHD system, for which maximal pathwise solutions were constructed[17].

The condition (1.3) is a sufficient condition for local well-posedness; it closes the known energy estimates but does not, by itself, establish global regularity, nor does it preclude small-scale growth or finite-time blow-up forα+β>2\alpha+\beta>2. Our aim is therefore not to test a global regularity threshold but to ask a sharper, complementary question: when small scales do form, which of the two dissipations controls their onset, and does the symmetric balanceα+β\alpha+\betathat governs the analysis also govern the observed numerical onset of current-sheet growth? We address this through a combination of scaling heuristics and resolution-controlled numerical experiments, taking care to distinguish what the computations show (a concentration mechanism and its parametric dependence) from what they cannot settle (the existence of a genuine finite-time singularity). Numerical studies of small-scale and near-singular dynamics are by now a mature tool in the analysis of nonlinear PDEs: tracking complex singularities through spectral data[26], continuation criteria of Beale–Kato–Majda type[2], and high-resolution investigations of near-singular dynamics[22]. We adopt that toolkit here, with particular attention to separating genuine small-scale structure from under-resolution.

In this work, we combine scaling heuristics with resolution-controlled numerical experiments to study how the split dissipations affect small-scale formation in the2.52.5D EMHD system. The scaling analysis identifies three competing mechanisms: a per-equation criticality, the symmetric sumα+β\alpha+\betaarising from the known cancellation-based local theory, and a possibleα\alpha-controlled mechanism associated with the out-of-plane currentΔ​a\Delta a. The numerical experiments point toward the last scenario: the observed current-sheet concentration occurs primarily inΔ​a\Delta aand appears more sensitive to the dissipation on the magnetic potential than to the sumα+β\alpha+\beta. The fitted concentration rate is consistent with the energy-critical scalingq∗≈3q^{*}\approx 3. The scaling analysis is developed in Section3; the solver, its validation, and the diagnostic and resolution-control protocol in Section4and Section5; and the numerical results in Section6.

A structure-preserving forward solver for (1.2) based on gradient recovery is developed in the companion work[15]; the present paper is concerned not with method design but with using high-accuracy computation to investigate how the local-theory balance (1.3) relates to the observed onset of small-scale growth.

## 2The2.52.5D EMHD system

This section introduces the notation and structural identities used throughout the paper: the transport form of the system, the current density, and the magnetic-energy balance.

## 2.1Transport form and the Hall nonlinearity

Introduce the in-plane velocityu:=∇⟂b=(−by,bx)u:=\nabla^{\perp}b=(-b_{y},b_{x}), which is divergence free,∇⋅u=0\nabla\cdot u=0. Sinceu⋅∇a=−by​ax+bx​ay=ay​bx−ax​byu\cdot\nabla a=-b_{y}a_{x}+b_{x}a_{y}=a_{y}b_{x}-a_{x}b_{y}, equation (1.2a) is a transport–dissipation equation for the magnetic potential,∂ta+u⋅∇a=−Λα​a,u=∇⟂b.\partial_{t}a+u\cdot\nabla a=-\Lambda^{\alpha}a,\qquad u=\nabla^{\perp}b.(2.1)

For the second equation, using thatΔ\Deltacommutes with∂x,∂y\partial_{x},\partial_{y}we haveax​Δ​ay−ay​Δ​ax=ax​(Δ​a)y−ay​(Δ​a)x={a,Δ​a}a_{x}\Delta a_{y}-a_{y}\Delta a_{x}=a_{x}(\Delta a)_{y}-a_{y}(\Delta a)_{x}=\{a,\Delta a\}, where{f,g}:=∇⟂f⋅∇g=fx​gy−fy​gx\{f,g\}:=\nabla^{\perp}f\cdot\nabla g=f_{x}g_{y}-f_{y}g_{x}is the Poisson bracket. Hence∂tb+∇⟂a⋅∇(Δ​a)=−Λβ​b.\partial_{t}b+\nabla^{\perp}a\cdot\nabla(\Delta a)=-\Lambda^{\beta}b.(2.2)

The Hall nonlinearity∇⟂a⋅∇(Δ​a)\nabla^{\perp}a\cdot\nabla(\Delta a)in (2.2) pairs one derivative ofaaagainst three derivatives ofaa; this is the quasilinear, derivative-losing structure responsible both for the difficulty of the well-posedness theory and for the appearance ofaaat one higher level of regularity thanbbin the energy.

## 2.2Current density: the singularity observable

The current density associated with the ansatz (1.1) is𝑱=∇×𝑩=(by,−bx,−Δ​a),\bm{J}=\nabla\times\bm{B}=(b_{y},\,-b_{x},\,-\Delta a),(2.3)

so that the in-plane current is∇⟂b\nabla^{\perp}band the out-of-plane current is−Δ​a-\Delta a. The scalar‖𝑱‖L∞​(t)∼max⁡(‖∇b‖L∞,‖Δ​a‖L∞)\left\|\bm{J}\right\|_{L^{\infty}}(t)\;\sim\;\max\!\big(\left\|\nabla b\right\|_{L^{\infty}},\,\left\|\Delta a\right\|_{L^{\infty}}\big)(2.4)

is the EMHD analogue of the vorticity maximum in incompressible flow and serves as our primary singularity observable. Tracking‖∇b‖L∞\left\|\nabla b\right\|_{L^{\infty}}and‖Δ​a‖L∞\left\|\Delta a\right\|_{L^{\infty}}separately resolves whether an incipient singularity is of in-plane or out-of-plane (current-sheet) type.

## 2.3Conserved magnetic energy

Define the magnetic energyM​(t):=12​∫𝕋2(|∇a|2+b2)​𝑑x=12​∫𝕋2|𝑩|2​𝑑x.M(t)\;:=\;\tfrac{1}{2}\int_{\mathbb{T}^{2}}\!\big(|\nabla a|^{2}+b^{2}\big)\,dx\;=\;\tfrac{1}{2}\int_{\mathbb{T}^{2}}\!|\bm{B}|^{2}\,dx.(2.5)

## Proposition 2.1(Magnetic-energy balance).

For smooth solutions of (1.2),dd​t​M​(t)=−‖Λ1+α/2​a‖L22−‖Λβ/2​b‖L22≤0,\frac{d}{dt}M(t)=-\left\|\Lambda^{1+\alpha/2}a\right\|_{L^{2}}^{2}-\left\|\Lambda^{\beta/2}b\right\|_{L^{2}}^{2}\;\leq\;0,(2.6)

and in particularM​(t)M(t)is conserved for the dissipationless system(α=β=0)(\alpha=\beta=0).

## Proof.

Differentiating (2.5) and integrating by parts,dd​t​M=∫∇a⋅∇​∂ta+∫b​∂tb=−∫Δ​a​∂ta+∫b​∂tb.\frac{d}{dt}M=\int\nabla a\cdot\nabla\partial_{t}a+\int b\,\partial_{t}b=-\int\Delta a\,\partial_{t}a+\int b\,\partial_{t}b.

Insert∂ta=−u⋅∇a−Λα​a\partial_{t}a=-u\cdot\nabla a-\Lambda^{\alpha}aand∂tb=−∇⟂a⋅∇Δ​a−Λβ​b\partial_{t}b=-\nabla^{\perp}a\cdot\nabla\Delta a-\Lambda^{\beta}b. The dissipative terms give∫Δ​a​Λα​a=−‖Λ1+α/2​a‖L22\int\Delta a\,\Lambda^{\alpha}a=-\left\|\Lambda^{1+\alpha/2}a\right\|_{L^{2}}^{2}and−∫b​Λβ​b=−‖Λβ/2​b‖L22-\int b\,\Lambda^{\beta}b=-\left\|\Lambda^{\beta/2}b\right\|_{L^{2}}^{2}. It remains to show the nonlinear terms cancel. The transport term contributes∫Δ​a​(u⋅∇a)\int\Delta a\,(u\cdot\nabla a), while the Hall term contributes−∫b​∇⟂a⋅∇Δ​a=∫Δ​a​(∇⟂a⋅∇b)-\int b\,\nabla^{\perp}a\cdot\nabla\Delta a=\int\Delta a\,(\nabla^{\perp}a\cdot\nabla b), where we integrated by parts using∇⋅∇⟂a=0\nabla\cdot\nabla^{\perp}a=0. Nowu⋅∇a=∇⟂b⋅∇a=−(ax​by−ay​bx)u\cdot\nabla a=\nabla^{\perp}b\cdot\nabla a=-(a_{x}b_{y}-a_{y}b_{x})and∇⟂a⋅∇b=ax​by−ay​bx\nabla^{\perp}a\cdot\nabla b=a_{x}b_{y}-a_{y}b_{x}, so the two integrands are∫Δ​a​[−(ax​by−ay​bx)]\int\Delta a\,[-(a_{x}b_{y}-a_{y}b_{x})]and∫Δ​a​(ax​by−ay​bx)\int\Delta a\,(a_{x}b_{y}-a_{y}b_{x}), which sum to zero. This proves (2.6).
∎

Proposition2.1plays two roles below. Analytically,MMis the base coercive quantity on which the higher-order well-posedness energy of[25]is built. Numerically, the structural identity behinddd​t​M=0\tfrac{d}{dt}M=0, the exact cancellation of the two nonlinear contributions, provides a stringent discrete check (Section4.3): the time integrator need not conserveMMexactly as a discrete invariant, but any implementation that fails to reproduce this nonlinear energy cancellation to round-off has the wrong nonlinear structure and cannot be trusted in the near-critical regime.

## 3Scaling, criticality, and competing predictions

This section derives the self-similar scaling of the dissipationless system, identifies the criticality of each fractional dissipation, and extracts three competing threshold predictions that the experiments will distinguish.

## 3.1Self-similar scaling of the dissipationless system

Consider the dissipationless system∂ta+∇⟂b⋅∇a=0,∂tb+∇⟂a⋅∇Δ​a=0.\partial_{t}a+\nabla^{\perp}b\cdot\nabla a=0,\qquad\partial_{t}b+\nabla^{\perp}a\cdot\nabla\Delta a=0.(3.1)

## Proposition 3.1(Scaling family).

If(a,b)(a,b)solves (3.1), then for everyλ>0\lambda>0and everyq∈ℝq\in\mathbb{R}so do the rescaled fieldsaλ​(x,t)=λp​a​(xλ,tλq),bλ​(x,t)=λr​b​(xλ,tλq),p=3−q,r=2−q.a_{\lambda}(x,t)=\lambda^{p}\,a\!\Big(\frac{x}{\lambda},\frac{t}{\lambda^{q}}\Big),\qquad b_{\lambda}(x,t)=\lambda^{r}\,b\!\Big(\frac{x}{\lambda},\frac{t}{\lambda^{q}}\Big),\qquad p=3-q,\quad r=2-q.(3.2)

## Proof.

Writeξ=x/λ\xi=x/\lambda,σ=t/λq\sigma=t/\lambda^{q}. In (1.2a) with no dissipation,∂taλ∼λp−q\partial_{t}a_{\lambda}\sim\lambda^{p-q}while∇⟂bλ⋅∇aλ∼λ(r−1)+(p−1)=λp+r−2\nabla^{\perp}b_{\lambda}\cdot\nabla a_{\lambda}\sim\lambda^{(r-1)+(p-1)}=\lambda^{p+r-2}; equality of exponents forcesr=2−qr=2-q. In the second equation,∂tbλ∼λr−q\partial_{t}b_{\lambda}\sim\lambda^{r-q}while∇⟂aλ⋅∇Δ​aλ∼λ(p−1)+(p−3)=λ2​p−4\nabla^{\perp}a_{\lambda}\cdot\nabla\Delta a_{\lambda}\sim\lambda^{(p-1)+(p-3)}=\lambda^{2p-4}; equality forcesr−q=2​p−4r-q=2p-4,i.e.p=3−qp=3-qafter substitutingr=2−qr=2-q.
∎

Two consequences of (3.2) fix the relevant observables. First, the current scales isotropically across its in-plane and out-of-plane parts:Δ​aλ∼λp−2=λ1−q\Delta a_{\lambda}\sim\lambda^{p-2}=\lambda^{1-q}and∇bλ∼λr−1=λ1−q\nabla b_{\lambda}\sim\lambda^{r-1}=\lambda^{1-q}, so‖𝑱‖L∞∼λ1−q,\left\|\bm{J}\right\|_{L^{\infty}}\sim\lambda^{1-q},(3.3)

and a focusing collapse (length scaleλ→0\lambda\to 0with‖𝑱‖L∞→∞\left\|\bm{J}\right\|_{L^{\infty}}\to\infty) requiresq>1q>1. This identifies𝑱\bm{J}as the natural normalizing quantity for dynamic rescaling (Section5.3). Second, sincep=r+1p=r+1, the two contributions to the magnetic energy scale identically,M∼λ2​p=λ6−2​qM\sim\lambda^{2p}=\lambda^{6-2q}, consistent with Proposition2.1. The exponent6−2​q6-2qseparates three regimes: forq<3q<3the magnetic energy of the collapsing core vanishes asλ→0\lambda\to 0(energy-subcritical collapse),q=3q=3is the energy-critical scaling at whichMMis exactly scale-invariant, andq>3q>3would require a diverging core energy and is incompatible with the conserved, finiteMM. The measured exponentq∗≈3q^{*}\approx 3in Section6thus sits at the energy-critical value, a point we return to below.

For later use we denote the temporal power laws implied by a self-similar collapse with exponentqq. If the length scaleL​(t)L(t)closes at the singular timet∗t^{*}in the self-similar fashion of Section5.3, thent∗−t∼Lqt^{*}-t\sim L^{q}, soL∼(t∗−t)1/qL\sim(t^{*}-t)^{1/q}; combining with (3.3) andδ∼L\delta\sim Lfor the analyticity-strip width gives‖𝑱‖L∞∼(t∗−t)−γJ,δ​(t)∼(t∗−t)ν,γJ=q−1q,ν=1q,q=1+γJν.\left\|\bm{J}\right\|_{L^{\infty}}\sim(t^{*}-t)^{-\gamma_{J}},\quad\delta(t)\sim(t^{*}-t)^{\nu},\qquad\gamma_{J}=\frac{q-1}{q},\quad\nu=\frac{1}{q},\qquad q=1+\frac{\gamma_{J}}{\nu}.(3.4)

The individual exponentsγJ\gamma_{J}andν\nudepend on the (extrapolated) singular time: over a narrow fitting window, misplacingt∗t^{*}approximately rescales both fitted exponents by a similar factor, so the ratioγJ/ν\gamma_{J}/\nu, and henceqqthrough (3.4), is far more robust than either exponent alone. We use this in Section6.

## 3.2Criticality of the fractional dissipation

Restoring the dissipation,Λα​aλ∼λp−α\Lambda^{\alpha}a_{\lambda}\sim\lambda^{p-\alpha}is to be compared with the inviscid balanceλp−q\lambda^{p-q}in (1.2a): theaa-dissipation is scalemarginalwhenα=q\alpha=q, scalesubcritical(negligible at small scales, unable to arrest collapse) whenα<q\alpha<q, andsupercritical(regularizing) whenα>q\alpha>q. The identical computation for (1.2b) gives marginality atβ=q\beta=q. Thus, at a self-similar collapse with exponentqq, dimensional analysis applied to each equation in isolation suggests that blow-up can proceed only if bothα<q\alpha<qandβ<q\beta<q, a split-dependent, corner-shaped condition in the(α,β)(\alpha,\beta)square.

## 3.3Three readings, and the role of the out-of-plane current

The corner prediction conflicts with the analytical threshold (1.3), which closes onα+β>2\alpha+\beta>2rather than onmax⁡(α,β)\max(\alpha,\beta). One resolution lies in the cancellation identified in[25]: the leading low–high frequency interactions of the two equations cancel exactly, so the two fractional dissipations are not independently tasked with regularizing their own equation. Instead they supply ajointsmoothing budget, of orderα2\tfrac{\alpha}{2}onaaandβ2\tfrac{\beta}{2}onbbbeyond the energy level, set against the single one-derivative loss of the Hall nonlinearity. Regularity then closes when the combined gain exceeds the loss,α2+β2>1⟺α+β>2,\tfrac{\alpha}{2}+\tfrac{\beta}{2}>1\;\Longleftrightarrow\;\alpha+\beta>2,(3.5)

pointing to the lineα+β=2\alpha+\beta=2rather than the corner{α<q}∩{β<q}\{\alpha<q\}\cap\{\beta<q\}.

There is, however, a third reading that the numerics will favor. The current density (2.3) has an out-of-plane part−Δ​a-\Delta athat carries two derivatives ofaa, against one derivative ofbbin the in-plane part∇⟂b\nabla^{\perp}b; the scaling (3.3) loads both equally, but the higher derivative count makesΔ​a\Delta athe more singular component. Crucially,Δ​a\Delta ais regularized only by theaa-equation dissipationΛα\Lambda^{\alpha}. If blow-up concentrates in the out-of-plane current, that is, in a current sheet inΔ​a\Delta a, then the binding constraint isα\alphaalone, and the onset boundary should be near-vertical in the(α,β)(\alpha,\beta)plane, controlled chiefly by the dissipation on the magnetic potential. These three readings (corner, line, andα\alpha-controlled) make distinct, falsifiable predictions that our experiments are designed to separate.

The conditionα+β>2\alpha+\beta>2is sufficient for local well-posedness[25]; for sufficiently weak dissipation we expect small scales to form and the out-of-plane current to concentrate. We test, in particular, whether the onset of this growth is governed by the symmetric lineα+β=2\alpha+\beta=2or instead primarily by the single exponentα\alpha, as the out-of-plane current argument suggests, and we seek the self-similar exponentq∗q^{*}of the observed concentration. We emphasize that local well-posedness forα+β>2\alpha+\beta>2does not preclude small-scale growth or later blow-up there, soα+β=2\alpha+\beta=2should be read as the threshold of the present theory, not as a proven global regularity boundary.

## 4Numerical method

We integrate (1.2) using a Fourier pseudospectral discretization in space and exponential time differencing in time. This treats the linear fractional dissipation exactly at the modal level while advancing the Hall nonlinearity explicitly. This section describes the scheme and its validation.

## 4.1Spatial discretization

We discretize (1.2) by a Fourier pseudospectral method on𝕋2=[0,2​π)2\mathbb{T}^{2}=[0,2\pi)^{2}withN2N^{2}collocation points and spectral resolution|kx|,|ky|≤N/2|k_{x}|,|k_{y}|\leq N/2. Linear operators act diagonally in Fourier space: the fractional dissipations are the multipliers|k|α|k|^{\alpha}and|k|β|k|^{\beta}, and all derivatives are evaluated spectrally. The Hall nonlinearitiesay​bx−ax​bya_{y}b_{x}-a_{x}b_{y}anday​Δ​ax−ax​Δ​aya_{y}\Delta a_{x}-a_{x}\Delta a_{y}are formed as physical-space products of spectrally computed derivatives and transformed back, with aliasing errors removed by the2/32/3rule[24]. In the most marginal runs we replace the sharp2/32/3cutoff by a smooth high-order exponential filter and verify that reported diagnostics are insensitive to the choice.

## 4.2Time integration

Because the fractional dissipation is linear, diagonal, and stiff, we integrate it exactly through an integrating factor and advance the Hall nonlinearity explicitly with the fourth-order exponential time-differencing Runge–Kutta scheme ETDRK4[8,20]. Writing the system as∂tw^=ℒ​w^+𝒩​(w^)\partial_{t}\hat{w}=\mathcal{L}\hat{w}+\mathcal{N}(\hat{w})withℒ=diag​(−|k|α,−|k|β)\mathcal{L}=\mathrm{diag}(-|k|^{\alpha},-|k|^{\beta}), the modewise integrating factors aree−|k|α​Δ​te^{-|k|^{\alpha}\Delta t}ande−|k|β​Δ​te^{-|k|^{\beta}\Delta t}; the ETDRK4 coefficient (φ\varphi-)functions are evaluated by the contour-integral quadrature of[20]to avoid cancellation error at small|k||k|. The time step is chosen from the stability constraint of the explicit treatment of the Hall term, which is dispersive: the linearized nonlinearity supports whistler-type waves with frequencyω∼|k|2​‖𝑩‖\omega\sim|k|^{2}\,\|\bm{B}\|, so explicit stability requiresΔ​t≲c/(kmax2​‖𝑩‖∞)\Delta t\lesssim c/(k_{\max}^{2}\,\|\bm{B}\|_{\infty}). This dispersive restriction, rather than the comparatively mild fractional stiffness (∼Nα\sim N^{\alpha}withα<2\alpha<2), is the binding one, and it tightens as small scales form; we chooseΔ​t\Delta tconservatively for each run and stop integrating once the resolution gate of Section5.2trips.

## 4.3Validation

We validate the solver by four independent tests, summarized in Table4.1and Figure4.1.

(V1a) Linear dissipation.A single Fourier mode decays at the exact ratee−|k|α​te^{-|k|^{\alpha}t}; the scheme reproduces this to relative error3.6×10−163.6\times 10^{-16}, confirming the fractional symbols.

(V1b) Conservation structure.For the dissipationless system the instantaneous nonlinear energy ratedd​t​M\frac{d}{dt}Mof Proposition2.1must vanish. The two contributions from theaa- andbb-equations cancel to2.8×10−162.8\times 10^{-16}(with and without dealiasing), verifying the signs and structure of the Hall nonlinearity. With dissipation restored, the discrete energy balanceM​(0)−M​(T)=∫0TD​𝑑tM(0)-M(T)=\int_{0}^{T}D\,dt,D=‖Λ1+α/2​a‖L22+‖Λβ/2​b‖L22D=\left\|\Lambda^{1+\alpha/2}a\right\|_{L^{2}}^{2}+\left\|\Lambda^{\beta/2}b\right\|_{L^{2}}^{2}, holds to relative residual5.5×10−75.5\times 10^{-7}(quadrature-limited). We note that the dissipationless system is genuinely ill-posed at the grid scale (the third-derivative Hall term is uncontrolled), so this invariant is verified onresolvedevolutions; it is the energy balance, not exact conservation, that the solver respects in the dissipative regime of interest.

(V2) Convergence.Self-convergence in a smooth, resolved regime confirms fourth-order temporal accuracy (measured rates4.014.01and3.943.94) and spectral spatial accuracy (error7.4×10−47.4\times 10^{-4},1.8×10−51.8\times 10^{-5},1.5×10−71.5\times 10^{-7}atN=16,32,64N=16,32,64).Table 4.1:Solver validation. Each test compares a measured quantity against the
behavior expected for an ETDRK4 Fourier pseudospectral scheme: the first two
tests probe the exact treatment of the linear and inviscid structure (near
machine precision), the third the discrete energy balance under dissipation, and
the last two the temporal and spatial convergence. All tests pass at the
expected levels, establishing that the diagnostics reported below reflect the
dynamics rather than the discretization.TestMeasured quantityExpectedResultLinear decay (V1a)rel. error in mode amplitudemach. prec.3.6×10−163.6\times 10^{-16}Conservation structure (V1b)instantaneousd​M/d​tdM/dt(inviscid)mach. prec.2.8×10−162.8\times 10^{-16}Energy balance (V1b)|M​(0)−M​(T)−∫D​𝑑t|/|Δ​M||M(0){-}M(T)-\!\int\!D\,dt|/|{\Delta M}|quad. accuracy5.5×10−75.5\times 10^{-7}Temporal order (V2)fitted convergence rate44(ETDRK4)4.01,3.944.01,\ 3.94Spatial accuracy (V2)max error,N=16→64N=16{\to}64spectral7.4×10−4​to​1.5×10−77.4{\times}10^{-4}\ \text{to}\ 1.5{\times}10^{-7}Figure 4.1:Solver convergence. (a) Fourth-order temporal accuracy of ETDRK4. (b) Spectral spatial accuracy. Together with the machine-precision conservation tests these establish the solver as a trustworthy instrument before any singularity claim.

## 5Singularity diagnostics and resolution control

The central difficulty of any numerical study of near-singular dynamics is to distinguish genuine small-scale concentration from under-resolution. We address this with a hierarchy of diagnostics required to agree on a common putative singular timet∗t^{*}, together with a resolution-control protocol.

## 5.1Diagnostics
- 1.

Analyticity-strip widthδ​(t)\delta(t).For an analytic field the energy spectrum decays exponentially,log⁡E​(k,t)∼C​(t)−2​δ​(t)​k\log E(k,t)\sim C(t)-2\delta(t)\,kat high wavenumber, whereδ​(t)\delta(t)is the distance from the real axis to the nearest complex-space singularity[26]. A real singularity att∗t^{*}is signalled byδ​(t)↓0\delta(t)\downarrow 0, typically asδ​(t)∼c​(t∗−t)ν\delta(t)\sim c\,(t^{*}-t)^{\nu}. We extractδ​(t)\delta(t)by least-squares fittinglog⁡E​(k,t)\log E(k,t)over the band in which the spectrum lies between10−310^{-3}and10−1010^{-10}of its peak (above round-off, below the energy-containing scales).
- 2.

Current-density growth.We track‖𝑱‖L∞​(t)\left\|\bm{J}\right\|_{L^{\infty}}(t)and its in-plane and out-of-plane parts‖∇b‖L∞\left\|\nabla b\right\|_{L^{\infty}},‖Δ​a‖L∞\left\|\Delta a\right\|_{L^{\infty}}, fitting an algebraic ansatz‖𝑱‖L∞∼(t∗−t)−γJ\left\|\bm{J}\right\|_{L^{\infty}}\sim(t^{*}-t)^{-\gamma_{J}}. In practice we monitor the componentwise proxy of (2.4), which lower-bounds the pointwise supremum of|𝑱||\bm{J}|by at most a factor2\sqrt{2}; in the runs reported the two differ by at most11%11\%and exhibit the same growth behavior.
- 3.

Sobolev energies.We monitorEs​(t)=‖a‖Hs+12+‖b‖Hs2E_{s}(t)=\left\|a\right\|_{H^{s+1}}^{2}+\left\|b\right\|_{H^{s}}^{2}withs=2s=2, the numerical analogue of the asymmetric energy in which the local theory of[25]closes, both to connect the experiments to the analysis and to detect loss of regularity.
- 4.

Beale–Kato–Majda (BKM) integral.A continuation criterion of BKM type[2]suggests monitoring∫0t‖𝑱‖L∞​𝑑τ\int_{0}^{t}\left\|\bm{J}\right\|_{L^{\infty}}\,d\tau; its growth provides an additional consistency check for the fittedt∗t^{*}.
- 5.

Dissipation channels and theHsH^{s}budget.The local theory controls the nonlinearity by the two dissipation normsDa​(t)=‖Λ1+α/2​a‖Hs2,Db​(t)=‖Λβ/2​b‖Hs2.D_{a}(t)=\left\|\Lambda^{1+\alpha/2}a\right\|_{H^{s}}^{2},\qquad D_{b}(t)=\left\|\Lambda^{\beta/2}b\right\|_{H^{s}}^{2}.(5.1)

We monitor these separately, together with the nonlinear inputs to12​dd​t​Es\tfrac{1}{2}\frac{d}{dt}E_{s},𝒩a=−⟨a,∇⟂b⋅∇a⟩Hs+1\mathcal{N}_{a}=-\langle a,\,\nabla^{\perp}b\cdot\nabla a\rangle_{H^{s+1}}and𝒩b=−⟨b,∇⟂a⋅∇Δ​a⟩Hs\mathcal{N}_{b}=-\langle b,\,\nabla^{\perp}a\cdot\nabla\Delta a\rangle_{H^{s}}, and the budget ratio(𝒩a+𝒩b)/(Da+Db)(\mathcal{N}_{a}+\mathcal{N}_{b})/(D_{a}+D_{b}). The ratio is signed: the numerator is negative when the nonlinearity transfers energy out of theHsH^{s}class (in the runs reported this occurs only at the first sample, and negligibly). A ratio persistently above one means the nonlinearity outruns the dissipative capacity in the energy class of the local theory. Throughout, the Sobolev norms are implemented with the inhomogeneous Fourier weights(1+|k|2)s(1+|k|^{2})^{s}; the energy identitydd​t​Es=2​(𝒩a+𝒩b)−2​(‖Λα/2​a‖Hs+12+‖Λβ/2​b‖Hs2)\frac{d}{dt}E_{s}=2(\mathcal{N}_{a}+\mathcal{N}_{b})-2\big(\left\|\Lambda^{\alpha/2}a\right\|_{H^{s+1}}^{2}+\left\|\Lambda^{\beta/2}b\right\|_{H^{s}}^{2}\big)is exact relative to these weights (and holds up to the equivalence of Sobolev weights otherwise), and we verified the implementation against it to a relative5×10−75\times 10^{-7}by centered differencing along the discrete flow.
- 6.

Dyadic shell energies.Since the local estimates are proved by Littlewood–Paley decomposition, withα+β>2\alpha+\beta>2entering as a positive summability margin in the dyadic sums, we track the weighted shell energiesEq​(t)=λq2​s​(‖Λ​Δq​a‖L22+‖Δq​b‖L22),λq=2q,E_{q}(t)=\lambda_{q}^{2s}\big(\left\|\Lambda\Delta_{q}a\right\|_{L^{2}}^{2}+\left\|\Delta_{q}b\right\|_{L^{2}}^{2}\big),\qquad\lambda_{q}=2^{q},(5.2)

where the sharp annular projections2q≤|k|<2q+12^{q}\leq|k|<2^{q+1}stand in for smooth Littlewood–Paley blocks. The profile ofEqE_{q}acrossqqmonitors the dyadic summability underlying theHs+1×HsH^{s+1}\times H^{s}estimates.
- 7.

Cancellation defect.With the weights(1+|k|2)(1+|k|^{2})onaaand11onbb, the two nonlinear inputs cancel exactly,𝒩a+𝒩b=0\mathcal{N}_{a}+\mathcal{N}_{b}=0ats=0s=0: this combines the magnetic-energy cancellation of Section2with incompressibility of the drift. We monitor the relative defectr0​(t)=|𝒩a+𝒩b|/(|𝒩a|+|𝒩b|)r_{0}(t)=|\mathcal{N}_{a}+\mathcal{N}_{b}|/(|\mathcal{N}_{a}|+|\mathcal{N}_{b}|)of this identity along the discrete flow. We emphasize that this tests the nonlinear magnetic-energy cancellation at the base energy level, not the full higher-order cancellation of low–high interactions in the Littlewood–Paley proof. It is a structural check that the discretization preserves the base-level cancellation on which the local theory is built, and it doubles as a resolution indicator: the defect sits at round-off while the solution is spectrally resolved and departs from it only when the truncation shell becomes populated.

## 5.2Resolution-control protocol

The diagnostics of Section5.1can each be mimicked by under-resolution: spectral energy piling up at the grid scale can produce spurious current growth and an apparent collapse of the analyticity strip, both artifacts of truncation rather than features of the continuous dynamics. The purpose of this subsection is to make the distinction operational, by fixing in advance the conditions that a reported onset must meet. A current-sheet onset is reported only if it survives the following controls.
- •

Resolution gate.The solution is trusted only while the analyticity strip remains resolved,δ​(t)≳C​Δ​x\delta(t)\gtrsim C\,\Delta x(several grid points per strip width), equivalently while the spectrum has decayed to round-off beforekmaxk_{\max}. Any extrapolated singular timet∗t^{*}is inferred from theresolvedwindow, never by integrating into the under-resolved regime.
- •

Resolution ladder.Representative runs are repeated at increasing resolutions withΔ​t\Delta treduced accordingly; the trusted-window diagnostics must converge under refinement, and the peak intensity must not decrease withNN. Only the resolved interval is reported.
- •

Aliasing insensitivity.Results hold under both the2/32/3rule and a high-order exponential filter.
- •

Cross-diagnostic consistency.The signalsδ​(t)→0\delta(t)\to 0,‖𝑱‖L∞→∞\left\|\bm{J}\right\|_{L^{\infty}}\to\infty, andEs​(t)→∞E_{s}(t)\to\inftyare required to indicate thesamet∗t^{*}, with exponents consistent with the scaling relations of Section3.

## 5.3Dynamic rescaling

To characterize the self-similar structure of a candidate collapse one may use the McLaughlin–Papanicolaou–Sulem–Sulem dynamic-rescaling strategy[23], normalizing by the current. We outline it here, as it motivates the static exponent estimates of Section6. Introducing a renormalized timeτ\tauthroughd​τ=L​(τ)−q​d​td\tau=L(\tau)^{-q}\,dtand rescaled fields adapted to (3.2), withL​(τ)L(\tau)pinned by the condition‖𝑱‖L∞≡1\left\|\bm{J}\right\|_{L^{\infty}}\equiv 1in rescaled variables, the exponentq=q​(τ)q=q(\tau)is determined adaptively and would converge to a valueq∗q^{*}if a self-similar profile exists; a finite-time singularity then corresponds tot∗=∫0∞L​(τ)q​𝑑τ<∞t^{*}=\int_{0}^{\infty}L(\tau)^{q}\,d\tau<\infty. The reduced equations in rescaled variables are recorded in AppendixA.

## 6Numerical results

We now report the numerical experiments. All runs follow the protocol of Section5, and all quantitative claims refer to the trusted window defined there.

## 6.1Validation and numerical setup

The solver passes all tests of Section4.3(Table4.1, Figure4.1).

For reproducibility we record the precise setup used in the remainder of this section. The initial data are the smooth, band-limited shear-type fieldsa0​(x,y)\displaystyle a_{0}(x,y)=cos⁡x+12​cos⁡2​y+310​sin⁡(x+y),\displaystyle=\cos x+\tfrac{1}{2}\cos 2y+\tfrac{3}{10}\sin(x+y),(6.1)b0​(x,y)\displaystyle b_{0}(x,y)=sin⁡y+12​sin⁡2​x+310​cos⁡(x−y),\displaystyle=\sin y+\tfrac{1}{2}\sin 2x+\tfrac{3}{10}\cos(x-y),

on𝕋2=[0,2​π)2\mathbb{T}^{2}=[0,2\pi)^{2}. Each field is made mean-free and then rescaled by a common factor, so thatmax⁡(‖a0‖∞,‖b0‖∞)=ϵ\max(\|a_{0}\|_{\infty},\|b_{0}\|_{\infty})=\epsilon. The amplitudeϵ\epsilonand the pair(α,β)(\alpha,\beta)are the only quantities varied, leaving the dissipation as the sole control parameter. Aliasing is removed by the2/32/3rule (with the smooth exponential-filter variant used as a cross-check in the most marginal runs). The time step is fixed per run at the dispersive-CFL value of Section4,Δ​t=cCFLkmax2​max⁡(ϵ,1),kmax=N/3,cCFL=0.18.\Delta t=\frac{c_{\rm CFL}}{k_{\max}^{2}\,\max(\epsilon,1)},\qquad k_{\max}=N/3,\quad c_{\rm CFL}=0.18.(6.2)

Because the whistler frequency involves the solution amplitude, which is not constant along a run, we verified the adequacy of this fixed step directly: halvingΔ​t\Delta tin the singular reference run changes the reported diagnostics by less than0.2%0.2\%over the trusted window. Diagnostics are sampled every2020steps; a run is integrated until the resolution gate trips, i.e. until the analyticity strip falls to the grid scale,δ​(t)<Δ​x\delta(t)<\Delta x, after which the solution is no longer trusted.

A run is classifiedsingularwhen the current grows by more than a factor1.61.6while the strip collapses below2​Δ​x2\,\Delta x,regularwhen the current never grows by more than a factor1.251.25, andmarginalotherwise. Current growth is the primary classifier; the strip condition reinforces the singular label rather than defining the regular one, because for weakly dissipated runs the saturated strip can settle below2​Δ​x2\,\Delta xwithout collapsing further, while the current shows no growth at all. In our data the two criteria never conflict: every run with growth above1.61.6also shows strip collapse toward the gate. The thresholds are deliberately conservative; the singular and regular populations are well separated from them (e.g.the regular cases of the phase diagram show essentially no current growth, withmaxt⁡‖𝑱‖L∞\max_{t}\left\|\bm{J}\right\|_{L^{\infty}}exceeding‖𝑱‖L∞​(0)\left\|\bm{J}\right\|_{L^{\infty}}(0)by at most a few percent and typically not at all), so the classification is insensitive to the precise cut-offs.

## 6.2The(α,β)(\alpha,\beta)phase diagram: an asymmetric,α\alpha-controlled boundary

Fixing the initial data and sweeping(α,β)(\alpha,\beta), we classify each run assingular(the out-of-plane current grows and the analyticity strip collapses to the grid scale),regular(the current decays and the strip saturates), ormarginal, using the resolution-controlled diagnostics of Section5. Figure6.1(a) shows the outcome at a representative amplitude. The singular region occupies smallα\alphaand the regular region largeα\alpha, separated by a near-vertical onset band; the symmetric lineα+β=2\alpha+\beta=2cutsacrossthe boundary rather than tracing it.

The asymmetry is sharpest along our sampled points on the lineα+β=2\alpha+\beta=2(Table6.1): holding the sum fixed and increasingα\alpha, the outcome runs from singular through marginal to regular. Two runs with identical sum,(α,β)=(0.4,1.6)(\alpha,\beta)=(0.4,1.6)and(1.6,0.4)(1.6,0.4), fall on opposite sides of the onset band. To localize the transition we sampled four additional points on the line; alongα+β=2\alpha+\beta=2the transition occurs within the sampled interval0.85≤α≤1.150.85\leq\alpha\leq 1.15, centered on the marginal pointα=1\alpha=1. The sum does not appear to determine the onset; the dissipationα\alphaon the magnetic potential does. The growth itself is monotone along the line, decreasing from3.03.0atα=0.4\alpha=0.4to no growth at all forα≥1.3\alpha\geq 1.3(Table6.1). This matches the third reading of Section3: because the concentration occurs in the out-of-plane currentΔ​a\Delta a, which onlyΛα\Lambda^{\alpha}regularizes,α\alphais the candidate binding parameter.

Theα\alpha-controlled asymmetry is not tied to the shear-type family (6.1). As a robustness check along the lineα+β=2\alpha+\beta=2(not a recomputation of the full phase diagram), we repeated the five original line points with band-limited random-phase initial data (independent Gaussian modes with1≤|k|≤31\leq|k|\leq 3, mean-free, rescaled to the same amplitudeϵ=3\epsilon=3); this reproduces the same sequence along the line: singular atα=0.4\alpha=0.4and0.70.7(growth2.42.4and1.91.9), marginal atα=1\alpha=1(growth1.41.4), and no growth atα=1.3\alpha=1.3and1.61.6.Table 6.1:Classification and current growth across our sampled points on the lineα+β=2\alpha+\beta=2at fixed data (N=96N=96,ϵ=3\epsilon=3). The same sum yields opposite outcomes, and the transition occurs within the sampled interval0.85≤α≤1.150.85\leq\alpha\leq 1.15, indicating that the observed onset boundary isα\alpha-controlled rather than symmetric.α\alpha0.40.40.550.550.70.70.850.851.01.01.151.151.31.31.451.451.61.6β\beta1.61.61.451.451.31.31.151.151.01.00.850.850.70.70.550.550.40.4outcomesing.sing.sing.sing.marg.reg.reg.reg.reg.maxt⁡‖𝑱‖L∞/‖𝑱‖L∞​(0)\max_{t}\left\|\bm{J}\right\|_{L^{\infty}}/\left\|\bm{J}\right\|_{L^{\infty}}(0)3.03.02.62.62.22.21.91.91.51.51.11.11.01.01.01.01.01.0Figure 6.1:(a) Phase diagram in the(α,β)(\alpha,\beta)plane at fixed initial data. Singular points (crosses) occupy smallα\alpha, regular points (circles) largeα\alpha, with a near-vertical onset band; the lineα+β=2\alpha+\beta=2(dashed) does not separate them. (b) The onset is amplitude dependent: current growth versus data amplitudeϵ\epsilonfor two families of equal split. A case regular at small amplitude becomes singular as the data grows.

The onset boundary is amplitude dependent (Figure6.1(b)): a case that is regular at small amplitude becomes singular at larger amplitude, and the boundary advances toward larger exponents as the data grows. This is the expected behavior of a fixed-data onset boundary lying below an all-data threshold. The amplitude-dependent growth is not in conflict with the local well-posedness result forα+β>2\alpha+\beta>2, which does not assert global regularity or uniform suppression of small-scale amplification; how close to the analytical threshold the boundary ultimately advances is left open.

## 6.3The singular mechanism and a resolution ladder

Figure6.2contrasts a sub-threshold run (α=β=0.8\alpha=\beta=0.8,α+β=1.6\alpha+\beta=1.6) with a super-threshold run (α=β=1.3\alpha=\beta=1.3,α+β=2.6\alpha+\beta=2.6) at the same data, the fields (6.1) at amplitudeϵ=3\epsilon=3; the same pair of runs is used throughout this subsection and the next two. In the singular case the analyticity strip collapses from𝒪​(1)\mathcal{O}(1)to the grid scale (panel a) while the current maximum grows (panel b); in the regular case the strip saturates well above the grid scale and the current decays monotonically. Panel (c) identifies the mechanism: the out-of-plane current‖Δ​a‖L∞\left\|\Delta a\right\|_{L^{\infty}}dominates the in-plane current‖∇b‖L∞\left\|\nabla b\right\|_{L^{\infty}}throughout, so the incipient singularity is a sheet inΔ​a\Delta a.

Refining the grid sharpens rather than softens the concentration: the peak current rises from12.512.5atN=96N=96to15.415.4atN=128N=128, and the strip reaches the same fraction (≈1.1\approx\!1.1grid cells) of the smaller mesh at the higher resolution. While under-resolution can in principle generate spurious oscillations, the increase of the peak current under refinement, taken together with the consistent analyticity-strip collapse and the spectral broadening of Figure6.6(c), is consistent with a resolved concentration mechanism rather than a discretization artifact. Beyond the point at which the strip reaches the grid scale the run is no longer trusted; the apparent turnover of the current in Figure6.2(b) marks this resolution limit, not the dynamics. Figure6.3shows the characteristic sheet structure of−Δ​a-\Delta anear the end of the trusted window.Figure 6.2:Singular versus regular dynamics. (a) Analyticity-strip widthδ​(t)/Δ​x\delta(t)/\Delta x: collapse to the grid scale (singular, two resolutions) versus saturation (regular). (b) Current maximum, normalized: growth that increases with resolution (singular) versus monotone decay (regular); the turnover of the singular curves marks the resolution limit. (c) In the singular run the out-of-plane currentΔ​a\Delta aleads the in-plane current∇b\nabla b, identifying a current-sheet collapse.Figure 6.3:Out-of-plane current−Δ​a-\Delta anear the end of the trusted window of the singular run, showing concentration into a sheet.

## 6.4Energy-budget and dyadic-shell diagnostics

The remaining diagnostics of Section5.1confirm the picture and tie it to the energy mechanism of the local theory (Figures6.4and6.5); the same quantities admit a direct physical reading as the natural description of anisotropic small-scale energy transfer between the two magnetic components. The energyE2​(t)=‖a‖H32+‖b‖H22E_{2}(t)=\left\|a\right\|_{H^{3}}^{2}+\left\|b\right\|_{H^{2}}^{2}, the numerical analogue of the asymmetric energy in which the local theory of[25]closes, grows by a factor of about88atN=96N=96and about1414atN=128N=128over the trusted window of the singular run, with the growth accelerating as the strip approaches the grid scale andincreasingunder refinement; in the regular run it decays monotonically, by a factor of about77over the longer integration. The Beale–Kato–Majda integral∫0t‖𝑱‖L∞​𝑑τ\int_{0}^{t}\left\|\bm{J}\right\|_{L^{\infty}}\,d\tauis convex in the singular run and concave in the regular one, consistent with accelerating current growth in the former and relaxation in the latter. All signals of the protocol of Section5.2(strip collapse, current growth, Sobolev-energy growth, convexity of the BKM integral) thus turn on together over the same window of the singular run, and all of them relax in the regular run.Figure 6.4:Cross-diagnostic consistency for the runs of Figure6.2. (a) The well-posedness Sobolev energyE2​(t)E_{2}(t)grows in the singular run, faster at higher resolution, and decays monotonically in the regular run. (b) The BKM integral∫0t‖𝑱‖L∞​𝑑τ\int_{0}^{t}\left\|\bm{J}\right\|_{L^{\infty}}\,d\tauis convex (singular) versus concave (regular).

Figure6.5resolves this energy balance into the ingredients of the local estimates. Panel (a) shows the two dissipation channels (5.1). In the regular run both channels decay after an initial transient, and theH2H^{2}budget ratio of panel (c) stays below one throughout (maximum0.880.88): the dissipation absorbs the nonlinear input, as the local estimates require. In the singular run the budget crosses one att≈0.09t\approx 0.09, before the current growth onset att≈0.14t\approx 0.14, and reaches2.252.25: from that point the nonlinearity outruns the combined dissipative capacity in the energy class, andE2E_{2}grows accordingly. Theaa-channel carries the larger dissipative load initially (Da/Db≈3D_{a}/D_{b}\approx 3); as the sheet forms, the two channels become comparable, so once the concentration is underway neither channel alone suffices. This does not contradict theα\alpha-controlled onset: the concentration is initiated in theΔ​a\Delta acurrent channel, which onlyΛα\Lambda^{\alpha}regularizes, while the subsequent proof-level energy balance involves both dissipative channels.

Panel (b) shows the dyadic shell energies (5.2) of the singular run. The weighted profile inverts: by the end of the trusted windowEqE_{q}increaseswithqq, withE5/E1E_{5}/E_{1}rising from2×10−32\times 10^{-3}att=0.1t=0.1to about5050, so the dyadic sums behind theHs+1×HsH^{s+1}\times H^{s}estimates lose summability from the top shells. This is consistent with the dyadic high-frequency failure mode against which the conditionα+β>2\alpha+\beta>2supplies the summability margin in the local theory. In the regular run (not shown) the weighted profile remains steeply decreasing,E5/E1≤2×10−2E_{5}/E_{1}\leq 2\times 10^{-2}throughout, and the top shells peak neart≈0.26t\approx 0.26before decaying by one to two orders of magnitude.

Finally, the cancellation defectr0​(t)r_{0}(t)confirms that the discretization preserves the inter-equation structure: in theN=128N=128singular run it stays below10−1510^{-15}while the strip exceeds2​Δ​x2\,\Delta xand rises only to about10−1210^{-12}at the resolution gate. The defect departs from round-off precisely when the truncation shell becomes populated, so it independently supports the trusted window.Figure 6.5:Proof-level energetics (s=2s=2) for the runs of Figure6.2: singular runα=β=0.8\alpha=\beta=0.8atN=128N=128(solid), regular runα=β=1.3\alpha=\beta=1.3atN=96N=96(dashed), both atϵ=3\epsilon=3. (a) Dissipation channelsDaD_{a},DbD_{b}of the local theory: both decay in the regular run and grow in the singular run. (b) Dyadic shell energiesEqE_{q}of the singular run: the weighted profile inverts, with the highest shells dominant by the end of the trusted window. (c) Signed ratio of nonlinear input to dissipation in theH2H^{2}energy balance; values above one mean the nonlinearity outruns the combined dissipation. The ratio stays below one in the regular run and crosses one att≈0.09t\approx 0.09in the singular run, before the onset of current growth att≈0.14t\approx 0.14.

## 6.5Self-similar concentration and the exponentq∗≈3q^{*}\approx 3

On the resolved growth window of the singular run the current and the strip follow power laws int∗−tt^{*}-t(Figure6.6a,b), wheret∗t^{*}is an extrapolated putative singular time. The fit window is necessarily narrow: it is bounded below by the resolution gate (its lower end abuts strip widths of one to two grid cells) and above by the onset of growth, sot∗−tt^{*}-tspans only a factor of about1.51.5. Within it, the individual exponentsγJ\gamma_{J}(current) andν\nu(strip) are only loosely determined and trade off againstt∗t^{*}: the measured valuesγJ=2.39\gamma_{J}=2.39andν=1.16\nu=1.16atN=128N=128exceed the self-similar predictionsγJ=(q∗−1)/q∗≈0.67\gamma_{J}=(q^{*}-1)/q^{*}\approx 0.67andν=1/q∗≈0.33\nu=1/q^{*}\approx 0.33of (3.4) by a common factor of about3.53.5. This discrepancy is consistent with sensitivity to the extrapolated value oft∗t^{*}over a narrow fitting window (see the discussion after (3.4)), rather than necessarily indicating a failure of the self-similar scaling. Their ratio, throughq∗=1+γJ/ν,q^{*}=1+\gamma_{J}/\nu,(6.3)

is by the same token robust, givingq∗=3.03q^{*}=3.03atN=96N=96andq∗=3.06q^{*}=3.06atN=128N=128. The valueq∗≈3q^{*}\approx 3is distinguished: it is the energy-critical scaling at which the conserved magnetic energy is invariant,M∼λ6−2​q=λ0M\sim\lambda^{6-2q}=\lambda^{0}(Proposition3.1and (3.3)). The observed concentration thus proceeds, to within the fit, at the energy-preserving self-similar rate: the magnetic energy neither concentrates nor disperses under the rescaling, while the current‖𝑱‖L∞∼λ1−q∗∼λ−2\left\|\bm{J}\right\|_{L^{\infty}}\sim\lambda^{1-q^{*}}\sim\lambda^{-2}grows. The spectra of Figure6.6(c) are consistent with the picture: as time advances the exponential tail extends and shallows,i.e.the analyticity strip closes.Figure 6.6:Self-similar structure of the singular run (α=β=0.8\alpha=\beta=0.8,ϵ=3\epsilon=3,N=128N=128). (a) Current maximum and (b) analyticity-strip width versust∗−tt^{*}-t, with fitted power laws; the ratio yields a resolution-robustq∗≈3q^{*}\approx 3. (c) Energy spectra at successive times: the exponential tail extends and shallows as the analyticity strip closes.

A full determination ofq∗q^{*}through dynamic rescaling, and a tight separation ofγJ\gamma_{J}andν\nu, would require following the collapse substantially closer tot∗t^{*}at much higher resolution; we regard the resolution-robust estimateq∗≈3q^{*}\approx 3and its energy-scaling interpretation as the most reliable conclusions from these fits.

## 7Conclusion

In this paper, we have studied the role of split fractional dissipation in the2.52.5D EMHD system by combining scaling analysis with numerical experiments under controlled grid refinement. Taking the local well-posedness conditionα+β>2\alpha+\beta>2as a reference balance, we compared three candidate pictures: a split-dependent corner, the symmetric lineα+β=2\alpha+\beta=2, and anα\alpha-controlled boundary tied to the out-of-plane current. The computations favor the third picture: across sampled points on the lineα+β=2\alpha+\beta=2, the behavior changes from concentration at smallα\alphato decay at largeα\alpha. Since the sumα+β\alpha+\betais fixed along this line, this transition cannot be attributed to the combined dissipation alone; it indicates instead that the dissipation on the magnetic potential is the controlling parameter. The concentrating runs form an out-of-plane current sheet inΔ​a\Delta a, sharpen under grid refinement, and show consistent collapse of the analyticity strip, growth of the asymmetric Sobolev energy, inversion of weighted dyadic shell energies, and nonlinear transfer exceeding the combined dissipative budget. On the resolved window, the growth is consistent with an energy-critical self-similar rateq∗≈3q^{*}\approx 3. These findings provide resolution-controlled numerical evidence for a concentration mechanism, but not a proof of finite-time singularity.

The observed asymmetry also suggests a practical implication for EMHD and Hall–MHD computation. Within this reduced split-dissipation model, distributing the same nominal damping budget differently between the two magnetic components can lead to qualitatively different small-scale behavior, with damping of the magnetic potential playing the decisive role in gating current-sheet formation.

## Acknowledgements

This work was partially supported by the ONR grant #N00014-24-1-2432, the Simons Foundation (MP-TSM-00002783), and the NSF grant DMS-2420988.

## References
- [1]M. Acheritogaray, P. Degond, A. Frouvelle, and J. Liu(2011)Kinetic formulation and global existence for the Hall-magneto-hydrodynamics system.Kinetic and Related Models4(4),pp. 901–918.Cited by:§1.
- [2]J. T. Beale, T. Kato, and A. Majda(1984)Remarks on the breakdown of smooth solutions for the 3-D Euler equations.Communications in Mathematical Physics94(1),pp. 61–66.Cited by:§1,item 4.
- [3]D. Biskamp, E. Schwarz, and J. F. Drake(1996)Two-dimensional electron magnetohydrodynamic turbulence.Physical Review Letters76(8),pp. 1264.Cited by:§1,§1.
- [4]D. Biskamp, E. Schwarz, A. Zeiler, and J. F. Drake(1999)Electron magnetohydrodynamic turbulence.Physics of Plasmas6(3),pp. 751–758.Cited by:§1,§1.
- [5]D. Chae, P. Degond, and J. Liu(2014)Well-posedness for Hall-magnetohydrodynamics.Annales de l’IHP Analyse non linéaire31,pp. 555–565.Cited by:§1,§1.
- [6]D. Chae and J. Lee(2014)On the blow-up criterion and small data global existence for the Hall-magnetohydrodynamics.Journal of Differential Equations256(11),pp. 3835–3858.Cited by:§1.
- [7]D. Chae, R. Wan, and J. Wu(2015)Local well-posedness for the Hall-MHD equations with fractional magnetic diffusion.Journal of Mathematical Fluid Mechanics17(4),pp. 627–638.Cited by:§1.
- [8]S. M. Cox and P. C. Matthews(2002)Exponential time differencing for stiff systems.Journal of Computational Physics176(2),pp. 430–455.Cited by:§4.2.
- [9]M. Dai and H. Babaei(2025)Well-posedness of the electron MHD with partial resistivity.arXiv preprint arXiv:2503.18149.Cited by:§1.
- [10]M. Dai(2021)Local well-posedness for the Hall-MHD system in optimal Sobolev spaces.Journal of Differential Equations289,pp. 159–181.Cited by:§1.
- [11]M. Dai(2023)Global existence of 2D electron MHD near a steady state.arXiv preprint arXiv:2306.13036.Cited by:§1.
- [12]R. Danchin and J. Tan(2021)On the well-posedness of the Hall-magnetohydrodynamics system in critical spaces.Communications in Partial Differential Equations46(1),pp. 31–65.Cited by:§1.
- [13]R. Danchin and J. Tan(2022)The global solvability of the Hall-magnetohydrodynamics system in critical Sobolev spaces.Communications in Contemporary Mathematics24(10),pp. 2150099.Cited by:§1.
- [14]A. V. Gordeev, A. S. Kingsep, and L. I. Rudakov(1994)Electron magnetohydrodynamics.Physics Reports243(5),pp. 215–315.Cited by:§1.
- [15]H. Guo, R. Hu, Q. Peng, and X. Yang(2026)A gradient recovery method for electron magnetohydrodynamics with fractional dissipation.arXiv:2606.19716.Cited by:§1.
- [16]R. Hu, Q. Peng, and X. Yang(2025)Well-posedness of the relaxed electron MHD equations with random diffusion.arXiv:2509.18640.Cited by:§1.
- [17]R. Hu, Q. Peng, and X. Yang(2026)The three-dimensional stochastic EMHD system: Local well-posedness and maximal pathwise solutions.arXiv:2604.07497.Cited by:§1.
- [18]I. Jeong and S. Oh(2022)On the Cauchy problem for the Hall and electron magnetohydrodynamic equations without resistivity I: illposedness near degenerate stationary solutions.Annals of PDE8,pp. 15.Cited by:§1.
- [19]I. Jeong and S. Oh(2025)Wellposedness of the electron MHD without resistivity for large perturbations of the uniform magnetic field.Annals of PDE11,pp. 14.Cited by:§1.
- [20]A. Kassam and L. N. Trefethen(2005)Fourth-order time-stepping for stiff PDEs.SIAM Journal on Scientific Computing26(4),pp. 1214–1233.Cited by:§4.2.
- [21]L. Liu and J. Tan(2021)Global well-posedness for the Hall-magnetohydrodynamics system in larger critical Besov spaces.Journal of Differential Equations274,pp. 382–413.Cited by:§1.
- [22]G. Luo and T. Y. Hou(2014)Toward the finite-time blowup of the 3D axisymmetric Euler equations: a numerical investigation.Multiscale Modeling & Simulation12(4),pp. 1722–1776.Cited by:§1.
- [23]D. W. McLaughlin, G. C. Papanicolaou, C. Sulem, and P.-L. Sulem(1986)Focusing singularity of the cubic Schrödinger equation.Physical Review A34(2),pp. 1200–1210.Cited by:Appendix A,§5.3.
- [24]S. A. Orszag(1971)On the elimination of aliasing in finite-difference schemes by filtering high-wavenumber components.Journal of the Atmospheric Sciences28(6),pp. 1074.Cited by:§4.1.
- [25]Q. Peng(2026)Local well-posedness for the two-and-a-half-dimensional EMHD system with split fractional dissipation.arXiv:2605.20845.Cited by:§1,§1,§2.3,§3.3,§3.3,item 3,§6.4.
- [26]C. Sulem, P.-L. Sulem, and H. Frisch(1983)Tracing complex singularities with spectral methods.Journal of Computational Physics50(1),pp. 138–161.Cited by:§1,item 1.

## Appendix ARescaled equations

Following Section5.3, introduce the rescaled space and time variablesξ=(x−x∗)/L​(τ)\xi=(x-x^{*})/L(\tau)andd​τ=L​(τ)−q​d​td\tau=L(\tau)^{-q}\,dt, and the rescaled fields consistent with the scaling (3.2),a​(x,t)=L3−q​A​(ξ,τ),b​(x,t)=L2−q​B​(ξ,τ).a(x,t)=L^{\,3-q}\,A(\xi,\tau),\qquad b(x,t)=L^{\,2-q}\,B(\xi,\tau).(A.1)

Writingκ:=(ln⁡L)τ\kappa:=(\ln L)_{\tau}for the renormalized growth rate, a direct computation transforms the dissipationless system (3.1) into the autonomous form∂τA+∇⟂B⋅∇A\displaystyle\partial_{\tau}A+\nabla^{\perp}B\cdot\nabla A=κ​[ξ⋅∇A−(3−q)​A],\displaystyle=\kappa\big[\,\xi\cdot\nabla A-(3-q)A\,\big],(A.2a)∂τB+∇⟂A⋅∇(Δ​A)\displaystyle\partial_{\tau}B+\nabla^{\perp}A\cdot\nabla(\Delta A)=κ​[ξ⋅∇B−(2−q)​B],\displaystyle=\kappa\big[\,\xi\cdot\nabla B-(2-q)B\,\big],(A.2b)

where all spatial operators are now inξ\xi. The scaleL​(τ)L(\tau)is fixed by the normalization that the rescaled current have unit amplitude,‖𝑱ξ‖L∞≡1\left\|\bm{J}_{\xi}\right\|_{L^{\infty}}\equiv 1, which by (3.3), where𝑱phys∼L1−q​𝑱ξ\bm{J}_{\rm phys}\sim L^{1-q}\bm{J}_{\xi}, amounts toL=‖𝑱‖L∞1/(1−q)=‖𝑱‖L∞−1/(q−1)L=\left\|\bm{J}\right\|_{L^{\infty}}^{1/(1-q)}=\left\|\bm{J}\right\|_{L^{\infty}}^{-1/(q-1)}(so that, sinceq>1q>1, the scaleL→0L\to 0as the current intensifies); the exponentq=q​(τ)q=q(\tau)is determined adaptively by requiring the rescaled fields to remain stationary in a chosen norm, in the manner of[23]. A self-similar collapse corresponds to aτ\tau-independent profile(A,B)(A,B)withq​(τ)→q∗q(\tau)\to q^{*}and constantκ\kappa; the finite singular time ist∗=∫0∞L​(τ)q​𝑑τ<∞t^{*}=\int_{0}^{\infty}L(\tau)^{q}\,d\tau<\infty.

## 


- 


Major funding support from
