# A Semiclassical Gaussian Wavepacket Method for Non-Adiabatic Molecular Dynamics

**arXiv ID**: 2607.09592v1
**Authors**: Lorenzo Bocchi, Jia-Xi Zeng, Michele Ceotto
**Published**: 2026-07-10
**Categories**: physics.chem-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.09592v1

## Abstract

We introduce two non-adiabatic semiclassical methods that employ two coupled Gaussian wavepackets, each one traveling on a separate diabatic potential energy surface. The wavepackets take the form of thawed Gaussians and are driven by classical equations of motion which account for the diabatic coupling. The classical equations of motion are derived in one case by enforcing the thawed Gaussian ansatz, while in the other the time-dependent variational principles to the thawed Gaussian ansatz. After a sanity check where both approximations reproduce Rabi oscillations, the methods are applied to two non-adiabatic potential energy scenarios. The first one involves two coupled displaced harmonic oscillators, as in a typical electron transfer reaction. The second one comprises a Morse potential coupled to an upper dissociative state, modeling a photo-dissociation process. In both scenarios, the variational thawed Gaussian approach is quite accurate, while the standard thawed Gaussian one fails to fully capture the non-adiabatic effects. Ultimately, non-adiabatic molecular dynamics is reproduced by means of two classical trajectories without introducing any artificial jump or other ad-hoc non-classical effects.

## Full Text

A Semiclassical Gaussian Wavepacket Method for Non-Adiabatic Molecular Dynamics

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
- License: CC BY-NC-ND 4.0arXiv:2607.09592v1 [physics.chem-ph] 10 Jul 2026

## A Semiclassical Gaussian Wavepacket Method for Non-Adiabatic Molecular
DynamicsLorenzo BocchiDipartimento di Chimica, Università degli Studi di Milano, via Golgi
19, 20133 Milano, ItalyJia-Xi Zengjiaxi.zeng@unimi.itDipartimento di Chimica, Università degli Studi di Milano, via Golgi
19, 20133 Milano, ItalyMichele Ceottomichele.ceotto@unimi.itDipartimento di Chimica, Università degli Studi di Milano, via Golgi
19, 20133 Milano, Italy(July 10, 2026)

## Abstract

We introduce two non-adiabatic semiclassical methods that employ two
coupled Gaussian wavepackets, each one traveling on a separate diabatic
potential energy surface. The wavepackets take the form of thawed
Gaussians and are driven by classical equations of motion which account
for the diabatic coupling. The classical equations of motion are derived
in one case by enforcing the thawed Gaussian ansatz, while in the
other the time-dependent variational principles to the thawed Gaussian
ansatz. After a sanity check where both approximations reproduce Rabi
oscillations, the methods are applied to two non-adiabatic potential
energy scenarios. The first one involves two coupled displaced harmonic
oscillators, as in a typical electron transfer reaction. The second
one comprises a Morse potential coupled to an upper dissociative state,
modeling a photo-dissociation process. In both scenarios, the variational
thawed Gaussian approach is quite accurate, while the standard thawed
Gaussian one fails to fully capture the non-adiabatic effects. Ultimately,
non-adiabatic molecular dynamics is reproduced by means of two classical
trajectories without introducing any artificial jump or otherad-hocnon-classical effects.nonadiabatic, non-adiabatic, semiclassical, quantum dynamics, diabatic

## IIntroduction

Many important processes in nature involve non-adiabatic molecular
events, i.e. they can not be described within the Born-Oppenheimer
framework. Proton-coupled electron transfer reactions,[30]homogeneous and heterogeneous catalysis,[65,57,73,20]photochemical reactions,[62]charge
transport in materials[26]and electron
transfer reactions[76]are just a few
examples of non-adiabatic processes in chemistry, physics and biology.

One can rigorously perform non-adiabatic dynamics and include both
nuclear and electronic quantum effects with exact grid-based methods,[1]as for example by employing multi-configurational time-dependent Hartree
methods,[49]or related methods, such
as variational multi-configurational Gaussian,[74]full multiple spawning,[46]and multi-configurational
Ehrenfest dynamics methods.[64,39,43]Alternatively, to alleviate the computational burden, a series of
mixed quantum-classical methods have been developed since the pioneering
surface hopping idea.[68,31,3,18]Spin-mapping methods[59,45,75]are an example of quantum-classical dynamics. Given the importance
of nuclear quantum effects, even in condensed phase processes,[61,21,44]methods based on classical trajectories and describing non-adiabatic
events have been developed. In this context, one can either employ
the Meyer-Miller Hamiltonian,[50,78,66,12,54,51,17],
a frozen Gaussian basis in conjunction with the time-dependent variational
principle,[40,41],
the phase-space electronic structure theory,[5]the path integral[2,19,6,77]or the Exact Factorization[36,37,28]formulations of non-adiabatic dynamics.

Here we focus on the simplest approach that one can employ for nuclear
quantum non-adiabatic molecular dynamics, which is the one based on
a single classical trajectory per electronic state. In the adiabatic
case, single trajectory approaches[8,7,67,71,4]showed that anharmonicity and quantum effects can be reproduced, at
least to some extent. Single-trajectory Ehrenfest dynamics is an example,[11]but it is mainly limited by the overestimation of the electronic coherence
because all electronic states share the same classical nuclear trajectory
and quantum nuclear effects are not accounted for. Very recently Vanicek’s
group introduced a method which is based on a single trajectory and
does include nuclear quantum effects.[60]The method is an implementation of Heller’s thawed Gaussian wavepacket
propagation,[33,29,69]where the wavepacket is driven by the classical evolution of its components.
In general, thawed Gaussian wavepacket dynamics (TGWD) is rather simple
to implement and it provides a clear interpretation of quantum dynamics,
because classical variables are intuitive, localized in space, and
only the potential values along the trajectory path are needed. In
addition, on-the-fly ab initio implementation is direct, as for many
semiclassical methods.[70,71,9,10,15,14,16,23,24,55]The accuracy of TGWD can be improved by including the third derivative
of the potential, as in the case of the “extended” semiclassical wavepacket
dynamics[72]and the symplectic semiclassical
wavepacket dynamics.[56,53,58]

A less approximated approach but still based on a single trajectory
Gaussian wavepacket propagation is the Variational Thawed Gaussian
Wavepacket Dynamics (VTGWD), which is derived by enforcing the McLachlan
variational principle[42]to the thawed
Gaussian ansatz.[25]Already Heller,[34]and then Heather and Metiu[32]and Karplus and
Coalson[13]derived the equations of motion
for the wavepacket. In comparison to TGWD, VTGWD has the advantage
of being symplectic,[42]energy preserving
and it can qualitatively describe tunneling.[53,52]However, these accuracy improvements come at the cost of evaluating
the expectation values of the potential and its derivatives.

Despite the success of VTGWD in adiabatic scenarios, the extension
of this approach to non-adiabatic cases is still a challenge. In this
work, we tackle this issue by introducing a non-adiabatic method for
nuclear quantum dynamics based on the thawed Gaussian idea. The idea
is to have a wavepacket for each electronic potential energy surface
and have the potential coupling to induce the wavepacket population
to exchange.

The paper is organized as follows. In sectionII, we
present the theoretical framework. The equations of motion of our
non-adiabatic thawed Gaussian wavepacket dynamics (NA-TGWD) are in
subsectionII.1, while the ones of the
non-adiabatic variational thawed Gaussian wavepacket dynamics (NA-VTGWD)
are in subsectionII.2. The results
are presented in SectionIII. In subsectionIII.1we perform a sanity check with a Rabi system. In subsectionIII.2we consider two coupled displaced harmonic oscillators, which describe
an electron-transfer type of reaction or a proton-electron transfer
reaction. In subsectionIII.3we present the results for a photodissociation or a non-adiabatic
unimolecular reaction potential energy profile. A Discussion and Conclusion
section (Sec.IV) concludes the
paper.

## IISemiclassical Wavepacket Non-Adiabatic Methods

We formulate the equivalent of TGWD and VTGWD for the non-adiabatic
case by using the diabatic potential energy surface representation.
Specifically, we consider two coupled electronic states and calculate
the nuclear wavepacket evolution on both surfaces simultaneously with
the addition, with respect to the adiabatic case, that in our non-adiabatic
formulation the wavepackets are coupled. The idea is to reproduce
quantum electronic transitions by allowing the wavepacket shape to
change, without introducing any artificial hops or forcing classical
trajectories to change potential energy surface. Instead, we stick
with Hamilton equations of motion for the wavepacket center positions
and momenta. More specifically, modified Hamilton equations and equations
for the wavepacket widths and phases are derived in order to reproduce
as much as possible electronic transitions, as shown in Subsec.sII.1andII.2.

## II.1A Thawed Gaussian Non-Adiabatic
Method

The quantum nuclear evolution of two wavepackets on two coupled electronic
states in the diabatic framework is described by the set of equations{i​ℏ​∂∂t​ϕ1​(x,t)=−ℏ22​m​∂2∂x2​ϕ1​(x,t)+V11​(x)​ϕ1​(x,t)+V12​(x)​ϕ2​(x,t)i​ℏ​∂∂t​ϕ2​(x,t)=−ℏ22​m​∂2∂x2​ϕ2​(x,t)+V22​(x)​ϕ2​(x,t)+V12​(x)​ϕ1​(x,t)\begin{cases}i\hbar\dfrac{\partial}{\partial t}\phi_{1}(x,t)&=-\dfrac{\hbar^{2}}{2m}\dfrac{\partial^{2}}{\partial x^{2}}\phi_{1}(x,t)+V_{11}(x)\phi_{1}(x,t)\\
&+V_{12}(x)\phi_{2}(x,t)\\
i\hbar\dfrac{\partial}{\partial t}\phi_{2}(x,t)&=-\dfrac{\hbar^{2}}{2m}\dfrac{\partial^{2}}{\partial x^{2}}\phi_{2}(x,t)+V_{22}(x)\phi_{2}(x,t)\\
&+V_{12}(x)\phi_{1}(x,t)\end{cases}(1)

whereV11​(x)V_{11}(x)andV22​(x)V_{22}(x)are the diabatic surfaces,V12​(x)V_{12}(x)is the diabatic coupling, andϕi​(x,t)\phi_{i}\left(x,t\right)is a diabatic
wavepacket. In our semiclassical approach we adopt the thawed Gaussian
ansatzϕ1​(x,t)\displaystyle\phi_{1}(x,t)=(2​α1R​(0)π)1/4​exp⁡[iℏ​S1​(t)+iℏ​φ1​(t)]\displaystyle=\left(\dfrac{2\alpha^{R}_{1}(0)}{\pi}\right)^{1/4}\exp\Big[\dfrac{i}{\hbar}S_{1}(t)+\dfrac{i}{\hbar}\varphi_{1}(t)\Big]×\displaystyle\timesexp⁡[−α1​(t)​(x−q1​(t))2+iℏ​p1​(t)​(x−q1​(t))]\displaystyle\exp\Big[-\alpha_{1}(t)\big(x-q_{1}(t)\big)^{2}+\dfrac{i}{\hbar}p_{1}(t)\big(x-q_{1}(t)\big)\Big](2)ϕ2​(x,t)\displaystyle\phi_{2}(x,t)=(2​α2R​(0)π)1/4​exp⁡[iℏ​S2​(t)+iℏ​φ2​(t)]\displaystyle=\left(\dfrac{2\alpha^{R}_{2}(0)}{\pi}\right)^{1/4}\exp\Big[\dfrac{i}{\hbar}S_{2}(t)+\dfrac{i}{\hbar}\varphi_{2}(t)\Big]×\displaystyle\timesexp⁡[−α2​(t)​(x−q2​(t))2+iℏ​p2​(t)​(x−q2​(t))]\displaystyle\exp\Big[-\alpha_{2}(t)\big(x-q_{2}(t)\big)^{2}+\dfrac{i}{\hbar}p_{2}(t)\big(x-q_{2}(t)\big)\Big](3)

whereSi​(t)=∫0t(pi2​(t′)2​m−Vi​(qi​(t′)))​𝑑t′S_{i}(t)=\int^{t}_{0}\left(\dfrac{p^{2}_{i}(t^{\prime})}{2m}-V_{i}(q_{i}(t^{\prime}))\right)\,dt^{\prime}is the usual classical action. The variablesαi​(t)\alpha_{i}(t)andφi​(t)\varphi_{i}(t)are complex-valued time-dependent quantities whose
equations of motion are to be determined together with the ones for
the wavepacket centerqi​(t)q_{i}\left(t\right)and momentumpi​(t)p_{i}\left(t\right).
The real partαiR​(t)\alpha^{R}_{i}(t)is the width parameter of the wavepacket,
while the imaginary part represents a spatial chirp. The real part
ofφi​(t)\varphi_{i}(t)is a time-dependent phase factor which accounts
for the wavepacket quantum zero-point energy, while the imaginary
part ensures normalization at each time-step. Eq.s (2)
and (3) are exact for constant, linear and harmonic
adiabatic potentials.

To solve Eq.s (1), we substitute Eq.s (2)
and (3) and expand each function of the nuclear
coordinatexxaround the respective wavepacket centerqi​(t)q_{i}\left(t\right).
The coupling termVi​j​(x)​ϕjV_{ij}\left(x\right)\phi_{j}(x,t)\left(x,t\right)is rewritten asVi​j​(x)​(ϕj​(x,t)/ϕi​(x,t))​ϕi​(x,t)V_{ij}\left(x\right)\left(\phi_{j}\left(x,t\right)/\phi_{i}\left(x,t\right)\right)\phi_{i}\left(x,t\right)and both the coupling potential and the ratio(ϕj​(x,t)/ϕi​(x,t))\left(\phi_{j}\left(x,t\right)/\phi_{i}\left(x,t\right)\right)are expanded. The resulting coupled equations are solved by equating
the coefficients of the same polynomial(x−qi​(t))n\big(x-q_{i}(t)\big)^{n}order. The entire procedure is reported in detail in Sec. IA of the
supplementary material. The resulting equations of motion for each
parameter driving the NA-TGWD areα˙i​(t)\displaystyle\dot{\alpha}_{i}(t)=−2​i​ℏmαi2(t)+i2​ℏ[Vi​i′′(qi)+Vi​j(qi)(ϕ~jϕ~i)′′\displaystyle=-\dfrac{2i\hbar}{m}\alpha^{2}_{i}(t)+\dfrac{i}{2\hbar}\left[V^{\prime\prime}_{ii}(q_{i})+V_{ij}(q_{i})\Big(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\Big)^{\prime\prime}\right.+2Vi​j′(qi)(ϕ~jϕ~i)′+Vi​j′′(qi)(ϕ~jϕ~i)],\displaystyle\left.+2V^{\prime}_{ij}(q_{i})\Big(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\Big)^{\prime}+V^{\prime\prime}_{ij}(q_{i})\Big(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\Big)\right],(4)

for the wavepacket width,q˙i​(t)\displaystyle\dot{q}_{i}(t)=pi​(t)m+12​ℏ​αiR​(t)[Vi​j(qi(t))Im(ϕ~jϕ~i)′\displaystyle=\dfrac{p_{i}(t)}{m}+\dfrac{1}{2\hbar\alpha^{R}_{i}(t)}\left[V_{ij}(q_{i}(t))\>\text{Im}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)^{\prime}\right.+Vi​j′(qi(t))Im(ϕ~jϕ~i)]\displaystyle\left.+V^{\prime}_{ij}(q_{i}(t))\>\text{Im}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)\right](5)p˙i​(t)\displaystyle\dot{p}_{i}(t)=−Vi​i′​(t)−[Vi​j​(qi​(t))​Re​(ϕ~jϕ~i)′+Vi​j′​(qi​(t))​Re​(ϕ~jϕ~i)]\displaystyle=-V^{\prime}_{ii}(t)-\left[V_{ij}(q_{i}(t))\text{Re}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)^{\prime}+V^{\prime}_{ij}(q_{i}(t))\text{Re}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)\right]−αiI​(t)αiR​(t)​[Vi​j​(qi​(t))​Re​(ϕ~jϕ~i)′+Vi​j′​(qi​(t))​Im​(ϕ~jϕ~i)],\displaystyle-\dfrac{\alpha^{I}_{i}(t)}{\alpha^{R}_{i}(t)}\left[V_{ij}(q_{i}(t))\text{Re}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)^{\prime}+V^{\prime}_{ij}(q_{i}(t))\text{Im}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)\right],(6)

for determining the wavepacket center phase space evolution, andφ˙i​(t)\displaystyle\dot{\varphi}_{i}(t)=−ℏ2m​αi​(t)−Vi​j​(qi​(t))​ϕ~jϕ~i\displaystyle=-\dfrac{\hbar^{2}}{m}\alpha_{i}(t)-V_{ij}(q_{i}(t))\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}+\displaystyle+pi​(t)2​ℏ​αiR​(t)​[Vi​j​(qi​(t))​Im​(ϕ~jϕ~i)′+Vi​j′​(qi​(t))​Im​(ϕ~jϕ~i)]\displaystyle\dfrac{p_{i}(t)}{2\hbar\alpha^{R}_{i}(t)}\left[V_{ij}(q_{i}(t))\text{Im}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)^{\prime}+V^{\prime}_{ij}(q_{i}(t))\text{Im}\left(\dfrac{\tilde{\phi}_{j}}{\tilde{\phi}_{i}}\right)\right](7)

for the wavepacket phase. In Eq.s (4), (5),
(6) and (7)ϕ~k=ϕk​(x=qi​(t),t)\tilde{\phi}_{k}=\phi_{k}\left(x=q_{i}\left(t\right),t\right)whereqi​(t)q_{i}\left(t\right)is the classical trajectory position
of theii-th diabatic state. Also,Re​(ϕj/ϕi)\text{Re}\left(\phi_{j}/\phi_{i}\right)andαiR​(t)\alpha^{R}_{i}(t)are the real part, andIm​(ϕj/ϕi)\text{Im}\left(\phi_{j}/\phi_{i}\right)andαiI​(t)\alpha^{I}_{i}(t)the imaginary part of the respective quantities.
Of course, we recover the original adiabatic thawed Gaussian equations
of motion when we takei=ji=jandV12=0V_{12}=0in all the equations
(4)-(7). In other words, the non-adiabatic
motion is composed of additive terms: One is the same as in the single
surface adiabatic case, while the others account for the non-adiabatic
coupling. Unfortunately, Eq.s (4)-(7)
do not conserve the norm,N​(t)=∫−∞+∞(|ϕ1​(x,t)|2+|ϕ2​(x,t)|2)​𝑑xN\left(t\right)=\int^{+\infty}_{-\infty}\left(|\phi_{1}\left(x,t\right)|^{2}+|\phi_{2}\left(x,t\right)|^{2}\right)dx,
under time-evolution. This is an important limitation and we provide
a proof in Sec. I B of the supplementary material.

A more accurate single trajectory Gaussian wavepacket method is the
VTGWD, as anticipated in the Introduction. VTGWD is more accurate
because the equations of motion are obtained from the time-dependent
variational principle. This approach guarantees that at each time-step
each wavepacket variable is best fitted to the solution of the Schrödinger
equation. One can prove, besides being more accurate, that VTGWD is
symplectic, it exactly conserves energy and norm, and it is time-reversible.

## II.2A Variational Gaussian Non-Adiabatic
Method

The application of the McLachlan time-dependent variational principle[42,41,13]to the set of Eq.s (1) yields{δ​∫−∞+∞𝑑x​|i​ℏ​∂tϕ1−(T^​ϕ1+V11​ϕ1+V12​ϕ2)|2=0δ​∫−∞+∞𝑑x​|i​ℏ​∂tϕ2−(T^​ϕ2+V22​ϕ2+V12​ϕ1)|2=0\begin{cases}\delta\int^{+\infty}_{-\infty}dx\,\left|i\hbar\partial_{t}\phi_{1}-(\hat{T}\phi_{1}+V_{11}\phi_{1}+V_{12}\phi_{2})\right|^{2}&=0\\
\delta\int^{+\infty}_{-\infty}dx\,\left|i\hbar\partial_{t}\phi_{2}-(\hat{T}\phi_{2}+V_{22}\phi_{2}+V_{12}\phi_{1})\right|^{2}&=0\end{cases}(8)

By introducing the collective variableΘi≡(qi​(t),pi​(t),αi​(t),φi​(t))=(θi​1,…,θi​4)\varTheta_{i}\equiv\left(q_{i}\left(t\right),p_{i}\left(t\right),\alpha_{i}\left(t\right),\varphi_{i}\left(t\right)\right)=\left(\theta_{i1},...,\theta_{i4}\right),
the first set of Eq.s (8) is equivalent
to∫−∞+∞𝑑x​∂∂θ˙1​j∗​|i​ℏ​∂tϕ1−(T^​ϕ1+V11​ϕ1+V12​ϕ2)|2\displaystyle\int^{+\infty}_{-\infty}dx\,\frac{\partial}{\partial\dot{\theta}^{*}_{1j}}\left|i\hbar\partial_{t}\phi_{1}-(\hat{T}\phi_{1}+V_{11}\phi_{1}+V_{12}\phi_{2})\right|^{2}=\displaystyle=−i​ℏ​∫𝑑x​(∂ϕ1∂θ1​j)∗​[(i​ℏ​∂t−T^+V11)​ϕ1+V12​ϕ2]\displaystyle-i\hbar\int dx\left(\frac{\partial\phi_{1}}{\partial\theta_{1j}}\right)^{*}\left[\left(i\hbar\partial_{t}-\hat{T}+V_{11}\right)\phi_{1}+V_{12}\phi_{2}\right]=0\displaystyle=0(9)

and a similar one is valid for the second set. This is described in
details in Sec. II A of the supplementary material. The single terms
in Eq. (9) can be evaluated as shown in
Sec. II B, II C and II D of the supplementary material. Setting up
and solving the systems of equations obtained from (9)
and using the ansatz of Eq.s (2) and (3)
where the classical actionSi​(t)S_{i}\left(t\right)has been incorporated
into the corresponding phaseφi​(t)\varphi_{i}\left(t\right), yields
the following equations of motion for the NA-VTGWDq˙1=p1m+Im​(C1(1))2​ℏ​α1R\dot{q}_{1}=\frac{p_{1}}{m}+\frac{\text{Im}(C^{(1)}_{1})}{2\hbar\alpha^{R}_{1}}(10)p˙1=−Re​(C1(1))−Im​(C1(1))​α1Iα1R\dot{p}_{1}=-\text{Re}(C^{(1)}_{1})-\text{Im}(C^{(1)}_{1})\frac{\alpha^{I}_{1}}{\alpha^{R}_{1}}(11)α˙1\displaystyle\dot{\alpha}_{1}=\displaystyle=−2​i​ℏm​α12+i2​ℏ​(2​α1Rπ)1/2​⟨V11′′⟩11​G\displaystyle-\frac{2i\hbar}{m}\alpha^{2}_{1}+\frac{i}{2\hbar}\left(\frac{2\alpha^{R}_{1}}{\pi}\right)^{1/2}\langle V^{\prime\prime}_{11}\rangle_{11G}(12a)+i2​ℏ​16​(α1R)2P1​(t)​[⟨ξ12​V12⟩12−⟨V12⟩124​α1R]\displaystyle+\frac{i}{2\hbar}\frac{16(\alpha^{R}_{1})^{2}}{P_{1}(t)}\left[\langle\xi^{2}_{1}V_{12}\rangle_{12}-\frac{\langle V_{12}\rangle_{12}}{4\alpha^{R}_{1}}\right](12b)φ˙1\displaystyle\dot{\varphi}_{1}=\displaystyle=p122​m−(2​α1Rπ)1/2​⟨V11⟩11​G−ℏ2m​α1\displaystyle\frac{p^{2}_{1}}{2m}-\left(\frac{2\alpha^{R}_{1}}{\pi}\right)^{1/2}\langle V_{11}\rangle_{11G}-\frac{\hbar^{2}}{m}\alpha_{1}(13a)+(2​α1Rπ)1/2​⟨V11′′⟩11​G8​α1R\displaystyle+\left(\frac{2\alpha^{R}_{1}}{\pi}\right)^{1/2}\frac{\langle V^{\prime\prime}_{11}\rangle_{11G}}{8\alpha^{R}_{1}}(13b)+p1​Im​(C1(1))2​ℏ​α1R\displaystyle+\frac{p_{1}\text{Im}(C^{(1)}_{1})}{2\hbar\alpha^{R}_{1}}(13c)+1P1​(t)​[−32​⟨V12⟩12+2​α1R​⟨ξ12​V12⟩12]\displaystyle+\frac{1}{P_{1}(t)}\left[-\frac{3}{2}\langle V_{12}\rangle_{12}+2\alpha^{R}_{1}\langle\xi^{2}_{1}V_{12}\rangle_{12}\right](13d)

where we omitted the time for each variable, andC1(1)\displaystyle C^{(1)}_{1}=(2​α1Rπ)1/2​⟨V11′⟩11​G\displaystyle=\left(\frac{2\alpha^{R}_{1}}{\pi}\right)^{1/2}\langle V^{\prime}_{11}\rangle_{11G}(14a)+4​α1RP1​(t)​{⟨V12′⟩122​G12(2)+[G12(1)2​G12(2)−q1]​⟨V12⟩12}\displaystyle+\frac{4\alpha^{R}_{1}}{P_{1}(t)}\left\{\frac{\langle V^{\prime}_{12}\rangle_{12}}{2G^{(2)}_{12}}+\left[\frac{G^{(1)}_{12}}{2G^{(2)}_{12}}-q_{1}\right]\langle V_{12}\rangle_{12}\right\}(14b)⟨V⟩11′′11​G=∫−∞+∞V(x)11′′e−2α1R(t)(x−q1(t))2dx\langle V{}^{\prime\prime}_{11}\rangle_{11G}=\int^{+\infty}_{-\infty}V{}^{\prime\prime}_{11}(x)e^{-2\alpha^{R}_{1}(t)\left(x-q_{1}\left(t\right)\right){}^{2}}dx(15)⟨V12n⟩12=∫−∞+∞V12n​(x)​ϕ1∗​(x,t)​ϕ2​(x,t)​𝑑x\langle V^{n}_{12}\rangle_{12}=\int^{+\infty}_{-\infty}V^{n}_{12}(x)\phi^{*}_{1}(x,t)\phi_{2}(x,t)\>dx(16)⟨ξ12​V12⟩12\displaystyle\langle\xi^{2}_{1}V_{12}\rangle_{12}=⟨V12′′⟩124​(G12(2))2+⟨V12′⟩122​(G12(2))2​[G12(1)−2​q1​G12(2)]\displaystyle=\frac{\langle V^{\prime\prime}_{12}\rangle_{12}}{4(G^{(2)}_{12})^{2}}+\frac{\langle V^{\prime}_{12}\rangle_{12}}{2(G^{(2)}_{12})^{2}}\left[G^{(1)}_{12}-2q_{1}G^{(2)}_{12}\right](17a)+[(G12(1)2​G12(2)−q1)2+12​G12(2)]​⟨V12⟩12\displaystyle+\left[\left(\frac{G^{(1)}_{12}}{2G^{(2)}_{12}}-q_{1}\right)^{2}+\frac{1}{2G^{(2)}_{12}}\right]\langle V_{12}\rangle_{12}(17b)P1​(t)=∫−∞+∞|ϕ1​(x,t)|2​𝑑x=(α1R​(0)α1R​(t))1/2​e−2ℏ​φ11I​(t)P_{1}(t)=\int^{+\infty}_{-\infty}|\phi_{1}(x,t)|^{2}dx=\left(\frac{\alpha^{R}_{1}(0)}{\alpha^{R}_{1}(t)}\right)^{1/2}e^{-\frac{2}{\hbar}\varphi^{I}_{11}(t)}(18)G12(1)=2​(α1∗​q1+α2​q2)+iℏ​(p2−p1)G^{(1)}_{12}=2(\alpha^{*}_{1}q_{1}+\alpha_{2}q_{2})+\frac{i}{\hbar}(p_{2}-p_{1})(19)G12(2)\displaystyle G^{(2)}_{12}=α1∗+α2\displaystyle=\alpha^{*}_{1}+\alpha_{2}(20)G12(0)=−(α1∗​q12+α2​q22)+iℏ​(p1​q1−p2​q2)+iℏ​(φ2−φ1∗)G^{(0)}_{12}=-(\alpha^{*}_{1}q^{2}_{1}+\alpha_{2}q^{2}_{2})+\frac{i}{\hbar}(p_{1}q_{1}-p_{2}q_{2})+\frac{i}{\hbar}(\varphi_{2}-\varphi^{*}_{1})(21)

Eq.s (10)-(13d) provide some interesting
physical insights on how the non-adiabatic processes can be reproduced
with a pair of coupled classical trajectories and by also taking into
account quantum nuclear delocalization. Specifically, Eq. (10)
for the position evolution is composed, as in the thawed Gaussian
case, of the usual adiabatic velocity plus a “frictional” contribution
in Eq. (14b) which accounts for the diabatic coupling.
Similarly, for the momentum evolution in Eq. (11), the
term in Eq. (14a) is the force averaged over the wavepacket
distribution, and the other term in Eq. (14b) describes
the non-adiabatic effects. The wavepacket width parameter is also
evolving as a direct sum of an adiabatic and non-adiabatic term. The
adiabatic one is given by Eq. (12a) and the non-adiabatic
one by Eq. (12b). Regarding the wavepacket phase in Eq.s
(13a)-(13d), we recognize the Lagrangian
in Eq. (13a) plus a term which depends on the widthα1​(t)\alpha_{1}\left(t\right)evolution. The terms in line (13a)
and line (13b) are the same as in the adiabatic case.
An interesting term is the one on line (13b), which
reproduces the wavepacket quantum delocalization. The non-adiabatic
phaseφ1​(t)\varphi_{1}\left(t\right)contribution is given by lines
(13c) and (13d). Interestingly, line (13c)
takes the form ofp1p_{1}times the non-adiabatic velocity contribution,
while line (13d) represents the coupling potential⟨V12⟩12\left\langle V_{12}\right\rangle_{12}between the two wavepackets and its quantum delocalization⟨ξ12​V12⟩12\langle\xi^{2}_{1}V_{12}\rangle_{12}.
From these observations we conclude that the termC1(1)C^{(1)}_{1}is
pivotal for non-adiabatic coupling and it is composed of a real part,
the quantum delocalization in line (14a), and an imaginary
part, the non-adiabatic coupling in line (14b). In conclusion,
as in NA-TGWD, the non-adiabatic motion in NA-VTGWD is composed of
additive terms which are either adiabatic, i.e. the same as in the
single surface case, or non-adiabatic. Within this formulation, one
can also appreciate and control the amount of non-adiabaticity.

In Sec. II E of the supplementary material we look at the norm conservation,
as in the thawed Gaussian case, and prove that the norm is always
conserved for NA-VTGWD of Eq.s (10)-(20).

## IIIResults

We start our simulations with a sanity check of the two methods and
reproduce Rabi oscillations. Then, we move to more realistic scenarios
and simulate an electron transfer and a photodissociation population
inversion.

## III.1Rabi oscillations

In the Rabi system, both diagonal and off-diagonal diabatic potential
terms are constant. The potential terms in Eq.s (4,5,6,7) for NA-TGWD and
in Eq.s (10,11,12a,12b,13a,13b,13c,13d)
for NA-VTGWD can be calculated analytically. Only the time-evolution
is performed numerically using a fourth-order Runge-Kutta algorithm.
We are aware that better algorithms are available for TGWD and especially
for VTGWD,[52]however for our purposes
we found the standard Runge-Kutta algorithm to be accurate enough.
The exact results are obtained by solving Eq.s (1) using the
split-operator quantum time-evolution[22]of the
same initial Gaussian wavepackets employed for NA-TGWD and NA-VTGWD.
Specifically, the Rabi model potential isV=(2.01.01.01.0)V=\begin{pmatrix}2.0&1.0\\
1.0&1.0\end{pmatrix}(22)

and the wavepackets are evolving on completely flat potentials which
are coupled to each other by a constant coupling. In this case the
potential elements for the wavepacket time-evolution reduce to the
following:⟨Vi​i⟩i​i​G\displaystyle\langle V_{ii}\rangle_{iiG}=Vi​i​(π2​αiR​(t))1/2\displaystyle=V_{ii}\left(\frac{\pi}{2\alpha^{R}_{i}(t)}\right)^{1/2}(23)⟨V12⟩12\displaystyle\langle V_{12}\rangle_{12}=V12​(4​α1R​(0)​α2R​(0)(G12(2))2)1/4​exp⁡[(G12(1))24​G12(2)+G12(0)]\displaystyle=V_{12}\left(\frac{4\alpha^{R}_{1}(0)\alpha^{R}_{2}(0)}{(G^{(2)}_{12})^{2}}\right)^{1/4}\exp\left[\frac{(G^{(1)}_{12})^{2}}{4G^{(2)}_{12}}+G^{(0)}_{12}\right](24)

The simulation was performed on a spatial grid ranging fromxmin=−20.0x_{\text{min}}=-20.0a.u. toxmax=20.0x_{\text{max}}=20.0a.u. usingNg=1024N_{g}=1024grid points.
The temporal evolution was propagated for a total time of10.010.0a.u., using a time-step ofd​t=0.01dt=0.01a.u. (yielding 1000 total steps).
The masses are set tom=1.0m=1.0a.u.. Electronic states are initialized
with identical Gaussian wavepackets, i.e. the same shape and initial
population. The initial populationPi​(0)P_{i}\left(0\right)is specified
for each wavepacket and the imaginary part of the initial phase is
determined by inverting the population definition,Pi​(0)=exp​[−2​φiI​(0)]P_{i}\left(0\right)=\text{exp}\left[-2\varphi^{I}_{i}\left(0\right)\right].
In all our simulations, the real part of the initial phase is set
to zero.Figure 1:Wavepacket heatmaps for the probability
time-evolution for the Rabi system of Eq. (22). Left
for the upperV11V_{11}electronic state. Right for the lowerV22V_{22}one. Bottom panel is the exact quantum evolution, middle one is NA-VTGWD,
while upper panel is for NA-TGWD approximation.Figure 2:Wavepacket populations. Dashed lines
are for the exact split-operator wavepacket propagation. Thick solid
lines are for NA-VTGWD method, while thin solid lines for NA-TGWD
approximation. Inset shows the accuracy of the methods.

Fig. (1) and Fig. (2)
show respectively the wavepacket density heatmaps and the time-dependent
diabatic state populations. In both cases, NA-TGWD and NA-VTGWD simulate
the exact dynamics, and Rabi oscillations are exactly reproduced in
Fig. (2). We believe that the very small
deviations that one can appreciate only in the zooming panel of Fig.
(2) are due to the numerical algorithm integration,
which is confirmed to be accurate enough for our purpose.

As a second sanity check, we consider two coupled harmonic electronic
states where two wavepackets are oscillating with opposite phases,
i.e. the wavepacket on one surface is traveling in the opposite direction
to the one on the other surface. The two states are identical, as
are the potential energy surfaces. Thus, if the numerical integration
is accurate, the population is invariant with respect to the time-evolution.
Also in this case the analytical solution is accurately reproduced
both by NA-TGWD and NA-VTGWD, as reported in Fig. S1 and Fig. S2,
where the initial population is equally distributed between the two
states.

After checking that both methods accurately reproduce basic non-adiabatic
dynamics, we can proceed to test them on more complex potential energy
profiles.

## III.2Electron transfer type of reactions

A more challenging system for non-adiabatic molecular dynamics is
that one reported in Fig. (3) by light
and dark gray lines. These types of diabatic potentials reproduce,
at least locally, the shape of a typical electronic structure crossing
and they serve as model potentials for electron-transfer reactions.
Specifically, the potential energy surface is given by(12​m​ω2​(x−x11eq)2+2.0C​e−D​(x−x12eq)2C​e−D​(x−x12eq)212​m​ω2​(x−x22eq)2)\begin{pmatrix}\dfrac{1}{2}m\omega^{2}(x-x^{\text{eq}}_{11})^{2}+2.0&Ce^{-D(x-x^{\text{eq}}_{12})^{2}}\\[8.0pt]
Ce^{-D(x-x^{\text{eq}}_{12})^{2}}&\dfrac{1}{2}m\omega^{2}(x-x^{\text{eq}}_{22})^{2}\end{pmatrix}(25)

where we set the mass tom=1.0m=1.0a.u. and the harmonic frequency
toω=0.5\omega=0.5a.u.. The equilibrium positions are located atx11eq=−2.0x^{\text{eq}}_{11}=-2.0a.u. for the upper state andx22eq=2.0x^{\text{eq}}_{22}=2.0a.u. for the
lower state. TheV12V_{12}term is given by a Gaussian-type coupling
centered atx12eq=−2.0x^{\text{eq}}_{12}=-2.0a.u.. We intentionally placed
the coupling at the minimum of the upper potential to have the wavepackets
interacting from the very beginning of the dynamics. We choose the
coupling constant to beC=1.0C=1.0a.u. andD=0.888D=0.888a.u.. The wavepacket
initial positions areq1​(0)=−5.0​a.u.q_{1}\left(0\right)=-5.0\>\text{a.u.}andq2​(0)=0.0​a.u.q_{2}\left(0\right)=0.0\>\text{a.u.}, the initial momenta are both
zero, the complex Gaussian widths are the same for both wavepackets,
withαi​(t)=(0.250,0.000)​a.u.\alpha_{i}\left(t\right)=\left(0.250,0.000\right)\>\text{a.u.},
and the initial populations are respectively 0.999 and 0.001. The
empty state population is not exactly zero to avoid numerical issues
in the coupling term calculation. The wavepackets are evolved with
a time-step of 0.01 a.u. for a total of 1000 steps. The split-operator
simulation is performed within a grid span of±20.0\pm 20.0a.u. sampled
by 1024 equally spaced grid-points and with a Gaussian wavepacket
width parameter equal to that of the initial thawed Gaussian wavepackets
for both surfaces.Figure 3:Diabatic wavepackets time-evolution.
Gray for the potential terms, blue for the upperV11V_{11}state wavepacket
and orange for the lowerV22V_{22}state one. Colored solid lines
for NA-VTGWD, and colored dashed lines for the exact split-operator
quantum time evolution.

Fig. (3) reports four snapshots of the
wavepacket time-evolution and the diabatic potential terms described
above as a reference. NA-VTGWD is reported with colored solid lines:
Blue for the upper state wavepacket and orange for the lower state
one. The exact split-operator wavepacket is reported in Fig. (3)
with the same color code but using dashed lines. These snapshots allow
us to appreciate how NA-VTGWD fits the shape of the exact wavepacket
with a Gaussian one at each time-step.Figure 4:Wavepacket heatmaps. Left for the upperV11V_{11}electronic state. Right for the lowerV22V_{22}one. Bottom
panel is the exact quantum evolution, middle one is NA-VTGWD, while
upper panel is for NA-TGWD approximation.

Fig. (4) reports a heatmap representation
of the wavepacket dynamics. In this way one can appreciate the accuracy
of each method at each time-step, as well as its ability to reproduce
quantum delocalization. While NA-TGWD completely misses the non-adiabatic
effects, as reported on the upper panels of Fig. (4),
the NA-VTGWD results in the middle panels (left panel for the upper
state and right one for the lower state) mimic quite well the exact
split-operator maps of the bottom panels. What NA-VTGWD can not capture
is the interference pattern generated by the wavepacket splitting
on the same potential energy surface. This is expected since the NA-VTGWD
ansatz is forced to always be a single Gaussian wavepacket. However,
since the wavepacket splitting within the same surface is limited,
the single Gaussian ansatz effectively handles this quantum nuclear
delocalization.

To quantify the accuracy of both methods we report in Fig. (5)
the population of each electronic state for each time-step.Figure 5:Wavepacket populations. Dashed lines
are for the exact split-operator wavepacket propagation. Thick solid
lines are for NA-VTGWD method, while thin solid lines for NA-TGWD
approximation.

Specifically, the thin black and red lines report the population
calculated by the NA-TGWD method. As anticipated by the heatmaps in
Fig. (4), in this case there is no population
exchange despite the local diabatic coupling. Instead, the thick red
and black lines show the population inversion between the electronic
states for the NA-VTGWD method, which mimics quite well the exact
populations reported by colored dashed lines.

## III.3Photodissociation
reaction potential energy profile

We now consider a potential energy profile which reproduces a photodissociation-type
reaction, where a ground state is photoexcited to an unbound upper
electronic state and the wavepacket decays into a dissociative configuration.
The potential is given by(V11​(x)C​e−D​(x−x12eq)2C​e−D​(x−x12eq)2E​e−F​(x−x22eq)+0.5)\begin{pmatrix}V_{11}(x)&Ce^{-D(x-x^{\text{eq}}_{12})^{2}}\\[8.0pt]
Ce^{-D(x-x^{\text{eq}}_{12})^{2}}&Ee^{-F(x-x^{\text{eq}}_{22})}+0.5\end{pmatrix}(26)

whereV11​(x)V_{11}(x)represents the bound Morse potentialV11​(x)=De​(1−exp​[−b​(x−x11e​q)])2V_{11}\left(x\right)=D_{e}\left(1-\text{exp}\left[-b\left(x-x^{eq}_{11}\right)\right]\right)^{2}.
We present two different cases: A deep Morse potential, with parametersDe=15.0D_{e}=15.0a.u. andb=0.091287b=0.091287a.u., and a shallow Morse potential,
withDe=4.0D_{e}=4.0a.u. andb=0.17678b=0.17678a.u.. In both cases we choosex11eq=−2.0x^{\text{eq}}_{11}=-2.0a.u.. The dissociative potential parameters
areE=0.1E=0.1a.u.,F=0.4F=0.4a.u., andx22eq=8.0x^{\text{eq}}_{22}=8.0a.u..
The coupling potential parameters areC=1.5C=1.5a.u.,D=0.888D=0.888a.u.
in both cases, and the coupling is centered atx12eq=2.195​a.u.x^{\text{eq}}_{12}=2.195\;\text{a.u.}for the deep Morse case, andx12eq=2.79​a.u.x^{\text{eq}}_{12}=2.79\;\text{a.u.}for the shallow Morse case. The split-operator simulation is performed
starting with a Gaussian wavepacket over a grid extension of±40.0\pm 40.0a.u. with 2048 equally spaced grid-points, and the wavepacket evolution
employs a time-step of 0.01 a.u. for a total of 1000 steps. The initial
Gaussian width is set atαi​(0)=(0.250,0.000)​a.u.\alpha_{i}\left(0\right)=\left(0.250,0.000\right)\>\text{a.u.}for all wavepackets. The photoexcited wavepacket, with a population
of 0.999, starts atq2​(0)=−2.00​a.u.q_{2}\left(0\right)=-2.00\>\text{a.u.}with
an initial momentump2​(0)=0.0​a.u.p_{2}\left(0\right)=0.0\>\text{a.u.}, and it
has enough initial energy to dissociate along the non-adiabatic path,
i.e. along the Morse potential profile, only for the shallow Morse
case. The bound Morse state wavepacket has a very small initial population
of 0.001 and in both cases it is initialized such that it crosses
the coupling region at the same time as the other wavepacket. Specifically,
for the deep Morse case it starts at the phase space pointq1​(0)=−5.00​a.u.q_{1}\left(0\right)=-5.00\>\text{a.u.}andp1​(0)=3.00​a.u.p_{1}\left(0\right)=3.00\>\text{a.u.}, while for the shallow
Morse case it starts atq1​(0)=−5.14​a.u.q_{1}\left(0\right)=-5.14\>\text{a.u.}andp1​(0)=2.74​a.u.p_{1}\left(0\right)=2.74\>\text{a.u.}Figure 6:Diabatic wavepackets time-evolution for
the deep Morse potential. Left axis for the probability density units
and right axis for the Hartree potential energy units. Gray for the
potential terms, blue for the lowerV11V_{11}state wavepacket and
orange for the upper dissociativeV22V_{22}state one. Colored solid
lines for NA-VTGWD, and colored dashed lines for the exact split-operator
quantum time evolution.

We first investigate the dynamics of the deep Morse case. Fig. (6)
shows the snapshots of the wavepacket dynamics, as in Fig. (3).
The wavepacket is initially placed in the dissociative potential,
a regime where NA-VTGWD is highly accurate, as confirmed by the comparison
between the colored solid and dashed lines in Fig. (6).
Importantly, this accuracy is preserved even after the wavepacket
crosses the non-adiabatic region, where most of the dissociative state
population is transferred to the bound Morse potential state.Figure 7:Wavepacket heatmaps for the deep Morse
potential. Left for the lowerV11V_{11}electronic state. Right for
the upper dissociativeV22V_{22}one. Bottom panel is the exact quantum
evolution, middle one is NA-VTGWD, while upper panel is for NA-TGWD
approximation.

A more comprehensive view is provided by the heatmaps in Fig. (7),
where the dissociative potential population density is reported in
orange and the Morse one in blue. Once again, NA-VTGWD performs better
than NA-TGWD, which partially reproduces the population transfer.
NA-VTGWD is accurate throughout the entire dynamics. This is even
more evident when looking at the populations of Fig. (11),
where NA-VTGWD is almost exact, while NA-TGWD fails to fully capture
the transfer and is not able to recover the correct asymptotic population.
For a better understanding of the differences between the two methods,
we report in Fig.s S3 and S4 of the Supplementary Material the phase
space trajectories respectively for the NA-TGWD and the NA-VTGWD cases.
These phase space plots suggest that the variational motion trajectory
is smoother than the NA-TGWD case.Figure 8:Diabatic populations time evolution
for the deep Morse potential.Figure 9:Diabatic wavepackets time-evolution for the
shallow Morse potential case (see units on the right axis). Gray for
the potential terms, blue for the lowerV11V_{11}state wavepacket
and orange for the upper dissociativeV22V_{22}state one. Colored
solid lines for NA-VTGWD, and colored dashed lines for the exact split-operator
quantum time evolution.

We now turn to the shallow Morse potential case, where the performance
difference between the two methods becomes even more striking. Fig.
(9) shows the wavepacket evolution for the variational
method. The solid NA-VTGWD lines are barely distinguishable from the
dashed ones corresponding to the exact split-operator evolution.Figure 10:Wavepacket heatmaps for the shallow Morse
potential case. Left for the lowerV11V_{11}electronic state. Right
for the upper dissociativeV22V_{22}one. Bottom panel is the exact
quantum evolution, middle one is NA-VTGWD, while upper panel is for
NA-TGWD approximation.

This accuracy is reflected in the heatmaps of Fig. (10).
In this case, the NA-TGWD approach fails completely to capture the
population transfer. This is due to the fact that from the very beginning
of the dynamics, the NA-TGWD wavepacket expansion is too localized
to contribute to the coupling between the wavepackets. Consequently,
the NA-TGWD evolution proceeds essentially as uncoupled adiabatic
dynamics.Figure 11:Diabatic populations time evolution for
the shallow Morse potential case.

These observations are futher confirmed by the population transfer
plot in Fig. (11), where the variational approach
is very accurate and the local NA-TGWD one completely misses the population
transfer. However, we suggest that NA-VTGWD accurately captures the
population inversion between the two electronic states in the cases
presented above because these types of photodissociation processes
involve only a single passage through the non-adiabatic coupling region.

## IVDiscussion and Conclusions

A non-adiabatic semiclassical method is introduced and tested on model
diabatic potentials. The method has the advantage of being described
by a pair of coupled classical trajectories on separated surfaces,
i.e. classical trajectories follow classical mechanics and are not
forced to jump. This straightforward approach avoids any convergence
issues over an ensemble of classical trajectories and can be easily
implemented for on-the-fly ab initio non-adiabatic molecular dynamics.
Since the method is based on a single Gaussian description of the
non-adiabatic events, interference phenomena represented by multiple
wavepackets per potential energy surface cannot be described.

We find that the NA-TGWD approximation fails to fully capture population
transfer, whereas NA-VTGWD proves to be consistently accurate. This
comparison shows that nuclear quantum effects in non-adiabatic processes
can not be fully reproduced simply by a local Gaussian propagation.
Instead, a time-dependent variational approach, which effectively
accounts for non-local nuclear quantum effects, is necessary. This
aligns with previous findings, where Vanicek’s group[52]has already shown that in the adiabatic case, VTGWD can at least partially
recover tunneling, which is a challenging nuclear quantum effect to
reproduce. All NA-VTGWD space integrals have been performed analytically
and the method is expected to be computationally intensive if one
is forced to perform these integrals numerically. However, Vanicek’s
group has also recently shown that if VTGWD integrands are approximated
up to the third order, the accuracy of the variational approach is
mostly retained.[53]This approximation is performed by applying a local cubic approximation
to the potential.[56,58]Also, on the numerical side, there is still room for improvement.
One can employ the Hagedorn formulation and exploit the symplectic
properties of the geometric integrators.[29,69,38]

In our formulation, we employ the diabatic framework instead of the
adiabatic one. One could think that this is a limitation because on-the-fly
ab initio molecular dynamics is performed in the adiabatic framework.
However, the non-adiabatic community is constantly developing diabatization
methods that allow one to perform, at least locally, quantum dynamics
using a diabatic potential.[35,63]The diabatic potential is preferable to the adiabatic one because
non-adiabatic coupling terms can be singular in the adiabatic representation.[48]However, a rigorous diabatic representation does not exist because
of the non-removable residual derivative coupling and, for this reason,
the local diabatization is usually called quasi-diabatization.[27,35,63,47]

In conclusion, we have introduced a method capable of reproducing
non-adiabatic effects through classical mechanics by employing coupled
trajectories confined to separate potential energy surfaces

## Supplementary Material

Supplementary material contains the derivations of the main equations
and additional graphics about the coupled displaced harmonic oscillators
and the classical trajectory for the coupled deep Morse potentials.

## Data Availability Statement

The data that support the findings of this study are available from
the corresponding author upon reasonable request.

## Acknowledgements.The authors thank Prof.s Riccardo Conte, Jiří Vaníček, Loïc Joubert-Doriol,
and Eli Pollak for useful discussions. M.C. thanks Università degli
Studi di Milano for funding under project PSR2025.

## References
- [1]F. Agostini and B. F. Curchod(2019)Different flavors of nonadiabatic molecular dynamics.Wiley interdisciplinary reviews: computational molecular science9(5),pp. e1417.Cited by:§I.
- [2]N. Ananth(2013)Mapping variable ring polymer molecular dynamics: A path-integral based method for nonadiabatic processes.J. Chem. Phys.139(12),pp. 124102.Cited by:§I.
- [3]M. Barbatti, R. S. Mattos, B. Demoulin, M. de O Bispo, M. Bondanza, M. Brady, R. Crespo-Otero, E. G. de Miranda, P. O. Dral, G. Granucci,et al.(2026)The newton-x platform for mixed quantum–classical dynamics.Physical Chemistry Chemical Physics.Cited by:§I.
- [4]T. Begušić and J. Vaníček(2020)On-the-fly ab initio semiclassical evaluation of vibronic spectra at finite temperature.J. Chem. Phys.153(2).Cited by:§I.
- [5]X. Bian, T. Duston, N. Bradbury, Z. Tao, M. Bhati, T. Qiu, X. Wu, Y. Wu, and J. E. Subotnik(2026)The phase-space way to electronic structure theory and subsequently chemical dynamics.Chemical Physics Reviews7(1).Cited by:§I.
- [6]D. Bossion, S. N. Chowdhury, and P. Huo(2021)Non-adiabatic ring polymer molecular dynamics with spin mapping variables.The Journal of Chemical Physics154(18).Cited by:§I.
- [7]M. Ceotto, S. Atahan, S. Shim, G. F. Tantardini, and A. Aspuru-Guzik(2009)First-principles semiclassical initial value representation molecular dynamics.Phys. Chem. Chem. Phys.11,pp. 3861–3867.External Links:DocumentCited by:§I.
- [8]M. Ceotto, S. Atahan, G. F. Tantardini, and A. Aspuru-Guzik(2009)Multiple coherent states for first-principles semiclassical initial value representation molecular dynamics.J. Chem. Phys.130(23),pp. 234113.Cited by:§I.
- [9]M. Ceotto, G. Di Liberto, and R. Conte(2017)Semiclassical "divide-and-conquer" method for spectroscopic calculations of high dimensional molecular systems.Phys. Rev. Lett.119(1),pp. 010401.Cited by:§I.
- [10]M. Ceotto, Y. Zhuang, and W. L. Hase(2013)Accelerated direct semiclassical molecular dynamics using a compact finite difference Hessian scheme.J. Chem. Phys.138(5),pp. 054116.Cited by:§I.
- [11]S. Choi and J. Vaníček(2021)High-order geometric integrators for representation-free ehrenfest dynamics.The Journal of Chemical Physics155(12).Cited by:§I.
- [12]M. S. Church, T. J. H. Hele, G. S. Ezra, and N. Ananth(2018)Nonadiabatic semiclassical dynamics in the mixed quantum-classical initial value representation.J. Chem. Phys.148(10),pp. 102326.Cited by:§I.
- [13]R. D. Coalson and M. Karplus(1990)Multidimensional variational gaussian wave packet dynamics with application to photodissociation spectroscopy.The Journal of Chemical Physics93,pp. 3919.Cited by:§I,§II.2.
- [14]R. Conte, C. Aieta, M. Cazzaniga, and M. Ceotto(2024)A perspective on the investigation of spectroscopy and kinetics of complex molecular systems with semiclassical approaches.J. Phys. Chem. Lett.15,pp. 7566–7576.Cited by:§I.
- [15]R. Conte, F. Gabas, G. Botti, Y. Zhuang, and M. Ceotto(2019)Semiclassical vibrational spectroscopy with Hessian databases.J. Chem. Phys.150(24).External Links:Document,ISSN 00219606Cited by:§I.
- [16]R. Conte, G. Mandelli, G. Botti, D. Moscato, C. Lanzi, M. Cazzaniga, C. Aieta, and M. Ceotto(2025)Semiclassical description of nuclear quantum effects in solvated and condensed phase molecular systems.Chem. Sci.16,pp. 20–28.Cited by:§I.
- [17]S. J. Cotton, R. Liang, and W. H. Miller(2017)On the adiabatic representation of meyer-miller electronic-nuclear dynamics.The Journal of Chemical Physics147(6).Cited by:§I.
- [18]E. G. de Miranda, R. Souza Mattos, S. Mukherjee, J. M. Toldo, C. H. Choi, M. T. d. N. Varella, and M. BarbattiSurface hopping with fully correlated methods.Journal of Chemical Theory and Computation.Cited by:§I.
- [19]J. R. Duke and N. Ananth(2016)Mean field ring polymer molecular dynamics for electronically nonadiabatic reaction rates.Faraday Discussions195,pp. 253–268.Cited by:§I.
- [20]E. Fallacara, F. Finocchi, M. Cazzaniga, S. Chenot, S. Stankic, and M. Ceotto(2024)The fate of the formic acid proton on the anatase tio2(101) surface.Angw. Chemie Intl. Ed.63(48),pp. e202409523.Cited by:§I.
- [21]R. Fausto, G. O. Ildiz, and C. M. Nunes(2022)IR-induced and tunneling reactions in cryogenic matrices: the (incomplete) story of a successful endeavor.Chemical Society Reviews51(7),pp. 2853–2872.Cited by:§I.
- [22]M. D. Feit, J. A. Fleck, and J. A. Steiger(1982)Solution of the schrödinger equation by a spectral method.Journal of Computational Physics47,pp. 412.Cited by:§III.1.
- [23]F. Gabas, R. Conte, and M. Ceotto(2017-06)On-The-Fly ab Initio Semiclassical Calculation of Glycine Vibrational Spectrum.J. Chem. Theory Comput.13(6),pp. 2378–2388.External Links:Document,ISSN 15499626Cited by:§I.
- [24]M. Gandolfi and M. Ceotto(2021)Unsupervised machine learning neural gas algorithm for accurate evaluations of the hessian matrix in molecular dynamics.J. Chem. Theory Comput.17(11),pp. 6733–6746.Cited by:§I.
- [25]S. Garashchuk, J. Stetzler, C. D. Jayawardana, M. A. Safo, and V. A. Rassolov(2025)Variational dynamics of multicomponent wave functions represented in a basis driven by a time-dependent gaussian wavepacket.Journal of Chemical Theory and Computation21(15),pp. 7249–7266.Cited by:§I.
- [26]S. Giannini and J. Blumberger(2022)Charge transport in organic semiconductors: the perspective from nonadiabatic molecular dynamics.Accounts of Chemical Research55(6),pp. 819–830.Cited by:§I.
- [27]B. Gu(2023)A discrete-variable local diabatic representation of conical intersection dynamics.Journal of Chemical Theory and Computation19(19),pp. 6557–6563.Cited by:§IV.
- [28]J. Ha, S. H. Kim, and S. K. Min(2026)Unifying decoherence and phase evolution in mixed quantum–classical dynamics through exact factorization.The Journal of Physical Chemistry Letters17(8),pp. 2321–2327.Cited by:§I.
- [29]G. A. Hagedorn(1998)Raising and lowering operators for semiclassical wave packets.Annals of Physics269(1),pp. 77–104.Cited by:§I,§IV.
- [30]S. Hammes-Schiffer(2010)Introduction: proton-coupled electron transfer.Chemical reviews110(12),pp. 6937–6938.Cited by:§I.
- [31]D. Han, M. Shakiba, and A. V. Akimov(2025)Fully-integrated surface hopping as quantum decoherence correction in nonadiabatic dynamics.The Journal of Physical Chemistry Letters16(28),pp. 7168–7176.Cited by:§I.
- [32]R. Heather and H. Metiu(1985)Some remarks concerning the propagation of a gaussian wave packet trapped in a morse potential.Chemical physics letters118(6),pp. 558–563.Cited by:§I.
- [33]E. J. Heller(1975)Time dependent approach to semiclassical dynamics.J. Chem. Phys.62(4),pp. 1544–1555.External Links:DocumentCited by:§I.
- [34]E. J. Heller(1976)Time dependent variational approach to semiclassical dynamics.The Journal of Chemical Physics64(1),pp. 63–73.Cited by:§I.
- [35]S. Hou, Z. Zhang, and C. Xie(2026)Constructing diabatic potential energy matrices with quantum dynamic accuracy: a neural network basedΔ\Delta-machine learning approach.Journal of Chemical Theory and Computation22(5),pp. 2089–2103.Cited by:§IV.
- [36]L. M. Ibele, E. Sangiogo Gil, P. Schuerger, B. Le Dé, R. Noc, and F. Agostini(2026)A coupled-trajectory strategy for decoherence, frustrated hops and internal consistency in surface hopping.Journal of Chemical Theory and Computation22(5),pp. 2170–2184.Cited by:§I.
- [37]L. M. Ibele, E. S. Gil, E. V. Arribas, and F. Agostini(2024)Simulations of photoinduced processes with the exact factorization: state of the art and perspectives.Physical Chemistry Chemical Physics26(42),pp. 26693–26718.Cited by:§I.
- [38]R. Issa, K. M. R. Afansounoudji, K. Sodoga, and D. Lauvergnat(2026)Quantum propagation using hagedorn wave packets: generalised scheme.Molecular Physics124(6),pp. e2554271.Cited by:§IV.
- [39]A. F. Izmaylov and L. Joubert-Doriol(2017)Quantum nonadiabatic cloning of entangled coherent states.The Journal of Physical Chemistry Letters8(8),pp. 1793–1797.Cited by:§I.
- [40]L. Joubert-Doriol and A. F. Izmaylov(2018)Nonadiabatic quantum dynamics with frozen-width gaussians.The Journal of Physical Chemistry A122(29),pp. 6031–6042.Cited by:§I.
- [41]L. Joubert-Doriol(2022)Variational approach for linearly dependent moving bases in quantum dynamics: application to gaussian functions.Journal of Chemical Theory and Computation18(10),pp. 5799–5809.Cited by:§I,§II.2.
- [42]C. Lubich(2008)From quantum to classical molecular dynamics: reduced models and numerical analysis.Vol.12,European Mathematical Society Zürich.Cited by:§I,§II.2.
- [43]D. V. Makhov, C. Symonds, S. Fernandez-Alberti, and D. V. Shalashilin(2017)Ab initio quantum direct dynamics simulations of ultrafast photochemistry with multiconfigurational ehrenfest approach.Chemical Physics493,pp. 200–218.Cited by:§I.
- [44]G. Mandelli, C. Aieta, and M. Ceotto(2026)Solvation or not solvation: tunneling reactions of molecules embedded in cryogenic matrices.Chemical Science17(1),pp. 448–455.Cited by:§I.
- [45]J. R. Mannouch and J. O. Richardson(2023)A mapping approach to surface hopping.The Journal of Chemical Physics158(10).Cited by:§I.
- [46]T. J. Martínez and R. D. Levine(1997)Non-adiabatic molecular dynamics: split-operator multiple spawning with applications to photodissociation.Journal of the Chemical Society, Faraday Transactions93(5),pp. 941–947.Cited by:§I.
- [47]R. Maskri and L. Joubert-Doriol(2022)The moving crude adiabatic alternative to the adiabatic representation in excited state dynamics.Philosophical Transactions of the Royal Society A380(2223),pp. 20200379.Cited by:§IV.
- [48]C. A. Mead and D. G. Truhlar(1982)Conditions for the definition of a strictly diabatic electronic basis for molecular systems.The Journal of Chemical Physics77(12),pp. 6090–6098.Cited by:§IV.
- [49]H. Meyer, U. Manthe, and L. S. Cederbaum(1990)The multi-configurational time-dependent Hartree approach.Chem. Phys. Lett.165(1),pp. 73–78.Cited by:§I.
- [50]H. Meyer and W. H. Miller(1979)A classical analog for electronic degrees of freedom in nonadiabatic collision processes.J. Chem. Phys.70(7),pp. 3214–3223.Cited by:§I.
- [51]W. H. Miller and S. J. Cotton(2016)Classical molecular dynamics simulation of electronically non-adiabatic processes.Faraday discussions195,pp. 9–30.Cited by:§I.
- [52]R. Moghaddasi Fereidani and J. J. L. Vaníček(2023)High-order geometric integrators for the variational gaussian approximation.The Journal of Chemical Physics159,pp. 094114.Cited by:§I,§III.1,§IV.
- [53]R. Moghaddasi Fereidani and J. Vanicek(2024)High-order geometric integrators for the local cubic variational Gaussian wavepacket dynamics.J. Chem. Phys.160(4),pp. 044113.Cited by:§I,§I,§IV.
- [54]D. Moscato, M. Gandolfi, and M. Ceotto(2025)A time averaged semiclassical approach to the computation of nonadiabatic vibronic absorption spectra.The Journal of Chemical Physics162(23).Cited by:§I.
- [55]D. Moscato, G. Mandelli, M. Bondanza, F. Lipparini, R. Conte, B. Mennucci, and M. Ceotto(2024)Unraveling water solvation effects with quantum mechanics/molecular mechanics semiclassical vibrational spectroscopy: the case of thymidine.J. Am. Chem. Soc.146(12),pp. 8179–8188.Cited by:§I.
- [56]T. Ohsawa and M. Leok(2013)Symplectic semiclassical wave packet dynamics.Journal of Physics A: Mathematical and Theoretical46(40),pp. 405201.Cited by:§I,§IV.
- [57]M. Orlandi, M. Ceotto, and M. Benaglia(2016)Kinetics versus thermodynamics in the proline catalyzed aldol reaction.Chemical Science7(8),pp. 5421–5427.Cited by:§I.
- [58]A. K. Pattanayak and W. C. Schieve(1994)Semiquantal dynamics of fluctuations: ostensible quantum chaos.Physical review letters72(18),pp. 2855.Cited by:§I,§IV.
- [59]J. E. Runeson and J. O. Richardson(2019)Spin-mapping approach for nonadiabatic molecular dynamics.The Journal of chemical physics151(4).Cited by:§I.
- [60]A. Scheidegger and J. L. J. Vanicek(2026)Thawed gaussian ehrenfest dynamics at conical intersections: when can a single mean-field trajectory capture internal conversion?.arXiv2504-05922v1.Cited by:§I.
- [61]T. Schleif, M. Prado Merini, S. Henkel, and W. Sander(2022)Solvation effects on quantum tunneling reactions.Accounts of Chemical Research55(16),pp. 2180–2190.Cited by:§I.
- [62]F. Segatta, L. Cupellini, M. Garavelli, and B. Mennucci(2019)Quantum chemical modeling of the photoinduced activity of multichromophoric biosystems: focus review.Chemical reviews119(16),pp. 9361–9380.Cited by:§I.
- [63]M. Sha and B. Gu(2026)Exponential convergence of the local diabatic representation for nonadiabatic eigenvalue problems.Physical Chemistry Chemical Physics28(15),pp. 9726–9744.Cited by:§IV.
- [64]D. V. Shalashilin(2009)Quantum mechanics with the basis set guided by ehrenfest trajectories: theory and application to spin-boson model.The Journal of chemical physics130(24).Cited by:§I.
- [65]A. Stirling, N. N. Nair, A. Lledós, and G. Ujaque(2014)Challenges in modelling homogeneous catalysis: new answers from ab initio molecular dynamics to the controversy over the wacker process.Chemical Society Reviews43(14),pp. 4940–4952.Cited by:§I.
- [66]G. Stock and M. Thoss(1997)Semiclassical description of nonadiabatic quantum dynamics.Phys. Rev. Lett.78(4),pp. 578.Cited by:§I.
- [67]M. Šulc and J. Vaníček(2012)Accelerating the calculation of time-resolved electronic spectra with the cellular dephasing representation.Mol. Phys.110(9-10),pp. 945–955.External Links:http://dx.doi.org/10.1080/00268976.2012.668971,LinkCited by:§I.
- [68]J. C. Tully and R. K. Preston(1971)Trajectory surface hopping approach to nonadiabatic molecular collisions: the reaction of h+ with d2.The Journal of chemical physics55(2),pp. 562–572.Cited by:§I.
- [69]J. J. Vanicek(2023)Family of gaussian wavepacket dynamics methods from the perspective of a nonlinear schrödinger equation.J. Chem. Phys159(1).Cited by:§I,§IV.
- [70]M. Wehrle, S. Oberli, and J. Vaníček(2015)On-the-Fly ab Initio Semiclassical Dynamics of Floppy Molecules: Absorption and Photoelectron Spectra of Ammonia.J. Phys. Chem. A119(22),pp. 5685–5690.External Links:LinkCited by:§I.
- [71]M. Wehrle, M. Sulc, and J. Vanicek(2014)On-the-fly ab initio semiclassical dynamics: Identifying degrees of freedom essential for emission spectra of oligothiophenes.J. Chem. Phys.140(24),pp. 244114.Cited by:§I.
- [72]M. Wenzel and R. Mitric(2023)Prediction of fluorescence quantum yields using the extended thawed gaussian approximation.The Journal of Chemical Physics159(23).Cited by:§I.
- [73]A. M. Wodtke(2016)Electronically non-adiabatic influences in surface chemistry and dynamics.Chemical Society Reviews45(13),pp. 3641–3657.Cited by:§I.
- [74]G. A. Worth, M. A. Robb, and I. Burghardt(2004)A novel algorithm for non-adiabatic direct dynamics using variational gaussian wavepackets.Faraday discussions127,pp. 307–323.Cited by:§I.
- [75]B. Wu, B. Li, X. He, X. Cheng, J. Ren, and J. Liu(2025)Nonadiabatic field: a conceptually novel approach for nonadiabatic quantum molecular dynamics.Journal of Chemical Theory and Computation21(8),pp. 3775–3813.Cited by:§I.
- [76]L. Zanetti-Polzi and S. Corni(2016)A dynamical approach to non-adiabatic electron transfers at the bio-inorganic interface.Physical Chemistry Chemical Physics18(15),pp. 10538–10549.Cited by:§I.
- [77]J. Zeng, X. Li, and W. Fang(2025)Surface hopping with nuclear quantum effects through path-integral coarse graining.The Journal of Chemical Physics163(22).Cited by:§I.
- [78]J. Zeng and X. Li(2025)The development and applications of semiclassical initial value representation, a promising tool for tackling quantum dynamics.Comput. Mater. Today6,pp. 100032.External Links:Document,ISSN 2950-4635,LinkCited by:§I.

## 


- 


Major funding support from
