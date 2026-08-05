# Probing nonlocal superconducting fluctuations with covariance noise magnetometry

**arXiv ID**: 2607.24906v1
**Authors**: Gustav Romare, Ilya Esterlis, Shimon Kolkowitz, Alex Levchenko
**Published**: 2026-07-27
**Categories**: cond-mat.supr-con, quant-ph
**Comments**: 16 pages, 9 figures
**HTML URL**: https://arxiv.org/html/2607.24906v1

## Abstract

The nonlocal superconducting fluctuation corrections to the conductivity tensor $σ_{ij}(\mathbf{q},ω)$ are calculated within the time-dependent Ginzburg-Landau framework, and their observable consequences for quantum noise magnetometry are worked out. For a single nitrogen-vacancy (NV) sensor we obtain the relaxation rate $1/T_1$ as a function of temperature, sample-sensor distance, and probe frequency, identifying the scales at which the nonlocality and the dynamics of the pair fluctuations cut off the critical enhancement near $T_c$. For two-sensor covariance magnetometry we show that the two-point field correlator develops additional spatial structure whose range directly measures the fluctuation correlation length $ξ(T)$. We further analyze two channels that accompany the paraconductivity: the Maki-Thompson correction to the spin susceptibility, and the fluctuation diamagnetism. Finally, we solve exactly, to all orders in a dc electric field and at all wave vectors, for the nonequilibrium current noise of the fluctuating film: the noise decouples from the nonlinear paraconductivity, violating the fluctuation-dissipation theorem by universal factors at criticality and acquiring a bias-induced spatial anisotropy directly measurable by covariance magnetometry. The results are connected to a recent experiment measuring current noise near a thin film of BSCCO.

## Full Text

Probing nonlocal superconducting fluctuations with covariance noise magnetometry

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.24906v1 [cond-mat.supr-con] 27 Jul 2026

## Probing nonlocal superconducting fluctuations with covariance noise magnetometryGustav RomareDepartment of Physics, University of Wisconsin-Madison, Madison, Wisconsin 53706, USAIlya EsterlisDepartment of Physics, University of Wisconsin-Madison, Madison, Wisconsin 53706, USAShimon KolkowitzUniversity of California at Berkeley, Department of Physics, Berkeley CA 94720, USAAlex LevchenkoDepartment of Physics, University of Wisconsin-Madison, Madison, Wisconsin 53706, USA

## Abstract

The nonlocal superconducting fluctuation corrections to the conductivity tensorσi​j​(𝐪,ω)\sigma_{ij}(\mathbf{q},\omega)are calculated within the time-dependent Ginzburg-Landau framework, and their observable consequences for quantum noise magnetometry are worked out. For a single nitrogen-vacancy (NV) sensor we obtain the relaxation rate1/T11/T_{1}as a function of temperature, sample-sensor distance, and probe frequency, identifying the scales at which the nonlocality and the dynamics of the pair fluctuations cut off the critical enhancement nearTcT_{c}. For two-sensor covariance magnetometry we show that the two-point field correlator develops additional spatial structure whose range directly measures the fluctuation correlation lengthξ​(T)\xi(T). We further analyze two channels that accompany the paraconductivity: the Maki-Thompson correction to the spin susceptibility, and the fluctuation diamagnetism. Finally, we solve exactly, to all orders in a dc electric field and at all wave vectors, for the nonequilibrium current noise of the fluctuating film: the noise decouples from the nonlinear paraconductivity, violating the fluctuation-dissipation theorem by universal factors at criticality and acquiring a bias-induced spatial anisotropy directly measurable by covariance magnetometry. The results are connected to a recent experiment measuring current noise near a thin film of BSCCO.††preprint:APS/123-QED

## IIntroduction

Near the superconducting transition, reduced dimensionality and short coherence lengths enhance pair fluctuation effects, which manifest in both thermodynamic and dynamical propertiesLarkin and Varlamov (2005); Varlamovet al.(2018). Fluctuation effects are well-documented in a variety of systems, including amorphousGlover (1971); Pourretet al.(2006)and crystallineKajimura and Mikoshiba (1971); Hsu and Kapitulnik (1992)thin films of conventional superconductorsSkocpol and Tinkham (1975), high-TcT_{c}cupratesVidalet al.(1988); Rullier-Albenqueet al.(2011); Cimberleet al.(1997); Hopfengärtneret al.(1991); Mandalet al.(1990); Duanet al.(1991), and superconductors based on two-dimensional van der Waals materialsSonget al.(2024).

Fluctuation corrections to the conductivity in particular arise through the Aslamazov-Larkin (AL) paraconductivityAslamazov and Larkin (1968), Maki-Thompson (MT) interference effectsMaki (1968); Thompson (1970), and density of states suppressionAbrahamset al.(1970). In general, the fluctuation conductivity—which encodes the low-energy dynamics of superconductors nearTcT_{c}—is a nonlocal, dynamical response function,σi​j​(𝐪,ω)\sigma_{ij}(\mathbf{q},\omega), that depends on both wave vector𝐪\mathbf{q}and frequencyω\omega. Conventional dc transport measurements probe only its long-wavelength, low-frequency limit,𝐪→0\mathbf{q}\to 0andω→0\omega\to 0, and consequently access only a small part of the information contained in the full fluctuation response. That information is considerable: the momentum dependence ofσi​j​(𝐪,ω)\sigma_{ij}(\mathbf{q},\omega)encodes the fluctuation correlation lengthξ​(T)\xi(T)and its critical divergence, while the frequency dependence encodes the order-parameter relaxation timeτGL\tau_{\rm GL}—the critical slowing down near the transition. A probe with access to finite(𝐪,ω)(\mathbf{q},\omega)can therefore measure static and dynamical critical properties, distinguish Gaussian from vortex-dominated (Berezinskii-Kosterlitz-Thouless) fluctuation regimes through the functional form ofξ​(T)\xi(T), separate intrinsic critical correlations from static, disorder-induced inhomogeneity, and—once driven out of equilibrium—expose physics with no counterpart in linear transport, such as the breakdown of the fluctuation-dissipation theorem (FDT) in the pair-fluctuation channel. Developing this program quantitatively is the purpose of the present paper.

Recent measurements of current noise near thin films of BSCCO have revealed signatures of pronounced superconducting fluctuations aroundTcT_{c}Liuet al.(2025); related experiments have also been recently carried out on NbLiet al.(2026). These experiments measured the relaxation rate1/T11/T_{1}of nitrogen-vacancy (NV) centers—point-like defects in diamond that act as single-spin (or qubit) magnetometers—placed near the sample surface as a function of temperatureTT. Magnetic field sensing with NV centers has been used in recent years to study a variety of static and dynamical phenomena in condensed matter systemsCasolaet al.(2018); Rovnyet al.(2024); Thielet al.(2019); Bhattacharyyaet al.(2024); Kuet al.(2020); Duet al.(2017); Andersenet al.(2019). In particular, measurements of NV relaxation rates have been proposed as a noninvasive probe of material properties, such as nonlocal conductivity, that are challenging to extract via conventional methodsAgarwalet al.(2017); Rustagiet al.(2020); Machadoet al.(2023), with example systems including superconductorsChatterjeeet al.(2022); Dolgirevet al.(2022); Curtiset al.(2024), magnetic insulatorsChatterjeeet al.(2019), one-dimensional quantum liquidsRodriguez-Nievaet al.(2018), and electron solidsDolgirevet al.(2024). A schematic of the experimental setup is shown in Fig.1.Figure 1:Schematic of the setup. Two NV sensors at heightddabove a two-dimensional superconductor, separated by an in-plane distanceRR, detect the magnetic noise generated by fluctuating Cooper pairs of sizeξ​(T)\xi(T). Single-sensor relaxometry measures the local field autocorrelation; covariance magnetometry measures the two-point correlator⟨Bz​(𝐫1)​Bz​(𝐫2)⟩ω\langle B_{z}(\mathbf{r}_{1})B_{z}(\mathbf{r}_{2})\rangle_{\omega}, which resolves the spatial structure of the fluctuations.

Here, we calculate the AL contribution toσi​j​(𝐪,ω)\sigma_{ij}(\mathbf{q},\omega)and the corresponding magnetic field noise generated near the sample, using the time-dependent Ginzburg-Landau (TDGL) formalismSchmid (1966); Larkin and Varlamov (2005). Closed-form results for the nonlocal fluctuation electromagnetic response were in fact obtained within TDGL already in the early 1990s, see Ref.Barash and Galaktionov (1993)for bulk superconductors and Ref.Galaktionov (1995)for thin filmsGalaktionov (1995); we make contact with those results below and extend them to the noise observables of interest here. We reproduce the theoretical results presented in Ref.Liuet al.(2025)for the dependence of1/T11/T_{1}on temperature, and extend them to include the variation of the relaxation rate with qubit-sample distance and qubit frequency. We also analyze the contribution to magnetic noise from spin (as opposed to current) fluctuations. We then show that the recently developed covariance magnetometry techniqueRovnyet al.(2022); Leet al.(2025); Rovnyet al.(2025); Chenget al.(2025); Huxteret al.(2025); Cambriaet al.(2025); Hosseinabadiet al.(2026)provides a particularly promising route for measuring nonlocal pair fluctuation effects. Going beyond the paraconductivity, we also quantify the fluctuation diamagnetism and argue that it is measurable with current NV magnetometers. Finally, we solve exactly for thenonequilibriumcurrent noise of the fluctuating film under a dc bias, obtaining the universal violation of the FDT in the pair-fluctuation channel.

The paper is organized as follows. SectionIIreviews the TDGL calculation of the nonlocal AL conductivity. SectionIIIdevelops the single-NV relaxometry, including the dependence on distance, frequency, and the spin (MT) channel. SectionIVtreats two-sensor covariance magnetometry. SectionVanalyzes fluctuation diamagnetism, and Sec.VIthe nonequilibrium noise and FDT breakdown. SectionVIIsummarizes the main results, and Sec.VIIIconcludes with a discussion. Further technical details are relegated to AppendicesA–D.

## IINonlocal fluctuation conductivity

In this section, we briefly review the TDGL approach to AL paraconductivity and summarize the connection between the nonlocal conductivity and the relevant quantities measured in NV experiments.

The AL contribution can be captured by TDGL theory, which gives the order parameter dynamics as[γ​∂∂t−∇22​m+a]​Ψ​(𝐫,t)=ζ​(𝐫,t).\left[\gamma\frac{\partial}{\partial t}-\frac{\nabla^{2}}{2m}+a\right]\Psi(\mathbf{r},t)=\zeta(\mathbf{r},t).(1)

Hereγ\gammadetermines the order-parameter relaxation rate,a​(T)=α​(T/Tc−1)a(T)=\alpha(T/T_{c}-1)andζ​(𝐫,t)\zeta(\mathbf{r},t)is a Langevin force with white noise correlations,⟨ζ​(𝐫,t)​ζ∗​(𝐫′,t′)⟩=2​γ​T​δ​(𝐫−𝐫′)​δ​(t−t′)\langle\zeta(\mathbf{r},t)\zeta^{*}(\mathbf{r}^{\prime},t^{\prime})\rangle=2\gamma T\delta(\mathbf{r}-\mathbf{r}^{\prime})\delta(t-t^{\prime}). Here and below,eeandmmdenote the charge and mass of a Cooper pair (e→2​e0e\to 2e_{0}andm→2​mem\to 2m_{e}in terms of the electron values) and we have setℏ=1\hbar=1,kB=1k_{B}=1. Eq. (1) can be solved using the Green’s function methodΨ​(𝐫,t)=∫𝒢​(𝐫,t;𝐫′,t′)​ζ​(𝐫′,t′)​dd​𝐫′​dt′,\Psi(\mathbf{r},t)=\int\mathcal{G}(\mathbf{r},t;\mathbf{r}^{\prime},t^{\prime})\zeta(\mathbf{r}^{\prime},t^{\prime})\mathrm{d}^{d}\mathbf{r}^{\prime}\mathrm{d}t^{\prime},(2)

with𝒢\mathcal{G}given in Fourier representation by𝒢​(𝐪,ω)=1ε𝐪−i​γ​ω,ε𝐪=𝐪22​m+a.\mathcal{G}(\mathbf{q},\omega)=\frac{1}{\varepsilon_{\mathbf{q}}-i\gamma\omega},\quad\varepsilon_{\mathbf{q}}=\frac{\mathbf{q}^{2}}{2m}+a.(3)

With this we can also construct the fluctuation propagator,Π​(𝐱1;𝐱2)=2​γ​T​∫𝒢​(𝐫1,t1;𝐫1′,t1′)​𝒢∗​(𝐫2,t2;𝐫1′,t1′)​dd​𝐫1′​dt1′\Pi(\mathbf{x}_{1};\mathbf{x}_{2})=2\gamma T\int\mathcal{G}(\mathbf{r}_{1},t_{1};\mathbf{r}^{\prime}_{1},t^{\prime}_{1})\mathcal{G}^{*}(\mathbf{r}_{2},t_{2};\mathbf{r}^{\prime}_{1},t^{\prime}_{1})\mathrm{d}^{d}\mathbf{r}^{\prime}_{1}\mathrm{d}t^{\prime}_{1}(4)

which has the Fourier representationΠ​(𝐩,ε)=2​γ​Tε𝐩2+γ2​ε2.\Pi(\mathbf{p},\varepsilon)=\frac{2\gamma T}{\varepsilon^{2}_{\mathbf{p}}+\gamma^{2}\varepsilon^{2}}.(5)

We are now in a position to calculate the conductivity tensor. The fluctuation dissipation theorem relates the current fluctuationCi​jJ​J=1/2​⟨{Ji,Jj}⟩=⟨Ji​Jj⟩C^{JJ}_{ij}=1/2\langle\{J_{i},J_{j}\}\rangle=\langle J_{i}J_{j}\rangleto the retarded responseχi​jJ​J\chi^{JJ}_{ij}byCi​jJ​J(𝐪,ω)=coth(ω2​T)Im{χi​jJ​J(𝐪.ω)}C^{JJ}_{ij}(\mathbf{q},\omega)=\coth\left(\frac{\omega}{2T}\right)\text{Im}\left\{\chi^{JJ}_{ij}(\mathbf{q}.\omega)\right\}(6)

The retarded response can be related to the conductivity tensor asχi​jJ​J=i​ω​σi​j\chi^{JJ}_{ij}=i\omega\sigma_{ij}and we findRe​σi​j​(𝐪,ω)=12​T​Ci​jJ​J​(𝐪,ω),\text{Re}\,\sigma_{ij}(\mathbf{q},\omega)=\frac{1}{2T}C^{JJ}_{ij}(\mathbf{q},\omega),(7)

where we expanded the hyperbolic function inω/T≪1\omega/T\ll 1. The currentJiJ_{i}entering the current correlation function is given by the usual GL expression,Ji​(𝐫,t)=e2​m​i​[Ψ∗​∇iΨ−Ψ​∇iΨ∗].J_{i}(\mathbf{r},t)=\frac{e}{2mi}[\Psi^{*}\nabla_{i}\Psi-\Psi\nabla_{i}\Psi^{*}].(8)

In Fourier space, this becomesJi​(q)=em​∫pi​Ψ​(p+q/2)​Ψ∗​(p−q/2)​dd+1​p(2​π)d+1,J_{i}(q)=\frac{e}{m}\int p_{i}\Psi(p+q/2)\Psi^{*}(p-q/2)\frac{\mathrm{d}^{d+1}p}{(2\pi)^{d+1}},(9)

where we used 4-vector notationq≡(𝐪,Ω)q\equiv(\mathbf{q},\Omega)andp≡(𝐩,ε)p\equiv(\mathbf{p},\varepsilon). The conductivity tensor can now be expressed using the fluctuation propagator asRe​σi​j​(k)=e22​m2​T​∫pi​pj​Π​(p+k/2)​Π​(p−k/2)​dd+1​p(2​π)d+1.\text{Re}\,\sigma_{ij}(k)=\frac{e^{2}}{2m^{2}T}\int\ p_{i}p_{j}\Pi(p+k/2)\Pi(p-k/2)\ \frac{\mathrm{d}^{d+1}p}{(2\pi)^{d+1}}.(10)

The imaginary part of the conductivity can be restored by Kramers-Kronig. The integrals can be performed for general momentum and frequency (see AppendixB); for brevity, below we will quote thed=2d=2static results. Assuming an isotropic system, the conductivity can be decomposed into its transverse and longitudinal partsσi​j​(κ)=σA​L​[(δi​j−κ^i​κ^j)​FT(2​D)​(κ)+κ^i​κ^j​FL(2​D)​(κ)],\sigma_{ij}(\kappa)=\sigma^{AL}\left[(\delta_{ij}-\hat{\kappa}_{i}\hat{\kappa}_{j})F_{T}^{(2D)}(\kappa)+\hat{\kappa}_{i}\hat{\kappa}_{j}F_{L}^{(2D)}(\kappa)\right],

with the dimensionless functions,FL(2​D)​(κ)\displaystyle F_{L}^{(2D)}(\kappa)=ln⁡(1+κ2)κ2,\displaystyle=\frac{\ln(1+\kappa^{2})}{\kappa^{2}}\;,(11)FT(2​D)​(κ)\displaystyle F_{T}^{(2D)}(\kappa)=2κ​1+κ2​arcsinh​κ−ln⁡(1+κ2)κ2.\displaystyle=\frac{2}{\kappa\sqrt{1+\kappa^{2}}}\,\mathrm{arcsinh}\,\kappa-\frac{\ln(1+\kappa^{2})}{\kappa^{2}}.(12)

Hereκ=𝐤​ξ/2\kappa=\mathbf{k}\xi/2is a dimensionless momentum vector withξ2​(T)=1/2​m​a\xi^{2}(T)=1/2mabeing the superconducting correlation length andσAL=γ​kB​T​e2​m​ξ24​π.\sigma^{\text{AL}}=\frac{\gamma k_{B}Te^{2}m\xi^{2}}{4\pi}.(13)

With the microscopic value of the TDGL relaxation constant,γ=π​α/8​kB​Tc\gamma=\pi\alpha/8k_{B}T_{c}Larkin and Varlamov (2005), Eq. (13) reduces to the universal Aslamazov-Larkin sheet conductivityσAL=e02/16​ℏ​ϵ\sigma^{\rm AL}=e_{0}^{2}/16\hbar\epsilon(restoringℏ\hbar), withe0e_{0}the electron charge andϵ=(T−Tc)/Tc\epsilon=(T-T_{c})/T_{c}. The static transverse kernel Eq. (12) coincides with the thin-film fluctuation response derived in Ref.Galaktionov (1995); the correspondence extends to finite frequency and to the reactive (diamagnetic) part of the kernel, as discussed in Sec.Vand AppendixD. Below we will make use of the limiting behaviors of functionFTF_{T}:FT​(κ)→{1−5​κ2/6,κ≪1,ln⁡(4)/κ2,κ≫1.F_{T}(\kappa)\to\begin{cases}1-5\kappa^{2}/6,&\kappa\ll 1,\\
\ln(4)/\kappa^{2},&\kappa\gg 1.\end{cases}(14)

The relevant physical observable for both qubit noise spectroscopy and covariance magnetometry based on NV centers is the magnetic noise tensor𝒩α​β​(𝐫,ω)=12​∫−∞∞dt​ei​ω​t​⟨{Bα​(𝐫,t),Bβ​(0,0)}⟩.\displaystyle\mathcal{N}_{\alpha\beta}(\mathbf{r},\omega)=\frac{1}{2}\int_{-\infty}^{\infty}\mathrm{d}t~e^{i\omega t}\langle\{B_{\alpha}(\mathbf{r},t),B_{\beta}(0,0)\}\rangle.(15)

The noisy magnetic fieldBα​(𝐫,t)B_{\alpha}(\mathbf{r},t)is related to fluctuating currents in the nearby 2D system by the Biot-Savart law. Combining this relation with the fluctuation-dissipation theorem yields an expression for the noise tensor in terms of the transverse conductivity111Strictly speaking, this formula also assumesΩ​d≪c\Omega d\ll c, whereccis the speed of light in vacuum. ForΩ∼GHz\Omega\sim\text{GHz}andd∼d\simtens of nm—the typical operating regime of single NV centers—this inequality is well-satisfied.(see AppendixA) . We focus on the component𝒩z​z​(𝐑,z,ω)\displaystyle\mathcal{N}_{zz}(\mathbf{R},z,\omega)=μ02​kB​T4​π​∫0∞dq​q​J0​(R​q)​e−2​q​z​σT′​(q,ω).\displaystyle=\frac{\mu_{0}^{2}k_{B}T}{4\pi}\int_{0}^{\infty}\mathrm{d}q\,qJ_{0}(Rq)e^{-2qz}\sigma^{\prime}_{T}(q,\omega).(16)

Here𝐫=(𝐑,z)\mathbf{r}=(\mathbf{R},z), with𝐑\mathbf{R}the 2D position vector in the plane of the material andzzthe distance above the plane;σT′\sigma^{\prime}_{T}denotes the real part of the transverse conductivity.

## IIILocal noiseFigure 2:(a) Transverse noise as a function of reduced temperatureϵ=(T−Tc)/Tc\epsilon=(T-T_{c})/T_{c}for different values of NV distanced/ξ0d/\xi_{0}. The dashed line corresponds toϵ−1\epsilon^{-1}divergence. (b) Effective exponentx=−d​ln⁡(𝒩z​z)/d​ln⁡ϵx=-d\ln(\mathcal{N}_{zz})/d\ln\epsilonof the divergence nearTcT_{c}.Figure 3:(a) Scaling behavior ford/ξ0≪1d/\xi_{0}\ll 1. The graph shows the local noise𝒩z​z\mathcal{N}_{zz}as a function of NV separation in units of the coherence lengthd/ξ0d/\xi_{0}for different values of the reduced temperature. The red dashed line is the logarithmic limiting behavior in Eq. (21). (b) Scaling relation ford/ξ0≫1d/\xi_{0}\gg 1. The red dashed line is theξ2​(T)/4​d2\xi^{2}(T)/4d^{2}limiting behavior in Eq. (21).Figure 4:Noise for various finite probe frequenciesω\omega. The noise saturates to a finite value below a reduced temperatureϵω∼ω/ω0\epsilon_{\omega}\sim\omega/\omega_{0}, whereω0=1/m​γ​ξ02\omega_{0}=1/m\gamma\xi_{0}^{2}. Inset: The frequency dependence of the noise atTcT_{c}. For largeω/ω0\omega/\omega_{0}, the noise decays∝1/ω\propto 1/\omega.

We start with the case of noise detection at a single point above the plane, which corresponds to setting𝐑=0\mathbf{R}=0in (16). The local noise𝒩z​z​(z,ω)≡𝒩z​z​(𝐑=0,z,ω)\mathcal{N}_{zz}(z,\omega)\equiv\mathcal{N}_{zz}(\mathbf{R}=0,z,\omega)is directly related to the relaxation rate1/T11/T_{1}of a NV center placed a distancez=dz=dabove the material with level-splittingω\omegaLangsjoenet al.(2012); Agarwalet al.(2017); for details see AppendixA. We have𝒩z​z​(z=d,ω)=μ02​kB​T4​π​∫0∞dq​q​e−2​q​d​σT′​(q,ω).\mathcal{N}_{zz}(z=d,\omega)=\frac{\mu_{0}^{2}k_{B}T}{4\pi}\int_{0}^{\infty}\mathrm{d}q\,qe^{-2qd}\sigma^{\prime}_{T}(q,\omega).(17)

Here and below we restorekBk_{B}.
For a rough estimate of the noise, note that the integration kernel is peaked at a wave vectorq∼1/2​dq\sim 1/2d, so that𝒩z​z​(d,ω)∼μ02​kB​Td2​σT′​(q⋆=12​d,Ω).\mathcal{N}_{zz}(d,\omega)\sim\frac{\mu_{0}^{2}k_{B}T}{d^{2}}\,\sigma^{\prime}_{T}\!\Big(q_{\star}=\frac{1}{2d},\,\Omega\Big).(18)

Local noise measurements thus probe the nonlocal conductivity at a single wave vector
selected by the sample-to-detector distance.

We now consider the AL correction to𝒩z​z​(d,ω)\mathcal{N}_{zz}(d,\omega). Here we observe that, in an NV experiment, the frequencyω\omegais typically a few GHz, so that the relevant dimensionless combinationω​τGL≪1\omega\tau_{\rm GL}\ll 1over most of the accessible temperature range and we may set the frequency to zero inσT′\sigma^{\prime}_{T}(see below for a discussion of the frequency dependence). Inserting the zero-frequency result (12) into (17) we obtain the AL fluctuation correction𝒩z​zAL​(d)=μ0216​π​kB​T​σALd2​∫0∞dx​x​e−x​FT​(ξ0​x4​d​ϵ)\mathcal{N}^{\rm AL}_{zz}(d)=\frac{\mu_{0}^{2}}{16\pi}\frac{k_{B}T\sigma^{\rm AL}}{d^{2}}\int_{0}^{\infty}\mathrm{d}x\,xe^{-x}F_{T}\left(\frac{\xi_{0}x}{4d\sqrt{\epsilon}}\right)(19)

where𝒩z​zAL​(d)≡𝒩z​zAL​(d,ω=0)\mathcal{N}_{zz}^{\rm AL}(d)\equiv\mathcal{N}_{zz}^{\rm AL}(d,\omega=0)andξ0=1/2​m​α\xi_{0}=1/\sqrt{2m\alpha}, so thatξ​(T)=ξ0/ϵ\xi(T)=\xi_{0}/\sqrt{\epsilon}.

For reference, we also record the relaxation rate deep in the metallic normal state,𝒩z​z0​(d,ω)\mathcal{N}^{0}_{zz}(d,\omega), where the qubit relaxation is due to evanescent Johnson noiseLangsjoenet al.(2012); Kolkowitzet al.(2015)𝒩z​z0​(d,ω=0)=μ0216​π​kB​T​σ0d2.\mathcal{N}^{0}_{zz}(d,\omega=0)=\frac{\mu_{0}^{2}}{16\pi}\frac{k_{B}T\sigma_{0}}{d^{2}}.(20)

Hereσ0\sigma_{0}is the ordinary dc sheet conductivity of the metal; this follows from Eq. (17) withσT′=σ0\sigma^{\prime}_{T}=\sigma_{0}and∫0∞q​e−2​q​d​dq=1/4​d2\int_{0}^{\infty}qe^{-2qd}\mathrm{d}q=1/4d^{2}.

We begin by investigating the expression Eq. (19) for the fluctuation contribution to the local noise in different limits. The argument ofFTF_{T}in the integrand contains the mean-field correlation lengthξ​(T)=ξ0/ϵ\xi(T)=\xi_{0}/\sqrt{\epsilon}, setting the natural length scale for the “close” detectord<ξ​(T)d<\xi(T)and the “distant” detectord>ξ​(T)d>\xi(T)regimes.
In the extreme limits, we find from Eq. (19)𝒩z​zAL​(d)∼σAL×{14​d2​[1−5​ξ2​(T)16​d2],d≫ξ​(T),8​ln⁡2ξ2​(T)​ln⁡[ξ​(T)c1​d],d≪ξ​(T),\mathcal{N}^{\rm AL}_{zz}(d)\sim\sigma^{\rm AL}\times\begin{cases}\dfrac{1}{4d^{2}}\left[1-\dfrac{5\,\xi^{2}(T)}{16\,d^{2}}\right],&d\gg\xi(T),\\[8.61108pt]
\dfrac{8\ln 2}{\xi^{2}(T)}\,\ln\!\left[\dfrac{\xi(T)}{c_{1}\,d}\right],&d\ll\xi(T),\end{cases}(21)

where the constantc1c_{1}under the logarithm is determined numerically asc1≈9.1c_{1}\approx 9.1SinceσAL∝ξ​(T)2∼1/ϵ\sigma^{\rm AL}\propto\xi(T)^{2}\sim 1/\epsilon, we see that, for a fixed detector distancedd, the local noise—and hence the single-NV relaxation rate—will grow as1/(T−Tc)1/(T-T_{c})as the system is cooled from the normal state; this behavior was observed in the1/T11/T_{1}measurements of Ref.Liuet al.(2025). This growth with decreasingTTwill continue untilξ​(T)>d\xi(T)>d, when the noise will cross over to the much slower logarithmic growth (note thatσAL/ξ2​(T)\sigma^{\rm AL}/\xi^{2}(T)is temperature independent); this regime is sensitive to theqq-dependence ofσT′\sigma_{T}^{\prime}. The offset constant in Eq. (21) shows that the logarithmic regime is fully developed only onceξ​(T)≳10​d\xi(T)\gtrsim 10\,d.

In Fig.2a we plot our numerical results for𝒩z​zAL​(d)\mathcal{N}_{zz}^{\rm AL}(d)obtained by numerical integration of Eq. (19), where the limiting behaviors (21) are also verified. In Fig.2b we also show the “apparent exponent” in the growth of the noise asT→TcT\to T_{c},x=−d​log⁡(𝒩z​zAL)/d​log⁡ϵx=-d\log(\mathcal{N}_{zz}^{\rm AL})/d\log\epsilon. From the figure it is clearly seen that the1/(T−Tc)1/(T-T_{c})scaling of the noise persists over a broader temperature range the further the detector is from the sample.

The probe frequencyω\omegaalso defines a certain length scaleξω∼kB​Tc/ℏ​ω×ξ0\xi_{\omega}\sim\sqrt{k_{B}T_{c}/\hbar\omega}\times\xi_{0}that serves to cut off the divergence of the noise asT→TcT\to T_{c}; a similar observation regarding the ac conductivity was made inDorsey (1991). The length scaleξω\xi_{\omega}corresponds roughly to the distance over which a fluctuation diffuses over the time scale1/ω1/\omegaset by the probe frequency. This translates to a reduced temperatureϵω∼ℏ​ω/kB​Tc\epsilon_{\omega}\sim\hbar\omega/k_{B}T_{c}below which the noise saturates to a finite value controlled byω\omega. The saturation criterion can equivalently be stated asω​τGL∼1\omega\tau_{\rm GL}\sim 1, withτGL=π​ℏ/8​kB​(T−Tc)\tau_{\rm GL}=\pi\hbar/8k_{B}(T-T_{c})the GL relaxation time. The evolution of the noise asT→TcT\to T_{c}for non-zero frequencies is shown in Fig.4. Close toTcT_{c}, the noise decreases with frequency asRe​FT∼1/ω\mathrm{Re}\,F_{T}\sim 1/\omegaat largeω\omega(see inset of Fig.4and AppendixB, Fig.9). Using a probe frequencyω≈3​GHz\omega\approx 3~{\rm GHz}andTc≈90T_{c}\approx 90K appropriate for the BSCCO NV experimentLiuet al.(2025), we estimate a reduced temperatureϵω∼10−3\epsilon_{\omega}\sim 10^{-3}below which noise should saturate. Since the NV splitting is field-tunable over∼1\sim 1–55GHz, frequency-resolved relaxometry directly measures the critical slowing downτGL​(ϵ)\tau_{\rm GL}(\epsilon), a quantity inaccessible to dc transport.

## III.1Spin channel: Maki-Thompson contribution

Except in very clean metals, the MT corrections to the fluctuationconductivityare much smaller than the AL corrections and we have thus ignored them. However, NV relaxation is also influenced by magnetic noise from spin fluctuations in the materialAgarwalet al.(2017); Chatterjeeet al.(2019), which are in turn related to the imaginary part of the spin susceptibilityχ′′\chi^{\prime\prime}, and in this channel the fluctuation physics enters through the anomalous MT process—the pairing of an electron with its time-reversed partner—analyzed for the NMR relaxation rate by Randeria and VarlamovRanderia and Varlamov (1994). The MT correction to the dissipative spin response is built from the product of the fluctuation propagator and the Cooperon and, in two dimensions, takes the formδ​χMT′′​(𝐪,ω)ω|ω→0=χ0′′​(ω)ω​βMT​ln⁡(ϵ/γϕ)ϵ−γϕ​𝒦​(q),\frac{\delta\chi^{\prime\prime}_{\text{MT}}(\mathbf{q},\omega)}{\omega}\bigg|_{\omega\to 0}=\frac{\chi^{\prime\prime}_{0}(\omega)}{\omega}\,\beta_{\rm MT}\,\frac{\ln(\epsilon/\gamma_{\phi})}{\epsilon-\gamma_{\phi}}\,\mathcal{K}(q),(22)

whereχ0′′/ω=π​ν02\chi^{\prime\prime}_{0}/\omega=\pi\nu_{0}^{2}is the normal-state (Korringa) value,γϕ=π​ℏ/8​kB​T​τϕ\gamma_{\phi}=\pi\hbar/8k_{B}T\tau_{\phi}is the pair-breaking parameter set by the phase-relaxation timeτϕ\tau_{\phi},βMT=𝒪​(G​i)\beta_{\rm MT}=\mathcal{O}(Gi)is a positive constant of order the Ginzburg number, and𝒦​(q)\mathcal{K}(q)is a form factor with𝒦​(0)=1\mathcal{K}(0)=1that decays forq≳min⁡(ξ−1,Lϕ−1)q\gtrsim\min(\xi^{-1},L_{\phi}^{-1}), withLϕ=ξ0/γϕL_{\phi}=\xi_{0}/\sqrt{\gamma_{\phi}}the dephasing length. The singular factor follows from the elementary pair-momentum integral∫d2​Q(2​π)2​[(ϵ+ξ2​Q2)​(γϕ+ξ2​Q2)]−1=ln⁡(ϵ/γϕ)/[4​π​ξ2​(ϵ−γϕ)]\int\!\frac{\mathrm{d}^{2}Q}{(2\pi)^{2}}[(\epsilon+\xi^{2}Q^{2})(\gamma_{\phi}+\xi^{2}Q^{2})]^{-1}=\ln(\epsilon/\gamma_{\phi})/[4\pi\xi^{2}(\epsilon-\gamma_{\phi})]. Considering, for simplicity, the regime where the detector heightd>ξd>\xi, the contribution to the noise from spin fluctuations is𝒩s∼μ02​μB2​T/d4×[δ​χMT′′​(0,ω)/ω]ω→0\mathcal{N}_{s}\sim\mu_{0}^{2}\mu_{B}^{2}T/d^{4}\times[\delta\chi_{\rm MT}^{\prime\prime}(0,\omega)/\omega]_{\omega\to 0}.

Two features are noteworthy. First, the MT enhancement grows as∼(1/ϵ)​ln⁡(ϵ/γϕ)\sim(1/\epsilon)\ln(\epsilon/\gamma_{\phi})forϵ≫γϕ\epsilon\gg\gamma_{\phi}butsaturatesatϵ∼γϕ\epsilon\sim\gamma_{\phi}: pair breaking cuts off the divergence, in analogy with the distance and frequency cutoffs of the orbital channel. Second, for a sign-changing (dd-wave) order parameter, as in BSCCO, the anomalous MT term is strongly suppressed, and the accompanying negative density-of-states correction,δ​(1/T1​T)DOS∝−ln⁡(1/ϵ)\delta(1/T_{1}T)_{\rm DOS}\propto-\ln(1/\epsilon), can dominate the spin channelRanderia and Varlamov (1994)—so that a near-TcT_{c}peakin the NV relaxation is a fingerprint of the orbital (paraconductivity) channel.

For the two-sensor covariance introduced in the next section, the same structure implies a spin-channel covariance𝒩s​(R)∝K0​(R/ξ)−K0​(R/Lϕ)Lϕ−2−ξ−2,\mathcal{N}_{s}(R)\propto\frac{K_{0}(R/\xi)-K_{0}(R/L_{\phi})}{L_{\phi}^{-2}-\xi^{-2}},(23)

a difference of modified Bessel functions whose spatial range is set by thelongerofξ​(T)\xi(T)andLϕL_{\phi}. In the regimeϵ>γϕ\epsilon>\gamma_{\phi}, where the MT enhancement operates, one hasξ​(T)<Lϕ\xi(T)<L_{\phi}, so the spin covariance decays on the dephasing length—which is only weakly temperature dependent—in sharp contrast to the orbital channel, whose range tracks the strongly temperature-dependentξ​(T)\xi(T). Covariance magnetometry can thus, in principle, disentangle the two channels by their range and its temperature dependence, and thereby extract the electronic dephasing length.

## IVTwo-point correlations and connection to covariance magnetometry

In NV covariance magnetometryRovnyet al.(2022), two NV centers are read out simultaneously, shot by shot, and the observable is the covariance of the two photon records, normalized as the Pearson coefficientr=Cov​(S1,S2)/σ1​σ2r=\mathrm{Cov}(S_{1},S_{2})/\sigma_{1}\sigma_{2}. Because the local photon shot noise and single-NV spin-projection noise are uncorrelated between the sensors, they cancel from the covariance, which isolates thesharedmagnetic signal produced by the sample. For phase-accumulation (Ramsey- or echo-type) protocols with filter functionW​(t)W(t), the covariance of the accumulated phases measuresγNV2​∫d​ω2​π​|W~​(ω)|2​𝒩z​z​(R,d,ω)\gamma_{\rm NV}^{2}\int\frac{\mathrm{d}\omega}{2\pi}|\tilde{W}(\omega)|^{2}\,\mathcal{N}_{zz}(R,d,\omega), withγNV=g​μB/ℏ\gamma_{\rm NV}=g\mu_{B}/\hbar; for relaxometry-mode covariance, the correlated part of the two decay rates measures the cross-spectral density at the NV splittingLeet al.(2025); Hosseinabadiet al.(2026); Rovnyet al.(2025). In either mode the measured correlations are governed by the two-point magnetic correlation function in Eq. (16), withr​(R)=𝒩z​z​(R)/[𝒩z​z​(0)+Nloc]r(R)=\mathcal{N}_{zz}(R)/[\mathcal{N}_{zz}(0)+N_{\rm loc}], withNlocN_{\rm loc}the local (uncorrelated) noise floor.
Notice tha the Bessel factorJ0​(q​R)J_{0}(qR)in Eq. (16) oscillates on the scaleq∼1/Rq\sim 1/R, so that varying the sensor separation scans the nonlocal conductivity in wave-vector space. We show below that, where the single-sensor rate saturates onceξ​(T)\xi(T)exceedsdd(see Eq. (21)), the covariance resolves the very structure responsible for that saturation

(i) Metallic regime.Deep in the metallic phase (or, nearTcT_{c}, wheneverξ​(T)≪d\xi(T)\ll d), the conductivity is local at the probed momenta,σT′→σ0\sigma^{\prime}_{T}\to\sigma_{0}, and the transform (16) is elementary:𝒩z​z​(R)𝒩z​z​(0)=[1+(R2​d)2]−3/2.\frac{\mathcal{N}_{zz}(R)}{\mathcal{N}_{zz}(0)}=\left[1+\left(\frac{R}{2d}\right)^{2}\right]^{-3/2}.(24)

The covariance is flat forR≲2​dR\lesssim 2dand falls as1/R31/R^{3}forR≫2​dR\gg 2d—a purely geometric profile whose range is set by the standoff distance alone and is strictly temperature independent; only the overall amplitude,∝kB​T​σ0\propto k_{B}T\sigma_{0}(Johnson noise), varies. (We ignore the ballistic regime where the mean free pathℓ>d\ell>dKolkowitzet al.(2015), which is irrelevant for the materials of interest.) A temperature-dependent change in theshapeofr​(R)r(R)therefore signals a growing correlation length.

(ii) Fluctuation regime.InsertingσT′=σAL​FT​(q​ξ/2)\sigma^{\prime}_{T}=\sigma^{\rm AL}F_{T}(q\xi/2)into Eq. (16), the covariance profile develops additional structure onceξ​(T)≫d\xi(T)\gg d(Fig.5):𝒩z​zAL​(R)≃μ02​kB​T​σAL4​π×{8​ln⁡2ξ2​[ln⁡ξR+c0],2​d≪R≪ξ,2​dR3,R≫ξ,\mathcal{N}^{\rm AL}_{zz}(R)\simeq\frac{\mu_{0}^{2}k_{B}T\sigma^{\rm AL}}{4\pi}\times\begin{cases}\dfrac{8\ln 2}{\xi^{2}}\Big[\ln\dfrac{\xi}{R}+c_{0}\Big],&2d\ll R\ll\xi,\\[6.45831pt]
\dfrac{2d}{R^{3}},&R\gg\xi,\end{cases}(25)

withc0c_{0}an𝒪​(1)\mathcal{O}(1)constant. In the window2​d≪R≪ξ​(T)2d\ll R\ll\xi(T)the covariance decays only logarithmically, with an amplitude that is independent of the reduced temperature (sinceσAL/ξ2=γ​T​e2​m/4​π\sigma^{\rm AL}/\xi^{2}=\gamma Te^{2}m/4\pi). AtR∼ξ​(T)R\sim\xi(T)the profile is cut off and can be well-approximated by an expression involving modified Bessel functions (see AppendixAfor details). For the largest separations the profile always reverts to the universal Ohmic tail∝2​d​σAL/R3\propto 2d\,\sigma^{\rm AL}/R^{3}, generated by the linear-in-qqterm of the evanescent kernele−2​q​de^{-2qd}; its prefactor contains the full1/ϵ1/\epsilondivergence of the paraconductivity. These regimes
are verified numerically in Fig.5.Figure 5:(a) Normalized covariance𝒩z​z​(R)/𝒩z​z​(0)\mathcal{N}_{zz}(R)/\mathcal{N}_{zz}(0)at fixed distanceddfor increasingξ/d\xi/d; the dashed curve is the exact local (metallic) form, Eq. (24). The range of the covariance grows with the correlation length. (b) Deep in the fluctuation regime (ξ=200​ξ0\xi=200\,\xi_{0},d=0.25​ξ0d=0.25\,\xi_{0}) the regimes of Eq. (25) are visible: logarithmic window (black dashed), and Ohmic tail2​d​ξ2/R32d\xi^{2}/R^{3}(dash-dotted).

## VFluctuation diamagnetism

The conductivity is the dissipative part of the fluctuation electromagnetic response; its reactive counterpart is the fluctuation diamagnetismSchmid (1969); Prange (1970); Kurkijärviet al.(1972); Larkin and Varlamov (2005), known to be large in the cupratesLiet al.(2010). It is natural to ask—particularly for an NV magnetometry experiment—whether fluctuating diamagnetic moments constitute an additional source of magnetic noise, and whether the diamagnetic response itself is detectable. To make more quantitative contact with experiment, in this section we also consider layered superconductors in the regimeξc≪ac\xi_{c}\ll a_{c}, whereξc\xi_{c}is the coherence length in the perpendicularcc-direction andaca_{c}is thecc-axis lattice constant.

The Gaussian fluctuation susceptibility of a 2D superconducting layer follows from the Landau-level spectrum of the pair fluctuations (AppendixD); per layer,χA​(T)=−π3​kB​T​ξ2​(T)Φ02∝−1ϵ,\chi_{A}(T)=-\frac{\pi}{3}\frac{k_{B}T\,\xi^{2}(T)}{\Phi_{0}^{2}}\;\propto\;-\frac{1}{\epsilon},(26)

withΦ0=h​c/2​e0\Phi_{0}=hc/2e_{0}the flux quantum. In a layered superconductor1/ϵ→[ϵ​(ϵ+r)]−1/21/\epsilon\to[\epsilon(\epsilon+r)]^{-1/2}, with the Lawrence-Doniach anisotropy parameterr=4​ξc2​(0)/ac2r=4\xi^{2}_{c}(0)/a_{c}^{2}.
The fluctuation diamagnetism is thus exactly as singular as the paraconductivity—both are governed byξ2​(T)\xi^{2}(T)—and, relative to its normal-state background (the Landau diamagnetism), it is parametrically muchlargerthan the conductivity correction relative to the Drude backgroundLarkin and Varlamov (2005).
The nonlocal generalizationχ​(Q)=χA​G​(Q​ξ/2)\chi(Q)=\chi_{A}\,G(Q\xi/2), withG​(0)=1G(0)=1andG​(x)≃3​ln⁡(2​x)/x2G(x)\simeq 3\ln(2x)/x^{2}atx≫1x\gg 1, was obtained in Ref.Galaktionov (1995), whose thin-film kernel in fact contains ourFT​(κ,ϖ)F_{T}(\kappa,\varpi)as its dissipative part (AppendixD).Figure 6:(a) Fluctuation susceptibility (26): 2D versus Lawrence-Doniach (r=0.04r=0.04). (b) Nonlocal scaling functionG​(q)G(q)ofχ​(Q)\chi(Q)Galaktionov (1995), with the edge-healing profileM​(x)M(x)(inset). (c) Estimated edge stray field versusϵ\epsilonfor the BSCCO flake geometry of Ref.Liuet al.(2025)at two applied fields, compared with single-NV and ensemble dc sensitivity bands.

(i) No new noise at zero field.—A divergence-free sheet current and an out-of-plane magnetization density are the same degree of freedom:𝐊=c​∇×(Mz​z^)\mathbf{K}=c\,\nabla\times(M_{z}\hat{z})impliesKT​(𝐪)=i​c​q​Mz​(𝐪)K_{T}(\mathbf{q})=icqM_{z}(\mathbf{q}), henceSKT​KT​(𝐪,ω)=c2​q2​SMz​Mz​(𝐪,ω).S_{K_{T}K_{T}}(\mathbf{q},\omega)=c^{2}q^{2}\,S_{M_{z}M_{z}}(\mathbf{q},\omega).(27)

The equilibrium magnetic noise of the fluctuating diamagnetic loops is thereforeidenticallythe transverse-current Johnson noise already encoded inσT′​(q,ω)\sigma^{\prime}_{T}(q,\omega): Eq. (16) contains all of it, and no double counting (or additional channel) arises at zero applied field. We have also checked that the noise generated at finite applied field by fluctuations of the local susceptibility (δ​M=H​δ​χ\delta M=H\,\delta\chi, sourced by|Ψ|2|\Psi|^{2}fluctuations) is negligible, smaller than the AL current noise by orders of magnitude at attainable fields.

(ii) Measurable response in an applied field.—What is measurable is the diamagnetic response itself. In a perpendicular fieldHHthe film acquires an areal magnetizationMA=Nℓ​χA​(T)​HM_{A}=N_{\ell}\,\chi_{A}(T)\,H(NℓN_{\ell}= number of superconducting layers in the flake). A uniform infinite sheet produces no stray field, but edges, holes, andTcT_{c}inhomogeneities do: near a straight edge the bound currentI=c​MAI=cM_{A}produces a stray field|δ​B|∼2​MA/d|\delta B|\sim 2M_{A}/dat heightdd, with the edge profile healed over the lengthξ​(T)/2\xi(T)/2Galaktionov (1995). For the geometry of Ref.Liuet al.(2025)(Tc=90T_{c}=90K,ξ0≈2\xi_{0}\approx 2nm, flake thickness 200 nm soNℓ≈130N_{\ell}\approx 130,z=50z=50nm),|δ​B|edge≈6.3​nTϵ​(ϵ+r)×μ0​H10​mT,|\delta B|_{\rm edge}\approx\frac{6.3~\text{nT}}{\sqrt{\epsilon(\epsilon+r)}}\times\frac{\mu_{0}H}{10~\text{mT}},(28)

which reaches∼0.3​μ\sim 0.3~\muT atϵ=10−2\epsilon=10^{-2}and remains above ensemble NV dc sensitivities (sub-nT) up toϵ∼0.5\epsilon\sim 0.5, i.e., tens of kelvin aboveTcT_{c}(Fig.6). The measurement mode is the ESR line shift (dc magnetometry)—previously used for NV Meissner imagingBhattacharyyaet al.(2024)—rather than relaxometry; field reversalH→−HH\to-Hflips the signal and provides clean lock-in background rejection; the response stays linear inHHup toh≡H/Hc​2​(0)∼ϵh\equiv H/H_{c2}(0)\sim\epsilon. Beyond detection, spatial maps carry quantitative information: the edge-healing profile (Fig.6) measuresξ​(T)\xi(T)directly, and interior maps ofχA​(ϵ​(𝐫))\chi_{A}(\epsilon(\mathbf{r}))can be used to image local-TcT_{c}disorder.

## VINonequilibrium fluctuation noise

All results so far concern equilibrium noise, where the FDT ties the current fluctuations to the dissipative conductivity, Eq. (6). A dc electric field drives the fluctuation gas out of equilibrium. The nonlinear response was computed within TDGL by DorseyDorsey (1991)(following early work in Refs.Hurault (1969); Schmidt (1968)) and beyond linear response the noise is no longer tied to the conductivity. Their difference is a direct, quantitative measure of the departure of the driven fluctuations from equilibrium. In this section we solve for the nonequilibrium current noise exactly—to all orders in the field and at all wave vectors—within Gaussian TDGL, and quantify the FDT violation. Details of the derivation are given in AppendixC.

(i) Exact solution—In a uniform field (𝐀=−c​𝐄​t\mathbf{A}=-c\mathbf{E}t,𝐄=E​x^\mathbf{E}=E\hat{x}) the linearized TDGL remains diagonal in the canonical momentum: each mode is an Ornstein-Uhlenbeck process with a “sliding” relaxation rate,γ​∂tΨ𝐩=−ε​(𝐩+e​𝐄​t)​Ψ𝐩+ζ𝐩\gamma\partial_{t}\Psi_{\mathbf{p}}=-\varepsilon(\mathbf{p}+e\mathbf{E}t)\Psi_{\mathbf{p}}+\zeta_{\mathbf{p}}. The two-time correlator is therefore exact [Eq. (65)], with the driven mode occupationN​(𝐏)=⟨Ψ𝐩​Ψ𝐩∗⟩N(\mathbf{P})=\langle\Psi_{\mathbf{p}}\Psi^{*}_{\mathbf{p}}\ranglereproducing Eq. (24) of Ref.Dorsey (1991). The mean current recovers Dorsey’s nonlinear paraconductivity: in 2D,σ​(E)≡J/E=σAL​Σ+​(E/E0)\sigma(E)\equiv J/E=\sigma^{\rm AL}\Sigma_{+}(E/E_{0})withΣ+​(x)=∫0∞du​e−u−x2​u3\Sigma_{+}(x)=\int_{0}^{\infty}\mathrm{d}u\,e^{-u-x^{2}u^{3}}and the threshold fieldE0=12​ℏ2​e​ξ​(T)​τGL∝ϵ3/2,E_{0}=\frac{\sqrt{12}\,\hbar}{2e\xi(T)\tau_{\rm GL}}\;\propto\;\epsilon^{3/2},(29)

so that at criticalityσ​(E)∝E−2/3\sigma(E)\propto E^{-2/3}. We use the equivalent dimensionless fieldf=4​3​E/E0=2​e​E​ξ​τGL/ℏf=4\sqrt{3}\,E/E_{0}=2eE\xi\tau_{\rm GL}/\hbar, the work done by the field across a coherence length during a GL lifetime.

Because the solution is Gaussian in𝐏\mathbf{P}at fixed time arguments, Wick factorization reduces the symmetrized current noise at any wave vector to an explicit three-fold quadrature; see AppendixC, Eq. (67).

(ii) FDT breakdown atk=0k=0—Define the FDT ratiosX∥=Sx​x/2​kB​T​σX_{\parallel}=S_{xx}/2k_{B}T\sigma,X∥diff=Sx​x/2​kB​T​σdiffX^{\rm diff}_{\parallel}=S_{xx}/2k_{B}T\sigma_{\rm diff}(withσdiff=d​J/d​E\sigma_{\rm diff}=\mathrm{d}J/\mathrm{d}E), andX⟂=Sy​y/2​kB​T​σX_{\perp}=S_{yy}/2k_{B}T\sigma; for an isotropic film the transverse differential conductivity equalsσdiff=σ\sigma_{\rm diff}=\sigmaexactly, and all three ratios equal unity in equilibrium. We find (Fig.7): at weak fields the FDT violation turns on quadratically,X∥=1+c∥​(E/E0)2,X⟂=1+c⟂​(E/E0)2,X_{\parallel}=1+c_{\parallel}\,(E/E_{0})^{2},\qquad X_{\perp}=1+c_{\perp}\,(E/E_{0})^{2},(30)

with constantsc∥≈4.96c_{\parallel}\approx 4.96andc⟂≈1.62c_{\perp}\approx 1.62,
while at strong fields—equivalently at criticality, whereϵeff∼(E/E0)2/3\epsilon_{\rm eff}\sim(E/E_{0})^{2/3}—they saturate atuniversal numbersof the 2D AL channel:X∥→X∥0≈1.83,X∥diff→3​X∥0X⟂→X⟂0≈1.18,X_{\parallel}\to X^{0}_{\parallel}\approx 1.83,\quad X^{\rm diff}_{\parallel}\to 3X^{0}_{\parallel}\quad X_{\perp}\to X_{\perp}^{0}\approx 1.18,(31)

the factor of 3 being exact sinceJ∝E1/3J\propto E^{1/3}atTcT_{c}. The driven fluctuation gas is “hotter” than Johnson-Nyquist at the measured conductivity, with an effective noise temperatureTeff=X∥0​TT_{\rm eff}=X_{\parallel}^{0}T(parallel) andTeff=X⟂0​TT_{\rm eff}=X_{\perp}^{0}T(transverse).
Physically, the field suppresses the response (a lifetime cutoff) more strongly than the noise, which weights the occupation squared; the noise therefore decays more slowly than2​kB​T​σ​(E)2k_{B}T\sigma(E).Figure 7:(a) Nonlinear AL conductivityΣ+​(E/E0)\Sigma_{+}(E/E_{0})Dorsey (1991)with the criticalE−2/3E^{-2/3}law; inset: the exact driven mode occupationn​(x∥,f)=N​(x∥,f)/N​(0,0)n(x_{\parallel},f)=N(x_{\parallel},f)/N(0,0), whose drift skew sources the anisotropic noise. (b) FDT ratiosX=SJ​J​(ω→0;E)/2​kB​T​σ​(E)X=S_{JJ}(\omega\to 0;E)/2k_{B}T\sigma(E)versusE/E0E/E_{0}; dotted lines mark the universal critical values, Eq. (31).

(iii) Bias-induced noise anisotropy at finitekk—At finite wave vector the driven transverse noise splits by orientation (Fig.8): fluctuations with𝐤∥𝐄\mathbf{k}\parallel\mathbf{E}are suppressed more strongly than those with𝐤⟂𝐄\mathbf{k}\perp\mathbf{E}, with the anisotropy ratio reaching∼1.05\sim 1.05,1.151.15, and1.301.30atf=1f=1,33, and1010forκ≲0.5\kappa\lesssim 0.5, and closing atκ≳2\kappa\gtrsim 2, where short-wavelength modes are stiffer than the drift scale. This is precisely the geometry that covariance magnetometry resolves: two NV sensors separated parallel versus perpendicular to an applied bias current measure different covariances, with a contrast of tens of percent atf∼1f\sim 1—a clear signature of nonequilibrium superconducting fluctuations. Combined with a conventional measurement ofσ​(E)\sigma(E)on the same device, the NV noise provides a direct experimental test of the FDT violation, Eq. (31). We note that a complementary covariance signature—anisotropic noise from vortex drift belowTcT_{c}—was proposed recently in Ref.Zhanget al.(2026); the present effect lives aboveTcT_{c}, where the theory is fully controlled.Figure 8:(a) Driven transverse noiseST​(κ;E)S_{T}(\kappa;E)for𝐤∥𝐄\mathbf{k}\parallel\mathbf{E}(solid) and𝐤⟂𝐄\mathbf{k}\perp\mathbf{E}(dashed); dotted: equilibriumFT​(κ)F_{T}(\kappa). (b) The bias-induced anisotropy ratio.

(iv) Why heating does not spoil the measurement—One might worry that applying a strong electric field simply leads to Joule heating, making the problem ill-defined. The key observation, however, is that the threshold field for the nonlinear response of the fluctuation Cooper pairs, Eq. (29), collapses rapidly asT→TcT\to T_{c},E0∝(T−Tc)3/2E_{0}\propto(T-T_{c})^{3/2}, whereas the nonlinearity (and heating) scales of the normal quasiparticle fluid are set by microscopic energies and are temperature independent in this window. Consequently, there is a parametrically broad regime in which the fluctuation contribution is driven deep into the nonlinear, non-equilibrium regime while the normal-state response remains strictly linear and the quasiparticle bath remains at the lattice temperature: the assumption of a fixed bath temperatureTTunderlying the TDGL Langevin dynamics is then self-consistent, and the fluctuation correction is cleanly separable, as it is precisely the part of the signal with the anomalous field, temperature, and wave-vector dependence derived above. Quantitatively,f=1f=1corresponds toE≈25E\approx 25V/cm for BSCCO atϵ=10−2\epsilon=10^{-2}(dropping asϵ3/2\epsilon^{3/2}closer toTcT_{c}), i.e., sheet current densities of a few A/m per layer—accessible with standard pulsed-bias techniques on narrow bridges, with duty cycling suppressing the average dissipated power. This opens the realistic possibility of experimentally probing the breakdown of the fluctuation-dissipation theorem through measurements of nonequilibrium current noise in the Cooper-pair fluctuation channel.

## VIISummary of main results

For convenience, we collect the main results of this work.

(i) Nonlocal paraconductivity.Within TDGL, the nonlocal AL paraconductivity has the closed formσi​j=σAL​[(δi​j−κ^i​κ^j)​FT+κ^i​κ^j​FL]\sigma_{ij}=\sigma^{\rm AL}[(\delta_{ij}-\hat{\kappa}_{i}\hat{\kappa}_{j})F_{T}+\hat{\kappa}_{i}\hat{\kappa}_{j}F_{L}], with thed=2d=2scaling functions of Eq. (12) and their finite-frequency generalization [AppendixB, Eq. (62)]; the kernel agrees with (and extends the observables associated to) the thin-film fluctuation electrodynamics of Refs.Barash and Galaktionov (1993); Galaktionov (1995).

(ii) Single-NV relaxometry.The critical enhancement1/T1∝1/ϵ1/T_{1}\propto 1/\epsilonobserved in Ref.Liuet al.(2025)follows from the 2D AL conductivity with mean-field exponent unity; it is rounded off belowtwodistinct scales—the distance scaleϵd∼(ξ0/d)2\epsilon_{d}\sim(\xi_{0}/d)^{2}(Eq. (21)) and the frequency scaleϵω∼ℏ​ω/kB​Tc\epsilon_{\omega}\sim\hbar\omega/k_{B}T_{c}—so that frequency-resolved relaxometry measures the critical slowing downτGL​(ϵ)\tau_{\rm GL}(\epsilon).

(iii) Covariance magnetometry.The two-point field correlator, Eq. (16), is a wave-vector-resolved probe: geometric and temperature independent in the metal (Eq. (24)), it develops the structure of Eq. (25) in the fluctuation regime, with a range that measuresξ​(T)\xi(T)—potentially enabling, e.g., a model-independent discrimination between Gaussian (ξ∝ϵ−1/2\xi\propto\epsilon^{-1/2}) and BKT (exponentialξ​(T)\xi(T)) fluctuation regimes.

(iv) Spin channel.The anomalous MT correction to the spin susceptibility, Eq. (22), produces a relaxation enhancement∝ln⁡(ϵ/γϕ)/(ϵ−γϕ)\propto\ln(\epsilon/\gamma_{\phi})/(\epsilon-\gamma_{\phi})cut off by pair breaking, and a covariance of rangeLϕL_{\phi}(Eq. (23)), separable from the orbital channel by its temperature dependence; fordd-wave BSCCO this channel is suppressed, identifying the observed noise peak as orbital.

(v) Fluctuation diamagnetism.At zero field, magnetization noise is not an additional channel (Eq. (27)); in an applied field, the diamagnetic response produces edge stray fields of order0.010.01–1​μ1~\muT (Eq. (28)), measurable by NV dc magnetometry tens of kelvin aboveTcT_{c}and yielding local maps ofξ​(T)\xi(T)andTcT_{c}disorder.

(vi) Nonequilibrium noise.The current noise of the driven fluctuation gas is obtained exactly to all orders in the bias and at all wave vectors (Eq. (67)); it violates the FDT by the universal critical ratios of Eq. (31) and acquires a bias-induced spatial anisotropy of tens of percent—both measurable with NV sensors, with the threshold fieldE0∝ϵ3/2E_{0}\propto\epsilon^{3/2}making the nonlinear fluctuation regime accessible at modest current densities while the normal fluid remains Ohmic.

The exact result obeys the finite-temperature critical scaling formSμ​ν=2​kB​T​σAL​(ϵ)​𝒮μ​ν​(k​ξ,ω​ξz,E​ξ1+z)S_{\mu\nu}=2k_{B}T\sigma^{\rm AL}(\epsilon)\,\mathcal{S}_{\mu\nu}(k\xi,\omega\xi^{z},E\xi^{1+z})with the
mean-field exponentsν=1/2\nu=1/2andz=2z=2of relaxational dynamics, the electric field entering only
through the combinationE​ξ1+zE\xi^{1+z}. In the critical limit the noise reduces toS=X∥∗​2​kB​T​σ​(E)S=X^{*}_{\parallel}\,2k_{B}T\,\sigma(E)withσ​(E)∝E−2/3\sigma(E)\propto E^{-2/3}and spectral weight collapsing on the scaleτE−1∝Ez/(1+z)\tau_{E}^{-1}\propto E^{z/(1+z)}—the thermal,z=2z=2counterpart of the universal
nonequilibrium noise scaling derived for thez=1z=1superconductor–insulator quantum critical pointGreenet al.(2006), whose formSj=T​Φ​[Teff​(E)/T]S_{j}=T\Phi[T_{\rm eff}(E)/T],Teff∝Ez/(1+z)T_{\rm eff}\propto E^{z/(1+z)}, is recovered here with the classical identificationTeff=X∗​TT_{\rm eff}=X^{*}T. Logarithmic factors in our expressions are confined to the asymptotics of the
scaling functions and do not modify the exponents.

## VIIIDiscussion

We have analyzed the contribution of SC fluctuations to the relaxation rate of single NV centers and covariance measurements of spatially separated NVs. In the case of an individual NV sensor, we have extended the theory presented in Ref.Liuet al.(2025)to account for the nonlocal, frequency-dependent paraconductivity, which determines the relaxation rate as a function of tip-to-sample distanceddand NV frequencyω\omega. The wave vector dependence of the paraconductivity is especially important in the regimed<ξ​(T)d<\xi(T). In the case of covariance measurements, we have shown how the nonlocal paraconductivity determines the scaling of the covariance with distanceRRbetween NVs; in the interesting regimed≪R≪ξ​(T)d\ll R\ll\xi(T), we find a slow logarithmic decay with temperature-independent amplitude, terminated by an exponential shoulder atR∼ξ​(T)R\sim\xi(T)whose decay length isξ​(T)/2\xi(T)/2, and ultimately by the universal Ohmic tail∝2​d​σAL/R3\propto 2d\,\sigma^{\rm AL}/R^{3}.

What new information about the superconducting state do these measurements provide? At the Gaussian level the AL noise is blind to the pairing symmetry—it measures lengths and times:ξ​(T)\xi(T)and its exponentν\nu(through the covariance range),τGL​(ϵ)\tau_{\rm GL}(\epsilon)and the dynamical exponentzdynz_{\rm dyn}(through the frequency cutoffϵω\epsilon_{\omega}), and the dephasing timeτϕ\tau_{\phi}(through the saturation of the MT spin channel). These are precisely the quantities that distinguish competing scenarios for two-dimensional superconductivity: a Gaussian correlation lengthξ∝ϵ−1/2\xi\propto\epsilon^{-1/2}versus the exponential BKT divergence versus 3D-XY criticality; relaxational versus propagating order-parameter dynamics; and intrinsic critical correlations versus static inhomogeneity, which produce covariance ranges with sharply different temperature dependence. Pairing symmetry enters indirectly but usefully: strong pair breaking in add-wave superconductor quenches the anomalous MT channel, and the diamagnetic response of Sec.Vadds an independent, response-based observable with its ownξ​(T)\xi(T)content. Out of equilibrium, the universal FDT-violation ratios, Eq. (31), characterize the driven pair-fluctuation gas itself and have no analogue in transport.

It is important to note that the Gaussian AL theory is controlled only when the fluctuation corrections are small compared to the normal state conductivity. In the experimentsLiuet al.(2025), the NV relaxation rate was found to increase by roughly an order of magnitude nearTcT_{c}. Per CuO2layer, the Gaussian expectation is(1/T1)fluct/(1/T1)0=R□​e02/16​ℏ​ϵ≈0.015/ϵ(1/T_{1})_{\rm fluct}/(1/T_{1})_{0}=R_{\square}e_{0}^{2}/16\hbar\epsilon\approx 0.015/\epsilonfor a normal-state sheet resistanceR□≈1R_{\square}\approx 1kΩ\Omega, reaching a tenfold enhancement only atϵ∼10−3\epsilon\sim 10^{-3}—far narrower than the observed few-kelvin peak. A more sophisticated theoretical treatment is thus required to explain the magnitude of this effect, taking into account the critical (BKT) nature of the 2D SC transitionCurtiset al.(2024)and, within the Ginzburg window, the self-consistent (Hartree) renormalization of the pair propagatorUllah and Dorsey (1991). We also note that the present framework can be straightforwardly extended to include the effects of an out-of-plane, orbital magnetic field by working in the Landau-level basis—a direction of immediate experimental relevance, given the field-dependent data already reported in Ref.Liuet al.(2025), and one that connects naturally to the diamagnetic response of Sec.V.

In this paper, we have only considered SC fluctuation effects aboveTcT_{c}. BelowTcT_{c}, the situation is more complex, as the noise is expected to receive contributions from both the amplitude and phase fluctuations of the order parameter, as well as collective modesCarlson and Goldman (1975); Schmid and Schön (1975). It will be interesting to understand whether nonlocal NV covariance magnetometry can shed light on the problem of collective modes in SCs.

Note added.—During the final stages of this work we became aware of a recent preprint by OrgadOrgad (2026), which addresses a closely related problem. Where the two works overlap—the equilibrium two-point (covariance) noise spectra generated by Gaussian superconducting fluctuations, the current noise to lowest order in an applied bias (linear order in the Ref.Orgad (2026)due to broken particle-hole symmetry), and bias-induced covariance anisotropy—we find complete agreement. The present work extends the analysis in several additional directions, including the Maki-Thompson spin channel and its covariance (Sec.III.1), the fluctuation-diamagnetism response channel (Sec.V), the exact all-order nonequilibrium current noise with its universal fluctuation-dissipation-violation ratios (Sec.VI), and the quantitative connection to the experiments of Ref.Liuet al.(2025).

## Acknowledgements.We thank Shubhayu Chatterjee for a discussion of the data in Ref.Liuet al.(2025)and Andrey Varlamov for pointing our attention to Ref.Barash and Galaktionov (1993). We are particularly grateful to Dror Orgad for valuable comments and for communicating with us regarding Ref.Orgad (2026). This work was supported by the U.S. Department of Energy (DOE), Office of Science, Basic Energy Sciences (BES) under Award No. DE-SC0020313.
A. L. acknowledges H. I. Romnes Faculty Fellowship provided by the University of Wisconsin-Madison Office of the Vice Chancellor for Research and Graduate Education with funding from the Wisconsin Alumni Research Foundation.
G.R. acknowledges financial support from the Sweden-America Foundation through the Ingegerd & Viking Olov Björks stipendiefond.
The authors acknowledges the use of Claude (Anthropic)Anthropic (2026)with manuscript preparation.

## References
- Larkin and Varlamov (2005)A. I. Larkin and A. A. Varlamov,Theory of fluctuations
in superconductors(Oxford University Press,
Oxford, 2005).
- Varlamovet al.(2018)A. A. Varlamov, A. Galda, and A. Glatz,Rev. Mod. Phys.90, 015009 (2018).
- Glover (1971)R. Glover,Physica55, 3 (1971).
- Pourretet al.(2006)A. Pourret, H. Aubin,
J. Lesueur, C. A. Marrache-Kikuchi, L. Bergé, L. Dumoulin, and K. Behnia,Nature
Physics2, 683 (2006).
- Kajimura and Mikoshiba (1971)K. Kajimura and N. Mikoshiba,Journal of Low Temperature Physics4, 331 (1971).
- Hsu and Kapitulnik (1992)J. W. P. Hsu and A. Kapitulnik,Phys. Rev. B45, 4819 (1992).
- Skocpol and Tinkham (1975)W. J. Skocpol and M. Tinkham,Reports on Progress in Physics38, 1049 (1975).
- Vidalet al.(1988)F. Vidal, J. A. Veira,
J. Maza, F. Garcia-Alvarado, E. Moran, and M. A. Alario,Journal of Physics C: Solid State Physics21, L599 (1988).
- Rullier-Albenqueet al.(2011)F. Rullier-Albenque, H. Alloul, and G. Rikken,Phys. Rev. B84, 014522 (2011).
- Cimberleet al.(1997)M. R. Cimberle, C. Ferdeghini, E. Giannini, D. Marré,
M. Putti, A. Siri, F. Federici, and A. Varlamov,Phys.
Rev. B55, R14745(R)
(1997).
- Hopfengärtneret al.(1991)R. Hopfengärtner, B. Hensel, and G. Saemann-Ischenko,Phys. Rev. B44, 741 (1991).
- Mandalet al.(1990)P. Mandal, A. Poddar,
A. Das, B. Ghosh, and P. Choudhury,Physica C: Superconductivity169, 43 (1990).
- Duanet al.(1991)H. M. Duan, W. Kiehl,
C. Dong, A. W. Cordes, M. J. Saeed, D. L. Viar, and A. M. Hermann,Phys.
Rev. B43, 12925
(1991).
- Songet al.(2024)T. Song, Y. Jia, G. Yu, Y. Tang, P. Wang, R. Singha, X. Gui,
A. J. Uzan-Narovlansky,
M. Onyszczak, K. Watanabe, T. Taniguchi, R. J. Cava, L. M. Schoop, N. P. Ong, and S. Wu,Nature Physics20, 269
(2024).
- Aslamazov and Larkin (1968)L. G. Aslamazov and A. I. Larkin,Phys. Lett. A26, 238 (1968).
- Maki (1968)K. Maki,Prog. Theor. Phys.39, 897 (1968).
- Thompson (1970)R. S. Thompson,Phys. Rev. B1, 327 (1970).
- Abrahamset al.(1970)E. Abrahams, M. Redi, and J. W. F. Woo,Phys. Rev. B1, 208 (1970).
- Liuet al.(2025)Z. Liu, R. Gong, J. Kim, O. K. Diessel, Q. Xu, Z. Rehfuss, X. Du, G. He, A. Singh, Y. S. Eo, E. A. Henriksen, G. D. Gu, N. Y. Yao, F. Machado, S. Ran, S. Chatterjee, and C. Zu,“Quantum noise spectroscopy of superconducting dynamics in thin film
Bi2Sr2CaCu2O8+δ,”(2025),arXiv:2502.04439 [cond-mat.supr-con].
- Liet al.(2026)S. Li, S. P. Kelly,
J. Zhou, H. Lu, Y. Tserkovnyak, H. Wang, and C. R. Du,Phys. Rev. Lett.136, 076004 (2026).
- Casolaet al.(2018)F. Casola, T. Van Der Sar,
 and A. Yacoby,Nat. Rev. Mater.3, 1 (2018).
- Rovnyet al.(2024)J. Rovny, S. Gopalakrishnan, A. C. B. Jayich, P. Maletinsky,
E. Demler, and N. P. de Leon,Nature Reviews Physics6, 753 (2024).
- Thielet al.(2019)L. Thiel, Z. Wang,
M. A. Tschudin, D. Rohner, I. Gutiérrez-Lezama, N. Ubrig, M. Gibertini, E. Giannini, A. F. Morpurgo, and P. Maletinsky,Science364, 973 (2019).
- Bhattacharyyaet al.(2024)P. Bhattacharyya, W. Chen,
X. Huang, S. Chatterjee, B. Huang, B. Kobrin, Y. Lyu, T. J. Smart, M. Block, E. Wang,
Z. Wang, W. Wu, S. Hsieh, H. Ma, S. Mandyam, B. Chen,
E. Davis, Z. M. Geballe, C. Zu, V. Struzhkin, R. Jeanloz, J. E. Moore, T. Cui, G. Galli, B. I. Halperin, C. R. Laumann, and N. Y. Yao,Nature627, 73
(2024).
- Kuet al.(2020)M. J. H. Ku, T. X. Zhou, Q. Li, Y. J. Shin, J. K. Shi, C. Burch, L. E. Anderson, A. T. Pierce, Y. Xie, A. Hamo, U. Vool, H. Zhang, F. Casola, T. Taniguchi, K. Watanabe, M. M. Fogler, P. Kim, A. Yacoby, and R. L. Walsworth,Nature583, 537 (2020).
- Duet al.(2017)C. Du, T. van der Sar,
T. X. Zhou, P. Upadhyaya, F. Casola, H. Zhang, M. C. Onbasli, C. A. Ross, R. L. Walsworth, Y. Tserkovnyak, and A. Yacoby,Science357, 195 (2017).
- Andersenet al.(2019)T. I. Andersen, B. L. Dwyer,
J. D. Sanchez-Yamagishi,
J. F. Rodriguez-Nieva,
K. Agarwal, K. Watanabe, T. Taniguchi, E. A. Demler, P. Kim, H. Park,et al.,Science364, 154
(2019).
- Agarwalet al.(2017)K. Agarwal, R. Schmidt,
B. Halperin, V. Oganesyan, G. Zaránd, M. D. Lukin, and E. Demler,Phys.
Rev. B95, 155107
(2017).
- Rustagiet al.(2020)A. Rustagi, I. Bertelli,
T. Van Der Sar, and P. Upadhyaya,Phys. Rev. B102, 220403 (2020).
- Machadoet al.(2023)F. Machado, E. A. Demler,
N. Y. Yao, and S. Chatterjee,Phys. Rev. Lett.131, 070801 (2023).
- Chatterjeeet al.(2022)S. Chatterjee, P. E. Dolgirev, I. Esterlis,
A. A. Zibrov, M. D. Lukin, N. Y. Yao, and E. Demler,Phys.
Rev. Res.4, L012001
(2022).
- Dolgirevet al.(2022)P. E. Dolgirev, S. Chatterjee, I. Esterlis, A. A. Zibrov, M. D. Lukin,
N. Y. Yao, and E. Demler,Phys. Rev. B105, 024507 (2022).
- Curtiset al.(2024)J. B. Curtis, N. Maksimovic,
N. R. Poniatowski,
A. Yacoby, B. Halperin, P. Narang, and E. Demler,Phys. Rev. B110, 144518 (2024).
- Chatterjeeet al.(2019)S. Chatterjee, J. F. Rodriguez-Nieva, and E. Demler,Phys. Rev. B99, 104425 (2019).
- Rodriguez-Nievaet al.(2018)J. F. Rodriguez-Nieva, K. Agarwal, T. Giamarchi,
B. I. Halperin, M. D. Lukin, and E. Demler,Phys.
Rev. B98, 195433
(2018).
- Dolgirevet al.(2024)P. E. Dolgirev, I. Esterlis,
A. A. Zibrov, M. D. Lukin, T. Giamarchi, and E. Demler,Phys. Rev. Lett.132, 246504 (2024).
- Schmid (1966)A. Schmid,Phys. Kondens. Materie5, 302 (1966).
- Barash and Galaktionov (1993)Y. S. Barash and A. V. Galaktionov,Phys. Rev. B48, 6284 (1993).
- Galaktionov (1995)A. V. Galaktionov,Physica C241, 118 (1995).
- Rovnyet al.(2022)J. Rovny, Z. Yuan,
M. Fitzpatrick, A. I. Abdalla, L. Futamura, C. Fox, M. C. Cambria, S. Kolkowitz, and N. P. de Leon,Science378, 1301 (2022).
- Leet al.(2025)X. H. Le, P. E. Dolgirev,
P. Put, E. L. Peterson, A. Pillai, A. A. Zibrov, E. Demler, H. Park, and M. D. Lukin,Phys. Rev. Lett.135, 170803 (2025).
- Rovnyet al.(2025)J. Rovny, S. Kolkowitz, and N. P. de Leon,Nature647, 876 (2025).
- Chenget al.(2025)K.-H. Cheng, Z. Kazi,
J. Rovny, B. Zhang, L. S. Nassar, J. D. Thompson, and N. P. de Leon,Phys. Rev. X15, 031014 (2025).
- Huxteret al.(2025)W. S. Huxter, F. Dalmagioni,
 and C. L. Degen,Phys. Rev. Lett.135, 153801 (2025).
- Cambriaet al.(2025)M. Cambria, S. Chand,
C. M. Reiter, and S. Kolkowitz,Phys. Rev. X15, 031015
(2025).
- Hosseinabadiet al.(2026)H. Hosseinabadi, P. E. Dolgirev, S. Gopalakrishnan, A. Yacoby, E. Demler, and J. Marino,“Theory of
two-qubitT2T_{2}spectroscopy of quantum many-body systems,”(2026),arXiv:2603.18176
[quant-ph].
- Note (1)Strictly speaking, this formula also assumesΩ​d≪c\Omega d\ll c, whereccis the speed of light in vacuum. ForΩ∼GHz\Omega\sim\text{GHz}andd∼d\simtens of nm—the typical operating regime of single
NV centers—this inequality is well-satisfied.
- Langsjoenet al.(2012)L. S. Langsjoen, A. Poudel,
M. G. Vavilov, and R. Joynt,Phys. Rev. A86, 010301 (2012).
- Kolkowitzet al.(2015)S. Kolkowitz, A. Safira,
A. High, R. Devlin, S. Choi, Q. Unterreithmeier, D. Patterson, A. Zibrov,
V. Manucharyan, H. Park,et al.,Science347, 1129 (2015).
- Dorsey (1991)A. T. Dorsey,Phys. Rev. B43, 7575 (1991).
- Randeria and Varlamov (1994)M. Randeria and A. A. Varlamov,Phys. Rev. B50, 10401(R) (1994).
- Schmid (1969)A. Schmid,Phys. Rev.180, 527 (1969).
- Prange (1970)R. E. Prange,Phys. Rev. B1, 2349 (1970).
- Kurkijärviet al.(1972)J. Kurkijärvi, V. Ambegaokar, and G. Eilenberger,Phys. Rev. B5, 868 (1972).
- Liet al.(2010)L. Li, Y. Wang, S. Komiya, S. Ono, Y. Ando, G. D. Gu, and N. P. Ong,Phys. Rev. B81, 054510 (2010).
- Hurault (1969)J. P. Hurault,Phys. Rev.179, 494 (1969).
- Schmidt (1968)H. Schmidt,Z. Phys.216, 336 (1968).
- Zhanget al.(2026)Y.-F. Zhang, R. Samajdar, and S. Gopalakrishnan,“Detecting vortex motion through spatially correlated nonequilibrium
noise,”(2026),arXiv:2605.18941 [cond-mat.supr-con].
- Greenet al.(2006)A. G. Green, J. E. Moore,
S. L. Sondhi, and A. Vishwanath,Phys. Rev. Lett.97, 227003 (2006).
- Ullah and Dorsey (1991)S. Ullah and A. T. Dorsey,Phys. Rev. B44, 262 (1991).
- Carlson and Goldman (1975)R. V. Carlson and A. M. Goldman,Phys. Rev. Lett.34, 11 (1975).
- Schmid and Schön (1975)A. Schmid and G. Schön,Phys. Rev. Lett.34, 941 (1975).
- Orgad (2026)D. Orgad,“Signatures of Gaussian superconducting fluctuations in nonlocal
noise magnetometry,”(2026),arXiv:2605.18970 [cond-mat.supr-con].
- Anthropic (2026)Anthropic, “Claude [large language model],”https://claude.ai(2026), version: Claude Fable 5; used June–July 2026.
- Cambriaet al.(2021)M. C. Cambria, A. Gardill,
Y. Li, A. Norambuena, J. R. Maze, and S. Kolkowitz,Phys. Rev. Res.3, 013123 (2021).
- Cambriaet al.(2023)M. C. Cambria, A. Norambuena,
H. T. Dinani, G. Thiering, A. Gardill, I. Kemeny, Y. Li, V. Lordi, A. Gali,
J. R. Maze, and S. Kolkowitz,Phys. Rev. Lett.130, 256903 (2023).

## Appendix AMagnetic noise tensor

The magnetic noise tensor𝒩a​b=⟨Ba​(𝐫1,z;t1)​Bb​(𝐫2,z;t2)⟩\mathcal{N}_{ab}=\langle B_{a}(\mathbf{r}_{1},z\,;t_{1})B_{b}(\mathbf{r}_{2},z\,;t_{2})\ranglecan be calculated directly using the Biot-Savart (BS) kernel,Ba​(𝐫,t)=∫ga​b​(𝐫−𝐫′)​Jb​(𝐫′,t)​d3​𝐫′.B_{a}(\mathbf{r},t)=\int g_{ab}(\mathbf{r}-\mathbf{r}^{\prime})J_{b}(\mathbf{r}^{\prime},t)\mathrm{d}^{3}\mathbf{r}^{\prime}.(32)

Using the fluctuation dissipation theorem we relate the noise to the response and using mode expansions we find,𝒩a​b​(𝐑,z,ω)=coth⁡(ω​β2)​∫ei​𝐑⋅𝐪​ga​a′​(𝐪)​gb​b′​(−𝐪)​ℑ⁡χa′​b′J​(𝐪,ω).\mathcal{N}_{ab}(\mathbf{R},z,\omega)=\coth\big(\frac{\omega\beta}{2}\big)\int e^{i\mathbf{R}\cdot\mathbf{q}}g_{aa^{\prime}}(\mathbf{q})g_{bb^{\prime}}(-\mathbf{q})\Im\chi_{a^{\prime}b^{\prime}}^{J}(\mathbf{q},\omega).(33)

The BS kernel can be found directly from Maxwell’s equations in the non-relativistic limit using the London gauge∇⋅𝐀=0\nabla\cdot\mathbf{A}=0,(q2−∂z2)​𝐀​(𝐪,z)=μ0​𝐉​(𝐪)​δ​(z)(q^{2}-\partial^{2}_{z})\mathbf{A}(\mathbf{q},z)=\mu_{0}\mathbf{J}(\mathbf{q})\delta(z)(34)

Solving this inhomogeneous DE inzzand taking the curl we find,Ba​(𝐪,z)=ga​b​(𝐪,z)​Jb​(𝐪),ga​b​(𝐪,z)=−μ02​e−q​z​[(i​𝐳^+𝐪^)×e^a]⋅e^bB_{a}(\mathbf{q},z)=g_{ab}(\mathbf{q},z)J_{b}(\mathbf{q}),\quad g_{ab}(\mathbf{q},z)=-\frac{\mu_{0}}{2}e^{-qz}[(i\hat{\mathbf{z}}+\hat{\mathbf{q}})\times\hat{e}_{a}]\cdot\hat{e}_{b}(35)

The current response is related to conductivity byχJ=i​ω​σ\chi^{J}=i\omega\sigmaand decomposing the conductivity tensor into the transverse and longitudinal parts we find, in the classical limitcoth⁡(ω​β/2)→2​kB​T/ℏ​ω\coth(\omega\beta/2)\to 2k_{B}T/\hbar\omega[the two-sided symmetrized convention,SKT​KT=2​kB​T​σT′S_{K_{T}K_{T}}=2k_{B}T\sigma^{\prime}_{T}, consistent with Eq. (6)],𝒩z​z​(𝐑,z,ω)\displaystyle\mathcal{N}_{zz}(\mathbf{R},z,\omega)=μ02​kB​T4​π​∫0∞dq​q​J0​(R​q)​e−2​q​z​σT′​(q,ω),\displaystyle=\frac{\mu_{0}^{2}k_{B}T}{4\pi}\int_{0}^{\infty}\mathrm{d}q\,qJ_{0}(Rq)e^{-2qz}\sigma^{\prime}_{T}(q,\omega),(36)𝒩x​x​(𝐑,z,ω)\displaystyle\mathcal{N}_{xx}(\mathbf{R},z,\omega)=μ02​kB​T4​π​R​∫0∞dq​J1​(R​q)​e−2​q​z​σT′​(q,ω).\displaystyle=\frac{\mu_{0}^{2}k_{B}T}{4\pi R}\int_{0}^{\infty}\mathrm{d}q\,J_{1}(Rq)e^{-2qz}\sigma^{\prime}_{T}(q,\omega).(37)

The overall normalization can be checked against the thin-film limit of the reflection-coefficient formulation of Ref.Dolgirevet al.(2022), with which it agrees. Thex​xxxcomponent depends on the longitudinal part of the conductivity only through relativistic corrections and is dominated byσT\sigma_{T}in the non-relativistic limit. The limitR→0R\to 0recovers the single NV equations used in the main text,𝒩z​z​(ω)\displaystyle\mathcal{N}_{zz}(\omega)=μ02​kB​T4​π​∫0∞dq​q​e−2​q​z​σT′​(q,ω),\displaystyle=\frac{\mu_{0}^{2}k_{B}T}{4\pi}\int_{0}^{\infty}\mathrm{d}q\,qe^{-2qz}\sigma^{\prime}_{T}(q,\omega),(38)𝒩x​x​(ω)\displaystyle\mathcal{N}_{xx}(\omega)=μ02​kB​T8​π​∫0∞dq​q​e−2​q​z​σT′​(q,ω),\displaystyle=\frac{\mu_{0}^{2}k_{B}T}{8\pi}\int_{0}^{\infty}\mathrm{d}q\,qe^{-2qz}\sigma^{\prime}_{T}(q,\omega),(39)

so that𝒩x​x=𝒩y​y=12​𝒩z​z\mathcal{N}_{xx}=\mathcal{N}_{yy}=\tfrac{1}{2}\mathcal{N}_{zz}. The NV relaxation rate is set by the field noise transverse to the NV axisn^\hat{n},1/T1=(g​μB/ℏ)2​[Tr​𝒩−n^⋅𝒩⋅n^]1/T_{1}=(g\mu_{B}/\hbar)^{2}\,[\,\mathrm{Tr}\,\mathcal{N}-\hat{n}\cdot\mathcal{N}\cdot\hat{n}\,], which for the axis at angleθ\thetafrom the film normal gives1/T1=(g​μB/ℏ)2​sn^​𝒩z​z1/T_{1}=(g\mu_{B}/\hbar)^{2}\,s_{\hat{n}}\,\mathcal{N}_{zz}withsn^=(3−cos2⁡θ)/2s_{\hat{n}}=(3-\cos^{2}\theta)/2Casolaet al.(2018); additional details regarding NV relaxation rates can be found in, e.g.,Cambriaet al.(2021,2023).

As discussed in AppendixBthe conductivity is conveniently writtenσT​(κ,ϖ)=σA​L​FT​(κ,ϖ)\sigma_{T}(\kappa,\varpi)=\sigma_{AL}F_{T}(\kappa,\varpi)and we introduce the notation,𝒩z​z​(𝐑,z,ω=0)=μ02​kB​T​σA​L4​π​∫0∞dq​q​e−2​d​q​J0​(R​q)​FT​(ξ​q2).\mathcal{N}_{zz}(\mathbf{R},z,\omega=0)=\frac{\mu_{0}^{2}k_{B}T\sigma_{AL}}{4\pi}\int_{0}^{\infty}\mathrm{d}q~qe^{-2dq}J_{0}(Rq)F_{T}\left(\frac{\xi q}{2}\right).(40)

## A.1Limiting behaviors of the noise

Focusing on the static caseω=0\omega=0, we can derive the behavior of𝒩z​z\mathcal{N}_{zz}in the different regimesd≫ξd\gg\xiandd≪ξd\ll\xi. Thed≫ξd\gg\xiis elementary and done in the main text, so let us focus on the more interesting regimed≪ξd\ll\xi. We focus on the integral𝒩~z​z=∫0∞dq​q​e−2​d​q​J0​(R​q)​FT​(ξ​q/2)=4ξ2​∫0∞dx​x​e−4​dξ​J0​(2​R​x/ξ)​FT​(x).\tilde{\mathcal{N}}_{zz}=\int_{0}^{\infty}\mathrm{d}q~qe^{-2dq}J_{0}(Rq)F_{T}(\xi q/2)=\frac{4}{\xi^{2}}\int_{0}^{\infty}\mathrm{d}x~xe^{-\frac{4d}{\xi}}J_{0}(2Rx/\xi)F_{T}(x).(41)

Since we are interested in the regimeξ≫d\xi\gg d, we can neglect the exponential factor and investigateI​(α)=∫0∞dx​x​J0​(α​x)​FT​(x)I(\alpha)=\int_{0}^{\infty}\mathrm{d}x~xJ_{0}(\alpha x)F_{T}(x)(42)

withα=2​R/ξ\alpha=2R/\xi. Due to the oscillatory nature ofJ0​(α​x)J_{0}(\alpha x)we will analytically continue the argument into the complex plane where the oscillations turn into damping. We employJ0​(x)=[H0(1)​(x)+H0(2)​(x)]/2J_{0}(x)=[H_{0}^{(1)}(x)+H_{0}^{(2)}(x)]/2to split the integralIIinto two partsI=I++I−I=I_{+}+I_{-}, whereI+I_{+}containsH0(1)H_{0}^{(1)}andI−I_{-}containsH0(2)H_{0}^{(2)}.I+I_{+}can be continued into the upper half-plane via an infinite quasi-circle covering the 1st quadrant andI−I_{-}can be continued into the lower half-plane the same way but for the 4th quadrant. It is easy to see thatI+​(α)\displaystyle I_{+}(\alpha)=−12​∫0∞dx​x​H0(1)​(i​R​x)​FT​(i​x+0+),\displaystyle=-\frac{1}{2}\int_{0}^{\infty}\mathrm{d}x\,xH_{0}^{(1)}(iRx)F_{T}(ix+0^{+}),(43)I−​(α)\displaystyle I_{-}(\alpha)=−12​∫0∞dx​x​H0(2)​(−i​R​x)​FT​(−i​x+0+).\displaystyle=-\frac{1}{2}\int_{0}^{\infty}\mathrm{d}x\,xH_{0}^{(2)}(-iRx)F_{T}(-ix+0^{+}).(44)

The infinitesimal real part in the argument ofFTF_{T}is included to avoid the poles on the imaginary axis. UsingH0(1)​(i​x)=−H0(2)​(−i​x)=2​K0​(x)/(i​π)H_{0}^{(1)}(ix)=-H_{0}^{(2)}(-ix)=2K_{0}(x)/(i\pi)we findI−=I+∗I_{-}=I_{+}^{\ast}andI=I++I+∗=2​Re​I+=−2π​∫0∞dx​K0​(α​x)​Im​FT​(i​x+0+).I=I_{+}+I_{+}^{\ast}=2\text{Re}I_{+}=-\frac{2}{\pi}\int_{0}^{\infty}\mathrm{d}xK_{0}(\alpha x)\text{Im}F_{T}(ix+0^{+}).(45)

The finiteddcase can be restored here byFT→exp⁡(−i​4​d​x/ξ)​FTF_{T}\to\exp(-i4dx/\xi)F_{T}but the expressions become too cumbersome to write here. Looking at the analytic continuationFT​(i​x+0+)={2​arcsin⁡(x)x​1−x2+ln⁡(1−x2)x2,x<1,−2​arccosh​(x)x​x2−1+ln⁡(1−x2)x2+i​π​(1x2−1x​x2−1),x>1,F_{T}(ix+0^{+})=\begin{cases}\dfrac{2\arcsin(x)}{x\sqrt{1-x^{2}}}+\dfrac{\ln(1-x^{2})}{x^{2}},\quad&x<1,\\
-2\dfrac{\text{arccosh}(x)}{x\sqrt{x^{2}-1}}+\dfrac{\ln(1-x^{2})}{x^{2}}+i\pi\left(\dfrac{1}{x^{2}}-\dfrac{1}{x\sqrt{x^{2}-1}}\right),\quad&x>1,\end{cases}(46)

we see that the imaginary part ofFTF_{T}is zero belowx=1x=1and henceI​(α)=2​∫1∞dx​K0​(α​x)​(1x2−1−1x)=[K0​(α/2)]2−2​∫1∞dx​K0​(α​x)x.I(\alpha)=2\int_{1}^{\infty}\mathrm{d}x\,K_{0}(\alpha x)\left(\frac{1}{\sqrt{x^{2}-1}}-\frac{1}{x}\right)=[K_{0}(\alpha/2)]^{2}-2\int_{1}^{\infty}\mathrm{d}x\,\frac{K_{0}(\alpha x)}{x}.(47)

This form is exact ford=0d=0and a good approximation ford≪R≲ξd\ll R\lesssim\xi. The trueR≫ξ≫dR\gg\xi\gg dlimit cannot be restored with Eq.47since the finiteddeventually restores the Ohmic tail shown in Fig.5. Let us instead look at the limitα≪1\alpha\ll 1corresponding toξ≫R≫d\xi\gg R\gg d. SinceK0​(x≪1)≈ln⁡(2/x)−γK_{0}(x\ll 1)\approx\ln(2/x)-\gamma,ξ2​𝒩~z​z​(ξ≫R≫d)=8​ln⁡(2)​[ln⁡(ξR)−c0],\xi^{2}\tilde{\mathcal{N}}_{zz}(\xi\gg R\gg d)=8\ln(2)\left[\ln\left(\frac{\xi}{R}\right)-c_{0}\right],(48)

matching the form in Eq.25and Fig.5. The constantc0c_{0}is,c0=γ+π248​ln⁡2−ln⁡24.c_{0}=\gamma+\frac{\pi^{2}}{48\ln 2}-\frac{\ln 2}{4}.(49)

For small, nonzerodd,c0c_{0}can be treated as a fitting parameter.

## Appendix BDerivation of AL contribution to conductivity

Starting from the expression of the Eq. (10) we perform the integral over frequency by methods of residues and find,σμ​ν′​(𝐤,ω)=γ​T​e2m2​∫pμ​pν​ε𝐩+𝐤/2+ε𝐩−𝐤/2ε𝐩+𝐤/2​ε𝐩−𝐤/2​[(ε𝐩+𝐤/2+ε𝐩−𝐤/2)2+γ2​ω2]​dd​p(2​π)d\sigma^{\prime}_{\mu\nu}(\mathbf{k},\omega)=\frac{\gamma Te^{2}}{m^{2}}\int p_{\mu}p_{\nu}\frac{\varepsilon_{\mathbf{p}+\mathbf{k}/2}+\varepsilon_{\mathbf{p}-\mathbf{k}/2}}{\varepsilon_{\mathbf{p}+\mathbf{k}/2}\varepsilon_{\mathbf{p}-\mathbf{k}/2}[(\varepsilon_{\mathbf{p}+\mathbf{k}/2}+\varepsilon_{\mathbf{p}-\mathbf{k}/2})^{2}+\gamma^{2}\omega^{2}]}\frac{\mathrm{d}^{d}p}{(2\pi)^{d}}(50)

The imaginary part can be restored using Kramers-Kronig relation,σμ​ν′′​(𝐤,ω)=γ​T​e2m2​∫pμ​pν​γ​ωε𝐩+𝐤/2​ε𝐩−𝐤/2​[(ε𝐩+𝐤/2+ε𝐩−𝐤/2)2+γ2​ω2]​dd​p(2​π)d.\sigma^{\prime\prime}_{\mu\nu}(\mathbf{k},\omega)=\frac{\gamma Te^{2}}{m^{2}}\int p_{\mu}p_{\nu}\frac{\gamma\omega}{\varepsilon_{\mathbf{p}+\mathbf{k}/2}\varepsilon_{\mathbf{p}-\mathbf{k}/2}[(\varepsilon_{\mathbf{p}+\mathbf{k}/2}+\varepsilon_{\mathbf{p}-\mathbf{k}/2})^{2}+\gamma^{2}\omega^{2}]}\frac{\mathrm{d}^{d}p}{(2\pi)^{d}}.(51)

Combining real and imaginary parts together, introducing
dimensionless momentaρ→=𝐤​ξ{\vec{\rho}}=\mathbf{k}\xi,κ→=𝐤​ξ/2{\vec{\kappa}}=\mathbf{k}\xi/2and dimensionless frequencyϖ=ω/Ω\varpi=\omega/\Omega, whereΩ=1/γ​m​ξ2\Omega=1/\gamma m\xi^{2}we find
conductivity tensorσμ​ν​(𝐤,ω)=σA​L​Fμ​ν​(𝐤,ω)\sigma_{\mu\nu}(\mathbf{k},\omega)=\sigma_{AL}F_{\mu\nu}(\mathbf{k},\omega)with,Fμ​ν​(κ,ϖ)=4​(4​π)d/2Γ​(2−d/2)​∫ρμ​ρν[1+ρ2+κ2+2​κ→​ρ→]​[1+ρ2+κ2−2​κ→​ρ→]​[1+ρ2+κ2−i​ϖ]​dd​ρ(2​π)d.F_{\mu\nu}(\kappa,\varpi)=\frac{4(4\pi)^{d/2}}{\Gamma(2-d/2)}\int\frac{\rho_{\mu}\rho_{\nu}}{[1+\rho^{2}+\kappa^{2}+2{\vec{\kappa}}{\vec{\rho}}][1+\rho^{2}+\kappa^{2}-2{\vec{\kappa}}{\vec{\rho}}][1+\rho^{2}+\kappa^{2}-i\varpi]}\frac{\mathrm{d}^{d}\rho}{(2\pi)^{d}}.(52)

The momentum integral can be performed by Feynman parametrization,1a​b=∫01d​x(a​x+(1−x)​b)2,1a2​b=−∂∂a​1a​b=∫012​x​d​x(a​x+(1−x)​b)3\frac{1}{ab}=\int_{0}^{1}\frac{\mathrm{d}x}{(ax+(1-x)b)^{2}},\quad\frac{1}{a^{2}b}=-\frac{\partial}{\partial a}\frac{1}{ab}=\int_{0}^{1}\frac{2x\mathrm{d}x}{(ax+(1-x)b)^{3}}(53)

Inserting these identities and completing the square in the denominator we find,Fμ​ν​(κ,ϖ)=8​(4​π)d/2Γ​(2−d/2)​∫01dz​∫01dy​y​∫dd​q(2​π)d​qμ​qν+z2​y2​κμ​κν[1+q2+κ2​(1−z2​y2)−(1−y)​i​ϖ]3F_{\mu\nu}(\kappa,\varpi)=\frac{8(4\pi)^{d/2}}{\Gamma(2-d/2)}\int\limits_{0}^{1}\mathrm{d}z\int\limits_{0}^{1}\mathrm{d}y\ y\int\frac{\mathrm{d}^{d}q}{(2\pi)^{d}}\frac{q_{\mu}q_{\nu}+z^{2}y^{2}\kappa_{\mu}\kappa_{\nu}}{[1+q^{2}+\kappa^{2}(1-z^{2}y^{2})-(1-y)i\varpi]^{3}}(54)

After integration over the momentumqqwe find following formulas
for the transverse and longitudinal scaling functionsFT​(κ,ϖ)=∫01∫012​y​d​z​d​y[1+κ2​(1−z2​y2)−(1−y)​i​ϖ]2−d/2F_{T}(\kappa,\varpi)=\int\limits_{0}^{1}\int\limits_{0}^{1}\frac{2y\mathrm{d}z\mathrm{d}y}{[1+\kappa^{2}(1-z^{2}y^{2})-(1-y)i\varpi]^{2-d/2}}(55)FL​(κ,ϖ)=FT​(κ,ϖ)+(2−d/2)​κ2​∫01∫01z2​y3​d​z​d​y[1+κ2​(1−z2​y2)−(1−y)​i​ϖ]3−d/2F_{L}(\kappa,\varpi)=F_{T}(\kappa,\varpi)+(2-d/2)\kappa^{2}\int\limits_{0}^{1}\int\limits_{0}^{1}\frac{z^{2}y^{3}\mathrm{d}z\mathrm{d}y}{[1+\kappa^{2}(1-z^{2}y^{2})-(1-y)i\varpi]^{3-d/2}}(56)

Ford=2d=2the transverse integral can be done exactly. Making the change in variablesx=z​yx=zythe domain is0≤x≤y0\leq x\leq yand the integral becomes,FT​(κ,ϖ)=∫01dy​∫0ydx​21+κ2​(1−x2)−(1−y)​i​ϖ.F_{T}(\kappa,\varpi)=\int_{0}^{1}\mathrm{d}y\int_{0}^{y}\mathrm{d}x\frac{2}{1+\kappa^{2}(1-x^{2})-(1-y)i\varpi}.(57)

Now changing order of integration (x≤y≤1x\leq y\leq 1) and integrating w.r.t.yywe find,FT​(κ,ϖ)=2i​ϖ​∫01dx​ln⁡(1+κ2​(1−x2)1+κ2​(1−x2)−(1−x)​i​ϖ)F_{T}(\kappa,\varpi)=\frac{2}{i\varpi}\int_{0}^{1}\mathrm{d}x\ln\left(\frac{1+\kappa^{2}(1-x^{2})}{1+\kappa^{2}(1-x^{2})-(1-x)i\varpi}\right)(58)

This is now just a sum of two integrals of the form,I=∫01dx​ln⁡(a​x2+b​x+c),I=\int_{0}^{1}\mathrm{d}x\ln(ax^{2}+bx+c),(59)

Performing these integrals and simplifying we find,FT​(κ,ϖ)=2i​ϖ​[2​1+κ2κ​arcsinh​(κ)−ln⁡(−κ2)−∑σ=±((1−rσ)​ln⁡(1−rσ)+rσ​ln⁡(−rσ))]F_{T}(\kappa,\varpi)=\frac{2}{i\varpi}\left[\frac{2\sqrt{1+\kappa^{2}}}{\kappa}\mathrm{arcsinh}(\kappa)-\ln(-\kappa^{2})-\sum_{\sigma=\pm}\big((1-r_{\sigma})\ln(1-r_{\sigma})+r_{\sigma}\ln(-r_{\sigma})\big)\right](60)

withln\lnbeing the principal value logarithmln⁡(−1)≡i​π\ln(-1)\equiv i\piand,r±=i​ϖ2​κ2±1+1κ2−i​ϖκ2+(i​ϖ)24​κ4.r_{\pm}=\frac{i\varpi}{2\kappa^{2}}\pm\sqrt{1+\frac{1}{\kappa^{2}}-\frac{i\varpi}{\kappa^{2}}+\frac{(i\varpi)^{2}}{4\kappa^{4}}}.(61)

This can be simplified to the form,FT​(κ,ϖ)\displaystyle F_{T}(\kappa,\varpi)=2i​ϖ​[2​1+κ2κ​arcsinh​(κ)−2κ​g​(κ,ϖ)​arctanh​(2​κ​g​(κ,ϖ)2+2​κ2−i​ϖ)]−ln⁡(1+κ2−i​ϖ)κ2,\displaystyle=\frac{2}{i\varpi}\left[\frac{2\sqrt{1+\kappa^{2}}}{\kappa}\mathrm{arcsinh}(\kappa)-\frac{2}{\kappa}g(\kappa,\varpi)\mathrm{arctanh}\left(\frac{2\kappa g(\kappa,\varpi)}{2+2\kappa^{2}-i\varpi}\right)\right]-\frac{\ln(1+\kappa^{2}-i\varpi)}{\kappa^{2}},(62)g​(κ,ϖ)\displaystyle g(\kappa,\varpi)=1+κ2−i​ϖ−ϖ2/4​κ2\displaystyle=\sqrt{1+\kappa^{2}-i\varpi-\varpi^{2}/4\kappa^{2}}(63)

Expanding this expression forϖ→0\varpi\to 0one easily finds,FT​(κ,ϖ→0)=2​a​r​c​s​i​n​h​(κ)κ​1+κ2−ln⁡(1+κ2)κ2F_{T}(\kappa,\varpi\to 0)=\frac{2\mathrm{arcsinh}(\kappa)}{\kappa\sqrt{1+\kappa^{2}}}-\frac{\ln(1+\kappa^{2})}{\kappa^{2}}(64)

As a sanity check, Eq. (62) has been numerically verified to satisfy Kramers-Kronig relations, to agree with direct numerical evaluation of the Feynman-parametric representation, and to coincide with the thin-film response kernel of Ref.Galaktionov (1995)through the identityBG​(κ,ϖ)=BG​(κ,0)+i​ϖ4​FT​(κ,ϖ)B_{G}(\kappa,\varpi)=B_{G}(\kappa,0)+\tfrac{i\varpi}{4}F_{T}(\kappa,\varpi), whereBGB_{G}denotes the bracket of Eq. (6) of that reference andBG​(κ,0)=1−1+κ2​arcsinh​(κ)/κB_{G}(\kappa,0)=1-\sqrt{1+\kappa^{2}}\,\mathrm{arcsinh}(\kappa)/\kappais its static (diamagnetic) part; see AppendixD.Figure 9:Real and imaginary parts of the dynamical scaling functionFT​(κ,ϖ)F_{T}(\kappa,\varpi), Eq. (62), versus the dimensionless frequencyϖ=ω​γ​m​ξ2\varpi=\omega\gamma m\xi^{2}for several values ofκ=k​ξ/2\kappa=k\xi/2. The dissipative part is flat forϖ≲1\varpi\lesssim 1(white-noise regime relevant to NV relaxometry atϵ≫ϵΩ\epsilon\gg\epsilon_{\Omega}) and falls off atϖ≳1\varpi\gtrsim 1, where the probe frequency exceeds the fluctuation relaxation rate; the reactive part peaks at the crossover.

## Appendix CNonequilibrium current noise: exact solution

In a uniform electric field,𝐀=−c​𝐄​t\mathbf{A}=-c\mathbf{E}twith𝐄=E​x^\mathbf{E}=E\hat{x}, the linearized TDGL equation remains diagonal in the canonical momentum𝐩\mathbf{p}, with the kinetic momentum sliding as𝐏​(t)=𝐩+e​𝐄​t\mathbf{P}(t)=\mathbf{p}+e\mathbf{E}t. Each mode is an Ornstein-Uhlenbeck process with time-dependent rate, and the two-time correlator is exact: forτ=t−t′≥0\tau=t-t^{\prime}\geq 0, with𝐏\mathbf{P}the kinetic momentum at the earlier time,⟨Ψ​(t)​Ψ∗​(t′)⟩𝐩=exp⁡[−1γ​∫0τε​(𝐏+e​𝐄​u)​du]​N​(𝐏),N​(𝐏)=2​Tγ​∫0∞ds​e−2γ​∫0sε​(𝐏−e​𝐄​v)​dv,\langle\Psi(t)\Psi^{*}(t^{\prime})\rangle_{\mathbf{p}}=\exp\left[-\frac{1}{\gamma}\int_{0}^{\tau}\varepsilon(\mathbf{P}+e\mathbf{E}u)\,\mathrm{d}u\right]N(\mathbf{P}),\qquad N(\mathbf{P})=\frac{2T}{\gamma}\int_{0}^{\infty}\mathrm{d}s\;e^{-\frac{2}{\gamma}\int_{0}^{s}\varepsilon(\mathbf{P}-e\mathbf{E}v)\,\mathrm{d}v},(65)

whereN​(𝐏)N(\mathbf{P})is the driven occupation [equal toT/ε𝐏T/\varepsilon_{\mathbf{P}}atE=0E=0, and reproducing Eq. (24) of Ref.Dorsey (1991)]. The mean current𝐉=(e/m)​∫𝐏𝐏​N​(𝐏)\mathbf{J}=(e/m)\int_{\mathbf{P}}\mathbf{P}N(\mathbf{P})recovers the nonlinear AL conductivity,σ​(E)=σAL​Σ+​(E/E0)\sigma(E)=\sigma^{\rm AL}\Sigma_{+}(E/E_{0})Dorsey (1991).

Since the theory is Gaussian, Wick factorization gives the symmetrized zero-frequency current noise at any wave vector asSμ​ν(𝐤,ω→0;E)=2(em)2∫d2​P(2​π)2∫0∞dτ(𝐏+e𝐄τ)μPνN(𝐏+𝐤2)N(𝐏−𝐤2)e−1γ​∫0τ[2​ε​(𝐏+e​𝐄​u)+k24​m]​du,S_{\mu\nu}(\mathbf{k},\omega\to 0;E)=2\left(\frac{e}{m}\right)^{2}\int\frac{\mathrm{d}^{2}P}{(2\pi)^{2}}\int_{0}^{\infty}\mathrm{d}\tau\;(\mathbf{P}+e\mathbf{E}\tau)_{\mu}P_{\nu}\,N\big(\mathbf{P}+\tfrac{\mathbf{k}}{2}\big)N\big(\mathbf{P}-\tfrac{\mathbf{k}}{2}\big)\,e^{-\frac{1}{\gamma}\int_{0}^{\tau}\left[2\varepsilon(\mathbf{P}+e\mathbf{E}u)+\frac{k^{2}}{4m}\right]\mathrm{d}u},(66)

where the identityε​(𝐏+𝐤2)+ε​(𝐏−𝐤2)=2​ε​(𝐏)+k2/4​m\varepsilon(\mathbf{P}+\tfrac{\mathbf{k}}{2})+\varepsilon(\mathbf{P}-\tfrac{\mathbf{k}}{2})=2\varepsilon(\mathbf{P})+k^{2}/4mhas been used. All time integrals carry cubic-in-time damping from the field [∫0s(…+e​𝐄​v)2​dv⊃e2​E2​s3/3\int_{0}^{s}(\ldots+e\mathbf{E}v)^{2}\mathrm{d}v\supset e^{2}E^{2}s^{3}/3], which regularizes theϵ→0\epsilon\to 0limit and generates the threshold field Eq. (29). Inserting the integral representation ofNNand performing the exact Gaussiand2​P\mathrm{d}^{2}Pintegral reduces Eq. (66) to a three-fold quadrature with explicit normalization. Withκ=k​ξ/2\kappa=k\xi/2,θ\thetathe angle between𝐤\mathbf{k}and𝐄\mathbf{E},f=4​3​E/E0f=4\sqrt{3}E/E_{0}, ands1,s2,τs_{1},s_{2},\tauin units ofγ/a=2​τGL\gamma/a=2\tau_{\rm GL},Sμ​ν(𝐤,ω→0;E)=32kBTσAL∫0∞ds1ds2dτe𝒜+|𝐛|2/8​ΣΣVμ​ν,Σ=s1+s2+τ,S_{\mu\nu}(\mathbf{k},\omega\to 0;E)=32\,k_{B}T\,\sigma^{\rm AL}\int_{0}^{\infty}\mathrm{d}s_{1}\mathrm{d}s_{2}\mathrm{d}\tau\;\frac{e^{\mathcal{A}+|\mathbf{b}|^{2}/8\Sigma}}{\Sigma}\,V_{\mu\nu},\qquad\Sigma=s_{1}+s_{2}+\tau,(67)𝒜=−2​Σ​(1+κ2)+2​κ∥​f​(s12−s22)−23​f2​(s13+s23+τ3),𝐛=(2​f​B−4​(s1−s2)​κ∥,−4​(s1−s2)​κ⟂),\mathcal{A}=-2\Sigma(1+\kappa^{2})+2\kappa_{\parallel}f(s_{1}^{2}-s_{2}^{2})-\tfrac{2}{3}f^{2}(s_{1}^{3}+s_{2}^{3}+\tau^{3}),\qquad\mathbf{b}=\big(2fB-4(s_{1}{-}s_{2})\kappa_{\parallel},\;-4(s_{1}{-}s_{2})\kappa_{\perp}\big),(68)

withB=s12+s22−τ2B=s_{1}^{2}+s_{2}^{2}-\tau^{2}and the vertex momentsVx​x=14​Σ+μx2+f​τ​μxV_{xx}=\tfrac{1}{4\Sigma}+\mu_{x}^{2}+f\tau\mu_{x},Vy​y=14​Σ+μy2V_{yy}=\tfrac{1}{4\Sigma}+\mu_{y}^{2},𝝁=𝐛/4​Σ\bm{\mu}=\mathbf{b}/4\Sigma. The prefactor carries two internal checks: (i) atE=0E=0,k=0k=0the triple integral evaluates elementarily to∫0∞du​(u2/2)​e−2​u/(4​u2)=1/16\int_{0}^{\infty}\mathrm{d}u\,(u^{2}/2)e^{-2u}/(4u^{2})=1/16, so thatSμ​ν=2​kB​T​σAL​δμ​νS_{\mu\nu}=2k_{B}T\sigma^{\rm AL}\delta_{\mu\nu}—the fluctuation-dissipation theorem emerges with the correct coefficient; (ii) atE=0E=0and finiteκ\kappait reproducesST,L=2​kB​T​σAL​FT,L​(κ)S_{T,L}=2k_{B}T\sigma^{\rm AL}F_{T,L}(\kappa)with the closed-form scaling functions of Sec.II(verified numerically to10−410^{-4}), while atk=0k=0the associated mean current reproduces Dorsey’sΣ+\Sigma_{+}exactly. The FDT ratios and anisotropies plotted in Figs.7and8follow by direct numerical evaluation of Eq. (67); for an isotropic film𝐉=σ​(|𝐄|)​𝐄\mathbf{J}=\sigma(|\mathbf{E}|)\mathbf{E}, so the transverse differential conductivity equalsσ\sigmaidentically, which is whyX⟂X_{\perp}is normalized byσ\sigma.

## Appendix DFluctuation diamagnetism

Susceptibility—In a perpendicular fieldBBthe quadratic fluctuation modes occupy Landau levels with eigenvaluesa+ℏ​ωc​(n+12)a+\hbar\omega_{c}(n+\tfrac{1}{2}),ωc=e​B/m​c\omega_{c}=eB/mc, and areal degeneracyB/Φ0B/\Phi_{0}. Applying the Euler-Maclaurin expansion to the Gaussian free energyF=T​(B/Φ0)​∑nln⁡[a+ℏ​ωc​(n+12)]F=T(B/\Phi_{0})\sum_{n}\ln[a+\hbar\omega_{c}(n+\tfrac{1}{2})]gives the field-dependent partδ​F=T​e2​B2/(48​π​m​c2​a)\delta F=Te^{2}B^{2}/(48\pi mc^{2}a)and hence the areal susceptibility per layerχA=−∂2δ​F/∂B2=−T​e2​ξ2/12​π​ℏ2​c2\chi_{A}=-\partial^{2}\delta F/\partial B^{2}=-Te^{2}\xi^{2}/12\pi\hbar^{2}c^{2}, which withe=2​e0e=2e_{0}is Eq. (26). The same result follows as theQ→0Q\to 0limit of the static transverse response kernel: the reactive part of the thin-film kernel of Ref.Galaktionov (1995),BG​(κ,0)=1−1+κ2​arcsinh​(κ)/κB_{G}(\kappa,0)=1-\sqrt{1+\kappa^{2}}\,\mathrm{arcsinh}(\kappa)/\kappa, yieldsχ​(Q)=χA​G​(Q​ξ/2)\chi(Q)=\chi_{A}G(Q\xi/2)withG​(x)=(3/x2)​[1+x2​arcsinh​(x)/x−1]G(x)=(3/x^{2})[\sqrt{1+x^{2}}\,\mathrm{arcsinh}(x)/x-1], which we have verified independently against the static GL current-current correlator. The full kernel obeysBG​(κ,ϖ)=BG​(κ,0)+i​ϖ4​FT​(κ,ϖ)B_{G}(\kappa,\varpi)=B_{G}(\kappa,0)+\tfrac{i\varpi}{4}F_{T}(\kappa,\varpi): the fluctuation diamagnetism and the AL conductivity are the reactive and dissipative parts of the same nonlocal response.

No-double-counting—For a 2D layer, the bound current of an out-of-plane magnetization density is purely transverse,KT​(𝐪)=i​c​q​Mz​(𝐪)K_{T}(\mathbf{q})=icqM_{z}(\mathbf{q}), giving Eq. (27): the spectral density of magnetization noise is the transverse current noise divided byc2​q2c^{2}q^{2}. Note the complementary roles of the two static objects: the (positive) spontaneous noise⟨|Mz​(𝐪)|2⟩=T​ΠT​(𝐪)/c2​q2\langle|M_{z}(\mathbf{q})|^{2}\rangle=T\,\Pi_{T}(\mathbf{q})/c^{2}q^{2}is set by the paramagnetic current correlatorΠT\Pi_{T}, while the (negative, diamagnetic) response is the gauge-invariant differenceχ​(Q)=[ΠT​(Q)−ΠT​(0)]/c2​Q2\chi(Q)=[\Pi_{T}(Q)-\Pi_{T}(0)]/c^{2}Q^{2}; both coexist consistently with the FDT, which ties the noise to the dissipative part of the response at finite frequency.

Edge fields—Near the edge of a uniformly magnetized film the moment density heals asM​(x)=M∞​[1−3​∫1∞e−2​x​u/ξ​u2−1​u−4​du]M(x)=M_{\infty}[1-3\int_{1}^{\infty}e^{-2xu/\xi}\sqrt{u^{2}-1}\,u^{-4}\mathrm{d}u]Galaktionov (1995), whereM∞M_{\infty}is the (fluctuational) diamagnetic moment in the bulk. The profileM​(x)M(x)rises linearly overξ​(T)/2\xi(T)/2; at heights above the samplez≫ξ/2z\gg\xi/2the edge acts as a line currentI=c​MAI=cM_{A}and the estimates of Eq. (28) follow, while forz≲ξ/2z\lesssim\xi/2the profile smoothing (and henceξ​(T)\xi(T)itself) becomes directly observable in a dc field map.

## 


- 


Major funding support from
