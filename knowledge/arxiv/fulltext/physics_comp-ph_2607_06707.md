# Impact of Courant number on the results of numerical simulating of signal propagation in non-dispersive homogeneous media

**arXiv ID**: 2607.06707v1
**Authors**: P. A. Makarov, R. N. Skandakov, V. A. Ustyugov, V. I. Shcheglov
**Published**: 2026-07-07
**Categories**: physics.comp-ph, math-ph, physics.optics
**Comments**: This is an English translation of the article published in Proceedings of the Komi Science Centre of the Ural Branch of the Russian Academy of Sciences. Series "Physical and Mathematical Sciences"
**DOI**: 10.19110/1994-5655-2024-5-73-83
**HTML URL**: https://arxiv.org/html/2607.06707v1

## Abstract

The paper is devoted to the study of the connection between the numerical dispersion arising in FDTD modeling of electromagnetic signal propagation in nondispersive homogeneous media optically different from vacuum and the Courant number in the 2D case. The main results are formulated in the form of four statements, as well as a number of corollaries and remarks that determine the nature of the numerical dispersion, the optimal value of the Courant number and the limitations of the method. It is proved that the optimal choice of the Courant number eliminates the numerical dispersion and extends the capabilities of the developed numerical algorithm to media, which refractive index lesser than refractive index of vacuum, as well as media with negative refraction.

## Full Text

Impact of Courant number on the results of numerical simulating of signal propagation in non-dispersive homogeneous media1footnote 11footnote 1This document is an English translation of the original article published in Proceedings of the Komi Science Centre of the Ural Branch of the Russian Academy of Sciences. Series “Physical and Mathematical Sciences”. The original publication is available at DOI: 10.19110/1994-5655-2024-5-73-83.

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- License: CC BY-NC-ND 4.0arXiv:2607.06707v1 [physics.comp-ph] 07 Jul 2026

## Impact of Courant number on the results of numerical simulating of signal propagation in non-dispersive homogeneous media111This document is an English translation of the original article published inProceedings of the Komi Science Centre of the Ural Branch of the Russian Academy of Sciences. Series “Physical and Mathematical Sciences”. The original publication is available at DOI:10.19110/1994-5655-2024-5-73-83.P.A. Makarov222makarovpa@ipm.komisc.ru, R.N. Skandakov, V.A. Ustyugov, V.I. Shcheglov

## Abstract

The paper is devoted to the study of the connection between the numerical dispersion arising in FDTD modeling of electromagnetic signal propagation in nondispersive homogeneous media optically different from vacuum and the Courant number in the 2D case.
The main results are formulated in the form of four statements, as well as a number of corollaries and remarks that determine the nature of the numerical dispersion, the optimal value of the Courant number and the limitations of the method.
It is proved that the optimal choice of the Courant number eliminates the numerical dispersion and extends the capabilities of the developed numerical algorithm to media, which refractive index lesser than refractive index of vacuum, as well as media with negative refraction.
Keywords:electrodynamics, simulation, FDTD method, numerical experiment

## Introduction

Numerical methods for solving wave equations play an important role not only in specific engineering applications, but also in fundamental science as a whole.
The FDTD (Finite-Difference Time-Domain) method[29]belongs to such methods, and some of its features are the subject of the present work.

The main advantage of the FDTD method is the simplicity of the implementation of the computational algorithm.
This is precisely what determines the widespread use of FDTD in a wide variety of applications: biology and medicine[17,26,24,19], ecology, geology and mineralogy[6,30], optics, photonics, electronics, communications and telecommunications[4,16,18,2,15,13].
In addition to numerous papers related in one way or another to the FDTD method, there is also extensive educational literature on this topic[21,7,25,12].

Despite its long history of development, researchers’ attention continues to be attracted by the fundamental foundations of the FDTD method.
Among these foundations is the issue of assessing the correctness of solutions obtained by the FDTD method in various problem formulations for signals with different spectral shapes[21,12,14].

It is well known (see, for example, the textbooks[21,7,25,12]) that the main parameter governing the accuracy of FDTD computations is the Courant number, which for the 2D case (1 spatial + 1 temporal dimension) has the formSc=c​ΔtΔxS_{\mathrm{c}}=\frac{c\Delta_{t}}{\Delta_{x}}(1)

and combines the main physical parametercc— the speed of light in vacuum — with the numerical parameters of the problemΔx\Delta_{x}andΔt\Delta_{t}, which determine the space-time discretization step.

## Remark 1.

The quality of the numerical solution is determined not only by the choice of the Courant numberScS_{\mathrm{c}}, but also by the requirements on the spectral composition of the signal, as well as by the level of the initial current of its source (see Statement 2 in our previous work[14]).
The influence of the latter two factors was precisely the subject of paper[14], in which the Courant number was chosen optimally for modeling electromagnetic processes in vacuum, namely, it was setSc=1S_{\mathrm{c}}=1.
The present study is a logical continuation of[14].

## 1Motivation and aim of the work

The choiceSc=1S_{\mathrm{c}}=1does not, in general, ensure the quality of the resulting numerical solution in homogeneous nondispersive media optically different from vacuum.
This can be easily seen by examining Figs.1and2.Figure 1:Simulating of the propagation of Gaussian form pulses in vacuum𝒫1\mathcal{P}_{1}and dielectric𝒫2\mathcal{P}_{2}with relative permittivityεr=4\varepsilon_{\mathrm{r}}=4.

Figs.1and2are constructed in accordance with the Yee algorithm, which was discussed in detail by us in the previous work[14](see formulas (13), (19)–(21) therein), with the difference that now the update equations (19)–(20) explicitly take into account the material parameters of the medium (namely, its dielectric permittivityεr\varepsilon_{\mathrm{r}}and magnetic permeabilityμr\mu_{\mathrm{r}}) in which the signals propagate:Hyq+12​[m+12]=Hyq−12​[m+12]+Scη​μr​(Ezq​[m+1]−Ezq​[m]),H_{y}^{q+\frac{1}{2}}\left[m+\frac{1}{2}\right]=H_{y}^{q-\frac{1}{2}}\left[m+\frac{1}{2}\right]+\frac{S_{\mathrm{c}}}{\eta\mu_{\mathrm{r}}}\left(E_{z}^{q}[m+1]-E_{z}^{q}[m]\right),(2)Ezq+1​[m]=Ezq​[m]−𝒥q+12​[m]+Sc​ηεr​(Hyq+12​[m+12]−Hyq+12​[m−12]),E_{z}^{q+1}[m]=E_{z}^{q}[m]-\mathcal{J}^{q+\frac{1}{2}}[m]+\frac{S_{\mathrm{c}}\eta}{\varepsilon_{\mathrm{r}}}\left(H_{y}^{q+\frac{1}{2}}\left[m+\frac{1}{2}\right]-H_{y}^{q+\frac{1}{2}}\left[m-\frac{1}{2}\right]\right),(3)

and the simplest absorbing boundary conditions (21) from[14]are replaced by us with more general equations constructed on the basis of second-order accurate differential equations for the advection of the electromagnetic field.
All the details of the implementation of this scheme are described in detail in[14]and the textbook[21].

## Remark 2.

Modeling the operation of a directional current source in the TF/SF formalism in this article has also undergone some changes compared to[14]and reduces to computing the fields according to the schemeHyq+12​[s−12]=Hyq−12​[s−12]−Scη​μr​Ezinc​[0,q],H_{y}^{q+\frac{1}{2}}\!\left[s-\frac{1}{2}\right]=H_{y}^{q-\frac{1}{2}}\!\left[s-\frac{1}{2}\right]-\frac{S_{\mathrm{c}}}{\eta\mu_{\mathrm{r}}}E_{z}^{\mathrm{inc}}\left[0,q\right],(4)Ezq+1​[s]=Ezq​[s]+Scεr​μr​Ezinc​[−12,q+12].E_{z}^{q+1}[s]=E_{z}^{q}[s]+\frac{S_{\mathrm{c}}}{\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}}E_{z}^{\mathrm{inc}}\!\left[-\frac{1}{2},q+\frac{1}{2}\right].(5)

Here (as in[14])s=50s=50is the fixed grid node number in all numerical experiments, specifying the spatial location of the point antenna that forms the incident fieldEzincE_{z}^{\mathrm{inc}}.
Computing the electricEz​[s]E_{z}[s]and magneticHy​[s−12]H_{y}\left[s-\frac{1}{2}\right]fields according to (5), (4) for a given type of incident waveEzincE_{z}^{\mathrm{inc}}allows one to simulate the operation of the current source𝒥q\mathcal{J}^{q}that forms the wave radiated into the right region of the gridm⩾sm\geqslant s.
Hereinafter, by the operation of the current source𝒥q\mathcal{J}^{q}we mean exactly this scheme.Figure 2:Simulating of pulse propagation in the form of a Ricker wavelet in vacuum𝒫3\mathcal{P}_{3}and dielectric𝒫4\mathcal{P}_{4}with relative permittivityεr=4\varepsilon_{\mathrm{r}}=4.

The parameters of the current sources𝒥q\mathcal{J}^{q}that form the signals shown in Figs.1and2are also described in detail in[14](see formulas (32)–(34) and the corresponding text therein), and are chosen such that the pulses𝒫1\mathcal{P}_{1}and𝒫3\mathcal{P}_{3}propagating in vacuum can be considered a correct numerical solution of the problem in the sense of Definition 2 given in[14].
Proceeding from this, the pulses𝒫1\mathcal{P}_{1}and𝒫3\mathcal{P}_{3}can be considered “reference” ones, comparing with which the pulses𝒫2\mathcal{P}_{2}and𝒫4\mathcal{P}_{4}, respectively, one can easily assess the influence of the medium on the correctness of the numerical solution.

Figs.1and2are constructed for the same value of the Courant numberSc=1S_{\mathrm{c}}=1, for which the source[21]states that it minimizes FDTD numerical errors, and the textbook[12]claims that such a choice allows one to obtain an exact solution of the problem.

At the same time, it is obvious that the FDTD solutions depicted by the pulses𝒫2\mathcal{P}_{2}in Fig.1and𝒫4\mathcal{P}_{4}in Fig.2are not correct in the sense of Definition 2 given by us in[14], which is in direct contradiction with what was noted in the previous paragraph.
This incorrectness is the result of a phenomenon that occurs everywhere in FDTD numerical calculations and is known in the literature[21,12]as “numerical dispersion”.

Indeed, the signals𝒫2\mathcal{P}_{2}in Fig.1and𝒫4\mathcal{P}_{4}in Fig.2do not represent either the original Gaussian pulse or the Ricker wavelet, respectively.
During the propagation of these wave packets in a dielectric withεr=4\varepsilon_{\mathrm{r}}=4over a sufficiently long time (Δ​q=230\Delta q=230and250250, respectively), their shape is significantly distorted (note that this effect is rather weak for the parameters used and begins to manifest itself clearly only towards the end of the simulation).
This contradicts the initial mathematical model of the phenomenon we are simulating, since the medium was assumed to be nondispersive.
This obvious contradiction raises a natural question — can the FDTD method be used at all to obtain correct simulation results for signal propagation in nondispersive materials?
And if this is possible, then how does the choice of the Courant numberScS_{\mathrm{c}}affect the correctness of the obtained solutions?

Despite the contradiction noted above, the FDTD method was previously used by us in a number of works that considered either wave propagation in randomly inhomogeneous media[15,13], or the features of the solution of the homogeneous and inhomogeneous Cauchy problems by the FDTD method[14].
In both the first and the second case, all problems associated with numerical dispersion were completely ignored, partly because in all these works a significant part of the path along which the propagation of electromagnetic signals was considered was air space (modeled by us as indistinguishable from vacuum).
At the same time, such an ignoring of this aspect of the matter cannot be fully justified, which requires, if not a complete correction of numerical dispersion, then at least a clarification of the effects associated with it.

Further, note that in the book[21]it is postulated without any proof that the valueSc=1S_{\mathrm{c}}=1is the maximum possible, which, generally speaking, does not correspond at all to the meaning of definition (1), which does not impose any restrictions on the arbitrarily chosen space-time grid stepsΔx\Delta_{x}andΔt\Delta_{t}, and the ratio between them.
The source[12]more cautiously states that the choiceSc>1S_{\mathrm{c}}>1leads to an exponential growth of noise caused by rounding errors, which are always present in numerical simulation, which ultimately completely destroys the obtained solution.

## Remark 3.

It should also be noted that in the works[21]and[12]different quantities are called the Courant numbers, which creates additional difficulties in understanding all the noted issues.
This is because in[21]in definition (1) the quantityccis the speed of light in vacuum (as is also adopted by us in this work), while in[12]it is considered thatccis the speed of wave propagation in a given specific medium.

In addition to the problems already noted, the question also arises about the possibility of applying the FDTD method for modeling electrodynamics in “not the most ordinary media” (even if the phenomenon of dispersion is neglected).
The following examples are meant here: the propagation of radio waves in the Earth’s ionosphere[28], electromagnetic waves of the terahertz or X-ray range in conductors, semiconductors or dielectrics[10,3], media with negative values of relative permittivities (in particular, “left-handed” media[22,27,20,1]).
In all these cases, the dispersion of electromagnetic waves plays a decisive role, the anomalous nature of which from the mathematical point of view consists in the fact that the permittivityεr\varepsilon_{\mathrm{r}}and permeabilityμr\mu_{\mathrm{r}}can take values less than unity, and even more so — negative ones.

At the same time, the usual algorithms found in the literature on the FDTD method[29,21,7,25,12,15,13,14]do not allow one to simulate the propagation of electromagnetic waves in such media simply by setting the values0<εr,μr<10<\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}}<1andεr,μr<0\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}}<0.

The present article is devoted to solving the noted issues, the aim of which is thus to consider the numerical dispersion of the FDTD method and to assess the influence of the choice of the Courant number values on the quality of modeling the propagation of signals in homogeneous nondispersive media.

## 2Numerical dispersion in the FDTD method

To obtain an expression describing the numerical dispersion in the Yee grid, let us return to the original discrete analogs of the Ampere (3) and Faraday (2) equations, which in a more compact and convenient form can be written using the shift operators in the space-time grid𝒮^xχ\widehat{\mathcal{S}}_{x}^{\chi}and𝒮^tτ\widehat{\mathcal{S}}_{t}^{\tau}(hereχ\chiandτ\tauare shift parameters having the formχ,τ=p/2,∀p∈ℤ\chi,\tau=p/2,\,\forall p\in\mathbb{Z}).
By definition, the action of these operators has the form𝒮^xχ:𝒮^xχ​ψq​[m]=ψq​[m+χ],\widehat{\mathcal{S}}_{x}^{\chi}:\,\widehat{\mathcal{S}}_{x}^{\chi}\psi^{q}[m]=\psi^{q}\left[m+\chi\right],(6)𝒮^tτ:𝒮^tτ​ψq​[m]=ψq+τ​[m],\widehat{\mathcal{S}}_{t}^{\tau}:\,\widehat{\mathcal{S}}_{t}^{\tau}\psi^{q}[m]=\psi^{q+\tau}[m],(7)

whereψ\psidenotes an arbitrary component of the electromagnetic field (in the 2D case considered by us —EzE_{z}orHyH_{y}).

It is easy to verify that with the help of the operators (6) and (7) the Ampere equation (3) in the absence of extraneous sources (𝒥=0\mathcal{J}=0) can be written in the form𝒮^t12​ε​(𝒮^t12−𝒮^t−12Δt)​Ezq​[m]=𝒮^t12​(𝒮^x12−𝒮^x−12Δx)​Hyq​[m].\displaystyle\widehat{\mathcal{S}}_{t}^{\frac{1}{2}}\varepsilon\left(\frac{\widehat{\mathcal{S}}_{t}^{\frac{1}{2}}-\widehat{\mathcal{S}}_{t}^{-\frac{1}{2}}}{\Delta_{t}}\right)E_{z}^{q}[m]=\widehat{\mathcal{S}}_{t}^{\frac{1}{2}}\left(\frac{\widehat{\mathcal{S}}_{x}^{\frac{1}{2}}-\widehat{\mathcal{S}}_{x}^{-\frac{1}{2}}}{\Delta_{x}}\right)H_{y}^{q}[m].(8)

Here we take into account the definition of the Courant number (1), the relationc=1/ε0​μ0c=1/\sqrt{\varepsilon_{0}\mu_{0}}of the speed of light in vacuum with its dielectric permittivityε0\varepsilon_{0}and magnetic permeabilityμ0\mu_{0}and the expression for the characteristic impedance of vacuumη=μ0/ε0≈120​π\eta=\sqrt{\mu_{0}/\varepsilon_{0}}\approx 120\pi(for reference see, for example, the textbooks[3,10]).
In addition, when writing (8), the notation for the absolute dielectric permittivity of the mediumε=εr​ε0\varepsilon=\varepsilon_{\mathrm{r}}\varepsilon_{0}is used.

For convenience, let us also define the finite-difference operators∂~i\tilde{\partial}_{i}according to∂~i=𝒮^i12−𝒮^i−12Δi,\tilde{\partial}_{i}=\frac{\widehat{\mathcal{S}}_{i}^{\frac{1}{2}}-\widehat{\mathcal{S}}_{i}^{-\frac{1}{2}}}{\Delta_{i}},(9)

whereiiis eitherxxortt.
With the help of (9) the Ampere law in a stationary medium without extraneous currents (8) can finally be written in the Yee form[21]ε​𝒮^t12​∂~t​Ezq​[m]=𝒮^t12​∂~x​Hyq​[m].\varepsilon\widehat{\mathcal{S}}_{t}^{\frac{1}{2}}\tilde{\partial}_{t}E_{z}^{q}[m]=\widehat{\mathcal{S}}_{t}^{\frac{1}{2}}\tilde{\partial}_{x}H_{y}^{q}[m].(10)

In the same way, using (6), (7) and (9) the discrete analog of the Faraday law (2) is reduced to the Yee formμ​𝒮^x12​∂~t​Hyq​[m]=𝒮^x12​∂~x​Ezq​[m].\mu\widehat{\mathcal{S}}_{x}^{\frac{1}{2}}\tilde{\partial}_{t}H_{y}^{q}[m]=\widehat{\mathcal{S}}_{x}^{\frac{1}{2}}\tilde{\partial}_{x}E_{z}^{q}[m].(11)

Now consider a plane monochromatic wave of frequencyω\omegapropagating in the Yee grid to the right (m⩾sm\geqslant s)Ezq​[m]=E0​ei​(ω​q​Δt−β~​m​Δx),E_{z}^{q}[m]=E_{0}\,e^{i(\omega q\Delta_{t}-\tilde{\beta}m\Delta_{x})},(12)Hyq​[m]=H0​ei​(ω​q​Δt−β~​m​Δx),H_{y}^{q}[m]=H_{0}\,e^{i(\omega q\Delta_{t}-\tilde{\beta}m\Delta_{x})},(13)

whereβ~\tilde{\beta}is the wavenumber, i.e., the propagation constant of a plane monochromatic wave in the FDTD grid (different from the corresponding constantβ\betain continuous space), andE0E_{0}andH0H_{0}are the complex amplitudes of the electric and magnetic field intensities.

## Lemma 1.

The action of the operators (9) on an arbitrary componentψ\psiof a plane monochromatic wave (12), (13) reduces to∂~t​ψ=i​2Δt​sin⁡(ω​Δt2)​ψ,\tilde{\partial}_{t}\psi=i\frac{2}{\Delta_{t}}\sin\left(\frac{\omega\Delta_{t}}{2}\right)\psi,(14)∂~x​ψ=−i​2Δx​sin⁡(β~​Δx2)​ψ.\tilde{\partial}_{x}\psi=-i\frac{2}{\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right)\psi.(15)

## Proof.

It is verified by direct substitution of (12), (13) into (9) taking into account (6), (7).
Let us write out here in explicit form only the action onψ\psiof the shift operators (6), (7) with parametersχ,τ=±12\chi,\tau=\pm\frac{1}{2}𝒮^t±12​ψ=e±i​ω​Δt/2​ψ,𝒮^x±12​ψ=e∓i​β~​Δx/2​ψ,\widehat{\mathcal{S}}_{t}^{\pm\frac{1}{2}}\psi=e^{\pm i\omega\Delta_{t}/2}\psi,\quad\widehat{\mathcal{S}}_{x}^{\pm\frac{1}{2}}\psi=e^{\mp i\tilde{\beta}\Delta_{x}/2}\psi,(16)

with the help of which the equalities (14) and (15) are obtained elementarily.
∎

## Proposition 1.

The dispersion relation for the Yee grid can be represented in the formsin⁡(ω​Δt2)=Δtε​μ​Δx​sin⁡(β~​Δx2).\sin\left(\frac{\omega\Delta_{t}}{2}\right)=\frac{\Delta_{t}}{\sqrt{\varepsilon\mu}\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right).(17)

## Proof.

Using the results (14) and (15) of Lemma1, as well as (16) in the Ampere law (10) for a plane monochromatic wave, we writei​ε​2Δt​sin⁡(ω​Δt2)​ei​ω​Δt/2​Ezq​[m]=−i​2Δx​sin⁡(β~​Δx2)​ei​ω​Δt/2​Hyq​[m].\displaystyle i\varepsilon\frac{2}{\Delta_{t}}\sin\left(\frac{\omega\Delta_{t}}{2}\right)e^{i\omega\Delta_{t}/2}E_{z}^{q}[m]=-i\frac{2}{\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right)e^{i\omega\Delta_{t}/2}H_{y}^{q}[m].(18)

Substituting into the last equality the explicit expressions for the fields (12), (13) for a plane monochromatic wave and canceling common factors, we obtainε​1Δt​sin⁡(ω​Δt2)​E0=−1Δx​sin⁡(β~​Δx2)​H0.\varepsilon\frac{1}{\Delta_{t}}\sin\left(\frac{\omega\Delta_{t}}{2}\right)E_{0}=-\frac{1}{\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right)H_{0}.(19)

Hence we arrive at the expression for the numerical impedance in the Yee gridE0H0=−Δtε​Δx⋅sin⁡β~​Δx2sin⁡ω​Δt2.\frac{E_{0}}{H_{0}}=-\frac{\Delta_{t}}{\varepsilon\Delta_{x}}\cdot\frac{\sin\cfrac{\tilde{\beta}\Delta_{x}}{2}}{\sin\cfrac{\omega\Delta_{t}}{2}}.(20)

Performing similar actions with respect to the Faraday law (11), we sequentially obtaini​μ​2Δt​sin⁡(ω​Δt2)​e−i​β~​Δx/2​Hyq​[m]=−i​2Δx​sin⁡(β~​Δx2)​e−i​β~​Δx/2​Ezq​[m],\displaystyle i\mu\frac{2}{\Delta_{t}}\sin\left(\frac{\omega\Delta_{t}}{2}\right)e^{-i\tilde{\beta}\Delta_{x}/2}H_{y}^{q}[m]=-i\frac{2}{\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right)e^{-i\tilde{\beta}\Delta_{x}/2}E_{z}^{q}[m],(21)μ​1Δt​sin⁡(ω​Δt2)​H0=−1Δx​sin⁡(β~​Δx2)​E0\mu\frac{1}{\Delta_{t}}\sin\left(\frac{\omega\Delta_{t}}{2}\right)H_{0}=-\frac{1}{\Delta_{x}}\sin\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right)E_{0}(22)

and the corresponding impedance in the formE0H0=−μ​ΔxΔt⋅sin⁡ω​Δt2sin⁡β~​Δx2.\frac{E_{0}}{H_{0}}=-\frac{\mu\Delta_{x}}{\Delta_{t}}\cdot\frac{\sin\cfrac{\omega\Delta_{t}}{2}}{\sin\cfrac{\tilde{\beta}\Delta_{x}}{2}}.(23)

Equating the right-hand sides of (20) and (23), and performing cross-multiplication of the factors in the resulting equality, we obtainsin2⁡(ω​Δt2)=Δt2ε​μ​Δx2​sin2⁡(β~​Δx2).\sin^{2}\left(\frac{\omega\Delta_{t}}{2}\right)=\frac{\Delta_{t}^{2}}{\varepsilon\mu\Delta_{x}^{2}}\sin^{2}\left(\frac{\tilde{\beta}\Delta_{x}}{2}\right).(24)

Taking the square root in the last equality, we finally arrive at (17), which completes the proof.
∎

## Remark 4.

The dispersion relation (17) of the FDTD method differs significantly from its continuous analog, which has the form[3,10]β=ω​ε​μ.\beta=\omega\sqrt{\varepsilon\mu}.(25)

At the same time, we note that this difference becomes vanishingly small with sufficiently fine space-time discretization.
Indeed, retaining in the Taylor series expansions of the sine atΔt\Delta_{t}andΔx→0\Delta_{x}\rightarrow 0only the first-order terms, one can easily obtain from (17)β~=ω​ε​μ.\tilde{\beta}=\omega\sqrt{\varepsilon\mu}.(26)

Let us emphasize, however, that (26) is valid only in the limit of infinitely fine discretizationΔt,Δx→0\Delta_{t},\Delta_{x}\rightarrow 0.
In the general case of finite space-time discretization, the phase velocities of the wave in the Yee FDTD gridc~p\tilde{c}_{\mathrm{p}}and in continuous spacecpc_{\mathrm{p}}will be different.

## Proposition 2.

The deviation of the phase velocity of the wave in the Yee grid from the corresponding value in the continuous case can be described by the equalityc~pcp=π​εr​μrNλ​arcsin⁡[εr​μrSc​sin⁡(π​ScNλ)],\frac{\tilde{c}_{\mathrm{p}}}{c_{\mathrm{p}}}=\frac{\pi\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}}{N_{\lambda}\arcsin\left[\cfrac{\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}}{S_{\mathrm{c}}}\,\sin\!\left(\cfrac{\pi S_{\mathrm{c}}}{N_{\lambda}}\right)\right]},(27)

where the parameterNλN_{\lambda}is the number of spatial grid nodes per wavelength in free spaceλ=Nλ​Δx.\lambda=N_{\lambda}\Delta_{x}.(28)

## Proof.

We use the relation of the phase velocity with the wavenumber in continuous space[3,10]and in the FDTD gridcp=ωβ,c~p=ωβ~,c_{\mathrm{p}}=\frac{\omega}{\beta},\quad\tilde{c}_{\mathrm{p}}=\frac{\omega}{\tilde{\beta}},(29)

which allows us to reduce the left-hand side of equality (27) to the formc~pcp=ββ~=β​Δx2β~​Δx2.\frac{\tilde{c}_{\mathrm{p}}}{c_{\mathrm{p}}}=\frac{\beta}{\tilde{\beta}}=\frac{\frac{\beta\Delta_{x}}{2}}{\frac{\tilde{\beta}\Delta_{x}}{2}}.(30)

Further, we apply (25) to the numerator of the last equalityβ=ω​ε​μ=2​π​cλ​ε0​εr​μ0​μr=2​πλ​εr​μr,\beta=\omega\sqrt{\varepsilon\mu}=2\pi\frac{c}{\lambda}\sqrt{\varepsilon_{0}\varepsilon_{\mathrm{r}}\mu_{0}\mu_{\mathrm{r}}}=\frac{2\pi}{\lambda}\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}},(31)

where the wavelength in vacuumλ\lambdais discretized according to (28), which givesβ​Δx2=π​εr​μrNλ.\frac{\beta\Delta_{x}}{2}=\frac{\pi\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}}{N_{\lambda}}.(32)

Applying now to the denominator of the right-hand side of (30) the dispersion relation (17), in which transformations similar to (31) are used, as well as the definition of the Courant number (1) together with (28), we obtainβ~​Δx2=arcsin⁡[εr​μrSc​sin⁡(π​ScNλ)].\frac{\tilde{\beta}\Delta_{x}}{2}=\arcsin\left[\frac{\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}}{S_{\mathrm{c}}}\sin\left(\frac{\pi S_{\mathrm{c}}}{N_{\lambda}}\right)\right].(33)

Substitution of the last two equalities into (30) leads to the result (27), which completes the proof.
∎

Relation (27) within the framework of the restrictions considered in this article (according to which nondispersive homogeneous media are investigated, for which bothεr\varepsilon_{\mathrm{r}}andμr\mu_{\mathrm{r}}are some real constants), has an obvious meaning in the following domain of definition of the parameters:Nλ∈ℕ\1,εr,μr,Sc∈(0,+∞)⊂ℝ,N_{\lambda}\in\mathbb{N}\backslash 1,\quad\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}},S_{\mathrm{c}}\in(0,+\infty)\subset\mathbb{R},(34)

where neither the set of natural numbers greater than unityℕ\1\mathbb{N}\backslash 1, nor the set of positive real numbers are considered to contain the element+∞+\inftyitself.
Going beyond the domain of definition (34) requires a separate detailed study, and we will return to it in the last section of this article.

Before proceeding to the discussion of the features of expression (27), we note that the dielectric and magnetic permittivities of the medium enter it only in the combinationnr=εr​μr,n_{\mathrm{r}}=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}},(35)

which has the physical meaning of the relative refractive index of the medium.

## Example 1.

Consider the propagation of a plane monochromatic wave withNλ=10N_{\lambda}=10in glass with a refractive indexnr=1.5n_{\mathrm{r}}=1.5in the case of the Courant numberSc=1S_{\mathrm{c}}=1.
The ratio (27) in this case isc~p/cp≈0.9777\tilde{c}_{\mathrm{p}}/c_{\mathrm{p}}\approx 0.9777, which in percentage terms amounts to a numerical error of about2.23%2.23\%.
Thus, in this situation, for each unit of path equal to the wavelength, the FDTD calculation accumulates a significant phase error of the order of8.03∘8.03^{\circ}.
Note also that improving the wavelength discretization by a factor of two (Nλ=20N_{\lambda}=20) reduces the corresponding errors to the values0.48%0.48\%and1.89∘1.89^{\circ}(i.e., approximately fourfold), as should happen for a second-order accurate computational method.Figure 3:Dependence of the phase velocity ratio, determined according to the FDTD method with respect to its exact value (27), on the wavelength discretization parameterNλN_{\lambda}for some media with relative refractive indicesnrn_{\mathrm{r}}. The Courant numberSc=1S_{\mathrm{c}}=1.

The features of the numerical dispersion of the FDTD method, determined by expression (27), and complementing the example given above, are presented in Fig.3.
This figure shows a family of curves for whichnr>Scn_{\mathrm{r}}>S_{\mathrm{c}}(namely,nr=2n_{\mathrm{r}}=\sqrt{2}for curve11,nr=3n_{\mathrm{r}}=\sqrt{3}— for line22, andnr=2n_{\mathrm{r}}=2— for33, respectively).
It can be seen that an increase in the refractive index of the medium with poor wavelength discretization leads to a significant lag of the wave simulated by the FDTD method, which is expressed in a significant deviation of the ratioc~p/cp\tilde{c}_{\mathrm{p}}/c_{\mathrm{p}}from unity.

In addition, Fig.3shows curve44, corresponding to the casenr<Scn_{\mathrm{r}}<S_{\mathrm{c}}(in this particular case, the valuenr=1/2n_{\mathrm{r}}=\sqrt{1/2}is chosen).
This example demonstrates that in media optically less dense than vacuum, the FDTD calculation leads to the propagation of the simulated waves with a lead compared to the true velocity.

## Corollary 1.

It can be seen from Fig.3that the accuracy of the FDTD calculation decreases with decreasingNλN_{\lambda}, and also — as the permittivity of the medium deviates from unity (which is the case for both dielectrics, and magnets, and magnetic dielectrics).

## Corollary 2.

It is easy to calculate the limit of the ratio (27), which, regardless of the values ofnrn_{\mathrm{r}}andScS_{\mathrm{c}}, is equal tolimNλ→+∞c~pcp=1.\lim_{N_{\lambda}\rightarrow+\infty}\frac{\tilde{c}_{\mathrm{p}}}{c_{\mathrm{p}}}=1.(36)

This means that the accuracy of the FDTD calculation improves with increasingNλN_{\lambda}.

## Remark 5.

The decrease in the accuracy of the FDTD calculation in a medium withnr>1n_{\mathrm{r}}>1is due to the fact that the wavelength in such a medium is shorter than in vacuum, and a small discretization of the wavelengthNλN_{\lambda}is not enough for a correct calculation.
However, a simple transfer of this statement to the case of a medium withεr<1\varepsilon_{\mathrm{r}}<1is not so obvious and requires clarification.

## Corollary 3.

In addition, Fig.3indicates that high-frequency components of a wave packet in media withεr>1\varepsilon_{\mathrm{r}}>1tend to lag behind, while in media withεr<1\varepsilon_{\mathrm{r}}<1this feature changes to the opposite — high-frequency components of the wave packet in the Yee grid propagate with a higher phase velocity than is actually the case.
In other words, in media optically denser compared to vacuum, the FDTD calculation leads to the occurrence of numerical dispersion having the character of anomalous dispersion[11].
And conversely — when modeling optically less dense media, the influence of FDTD discretization corresponds to the behavior of normal dispersion (in this case, the “red” components of the wave packet “overtake the blue” ones).

## Remark 6.

The structure of the denominator (27) has an obvious resemblance to the form of dispersion equations obtained in problems of wave propagation in media with periodic inhomogeneities[28,9,8,5].
Namely, the function appears hereφ​(Nλ,Sc,nr)=nrSc​sin⁡π​ScNλ,\varphi(N_{\lambda},S_{c},n_{\mathrm{r}})=\frac{n_{\mathrm{r}}}{S_{\mathrm{c}}}\sin\frac{\pi S_{\mathrm{c}}}{N_{\lambda}},(37)

the character of which determines the passbands and stopbands of the Yee grid.
Indeed, it is easy to understand that the region of parameter values(Nλ,Sc,nr)(N_{\lambda},S_{\mathrm{c}},n_{\mathrm{r}})in which the condition|φ​(Nλ,Sc,nr)|>1\left|\varphi(N_{\lambda},S_{c},n_{\mathrm{r}})\right|>1is satisfied corresponds to the non-transmission of waves, since the expressionarcsin⁡φ\arcsin\varphiin this case has no meaning in real values.

A similar picture of the phenomenon takes place in the Kronig–Penney model, as well as in the Hill and Mathieu equations describing parametric oscillations[28,9,8,5], as well as wave propagation in systems with spatial periodicity in the arrangement of inhomogeneities.
As a periodic structure in our case (in the FDTD method), the Yee computational grid itself acts directly.
In this case, the transmission and non-transmission of waves (the quantum-mechanical analog — allowed and forbidden bands) is determined precisely by the quantitiesNλN_{\lambda},ScS_{\mathrm{c}}andnrn_{\mathrm{r}}.Figure 4:(Nλ,Sc)(N_{\lambda},S_{\mathrm{c}})-diagram of Yee grid bandwidths whennr=100n_{\mathrm{r}}=100.

Fig.4illustrates the(Nλ,Sc)(N_{\lambda},S_{\mathrm{c}})-diagram of the Yee grid passbands, constructed on the basis of the function (37) for a relatively large value of the refractive index of the mediumnr=100n_{\mathrm{r}}=100.
The regions of the stopbands{𝒜i}i=1𝒩\left\{\mathcal{A}_{i}\right\}_{i=1}^{\mathcal{N}}, corresponding to the condition|φ​(Nλ,Sc,nr)|>1\left|\varphi(N_{\lambda},S_{c},n_{\mathrm{r}})\right|>1, are shown in this diagram by a monotone gray shading.
The total number of such regions𝒩\mathcal{N}(the first two of them are marked in Fig.4) depends on the value of the refractive index of the mediumnrn_{\mathrm{r}}, and grows with its increase.
The passbands are shown in this diagram by a gradient fill, changing from black (φ=+1\varphi=+1) to white (φ=−1\varphi=-1).
It is within the framework of the latter regions that the dispersion relation in the form (27) makes sense.

Also in Fig.4the regionℬ\mathcal{B}defined by the inequalitySc>ncS_{\mathrm{c}}>n_{\mathrm{c}}is highlighted in gray, within which the FDTD method also cannot provide a correct numerical solution of the problem of wave propagation in a homogeneous nondispersive medium.
The arguments confirming the validity of this statement are given in the next section of the article when discussing Fig.6.

## 3Relation of numerical dispersion with the Courant number

Now, after the preliminary study, let us discuss the algorithm for correcting the numerical dispersion by a special choice of the Courant number.
Its possibility is based on the relation (27), from which the following result directly follows.

## Proposition 3.

For any givenεr\varepsilon_{\mathrm{r}}andμr\mu_{\mathrm{r}}belonging to the domain of definition (34), it is always possible to eliminate the computational errors associated with numerical dispersion by setting the Courant number equal toSc=εr​μr.S_{\mathrm{c}}=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}.(38)

## Proof.

It is verified by direct substitution of (38) into (27).
∎

## Remark 7.

The value of the Courant number (38) can be called “magic”, since in this case the phase velocity of the wave in the FDTD gridc~p\tilde{c}_{\mathrm{p}}exactly coincides with the real value of the phase velocitycpc_{\mathrm{p}}regardless of the chosen wavelength discretizationNλN_{\lambda}.
At the same time, in the source[21], the valueSc=1S_{\mathrm{c}}=1is called “magic”, which is valid only for vacuum, but not in the general case.
Here we also note that our choice (38) is equivalent to settingSc=1S_{\mathrm{c}}=1used in the book[12].

Several examples illustrating the idea of applying the “magic” Courant number (38) to correct the numerical dispersion in nondispersive homogeneous media, limited by the choice of parameters (34), are given in Fig.5.Figure 5:Simulating of Gaussian pulse propagation in media optically denser𝒫5\mathcal{P}_{5}(nr=2n_{\mathrm{r}}=2) and less dense𝒫6\mathcal{P}_{6}(nr=1/2n_{\mathrm{r}}=\sqrt{1/2}) than vacuum, with using correction of numeric dispersion (38).

Fig.5confirms the idea formulated in the form of Statement3— numerical dispersion is indeed absent here both in the case of a medium optically denser compared to vacuum (pulse𝒫5\mathcal{P}_{5}) and in the case of an optically less dense medium (pulse𝒫6\mathcal{P}_{6}).
Fig.5should be compared with Fig.1, in which numerical dispersion is clearly manifested in the shape of the pulse𝒫2\mathcal{P}_{2}.

## Remark 8.

Note also that the propagation of the electromagnetic field in space over time (determined, as always, by the value of the discrete indexqq), presented in Fig.5for the pulse𝒫5\mathcal{P}_{5}, occurs with a visible lead compared to the similar process for the pulse𝒫2\mathcal{P}_{2}in Fig.1by a factor of two.
It should be emphasized that this lead is only apparent, since its cause is precisely the twofold difference in the Courant numbers chosen in the case of Fig.1and Fig.5.
In reality (taking into account the correction forScS_{\mathrm{c}}), all the temporal characteristics of the signals in Figs.1and5are identical.
In other words, if we consider the spatial step of the gridΔx\Delta_{x}as a fixed parameter that does not change when switching from the simulation in the caseSc=1S_{\mathrm{c}}=1presented in Fig.1to the simulation with the Courant number (38), then the “price” of each time stepΔt\Delta_{t}(and along with it, the total duration of the simulation) will change by a factor ofεr​μr\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}.
The same effect (with the replacement of the word “lead” by “lag”) also takes place in the case of optically less dense media (see pulse𝒫6\mathcal{P}_{6}) in Fig.5.

## Remark 9.

We also separately point out that the simulation of the propagation of the pulse𝒫6\mathcal{P}_{6}in a medium optically less dense than vacuum in accordance with the computational algorithm (2) – (5) with the choice of the Courant numberSc=1S_{\mathrm{c}}=1is fundamentally impossible.
It is easy to verify that the calculations in this case very quickly lead to divergences, without giving any useful information, and fundamentally do not describe this particular case.

The last remark is perfectly illustrated by Fig.6, which shows the avalanche-like process of accumulation of numerical errors during the calculation according to the algorithm (2) – (5) in the case of exceeding the Courant numberScS_{\mathrm{c}}compared tonrn_{\mathrm{r}}by only0.1%0.1\%.
This illustration is constructed with the same parameters of the signal source𝒥q\mathcal{J}^{q}as in Figs.1and5, for the case of vacuum, although fundamentally the same picture takes place in the case of any other homogeneous nondispersive media from the domain of definition (34).Figure 6:Time dynamics of the numerical solution destruction obtained during computation according to the algorithm (2) – (5) whenSc−nr=10−3S_{\mathrm{c}}-n_{\mathrm{r}}=10^{-3}.

As can be seen from Fig.6, by the timeq=130q=130the level of noise that arises randomly as a result of calculations according to the scheme (2) – (5) atSc−nr=10−3S_{\mathrm{c}}-n_{\mathrm{r}}=10^{-3}, twice exceeds the magnitude of the useful signal in absolute value.
At the same time, the spatial extent of the part of the Yee grid affected by this noise is3/43/4of the entire length of the computational domain.
The latter circumstance significantly distorts the shape of the trailing edge of the simulated useful signal.
Further, with the subsequent development of the process atq>130q>130the useful solution is completely destroyed.

Additional numerical experiments performed by us also show that the effects associated with the accumulation of errors due to self-excitation of the grid always occur when the inequalitySc>nrS_{\mathrm{c}}>n_{\mathrm{r}}is satisfied.
Thus, atSc−nr=10−4S_{\mathrm{c}}-n_{\mathrm{r}}=10^{-4}the self-excitation of the grid becomes noticeable already after the passage of the useful signal, but its avalanche-like character is observed in this case as well.
All these observations can be generalized in the form of the following statement.

## Proposition 4.

The computational algorithm (2) – (5) diverges rapidly and cannot be used to obtain a correct numerical solution of the problem of signal propagation in nondispersive homogeneous media when choosingSc>nrS_{\mathrm{c}}>n_{\mathrm{r}}.

## Proof.

An exhaustive argument for the validity of this statement at the “physical level of rigor” is given above when discussing Fig.6.
∎

It is by applying this statement that the presence of the regionℬ\mathcal{B}shown in Fig.4is explained, although from a formal point of view the function (37) does not exceed unity in absolute value in this case.

## Remark 10.

At the same time, we note that the choice of valuesSc⩽nrS_{\mathrm{c}}\leqslant n_{\mathrm{r}}, consistent with the condition|φ​(Nλ,Sc,nr)|⩽1\left|\varphi(N_{\lambda},S_{\mathrm{c}},n_{\mathrm{r}})\right|\leqslant 1, does not lead to such dramatic consequences as those that take place in Statement4.

An important consequence of the detailed study carried out in this way, the main results of which are Statements3and4, is one more fact.

## Corollary 4.

Setting the Courant number in the form (38) is the only possible optimal choice from the point of view of applying the numerical FDTD algorithm (2) – (5) to model the propagation of signals in nondispersive homogeneous media.

## Proof.

The optimality of such a choice is due to the fact that it eliminates the numerical dispersion when simulating signals of any shape and spectral composition, not contradicting Statement 2 of[14], propagating in a wide class of nondispersive homogeneous media described by the domain of definition (34).
The uniqueness follows from Statement4.
∎

## Remark 11.

The problem that has remained unresolved to date (arising from a careful study of the application of the algorithm (2) – (5) to homogeneous nondispersive media optically different from vacuum) is that in this case, in addition to the main signal with the selected direction, a signal of relatively small amplitude of the opposite direction is always observed.
Let us call this last signal for brevity — backward𝒫b\mathcal{P}_{\mathrm{b}}, in contrast to the original — forward𝒫f\mathcal{P}_{\mathrm{f}}.
An illustration of this problem is given in Fig.7, which is constructed with the same parameters of the signal source as Figs.1and5.

Fig.7demonstrates the formation of the backward pulse𝒫b\mathcal{P}_{\mathrm{b}}when simulating the propagation of a Gaussian-shaped signal in media optically less dense than vacuum with the optimal choice of the Courant number.
It can be seen that the character of this phenomenon depends significantly on the value of the relative refractive indexnrn_{\mathrm{r}}of the medium.
As the latter tends to zero, this phenomenon can no longer be neglected, since it leads to a distortion of the characteristics of the useful forward signal𝒫f\mathcal{P}_{\mathrm{f}}as well.
At the same time, in the casenr>10−1n_{\mathrm{r}}>10^{-1}the corresponding numerical error is relatively small and can be estimated not to exceed the level of1%1\%.Figure 7:Dynamics of forward𝒫f\mathcal{P}_{\mathrm{f}}and backward𝒫b\mathcal{P}_{\mathrm{b}}pulse forming in simulating the propagation of a Gaussian-shaped signal in media optically less dense than vacuum under optimal choice of the Courant number.
The dashed-dotted curve11corresponds to the case ofSc=nr=10−1S_{\mathrm{c}}=n_{\mathrm{r}}=10^{-1}, the solid line22—Sc=nr=10−2S_{\mathrm{c}}=n_{\mathrm{r}}=10^{-2}.

## 4Limits of applicability of the main results

In conclusion of this work, let us discuss the question of the applicability of the results obtained here beyond the domain of definition (34).

First, we point out that the interval of values0<εr,μr<10<\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}}<1included in the domain of definition (34), used when fulfilling the conditions of Statement3, in itself already extends the range of applicability of the computational algorithm developed in this work to the region of exotic media usually not considered in the literature.

Second, we note that our numerical algorithm (2) – (5) remains valid also when extending the domain of definition (34) to the intervalεr,μr∈(−∞,+∞)\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}}\in(-\infty,+\infty)under the condition of simultaneous negativity of the medium permittivitiesεr​μr>0\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}>0.

Media with simultaneously negative permittivities, as is known[27,20,1], are called left-handed.
In such media, backward waves can propagate[23], determined by the fact that for them the scalar product of the wave vector𝐤\mathbf{k}(in our work everywhere𝐤=β​𝐞x\mathbf{k}=\beta\mathbf{e}_{x}) and the Umov–Poynting vector𝐒\mathbf{S}is negative(𝐤⋅𝐒)<0,\left(\mathbf{k}\cdot\mathbf{S}\right)<0,(39)

where the energy flux carried by the wave, and determined by the vector𝐒\mathbf{S}, is equal to[3,10,22,27,11]𝐒=c4​π​[𝐄×𝐇].\mathbf{S}=\frac{c}{4\pi}\left[\mathbf{E}\times\mathbf{H}\right].(40)

The validity of such a generalization is demonstrated by Fig.8, which presents the results of comparing the wave packets formed by the same signal source as in Figs.1,5–7, recorded at the same timeq=100q=100, when propagating in a right-handed medium withεr=μr=+1\varepsilon_{\mathrm{r}}=\mu_{\mathrm{r}}=+1(bottom half of the figure) and in a left-handed medium withεr=μr=−1\varepsilon_{\mathrm{r}}=\mu_{\mathrm{r}}=-1(top half).Figure 8:Instantaneous snapshots of forward (bottom half) and backward (top half) waves propagating in the Yee grid according to the computational algorithm (2) – (5).

It is easy to verify that for the wave packet shown in the upper part of Fig.8the Umov–Poynting vector (40)𝐒⇅𝐞x\mathbf{S}\updownarrows\mathbf{e}_{x}, which is precisely what defines the backward wave according to condition (39).

And finally, let us explain that the validity of the algorithm (2) – (5) when extending the domain of definition (34) to the intervalεr,μr∈(−∞,+∞)\varepsilon_{\mathrm{r}},\mu_{\mathrm{r}}\in(-\infty,+\infty)under the condition of non-simultaneous negativity of the medium permittivitiesεr​μr<0\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}<0was not investigated in this work.
This is due to the fact that atεr​μr<0\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}<0the propagation constant (25) turns out to be an imaginary quantity, which corresponds to a strong attenuation of waves in such media, which as a result turn out to be strongly dispersive (for them, the propagation of plane waves turns out to be impossible, and along with this Statement2loses its simple meaning, which requires a different formulation in this case).
All this goes beyond the scope of this work.

## Conclusion

Thus, in this work the phenomenon of numerical dispersion in FDTD modeling of electromagnetic signal propagation in nondispersive homogeneous media has been investigated.
Several statements are formulated that determine the character of this dispersion, and the influence of the Courant number on it is also described.
The optimal value of the Courant number that eliminates the numerical dispersion of wave packets is determined.
The limits of applicability of the developed simulation method are investigated, and for the first time the possibility of its application to media optically less dense than vacuum, as well as to left-handed media, is indicated.

At the same time, the topic of the research still remains quite interesting, since many interesting questions were not investigated in this article, some of which are listed below.

## Some open questions
- 1.

What can explain from a physical point of view the decrease in the accuracy of the FDTD calculation in media withnr<1n_{\mathrm{r}}<1?
An explanation similar to the situation in media for whichnr>1n_{\mathrm{r}}>1, and based on the decrease in the wavelength in them (and, accordingly, its poor discretization), does not work here.
- 2.

What is the reason for the formation of the backward pulse𝒫b\mathcal{P}_{b}and how can it be eliminated?
Perhaps it is a consequence of some analytical errors made when writing (2) – (5) or of the unavoidable errors of floating-point machine representation of numbers in computer calculations.
- 3.

Is it possible to correct numerical dispersion when simulating the propagation of signals in inhomogeneous media?
Can this be achieved by changing the Courant number dynamically during the simulation?

This list of interesting questions does not claim to be complete in any way, and can well be expanded.

## Acknowledgement (state task)

The work was done in frames of the State task of the Institute of Physics and Mathematics FRC Komi SC UB RAS on the research topic # 122040400069-8.

## References
- [1]V. M. Agranovich and Yu. N. Gartstein(2006)Spatial dispersion and negative refraction of light.Phys. Usp.49,pp. 1029–1044.Cited by:§1,§4.
- [2]S. Bakirtzis, T. Hashimoto, and C. D. Sarris(2021)FDTD-based diffuse scattering and transmission models for ray tracing of millimeter-wave communication systems.IEEE Trans. AP69(6),pp. 3389–3398.Cited by:Introduction.
- [3]M. M. Bredov, V. V. Rumyantsev, and I. N. Toptygin(1985)Classical electrodynamics.Nauka,Moscow.Cited by:§1,§2,§2,§4,Remark 4.
- [4]A. Fantoni, P. Loureniço, and M. Vieira(2017)A model for the refractive index of amorphous silicon for FDTD simulation of photonics waveguides.InInternational Conference on Numerical Simulation of Optoelectronic Devices (NUSOD), Copenhagen, Denmark,pp. 167–168.Cited by:Introduction.
- [5]S. Flügge(1974)Practical quantum mechanics, vol. I.Mir,Moscow.Cited by:§2,Remark 6.
- [6]S. Glubokovskikhet al.(2016)Seismic monitoring of CO2geosequestration: CO2CRC Otway case study using full 4D FDTD approach.International Journal of Greenhouse Gas Control49,pp. 201–216.Cited by:Introduction.
- [7]U. S. Inan and R. A. Marshall(2011)Numerical electromagnetics. the FDTD method.Cambridge University Press,Cambridge.Cited by:§1,Introduction,Introduction.
- [8]N. V. Karlov and N. A. Kirichenko(2008)Oscillations, waves, structures.Fizmatlit,Moscow.Cited by:§2,Remark 6.
- [9]G. L. Kotkin, V. G. Serbo, and A. I. Chernykh(2017)Lectures on analytic mechanics.NITc RChD,Moscow, Izhevsk.Cited by:§2,Remark 6.
- [10]A. M. Kugushev, N. S. Golubeva, and V. N. Mitrohin(2001)Fundamentals of radioelectronics. electrodynamics and radio waves propagation.Bauman Moscow State Technical University Press,Moscow.Cited by:§1,§2,§2,§4,Remark 4.
- [11]G. S. Landsberg(2010)Optics.Fizmatlit,Moscow.Cited by:§4,Corollary 3.
- [12]H. P. Langtangen and S. Linge(2017)Finite difference computing with PDEs: a modern software approach.Springer,Cham.Cited by:§1,§1,§1,§1,Introduction,Introduction,Introduction,Remark 3,Remark 7.
- [13]P. A. Makarov, V. A. Ustyugov, and V. I. Shcheglov(2022)Modelling of electromagnetic wave propagation in magnetically inhomogeneous media.Proceedings of the Komi Science Centre of the Ural Branch of the Russian Academy of Sciences. Series <<Physical and Mathematical Sciences>>(5 (57)),pp. 100–105.Cited by:§1,§1,Introduction.
- [14]P. A. Makarov, V. A. Ustyugov, and V. I. Shcheglov(2023)Numerical solution features of Maxwell equations by FDTD method in the homogeneous and non-homogeneous formulations of the problems.Proceedings of the Komi Science Centre of the Ural Branch of the Russian Academy of Sciences. Series <<Physical and Mathematical Sciences>>(4 (62)),pp. 96–107.Cited by:§1,§1,§1,§1,§1,§1,§3,Introduction,Remark 1,Remark 2,Remark 2.
- [15]P. Makarovet al.(2022)Simulation of electromagnetic wave propagation in magnetic randomly inhomogeneous magnetic media.IEEE Magnetics Letters13,pp. 1–5.Cited by:§1,§1,Introduction.
- [16]C. S. Mishraet al.(2019)FDTD approach to photonic based angular waveguide for wide range of sensing application.Optik176,pp. 56–59.Cited by:Introduction.
- [17]Y. Miyazaki and K. Kouno(2009)FDTD analysis of spatial filtering of scattered waves for optical CT of medical diagnosis.IEEJ Trans. FM129(10),pp. 693–698.Cited by:Introduction.
- [18]S. P. Mohanty, S. K. Sahoo, A. Panda, and G. Palai(2019)FDTD method to photonic waveguides for application of optical demultiplexer at 3-communication windows.Optik185,pp. 146–150.Cited by:Introduction.
- [19]A. B. S. Nzao(2022)Analysis and FDTD modeling of the influences of microwave electromagnetic waves on human biological systems.Open Journal of Applied Sciences12,pp. 912–929.Cited by:Introduction.
- [20]J. Pendry(2004)Negative refraction.Contemporary Physics45(3),pp. 191–202.Cited by:§1,§4.
- [21]J. B. Schneider(2010)Understanding the finite-difference time-domain method.www.eecs.wsu.edu/˜schneidj/ufdtd.Cited by:§1,§1,§1,§1,§1,§2,Introduction,Introduction,Introduction,Remark 3,Remark 7.
- [22]A. Schuster(1935)An introduction to the theory of optics.ONTI, main. ed. all-tech. lit.,Leningrad, Moscow.Cited by:§1,§4.
- [23]V. V. Shevchenko(2007)Forward and backward waves: three definitions and their interrelation and applicability.Phys. Usp.50,pp. 287–292.Cited by:§4.
- [24]J. Starket al.(2016)Light scattering microscopy measurements of single nuclei compared with GPU-accelerated FDTD simulations.Phys. Med. Biol.61(7),pp. 2749–2761.Cited by:Introduction.
- [25]A. Taflove, A. Oskooi, and S. G. Johnson(2013)Advances in FDTD computational electrodynamics photonics and nanotechnology.Artech House,Boston.Cited by:§1,Introduction,Introduction.
- [26]T. Tan, A. Taflove, and V. Backman(2013)Single realization stochastic FDTD for weak scattering waves in biological random media.IEEE Trans. AP61(2),pp. 818–828.Cited by:Introduction.
- [27]V. G. Veselago(1968)The electrodynamics of substances with simultaneously negative values ofε\varepsilonandμ\mu.Sov. Phys. Usp.10,pp. 509–514.Cited by:§1,§4,§4.
- [28]M. B. Vinogradova, O. V. Rudenko, and A. P. Suhorukov(1979)Wave theory.Nauka,Moscow.Cited by:§1,§2,Remark 6.
- [29]K. Yee(1966)Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media.IEEE Trans. on Ant. and Prop.14(3),pp. 302–307.Cited by:§1,Introduction.
- [30]J. Yu, R. Malekian, J. Chang, and B. Su(2017)Modeling of Whole-Space transient electromagnetic responses based on FDTD and its application in the mining industry.IEEE Trans. Indust. Inform.13(6),pp. 2974–2982.Cited by:Introduction.

## 


- 


Major funding support from
