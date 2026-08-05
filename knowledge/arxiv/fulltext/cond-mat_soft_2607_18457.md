# Variational formulation for the dynamics of soft matter including inertia

**arXiv ID**: 2607.18457v1
**Authors**: Andrew J Archer
**Published**: 2026-07-20
**Categories**: cond-mat.soft, cond-mat.stat-mech, math-ph
**Comments**: 6 pages
**HTML URL**: https://arxiv.org/html/2607.18457v1

## Abstract

The motion of liquids and soft matter is over-damped and `slow' when viscosity dominates. In this (low Reynolds-number) limit and when the system is isothermal, the equations of motion may be generated via Onsager's variational principle, which neglects inertia. This variational approach is immensely powerful, being used to obtain equations of motion for colloidal fluids, droplets on surfaces and much more. However, inertia can play a role, manifesting as vibrations and under-damped motion. Here we show how to extend this variational framework so that it remains valid for when damping/dissipation and inertia are both equally important.

## Full Text

Variational formulation for the dynamics of soft matter including inertia

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18457v1 [cond-mat.soft] 20 Jul 2026

## Variational formulation for the dynamics of soft matter including inertiaAndrew J. Archera.j.archer@lboro.ac.ukDepartment of Mathematical Sciences and Interdisciplinary Centre for Mathematical Modelling, Loughborough University, Loughborough, Leicestershire, LE11 3TU, United Kingdom

## Abstract

The motion of liquids and soft matter is over-damped and ‘slow’ when viscosity dominates. In this (low Reynolds-number) limit and when the system is isothermal, the equations of motion may be generated via Onsager’s variational principle, which neglects inertia. This variational approach is immensely powerful, being used to obtain equations of motion for colloidal fluids, droplets on surfaces and much more. However, inertia can play a role, manifesting as vibrations and under-damped motion. Here we show how to extend this variational framework so that it remains valid for when damping/dissipation and inertia are both equally important.††preprint:AIP/123-QED

## IIntroduction

In physics there is a long history of formulating dynamical equations as functional minimisation problems.
Variational principles are elegant and powerful formulations of the governing physics.
For over-damped dissipative systems, where frictional forces dominate, Onsager’s variational principle (OVP) is a minimum free energy dissipation principle that allows us to express the governing equations in a variational manner.Onsager (1931); de Groot and Mazur (1962)This approach directly connects to the extensive knowledge we have from thermodynamics, statistical mechanics, Landau theory and its symmetry based arguments, which all lead to good approximations for the free energy,FF.Chaikin and Lubensky (2000)OVP takes us directly from the free energy to the time evolution equations.
The OVP approach is thus extremely powerful, but it is only applicable in the over-damped (slow dynamics) limit.
Here, we extending the OVP approach to include under-damped dynamics and other inertial effects, yielding a theoretical framework for generating the equations of motion
of liquids and other soft matter systems whenever damping/dissipation and inertia are equally relevant.

The OVP approach has been successfully used in recent years to derive equations of motion for fluids and other soft condensed matter systems in the viscosity dominated (low Reynolds-number) regime.Doi (2011,2013); Doiet al.(2019); Wang, Qian, and Xu (2021)For colloidal fluids, the particle equations of motion can often be approximated as a Brownian motion, i.e. via over-damped stochastic equations of motion.
Here, the power functional theory (PFT) of Brader and SchmidtSchmidt and Brader (2013); Schmidt (2022)shows that the OVP formulation of the dynamics is exact, albeit not all the involved quantities are known exactly.

The starting point for the OVP approach is an expression for the free energyFFthat incorporates the relevant physics, written as a function/functional of the slow variables/fields characterizing the state of the system.
For example, for colloidal suspensions, the relevant field is the local densityρ​(𝐫,t)\rho({\mathbf{r}},t)at position𝐫{\mathbf{r}}and timett.
Or, for liquid drops on surfaces, the relevant quantity is the thickness of the liquidh​(𝐱,t)h({\mathbf{x}},t)over position𝐱{\mathbf{x}}on the surface.Oron, Davis, and Bankoff (1997); De Gennes, Brochard-Wyart, and Quéré (2003); Craster and Matar (2009)For each relevant variable/field there is an associated velocity,𝐯​(𝐫,t){\mathbf{v}}({\mathbf{r}},t).
Next, one constructs the RayleighanR=F˙+Φ,R=\dot{F}+\Phi,(1)

whereF˙\dot{F}denotes the time derivative ofFF, andΦ\Phiis the dissipation function/functional.
The exact form ofΦ\Phiis generally unknown, as evident in the PFT formulation for colloidal particles.Schmidt and Brader (2013); Schmidt (2022); Lutsko and Oettel (2021)However, the leading order contributions must be quadratic in the velocity𝐯{\mathbf{v}}, and in many systems using just this is a good approximation.Doi (2011,2013); Doiet al.(2019)The dynamical equations are then given by minimising the RayleighanRRwith respect to the relevant velocities/currents, giving the stationary condition(s)δ​Rδ​𝐯=0,\frac{\delta R}{\delta{\mathbf{v}}}=0,(2)

i.e. the functional derivative ofRRwith respect to the velocities𝐯{\mathbf{v}}must equal zero.
The structure of Eq.\eqrefeq:2 already indicates it applies only in the over-damped limit.
Since it involves just the velocity𝐯{\mathbf{v}}and not the acceleration𝐯˙\dot{{\mathbf{v}}}, it therefore neglects inertia, preventing accurate description of under-dampened dynamics.
Note that ifRRis approximated by a function (not a functional) of𝐯{\mathbf{v}}, then\eqrefeq:2 should be interpreted as just a partial derivative.Doi (2011,2013); Doiet al.(2019)

From\eqrefeq:2 we obtain an expression for the velocity𝐯{\mathbf{v}}in terms of (functional) derivatives ofFF.
For colloidal fluids (see below), this expression can be used with the continuity equation,∂ρ∂t=−∇⋅(ρ​𝐯),\frac{\partial\rho}{\partial t}=-\nabla\cdot(\rho{\mathbf{v}}),(3)

to obtain the dynamics.
If the relevant slow field is not conserved or there is a non-conserved aspect to the dynamics, such as in the case of liquids drops on surfaces, one instead has∂h∂t=−∇⋅(h​𝐯)+σ\frac{\partial h}{\partial t}=-\nabla\cdot(h{\mathbf{v}})+\sigma.
This includes the non-conserved termσ\sigma, which describes the evaporation from the drop or condensation of vapour in the air onto the drop.Oron, Davis, and Bankoff (1997); Moosman and Homsy (1980); Ajaev (2005); Thieleet al.(2009); Thiele (2010); Tóthet al.(2026)It should now be evident that this variational approach is extremely powerful.

This brings us to our central hypothesis: for systems where inertial effects are as equally relevant as viscous/dissipative effects, we argue that Eq.\eqrefeq:2 should be replace withδ​Rδ​𝐯=−∂∂t​(δ​Kδ​𝐯),\frac{\delta R}{\delta{\mathbf{v}}}=-\frac{\partial}{\partial t}\left(\frac{\delta K}{\delta{\mathbf{v}}}\right),(4)

whereKKis the kinetic energy of the system, which is a function(al) of𝐯{\mathbf{v}}.

## IIDynamics of a single particle

Rather than starting with a derivation of Eq.\eqrefeq:4 (which we postpone to later, in Sec.V), for now we assume Eq.\eqrefeq:4 and explore where that assumption leads to.
As alluded to above, we are building towards showing that Eq.\eqrefeq:4 can be used to formulate the dynamical equations for the (number) density distributionρ​(𝐫,t)\rho({\mathbf{r}},t)ofNNinteracting colloidal particles suspended in a fluid.
However, as an instructive ‘warm-up problem’ it helps if we first consider the much simpler case of a single colloid that is suspended in a background fluid and under the influence of an external potentialU​(𝐫)U({\mathbf{r}}).
In this case, the free energy is simply the potential energy, i.e.F=U​(𝐫)F=U({\mathbf{r}}).
Differentiating with respect to time, we obtainF˙=∇U⋅𝐯\dot{F}=\nabla U\cdot{\mathbf{v}}(chain rule), where𝐯=𝐫˙{\mathbf{v}}=\dot{{\mathbf{r}}}is the velocity and∇=∂/∂𝐫\nabla=\partial/\partial{\mathbf{r}}.

As mentioned, the leading order contribution toΦ\Phimust be quadratic in𝐯{\mathbf{v}}, so we writeΦ=12​γ​𝐯2+Φe​x\Phi=\frac{1}{2}\gamma{\mathbf{v}}^{2}+\Phi_{ex}, whereγ\gammais a friction constant, the value of which will become clear shortly, andΦe​x\Phi_{ex}is the remainder, incorporating everything neglected in the leading order quadratic contribution.
AssumingΦe​x≈0\Phi_{ex}\approx 0and then plugging these into Eq.\eqrefeq:1 gives,R=∇U⋅𝐯+12​γ​𝐯2R=\nabla U\cdot{\mathbf{v}}+\frac{1}{2}\gamma{\mathbf{v}}^{2}.
As a first check, we substitute this into Eq.\eqrefeq:2, i.e. we differentiate the RayleighanRRwith respect to𝐯{\mathbf{v}}(keeping𝐫{\mathbf{r}}constant), to obtainγ​𝐯+∇U=0.\gamma{\mathbf{v}}+\nabla U=0.(5)

This is simply the over-damped dynamical equation for a particle in a fluid, given as the balance of the Stokes drag force and the force due to the potentialUU, as long as we identifyγ=6​π​η​ℛ\gamma=6\pi\eta{\cal R}(the Stokes law), whereη\etais the fluid viscosity andℛ{\cal R}is the radius of the particle.

In the under-damped case, we must consider the kinetic energyK=12​m​𝐯2K=\frac{1}{2}m{\mathbf{v}}^{2}, wheremmis the mass of the particle. Plugging this into Eq.\eqrefeq:4, together with the result in Eq.\eqrefeq:5 for the left hand side, gives−γ​𝐯−∇U=m​𝐯˙,-\gamma{\mathbf{v}}-\nabla U=m\dot{{\mathbf{v}}},(6)

which of course is just Newton’s equations for a particle under the influence of the Stokes drag force and an external force−∇U-\nabla U.
We are now ready to tackle the real problem of interest.

## IIIUnder-damped interacting colloids

We consider systems ofNNinteracting Brownian particles with under-damped (Langevin) equations of motion.
For these systems we now show that the formally exact isothermal equations of motion for the coupled fieldsρ\rhoand𝐯{\mathbf{v}}that were obtained in Ref.Archer,2009, can instead be obtained from Eq.\eqrefeq:4.
In other words, Eq.\eqrefeq:4 is the generalised variational principle (or PFT) for generating the dynamical equations.
These are also often referred to as ‘dynamical density functional theory’ (DDFT),Marconi and Tarazona (1999); Archer and Evans (2004); Archer (2009); Hansen and McDonald (2013); te Vrugt, Löwen, and Wittkowski (2020)building on the extremely powerful equilibrium classical density functional theory (DFT).Hansen and McDonald (2013); Evans (1979)DFT is a theory for the free energy functionalF​[ρ]F[\rho].
The advantage of DDFT/PFT is that it builds on this extensive body of knowledge.

The first term in the Rayleighan\eqrefeq:1 can be evaluated simply by applying the chain rule for functionals, giving{align}˙F=∫δFδρ∂ρ∂t dr
=-∫δFδρ∇⋅(ρv) dr
=∫ρv⋅∇δFδρdr,


where the second line comes from using Eq.\eqrefeq:continuity and the last from an integration by parts and also assuming that the boundary terms are zero, i.e. that the flux𝐣=ρ​𝐯{\mathbf{j}}=\rho{\mathbf{v}}is zero on the boundaries.
The dissipation functional can be written asSchmidt (2022)Φ=∫γ2​m​ρ​𝐯2​𝑑𝐫+Φe​x,\Phi=\int\frac{\gamma}{2}m\rho{\mathbf{v}}^{2}d{\mathbf{r}}+\Phi_{ex},(7)

whereγ\gammais the same friction coefficient introduced in Sec.II.
Notice the leading order term is quadratic in𝐯{\mathbf{v}}, while all higher order contributions are incorporated inΦe​x\Phi_{ex}.
Taking the functional derivative of the RayleighanRRwith respect to𝐯{\mathbf{v}}(keepingρ\rhofixed), we obtainδ​Rδ​𝐯=ρ​∇δ​Fδ​ρ+γ​m​ρ​𝐯+δ​Φe​xδ​𝐯.\frac{\delta R}{\delta{\mathbf{v}}}=\rho\nabla\frac{\delta F}{\delta\rho}+\gamma m\rho{\mathbf{v}}+\frac{\delta\Phi_{ex}}{\delta{\mathbf{v}}}.(8)

In the over-damped case\eqrefeq:2, where the expression above equals zero, together with Eq.\eqrefeq:continuity, this is just the PFT of Schmidt and Brader.Schmidt and Brader (2013); Schmidt (2022)Making the further approximation thatΦe​x=0\Phi_{ex}=0, then in the over-damped limit we obtain that the fluxρ​𝐯=−Γ​ρ​∇δ​F/δ​ρ\rho{\mathbf{v}}=-\Gamma\rho\nabla\delta F/\delta\rho, whereΓ=1/(m​γ)\Gamma=1/(m\gamma), which can be inserted into Eq.\eqrefeq:continuity to obtain the usual adiabatic DDFT equation.Marconi and Tarazona (1999); Archer and Evans (2004); Hansen and McDonald (2013); te Vrugt, Löwen, and Wittkowski (2020)

Returning to the under-damped case, we must consider the kinetic energyK=∫12​m​ρ​𝐯2​𝑑𝐫.K=\int\frac{1}{2}m\rho{\mathbf{v}}^{2}d{\mathbf{r}}.(9)

From this we obtain∂∂t​(δ​Kδ​𝐯)=∂∂t​(m​ρ​𝐯)=m​∂𝐣∂t.\frac{\partial}{\partial t}\left(\frac{\delta K}{\delta{\mathbf{v}}}\right)=\frac{\partial}{\partial t}\left(m\rho{\mathbf{v}}\right)=m\frac{\partial{\mathbf{j}}}{\partial t}.(10)

On plugging the results in Eqs.\eqrefeq:9 and\eqrefeq:11 into Eq.\eqrefeq:4 and dividing through bymm, we obtain∂𝐣∂t+γ​𝐣+1m​δ​Φe​xδ​𝐯+1m​ρ​∇δ​Fδ​ρ=0.\frac{\partial{\mathbf{j}}}{\partial t}+\gamma{\mathbf{j}}+\frac{1}{m}\frac{\delta\Phi_{ex}}{\delta{\mathbf{v}}}+\frac{1}{m}\rho\nabla\frac{\delta F}{\delta\rho}=0.(11)

This is identical to Eq. (20) in Ref.Archer,2009, although in the notation ofArcher,2009we would instead write the term1m​δ​Φe​xδ​𝐯=A​(𝐫,t)\frac{1}{m}\frac{\delta\Phi_{ex}}{\delta{\mathbf{v}}}=A({\mathbf{r}},t).
The starting point of the derivation of this equation in Ref.Archer,2009is theNN-particle Kramers (Fokker-Plank) equation.
The approach of Ref.Archer,2009it to integrate Kramers’ equation with respect to(N−1)(N-1)degrees of freedom, in order to obtain the time evolution equation for the one-body densityρ​(𝐫,t)\rho({\mathbf{r}},t).
It should also be emphasised that the free energyFFin Eq.\eqrefeq:12 is a quantity given in Ref.Archer,2009in terms of non-equilibrium distribution functions, which we approximate by corresponding equilibrium distributions.
Another way to say this is thatFFin Eq.\eqrefeq:12 is a
non-equilibrium free energy, which we then approximate by the corresponding equilibrium free energy.

The main conclusion we draw from the derivation above is that the formally exact dynamical equation\eqrefeq:12 isgeneratedby the expression in Eq.\eqrefeq:4.
Thus, we may view\eqrefeq:4 as the (PFT) variational principle for generating the dynamics in the under-damped isothermal case.
We must remember of course that for most systems in practice neitherF​[ρ]F[\rho]norΦe​x​[ρ,𝐯]\Phi_{ex}[\rho,{\mathbf{v}}]are known exactly, as discussed in Ref.Schmidt,2022in the context of the over-damped case.

In the over-damped case, there has been good progress to develop suitable approximations forΦe​x\Phi_{ex}, that is summarised well in Ref.Schmidt,2022, whereΦe​x\Phi_{ex}is referred to as the excess power functionalPe​x​cP^{exc}.
The derivative−δ​Pe​x​c/δ​𝐯-\delta P^{exc}/\delta{\mathbf{v}}gives the ‘super-adiabatic forces’ that have been studied extensively by Schmidt and coworkers – seeSchmidt and Brader (2013); Schmidt (2022); Stuhlmülleret al.(2018); Treffenstädt and Schmidt (2020); de Las Heras and Schmidt (2020); Geigenfeind, de las Heras, and Schmidt (2020); Treffenstädt, Schindler, and Schmidt (2022); de Las Heraset al.(2023), for further details.
We see no reason why all the approximations developed for the over-damped case should not also be applicable in the under-damped case.
In Ref.Archer,2009a simple local-equilibrium approximation leads toA​(𝐫,t)≈Al​e​(𝐫,t)=∇⋅(ρ​𝐯⊗𝐯)A({\mathbf{r}},t)\approx A_{le}({\mathbf{r}},t)=\nabla\cdot(\rho{\mathbf{v}}\otimes{\mathbf{v}}), where⊗\otimesdenotes a dyadic product, which then results in Eq.\eqrefeq:12 having the form of a generalised Stokes equation.
Clearly, further work applying and perhaps developing other approximations forΦe​x\Phi_{ex}is required, building on the work inSchmidt and Brader (2013); Schmidt (2022); Stuhlmülleret al.(2018); Treffenstädt and Schmidt (2020); de Las Heras and Schmidt (2020); Geigenfeind, de las Heras, and Schmidt (2020); Treffenstädt, Schindler, and Schmidt (2022); de Las Heraset al.(2023).
We hope the ideas presented here provide impetus for such activity.

Having demonstrated that Eq.\eqrefeq:4 generates the correct equations of motion for both a single particle in a fluid and also the equations of motion for the density distribution of interacting Brownian colloidal particles, we feel we have sufficient evidence to postulate that Eq.\eqrefeq:4 is in fact much more general.
In other words, whenever inertial effects are expected to be just as relevant as viscous dissipation, we propose that Eq.\eqrefeq:4 may be applied entirely in the same spirit as the OVP approach based on Eq.\eqrefeq:2.
As discussed in the introduction, the essence of the OVP approach is to identify the relevant slow variables/fields and then express the free energy and Rayleighan in terms of these.
This view is supported by the arguments of Ref.Laurilaet al.,2006, which shows that when a high-dimensional system, with dynamics that can be written as the variation of a RayleighanRR, is projected down onto a lower dimensional phase space, then the variational structure is preserved. In other words, the projected dynamics can still be obtained from a stationary condition on a more course-grained RayleighanRR.
Such arguments imply that such a coarse graining from microscopic to more mesoscopic degrees of freedom should retain the variational structure implicit in Eq.\eqrefeq:4.
Taking this view, we now apply our approach in order to derive equations of motion for liquid films and droplets on surfaces.

## IVliquid films and drops on solid surfaces

The time evolution equation for the heighth​(𝐱,t)h({\mathbf{x}},t)of liquid films/droplets on surfaces (generally referred to as the ‘thin-film equation’) is normally derived via a long-wave analysis of the Navier-Stokes equations,Oron, Davis, and Bankoff (1997); De Gennes, Brochard-Wyart, and Quéré (2003); Craster and Matar (2009)although it can instead be derived via the OVP in Eq.\eqrefeq:2, as discussed inQian, Wang, and Sheng (2006); Xu, Thiele, and Qian (2015); Xu, Di, and Doi (2016); Thiele (2018); Lopes, Thiele, and Hazel (2018); Peschka (2018); Tóthet al.(2026).
The gradient dynamics formulation of thin-film hydrodynamicsMitlin (1993); Thiele (2010,2011)helps to see the connections between these two different approaches.
However, there are numerous situations where liquids on surfaces exhibit under-damped vibrational (oscillatory) behaviour, that are not described by the (over-damped) thin-film equation.
By starting from Eq.\eqrefeq:4, inertial effects are incorporated, giving a theory that should be capable of describing these cases.

The derivation proceeds in a manner somewhat analogous to the colloidal case in Sec.III.
Exactly equivalent to Eq.\eqrefeq:7, we obtainF˙=∫h​𝐯⋅∇δ​Fδ​h​d​𝐱.\dot{F}=\int h{\mathbf{v}}\cdot\nabla\frac{\delta F}{\delta h}d{\mathbf{x}}.(12)

Note that in the aboveh​𝐯=𝐣h{\mathbf{v}}={\mathbf{j}}, the two dimensional height-averaged flux over the surface.
The dissipation functional isTóthet al.(2026){align}Φ=∫j22Mdx+Φ_ex
=∫3ηv22hdx+Φ_ex,

where we have used the mobilityM=h3/(3​η)M=h^{3}/(3\eta), whereη\etais the fluid viscosity, which is derived by assuming no-slip plane Poiseuille film flow over the surface.Oron, Davis, and Bankoff (1997); De Gennes, Brochard-Wyart, and Quéré (2003); Craster and Matar (2009); Tóthet al.(2026)From Eqs.\eqrefeq:13 and\eqrefeq:14 we obtainδ​Rδ​𝐯=h​∇δ​Fδ​h+3​η​𝐯h+δ​Φe​xδ​𝐯.\frac{\delta R}{\delta{\mathbf{v}}}=h\nabla\frac{\delta F}{\delta h}+\frac{3\eta{\mathbf{v}}}{h}+\frac{\delta\Phi_{ex}}{\delta{\mathbf{v}}}.(13)

In the case where the dynamics is over-damped (the usual thin-film long-wave limit) then the right hand side of\eqrefeq:15 equals zero.
If we also assume thatΦe​x=0\Phi_{ex}=0and that evaporationσ\sigmacan be neglected, then Eq.\eqrefeq:15 gives the over-damped result𝐣=h​𝐯=−h33​η​∇δ​Fδ​h.{\mathbf{j}}=h{\mathbf{v}}=-\frac{h^{3}}{3\eta}\nabla\frac{\delta F}{\delta h}.(14)

The usual thin-film approximation for the free energy isOron, Davis, and Bankoff (1997); De Gennes, Brochard-Wyart, and Quéré (2003); Craster and Matar (2009)F​[h]=∫(f​(h)+γ2​(∇h)2)​𝑑𝐱,F[h]=\int\left(f(h)+\frac{\gamma}{2}(\nabla h)^{2}\right)d{\mathbf{x}},(15)

wheref​(h)f(h)is the binding potential andγ\gammais the surface tension.
Taking this free energy, together with the expression for the flux in Eq.\eqrefeq:16 and the continuity equation gives the usual thin-film equation.Oron, Davis, and Bankoff (1997); De Gennes, Brochard-Wyart, and Quéré (2003); Craster and Matar (2009); Qian, Wang, and Sheng (2006); Xu, Thiele, and Qian (2015); Xu, Di, and Doi (2016); Thiele (2018); Lopes, Thiele, and Hazel (2018); Peschka (2018); Tóthet al.(2026)

In the under-damped case, we must consider the kinetic energyK=∫3​ϱm​𝐣25​h​𝑑𝐱=∫35​h​ϱm​𝐯2​𝑑𝐱,K=\int\frac{3\varrho_{m}\,{\mathbf{j}}^{2}}{5h}d{\mathbf{x}}=\int\frac{3}{5}h\varrho_{m}\,{\mathbf{v}}^{2}d{\mathbf{x}},(16)

whereϱm\varrho_{m}is the mass density of the liquid (assumed constant within the liquid film).
The above result comes from assuming that the velocity profileu​(𝐫,t)u({\mathbf{r}},t)within the liquid film is a plane Poiseuille film flow with no slip at the solid surface, i.e. in one dimension having the parabolic formu​(z)=u0​(z2/2−h​z)u(z)=u_{0}(z^{2}/2-hz)for0<z<h0<z<h, wherezzis the distance perpendicular to the surface.
The corresponding flux isj=−∫0hu​(z)​𝑑zj=-\int_{0}^{h}u(z)dz(see e.g.Oron, Davis, and Bankoff (1997); Tóthet al.(2026)) and the kinetic energy density is therefore∫0h12​ϱm​u​(z)2​𝑑z=3​ϱm​j25​h\int_{0}^{h}\frac{1}{2}\varrho_{m}u(z)^{2}dz=\frac{3\varrho_{m}\,j^{2}}{5h}.

Plugging Eq.\eqrefeq:film_KE into the right hand side of Eq.\eqrefeq:4 and using the result in\eqrefeq:15 for the left hand side, we obtainh​∇δ​Fδ​h+3​η​𝐣h2+δ​Φe​xδ​𝐯=−65​ϱm​d​𝐣d​t.h\nabla\frac{\delta F}{\delta h}+\frac{3\eta{\mathbf{j}}}{h^{2}}+\frac{\delta\Phi_{ex}}{\delta{\mathbf{v}}}=-\frac{6}{5}\varrho_{m}\frac{d{\mathbf{j}}}{dt}.(17)

Taking this result together with the approximation for the free energy in Eq.\eqrefeq:free_thin and also assumingf=0f=0, we obtaind​𝐣d​t=5​h6​ϱm​∇(γ​∇2h)−5​η2​h2​ϱm​𝐣−56​ϱm​δ​Φe​xδ​h.\frac{d{\mathbf{j}}}{dt}=\frac{5h}{6\varrho_{m}}\nabla(\gamma\nabla^{2}h)-\frac{5\eta}{2h^{2}\varrho_{m}}{\mathbf{j}}-\frac{5}{6\varrho_{m}}\frac{\delta\Phi_{ex}}{\delta h}.(18)

Comparing the above result with Eq. (8) in Ref.Ruyer-Quil and Manneville,2002allows to see what would be neglected if one were to assumeΦe​x=0\Phi_{ex}=0, and already gives hints for how to chooseΦe​x\Phi_{ex}.
In other words, Eq.\eqrefeq:20 together with a suitable approximation forΦe​x\Phi_{ex}is a good place to start when deriving thin-film flow type equations incorporating inertia.

A fruitful future avenue for research that we do not pursue here is to explore what choice of approximation forΦe​x\Phi_{ex}leads to either (i) the Benney equation,Benney (1966)(ii) the theory of Ref.Zitzet al.,2019, (iii) the weighted residuals theory,Ruyer-Quil and Manneville (2000,2002); Holroyd, Cimpeanu, and Gomes (2024)or possibly an improvement on these.
We believe such an exploration will be extremely fruitful.
We expect that generating evolution equations forh​(𝐫,t)h({\mathbf{r}},t)in this way will lead to identifying new physics and specifically to good approximations forΦe​x\Phi_{ex}.

Before we move on, we note that settingΦe​x=0\Phi_{ex}=0and introducing the integrating factorϕ=exp⁡(5​η2​ϱm​∫1h2​𝑑t)\phi=\exp(\frac{5\eta}{2\varrho_{m}}\int\frac{1}{h^{2}}dt)allows us to rewrite Eq.\eqrefeq:18 asdd​t​(ϕ​𝐣)=−5​ϕ​h6​ϱm​∇δ​Fδ​h,\frac{d}{dt}(\phi{\mathbf{j}})=-\frac{5\phi h}{6\varrho_{m}}\nabla\frac{\delta F}{\delta h},(19)

which can be integrated to giveϕ​(h,t)​𝐣=−∫0t5​ϕ​(h,t′)​h6​ϱm​∇δ​Fδ​h​d​t′,\phi(h,t){\mathbf{j}}=-\int_{0}^{t}\frac{5\phi(h,t^{\prime})h}{6\varrho_{m}}\nabla\frac{\delta F}{\delta h}dt^{\prime},(20)

or equivalently𝐣=−∫0tℳ​∇δ​Fδ​h​d​t′,{\mathbf{j}}=-\int_{0}^{t}{\cal M}\nabla\frac{\delta F}{\delta h}dt^{\prime},(21)

with the following explicit result for the memory function:ℳ=5​h′​ϕ′/(6​ϱm​ϕ){\cal M}=5h^{\prime}\phi^{\prime}/(6\varrho_{m}\phi), where quantities with a prime are evaluated at timet′t^{\prime}, while theϕ\phiwithout a prime is evaluated at the later timett.
The result in Eq.\eqrefeq:23 is precisely what one would expect if one were to derive the thin-film equation via the Mori-Zwanzig formalism.Te Vrugtet al.(2024)The integrating factor approach used here can also be applied to Eq.\eqrefeq:12 in the colloidal case whenΦe​x=0\Phi_{ex}=0.
The resulting memory function in that case is a simple exponential. See also Refs.Anero, Español, and Tarazona,2013; Wittkowski, Löwen, and Brand,2013for further discussion of such DDFT-type theories that include memory.

## VA derivation of equation (4)

Having taken a ‘try it and see’ approach to presenting our arguments for why Eq.\eqrefeq:4 should be taken as the generalisation of OVP to situations where inertial effect must also be included, we now present a derivation of Eq.\eqrefeq:4 that starts from ideas in particle mechanics.
We commence this by recapitulating some key ideas given in Refs.Edwards and Freed,1974; Whittacker,1937; see also Ref.Giga, Kirshtein, and Liu,2018.
In conservative dynamical systems, the dynamics can be obtained from minimising the time integral of the Lagrangianℒ{\cal L},δ​∫ℒ​[𝐫​(t),𝐫˙​(t),⋯]​𝑑t=0,\delta\int{\cal L}[{\mathbf{r}}(t),\dot{{\mathbf{r}}}(t),\cdots]dt=0,(22)

which then yields the familiar Euler-Lagrange equationsδ​ℒδ​𝐫−dd​t​(δ​ℒδ​𝐫˙)+d2d​t2​(δ​ℒδ​𝐫¨)+⋯=0.\frac{\delta{\cal L}}{\delta{\mathbf{r}}}-\frac{d}{dt}\left(\frac{\delta{\cal L}}{\delta\dot{{\mathbf{r}}}}\right)+\frac{d^{2}}{dt^{2}}\left(\frac{\delta{\cal L}}{\delta\ddot{{\mathbf{r}}}}\right)+\cdots=0.(23)

To extend to the case where friction is present, we must introduce the dissipation by including another term that depends on the velocities, which to be consistent with previous discussion we denote as−Φ​(𝐯)-\Phi({\mathbf{v}}), so that the variational principle becomesδ​∫ℒ​[𝐫​(t),𝐫˙​(t),⋯]​𝑑t−δ​∫Φ​[𝐯​(t),𝐯˙​(t),⋯]​𝑑t=0,\delta\int{\cal L}[{\mathbf{r}}(t),\dot{{\mathbf{r}}}(t),\cdots]dt-\delta\int\Phi[{\mathbf{v}}(t),\dot{{\mathbf{v}}}(t),\cdots]dt=0,(24)

and so Eq.\eqrefeq:EL_eq_1 becomes{align}δLδr- ddt(δLδ˙r) +…
-[δΦδv- ddt(δΦδ˙v) +⋯]_v=˙r,˙v=¨r,⋯
=0.


The above pair of equations are just Eqs. (2.3) and (2.4) from Ref.Edwards and Freed,1974.
For simplicity, we now revert to the notation of Sec.II.
As always,ℒ=K−U{\cal L}=K-Uand so Eq.\eqrefeq:EL_eq_2 becomes−∂U∂𝐫−dd​t​(∂K∂𝐫˙)−∂Φ∂𝐯=0.-\frac{\partial U}{\partial{\mathbf{r}}}-\frac{d}{dt}\left(\frac{\partial K}{\partial\dot{{\mathbf{r}}}}\right)-\frac{\partial\Phi}{\partial{\mathbf{v}}}=0.(25)

The first term above can be rewritten as−∂U˙∂𝐫˙-\frac{\partial\dot{U}}{\partial\dot{{\mathbf{r}}}}, which comes from noting thatU˙=∂U∂𝐫​𝐫˙\dot{U}=\frac{\partial U}{\partial{\mathbf{r}}}\dot{{\mathbf{r}}}(chain rule) and so∂U˙∂𝐫˙=∂U∂𝐫\frac{\partial\dot{U}}{\partial\dot{{\mathbf{r}}}}=\frac{\partial U}{\partial{\mathbf{r}}}.
Using this result in Eq.\eqrefeq:EL_3 then allows us to rewrite it as∂(U˙+Φ)∂𝐯=−dd​t​(∂K∂𝐯),\frac{\partial(\dot{U}+\Phi)}{\partial{\mathbf{v}}}=-\frac{d}{dt}\left(\frac{\partial K}{\partial{\mathbf{v}}}\right),(26)

which is just a way of writing Eq.\eqrefeq:4.

## VIConcluding remarks

In this paper we have postulated that Eq.\eqrefeq:4 should replace the OVP in Eq.\eqrefeq:2 whenever inertial effects are expected to be just as important as dissipative/frictional effects.
To support this, we have demonstrated that Eq.\eqrefeq:4 is a valid and useful way to formulate the dynamical equations for colloidal particles suspended in a fluid, both in the one-particle case and for a fluid of interacting colloidal particles.
Thus, we have provided the generalisation of PFTSchmidt (2022)to the isothermal under-damped Brownian dynamics case.

Thinking broadly, the OVP in Eq.\eqrefeq:2 has turned out to be quite general and has been applied successfully to a wide range of systems where friction or viscous dissipation dominates the dynamicsDoi (2011,2013); Doiet al.(2019)(i.e. not just colloidal fluids and droplets on surfaces).
For example, the OVP/PFT has been applied to active matter and biological systems.Krinninger and Schmidt (2019); Hermannet al.(2019); Liu, Ou-Yang, and Wu (2026); Xu (2026)We expect the same success for Eq.\eqrefeq:4 whenever inertial effects start to become relevant.

To build on the ideas presented here, we see several avenues for fruitful future work. The first direction concerns the foundations of Eq.\eqrefeq:4 and determining in greater detail the implicit assumptions and limitations.
In the literature, there are various theories of ‘analytical thermodynamics’,Podio-Guidugli and Virga (2023)the GENERIC formulation of fluid dynamics,Grmela and Öttinger (1997); Grmela (2026)applications of the Herglotz variational principle to dissipative field theoriesLazoet al.(2018); Gasetet al.(2024)and the formulation in Ref.Yasudaet al.,2026.
Working through these other approaches to see if and how they connect to the formulation in Eq.\eqrefeq:4 should be extremely fruitful.
This will build connections to other areas, where ideas may exist that are new to the soft matter areas discussed here.
By addressing these questions and investigating these possible connections, this should allow to determine how widely applicable Eq.\eqrefeq:4 is.

A powerful coarse-grained application/extension of the general OVP-based\eqrefeq:2 approach is to parametrise the system of interest with just a few relevant variables, resulting in simple (ordinary differential equation) models that are easy to solve numerically.
For example, for droplets on surfaces, instead of treating the full profileh​(𝐫,t)h({\bf r},t), one can consider just the dynamics of the droplet radius and maximum height.
This simplified approach has successfully incorporated/captured evaporation, solute deposition (coffee ring effect), contact line motion, droplet interactions and more.Tóthet al.(2026); Man and Doi (2017); Wu, Man, and Doi (2018); Wuet al.(2019); Wu, Doi, and Man (2021); Yanget al.(2021)Future work to extend and build on these approaches, by incorporating inertial effects via Eq.\eqrefeq:4, will allow us to determine when and how inertia changes the dynamics.
This will enable us to predict e.g. the onset of damped-oscillatory dynamics of liquid bridges suspended between parallel rod-shaped electrodes.Bokányi-Tóthet al.(2026)

Finally, we expect our generalisation of the OVP and PFT to the under-damped regime to be especially valuable for systems that are driven to be far-from-equilibrium, since this is where inertia and friction/dissipation can become of equal significance, due to the driving.

## Acknowledgements.We gratefully acknowledge useful discussions and feedback from Achilleas Lazarides, Tapio Ala-Nissila and Uwe Thiele.

## References
- Onsager (1931)L. Onsager, “Reciprocal
relations in irreversible processes. I.” Phys. Rev.37, 405 (1931).
- de Groot and Mazur (1962)S. R. de Groot and P. Mazur,Non-equilibrium
Thermodynamics(North Holland Publishing
Company, 1962).
- Chaikin and Lubensky (2000)P. M. Chaikin and T. C. Lubensky,Principles of
condensed matter physics(Cambridge University
Press, 2000).
- Doi (2011)M. Doi, “Onsager’s
variational principle in soft matter,” J. Phys.: Condens. Matter23, 284118 (2011).
- Doi (2013)M. Doi,Soft matter physics(Oxford University Press, 2013).
- Doiet al.(2019)M. Doi, J. Zhou, Y. Di, and X. Xu, “Application of the Onsager-Machlup integral in solving
dynamic equations in nonequilibrium systems,” Phys. Rev. E99, 063303 (2019).
- Wang, Qian, and Xu (2021)H. Wang, T. Qian, and X. Xu, “Onsager’s variational principle in
active soft matter,” Soft Matter17, 3634 (2021).
- Schmidt and Brader (2013)M. Schmidt and J. M. Brader, “Power functional
theory for Brownian dynamics,” J. Chem. Phys.138, 214101 (2013).
- Schmidt (2022)M. Schmidt, “Power
functional theory for many-body dynamics,” Rev. Mod. Phys.94, 015007 (2022).
- Oron, Davis, and Bankoff (1997)A. Oron, S. H. Davis, and S. G. Bankoff, “Long-scale evolution of thin
liquid films,” Rev. Mod. Phys.69, 931
(1997).
- De Gennes, Brochard-Wyart, and Quéré (2003)P.-G. De Gennes, F. Brochard-Wyart, and D. Quéré,Capillarity and
wetting phenomena: drops, bubbles, pearls, waves(Springer Science & Business Media, 2003).
- Craster and Matar (2009)R. V. Craster and O. K. Matar, “Dynamics and
stability of thin liquid films,” Rev. Mod. Phys.81, 1131 (2009).
- Lutsko and Oettel (2021)J. F. Lutsko and M. Oettel, “Reconsidering
power functional theory,” J. Chem. Phys.155, 094901 (2021).
- Moosman and Homsy (1980)S. Moosman and G. M. Homsy, “Evaporating
menisci of wetting fluids,”J Colloid Interface Sci.73, 212 (1980).
- Ajaev (2005)V. S. Ajaev, “Evolution of dry
patches in evaporating liquid films,”Phys.
Rev. E72, 031605
(2005).
- Thieleet al.(2009)U. Thiele, I. Vancea,
A. J. Archer, M. J. Robbins, L. Frastia, A. Stannard, E. Pauliac-Vaujour, C. P. Martin, M. O. Blunt, and P. J. Moriarty, “Modelling approaches to the dewetting of evaporating thin films of
nanoparticlesuspensions,” J. Phys.: Condens. Matter21, 264016 (2009).
- Thiele (2010)U. Thiele, “Thin film
evolution equations from (evaporating) dewetting liquid layers to
epitaxialgrowth,” J. Phys.: Condens. Matter22, 084019 (2010).
- Tóthet al.(2026)G. I. Tóth, D. N. Sibley, A. J. Bokányi-Tóth, D. Tseluiko, and A. J. Archer, “Variational
approach to droplet motion on uneven solid surfaces, including contact line
dynamics and evaporation,” arXiv preprint arXiv:2605.12393 (2026).
- Archer (2009)A. J. Archer, “Dynamical
density functional theory for molecular and colloidal fluids: A microscopic
approach to fluid mechanics,” J. Chem. Phys.130, 014509 (2009).
- Marconi and Tarazona (1999)U. M. B. Marconi and P. Tarazona, “Dynamic density functional theory of fluids,” J. Chem. Phys.110, 8032 (1999).
- Archer and Evans (2004)A. J. Archer and R. Evans, “Dynamical density functional
theory and its application to spinodal decomposition,” J. Chem. Phys.121, 4246 (2004).
- Hansen and McDonald (2013)J.-P. Hansen and I. R. McDonald,Theory of simple
liquids: with applications to soft matter(Academic press, 2013).
- te Vrugt, Löwen, and Wittkowski (2020)M. te Vrugt, H. Löwen,
 and R. Wittkowski, “Classical dynamical density
functional theory: from fundamentals to applications,” Adv. Phys.69, 121 (2020).
- Evans (1979)R. Evans, “The nature of the
liquid-vapour interface and other topics in the statistical mechanics of
non-uniform, classical fluids,” Adv. Phys.28, 143 (1979).
- Stuhlmülleret al.(2018)N. C. X. Stuhlmüller, T. Eckert, D. de Las Heras, and M. Schmidt, “Structural nonequilibrium forces in driven colloidal systems,” Phys. Rev. Lett.121, 098002 (2018).
- Treffenstädt and Schmidt (2020)L. L. Treffenstädt and M. Schmidt, “Memory-induced
motion reversal in brownian liquids,” Soft Matter16, 1518–1526 (2020).
- de Las Heras and Schmidt (2020)D. de Las Heras and M. Schmidt, “Flow and
structure in nonequilibrium brownian many-body systems,” Phys. Rev. Lett.125, 018001 (2020).
- Geigenfeind, de las Heras, and Schmidt (2020)T. Geigenfeind, D. de las
Heras, and M. Schmidt, “Superadiabatic
demixing in nonequilibrium colloids,” Commun. Phys.3, 23 (2020).
- Treffenstädt, Schindler, and Schmidt (2022)L. L. Treffenstädt, T. Schindler, and M. Schmidt, “Dynamic decay
and superadiabatic forces in the van hove dynamics of bulk hard sphere
fluids,” SciPost
Phys.12, 133 (2022).
- de Las Heraset al.(2023)D. de Las Heras, T. Zimmermann, F. Sammüller, S. Hermann, and M. Schmidt, “Perspective:
How to overcome dynamical density functional theory,” J. Phys.: Condens Matter35, 271501 (2023).
- Laurilaet al.(2006)T. Laurila, C. Tong,
S. Majaniemi, and T. Ala-Nissila, “Interface equations for
capillary rise in random environment,” Phys. Rev. E74, 041601 (2006).
- Qian, Wang, and Sheng (2006)T. Qian, X.-P. Wang, and P. Sheng, “A variational approach to moving
contact line hydrodynamics,” J. Fluid Mech.564, 333 (2006).
- Xu, Thiele, and Qian (2015)X. Xu, U. Thiele, and T. Qian, “A variational approach to thin film
hydrodynamics of binary mixtures,” J. Phys.: Condens. Matter27, 085005 (2015).
- Xu, Di, and Doi (2016)X. Xu, Y. Di, and M. Doi, “Variational method for liquids moving on
a substrate,” Phys. Fluids28, 087101
(2016).
- Thiele (2018)U. Thiele, “Recent advances
in and future challenges for mesoscopic hydrodynamic modelling of complex
wetting,”Colloid Surf. A553, 487 (2018).
- Lopes, Thiele, and Hazel (2018)A. v. B. Lopes, U. Thiele, and A. L. Hazel, “On the multiple
solutions of coating and rimming flows on rotating cylinders,” J. Fluid Mech.835, 540 (2018).
- Peschka (2018)D. Peschka, “Variational
approach to dynamic contact angles for thin films,” Phys. Fluids30, 082115 (2018).
- Mitlin (1993)V. S. Mitlin, “Dewetting of
solid surface: Analogy with spinodal decomposition,” J. Colloid Interface Sci.156, 491 (1993).
- Thiele (2011)U. Thiele, “Note on thin
film equations for solutions and suspensions,” Eur. Phys. J. Special Topics197, 213 (2011).
- Ruyer-Quil and Manneville (2002)C. Ruyer-Quil and P. Manneville, “Further
accuracy and convergence results on the modeling of flows down inclined
planes by weighted-residual approximations,” Phys. Fluids14, 170 (2002).
- Benney (1966)D. J. Benney, “Long waves on
liquid films,” J. Math. Phys.45, 150
(1966).
- Zitzet al.(2019)S. Zitz, A. Scagliarini,
S. Maddu, A. A. Darhuber, and J. Harting, “Lattice boltzmann method for thin-liquid-film
hydrodynamics,” Phys. Rev. E100, 033313 (2019).
- Ruyer-Quil and Manneville (2000)C. Ruyer-Quil and P. Manneville, “Improved
modeling of flows down inclined planes,” Eur. Phys. J. B15, 357 (2000).
- Holroyd, Cimpeanu, and Gomes (2024)O. A. Holroyd, R. Cimpeanu, and S. N. Gomes, “Linear quadratic regulation
control for falling liquid films,” SIAM J. Appl. Math.84, 940 (2024).
- Te Vrugtet al.(2024)M. Te Vrugt, L. Topp,
R. Wittkowski, and A. Heuer, “Microscopic derivation of the thin film
equation using the Mori–Zwanzig formalism,” J. Chem. Phys.161, 094904 (2024).
- Anero, Español, and Tarazona (2013)J. G. Anero, P. Español,
 and P. Tarazona, “Functional thermo-dynamics:
a generalization of dynamic density functional theory to non-isothermal
situations,” J.
Chem. Phys.139(2013).
- Wittkowski, Löwen, and Brand (2013)R. Wittkowski, H. Löwen, and H. R. Brand, “Microscopic
approach to entropy production,” J. Phys. A46, 355003 (2013).
- Edwards and Freed (1974)S. F. Edwards and K. F. Freed, “Theory of the
dynamical viscosity of polymer solutions,” J. Chem. Phys.61, 1189 (1974).
- Whittacker (1937)E. T. Whittacker,Analytical
dynamics(Cambridge University Press, 1937).
- Giga, Kirshtein, and Liu (2018)M.-H. Giga, A. Kirshtein, and C. Liu, “Variational modeling and complex
fluids,” Springer Books , 73–113 (2018).
- Krinninger and Schmidt (2019)P. Krinninger and M. Schmidt, “Power
functional theory for active brownian particles: general formulation and
power sum rules,” J Chem. Phys.150, 074112 (2019).
- Hermannet al.(2019)S. Hermann, P. Krinninger,
D. de Las Heras, and M. Schmidt, “Phase coexistence of active brownian
particles,” Phys. Rev. E100, 052604 (2019).
- Liu, Ou-Yang, and Wu (2026)J. Liu, Z.-C. Ou-Yang, and H. Wu, “Entropy-driven initiation and cellular
uptake mediated by viscoelastic cytoskeleton: A kinetic phase diagram from
Onsager variational principle,” arXiv preprint arXiv:2607.12766 (2026).
- Xu (2026)X. Xu, “Onsager-variational
formulation of diffuse-domain methods for computational modeling of
microscale fluid-structure interactions,” arXiv preprint arXiv:2605.13196 (2026).
- Podio-Guidugli and Virga (2023)P. Podio-Guidugli and E. G. Virga, “Analytical thermodynamics,” J. Elast.153, 787 (2023).
- Grmela and Öttinger (1997)M. Grmela and H. C. Öttinger, “Dynamics
and thermodynamics of complex fluids. i. development of a general
formalism,” Phys. Rev. E56, 6620
(1997).
- Grmela (2026)M. Grmela, “Rheological
modeling with GENERIC and with the Onsager principle,” J. Non-Equilib. Thermodyn.51, 151 (2026).
- Lazoet al.(2018)M. J. Lazo, J. Paiva,
J. T. Amaral, and G. S. Frederico, “An action principle for
action-dependent Lagrangians: Toward an action principle to
non-conservative systems,” J. Math. Phys.59, 032902 (2018).
- Gasetet al.(2024)J. Gaset, M. Lainz,
A. Mas, and X. Rivas, “The Herglotz variational principle for
dissipative field theories,” Geometric Mechanics1, 153 (2024).
- Yasudaet al.(2026)K. Yasuda, B. Zheng,
Z. Xiong, Z. Hou, K. Ishimoto, X. Xu, D. Andelman, and S. Komura, “Covariant Onsager and Onsager-Machlup principles for active and
inertial dynamics,” arXiv preprint arXiv:2604.22371 (2026).
- Man and Doi (2017)X. Man and M. Doi, “Vapor-induced motion of
liquid droplets on an inert substrate,” Phys. Rev. Lett.119, 044502 (2017).
- Wu, Man, and Doi (2018)M. Wu, X. Man, and M. Doi, “Multi-ring deposition pattern of drying
droplets,” Langmuir34, 9572
(2018).
- Wuet al.(2019)M. Wu, Y. Di, X. Man, and M. Doi, “Drying droplets with soluble surfactants,” Langmuir35, 14734 (2019).
- Wu, Doi, and Man (2021)M. Wu, M. Doi, and X. Man, “The contact angle of an evaporating
droplet of a binary solution on a super wetting surface,” Soft Matter17, 7932 (2021).
- Yanget al.(2021)X. Yang, Z. Jiang,
P. Lyu, Z. Ding, and X. Man, “Deposition pattern of drying droplets,” Commun. Theor. Phys.73, 047601 (2021).
- Bokányi-Tóthet al.(2026)A. J. Bokányi-Tóth, A. J. Archer, R. Cimpeanu,
H. Bandulasena, G. I. Tóth, and D. Tseluiko, “Liquid bridges between horizontal cylindrical
electrodes,” Submitted to J. Fluid Mech. (2026).

## 


- 


Major funding support from
