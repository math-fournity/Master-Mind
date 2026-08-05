# Why a mid-depth stress-free boundary condition is incorrect for Ekman flows

**arXiv ID**: 2607.29261v1
**Authors**: Christian Puntini, Luigi Roberti
**Published**: 2026-07-31
**Categories**: physics.flu-dyn, math-ph, math.AP, physics.ao-ph
**Comments**: 6 pages, 4 figures
**HTML URL**: https://arxiv.org/html/2607.29261v1

## Abstract

We show that the assumption of a stress-free boundary condition at a finite intermediate depth, namely, at the bottom of the Ekman layer, in the analysis of wind-driven ocean flows necessarily leads to an unphysical current profile. Indeed, if the $z$-derivative of the fluid velocity vanishes at a given depth, then this depth necessarily corresponds to a minimum of the velocity profile, with the velocity increasing beneath it. Using a WKB ansatz based on the small variations of the ocean's water density at great depths, we also argue that a no-slip condition at the bottom of the ocean, if sufficiently deep, still effectively implies (up to a very small error) the orthogonality of the Ekman transport and the wind-stress.

## Full Text

Why a mid-depth stress-free boundary condition is incorrect for Ekman flows

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2607.29261v1 [physics.flu-dyn] 31 Jul 2026

## Why a mid-depth stress-free boundary condition is incorrect for Ekman flowsChristian Puntinichristian.puntini@univie.ac.atFaculty of Mathematics, University of Vienna, Oskar–Morgenstern–Platz 1, 1090 Vienna, AustriaLuigi Robertiroberti@ifam.uni-hannover.deInstitut für Angewandte Mathematik, Leibniz Universität Hannover, Welfengarten 1, 30167 Hannover, Germany

## Abstract

We show that the assumption of a stress-free boundary condition at a finite intermediate depth, namely, at the bottom of the Ekman layer, in the analysis of wind-driven ocean flows necessarily leads to an unphysical current profile. Indeed, if thezz-derivative of the fluid velocity vanishes at a given depth, then this depth necessarily corresponds to a minimum of the velocity profile, with the velocity increasing beneath it. Using a WKB ansatz based on the small variations of the ocean’s water density at great depths, we also argue that a no-slip condition at the bottom of the ocean, if sufficiently deep, still effectively implies (up to a very small error) the orthogonality of the Ekman transport and the wind-stress.

## IIntroduction and governing equations

The study of wind-driven processes at the ocean surface is a classic topic in physical oceanography, with important implications for the ocean circulation and, consequently, Earth’s climate[11,21,19]. Its origins can be traced back to the pioneering work of Ekman[4], who, in 1905, was the first to provide a theoretical description of wind-driven surface currents. His analysis was motivated by the observations made by F. Nansen during the 1893–1896 Arctic expedition aboard theFramvessel, which revealed that sea ice drifts at an angle to the right of the prevailing wind direction. Ekman’s explicit solution (see[6]for a concise overview of Ekman’s work) applies to the idealised setting of a homogeneous ocean forced by a steady, spatially uniform wind and characterised by a constant vertical eddy viscosity. The interplay between the Coriolis force and the frictional force induced by the wind stress gives rise to the characteristic dynamics of the Ekman currents. The resulting solution exhibits the following key features (see Fig.1):
- •

the surface current is directed at an angle of45∘45^{\circ}to the wind, to the right in the Northern Hemisphere and to the left in the Southern Hemisphere;
- •

as the depth increases, the current velocity gradually decreases while its direction rotates progressively away from the wind, giving rise to the characteristicEkman spiral;
- •

the depth-integrated wind-driven transport, known as theEkman transport, is directed at a right angle to the wind, to the right in the Northern Hemisphere and to the left in the Southern Hemisphere.Figure 1:Schematic representation of the classical Ekman flow: the surface current is deflected by45∘45^{\circ}relative to the wind direction, and progressively deeper layers exhibit decreasing deflection and velocity. The vertically integrated, wind-driven water transport is directed at right angles to the wind. Credit: NOAA.

However, field observations show that the surface deflection angle is far from constant, typically ranging from10∘10^{\circ}to80∘80^{\circ}(see[14,16]and the references therein), in contrast to the fixed45∘45^{\circ}predicted by the classical Ekman model. Although it can be proven that the qualitative features of Ekman dynamics persist even when both the water density and the eddy viscosity vary with depth (see[2,14]), the observed variability of the deflection angle is widely attributed to the vertical structure of the eddy viscosity. In fact,[14]shows that the surface deflection angle is highly sensitive to this structure: different viscosity profiles can produce markedly different departures of the surface current from the wind direction.
Nevertheless, experimental results provide evidence that the Ekman transport is effectively (up to some errors) at a right angle to the blowing wind (see, e.g.,[1,13]).

From a theoretical point of view, wind-driven flows are governed by a set of differential equations derived asymptotically from the Navier–Stokes equations, together with a surface boundary condition (coupling the wind and the ocean stresses) and a bottom boundary condition. The Ekman layer is effectively the oceanic boundary layer generated by the transfer of momentum from the wind to the ocean; therefore, it is reasonable to impose the continuity of the stress at the ocean surface. The present letter instead aims to analyse the bottom boundary condition for Ekman flows. Before proceeding further, let us briefly recall the governing equations of Ekman dynamics.

## I.1The governing equations of Ekman-type flows

We define a local Cartesian coordinate system(x,y,z)(x,y,z)with orthonormal basis vectors(𝐞x,𝐞y,𝐞z)(\mathbf{e}_{x},\mathbf{e}_{y},\mathbf{e}_{z}). The frame is centred at a point on the spherical surface (excluding the poles, where the horizontal basis vectors are ill-defined) and rotates rigidly with the sphere at the angular velocityΩ≈7.29⋅10−5​s−1\Omega\approx 7.29\,\cdot\,10^{-5}\,\rm{s^{-1}}about the polar axis (see Fig.2). The velocity components in this frame are denoted by(u,v,w)(u,v,w).Figure 2:The Cartesian coordinate system associated with the rotating Earth. The position vectorrrspecifies the location of a pointPPwith latitudeθ\thetaand longitudeφ\varphi. whileZZdenotes Null Island (coordinates0∘​N,0∘​E0^{\circ}\,\rm{N},0^{\circ}\,\rm{E}).

The common practice in the study of Ekman flows is to consider the equations of motion in the so-calledff-plane approximation, that is, considering a relatively small region of the ocean under consideration to be approximated by a tangent plane and keeping the Coriolis parameterf=2​Ω​sin⁡θf=2\Omega\sin\thetafixed. Moreover, in the analysis of wind-driven currents, it is common to assume that the surface of the ocean is flat (this is a consequence of the fact that vertical motion is weaker than the horizontal one and can be justified via asymptotics, see e.g.[15]) and the atmospheric pressurepatmp_{\rm atm}at the surface constant. This implies that the geostrophic components of the horizontal velocity field vanish, so the momentum equations reduce to(m​(z)​u′​(z))′=−f​ρ​(z)​v​(z)(m​(z)​v′​(z))′=f​ρ​(z)​u​(z)}for−H<z<0\left.\begin{aligned} (m(z)u^{\prime}(z))^{\prime}&=-f\rho(z)v(z)\\
(m(z)v^{\prime}(z))^{\prime}&=f\rho(z)u(z)\end{aligned}\right\}\qquad\text{for $-H<z<0$}(1)

(see, e.g.,[2,16,23]), where we denote azz-derivative by a prime. In the system (1),mmis the dynamic (vertical) eddy viscosity andρ\rhois the density of the fluid, both assumed to be depth-dependent. Givenuuandvv, the vertical velocitywwis obtained by integrating the incompressibility condition∂u∂x+∂v∂y+∂w∂z=0,\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=0,(2)

resulting from the fact that, even if we are assuming that the water’s density is depth dependent, water is only weakly compressible. For example, at a depth of approximately1500​m1500\,\rm{m}, where the hydrostatic pressure reaches about150150times the atmospheric pressure, water compresses by less than1%1\%, implying only a very small increase in density. Finally, the pressure is given byp​(z)=patm+g​∫z0ρ​(s)​ds.p(z)=p_{\rm atm}+g\int^{0}_{z}\rho(s)\,\mathrm{d}s.(3)

On the flat surfacez=0z=0, the water’s shear stress matches the wind stress(τx,τy)\bigl(\tau_{x},\tau_{y}\bigr):m​(0)​(u′​(0),v′​(0))=(τx,τy).m(0)\bigl(u^{\prime}(0),\,v^{\prime}(0)\bigr)=\bigl(\tau_{x},\tau_{y}\bigr).(4)

Note that, in general,(τx,τy)\bigl(\tau_{x},\tau_{y}\bigr)is a function of the wind speed and the surface current(u​(0),v​(0))(u(0),v(0))and may be given by a (possibly nonlinear) bulk formula, such as in[20], but its precise form will not be important for us in this work.

An importantcaveat, which we note here only as a side remark, is that in fact the formulation of the stress in the water, namely, the left-hand side of (4), is debatable, in the sense that the definition of an eddy viscosity at the surface is not completely formally correct; for a detailed discussion of this fact, we refer the interested reader to[14]. Here, we simply fix the boundary condition on the surface in the form (4), which is the most common one in physical oceanography[2,16,15,21,22]; the precise choice of this condition is, in fact, irrelevant to our subsequent discussion. Indeed, the subject of this paper is not the boundary condition on the surface but rather the one to impose at a lower depth, the choice of which is often motivated by the notion ofEkman transport.

The Ekman transport, in the case of variable density, is defined asME\displaystyle\mathrm{M_{E}}=∫−H0ρ​(z)​(u​(z),v​(z))​dz\displaystyle=\int^{0}_{-H}\rho(z)\bigl(u(z),\,v(z)\bigr)\,\mathrm{d}z(5)=1f​∫−H0((m​(z)​v′​(z))′,−(m​(z)​u′​(z))′)​dz\displaystyle=\dfrac{1}{f}\int^{0}_{-H}\bigl((m(z)v^{\prime}(z))^{\prime},\,-(m(z)u^{\prime}(z))^{\prime}\bigr)\,\mathrm{d}z=1f​{(τy,−τx)−m​(−H)​(v′​(−H),−u′​(−H))}.\displaystyle=\dfrac{1}{f}\left\{\bigl(\tau_{y},\,-\tau_{x}\bigr)-m(-H)\bigl(v^{\prime}(-H),\,-u^{\prime}(-H)\bigr)\right\}.

As we mentioned earlier, measurements show that the Ekman transport and the wind stress form a90∘90^{\circ}-angle[1,13]. Looking at the formula in (5), it is immediate to observe that the first term(τy,−τx)\bigl(\tau_{y},\,-\tau_{x}\bigr)is perpendicular to the wind stress vector𝝉=(τx,τy)\boldsymbol{\tau}=\bigl(\tau_{x},\,\tau_{y}\bigr),
and therefore the termm​(−H)​(v′​(−H),−u′​(−H))m(-H)\bigl(v^{\prime}(-H),\,-u^{\prime}(-H)\bigr)should be zero to satisfy the orthogonality conditionME⟂𝝉\mathrm{M_{E}}\perp\boldsymbol{\tau}. This is where the bottom boundary condition enters.

Often, the simplification of infinite depth (H=∞H=\infty) is made[6,2,16,21,15]. Since the Ekman flow should vanish at large depths, this translates to the requirementlimz→−∞(u​(z),v​(z))=(0,0);\lim_{z\to-\infty}(u(z),v(z))=(0,0);(6)

then,limz→−∞(u′​(z),v′​(z))=(0,0)\displaystyle\lim_{z\to-\infty}(u^{\prime}(z),v^{\prime}(z))=(0,0), as long as the eddy viscosity is “well behaved” at large depths (which is the case, since the eddy viscosity may be assumed to tend to the constant molecular viscosity at large depths). However, it is of course more physically realistic to consider a finite depth. Then,z=−Hz=-Hcan be viewed as the bottom of the ocean, in which case either the no-slip condition(u​(−H),v​(−H))=(0,0)(u(-H),\,v(-H))=(0,0)(7)

or the stress-free condition(u′​(−H),v′​(−H))=(0,0),(u^{\prime}(-H),\,v^{\prime}(-H))=(0,0),(8)

may be imposed; see, e.g.,[18,5,3]. The condition (8) ensures the orthogonality conditionME⟂𝝉\mathrm{M_{E}}\perp\boldsymbol{\tau}, but, except in the trivial case of zero wind, implies that the current is not zero at the bottom of the ocean; on the other hand, (7) imposes no motion on the ocean’s bed, which is more physically realistic, but has the drawback that, in (5), the Ekman transport is only approximately—though, usually, very nearly—perpendicular to the wind stress (cf. the discussion at the end of the paper). Finally, in several instances (such as[10,12,9]), the depth of the Ekman layer is takena priorito be a value−D∈(−H,0)-D\in(-H,0), thus an intermediate value between the ocean’s bed and the free surface. In this case, a stress-free condition at−D-Danalogous to (7), namely(u′​(−D),v′​(−D))=(0,0),(u^{\prime}(-D),\,v^{\prime}(-D))=(0,0),(9)

is the norm, and in order to match the orthogonality conditionME⟂𝝉\mathrm{M_{E}}\perp\boldsymbol{\tau}, the flow is assumed to be negligible forz<−Dz<-D.

The goal of this paper is to show how the case (9) inevitably leads to inconsistency: in fact, with this assumption, the Ekman flow, which is always implicitly assumed to be negligible below the depthz=−Dz=-D, in fact increases below this depth, essentially describing a “reverse Ekman spiral”.

## IIMain result

Let−H<−D<0-H<-D<0, where−H-His the ocean’s depth and−D-Dan intermediate depth (usually the bottom of the Ekman layer). It is convenient to reformulate the problem in terms of the complex notationU=u+i​v,𝝉=τx+i​τy;U=u+\mathrm{i}v,\qquad\bm{\tau}=\tau_{x}+\mathrm{i}\tau_{y};(10)

with this notation, we can write (1) , (4) and (9) as:{(m​(z)​U′​(z))′=i​f​ρ​(z)​U​(z),z∈(−H,0),m​(0)​U′​(0)=𝝉,U′​(−D)=0.\left\{\begin{aligned} &(m(z)U^{\prime}(z))^{\prime}=\mathrm{i}f\rho(z)U(z),\quad z\in(-H,0),\\
&m(0)U^{\prime}(0)=\bm{\tau},\\
&U^{\prime}(-D)=0.\end{aligned}\right.(11)

## Theorem 1.

Let−H<−D<0-H<-D<0and suppose thatUUsatisfies (11). Then|U||U|decreases with depth untilz=−Dz=-D, where it reaches its minimum, and increases again with depth belowz=−Dz=-D. Similarly, in the northern hemisphere (f>0f>0), the angle between𝛕\bm{\tau}andU​(z)U(z)increases with depth untilz=−Dz=-D, reaches a maximum there, and subsequently decreases for greater depths.

## Proof.

We argue along the lines of the proof of Theorem 1 in[14]. We multiply the first equation in (11) byU​(z)¯\overline{U(z)}, integrate from−D-Dtoz∈[−H,0]z\in[-H,0], and perform an integration by parts; this yieldsm​(z)​U′​(z)​U​(z)¯\displaystyle m(z)U^{\prime}(z)\overline{U(z)}=∫−Dzm​(s)​|U′​(s)|2​ds\displaystyle=\int_{-D}^{z}m(s)|U^{\prime}(s)|^{2}\,\mathrm{d}s(12)+i​f​∫−Dzρ​(s)​|U​(s)|2​ds.\displaystyle\quad+\mathrm{i}f\int_{-D}^{z}\rho(s)|U(s)|^{2}\,\mathrm{d}s.

WritingU​(z)U(z)in the exponential formU​(z)=r​(z)​ei​ϕ​(z),U(z)=r(z)\operatorname{e}^{\mathrm{i}\phi(z)},(13)

wherer​(z)=|U​(z)|r(z)=|U(z)|andϕ​(z)=arg​(U​(z))\phi(z)={\rm arg}(U(z)), plugging into (12), and comparing the real and imaginary parts of the two sides, we obtainm​(z)​r′​(z)​r​(z)=∫−Dzm​(s)​|U′​(s)|2​dsm(z)r^{\prime}(z)r(z)=\int_{-D}^{z}m(s)|U^{\prime}(s)|^{2}\,\mathrm{d}s(14)

andm​(z)​ϕ′​(z)​r​(z)2=f​∫−Dzρ​(s)​|U​(s)|2​ds.m(z)\phi^{\prime}(z)r(z)^{2}=f\int_{-D}^{z}\rho(s)|U(s)|^{2}\,\mathrm{d}s.(15)

From (14), it followsr′​(z)​{>0ifz∈(−D,0],=0ifz=−D,<0ifz∈[−H,−D),r^{\prime}(z)\,\begin{cases}>0&\text{if $z\in(-D,0]$},\\[1.99997pt]
=0&\text{if $z=-D$},\\[1.99997pt]
<0&\text{if $z\in[-H,-D)$},\end{cases}(16)

whereas (15) impliessign⁡(f)​ϕ′​(z)​{>0ifz∈(−D,0],=0ifz=−D,<0ifz∈[−H,−D).\operatorname{sign}(f)\phi^{\prime}(z)\,\begin{cases}>0&\text{if $z\in(-D,0]$},\\[1.99997pt]
=0&\text{if $z=-D$},\\[1.99997pt]
<0&\text{if $z\in[-H,-D)$}.\end{cases}(17)

This gives the claim.
∎

See Fig.3for a sketch of the behaviour of the solution to (11).Figure 3:An illustration of the behaviour of the “reverse Ekman spiral” from Theorem1. Here, for simplicity,m​(z)≡m=const.m(z)\equiv m={\rm const.},f>0f>0,𝝉=(τ,0)\bm{\tau}=(\tau,0)forτ>0\tau>0, and the vertical variablezzand the horizontal velocity components are scaled with respect tof/2\sqrt{f/2}andτ/(m​f)\tau/(m\sqrt{f}), respectively. The red arrow denotes the direction of the wind. The derivative ofU=u+i​vU=u+\mathrm{i}vvanishes forz=−5​f/2z=-5\sqrt{f/2}.

## IIIConclusion

In this work, we have analysed the bottom boundary condition for the Ekman dynamics, and we have proved that the common practice of assuminga prioria certain depth for the Ekman layer, with a stress-free boundary condition, leads to an unrealistic current profile. On the other side, also assuming the depth to be infinite is not physical, and on the mathematical side it implies the cancellation of one of the two linearly independent solutions of the second-order ODE governing the Ekman flows.

In our opinion, the correct choice is to take a finite-depth ocean with the no-slip boundary condition (7). In this scenario, the Ekman depth emerges in the parametrisation of the vertical eddy viscositym​(z)m(z). Since the eddy viscosity in this context could be thought of as the turbulent viscosity generated by the wind stress, the Ekman depth, or the bottom of the Ekman layer, can be identified as the depth below which the wind effects are negligible, and hence such eddy viscosity becomes the very small molecular viscosity. Field measurements confirm this qualitative picture: the eddy viscosity typically increases with depth up to a certain point, beyond which it decreases towards the molecular value[17]. From a theoretical standpoint, this profile is commonly reproduced through the so-called KPP (K-Profile Parametrisation) scheme[7], which prescribesm​(z)m(z)as a smooth function matching the surface boundary layer physics to the interior, and is widely adopted in ocean models for its ability to capture this non-monotonic behaviour. The resulting shape is illustrated in Fig.4.Figure 4:Depiction of a typical eddy viscosity profile according to the KPP parametrisation: it increases as depth increases, up to reaching a maximum at depth−d-d, then it decreases to a very small value (that can be thought of as the molecular viscosity) at a certain depth−D-D, below which it attains an almost constant value. As the eddy viscosity is generated by turbulent motion, which in this problem is due by the wind, the depth−D-Dcan be considered as the Ekman depth, below which wind effects are negligible. The image is not to scale.

On the other hand, since the Ekman transport isME=1f​{(τy,−τx)−m​(−H)​(v′​(−H),−u′​(−H))},\displaystyle\mathrm{M_{E}}=\dfrac{1}{f}\left\{\bigl(\tau_{y},\,-\tau_{x}\bigr)-m(-H)\bigl(v^{\prime}(-H),\,-u^{\prime}(-H)\bigr)\right\},(18)

one could argue that assuming a no-slip condition at the ocean’s bottom, i.e.u​(−H)=v​(−H)=0u(-H)=v(-H)=0, does not guarantee thatME⟂𝝉\mathrm{M_{E}}\perp\boldsymbol{\tau}. In this last part, we show that in the regimeH≫DH\gg D, the derivativeU′​(−H)U^{\prime}(-H)is very small, so that the orthogonality condition for the Ekman transport holds up to a small error. The main difficulty stems from the depth-dependence ofρ\rho, which does not allow us to find an explicit solution of the governing ODE; however, since density variations are small at great depths (see[21]), we may use the following WKB ansatz to obtain an estimate onU′​(−H)U^{\prime}(-H). Let𝔪\mathfrak{m}denote the (constant) value of the eddy viscosity below−D-D, and letUD:=u​(−D)+i​v​(−D)U_{D}:=u(-D)+\mathrm{i}\,v(-D). The governing ODE (1) then reads𝔪​U′′​(z)=i​f​ρ​(z)​U​(z),z∈(−H,−D),\mathfrak{m}\,U^{\prime\prime}(z)=\mathrm{i}f\rho(z)\,U(z),\qquad z\in(-H,-D),(19)

coupled with the boundary conditionsU​(−D)=UD(given),U​(−H)=0.U(-D)=U_{D}\quad(\text{given}),\qquad U(-H)=0.(20)

Note that, due to Theorem 1, we have that|UD|<|U​(0)||U_{D}|<|U(0)|.
Introducing the local wave-numberκ​(z)=i​f​ρ​(z)𝔪=(1+i)​μ​(z),μ​(z)=f​ρ​(z)2​𝔪>0,\kappa(z)=\sqrt{\frac{\mathrm{i}f\rho(z)}{\mathfrak{m}}}=(1+\mathrm{i})\,\mu(z),\qquad\mu(z)=\sqrt{\frac{f\rho(z)}{2\mathfrak{m}}}>0,(21)

we look for solutions of (19) of WKB formU​(z)≈κ​(z)−12​exp⁡(±∫zκ​(s)​ds).U(z)\approx\kappa(z)^{-\frac{1}{2}}\exp\!\left(\pm\int^{z}\kappa(s)\,\mathrm{d}s\right).(22)

Substituting this ansatz into (19), one finds that the terms neglected in the approximation areO​(κ′/κ2)O(\kappa^{\prime}/\kappa^{2}); the WKB approximation is therefore justified provided|κ′​(z)κ2​(z)|≪1⟺|ρ′​(z)ρ​(z)|≪|κ​(z)|,\left|\frac{\kappa^{\prime}(z)}{\kappa^{2}(z)}\right|\ll 1\qquad\Longleftrightarrow\qquad\left|\frac{\rho^{\prime}(z)}{\rho(z)}\right|\ll|\kappa(z)|,(23)

i.e. provided thatρ\rhovaries slowly compared to the local wavelength of oscillation—a condition that, as noted above, is satisfied at great depths. With this in hand, we setI​(z)=∫−Hzκ​(s)​dsandJ=∫−H−Dκ​(s)​ds=I​(−D),I(z)=\int_{-H}^{z}\kappa(s)\,\mathrm{d}s\quad\text{and}\quad J=\int_{-H}^{-D}\kappa(s)\,\mathrm{d}s=I(-D),(24)

and define the WKB solutionsU±​(z)=κ​(z)−12​e±I​(z)U_{\pm}(z)=\kappa(z)^{-\frac{1}{2}}\operatorname{e}^{\,\pm I(z)}, so that the general solution isU​(z)=a​U+​(z)+b​U−​(z)U(z)=a\,U_{+}(z)+b\,U_{-}(z). Imposing the boundary conditionsU​(−H)=0U(-H)=0(noting thatI​(−H)=0I(-H)=0) andU​(−D)=UDU(-D)=U_{D}, we get the following expression for the WKB solution:U​(z)\displaystyle U(z)=UD​(κ​(−D)κ​(z))12​sinh⁡(I​(z))sinh⁡(J)\displaystyle=U_{D}\left(\frac{\kappa(-D)}{\kappa(z)}\right)^{\frac{1}{2}}\frac{\sinh\big(I(z)\big)}{\sinh(J)}(25)=UD​ρ​(−D)ρ​(z)4​sinh⁡(I​(z))sinh⁡(J),\displaystyle=U_{D}\sqrt[4]{\frac{\rho(-D)}{\rho(z)}}\frac{\sinh\big(I(z)\big)}{\sinh(J)},

leading toU′​(z)\displaystyle U^{\prime}(z)=UD​κ​(−D)12sinh⁡(J)(κ(z)12cosh(I(z))\displaystyle=\frac{U_{D}\,\kappa(-D)^{\frac{1}{2}}}{\sinh(J)}\bigl(\kappa(z)^{\frac{1}{2}}\cosh\big(I(z)\big)\bigr.(26)−12κ(z)−3/2κ′(z)sinh(I(z))).\displaystyle\hskip 73.97733pt\bigl.-\tfrac{1}{2}\,\kappa(z)^{-3/2}\kappa^{\prime}(z)\,\sinh\big(I(z)\big)\bigr).

Note that the second term, which comes from differentiating the slowly varying WKB prefactorκ​(z)−12\kappa(z)^{-\frac{1}{2}}, has size relative to the other (leading order) term controlled by|12​κ​(z)−3/2​κ′​(z)​sinh⁡(I​(z))κ​(z)12​cosh⁡(I​(z))|\displaystyle\left|\frac{\tfrac{1}{2}\kappa(z)^{-3/2}\kappa^{\prime}(z)\sinh(I(z))}{\kappa(z)^{\frac{1}{2}}\cosh(I(z))}\right|=|12​κ′​(z)κ​(z)2​tanh⁡(I​(z))|\displaystyle=\left|\frac{1}{2}\,\frac{\kappa^{\prime}(z)}{\kappa(z)^{2}}\,\tanh\big(I(z)\big)\right|(27)≤|κ′​(z)2​κ​(z)2|,\displaystyle\leq\left|\frac{\kappa^{\prime}(z)}{2\,\kappa(z)^{2}}\right|,

which is consistent with the WKB ansatz (|ρ′​(z)/ρ​(z)|≪|κ​(z)||\rho^{\prime}(z)/\rho(z)|\ll|\kappa(z)|). Therefore, dropping this term is consistent with, and not worse than, the WKB approximation already made when constructingU​(z)U(z)itself. Moreover, note that the second term is exactly zero at the evaluation point−H-H, independently of the size ofκ′/κ2\kappa^{\prime}/\kappa^{2}. Indeed, we have that12​κ​(−H)−3/2​κ′​(−H)​sinh⁡(I​(−H))=0,\tfrac{1}{2}\,\kappa(-H)^{-3/2}\kappa^{\prime}(-H)\,\sinh\big(I(-H)\big)=0,so the formula forU′​(−H)U^{\prime}(-H)below is not merely leading-order WKB, but it is exact at this particular point, given the WKB form ofU​(z)U(z); the WKB error only enters indirectly, through how wellU​(z)U(z)itself approximates the true solution away fromz=−Hz=-H.

Consequently, forz=−Hz=-Hwe haveU′​(−H)\displaystyle U^{\prime}(-H)≈UD​[κ​(−H)​κ​(−D)]12sinh⁡(J)\displaystyle\approx\frac{U_{D}\,\bigl[\kappa(-H)\,\kappa(-D)\bigr]^{\frac{1}{2}}}{\sinh(J)}(28)=UD​i​f𝔪​ρ​(−H)​ρ​(−D)4sinh⁡(J).\displaystyle=U_{D}\sqrt{\frac{\mathrm{i}f}{\mathfrak{m}}}\dfrac{\sqrt[4]{\rho(-H)\rho(-D)}}{\sinh(J)}.

Note that for constantρ\rhowe haveJ=(1+i)​(H−D)δJ=\dfrac{(1+\mathrm{i})(H-D)}{\delta}, whereδ=2​𝔪f​ρ\delta=\sqrt{\dfrac{2\mathfrak{m}}{f\rho}}, and (28) reduces to|U′​(−H)|≈2​2​|UD|δ​eD−Hδ.|U^{\prime}(-H)|\approx 2\sqrt{2}\,\frac{|U_{D}|}{\delta}\,e^{\frac{D-H}{\delta}}.(29)

To provide an estimate ofU′​(−H)U^{\prime}(-H), we consider the following example for a linearly increasing density: set the bottom of the ocean to beH=1000​mH=1000\,\text{m}and the depth below which the wind effects are negligible to beD=100​mD=100\,\text{m}, and writeL≔H−D=900​mL\coloneqq H-D=900\,\text{m}. Moreover, the values for the molecular dynamic viscosity of the water and the mid-latitude Coriolis parameter are, respectively,𝔪≈10−3​kg​m−1​s−1\mathfrak{m}\approx 10^{-3}\ \mathrm{kg\,m^{-1}\,s^{-1}}andf≈10−4​s−1f\approx 10^{-4}\ \text{s}^{-1}. Finally, we assume that the density varies linearly fromρ​(−D)=1020​kg​m−3\rho(-D)=1020\,\mathrm{kg\,m}^{-3}toρ​(−H)=1050​kg​m−3\rho(-H)=1050\,\mathrm{kg\,m}^{-3}. Note that, in general, density variations are much smaller than assumed in this example (see, for example,[21]). With these data, we haveμ​(z)=f​ρ​(z)2​𝔪≈0.23​ρ​(z).\mu(z)=\sqrt{\frac{f\,\rho(z)}{2\mathfrak{m}}}\approx 0.23\sqrt{\rho(z)}.

Sinceρ​(z)\rho(z)is linear inzz, we can perform the change of variablesξ=ρ​(z)∈[1020,1050]\xi=\rho(z)\in[1020,1050], withd​z=30​d​ξ\mathrm{d}z=30\,\mathrm{d}\xi, so thatJ\displaystyle J=(1+i)​∫−H−Dμ​(z)​dz\displaystyle=(1+\mathrm{i})\int_{-H}^{-D}\mu(z)\,\mathrm{d}z(30)≈6.9​(1+i)​∫10201050ξ​dξ≈6700​(1+i),\displaystyle\approx 9\,(1+\mathrm{i})\int_{1020}^{1050}\sqrt{\xi}\,\mathrm{d}\xi\approx 700\,(1+\mathrm{i}),

which gives the bound|U′​(−H)|≲35​|UD|​10−2910≈0,|U^{\prime}(-H)|\lesssim 35\;|U_{D}|\;10^{-2910}\approx 0,

ensuring that, if the ocean is sufficiently deep and the Ekman depth is sufficiently smaller than the total depth of the ocean, imposingU​(−H)=0U(-H)=0also givesU′​(−H)≈0U^{\prime}(-H)\approx 0, and the orthogonality condition between the wind and the Ekman transport is ensured. However, this estimate breaks down in regions where density variations play a more significant role, such as coastal areas, where the water column is also shallower. Indeed, in such regions the angle between the wind and the Ekman transport can deviate from90∘90^{\circ}(see the discussion in[8]), as the wind stress is balanced primarily by bottom stress and along-shelf pressure gradients.

Data availability statement.No data were created or analysed in this study.

## References
- [1]T. K. Chereskin(1995)Direct evidence for an Ekman balance in the California Current.J. Geophys. Res.100(C9),pp. 18261–18269.External Links:DocumentCited by:§I.1,§I.
- [2]A. Constantin(2020)Frictional effects in wind-driven ocean currents.Geophys. Astrophys. Fluid Dyn.115(1),pp. 1–14.External Links:DocumentCited by:§I.1,§I.1,§I.1,§I.
- [3]E. Deusebio, G. Brethouwer, P. Schlatter, and E. Lindborg(2014)A numerical study of the unstratified and stratified ekman layer.J. Fluid Mech.755,pp. 672–704.External Links:DocumentCited by:§I.1.
- [4]V. W. Ekman(1905)On the influence of the Earth’s rotation on ocean currents.Ark. Mat. Astr. Fys.2,pp. 1–52.Cited by:§I.
- [5]D. Gérard-Varet and E. Dormy(2006)Ekman layers near wavy boundaries.J. of Fluid Mech.565,pp. 115–134.External Links:DocumentCited by:§I.1.
- [6]A. D. Jenkins and J. A. T. Bye(2006)Some aspects of the work of V. W. Ekman.Polar Rec.42(1),pp. 15–22.External Links:DocumentCited by:§I.1,§I.
- [7]W. G. Large, J. C. McWilliams, and S. C. Doney(1994)Oceanic vertical mixing: A review and a model with a nonlocal boundary layer parameterization.Rev. Geophys.32,pp. 363–403.External Links:DocumentCited by:§III.
- [8]S. J. Lentz and M. R. Fewings(2012)The wind- and wave-driven inner-shelf circulation..Annu. Rev. Mar. Sci.4,pp. 317–43.External Links:DocumentCited by:§III.
- [9]D. M. Lewis and S. E. Belcher(2004)Time-dependent, coupled, Ekman boundary layer solutions incorporating stokes drift.Dyn. Atmos. Oceans37,pp. 313–351.External Links:DocumentCited by:§I.1.
- [10]J. C. McWilliams, E. Huckle, and A. F. Shchepetkin(2009)Buoyancy Effects in a Stratified Ekman Layer.J. Phys. Oceanogr.39,pp. 2581–2599.External Links:DocumentCited by:§I.1.
- [11]J. P. Pedlosky(1998)Ocean Circulation theory.Springer Berlin, Heidelberg.Cited by:§I.
- [12]J. F. Price and M. A. Sundermeyer(1999)Stratified Ekman layers.J. Geophys. Res.104(C9),pp. 20467–20494.External Links:DocumentCited by:§I.1.
- [13]J. F. Price, R. A. Weller, and R. R. Schudlich(1987)Wind-driven Ocean Currents and Ekman Transport.Science238,pp. 1534 – 1538.External Links:DocumentCited by:§I.1,§I.
- [14]C. Puntini, L. Roberti, and E. Stefanescu(2026)On large-scale wind-drift ocean currents: An asymptotic approach in spherical coordinates..External Links:2602.06473,LinkCited by:§I.1,§I,§II.
- [15]C. Puntini(2026)Nonlinear dynamics of wind-drift currents at mid-latitudes.Nonlinear Anal. Real World Appl.90,pp. 104557.External Links:DocumentCited by:§I.1,§I.1,§I.1.
- [16]L. Roberti(2022)The Ekman spiral for piecewise-constant eddy viscosity.Appl. Anal.101(15),pp. 5528–5536.External Links:DocumentCited by:§I.1,§I.1,§I.1,§I.
- [17]A. Sentchev, M. Yaremchuk, D. Bourras, I. Pairaud, and P. Fraunié(2023)Estimation of the Eddy Viscosity Profile in the Sea Surface Boundary Layer from Underway ADCP Observations.J. Atmos. Ocean. Technol.40(10),pp. 1291 – 1305.External Links:DocumentCited by:§III.
- [18]V. I. Shrira and R. B. Almelah(2020)Upper-ocean Ekman current dynamics: a new perspective.J. Fluid Mech.887,pp. A24.External Links:DocumentCited by:§I.1.
- [19]G. Siedler, S. M. Griffies, J. Gould, and J. A. Church (Eds.)(2013)Ocean circulation and climate: a 21st century perspective.Academic Press,Oxford, UK.Cited by:§I.
- [20]A. Soloviev and R. Lucas(2014)The near-surface layer of the ocean.Springer,Dordrecht.External Links:DocumentCited by:§I.1.
- [21]L. D. Talley, G. L. Pickard, W. J. Emery, and J. H. Swift(2011)Descriptive physical oceanography: an introduction.Academic Press,San Diego.Cited by:§I.1,§I.1,§I,§III,§III.
- [22]G. K. Vallis(2017)Atmospheric and oceanic fluid dynamics.Cambridge University Press,Cambridge.Cited by:§I.1.
- [23]W. Wang and R. X. Huang(2004)Wind energy input to the Ekman layer.J. Phys. Oceanogr.34,pp. 1267–1275.External Links:DocumentCited by:§I.1.

## 


- 


Major funding support from
