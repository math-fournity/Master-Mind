# An explicit, energy-conserving particle-in-cell scheme for relativistic plasmas

**arXiv ID**: 2605.18542v1
**Authors**: Lee Ricketson, Jingwei Hu
**Published**: 2026-05-18
**Categories**: physics.plasm-ph, math-ph, math.NA
**HTML URL**: https://arxiv.org/html/2605.18542v1

## Abstract

We extend the recently-developed explicit, energy-conserving particle-in-cell (PIC) scheme of [1] to the relativistic Vlasov-Maxwell system. As in the non-relativistic case, the method is built on an optimization problem that is analytically solvable, local to each particle, and designed to enforce exact energy conservation. Although the solution to this optimization problem is not guaranteed to be real, we show that such instances are rare enough for practical simulation parameters to permit dramatic improvements in energy conservation over traditional explicit PIC schemes. We show that, as in the non-relativistic case, the scheme is compatible with popular field-solvers for electromagnetic PIC schemes, including the Yee/FDTD and pseudo-spectral analytic time-domain (PSATD) methods. The scheme is verified on standard relativistic test problems, where its conservation properties are confirmed.

## Full Text

An explicit, energy-conserving particle-in-cell scheme for relativistic plasmas

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
- License: CC BY 4.0arXiv:2605.18542v1 [physics.plasm-ph] 18 May 2026

## An explicit, energy-conserving particle-in-cell scheme for relativistic plasmasLee F. RicketsonJingwei Hu

## Abstract

We extend the recently-developed explicit, energy-conserving particle-in-cell (PIC) scheme of[28]to the relativistic Vlasov-Maxwell system. As in the non-relativistic case, the method is built on an optimization problem that is analytically solvable, local to each particle, and designed to enforce exact energy conservation. Although the solution to this optimization problem is not guaranteed to be real, we show that such instances are rare enough for practical simulation parameters to permit dramatic improvements in energy conservation over traditional explicit PIC schemes. We show that, as in the non-relativistic case, the scheme is compatible with popular field-solvers for electromagnetic PIC schemes, including the Yee/FDTD and pseudo-spectral analytic time-domain (PSATD) methods. The scheme is verified on standard relativistic test problems, where its conservation properties are confirmed.

## keywords:particle-in-cell , relativistic , energy conservation , plasma , Vlasov††journal:Journal of Computational Physics\affiliation

[LLNL]organization=Lawrence Livermore National Laboratory, Center for Applied Scientific Computing,addressline=7000 East Avenue,
city=Livermore,
postcode=94550,
state=CA,
country=USA\affiliation

[UW]organization=Department of Applied Mathematics, University of Washington,addressline=Box 353925,
city=Seattle,
postcode=98195,
state=WA,
country=USA

## 1Introduction

Particle-in-cell (PIC) schemes are widely used to simulate kinetic plasma phenomena in a variety of scenarios. Such schemes are simple, scalable, and relatively robust. However, their speed and accuracy have historically been denigrated by a lack of discrete conservation properties, most famously leading to so-called “grid heating” arising from the finite grid instability[4,5].

There has been considerable recent work on PIC schemes that conserve total energy exactly, thereby eliminating grid heating (and effectively mitigating the finite grid instability itself in many practical contexts[4]). These schemes have largely been fully implicit[11,10,13]or semi-implicit[12,21,23,3]. More recently, a few efforts have captured exact energy conservation in fully explicit schemes[17,20], including in the authors’ precursor to this work[28].

Much of this development has naturally begun in the non-relativistic limit, where the governing PDEs and resulting dynamics are somewhat simplified. However, relativistic effects play an important role in several applications of physical interest, including runaway electrons in tokamaks[8], inertial confinement fusion[2], and astrophysical plasmas[24]. This has motivated development of semi-implicit[12]and explicit[17]energy-conserving PIC schemes for the relativistic Vlasov-Maxwell system.

Here, we extend the scheme of[28]to the relativistic case. Compared to the semi-implicit scheme of[12], a reduced cost per time-step is expected at the expense of the ability to step over stiff time-scales in the particle advance. Although both[17]and the present scheme are fully explicit,[17]relies on a splitting scheme that requires that particles within an individual cell be advanced in serial. The present scheme has no such requirement, and thus improved parallel scalability of the present scheme is expected in some contexts.

As in[28], the scheme is built on a standard time integration scheme with an additional correction at the end of each time-step that enforces energy conservation. The correction is defined as the solution to a constrained optimization problem, with the objective function preserving accuracy by minimizing distance to a velocity with known accuracy, and the constraint enforcing exact conservation. Importantly, this optimization problem is analytically solvable, thus preserving the explicit nature of the scheme, and local to each particle, thus preserving parallel scalability.

As in the non-relativistic case, we show that the new time-integration scheme is compatible with popular Maxwell solvers from the relativistic PIC literature. In particular, energy conservation can be achieved with both the Yee grid/finite difference time domain (FDTD) scheme[34]and the pseudospectral analytic time domain (PSATD) scheme[5,22,33]. Each scheme is desirable for its accurate (and in the case of PSATD, exact) capturing of the light-wave dispersion relation, which is of particular importance in relativistic applications.

The scheme is verified on four test problems that feature relativistic effects: the relativistic two-stream instability, relativistic Landau damping, the filamentation instability, and the relativistic Weibel instability. In each case, agreement with standard PIC schemes and/or linear theory is observed, along with dramatically improved energy conservation.

The remainder of the article is structured as follows. In Section2, we review relevant background material, including the relativistic Vlasov-Maxwell system, its standard PIC discretizations, and the previous energy-conserving scheme in the non-relativistic case. In Section3, we derive the scheme, showing both that it retains second-order accuracy and reduces to the previous scheme in the non-relativistic limit. Numerical results confirming the theoretical predictions are shown in Section4, and we conclude in Section5.

## 2Background

## 2.1Relativistic Vlasov-Maxwell system

This work concerns numerical solution of the relativistic Vlasov-Maxwell system. The relativistic Vlasov equation is given by∂tf+𝐯⋅∇𝐱f+(𝐄+𝐯×𝐁)⋅∇𝐮f=0.\partial_{t}f+\mathbf{v}\cdot\nabla_{\mathbf{x}}f+\left(\mathbf{E}+\mathbf{v}\times\mathbf{B}\right)\cdot\nabla_{\mathbf{u}}f=0.(1)

Here,f​(𝐱,𝐮,t)f(\mathbf{x},\mathbf{u},t)is the phase space particle distribution function.𝐱\mathbf{x}denotes position in physical space,𝐯\mathbf{v}denotes particle velocity, and𝐮=𝐯​γ\mathbf{u}=\mathbf{v}\gammadenotes proper velocity, with the Lorentz factorγ=1+‖𝐮‖2/c2=11−‖𝐯‖2/c2.\gamma=\sqrt{1+\left\|\mathbf{u}\right\|^{2}/c^{2}}=\frac{1}{\sqrt{1-\left\|\mathbf{v}\right\|^{2}/c^{2}}}.(2)

We work here and in the remainder of the paper in a non-dimensional formulation in which time is scaled by the plasma frequencyωp=n0​e2/m​ϵ0\omega_{p}=\sqrt{n_{0}e^{2}/m\epsilon_{0}}, space by an arbitrary factorLL, and velocity byL​ωpL\omega_{p}. Here,n0n_{0}is a reference number density,mmthe particle mass,eethe fundamental unit charge, andϵ0\epsilon_{0}the permittivity of free space. Common choices forLLinclude the DeBye lengthλD\lambda_{D}and the distance traveled by light in a plasma periodc/ωpc/\omega_{p}, but we need not specify the choice here. The resulting normalization factors forff,𝐄\mathbf{E}, and𝐁\mathbf{B}are, respectively,n0/(ωp​L)3n_{0}/(\omega_{p}L)^{3},n0​L​e/ϵ0n_{0}Le/\epsilon_{0}andn0​e/ϵ0​ωpn_{0}e/\epsilon_{0}\omega_{p}.

𝐄\mathbf{E}and𝐁\mathbf{B}denote the electric and magnetic fields, which are specified by Maxwell’s equations:∇x⋅𝐄=ρ−1,∇x⋅𝐁=0,∇x×𝐄=−∂𝐁∂t,∇x×𝐁=1c2​(∂𝐄∂t+𝐣).\begin{split}\nabla_{x}\cdot\mathbf{E}&=\rho-1,\\
\nabla_{x}\cdot\mathbf{B}&=0,\\
\nabla_{x}\times\mathbf{E}&=-\frac{\partial\mathbf{B}}{\partial t},\\
\nabla_{x}\times\mathbf{B}&=\frac{1}{c^{2}}\left(\frac{\partial\mathbf{E}}{\partial t}+\mathbf{j}\right).\end{split}(3)

These equations couple back to Vlasov via the charge densityρ\rhoand current density𝐣\mathbf{j}, given byρ=∫f​𝑑𝐮,𝐣=∫𝐯​f​𝑑𝐮.\rho=\int f\,d\mathbf{u},\qquad\mathbf{j}=\int\mathbf{v}f\,d\mathbf{u}.(4)

The speed of lightcchere is understood to be written in our dimensionless variables – that is, the physical speed of light divided byL​ωpL\omega_{p}. Note also the inclusion of a neutralizing background in Gauss’ law, representing an ion density that is constant on time-scales of interest. All methods developed here can be trivially extended to the multi-species case.

This system features a conserved total energy. To see it, we first note that equation (1)
can be written in a conservative form:∂tf+∇𝐱⋅(𝐯​f)+∇𝐮⋅((𝐄+𝐯×𝐁)​f)=0.\partial_{t}f+\nabla_{\mathbf{x}}\cdot(\mathbf{v}f)+\nabla_{\mathbf{u}}\cdot\left((\mathbf{E}+\mathbf{v}\times\mathbf{B})f\right)=0.(5)

Taking the moments∫⋅(1,γ)T​d​𝐮\int\cdot\,(1,\gamma)^{T}\,d\mathbf{u}of the above equation and using integration by parts, one obtains the local conservation of charge and energy:∂tρ+∇𝐱⋅𝐣=0,\displaystyle\partial_{t}\rho+\nabla_{\mathbf{x}}\cdot\mathbf{j}=0,(6)∂t∫γ​f​𝑑𝐮+∇𝐱⋅∫𝐮​f​d𝐮=1c2​𝐄⋅𝐣.\displaystyle\partial_{t}\int\gamma f\,d{\mathbf{u}}+\nabla_{\mathbf{x}}\cdot\int\mathbf{u}f\,\,\mathrm{d}{\mathbf{u}}=\frac{1}{c^{2}}\mathbf{E}\cdot\mathbf{j}.(7)

Further integration of (7) in𝐱\mathbf{x}and assuming periodic or zero boundary condition gives∂t∬γ​f​𝑑𝐮​𝑑𝐱=∫1c2​𝐄⋅𝐣​𝑑𝐱,\partial_{t}\iint\gamma f\,d{\mathbf{u}}\,d{\mathbf{x}}=\int\frac{1}{c^{2}}\mathbf{E}\cdot\mathbf{j}\,d{\mathbf{x}},(8)

which, combined with the Maxwell’s equations, yields∂t(c2​∬γ​f​𝑑𝐮​𝑑𝐱+12​∫(‖𝐄‖2+c2​‖𝐁‖2)​𝑑𝐱)=0.\partial_{t}\left(c^{2}\iint\gamma f\,d{\mathbf{u}}\,d{\mathbf{x}}+\frac{1}{2}\int\left(\|\mathbf{E}\|^{2}+c^{2}\|\mathbf{B}\|^{2}\right)\,d\mathbf{x}\right)=0.(9)

Using thatc2​∬f​𝑑𝐮​𝑑𝐱c^{2}\iint f\,d\mathbf{u}d\mathbf{x}is conserved (from integration of (6) in𝐱\mathbf{x}), we can see that the total energy defined byℰ=c2​∫(γ−1)​f​𝑑𝐮​𝑑𝐱+12​∫(‖𝐄‖2+c2​‖𝐁‖2)​𝑑𝐱\mathcal{E}=c^{2}\int(\gamma-1)f\,d\mathbf{u}d\mathbf{x}+\frac{1}{2}\int\left(\left\|\mathbf{E}\right\|^{2}+c^{2}\left\|\mathbf{B}\right\|^{2}\right)\,d\mathbf{x}(10)

is conserved over time. In the non-relativistic limit,𝐮c→0\frac{\mathbf{u}}{c}\rightarrow 0(or𝐮c≪1\frac{\mathbf{u}}{c}\ll 1), thenγ→1\gamma\rightarrow 1, and𝐮→𝐯\mathbf{u}\rightarrow\mathbf{v}. Sincec2​(γ−1)=|𝐮|2γ+1c^{2}(\gamma-1)=\frac{|\mathbf{u}|^{2}}{\gamma+1}, thenc2​(γ−1)→|𝐯|22c^{2}(\gamma-1)\rightarrow\frac{|\mathbf{v}|^{2}}{2}and the above energy reduces to the classical non-relativistic energy. We seek a discretization that exactly preserves the conservation of (10).

## 2.2Particle-in-cell discretization

Motivated by the high-dimensionality of the Vlasov equation, particle-in-cell (PIC) schemes work from the ansatz thatffcan be approximated by a weighted sum of Dirac delta functions:f​(𝐱,𝐮,t)=∑p=1Npwp​δ​(𝐱−𝐱p​(t))​δ​(𝐮−𝐮p​(t)).f(\mathbf{x},\mathbf{u},t)=\sum_{p=1}^{N_{p}}w_{p}\delta\left(\mathbf{x}-\mathbf{x}_{p}(t)\right)\delta\left(\mathbf{u}-\mathbf{u}_{p}(t)\right).(11)

The evolution equations for the “particle” states(𝐱p,𝐯p,wp)(\mathbf{x}_{p},\mathbf{v}_{p},w_{p})are of course the characteristic equations for Vlasov:d​𝐱pd​t=𝐯p,d​𝐮pd​t=𝐄​(𝐱p,t)+𝐯p×𝐁​(𝐱p,t),d​wpd​t=0.\frac{d\mathbf{x}_{p}}{dt}=\mathbf{v}_{p},\qquad\frac{d\mathbf{u}_{p}}{dt}=\mathbf{E}(\mathbf{x}_{p},t)+\mathbf{v}_{p}\times\mathbf{B}(\mathbf{x}_{p},t),\qquad\frac{dw_{p}}{dt}=0.(12)

The electromagnetic fields are computed on a configuration-space mesh with grid-points denoted by𝐱h\mathbf{x}_{h}. Particle data is deposited on the mesh via so-called “shape functions”. In particular, charge and current densities at grid points are defined byρh​(t)=1|𝐡|​∑pwp​Sρh​(𝐱h−𝐱p​(t)),𝐣h​(t)=1|𝐡|​∑pwp​𝐯p​(t)​Sjh​(𝐱h−𝐱p​(t)).\rho_{h}(t)=\frac{1}{|\mathbf{h}|}\sum_{p}w_{p}S^{h}_{\rho}\left(\mathbf{x}_{h}-\mathbf{x}_{p}(t)\right),\qquad\mathbf{j}_{h}(t)=\frac{1}{|\mathbf{h}|}\sum_{p}w_{p}\mathbf{v}_{p}(t)S^{h}_{j}\left(\mathbf{x}_{h}-\mathbf{x}_{p}(t)\right).(13)

Here|𝐡||\mathbf{h}|denotes cell volume andShS^{h}is a shape function such thatSh/|𝐡|S^{h}/|\mathbf{h}|is a second-order approximation of the Dirac delta function. The most commonly used example is the “tent” function,Sh​(z)=max⁡{0,1−|z|/h}S^{h}(z)=\max\{0,1-|z|/h\}and its tensor products in higher dimensions. However, arbitrary-orderBB-splines may be used as well.

ρh​(t)\rho_{h}(t)and𝐣h​(t)\mathbf{j}_{h}(t)are used to compute𝐄h​(t)\mathbf{E}_{h}(t)and𝐁h​(t)\mathbf{B}_{h}(t)via some discretization of Maxwell’s equations. The electromagnetic fields are then interpolated to particle locations:𝐄​(𝐱p,t)=∑h𝐄h​(t)​SEh​(𝐱p−𝐱h),𝐁​(𝐱p,t)=∑h𝐁h​(t)​SBh​(𝐱p−𝐱h).\begin{split}\mathbf{E}(\mathbf{x}_{p},t)&=\sum_{h}\mathbf{E}_{h}(t)S^{h}_{E}\left(\mathbf{x}_{p}-\mathbf{x}_{h}\right),\\
\mathbf{B}(\mathbf{x}_{p},t)&=\sum_{h}\mathbf{B}_{h}(t)S^{h}_{B}\left(\mathbf{x}_{p}-\mathbf{x}_{h}\right).\end{split}(14)

Typically, some of the shape functionsSρhS^{h}_{\rho},SjhS^{h}_{j},SEhS^{h}_{E}, andSBhS^{h}_{B}are identical. Energy conservation proofs, in particular, usually requireSjh=SEhS^{h}_{j}=S^{h}_{E}. The scheme is finally completed by choosing a temporal discretization of the resulting system of ordinary differential equations.

It will be instructive to review some of the commonly used discretizations of the characteristic equation and of Maxwell’s equations. We do so in the next two subsections.

## 2.3Particle advance

In the non-relativistic limit, the Boris scheme[26,18]is thede factostandard for explicit discretization of the characteristic equation. In the relativistic case, the Lorentz factor introduces additional discretization choices that have resulted in several similar methods in common use. They can all be written in the form𝐱p∗=𝐱pn+Δ​t2​𝐯pn,𝐮pn+1=𝐮pn+Δ​t​(𝐄​(𝐱p∗,tn+1/2)+𝐯¯p×𝐁​(𝐱p∗,tn+1/2)),𝐱pn+1=𝐱p∗+Δ​t2​𝐯pn+1.\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\mathbf{v}_{p}^{n},\\
\mathbf{u}_{p}^{n+1}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}(\mathbf{x}_{p}^{*},t^{n+1/2})+\bar{\mathbf{v}}_{p}\times\mathbf{B}(\mathbf{x}_{p}^{*},t^{n+1/2})\right),\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{*}+\frac{\Delta t}{2}\mathbf{v}_{p}^{n+1}.\end{split}(15)

Here,nnindexes time-step,𝐯pn=𝐮pn/γpn\mathbf{v}_{p}^{n}=\mathbf{u}_{p}^{n}/\gamma_{p}^{n},γpn=1+‖𝐮pn‖2/c2\gamma_{p}^{n}=\sqrt{1+\left\|\mathbf{u}_{p}^{n}\right\|^{2}/c^{2}}and similar for𝐯pn+1\mathbf{v}_{p}^{n+1}. Three frequently-used schemes differ only in their definition of𝐯¯p\bar{\mathbf{v}}_{p}.

The relativistic version of the Boris scheme[7]uses𝐯¯p=𝐮pn+1/2/γ¯pB​o​r​i​s\bar{\mathbf{v}}_{p}=\mathbf{u}_{p}^{n+1/2}/\bar{\gamma}_{p}^{Boris}, where𝐮pn+1/2=(𝐮pn+𝐮pn+1)/2\mathbf{u}_{p}^{n+1/2}=(\mathbf{u}_{p}^{n}+\mathbf{u}_{p}^{n+1})/2andγ¯pBoris=1+‖𝐮pn+Δ​t2​𝐄​(𝐱pn,tn)‖2c2.\bar{\gamma}_{p}^{\text{Boris}}=\sqrt{1+\frac{\left\|\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\mathbf{E}(\mathbf{x}_{p}^{n},t^{n})\right\|^{2}}{c^{2}}}.(16)

Note that this value ofγ¯p\bar{\gamma}_{p}is explicitly computable. Thus, the velocity update in (15) is linearly implicit in the same sense as the non-relativistic version of Boris. It can thus be analytically inverted using the same techniques.

However, in the relativistic case, the Boris method does not accurately capture the𝐄×𝐁\mathbf{E}\times\mathbf{B}drift. Vay[32]introduced a modification that does, choosing instead𝐯¯pVay=12​(𝐮pn+1γpn+1+𝐮pnγpn).\bar{\mathbf{v}}_{p}^{\text{Vay}}=\frac{1}{2}\left(\frac{\mathbf{u}_{p}^{n+1}}{\gamma_{p}^{n+1}}+\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}}\right).(17)

Note that this scheme is nownonlinearlyimplicit in the velocity update, sinceγpn+1\gamma_{p}^{n+1}now depends on the updated velocity. Nevertheless, Vay showed that this relation can be inverted analytically and thus remains effectively explicit in the same sense as Boris.

While the Vay method corrects the𝐄×𝐁\mathbf{E}\times\mathbf{B}drift velocity, it breaks the conservation of phase-space volume enjoyed by the Boris method. Higuera and Cary[19]introduced a scheme that both conserves phase-space volume and captures the𝐄×𝐁\mathbf{E}\times\mathbf{B}drift. That scheme makes the choice𝐯¯pHC=𝐮pn+1/2γpn+1/2,γpn+1/2=1+‖𝐮pn+1/2‖2c2\bar{\mathbf{v}}_{p}^{\text{HC}}=\frac{\mathbf{u}_{p}^{n+1/2}}{\gamma_{p}^{n+1/2}},\qquad\gamma_{p}^{n+1/2}=\sqrt{1+\frac{\left\|\mathbf{u}_{p}^{n+1/2}\right\|^{2}}{c^{2}}}(18)

Like the Vay scheme, this results in a nonlinearly implicit velocity update. Also like Vay, Higuera and Cary show that this relation can be inverted analytically using an analogous algebraic process, preserving the effective explicitness, and thus low per-step cost, of the method.

A review and numerical comparison of all three schemes may be found in[3]. A review of these and many other methods appears in[29], in which it is concluded that while no scheme is universally optimial, Higuera-Cary performs quite well overall. Also notable for our purposes is the use of a Higuera-Cary-like choice in[12]to find a semi-implicit PIC scheme with exact energy conservation. For both its structure-preserving properties and its convenience in our energy-conservation derivation, we make the Higuera-Cary choice of𝐯¯p\bar{\mathbf{v}}_{p}in the remainder of this work.

## 2.4Maxwell discretizations

It is widely acknowledged that it is important in a variety of contexts to discretize Maxwell’s equations in a manner that preserves the analytic light-wave dispersion to the extent possible. Doing so mitigates numerical Cherenkov radiation, helps capture dephasing in laser-wakefield acceleration[15], and captures Doppler harmonics in high-density plasmas subjected to petawatt class lasers[6].

Two particularly popular methods for doing this are the (a) finite difference time domain (FDTD) and (b) pseudo-spectral analytic time domain (PSATD) schemes. The former uses a finite difference spatial discretization on Yee’s lattice[34,16]in concert with a leapfrog-type temporal discretization. This leads to light-wave dispersion errors that are tolerable in many scenarios[25,30]. The latter uses a pseudospectral spatial discretization, leveraging this description to time-advance the vacuum portion of Maxwell’s equationsanalytically, with the only approximation coming from the assumption that the current is constant within a time-step[5,33]. This scheme thus captures light wave dispersionexactly. In particular, the Fourier transform of the electromagnetic fields are, given some current𝐣\mathbf{j}considered fixed within a time-step,ℱ​[𝐄hn+1]=C​ℱ​[𝐄hn]+i​S​c​𝐤^×ℱ​[𝐁hn]−Sk​c​ℱ​[𝐣]+(1−C)​𝐤^​(𝐤^⋅ℱ​[𝐄hn])+𝐤^​(𝐤^⋅ℱ​[𝐣])​(Sk​c−Δ​t),ℱ​[𝐁hn+1]=C​ℱ​[𝐁hn]−i​Sc​𝐤^×ℱ​[𝐄hn]+i​1−Ck​c2​𝐤^×ℱ​[𝐣],\begin{split}\mathcal{F}\left[\mathbf{E}^{n+1}_{h}\right]&=C\mathcal{F}\left[\mathbf{E}^{n}_{h}\right]+iSc\widehat{\mathbf{k}}\times\mathcal{F}\left[\mathbf{B}^{n}_{h}\right]-\frac{S}{kc}\mathcal{F}\left[\mathbf{j}\right]\\
&\qquad+(1-C)\widehat{\mathbf{k}}\left(\widehat{\mathbf{k}}\cdot\mathcal{F}\left[\mathbf{E}^{n}_{h}\right]\right)+\widehat{\mathbf{k}}\left(\widehat{\mathbf{k}}\cdot\mathcal{F}\left[\mathbf{j}\right]\right)\left(\frac{S}{kc}-\Delta t\right),\\
\mathcal{F}\left[\mathbf{B}^{n+1}_{h}\right]&=C\mathcal{F}\left[\mathbf{B}^{n}_{h}\right]-i\frac{S}{c}\widehat{\mathbf{k}}\times\mathcal{F}\left[\mathbf{E}^{n}_{h}\right]+i\frac{1-C}{kc^{2}}\widehat{\mathbf{k}}\times\mathcal{F}\left[\mathbf{j}\right],\end{split}(19)

whereC=cos⁡(k​c​Δ​t)C=\cos(kc\Delta t),S=sin⁡(k​c​Δ​t)S=\sin(kc\Delta t), andℱ\mathcal{F}denotes the discrete Fourier transform. The fields themselves are then recovered via an inverse Fourier transform

Most critically for our purposes, each of these schemes respects integration by parts in the sense that for arbitrary functions𝐅h\mathbf{F}_{h}and𝐆h\mathbf{G}_{h}defined on the mesh, one has∑h(𝐆h⋅∇h×𝐅h−𝐅h⋅∇h×𝐆h)=0,\sum_{h}\left(\mathbf{G}_{h}\cdot\nabla_{h}\times\mathbf{F}_{h}-\mathbf{F}_{h}\cdot\nabla_{h}\times\mathbf{G}_{h}\right)=0,(20)

where∇h×\nabla_{h}\timesdenotes the discretized curl operator. This identity is well-known to hold for the Yee lattice[34]and was proved for pseudospectral discretization in Appendix D of[28].

## 2.5Non-relativistic energy-conserving scheme

The scheme developed in this manuscript is the relativistic extension of the scheme from[28]. We thus find it useful to summarize the development of that scheme, as it strongly informs the relativistic case. Although the original scheme can be applied to either electrostatic or electromagnetic systems, we focus here only on the electromagnetic case. Finally, the non-relativistic scheme featured two versions. We present only “version 2” here, which was shown in[28]to feature improved energy conservation compared to “version 1” at minimal extra cost.

Even within “version 2”, there are several variants of the scheme depending on how Maxwell’s equations are discretized. The most immediate and natural takes the form𝐱p∗=𝐱pn+Δ​t2​𝐯pn,𝐄h∗=𝐄hn+Δ​t2​(c2​∇h×𝐁hn−𝐣hn,∗),𝐁h∗=𝐁hn−Δ​t2​∇h×𝐄hn,𝐯p∗=𝐯pn+Δ​t2​(𝐄p∗,∗+𝐯p∗×𝐁p∗,∗),𝐱pn+1=𝐱pn+Δ​t​𝐯p∗,𝐄hn+1=𝐄hn+Δ​t​(c2​∇h×𝐁hn+1/2−𝐣h∗,n+1/2),𝐁hn+1=𝐁hn−Δ​t​∇h×𝐄hn+1/2,𝐯p†=𝐯pn+Δ​t​(𝐄pn+1/2+𝐯p∗×𝐁pn+1/2),𝐯pn+1=𝐯p†​1+2​(𝐯p∗−𝐯p†+𝐯pn2)⋅(𝐯p†−𝐯pn)‖𝐯p†‖2,\begin{split}\mathbf{x}^{*}_{p}&=\mathbf{x}^{n}_{p}+\frac{\Delta t}{2}\mathbf{v}^{n}_{p},\\
\mathbf{E}_{h}^{*}&=\mathbf{E}_{h}^{n}+\frac{\Delta t}{2}\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n}-\mathbf{j}_{h}^{n,*}\right),\\
\mathbf{B}_{h}^{*}&=\mathbf{B}_{h}^{n}-\frac{\Delta t}{2}\nabla_{h}\times\mathbf{E}_{h}^{n},\\
\mathbf{v}^{*}_{p}&=\mathbf{v}^{n}_{p}+\frac{\Delta t}{2}\left(\mathbf{E}^{*,*}_{p}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{*,*}\right),\\
\mathbf{x}^{n+1}_{p}&=\mathbf{x}^{n}_{p}+\Delta t\mathbf{v}^{*}_{p},\\
\mathbf{E}_{h}^{n+1}&=\mathbf{E}_{h}^{n}+\Delta t\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{*,n+1/2}\right),\\
\mathbf{B}_{h}^{n+1}&=\mathbf{B}_{h}^{n}-\Delta t\nabla_{h}\times\mathbf{E}_{h}^{n+1/2},\\
\mathbf{v}^{\dagger}_{p}&=\mathbf{v}^{n}_{p}+\Delta t\left(\mathbf{E}^{n+1/2}_{p}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{v}^{n+1}_{p}&=\mathbf{v}_{p}^{\dagger}\sqrt{1+2\frac{\left(\mathbf{v}_{p}^{*}-\frac{\mathbf{v}_{p}^{\dagger}+\mathbf{v}_{p}^{n}}{2}\right)\cdot(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n})}{\|\mathbf{v}_{p}^{\dagger}\|^{2}}},\end{split}(21)

where𝐣hn,∗=1|𝐡|​∑pwp​𝐯pn​Sh​(𝐱p∗−𝐱h),𝐄p∗,∗=∑h𝐄h∗​Sh​(𝐱p∗−𝐱h),𝐣h∗,n+1/2=1|𝐡|​∑pwp​𝐯p∗​Sh​(𝐱pn+1/2−𝐱h),𝐱pn+1/2=𝐱pn+𝐱pn+12,𝐄hn+1/2=𝐄hn+𝐄hn+12,𝐄pn+1/2=∑h𝐄hn+1/2​Sh​(𝐱pn+1/2−𝐱h),\begin{split}\mathbf{j}_{h}^{n,*}&=\frac{1}{\lvert\mathbf{h}\rvert}\sum_{p}w_{p}\mathbf{v}_{p}^{n}S^{h}\left(\mathbf{x}_{p}^{*}-\mathbf{x}_{h}\right),\\
\mathbf{E}^{*,*}_{p}&=\sum_{h}\mathbf{E}_{h}^{*}S^{h}\left(\mathbf{x}^{*}_{p}-\mathbf{x}_{h}\right),\\
\mathbf{j}_{h}^{*,n+1/2}&=\frac{1}{\lvert\mathbf{h}\rvert}\sum_{p}w_{p}\mathbf{v}_{p}^{*}S^{h}\left(\mathbf{x}_{p}^{n+1/2}-\mathbf{x}_{h}\right),\\
\mathbf{x}_{p}^{n+1/2}&=\frac{\mathbf{x}_{p}^{n}+\mathbf{x}_{p}^{n+1}}{2},\quad\mathbf{E}_{h}^{n+1/2}=\frac{\mathbf{E}_{h}^{n}+\mathbf{E}_{h}^{n+1}}{2},\\
\mathbf{E}^{n+1/2}_{p}&=\sum_{h}\mathbf{E}_{h}^{n+1/2}S^{h}\left(\mathbf{x}^{n+1/2}_{p}-\mathbf{x}_{h}\right),\end{split}(22)

and definitions of the various evaluations of𝐁\mathbf{B}are directly analogous to those for𝐄\mathbf{E}.

Note that this scheme is explicit in the particle update, but that the time-integrator for Maxwell’s equations is Crank-Nicolson, making it linearly implicit in the field variables. The scheme can be made fully explicit with different Maxwell discretizations, which we detail below, but we begin with the simplest case.

Deriving energy conservation begins with the observation that∑pwp​𝐯p∗⋅(𝐯p†−𝐯pn)=Δ​t​∑pwp​𝐯p∗⋅(𝐄pn+1/2+𝐯p∗×𝐁pn+1/2)=Δ​t​∑p∑hwp​𝐯p∗⋅𝐄hn+1/2​Sh​(𝐱pn+1/2−𝐱h)=Δ​t​|𝐡|​∑h𝐄hn+1/2⋅𝐣h∗,n+1/2.\begin{split}\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\left(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n}\right)&=\Delta t\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\left(\mathbf{E}_{p}^{n+1/2}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{n+1/2}\right)\\
&=\Delta t\sum_{p}\sum_{h}w_{p}\mathbf{v}_{p}^{*}\cdot\mathbf{E}_{h}^{n+1/2}S^{h}\left(\mathbf{x}_{p}^{n+1/2}-\mathbf{x}_{h}\right)\\
&=\Delta t|\mathbf{h}|\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\mathbf{j}_{h}^{*,n+1/2}.\end{split}(23)

Analysis of the field update shows thatΔ​t​∑h𝐄hn+1/2⋅𝐣h∗,n+1/2=−∑h𝐄hn+1/2⋅(𝐄hn+1−𝐄hn−Δ​t​c2​∇h×𝐁hn+1/2)=−12​∑h(‖𝐄hn+1‖2−‖𝐄hn‖2)+Δ​t​c2​∑h𝐄hn+1/2⋅∇h×𝐁hn+1/2=−12​∑h(‖𝐄hn+1‖2−‖𝐄hn‖2)+Δ​t​c2​∑h𝐁hn+1/2⋅∇h×𝐄hn+1/2=−12​∑h(‖𝐄hn+1‖2−‖𝐄hn‖2)−c2​∑h𝐁hn+1/2⋅(𝐁hn+1−𝐁hn)=−12​∑h(‖𝐄hn+1‖2+c2​‖𝐁hn+1‖2−‖𝐄hn‖2−c2​‖𝐁hn‖2).\begin{split}\Delta t\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\mathbf{j}_{h}^{*,n+1/2}&=-\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\left(\mathbf{E}_{h}^{n+1}-\mathbf{E}_{h}^{n}-\Delta tc^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}\right)\\
&=-\frac{1}{2}\sum_{h}\left(\|\mathbf{E}_{h}^{n+1}\|^{2}-\|\mathbf{E}_{h}^{n}\|^{2}\right)\\
&\qquad+\Delta tc^{2}\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}\\
&=-\frac{1}{2}\sum_{h}\left(\|\mathbf{E}_{h}^{n+1}\|^{2}-\|\mathbf{E}_{h}^{n}\|^{2}\right)\\
&\qquad+\Delta tc^{2}\sum_{h}\mathbf{B}_{h}^{n+1/2}\cdot\nabla_{h}\times\mathbf{E}_{h}^{n+1/2}\\
&=-\frac{1}{2}\sum_{h}\left(\|\mathbf{E}_{h}^{n+1}\|^{2}-\|\mathbf{E}_{h}^{n}\|^{2}\right)\\
&\qquad-c^{2}\sum_{h}\mathbf{B}_{h}^{n+1/2}\cdot\left(\mathbf{B}_{h}^{n+1}-\mathbf{B}_{h}^{n}\right)\\
&=-\frac{1}{2}\sum_{h}\left(\|\mathbf{E}_{h}^{n+1}\|^{2}+c^{2}\|\mathbf{B}_{h}^{n+1}\|^{2}-\|\mathbf{E}_{h}^{n}\|^{2}-c^{2}\|\mathbf{B}_{h}^{n}\|^{2}\right).\end{split}(24)

Critically, this line of reasoning relies on the spatial discretization satisfying the integration by parts identity (20).

Finally,𝐯pn+1\mathbf{v}_{p}^{n+1}in (21) isdefinedto be the solution of the optimization problem𝐯pn+1=arg​min𝐯⁡‖𝐯−𝐯p†‖s.t.12​‖𝐯pn+1‖2−12​‖𝐯pn‖2=𝐯p∗⋅(𝐯p†−𝐯pn).\mathbf{v}_{p}^{n+1}=\operatorname*{arg\,min}_{\mathbf{v}}\left\|\mathbf{v}-\mathbf{v}_{p}^{\dagger}\right\|\quad\text{s.t.}\quad\frac{1}{2}\left\|\mathbf{v}_{p}^{n+1}\right\|^{2}-\frac{1}{2}\left\|\mathbf{v}_{p}^{n}\right\|^{2}=\mathbf{v}_{p}^{*}\cdot\left(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n}\right).(25)

It happens that this optimization problem has an analytic solution, given by the expression in the last line of (21). Thus, one trivially has∑p(wp2​‖𝐯pn+1‖2−wp2​‖𝐯pn‖2)=∑pwp​𝐯p∗⋅(𝐯p†−𝐯pn).\sum_{p}\left(\frac{w_{p}}{2}\left\|\mathbf{v}_{p}^{n+1}\right\|^{2}-\frac{w_{p}}{2}\left\|\mathbf{v}_{p}^{n}\right\|^{2}\right)=\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\left(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n}\right).(26)

Equations (23), (24), and (26) combine to straightforwardly imply∑pwp2​‖𝐯pn+1‖2+|𝐡|2​∑h(‖𝐄hn+1‖2+c2​‖𝐁hn+1‖2)=∑pwp2​‖𝐯pn‖2+|𝐡|2​∑h(‖𝐄hn‖2+c2​‖𝐁hn‖2),\begin{split}&\sum_{p}\frac{w_{p}}{2}\left\|\mathbf{v}_{p}^{n+1}\right\|^{2}+\frac{|\mathbf{h}|}{2}\sum_{h}\left(\left\|\mathbf{E}_{h}^{n+1}\right\|^{2}+c^{2}\left\|\mathbf{B}_{h}^{n+1}\right\|^{2}\right)\\
=&\sum_{p}\frac{w_{p}}{2}\left\|\mathbf{v}_{p}^{n}\right\|^{2}+\frac{|\mathbf{h}|}{2}\sum_{h}\left(\left\|\mathbf{E}_{h}^{n}\right\|^{2}+c^{2}\left\|\mathbf{B}_{h}^{n}\right\|^{2}\right),\end{split}(27)

which is precisely the statement of discrete energy conservation.

In[28], it is shown that the same line of reasoning may be adapted to show energy conservation when Maxwell’s equations are discretized with either the FDTD or PSATD methods described in Section2.4. In the case of FDTD, the scheme now reads𝐱p∗=𝐱pn+Δ​t2​𝐯pn,𝐁hn+1/2=𝐁hn−1/2−Δ​t​∇h×𝐄hn,𝐄h∗=𝐄hn+Δ​t2​(c2​∇h×𝐁hn+1/2−𝐣hn,∗),𝐯p∗=𝐯pn+Δ​t2​(𝐄p∗,∗+𝐯p∗×𝐁pn+1/2,∗),𝐄hn+1=𝐄hn+Δ​t​(c2​∇h×𝐁hn+1/2−𝐣h∗,n+1/2),𝐱pn+1=𝐱pn+Δ​t​𝐯p∗,𝐯p†=𝐯pn+Δ​t​(𝐄pn+1/2+𝐯p∗×𝐁pn+1/2),𝐯pn+1=𝐯p†​1+2​(𝐯p∗−𝐯p†+𝐯pn2)⋅(𝐯p†−𝐯pn)‖𝐯p†‖2.\begin{split}\mathbf{x}^{*}_{p}&=\mathbf{x}^{n}_{p}+\frac{\Delta t}{2}\mathbf{v}^{n}_{p},\\
\mathbf{B}_{h}^{n+1/2}&=\mathbf{B}_{h}^{n-1/2}-\Delta t\nabla_{h}\times\mathbf{E}_{h}^{n},\\
\mathbf{E}_{h}^{*}&=\mathbf{E}_{h}^{n}+\frac{\Delta t}{2}\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{n,*}\right),\\
\mathbf{v}^{*}_{p}&=\mathbf{v}^{n}_{p}+\frac{\Delta t}{2}\left(\mathbf{E}^{*,*}_{p}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{n+1/2,*}\right),\\
\mathbf{E}_{h}^{n+1}&=\mathbf{E}_{h}^{n}+\Delta t\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{*,n+1/2}\right),\\
\mathbf{x}^{n+1}_{p}&=\mathbf{x}^{n}_{p}+\Delta t\mathbf{v}^{*}_{p},\\
\mathbf{v}^{\dagger}_{p}&=\mathbf{v}^{n}_{p}+\Delta t\left(\mathbf{E}^{n+1/2}_{p}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{v}^{n+1}_{p}&=\mathbf{v}_{p}^{\dagger}\sqrt{1+2\frac{\left(\mathbf{v}_{p}^{*}-\frac{\mathbf{v}_{p}^{\dagger}+\mathbf{v}_{p}^{n}}{2}\right)\cdot(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n})}{\|\mathbf{v}_{p}^{\dagger}\|^{2}}}.\end{split}(28)

Directly analogous logic to that followed in (24) allows one to show that the total energyℰn=∑pwp2​‖𝐯pn‖2+|𝐡|2​∑h(‖𝐄hn‖2+c2​𝐁hn−1/2⋅𝐁hn+1/2)\mathcal{E}^{n}=\sum_{p}\frac{w_{p}}{2}\left\|\mathbf{v}_{p}^{n}\right\|^{2}+\frac{|\mathbf{h}|}{2}\sum_{h}\left(\left\|\mathbf{E}_{h}^{n}\right\|^{2}+c^{2}\mathbf{B}_{h}^{n-1/2}\cdot\mathbf{B}_{h}^{n+1/2}\right)(29)

is conserved. The definition of magnetic potential energy is non-standard, but differs from the standard definition only by𝒪​(Δ​t2)\mathcal{O}\left(\Delta t^{2}\right), is almost-surely non-negative, and has precedent in its usage in energy-conserving schemes with the FDTD method[12].

On the other hand, in the case of PSATD, it is necessary to modify𝐄pn+1/2→⟨𝐄p⟩nn+1≔1Δ​t​∫tntn+1𝐄h​(t)​𝑑t.\mathbf{E}_{p}^{n+1/2}\rightarrow\left\langle\mathbf{E}_{p}\right\rangle_{n}^{n+1}\coloneq\frac{1}{\Delta t}\int_{t^{n}}^{t^{n+1}}\mathbf{E}_{h}(t)\,dt.(30)

Computation is⟨𝐄h⟩nn+1\langle\mathbf{E}_{h}\rangle_{n}^{n+1}is rendered tractable by the fact that PSATD in fact gives an expression for𝐄h​(t)\mathbf{E}_{h}(t)on theentiretime interval[tn,tn+1][t^{n},t^{n+1}]. One can thus integrate this expression to find a formula for the Fourier transform of⟨𝐄h⟩nn+1\langle\mathbf{E}_{h}\rangle_{n}^{n+1}[28,31]ℱ​[⟨𝐄h⟩nn+1]=Sk​c​Δ​t​ℱ​[𝐄n]+i​1−Ck​Δ​t​𝐤^×ℱ​[𝐁n]−1−Ck2​c2​Δ​t​ℱ​[𝐣∗,n+1/2]+(1−Sk​c​Δ​t)​𝐤^​(𝐤^⋅ℱ​[𝐄n])+𝐤^​(𝐤^⋅ℱ​[𝐣∗,n+1/2])​(1−Ck2​c2​Δ​t−Δ​t2).\begin{split}\mathcal{F}\left[\left\langle\mathbf{E}_{h}\right\rangle_{n}^{n+1}\right]&=\frac{S}{kc\Delta t}\mathcal{F}\left[\mathbf{E}^{n}\right]+i\frac{1-C}{k\Delta t}\widehat{\mathbf{k}}\times\mathcal{F}\left[\mathbf{B}^{n}\right]-\frac{1-C}{k^{2}c^{2}\Delta t}\mathcal{F}\left[\mathbf{j}^{*,n+1/2}\right]\\
&\qquad+\left(1-\frac{S}{kc\Delta t}\right)\widehat{\mathbf{k}}\left(\widehat{\mathbf{k}}\cdot\mathcal{F}\left[\mathbf{E}^{n}\right]\right)\\
&\qquad+\widehat{\mathbf{k}}\left(\widehat{\mathbf{k}}\cdot\mathcal{F}\left[\mathbf{j}^{*,n+1/2}\right]\right)\left(\frac{1-C}{k^{2}c^{2}\Delta t}-\frac{\Delta t}{2}\right).\end{split}(31)

With these definitions in hand, the conclusion of (24) still holds, and is obtained through similar logic, so exact energy conservation is again achieved.

In addition to energy conservation, the scheme is second-order accurate by the following logic. DefineΓpn=1+2​(𝐯p∗−𝐯p†+𝐯pn2)⋅(𝐯p†−𝐯pn)‖𝐯p†‖2\Gamma_{p}^{n}=\sqrt{1+2\frac{\left(\mathbf{v}_{p}^{*}-\frac{\mathbf{v}_{p}^{\dagger}+\mathbf{v}_{p}^{n}}{2}\right)\cdot(\mathbf{v}_{p}^{\dagger}-\mathbf{v}_{p}^{n})}{\|\mathbf{v}_{p}^{\dagger}\|^{2}}}(32)

so that𝐯pn+1=Γpn​𝐯p†\mathbf{v}_{p}^{n+1}=\Gamma_{p}^{n}\mathbf{v}_{p}^{\dagger}.𝐯p†\mathbf{v}_{p}^{\dagger}is obtained using an explicit midpoint scheme that is trivially second-order accurate, so the scheme remains second-order if𝐯pn+1\mathbf{v}_{p}^{n+1}differs from𝐯p†\mathbf{v}_{p}^{\dagger}by at most𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right)(an extra order is required since we’re dealing with local truncation error). It can be shown that, for the versions of the scheme described here,Γpn=1+𝒪​(Δ​t4)\Gamma_{p}^{n}=1+\mathcal{O}\left(\Delta t^{4}\right), which trivially implies‖𝐯pn+1−𝐯p†‖=𝒪​(Δ​t4)\|\mathbf{v}_{p}^{n+1}-\mathbf{v}_{p}^{\dagger}\|=\mathcal{O}\left(\Delta t^{4}\right).

A minor caveat in this scheme is that there is no guarantee thatΓpn\Gamma_{p}^{n}is real, meaning it can give rise to rare particles with unphysical, imaginary velocities. The fraction of such particles is small simply because of the fact thatΓpn\Gamma_{p}^{n}is asymptotically close to unity. This fraction was further quantified in[28], where is was shown that it scales like𝒪​(Δ​t2​d)\mathcal{O}\left(\Delta t^{2d}\right), withddthe velocity-space dimension of the problem. That analysis will apply equally well to the relativistic scheme proposed here.

In practice, for the few particles with imaginary values ofΓpn\Gamma_{p}^{n}, we artificially setΓpn=1\Gamma_{p}^{n}=1as this still results in second-order temporal accuracy. This has been observed to still admit fractional energy errors of10−1010^{-10}or better in benchmark problems with reasonable time-step sizes.

## 3The method

As in the non-relativistic case, when incorporating relativistic effects it is simplest and most natural to begin with a Crank-Nicolson discretization of Maxwell’s equations. We thus propose the following relativistic generalization of the scheme (21):𝐱p∗=𝐱pn+Δ​t2​𝐮pnγpn,𝐄h∗=𝐄hn+Δ​t2​(c2​∇h×𝐁hn−𝐣hn,∗),𝐁h∗=𝐁hn−Δ​t2​∇h×𝐄hn,𝐮p∗=𝐮pn+Δ​t2​(𝐄p∗,∗+𝐮p∗γp∗×𝐁p∗,∗),𝐱pn+1=𝐱pn+Δ​t​𝐮p∗γp∗,𝐄hn+1=𝐄hn+Δ​t​(c2​∇h×𝐁hn+1/2−𝐣h∗,n+1/2),𝐁hn+1=𝐁hn−Δ​t​∇h×𝐄hn+1/2,𝐮p†=𝐮pn+Δ​t​(𝐄pn+1/2+𝐮p∗γp∗×𝐁pn+1/2),𝐮pn+1=Gr​(𝐮pn,𝐮p∗,𝐮p†),\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}},\\
\mathbf{E}_{h}^{*}&=\mathbf{E}_{h}^{n}+\frac{\Delta t}{2}\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n}-\mathbf{j}_{h}^{n,*}\right),\\
\mathbf{B}_{h}^{*}&=\mathbf{B}_{h}^{n}-\frac{\Delta t}{2}\nabla_{h}\times\mathbf{E}_{h}^{n},\\
\mathbf{u}_{p}^{*}&=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\left(\mathbf{E}_{p}^{*,*}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{*,*}\right),\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{n}+\Delta t\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}},\\
\mathbf{E}_{h}^{n+1}&=\mathbf{E}_{h}^{n}+\Delta t\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{*,n+1/2}\right),\\
\mathbf{B}_{h}^{n+1}&=\mathbf{B}_{h}^{n}-\Delta t\nabla_{h}\times\mathbf{E}_{h}^{n+1/2},\\
\mathbf{u}_{p}^{\dagger}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}_{p}^{n+1/2}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{u}^{n+1}_{p}&=G^{r}(\mathbf{u}_{p}^{n},\mathbf{u}_{p}^{*},\mathbf{u}_{p}^{\dagger}),\end{split}(33)

All definitions from (22) carry over unchanged, with only the additional specification that𝐯pn=𝐮pn/γpn\mathbf{v}_{p}^{n}=\mathbf{u}_{p}^{n}/\gamma_{p}^{n}and𝐯p∗=𝐮p∗/γp∗\mathbf{v}_{p}^{*}=\mathbf{u}_{p}^{*}/\gamma_{p}^{*}, whereγp∗=1+‖𝐮p∗‖2/c2\gamma_{p}^{*}=\sqrt{1+\left\|\mathbf{u}_{p}^{*}\right\|^{2}/c^{2}}and similar forγpn\gamma_{p}^{n}. The functionGrG^{r}is momentarily unspecified, but will be the central object of the development below.

Maxwell’s equations are unmodified when relativistic effects are taken into account, so it is unsurprising that the field update steps are identical in (33) and (21). We thus focus here on the particle push, knowing that if we can relate the one-step change in kinetic energy to∑h𝐄hn+1/2⋅𝐣h∗,n+1/2\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\mathbf{j}_{h}^{*,n+1/2}, the field-related portions of the energy conservation derivation – see (24) – will carry through without modification. In addition, we work with𝐄pn+1/2\mathbf{E}_{p}^{n+1/2}, secure in the knowledge that conservation can be recovered with PSATD by replacing it with⟨𝐄p⟩nn+1\langle\mathbf{E}_{p}\rangle^{n+1}_{n}as in Section2.5. We will give specifications of the scheme in FDTD and PSATD forms at the end of this section.

Note that the update equation for𝐮p∗\mathbf{u}^{*}_{p}is nonlinearly implicit, but in exactly the same sense as the Higuera-Cary scheme, this being the natural translation of that scheme to our context. The nonlinear system is thus analytically solvable in exactly the same manner. We outline that procedure in Appendix A for completeness. The particle update is thus effectively explicit in the same sense as the Boris, Vay, and Higuera-Cary schemes.

We now move to the definition ofGrG^{r}: it is defined as the solution of the optimization problemGr​(𝐮pn,𝐮p∗,𝐮p†)=arg​min𝐮⁡‖𝐮−𝐮p†‖2s.t.𝐯p∗⋅(𝐮p†−𝐮pn)=(γ​(𝐮)−γpn)​c2,G^{r}\left(\mathbf{u}_{p}^{n},\mathbf{u}_{p}^{*},\mathbf{u}_{p}^{\dagger}\right)=\operatorname*{arg\,min}_{\mathbf{u}}\left\|\mathbf{u}-\mathbf{u}_{p}^{\dagger}\right\|^{2}\quad\text{s.t.}\quad\mathbf{v}_{p}^{*}\cdot\left(\mathbf{u}_{p}^{\dagger}-\mathbf{u}_{p}^{n}\right)=\left(\gamma(\mathbf{u})-\gamma_{p}^{n}\right)c^{2},(34)

withγ​(𝐮)=1+‖𝐮‖2/c2\gamma(\mathbf{u})=\sqrt{1+\left\|\mathbf{u}\right\|^{2}/c^{2}}. To see why this is a logical choice, note thatΔ​t​|𝐡|​∑h𝐄hn+1/2⋅𝐣h∗,n+1/2=Δ​t​∑pwp​𝐯p∗⋅∑h𝐄hn+1/2​Sh​(𝐱pn+1/2−𝐱h)=Δ​t​∑pwp​𝐯p∗⋅𝐄pn+1/2=∑pwp​𝐯p∗⋅(𝐮p†−𝐮pn).\begin{split}\Delta t|\mathbf{h}|\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\mathbf{j}_{h}^{*,n+1/2}&=\Delta t\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\sum_{h}\mathbf{E}_{h}^{n+1/2}S^{h}\left(\mathbf{x}_{p}^{n+1/2}-\mathbf{x}_{h}\right)\\
&=\Delta t\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\mathbf{E}_{p}^{n+1/2}\\
&=\sum_{p}w_{p}\mathbf{v}_{p}^{*}\cdot\left(\mathbf{u}_{p}^{\dagger}-\mathbf{u}_{p}^{n}\right).\end{split}(35)

Thus, the constraint in the optimization problem that defines𝐮pn+1\mathbf{u}_{p}^{n+1}enforcesΔ​t​|𝐡|​∑h𝐄hn+1/2⋅𝐣h∗,n+1/2=∑pwp​c2​(γpn+1−γpn)=∑pwp​c2​(γpn+1−1)⏟K​En+1−∑pwp​c2​(γpn−1)⏟K​En,\begin{split}\Delta t|\mathbf{h}|\sum_{h}\mathbf{E}_{h}^{n+1/2}\cdot\mathbf{j}_{h}^{*,n+1/2}&=\sum_{p}w_{p}c^{2}\left(\gamma_{p}^{n+1}-\gamma_{p}^{n}\right)\\
&=\underbrace{\sum_{p}w_{p}c^{2}\left(\gamma_{p}^{n+1}-1\right)}_{KE^{n+1}}-\underbrace{\sum_{p}w_{p}c^{2}\left(\gamma_{p}^{n}-1\right)}_{KE^{n}},\end{split}(36)

whereK​EnKE^{n}denotes kinetic energy at time-stepnn. The remainder of the derivation of energy conservation, in which one shows that the grid-sum of𝐄⋅𝐣\mathbf{E}\cdot\mathbf{j}is related to the one-step change in potential energy, carries through completely unchanged from the non-relativistic case – again, because Maxwell’s equations and their discretization are unmodified. So, the constraint in (34) does indeed enforce exact total energy conservation.

As in the non-relativistic case, the objective function being minimized in (34) serves both to specify a unique value of𝐮pn+1\mathbf{u}_{p}^{n+1}– indeed, infinitely many values of𝐮\mathbf{u}satisfy the constraint – and to preserve convergence in the limit of small time-step. The value𝐮p†\mathbf{u}_{p}^{\dagger}is already a second-order accurate estimate of the proper velocity at timetn+1t^{n+1}, so it is sensible to ask that𝐮pn+1\mathbf{u}_{p}^{n+1}remain close to that value.

It remains to show both that (a) the optimization problem in (34) can be analytically solved so that the scheme’s computational cost remains comparable to other explicit methods, and (b) the resulting value of𝐮pn+1\mathbf{u}_{p}^{n+1}is in fact second-order accurate. As an additional verification exercise, we show that the scheme reduces to the non-relativistic one introduced in[28]as𝐮/c→0\mathbf{u}/c\rightarrow 0(i.e. the non-relativistic limit).

As a brief aside before proceeding, we note that local charge conservation is also an important issue in PIC schemes. By local charge conservation, we mean exact satisfaction of a discrete continuity equationρhn+1−ρhnΔ​t+∇h⋅𝐣h∗,n+1/2=0,\frac{\rho_{h}^{n+1}-\rho_{h}^{n}}{\Delta t}+\nabla_{h}\cdot\mathbf{j}_{h}^{*,n+1/2}=0,(37)

which guarantees that Gauss’s law is exactly satisfied at each time. The non-relativistic scheme was shown in[28]to be trivially compatible with existing charge conservation schemes developed in[11,12,27]. Key features of these schemes are that shape functions for current and charge deposition are different, and particle trajectories within a time-step must be decomposed cell-wise. Because the continuity equation and current deposition are unmodified by relativistic effects, these arguments extend trivially to the relativistic case. Since the derivations are quite cumbersome, we refer to the references above for more detail.

## 3.1Optimization solution

We proceed using Lagrange multipliers: the minimizer𝐮pn+1\mathbf{u}_{p}^{n+1}satisfies∇𝐮{12​‖𝐮−𝐮p†‖+λ​𝐯p∗⋅(𝐮p†−𝐮pn)−λ​(γ​(𝐮)−γpn)​c2}|𝐮=𝐮pn+1=0,\left.\nabla_{\mathbf{u}}\left\{\frac{1}{2}\left\|\mathbf{u}-\mathbf{u}_{p}^{\dagger}\right\|+\lambda\mathbf{v}_{p}^{*}\cdot\left(\mathbf{u}_{p}^{\dagger}-\mathbf{u}_{p}^{n}\right)-\lambda\left(\gamma(\mathbf{u})-\gamma_{p}^{n}\right)c^{2}\right\}\right\rvert_{\mathbf{u}=\mathbf{u}_{p}^{n+1}}=0,(38)

where the factor of1/21/2is introduced for convenience and does not move the minimizer. Computing the derivative and doing some mild rearranging yields(1−λ1+‖𝐮n+1‖2/c2)​𝐮n+1=𝐮†,\left(1-\frac{\lambda}{\sqrt{1+\left\|\mathbf{u}^{n+1}\right\|^{2}/c^{2}}}\right)\mathbf{u}^{n+1}=\mathbf{u}^{\dagger},(39)

where we have suppressed theppsubscript when no confusion results. We see that the minimizer is a scalar multiple of𝐮†\mathbf{u}^{\dagger}. We call that scalarΓn\Gamma^{n}as in[28]. Note thatΓn\Gamma^{n}is now a function of the minimizer, but we may still assign it a name and compute it in terms of the other known velocities, since they specify𝐮n+1\mathbf{u}^{n+1}. So, we proceed with substituting𝐮n+1=Γn​𝐮†\mathbf{u}^{n+1}=\Gamma^{n}\mathbf{u}^{\dagger}into the constraint in (34) to find an explicit formula forΓn\Gamma^{n}. A few lines of straightforward algebra bring us toΓn=c‖𝐮†‖​[(γn+𝐯∗⋅(𝐮†−𝐮n)c2)2−1]1/2.\Gamma^{n}=\frac{c}{\left\|\mathbf{u}^{\dagger}\right\|}\left[\left(\gamma^{n}+\frac{\mathbf{v}^{*}\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}\right)^{2}-1\right]^{1/2}.(40)

While this is a satisfactory expression for implementation in code, it will facilitate later analysis to rearrange this expression. Note first that𝐯∗⋅(𝐮†−𝐮n)c2=(𝐯∗−𝐮†+𝐮nγ†+γn+𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2=(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2+1c2​‖𝐮†‖2−‖𝐮n‖2γ†+γn=(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2+(γ†)2−(γn)2γ†+γn=(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2+γ†−γn.\begin{split}\frac{\mathbf{v}^{*}\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}&=\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}+\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}\\
&=\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}+\frac{1}{c^{2}}\frac{\left\|\mathbf{u}^{\dagger}\right\|^{2}-\left\|\mathbf{u}^{n}\right\|^{2}}{\gamma^{\dagger}+\gamma^{n}}\\
&=\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}+\frac{(\gamma^{\dagger})^{2}-(\gamma^{n})^{2}}{\gamma^{\dagger}+\gamma^{n}}\\
&=\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}+\gamma^{\dagger}-\gamma^{n}.\end{split}(41)

Substituting this into the expression forΓn\Gamma^{n}above, and also bringing the factor ofc/‖𝐮†‖c/\|\mathbf{u}^{\dagger}\|inside the square root and expressing it in terms ofγ†\gamma^{\dagger}, givesΓn=[(γ†+(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2)2−1(γ†)2−1]1/2.\Gamma^{n}=\left[\frac{\left(\gamma^{\dagger}+\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\frac{\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}\right)^{2}-1}{\left(\gamma^{\dagger}\right)^{2}-1}\right]^{1/2}.(42)

In the name of brevity, defineδ=(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)c2.\delta=\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\frac{\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{c^{2}}.(43)

Then, expanding the square in the expression forΓ\Gammaand canceling terms givesΓn=[1+2​δ​γ†+δ2(γ†)2−1]1/2.\Gamma^{n}=\left[1+\frac{2\delta\gamma^{\dagger}+\delta^{2}}{\left(\gamma^{\dagger}\right)^{2}-1}\right]^{1/2}.(44)

This expression makes it abundantly clear that understanding the proximity ofΓ\Gammato unity comes down to understanding the size ofδ\delta. Analyzing the scaling ofδ\deltawith time-step will be the crux of the next subsection in which we understand the order of the scheme.

Before proceeding, we note that as in the non-relativistic case[28], there is no guarantee thatΓ\Gammais a real number.δ\deltamay be negative, and in some rare cases this may lead toΓ\Gammataking on an imaginary value. As noted above, the frequency of such occurrences was quantified in[28], and that analysis is unmodified by moving to the relativistic regime.

## 3.2Reproducing the non-relativistic case

Writing(γ†)2−1\left(\gamma^{\dagger}\right)^{2}-1in terms of velocities, we can findδ(γ†)2−1=(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)‖𝐮†‖2.\frac{\delta}{\left(\gamma^{\dagger}\right)^{2}-1}=\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\frac{\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)}{\left\|\mathbf{u}^{\dagger}\right\|^{2}}.(45)

In the non-relativistic limit, i.e.𝐯/c→0\mathbf{v}/c\rightarrow 0, one has𝐮→𝐯\mathbf{u}\rightarrow\mathbf{v}, so we getδ(γ†)2−1→(𝐯∗−𝐯†+𝐯n2)⋅(𝐯†−𝐯n)‖𝐯†‖2.\frac{\delta}{\left(\gamma^{\dagger}\right)^{2}-1}\rightarrow\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{v}^{\dagger}+\mathbf{v}^{n}}{2}\right)\cdot\left(\mathbf{v}^{\dagger}-\mathbf{v}^{n}\right)}{\left\|\mathbf{v}^{\dagger}\right\|^{2}}.(46)

On the other hand,δ2(γ†)2−1=1‖𝐮†‖2​c2​[(𝐯∗−𝐮†+𝐮nγ†+γn)⋅(𝐮†−𝐮n)]2→0,\frac{\delta^{2}}{\left(\gamma^{\dagger}\right)^{2}-1}=\frac{1}{\left\|\mathbf{u}^{\dagger}\right\|^{2}c^{2}}\left[\left(\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right)\cdot\left(\mathbf{u}^{\dagger}-\mathbf{u}^{n}\right)\right]^{2}\rightarrow 0,(47)

where this goes to zero in the non-relativistic limit because all velocities are negligible compared tocc.

So, we get that in the non-relativistic limitΓn→[1+2​(𝐯∗−𝐯†+𝐯n2)⋅(𝐯†−𝐯n)‖𝐯†‖2]1/2,\Gamma^{n}\rightarrow\left[1+2\frac{\left(\mathbf{v}^{*}-\frac{\mathbf{v}^{\dagger}+\mathbf{v}^{n}}{2}\right)\cdot\left(\mathbf{v}^{\dagger}-\mathbf{v}^{n}\right)}{\left\|\mathbf{v}^{\dagger}\right\|^{2}}\right]^{1/2},(48)

which is exactly the non-relativistic expression (32).

## 3.3Accuracy

As already discussed,𝐮†\mathbf{u}^{\dagger}is a second-order accurate approximation of the (proper) velocity at timetn+1t^{n+1}. To establish that𝐮n+1\mathbf{u}^{n+1}is as well, it suffices to show that‖𝐮n+1−𝐮†‖=𝒪​(Δ​t3)\|\mathbf{u}^{n+1}-\mathbf{u}^{\dagger}\|=\mathcal{O}\left(\Delta t^{3}\right). For this, it suffices to show thatΓn=1+𝒪​(Δ​t3)\Gamma^{n}=1+\mathcal{O}\left(\Delta t^{3}\right).

Recall that in the non-relativistic case, we were actually able to show thatΓn=1+𝒪​(Δ​t4)\Gamma^{n}=1+\mathcal{O}\left(\Delta t^{4}\right)for the version of the scheme considered here. This has the benefit of reducing the instances in whichΓ\Gammais imaginary, thus improving energy conservation in practice. We are not able to show a result quite this strong here, but settle instead forΓn=1+𝒪​(Δ​t3)\Gamma^{n}=1+\mathcal{O}\left(\Delta t^{3}\right). The derivation appears in Appendix B. However, the𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right)term arises exclusively from a difference of Lorentz factors, and thus is only non-negligible when velocities are large.

That is to say,Γn\Gamma^{n}differs from unity by only𝒪​(Δ​t4)\mathcal{O}\left(\Delta t^{4}\right)when velocities are non-relativistic, but for large velocities may differ from unity by𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right). In both cases, the scheme remains second-order accurate. We merely desire the improved scaling to minimize the frequency of imaginary values ofΓn\Gamma^{n}. However, as discussed at length in[28], imaginary values ofΓn\Gamma^{n}are far more likely forextremely smallvelocities, since this makes the denominator appearing in (44) small. Thus, we find degraded scaling inΔ​t\Delta tthat occurs only atlargevelocities to be quite tolerable.

It is possible to achieveΓn=1+𝒪​(Δ​t4)\Gamma^{n}=1+\mathcal{O}\left(\Delta t^{4}\right)by making significant modifications to the scheme. Namely, we show in Appendix C that if instead of using any of the well-studied definitions of𝐯¯p\bar{\mathbf{v}}_{p}defined in (16), (17), and (18) we build the scheme from the definition𝐯¯p=𝐮pn+𝐮pn+1γpn+γpn+1,\bar{\mathbf{v}}_{p}=\frac{\mathbf{u}_{p}^{n}+\mathbf{u}_{p}^{n+1}}{\gamma_{p}^{n}+\gamma_{p}^{n+1}},(49)

then we do, in fact, achieveΓn=1+𝒪​(Δ​t4)\Gamma^{n}=1+\mathcal{O}\left(\Delta t^{4}\right). Note that this choice of𝐯¯p\bar{\mathbf{v}}_{p}still results in second-order accuracy but is, to the best of our knowledge, unstudied. However, we seenoimprovement whatsoever in energy conservation with this version of the scheme in any of the numerical tests detailed in Section4. This lends further credence to our assessment above that the𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right)scaling above is acceptable because it only affects particles with large velocities. We prefer the scheme described here in the main text due to its analogy to the Higuera-Cary integrator, which has well-known structure preserving properties, but report the alternative scheme’s derivation in Appendix C as a point of academic interest.

## 3.4FDTD and PSATD versions

The scheme (33) uses the Crank-Nicolson discretization of Maxwell’s equations. As in the non-relativistic case, the developments here can be straightforwardly applied to FDTD and PSATD Maxwell discretizations, with the latter only requiring modification of the evaluation of𝐄\mathbf{E}as described in Section2.5. We record these versions of the scheme here for completeness, with the derivations of energy conservation requiring no additional insights.

The FDTD version is written as follows.𝐱p∗=𝐱pn+Δ​t2​𝐮pnγpn,𝐁hn+1/2=𝐁hn−1/2−Δ​t​∇h×𝐄hn,𝐄h∗=𝐄hn+Δ​t2​(c2​∇h×𝐁hn+1/2−𝐣hn,∗),𝐮p∗=𝐮pn+Δ​t2​(𝐄p∗,∗+𝐮p∗γp∗×𝐁p∗,∗),𝐄hn+1=𝐄hn+Δ​t​(c2​∇h×𝐁hn+1/2−𝐣h∗,n+1/2),𝐱pn+1=𝐱pn+Δ​t​𝐮p∗γp∗,𝐮p†=𝐮pn+Δ​t​(𝐄pn+1/2+𝐮p∗γp∗×𝐁pn+1/2),𝐮pn+1=𝐮p†​1+2​δp​γp†+δp2(γp†)2−1,\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}},\\
\mathbf{B}_{h}^{n+1/2}&=\mathbf{B}_{h}^{n-1/2}-\Delta t\nabla_{h}\times\mathbf{E}_{h}^{n},\\
\mathbf{E}_{h}^{*}&=\mathbf{E}_{h}^{n}+\frac{\Delta t}{2}\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{n,*}\right),\\
\mathbf{u}_{p}^{*}&=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\left(\mathbf{E}_{p}^{*,*}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{*,*}\right),\\
\mathbf{E}_{h}^{n+1}&=\mathbf{E}_{h}^{n}+\Delta t\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{*,n+1/2}\right),\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{n}+\Delta t\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}},\\
\mathbf{u}_{p}^{\dagger}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}_{p}^{n+1/2}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{u}^{n+1}_{p}&=\mathbf{u}_{p}^{\dagger}\sqrt{1+\frac{2\delta_{p}\gamma^{\dagger}_{p}+\delta_{p}^{2}}{\left(\gamma_{p}^{\dagger}\right)^{2}-1}},\end{split}(50)

withδ\deltaas defined in (43). Note that the non-standard definition of magnetic potential energy in (29) is still required here, and for precisely the same reasons.

The PSATD version of the scheme is written as follows.𝐱p∗=𝐱pn+Δ​t2​𝐮pnγpn,(𝐄h∗,𝐁h∗)=PSATD​(𝐄hn,𝐁hn,𝐣hn,∗,Δ​t/2),𝐮p∗=𝐮pn+Δ​t2​(𝐄p∗,∗+𝐮p∗γp∗×𝐁p∗,∗),𝐱pn+1=𝐱pn+Δ​t​𝐮p∗γp∗,(𝐄hn+1,𝐁hn+1)=PSATD​(𝐄hn,𝐁hn,𝐣h∗,n+1/2,Δ​t)𝐮p†=𝐮pn+Δ​t​(⟨𝐄p⟩nn+1+𝐮p∗γp∗×𝐁pn+1/2),𝐮pn+1=𝐮p†​1+2​δp​γp†+δp2(γp†)2−1,\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}},\\
\left(\mathbf{E}_{h}^{*},\mathbf{B}_{h}^{*}\right)&=\text{PSATD}\left(\mathbf{E}_{h}^{n},\mathbf{B}_{h}^{n},\mathbf{j}_{h}^{n,*},\Delta t/2\right),\\
\mathbf{u}_{p}^{*}&=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\left(\mathbf{E}_{p}^{*,*}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{*,*}\right),\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{n}+\Delta t\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}},\\
\left(\mathbf{E}_{h}^{n+1},\mathbf{B}_{h}^{n+1}\right)&=\text{PSATD}\left(\mathbf{E}_{h}^{n},\mathbf{B}_{h}^{n},\mathbf{j}_{h}^{*,n+1/2},\Delta t\right)\\
\mathbf{u}_{p}^{\dagger}&=\mathbf{u}_{p}^{n}+\Delta t\left(\left\langle\mathbf{E}_{p}\right\rangle^{n+1}_{n}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{u}^{n+1}_{p}&=\mathbf{u}_{p}^{\dagger}\sqrt{1+\frac{2\delta_{p}\gamma^{\dagger}_{p}+\delta_{p}^{2}}{\left(\gamma_{p}^{\dagger}\right)^{2}-1}},\end{split}(51)

wherePSATD​(𝐄,𝐁,𝐣,Δ​t)\text{PSATD}(\mathbf{E},\mathbf{B},\mathbf{j},\Delta t)denotes that PSATD advancement of𝐄\mathbf{E}and𝐁\mathbf{B}by the time-stepΔ​t\Delta tusing the fixed current𝐣\mathbf{j}according to (19), and⟨𝐄p⟩nn+1=∑h⟨𝐄h⟩nn+1​Sh​(𝐱h−𝐱pn+1/2)\left\langle\mathbf{E}_{p}\right\rangle^{n+1}_{n}=\sum_{h}\left\langle\mathbf{E}_{h}\right\rangle^{n+1}_{n}S^{h}(\mathbf{x}_{h}-\mathbf{x}_{p}^{n+1/2})and⟨𝐄h⟩nn+1\left\langle\mathbf{E}_{h}\right\rangle^{n+1}_{n}is defined by its Fourier transform given in (31).

Note that both of these versions of the scheme are fully explicit.

## 4Numerical results

We report results from an implementation of the scheme above on a periodic box in two spatial and two velocity dimensions. We denote the dimensions of the box byLxL_{x}andLyL_{y}. The number of cells in each direction isNxN_{x}andNyN_{y}, respectively. Except where explicitly noted, we work in the non-dimensionlization in which length is scaled byc/ωpc/\omega_{p}, so that the speed of light is normalized to unity.

Throughout, we compare against a “standard PIC” discretization, either with PSATD or Crank-Nicolson discretization. By “standard”, we will mean the following scheme, written in the CN case for simplicity but readily generalizable to PSATD as in the discussion above:𝐱p∗=𝐱pn+Δ​t2​𝐮pnγpn,𝐮p∗=𝐮pn+Δ​t2​(𝐄pn,∗+𝐮p∗γp∗×𝐁pn,∗),𝐱pn+1=𝐱pn+Δ​t​𝐮p∗γp∗,𝐄hn+1=𝐄hn+Δ​t​(c2​∇h×𝐁hn+1/2−𝐣h∗,n+1/2),𝐁hn+1=𝐁hn−Δ​t​∇h×𝐄hn+1/2,𝐮pn+1=𝐮pn+Δ​t​(𝐄pn+1/2+𝐮p∗γp∗×𝐁pn+1/2),\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}},\\
\mathbf{u}_{p}^{*}&=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\left(\mathbf{E}_{p}^{n,*}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{n,*}\right),\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{n}+\Delta t\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}},\\
\mathbf{E}_{h}^{n+1}&=\mathbf{E}_{h}^{n}+\Delta t\left(c^{2}\nabla_{h}\times\mathbf{B}_{h}^{n+1/2}-\mathbf{j}_{h}^{*,n+1/2}\right),\\
\mathbf{B}_{h}^{n+1}&=\mathbf{B}_{h}^{n}-\Delta t\nabla_{h}\times\mathbf{E}_{h}^{n+1/2},\\
\mathbf{u}_{p}^{n+1}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}_{p}^{n+1/2}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\end{split}(52)

Note that this resembles the energy conserving scheme closely, but without the correction to enforce energy conservation and without the initial half-step, “predictor” stage for the electromagnetic fields (recall that this is what distinguishes “version 1” and “version 2” in[28]). The scheme is second-order accurate and still based on the Higuera-Cary particle update, thus isolating the differences between this and the new scheme to the novel pieces introduced above.

## 4.1Relativistic two-stream instability

Our implementation is verified using a standard two-stream instability test problem. We work in one configuration (Ny=1N_{y}=1) and two velocity dimensions. We initializeffwith two counter-streaming beams as follows:f0​(x,ux,uy)=14​π​ut​h2​e−uy2/2​ut​h​(e−(ux−ub)2/2​ut​h+e−(ux+ub)2/2​ut​h)×(1+αx​cos⁡(2​π​xL)).\begin{split}f_{0}(x,u_{x},u_{y})&=\frac{1}{4\pi u_{th}^{2}}e^{-u_{y}^{2}/2u_{th}}\left(e^{-(u_{x}-u_{b})^{2}/2u_{th}}+e^{-(u_{x}+u_{b})^{2}/2u_{th}}\right)\\
&\qquad\times\left(1+\alpha_{x}\cos\left(\frac{2\pi x}{L}\right)\right).\end{split}(53)

In the cold beam limit (ut​h→0u_{th}\rightarrow 0), the linear dispersion relation for this problem is[12]γb−3(ω+k​vb)2+γb−3(ω−k​vb)2=2,\frac{\gamma_{b}^{-3}}{(\omega+kv_{b})^{2}}+\frac{\gamma_{b}^{-3}}{(\omega-kv_{b})^{2}}=2,(54)

whereγb=1+ub2/c2\gamma_{b}=\sqrt{1+u_{b}^{2}/c^{2}}andvb=ub/γbv_{b}=u_{b}/\gamma_{b}. Note that the only distinction between this and the non-relativistic dispersion relation is the factor ofγb−3\gamma_{b}^{-3}, which serves to reduce the growth rate at relativistic beam velocities.

For our test, we chooseL=2​πL=2\pi,αx=0.01\alpha_{x}=0.01,ut​h=0.05u_{th}=0.05, and test four values ofvb=0.3,0.4,0.5,0.6v_{b}=0.3,0.4,0.5,0.6. Withub≫ut​hu_{b}\gg u_{th}, we find that the cold-beam approximation accurately predicts growth rates.

We use the discretization parametersΔ​t=0.1\Delta t=0.1,Nx=32N_{x}=32,10001000particles per cell (for a total of32,00032,000particles), and run to final timeT=40T=40. We utilize a quiet start in configuration space, while velocities are randomly sampled from the appropriate normal distributions. The same random sampling is used for each scheme tested, so initial conditions are in fact identical. In Figure1, we observe excellent agreement with the relativistic growth rate as well as with the classical limit for smaller values ofvbv_{b}. In addition, the energy-conserving and standard PIC schemes agree well.Figure 1:Electrostatic potential energy for the two-stream test cases, showing good agreement with theoretical growth rate, even when the relativistic growth rate differs markedly from the classical one.

In Figure2we report fractional energy errors and, for the energy-conserving schemes, the number of particles withΓp2<0\Gamma_{p}^{2}<0at each time-step. The improved energy conservation of the new scheme is readily apparent, as is the rarity of particles with imaginaryΓ\Gamma. The displayed plots are for thevb=0.6v_{b}=0.6case, but other cases are not meaningfully different.Figure 2:Left: Fractional error in total energy as a function of time for the two-stream test problem. Improved energy accuracy of the new scheme is readily observed.Right: Number of particles at each time-step with imaginaryΓ\Gammavalues at each time-step.

## 4.2Relativistic Landau Damping

We reproduce a test case studied in[1], in which a method for machine-precision evaluation of the plasma dispersion function is presented that applies to relativistic plasmas. This results in predictions for relativistic modifications of the classical Landau damping rates.

In contrast to other tests, we work here in a non-dimensionalization consistent with that used in[1]. Namely, while time is still scaled by the plasma frequency, length is scaled by Debye length and velocity by the thermal velocity. The speed of light presented is then given in multiples of the thermal velocity, with smaller values ofcccorresponding to more relativistic cases.

We useL=6​πL=6\pi, to admit perturbations with wave-numberk=1/3k=1/3to mirror the published damping rates of[1]. The initial distribution isf0​(x,ux,uy)=12​π​e−(ux2+uy2)/2​(1+α​cos⁡k​x).f_{0}(x,u_{x},u_{y})=\frac{1}{2\pi}e^{-(u_{x}^{2}+u_{y}^{2})/2}\left(1+\alpha\cos kx\right).(55)

We chooseα=0.05\alpha=0.05. Discretization parameters areΔ​t=0.025\Delta t=0.025(to resolve the faster light speed compared to other test problems),Nx=64N_{x}=64, final timeT=30T=30, and80008000particles per cell to mitigate sampling noise that can affect the observation of the very small damping rates in these problems.

Again following[1], we setc=8c=8– the “strongly relativistic” case studied there. The predicted damping rate isγr​e​l=0.01113948\gamma_{rel}=0.01113948for the proper-velocity Maxwellian we use as our initial condition. Meanwhile, the non-relativistic prediction of damping rate isγc​l​a​s​s=0.02587\gamma_{class}=0.02587. Potential energy is reported in Figure3, which shows a damping rate that matches the relativistic prediction for all schemes tested.Figure 3:Potential energy as a function of time for relativistic Landau damping test case. All tested schemes match the relativistic damping rate predicted by linear theory.

Energy conservation and the number of problematic particles for the energy-conserving schemes are reported in Figure4. While standard PIC conserves energy quite well for this simple problem, 6 orders of magnitude improvement in conservation is still observed for the new energy-conserving schemes. Problematic particles are quite rare in this example.Figure 4:Energy conservation (left) and number of problematic particles at each time-step (right) for the Landau damping test case. The expected roundoff-level energy accuracy is observed for the energy conserving schemes.

## 4.3Relativistic Weibel instability

We study a slightly modified version of the 1D2V Weibel instability test case of[14], with the modifications coming only from the inclusion of relativistic effects. Using our nondimensionalization in whichc=1c=1corresponds to the scaling used in[14], and we initialize the distribution function and fields according tof​(y,ux,uy,t=0)=1π​β​e−uy2/β​[δ​e−(ux−u0,1)2/β+(1−δ)​e−(ux+u0,2)2/β],Ex​(y,t=0)=Ey​(y,t=0)=0,Bz​(y,t=0)=b​sin⁡(k0​y).\begin{split}f(y,u_{x},u_{y},t=0)&=\frac{1}{\pi\beta}e^{-u_{y}^{2}/\beta}\left[\delta e^{-(u_{x}-u_{0,1})^{2}/\beta}+(1-\delta)e^{-(u_{x}+u_{0,2})^{2}/\beta}\right],\\
E_{x}(y,t=0)&=E_{y}(y,t=0)=0,\\
B_{z}(y,t=0)&=b\sin(k_{0}y).\end{split}(56)

We mimic the parameters of Run 1 from[14], but with increased beam velocitiesu0,1u_{0,1}andu0,2u_{0,2}to emphasize relativistic effects. We chooseβ=0.01,δ=0.5,u0,1=u0,2=1.25,b=0.001,k0=0.2.\begin{split}&\beta=0.01,\qquad\delta=0.5,\qquad u_{0,1}=u_{0,2}=1.25,\\
&b=0.001,\qquad k_{0}=0.2.\end{split}(57)

This choice of proper velocity for the two counter-streaming beams corresponds to a physical velocity of0.78​c0.78c, making relativistic effects quite significant.

Because the initial perturbation amplitude (controlled bybb) is so small, and the Weibel instability saturates at relatively low amplitude, we again employ a for this test to observe the linear growth of the instability over several orders of magnitude. In particular, the initial particle positions are specified deterministically on a uniform grid. Particle velocities are still randomly sampled from the specified bi-Maxwellian distribution.

We useNy=32N_{y}=32,Δ​t=0.1\Delta t=0.1, and32003200particles per cell. The total potential energy for both conservative and non-conservative schemes with Crank-Nicolson and PSATD appears in Figure5. All schemes agree well.Figure 5:Total potential energy for Weibel test problem, using Crank-Nicolson and PSATD discretizations of Maxwell’s equations. We show both the new conservative schemes and classical PIC methods. All results agree well, in that all four curves overlap.

Some minor differences are visible in the nonlinear phase of the instability when the potential energy is broken into components from magnetic and electric potentials, similar to what is shown in[14]. This is shown in Figure6. Distinctions between the conservative and non-conservative schemes are only visible for this problem by plotting total energy conservation errors, which we do in Figure7. As indicated by the fact that the conservative schemes conserve energy to double precision, we observezeroproblematic particles for this test problem, both with PSATD and Crank-Nicolson.Figure 6:Breakdown of sources of potential energy in Weibel test problem. We show only the conservative schemes here, as non-conservative schemes agree well on these axes.Figure 7:Fractional error in total energy for Weibel instability problem. Improved energy accuracy of the proposed scheme is readily observed.

## 4.4Filamentation instability

The filamentation instability presents a more challenging verification exercise because (a) it is inherently two dimensional, since the beam propagation direction and unstable wave-vectors are orthogonal, and (b) the fastest growing wave numbers occur ask→∞k\rightarrow\infty. In an effort to resolve largekkvalues where the asymptotic growth rate is known, we use a small domain sizeLx=Ly=πL_{x}=L_{y}=\pi. We initialize particles by sampling from the distributionf0​(ux,uy)=14​π​e−uy2/2​ut​h​(e−(ux−ub)2/2​ut​h+e−(ux+ub)2/2​ut​h).f_{0}(u_{x},u_{y})=\frac{1}{4\pi}e^{-u_{y}^{2}/2u_{th}}\left(e^{-(u_{x}-u_{b})^{2}/2u_{th}}+e^{-(u_{x}+u_{b})^{2}/2u_{th}}\right).(58)

Note that unlike the two-stream case, we initialize an exactly homogeneous distribution in configuration space, relying on sampling noise to trigger the instability at arbitrary wave numbers.

With beams propagating along thexx-axis, the instability generates density perturbations along theyy-axis. Again motivated by the desire to capture large wave-numbers inyywhile keeping computational cost manageable, we chooseNx=32N_{x}=32andNy=2048N_{y}=2048. We use200200particles per cell,Δ​t=0.1\Delta t=0.1, and show results withub=0.75u_{b}=0.75.

We verify against the theoretical linear growth rate in the cold beam and infinite wave-number limits, given in our normalization by[9]δ=vbγb,\delta=\frac{v_{b}}{\sqrt{\gamma_{b}}},(59)

whereγb=1+ub2\gamma_{b}=\sqrt{1+u_{b}^{2}}andvb=ub/γbv_{b}=u_{b}/\gamma_{b}. This expression differs from that in[9]by a factor of2\sqrt{2}only because we normalize time by the plasma frequency corresponding to the overall plasma density, while they use the density of an individual beam.

For verification, we present a case with perfectly cold beams – i.e.ut​h=0u_{th}=0. The growth in magnetic potential compared to the analytically predicted growth rate is shown in Figure8.Figure 8:Growth of potential energy in the filamentation test case with cold initial beams. Theoretical growth rate ink→∞k\rightarrow\inftylimit is approximately reproduced.

Of course, any numerical simulation can resolve only finite wave-numbers, so we are satisfied in observing that the growth rate is near, but slightly smaller than, the theoretical prediction ask→∞k\rightarrow\infty.

We also plot energy conservation for each scheme in Figure9. As in the Weibel test case, no problematic particles are observed in the entire simulation run, and the new scheme thus features excellent conservation, improving on standard schemes by as much as 7 orders of magnitude.Figure 9:Fractional energy errors over time for the filamentation test case with cold initial beams. Excellent conservation is observed for the new schemes with both spatial discretizations.

A more interesting test case uses non-zerout​h=0.05u_{th}=0.05and a larger domainLx=Ly=4​πL_{x}=L_{y}=4\pi, for break-up of the “filaments” formed by the instability. In Figure10we show density snapshots from a run withNx=Ny=256N_{x}=N_{y}=256and800800particles per cell that illustrate the formation of filaments, their finite width induced by thermal effects, and their breakup in the nonlinear phase of the instability. Energy conservation for this test case with PSATD – both with standard PIC and the new energy-conserving method – are reported in Figure11, again showing roundoff-level energy accuracy achieved by the new scheme.Figure 10:Temporal snapshots of electron density in a filamentation instability test case withut​h=0.05u_{th}=0.05, showing formation and breakup of the eponymous “filaments”.Figure 11:Energy error as a function of time for the filamentation instability test case withut​h=0.05u_{th}=0.05.

## 5Conclusions

We have extended our earlier explicit, energy conserving PIC scheme[28]to apply to relativistic plasmas. We have shown that, as in the classical case, the analytic solution of a local optimization problem for each particle may be used to enforce exact energy conservation. The formulation of that optimization problem and its solution are described, as is the recovery of the non-relativistic limit. As before, the optimization is not guaranteed to admit a real solution, but we show that such issues are sufficiently rare to admit round-off level energy accuracy in many practical simulations. As in the non-relativistic case, we show that the scheme is compatible with widely used spatial discretizations for Maxwell’s equations.

Opportunities for future work are myriad, and include application to more challenging problems as well as extension to relativistic collisional plasmas, building on[35].

## Acknowledgements

The authors wish to acknowledge valuable private communication with Luis Chacón and Andrew Christlieb. This work was performed under the auspices of the U.S. Department of Energy by LLNL under contract DE-AC52-07NA27344. Both authors were supported by the DOE Office of Applied Scientific Computing Research (ASCR) Mathematical Multifaceted Integrated
Capabilities Center (MMICC) Program under grant DE-SC0023164. Additionally, the work of J. Hu was partially supported by AFOSR grant FA9550-21-1-0358.

## Appendix A

It is instructive to first rederive the fact that, if any three vectors𝐯,𝐚,𝐛∈ℝ3\mathbf{v},\mathbf{a},\mathbf{b}\in\mathbb{R}^{3}are related by𝐯=𝐚+𝐯×𝐛,\mathbf{v}=\mathbf{a}+\mathbf{v}\times\mathbf{b},(60)

one can solve for𝐯\mathbf{v}explicitly and find𝐯=𝐚+(𝐚⋅𝐛)​𝐛+𝐚×𝐛1+b2.\mathbf{v}=\frac{\mathbf{a}+(\mathbf{a}\cdot\mathbf{b})\mathbf{b}+\mathbf{a}\times\mathbf{b}}{1+b^{2}}.(61)

To see why, decompose𝐯\mathbf{v}and𝐚\mathbf{a}into components parallel and perpendicular to𝐛\mathbf{b}:𝐯=𝐯∥+𝐯⟂\mathbf{v}=\mathbf{v}_{\parallel}+\mathbf{v}_{\perp}and similar for𝐚\mathbf{a}. Trivially,𝐯∥=𝐚∥=𝐛​(𝐚⋅𝐛)/b2\mathbf{v}_{\parallel}=\mathbf{a}_{\parallel}=\mathbf{b}(\mathbf{a}\cdot\mathbf{b})/b^{2}. Crossing the perpendicular component of (60) with𝐛\mathbf{b}and noting that(𝐯⟂×𝐛)×𝐛=−b2​𝐯⟂(\mathbf{v}_{\perp}\times\mathbf{b})\times\mathbf{b}=-b^{2}\mathbf{v}_{\perp}, we have𝐯×𝐛=𝐯⟂×𝐛=𝐚×𝐛−𝐯⟂​b2.\mathbf{v}\times\mathbf{b}=\mathbf{v}_{\perp}\times\mathbf{b}=\mathbf{a}\times\mathbf{b}-\mathbf{v}_{\perp}b^{2}.(62)

Substituting this back into the perpendicular component of (60) gives𝐯⟂=𝐚⟂+𝐚×𝐛−b2​𝐯⟂⟹𝐯⟂=𝐚⟂+𝐚×𝐛1+b2.\mathbf{v}_{\perp}=\mathbf{a}_{\perp}+\mathbf{a}\times\mathbf{b}-b^{2}\mathbf{v}_{\perp}\qquad\implies\qquad\mathbf{v}_{\perp}=\frac{\mathbf{a}_{\perp}+\mathbf{a}\times\mathbf{b}}{1+b^{2}}.(63)

Combining this with our observation about the parallel component, we have𝐯=𝐚⋅𝐛b2​𝐛+𝐚−𝐚⋅𝐛b2​𝐛+𝐚×𝐛1+b2,\mathbf{v}=\frac{\mathbf{a}\cdot\mathbf{b}}{b^{2}}\mathbf{b}+\frac{\mathbf{a}-\frac{\mathbf{a}\cdot\mathbf{b}}{b^{2}}\mathbf{b}+\mathbf{a}\times\mathbf{b}}{1+b^{2}},(64)

which simplifies to (61).

Next, consider the proposed update for𝐮p∗\mathbf{u}_{p}^{*}:𝐮p∗=𝐮pn+Δ​t2​(𝐄p∗,∗+𝐮p∗γp∗×𝐁p∗,∗).\mathbf{u}_{p}^{*}=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\left(\mathbf{E}_{p}^{*,*}+\frac{\mathbf{u}_{p}^{*}}{\gamma_{p}^{*}}\times\mathbf{B}_{p}^{*,*}\right).(65)

Letting𝐚¯=𝐮pn+Δ​t2​𝐄p∗,∗\bar{\mathbf{a}}=\mathbf{u}_{p}^{n}+\frac{\Delta t}{2}\mathbf{E}_{p}^{*,*}and𝐛¯=Δ​t2​𝐁p∗,∗\bar{\mathbf{b}}=\frac{\Delta t}{2}\mathbf{B}_{p}^{*,*}, (61) implies𝐮p∗=𝐚¯+(𝐚¯⋅𝐛¯)​𝐛¯/(γp∗)2+𝐚¯×𝐛¯/γp∗1+b¯2/(γp∗)2.\mathbf{u}_{p}^{*}=\frac{\bar{\mathbf{a}}+(\bar{\mathbf{a}}\cdot\bar{\mathbf{b}})\bar{\mathbf{b}}/(\gamma_{p}^{*})^{2}+\bar{\mathbf{a}}\times\bar{\mathbf{b}}/\gamma_{p}^{*}}{1+\bar{b}^{2}/(\gamma_{p}^{*})^{2}}.(66)

Next, note that dotting (65) with𝐮p∗\mathbf{u}_{p}^{*}implies that‖𝐮p∗‖2=𝐚¯⋅𝐮p∗\|\mathbf{u}_{p}^{*}\|^{2}=\bar{\mathbf{a}}\cdot\mathbf{u}_{p}^{*}. Substituting in the expression above for𝐮p∗\mathbf{u}_{p}^{*}on the right and noting that‖𝐮p∗‖2=c2​((γp∗)2−1)\|\mathbf{u}_{p}^{*}\|^{2}=c^{2}((\gamma_{p}^{*})^{2}-1), we havec2​((γp∗)2−1)=a¯2+(𝐚¯⋅𝐛¯)2/(γp∗)21+b¯2/(γp∗)2.c^{2}\left((\gamma_{p}^{*})^{2}-1\right)=\frac{\bar{a}^{2}+(\bar{\mathbf{a}}\cdot\bar{\mathbf{b}})^{2}/(\gamma_{p}^{*})^{2}}{1+\bar{b}^{2}/(\gamma_{p}^{*})^{2}}.(67)

Multiplying through by factors ofγp∗\gamma_{p}^{*}as appropriate, we arrive at a quadratic equation for(γp∗)2(\gamma_{p}^{*})^{2}:(γp∗)4+(b¯2−1−a¯2/c2)​(γp∗)2−b¯2−(𝐚¯⋅𝐛¯)2/c2=0,\begin{split}&(\gamma_{p}^{*})^{4}+\left(\bar{b}^{2}-1-\bar{a}^{2}/c^{2}\right)(\gamma_{p}^{*})^{2}-\bar{b}^{2}-(\bar{\mathbf{a}}\cdot\bar{\mathbf{b}})^{2}/c^{2}=0,\end{split}(68)

whose (positive) solution is(γp∗)2=12​(γ2​(𝐚¯)−b¯2+(γ2​(𝐚¯)−b¯2)2+4​(b¯2+(𝐚¯⋅𝐛¯)2/c2)),(\gamma_{p}^{*})^{2}=\frac{1}{2}\left(\gamma^{2}(\bar{\mathbf{a}})-\bar{b}^{2}+\sqrt{\left(\gamma^{2}(\bar{\mathbf{a}})-\bar{b}^{2}\right)^{2}+4\left(\bar{b}^{2}+(\bar{\mathbf{a}}\cdot\bar{\mathbf{b}})^{2}/c^{2}\right)}\right),(69)

whereγ2​(𝐚¯):=1+a¯2/c2\gamma^{2}(\bar{\mathbf{a}}):=1+\bar{a}^{2}/c^{2}.
The positive square root of this expression completely specifiesγp∗\gamma_{p}^{*}in terms of known quantities.

Knowingγp∗\gamma_{p}^{*}, (66) now completely specifies𝐮p∗\mathbf{u}_{p}^{*}in terms of known quantities.

## Appendix B

As one may expect, the key to understanding the scaling ofΓ\Gammain (44) is to understand the scaling ofδ\delta, defined in (43). The second term in the dot product that definesδ\deltais manifestly𝒪​(Δ​t)\mathcal{O}(\Delta t), so we concern ourselves primarily with the first. We begin by noticing that𝐯∗−𝐮†+𝐮nγ†+γn=𝐮∗γ∗−𝐮†+𝐮nγ†+γn=2​γ†+γn2​𝐮∗−γ∗​𝐮†+𝐮n2γ∗​(γ†+γn)=2γ∗​(γ†+γn)​[𝐮∗​(γ†+γn2−γ∗)+γ∗​(𝐮∗−𝐮†+𝐮n2)].\begin{split}\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}&=\frac{\mathbf{u}^{*}}{\gamma^{*}}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\\
&=2\frac{\frac{\gamma^{\dagger}+\gamma^{n}}{2}\mathbf{u}^{*}-\gamma^{*}\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{2}}{\gamma^{*}\left(\gamma^{\dagger}+\gamma^{n}\right)}\\
&=\frac{2}{\gamma^{*}\left(\gamma^{\dagger}+\gamma^{n}\right)}\left[\mathbf{u}^{*}\left(\frac{\gamma^{\dagger}+\gamma^{n}}{2}-\gamma^{*}\right)+\gamma^{*}\left(\mathbf{u}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{2}\right)\right].\end{split}(70)

By precisely the same logic used in[28], the difference of velocities in the last line is𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right). Indeed, directly substituting in the definition of the (proper) velocity update gives𝐮∗−𝐮†+𝐮n2=Δ​t2​(𝐄∗,∗−𝐄n+1/2+𝐯∗×(𝐁∗,∗−𝐁n+1/2)).\mathbf{u}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{2}=\frac{\Delta t}{2}\left(\mathbf{E}^{*,*}-\mathbf{E}^{n+1/2}+\mathbf{v}^{*}\times\left(\mathbf{B}^{*,*}-\mathbf{B}^{n+1/2}\right)\right).(71)

The differences of fields are specifically constructed to be𝒪​(Δ​t2)\mathcal{O}\left(\Delta t^{2}\right)– see[28]for the full derivation.

We next analyze the difference ofγ\gamma’s. Taylor expansion to second order and diligent but straightforward algebraic manipulation tells us that1+|𝐮+𝐚|2c2=γ​(𝐮)+𝐚⋅𝐮/c2γ​(u)+12​γ​(u)​c2​(‖𝐚‖2−(𝐚⋅𝐯)2c2)+𝒪​(a3),\sqrt{1+\frac{|\mathbf{u}+\mathbf{a}|^{2}}{c^{2}}}=\gamma(\mathbf{u})+\frac{\mathbf{a}\cdot\mathbf{u}/c^{2}}{\gamma(u)}+\frac{1}{2\gamma(u)c^{2}}\left(\|\mathbf{a}\|^{2}-\frac{(\mathbf{a}\cdot\mathbf{v})^{2}}{c^{2}}\right)+\mathcal{O}\left(a^{3}\right),(72)

for arbitrary vectors𝐚\mathbf{a}and𝐮\mathbf{u}. Here,γ​(𝐮)\gamma(\mathbf{u})is simply the Lorentz factor evaluated at𝐮\mathbf{u}, and𝐯=𝐮/γ​(𝐮)\mathbf{v}=\mathbf{u}/\gamma(\mathbf{u}). Applying this formula to Taylor expand bothγ†\gamma^{\dagger}andγn\gamma^{n}about𝐮∗\mathbf{u}^{*}, we find thatγ†+γn2−γ∗=𝐮∗c2​γ∗⋅[𝐮†+𝐮n2−𝐮∗]+12​γ∗​c2​∑r=n,†{‖𝐮r−𝐮∗‖2−((𝐮r−𝐮∗)⋅𝐯∗)2c2}+𝒪​(Δ​t3).\begin{split}\frac{\gamma^{\dagger}+\gamma^{n}}{2}-\gamma^{*}&=\frac{\mathbf{u}^{*}}{c^{2}\gamma^{*}}\cdot\left[\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{2}-\mathbf{u}^{*}\right]\\
&\quad+\frac{1}{2\gamma^{*}c^{2}}\sum_{r=n,\dagger}\left\{\left\|\mathbf{u}^{r}-\mathbf{u}^{*}\right\|^{2}-\frac{((\mathbf{u}^{r}-\mathbf{u}^{*})\cdot\mathbf{v}^{*})^{2}}{c^{2}}\right\}\\
&\quad+\mathcal{O}\left(\Delta t^{3}\right).\end{split}(73)

The term in the first line is𝒪​(Δ​t3)\mathcal{O}(\Delta t^{3}), since it features the same difference of velocities that was considered above. The second line is manifestly𝒪​(Δ​t2)\mathcal{O}\left(\Delta t^{2}\right)and does not vanish. Overall, we thus have𝐯∗−𝐮†+𝐮nγ†+γn=𝒪​(Δ​t2),\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}=\mathcal{O}\left(\Delta t^{2}\right),(74)

with the leading order termonlycoming from a difference of Lorentz factors. It follows immediately thatδ=𝒪​(Δ​t3)\delta=\mathcal{O}\left(\Delta t^{3}\right)and thatΓ=1+𝒪​(Δ​t3)\Gamma=1+\mathcal{O}\left(\Delta t^{3}\right).

## Appendix C

It is somewhat disappointing that theΓ=1+𝒪​(Δ​t4)\Gamma=1+\mathcal{O}\left(\Delta t^{4}\right)result has not carried over from the non-relativistic to the relativistic case in the scheme presented above. The reason, as discussed further in Appendix B, comes down to the distinction between midpoint and trapezoidal evaluation ofγ\gamma. The use of Higuera-Cary’s midpoint-based choice ofγ¯p\bar{\gamma}_{p}to define𝐯p∗\mathbf{v}_{p}^{*}, which appears in the definition of current density, conflicts with the trapezoidal evaluation ofγ\gamma– namely, at𝐮†\mathbf{u}^{\dagger}and𝐮n\mathbf{u}^{n}– that is inherent in the energy conservation constraint.

One is thus motivated to wonder whether replacing our update of𝐮p∗\mathbf{u}_{p}^{*}with a different choice of the parameter𝐯¯p\bar{\mathbf{v}}_{p}appearing in (15), can lead to a scheme withΓ=1+𝒪​(Δ​t4)\Gamma=1+\mathcal{O}\left(\Delta t^{4}\right). It turns out this can be done. To see this, consider the modified particle update𝐱p∗=𝐱pn+Δ​t2​𝐮pnγpn,𝐮p∗∗=𝐮pn+Δ​t​(𝐄p∗,∗+(𝐮p∗∗+𝐮pnγ∗∗+γpn+)⏟≔𝐯p∗×𝐁p∗,∗),𝐮p∗=12​(𝐮pn+𝐮p∗∗)𝐱pn+1=𝐱pn+Δ​t​𝐯p∗,𝐮p†=𝐮pn+Δ​t​(𝐄pn+1/2+𝐯p∗×𝐁pn+1/2),𝐮pn+1=Gr​(𝐮pn,𝐮p∗,𝐮p†).\begin{split}\mathbf{x}_{p}^{*}&=\mathbf{x}_{p}^{n}+\frac{\Delta t}{2}\frac{\mathbf{u}_{p}^{n}}{\gamma_{p}^{n}},\\
\mathbf{u}_{p}^{**}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}_{p}^{*,*}+\underbrace{\left(\frac{\mathbf{u}_{p}^{**}+\mathbf{u}_{p}^{n}}{\gamma^{**}+\gamma_{p}^{n}}+\right)}_{\coloneqq\mathbf{v}_{p}^{*}}\times\mathbf{B}_{p}^{*,*}\right),\\
\mathbf{u}_{p}^{*}&=\frac{1}{2}\left(\mathbf{u}_{p}^{n}+\mathbf{u}_{p}^{**}\right)\\
\mathbf{x}_{p}^{n+1}&=\mathbf{x}_{p}^{n}+\Delta t\mathbf{v}_{p}^{*},\\
\mathbf{u}_{p}^{\dagger}&=\mathbf{u}_{p}^{n}+\Delta t\left(\mathbf{E}_{p}^{n+1/2}+\mathbf{v}_{p}^{*}\times\mathbf{B}_{p}^{n+1/2}\right),\\
\mathbf{u}_{p}^{n+1}&=G^{r}(\mathbf{u}_{p}^{n},\mathbf{u}_{p}^{*},\mathbf{u}_{p}^{\dagger}).\end{split}(75)

In this version, the definition of𝐯p∗\mathbf{v}_{p}^{*}introduced in the second line is the same quantity used when computing the current density𝐣h∗,n+1/2\mathbf{j}_{h}^{*,n+1/2}. In this way, the optimization problem (34) that definesGrG^{r}is unchanged, since (35) is unmodified.

As a result, the expression forΓ\Gammain (43) – (44) also carries through unchanged. It only remains to carry out an analysis of the size ofδ\delta. With this definition of𝐯p∗\mathbf{v}_{p}^{*}, one has𝐯∗−𝐮†+𝐮nγ†+γn=𝐮∗∗+𝐮nγ∗∗+γn−𝐮†+𝐮nγ†+γn=(𝐮∗∗+𝐮n)−(𝐮†+𝐮n)γ∗∗+γn+(𝐮†+𝐮n)​(1γ∗∗+γn−1γ†+γn)=𝐮∗∗−𝐮†γ∗∗+γn+𝐮†+𝐮n(γ∗∗+γn)​(γ†+γn)​(γ†−γ∗∗).\begin{split}\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}&=\frac{\mathbf{u}^{**}+\mathbf{u}^{n}}{\gamma^{**}+\gamma^{n}}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\\
&=\frac{(\mathbf{u}^{**}+\mathbf{u}^{n})-(\mathbf{u}^{\dagger}+\mathbf{u}^{n})}{\gamma^{**}+\gamma^{n}}+(\mathbf{u}^{\dagger}+\mathbf{u}^{n})\left(\frac{1}{\gamma^{**}+\gamma^{n}}-\frac{1}{\gamma^{\dagger}+\gamma^{n}}\right)\\
&=\frac{\mathbf{u}^{**}-\mathbf{u}^{\dagger}}{\gamma^{**}+\gamma^{n}}+\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\left(\gamma^{**}+\gamma^{n}\right)\left(\gamma^{\dagger}+\gamma^{n}\right)}\left(\gamma^{\dagger}-\gamma^{**}\right).\end{split}(76)

Trivially,|γ†−γ∗∗|=𝒪​(‖𝐮†−𝐮∗∗‖)|\gamma^{\dagger}-\gamma^{**}|=\mathcal{O}\left(\left\|\mathbf{u}^{\dagger}-\mathbf{u}^{**}\right\|\right), sinceγ\gammais a Lipschitz function of𝐮\mathbf{u}. Thus, for this version of the scheme we have‖𝐯∗−𝐮†+𝐮nγ†+γn‖=𝒪​(‖𝐮∗∗−𝐮†‖).\left\|\mathbf{v}^{*}-\frac{\mathbf{u}^{\dagger}+\mathbf{u}^{n}}{\gamma^{\dagger}+\gamma^{n}}\right\|=\mathcal{O}\left(\left\|\mathbf{u}^{**}-\mathbf{u}^{\dagger}\right\|\right).(77)

By construction,‖𝐮∗∗−𝐮†‖=𝒪​(Δ​t3)\left\|\mathbf{u}^{**}-\mathbf{u}^{\dagger}\right\|=\mathcal{O}\left(\Delta t^{3}\right), so we haveδ=𝒪​(Δ​t4)\delta=\mathcal{O}\left(\Delta t^{4}\right). Indeed,𝐮∗∗−𝐮†=Δ​t​(𝐄∗,∗−𝐄n+1/2+𝐯∗×(𝐁∗,∗−𝐁n+1/2)).\mathbf{u}^{**}-\mathbf{u}^{\dagger}=\Delta t\left(\mathbf{E}^{*,*}-\mathbf{E}^{n+1/2}+\mathbf{v}^{*}\times\left(\mathbf{B}^{*,*}-\mathbf{B}^{n+1/2}\right)\right).(78)

As in Appendix B and[28], the differences of fields are constructed specifically to be𝒪​(Δ​t2)\mathcal{O}\left(\Delta t^{2}\right), making the entire right side is trivially𝒪​(Δ​t3)\mathcal{O}\left(\Delta t^{3}\right). This implies thatΓ=1+𝒪​(Δ​t4)\Gamma=1+\mathcal{O}\left(\Delta t^{4}\right)by following the logic in Appendix B.

## References
- [1]W. J. Arrighi, J. W. Banks, R. Berger, T. Chapman, A. G. Odu, and J. Gorman(2024)A new approach to the evaluation and solution of the relativistic kinetic dispersion relation and verification with continuum kinetic simulation.Journal of Computational Physics508,pp. 113001.Cited by:§4.2,§4.2,§4.2,§4.2.
- [2]S. Atzeni, A. Schiavi, F. Califano, F. Cattani, F. Cornolti, D. Del Sarto, T. Liseykina, A. Macchi, and F. Pegoraro(2005)Fluid and kinetic simulation of inertial confinement fusion plasmas.Computer physics communications169(1-3),pp. 153–159.Cited by:§1.
- [3]F. Bacchini, J. Amaya, and G. Lapenta(2019)The relativistic implicit particle-in-cell method.InJournal of Physics: Conference Series,Vol.1225,pp. 012011.Cited by:§1,§2.3.
- [4]D. C. Barnes and L. Chacón(2021)Finite spatial-grid effects in energy-conserving particle-in-cell algorithms.Computer Physics Communications258,pp. 107560.Cited by:§1,§1.
- [5]C. K. Birdsall and A. B. Langdon(2018)Plasma physics via computer simulation.CRC press.Cited by:§1,§1,§2.4.
- [6]G. Blaclard, H. Vincenti, R. Lehe, and J. Vay(2017)Pseudospectral maxwell solvers for an accurate modeling of doppler harmonic generation on plasma mirrors with particle-in-cell codes.Physical Review E96(3),pp. 033305.Cited by:§2.4.
- [7]J. P. Boriset al.(1970)Relativistic plasma simulation-optimization of a hybrid code.InProc. Fourth Conf. Num. Sim. Plasmas,pp. 3–67.Cited by:§2.3.
- [8]B. N. Breizman, P. Aleynikov, E. M. Hollmann, and M. Lehnen(2019)Physics of runaway electrons in tokamaks.Nuclear Fusion59(8),pp. 083001.Cited by:§1.
- [9]A. Bret, L. Gremillet, and M. E. Dieckmann(2010)Multidimensional electron beam-plasma instabilities in the relativistic regime.Physics of Plasmas17(12).Cited by:§4.4,§4.4.
- [10]L. Chacón and G. Chen(2016)A curvilinear, fully implicit, conservative electromagnetic pic algorithm in multiple dimensions.Journal of computational physics316,pp. 578–597.Cited by:§1.
- [11]G. Chen, L. Chacón, and D. C. Barnes(2011)An energy-and charge-conserving, implicit, electrostatic particle-in-cell algorithm.Journal of Computational Physics230(18),pp. 7018–7036.Cited by:§1,§3.
- [12]G. Chen, L. Chacon, L. Yin, B. J. Albright, D. J. Stark, and R. F. Bird(2020)A semi-implicit, energy-and charge-conserving particle-in-cell algorithm for the relativistic vlasov-maxwell equations.Journal of Computational Physics407,pp. 109228.Cited by:§1,§1,§1,§2.3,§2.5,§3,§4.1.
- [13]G. Chen and L. Chacon(2015)A multi-dimensional, energy-and charge-conserving, nonlinearly implicit, electromagnetic vlasov–darwin particle-in-cell algorithm.Computer Physics Communications197,pp. 73–87.Cited by:§1.
- [14]Y. Cheng, A. J. Christlieb, and X. Zhong(2014)Energy-conserving discontinuous galerkin methods for the vlasov–maxwell system.Journal of Computational Physics279,pp. 145–173.Cited by:§4.3,§4.3,§4.3.
- [15]B. M. Cowan, D. L. Bruhwiler, J. R. Cary, E. Cormier-Michel, and C. G. Geddes(2013)Generalized algorithm for control of numerical dispersion in explicit time-domain electromagnetic simulations.Physical Review Special Topics—Accelerators and Beams16(4),pp. 041303.Cited by:§2.4.
- [16]S. D. Gedney(2011)Yee algorithm for maxwell’s equations.InIntroduction to the Finite-Difference Time-Domain (FDTD) Method for Electromagnetics,pp. 39–73.Cited by:§2.4.
- [17]A. Gonoskov(2024)Explicit energy-conserving modification of relativistic pic method.Journal of Computational Physics502,pp. 112820.Cited by:§1,§1,§1.
- [18]E. Hairer and C. Lubich(2018)Energy behaviour of the Boris method for charged-particle dynamics.BIT Numer. Math.58,pp. 969–979.Cited by:§2.3.
- [19]A. V. Higuera and J. R. Cary(2017)Structure-preserving second-order integration of relativistic charged particle trajectories in electromagnetic fields.Physics of Plasmas24(5).Cited by:§2.3.
- [20]L. Ji, Z. Yang, Z. Li, D. Wu, S. Jin, and Z. Xu(2023)An asymptotic-preserving and energy-conserving particle-in-cell method for vlasov–maxwell equations.Journal of Mathematical Physics64(6).Cited by:§1.
- [21]G. Lapenta(2017)Exactly energy conserving semi-implicit particle in cell formulation.Journal of Computational Physics334,pp. 349–366.Cited by:§1.
- [22]R. Lehé, J. Vay,et al.(2018)Review of spectral maxwell solvers for electromagnetic particle-in-cell: algorithms and advantages.InProceedings of the 13th International Computational Accelerator Physics Conference, Key West, FL, USA,pp. 20–24.Cited by:§1.
- [23]S. Markidis and G. Lapenta(2011)The energy conserving particle-in-cell method.Journal of Computational Physics230(18),pp. 7037–7052.Cited by:§1.
- [24]K. Nishikawa, I. Duţan, C. Köhn, and Y. Mizuno(2021)PIC methods in astrophysics: simulations of relativistic jets and kinetic physics in astrophysical systems.Living Reviews in Computational Astrophysics7(1),pp. 1.Cited by:§1.
- [25]P. G. Petropoulos(1994)Phase error control for fd-td methods of second and fourth order accuracy.IEEE transactions on antennas and propagation42(6),pp. 859–862.Cited by:§2.4.
- [26]H. Qin, S. Zhang, J. Xiao, J. Liu, Y. Sun, and W. M. Tang(2013)Why is boris algorithm so good?.Physics of Plasmas20(8).Cited by:§2.3.
- [27]L. F. Ricketson and G. Chen(2023)A pseudospectral implicit particle-in-cell method with exact energy and charge conservation.Computer Physics Communications,pp. 108811.Cited by:§3.
- [28]L. F. Ricketson and J. Hu(2025)An explicit, energy-conserving particle-in-cell scheme.Journal of Computational Physics537,pp. 114098.Cited by:Appendix B,Appendix B,Appendix C,§1,§1,§1,§2.4,§2.5,§2.5,§2.5,§2.5,§3.1,§3.1,§3.3,§3,§3,§4,§5.
- [29]H. Schmitz(2026)An overview of relativistic particle pushers and their extension to arbitrary order accuracy.arXiv preprint arXiv:2603.06509.Cited by:§2.3.
- [30]J. B. Schneider and R. J. Kruhlak(2001)Dispersion of homogeneous and inhomogeneous waves in the yee finite-difference time-domain grid.IEEE transactions on microwave theory and techniques49(2),pp. 280–287.Cited by:§2.4.
- [31]O. Shapoval, R. Lehe, M. Thévenet, E. Zoni, Y. Zhao, and J. Vay(2021)Overcoming timestep limitations in boosted-frame particle-in-cell simulations of plasma-based acceleration.Physical Review E104(5),pp. 055311.Cited by:§2.5.
- [32]J. Vay(2008)Simulation of beams or plasmas crossing at relativistic velocity.Physics of Plasmas15(5).Cited by:§2.3.
- [33]J. Vay, I. Haber, and B. B. Godfrey(2013)A domain decomposition method for pseudo-spectral electromagnetic simulations of plasmas.Journal of Computational Physics243,pp. 260–268.Cited by:§1,§2.4.
- [34]K. Yee(1966)Numerical solution of initial boundary value problems involving Maxwell’s equations in istropic media.IEEE Trans. Antennas Propag.14,pp. 302–307.Cited by:§1,§2.4,§2.4.
- [35]J. Yoo, J. Hu, and L. F. Ricketson(2025)An explicit energy-conserving particle method for the Vlasov-Fokker-Planck equation.arXiv preprint arXiv:2510.03960.Cited by:§5.

## 


- 


Major funding support from
