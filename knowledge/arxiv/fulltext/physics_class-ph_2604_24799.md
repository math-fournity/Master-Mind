# The Inverse Cube Force Law

**arXiv ID**: 2604.24799v1
**Authors**: John C. Baez
**Published**: 2026-04-26
**Categories**: physics.class-ph, math.HO
**Comments**: 2 pages
**HTML URL**: https://arxiv.org/html/2604.24799v1

## Abstract

Newton's Principia is famous for its investigations of the inverse square force law for gravity. But in this book Newton also did something that remained little-known until fairly recently. He figured out what kind of central force exerted upon a particle can rescale its angular velocity by a constant factor without affecting its radial motion. This turns out to be a force obeying an inverse cube law! Here we discuss this and some other interesting features of the inverse cube force law.

## Full Text

The Inverse Cube Force Law

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- License: arXiv.org perpetual non-exclusive licensearXiv:2604.24799v1 [physics.class-ph] 26 Apr 2026

## The Inverse Cube Force LawJohn C. BaezSchool of Mathematics, University of Edinburgh, James Clerk Maxwell Building, Peter Guthrie Tait Road, Edinburgh, UK EH9 3FDFigure 1.A particle spiraling into the origin in an inverse cube force.

Newton’sPrincipiais famous for its investigations of the inverse square force law for gravity. But in this book Newton also did something that remained little-known until fairly recently[1,5]. He figured out what kind of central force exerted upon a particle can rescale its angular velocity by a constant factor without affecting its radial motion. This turns out to be a force obeying an inversecubelaw.

Given a particle in Euclidean space, acentral forceis a force that points toward or away from the origin and depends only on the particle’s distance from the origin. If the particle’s position at timettis𝐫​(t)∈ℝn\mathbf{r}(t)\in{\mathbb{R}}^{n}and its mass is some numberm>0m>0, we havem​𝐫¨​(t)=F​(r​(t))​𝐫^​(t),m\,\ddot{\mathbf{r}}(t)=F(r(t))\,\hat{\mathbf{r}}(t),

where𝐫^​(t)\hat{\mathbf{r}}(t)is a unit vector pointing outward from the origin at the point𝐫​(t)\mathbf{r}(t). A particle obeying this equation always moves in a plane through the origin, so we can use polar coordinates and write the particle’s position as(r​(t),θ​(t))\bigl(r(t),\theta(t)\bigr). With some calculation one can show the particle’s distance from the origin,r​(t)r(t), obeys(1)m​r¨​(t)=F​(r​(t))+L2/m​r​(t)3.m\ddot{r}(t)=F(r(t))+L^{2}/mr(t)^{3}.

HereL=m​r​(t)2​θ˙​(t)L=mr(t)^{2}\dot{\theta}(t), the particle’sangular momentum, is constant in time. The second term in Equation (1) says that the particle’s distance from the origin changes as if there were an additional force pushing it outward. This is a “fictitious force”, an artifact of working in polar coordinates. It is called thecentrifugal force. And it obeys an inverse cube force law!

This explains Newton’s observation. Let us see why. Suppose that we have two particles moving in two different central forcesF1F_{1}andF2F_{2}, each obeying a version of Equation (1), with the same massmmand the same radial motionr​(t)r(t), but different angular momentaL1L_{1}andL2L_{2}. Then we must haveF1​(r​(t))+L12/m​r​(t)3=F2​(r​(t))+L22/m​r​(t)3.F_{1}(r(t))+L_{1}^{2}/mr(t)^{3}=F_{2}(r(t))+L_{2}^{2}/mr(t)^{3}.

If the particle’s angular velocities are proportional thenL2=k​L1L_{2}=kL_{1}for some constantkk, soF2​(r1​(t))−F1​(r​(t))=(k2−1)​L12/m​r​(t)3.F_{2}(r_{1}(t))-F_{1}(r(t))=(k^{2}-1)L_{1}^{2}/mr(t)^{3}.

This says thatF2F_{2}equalsF1F_{1}plus an additional inverse cube force.

A particle’s motion in an inverse cube force has curious features. First compare Newtonian gravity, which is an attractive inverse square force, sayF​(r)=−c/r2F(r)=-c/r^{2}withc>0c>0. In this case we havem​r¨​(t)=−c/r​(t)2+L2/m​r​(t)3.m\ddot{r}(t)=-c/r(t)^{2}+L^{2}/mr(t)^{3}.

Because1/r31/r^{3}grows faster than1/r21/r^{2}asr↓0r\downarrow 0, as long as the angular momentumLLis nonzero the repulsion of the centrifugal force will beat the attraction of gravity for sufficiently smallrr, and the particle will not fall in to the origin. The same is true for any attractive forceF​(r)=−c/rpF(r)=-c/r^{p}withp<3p<3. But an attractive inverse cube force can overcome the centrifugal force and make a particle fall in to the origin.

In fact there are three qualitatively different possibilities for the motion of a particle in an attractive inverse cube forceF​(r)=−c/r3F(r)=-c/r^{3}, depending on the value ofcc. With work[4]we can solve for1/r1/ras a function ofθ\theta(which is easier than solving forrr). There are three cases depending on the value ofω2=1−c​m/L2,\omega^{2}=1-cm/L^{2},

vaguely analogous to the elliptical, parabolic and hyperbolic orbits of a particle in an inverse square force law:1r​(θ)={A​cos⁡(ω​θ)+B​sin⁡(ω​θ)ifω2>0A+B​θifω=0A​e|ω|​θ+B​e−|ω|​θifω2<0.\frac{1}{r(\theta)}=\left\{\begin{array}[]{lcl}A\cos(\omega\theta)+B\sin(\omega\theta)&\text{if}&\omega^{2}>0\\[3.0pt]
A+B\theta&\text{if}&\omega=0\\[3.0pt]
Ae^{|\omega|\theta}+Be^{-|\omega|\theta}&\text{if}&\omega^{2}<0.\end{array}\right.

The third case occurs when the attractive inverse cube force is strong enough to overcome the centrifugal force:c>L2/mc>L^{2}/m. Then the particle canspiral in to its doom, hitting the origin in a finite amount of time after infinitely many orbits. An example is shown in Figure1.

All three curves are calledCotes spirals, after Roger Cotes’ work on the inverse cube force law, published posthumously in 1722. Cotes seems to have been the first to compute the derivative of the sine function. After Cotes’ death at the age of 33, Newton supposedly said “If he had lived we would have known something”[3].

The subtlety of the inverse cube force law is greatly heightened when we study it using quantum rather than classical mechanics[2]. Here ifccis too large the theory is ill-defined, because there is no reasonable choice of self-adjoint Hamiltonian. Ifccis smaller the theory is well-behaved. But at a certain borderline point it exhibits a remarkable property: spontaneous breaking of scaling symmetry. I hope to discuss this in my next column.

## References
- [1]S. Chandrasekhar,Newton’s Principia for the Common Reader, Oxford U. Press, Oxford, 1995, pp. 183–200.
- [2]D. M. Gitman, I. V. Tyutin and B. L. Voronov, Self-adjoint extensions and spectral analysis in Calogero problem,J. Phys. A43(14) (2010), 145205. Also available atarXiv:0903.5277.
- [3]R. Gowing,Roger Cotes—Natural Philosopher, Cambridge U. Press, Cambridge, 2002.
- [4]N. Grossman,The Sheer Joy of Celestial Mechanics, Birkhäuser, Basel, 1996, p. 34.
- [5]Newton’s theorem of revolving orbits, Wikipedia. Available athttps://en.wikipedia.org/wiki/Newton’s¯\underline{\;\;}theorem¯\underline{\;\;}of¯\underline{\;\;}revolving¯\underline{\;\;}orbits.

## 


- 


Major funding support from
