# Coupled-Mode Equations with Arbitrary Mode Combinations for Kinetic-Inductance Superconducting Traveling-Wave Parametric Devices: Theory and Experimental Validation

**arXiv ID**: 2606.17264v1
**Authors**: F. Patricio Mena, Camilo Espinoza, Ryan O. Berriel, Ricardo Finger, David J. Thoen
**Published**: 2026-06-15
**Categories**: physics.app-ph, cond-mat.supr-con, quant-ph
**Comments**: 28 pages, 13 figures, submitted to Physical Review Applied
**HTML URL**: https://arxiv.org/html/2606.17264v1

## Abstract

The coupled-mode equations (CMEs) have proven very successful in describing parametric processes in nonlinear optics. More recently, the same formulation has been used to model microwave superconducting parametric amplifiers and frequency multipliers. However, when applied to the microwave regime, not all assumptions remain valid and losses play a more dramatic role. Here, we revisit the CMEs applied to traveling-wave superconducting amplifiers to include losses and provide a formulation that enables their systematic derivation for any combination of traveling waves. As examples, we discuss the impact of unwanted harmonics and intermodulation products on parametric amplification, as well as harmonic generation. We verify that, if not properly accounted for, device performance can deviate considerably from the ideal case. Furthermore, using a superconducting CPW-based artificial transmission line and combining an independent experimental determination of its nonlinear parameter $I'_*$ with simulations of its linear properties, we obtain a parameter-free validation of this formulation. The nonlinear parameter was determined to be $I'_* \approx 27$ mA which, surprisingly, scales with the theoretical depairing current and not with the much smaller critical current of the device. For the validation, we measured multiple-harmonic generation and found excellent agreement between theory and experiment. The fact that $I'_* \gg I_C$ has direct implications for device design.

## Full Text

Coupled-Mode Equations with Arbitrary Mode Combinations for Kinetic-Inductance Superconducting Traveling-Wave Parametric Devices: Theory and Experimental Validation

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
- 
- 
- 
- 
- License: CC ZeroarXiv:2606.17264v1 [physics.app-ph] 15 Jun 2026

## Coupled-Mode Equations with Arbitrary Mode Combinations for Kinetic-Inductance Superconducting Traveling-Wave Parametric Devices: Theory and Experimental ValidationF. P. MenaCentral Development Laboratory, National Radio Astronomy Observatory, 1180 Boxwood Estate Rd, Charlottesville, VA 22903R. O. BerrielAstronomy Department, Faculty of Physical and Mathematical Sciences, University of Chile, Camino El Observatorio 1515, Santiago, ChileC. EspinozaCentral Development Laboratory, National Radio Astronomy Observatory, 1180 Boxwood Estate Rd, Charlottesville, VA 22903R. FingerAstronomy Department, Faculty of Physical and Mathematical Sciences, University of Chile, Camino El Observatorio 1515, Santiago, ChileD. J. ThoenSpace Research Organization Netherlands (SRON), Instrument Science Group - Litho, Niels Bohrweg 4, 2333 CA Leiden, The Netherlands

## Abstract

The coupled-mode equations (CMEs) have proven to be very successful in describing different parametric processes in nonlinear optics. More recently, the very same formulation has been used to model the behavior of microwave superconducting parametric amplifiers and frequency multipliers. However, when applied to the microwave regime, one has to take into account that not all the same assumptions remain valid and one expects that losses play a more dramatic role. Here, we revisit the CMEs applied to traveling-wave superconducting amplifiers not only to include losses, but also to provide a formulation that enables their systematic derivation for any combination of traveling waves. Whereas CMEs are typically derived separately for each specific process, within this approach the modeling of different scenarios pertinent to practical applications is rather straightforward. As examples, we discuss the impact of unwanted harmonics and intermodulation products on parametric amplification, as well as harmonic generation. We verify that, if not taken into account properly, the performance of the devices can deviate considerably from the ideal case where the unwanted tones are not excited. Furthermore, by using a superconducting CPW-based artificial transmission line and combining an independent experimental determination of its nonlinear parameterI∗′I^{\prime}_{*}with simulations of its linear properties, we have been able to obtain a parameter-free validation of this formulation. The nonlinear parameter was determined to beI∗′≈27mAI^{\prime}_{*}\approx$27\text{\,}\mathrm{mA}$which, surprisingly, scales with its theoretical depairing current and not with the actual much smaller critical current of the device. The properties of the line, characteristic impedance and propagation constant, on the other hand, were determined through a combination of electromagnetic simulations and a transmission matrix model. For the validation of the CMEs, we measured multiple-harmonic generation in the line and found an excellent agreement between theory and experiment up to the highest measured harmonic. This experiment also confirms independently the value ofI∗′≫ICI^{\prime}_{*}\gg I_{C}, which has direct implications for the device design.Superconductivity, amplitude equations, harmonic generation, CPW, artificial transmission line

## IIntroduction

Their demonstrated capacity of achieving near quantum-limited noise has brought superconducting amplifiers considerable attention for their use in very sensitive applications like quantum computing or astronomy (for some recent examples see[29,13,32,4,16,21]). Of particular interest are implementations in the form of traveling-wave amplifiers (TWPAs) since they may, in principle, overcome the main limitations of the lumped-element versions, namely low-power handling and a limited operational bandwidth[14,3,12,26]. TWPAs can be either implemented as a multitude of lumped elements connected in series or using the kinetic-inductance of a long low-temperature superconductor transmission line. The latter, dubbed more specifically as TKIPAs, have the additional benefit of possible operation at high frequencies, limited by the superconducting gap of the selected material (around1THz1\text{\,}\mathrm{THz}in NbTiN)[11]. As it is the case in most superconducting amplifiers, TKIPAs use the principle of parametric amplification, one of many possible parametric processes. Briefly, a parametric process is produced when different (cavity or traveling wave) modes present in a medium are coupled (through a non-linearity or excitation centers), resulting in an exchange of energy between them and, eventually, exciting ones whose initial amplitude was zero. If the correct conditions are created, large amplification of certain modes is possible.

Parametric processes can be studied using the coupled-mode equations (CMEs), also called amplitude equations, which can be obtained from either of two starting points. One is to start from the Hamiltonian of the used lumped-element device, leading to temporal-variation equations[9,27]. The other is to consider propagating waves in a non-linear medium, through the wave equation, leading to spatial-variation equations[34]. The description of TWPAs requires a link between these two frameworks[14]. On the contrary, since TKIPAs are constructed in the form of transmission lines, they can be studied entirely starting from propagating waves[11]. The term CMEs is usually applied only to the spatial-variation versions and this paper will follow that convention.

CMEs were first heuristically obtained for the study of multi-mode coupled microwave waveguides, and later introduced in the field of guided-wave optics to study coupled waveguides and nonlinear effects[18]. The CMEs have been amply studied in the field of non-linear optics[5,24,1]and the methods developed there can be almost directly applied to the study of TKIPAs[11]. However, an aspect not often discussed is the fact that not all of the assumptions used in nonlinear optics are applicable to the microwave range. Furthermore, there are two practical limitations when using the CMEs. (i) They have to be deduced on a case-by-case basis depending on the number of traveling waves that are allowed to participate in the considered parametric process[7,19,10]. (ii) The equations are normalized by the nonlinear parameterI∗′I^{\prime}_{*}preventing a parameter-free validation of the equations. Although not often discussed, it is used as a fitting parameter and usually taken to be approximately equal toICI_{C}[11,7,19,10,37]. In this work, we address these two limitations. First, we derive a general expression for the CMEs in superconducting transmission lines including losses and applicable to different parametric processes (§II). The formulation allows for the systematic derivation for any combination of traveling waves and is suitable for automated implementation. We then illustrate its use through examples, relevant to practical devices, including harmonic generation and four-wave mixing (§III). We verify that, if high-order harmonics and intermodulation products are not taken into account properly, the desired response can deviate considerably from the ideal case where the unwanted tones are not excited. Second, we provide a parameter-free validation of the presented CMEs, in the case of harmonic generation, using a superconducting CPW artificial transmission line (§§IVandV). In order to achieve this validation, we make an independent determination ofI∗′I^{\prime}_{*}by combining simulations and measurements of the variation of the sample’s RF transmission with injected DC current. The former are used to determine the properties of the line, namely the propagation constant and characteristic impedance, that are necessary to analyze the experimental results. We find, surprisingly, that the nonlinear parameter does not scale with the measured critical current but scales with the much larger theoretical depairing current, giving more precise design rules for device fabrication. Resistance-current measurements of the sample independently confirm this value and reveal the presence of dissipative regions whose onset is consistent with the harmonic generation results. The measuredI∗′I^{\prime}_{*}allows us to pin the CMEs and make a direct comparison with a measurement of the harmonic generation in the line. We find a strikingly good agreement.

## IIRevisiting & Extending the Coupled-Mode EquationsFigure 1:Lumped-element model of a transmission line considering losses. In the dispersion-engineered (DE) superconducting transmission lines considered in this work, the termsRRandGGcome not only from the material properties but also from the presence of stopbands.

As in[6]and[22], we start from the more general model of a transmission line (Fig.1) and consider a superconductor medium. The superconductor is characterized by its inductance which is the sum of a geometrical and a kinetic parts[2,8,37],L=LG+LK​0​[1+(II∗)2]≡L0​(1+I2I∗′2),L=L_{G}+L_{K0}\left[1+\left(\frac{I}{I_{*}}\right)^{2}\right]\equiv L_{0}\left(1+\frac{I^{2}}{{I^{\prime}_{*}}^{2}}\right),(1)

whereL0=LG+LK​0L_{0}=L_{G}+L_{K0},I∗′=I∗/αKI^{\prime}_{*}=I_{*}/\sqrt{\alpha_{K}}, andαK=LK​0/L0\alpha_{K}=L_{K0}/L_{0}is the kinetic-inductance fraction. Notice thatI∗′I^{\prime}_{*}is an important parameter determining the strength of the nonlinearity in a given device and has to be found experimentally. In order to obtain the CMEs, the next step is to obtain the wave equation using the telegrapher’s equations.

## II.1Linear Wave Equation (I≈0I\approx 0)

First, we consider the caseI≈0I\approx 0, whereL=L0≠L​(I)L=L_{0}\neq L(I), leading us to a linear wave equation,ℒ​I≡(∂z2−C​L0​∂t2−(G​L0+C​R)​∂t−G​R)​I=0,\mathcal{L}I\equiv\left(\partial_{z}^{2}-CL_{0}\partial_{t}^{2}-(GL_{0}+CR)\,\partial_{t}-GR\right)I=0,

whose solutions are orthogonal linearly-independent attenuated plane waves,ψm=e−γm​z+j​ωm​t.\psi_{m}=e^{-\gamma_{m}z+j\omega_{m}t}.(2)

The propagation constant and characteristic impedance at frequencyωm\omega_{m}are, respectively,γm=αm+j​βm=(Rm+j​ωm​L0​m)​(Gm+j​ωm​Cm)\gamma_{m}=\alpha_{m}+j\beta_{m}=\sqrt{(R_{m}+j\omega_{m}L_{0m})(G_{m}+j\omega_{m}C_{m})}

andZC​m=rC​m+j​xC​m=Rm+j​ωm​L0​mGm+j​ωm​Cm.Z_{Cm}=r_{Cm}+jx_{Cm}=\sqrt{\frac{R_{m}+j\omega_{m}L_{0m}}{G_{m}+j\omega_{m}C_{m}}}.

## II.2Nonlinear Wave Equation (I≠0I\neq 0)

In the general case we obtainℒ​I=13​(G​L0​∂t+C​L0​∂t2)​I3≡𝒩​I3,\mathcal{L}I=\frac{1}{3}\left(GL_{0}\partial_{t}+CL_{0}\partial_{t}^{2}\right)I^{3}\equiv\mathcal{N}I^{3},

where we have made a variable change,I→I/I∗′I\to I/I_{*}^{\prime}. To solve this equation it is assumed that the current is a superposition of the plane waves given by Eq. (2), but assuming a position-dependent amplitude,I​(z)=12​[∑n=1NAn​(z)​e−γn​z+j​ωn​t+c.c.].I(z)=\frac{1}{2}\left[\sum_{n=1}^{N}A_{n}(z)\,e^{-\gamma_{n}z+j\omega_{n}t}+\text{c.c.}\right].(3)

In order to find the equation that governs the spatial evolution of any amplitudeAmA_{m}, the next step is to projectℒ​I\mathcal{L}Iand𝒩​I3\mathcal{N}I^{3}over the temporal part of the plane waveψm\psi_{m}using the ansatz (3). To facilitate the calculations, we define𝒜n​(z)≡An​(z)​e−γn​z\mathscr{A}_{n}(z)\equiv A_{n}(z)\,e^{-\gamma_{n}z}andIc≡∑𝒜n​(z)​ej​ωn​tI_{\mathrm{c}}\equiv\sum\mathscr{A}_{n}(z)\,e^{j\omega_{n}t}, which allow us to write the ansatz asI=12​(Ic+Ic∗)I=\frac{1}{2}(I_{\mathrm{c}}+I_{\mathrm{c}}^{*})and its third power asI3=18(Ic3+3Ic2Ic∗+c.c.)I^{3}=\frac{1}{8}(I_{\mathrm{c}}^{3}+3I_{\mathrm{c}}^{2}I_{\mathrm{c}}^{*}+\mathrm{c.c.}). In this manner, the projection can be done over the operators applied toIcI_{\mathrm{c}}and its powers, and, later, conjugate them. As an example, let us consider the first term ofℒ​Ic\mathcal{L}I_{\mathrm{c}},∂z2Ic=∂z2∑𝒜n​ej​ωn​t=∑ej​ωn​t​∂z2𝒜n.\partial_{z}^{2}I_{\mathrm{c}}=\partial_{z}^{2}\textstyle\sum\mathscr{A}_{n}e^{j\omega_{n}t}=\textstyle\sum e^{j\omega_{n}t}\partial_{z}^{2}\mathscr{A}_{n}.

Its projection over the temporal part ofψm\psi_{m}is, then,⟨ej​ωm​t|∂z2Ic⟩=∑∂z2𝒜n​⟨ej​ωm​t|ej​ωn​t⟩=∂z2𝒜m,\langle e^{j\omega_{m}t}|\partial_{z}^{2}I_{\mathrm{c}}\rangle=\textstyle\sum\,\partial_{z}^{2}\mathscr{A}_{n}\langle e^{j\omega_{m}t}|e^{j\omega_{n}t}\rangle=\partial_{z}^{2}\mathscr{A}_{m},

where we have used the fact that⟨ej​ωm​t|ej​ωn​t⟩=δωm,ωn\langle e^{j\omega_{m}t}|e^{j\omega_{n}t}\rangle=\delta_{\omega_{m},\omega_{n}}. Proceeding in the same manner with all the other terms of the wave equation we obtain12​(∂z2𝒜m−γm2​𝒜m)=−124​ωm​(ωm​Cm​L0,m−j​Gm​L0,m)\displaystyle\frac{1}{2}\big(\partial_{z}^{2}\mathscr{A}_{m}-\gamma_{m}^{2}\mathscr{A}_{m}\big)=-\frac{1}{24}\omega_{m}(\omega_{m}C_{m}L_{0,m}-jG_{m}L_{0,m})×∑p,q,r{𝒜p𝒜q𝒜rδωm,ωp+ωq+ωr\displaystyle\hphantom{\frac{1}{2}\big(\partial_{z}^{2}\mathscr{A}_{m}-\gamma_{m}^{*2}\mathscr{A}_{m}\big)}\times\sum_{p,q,r}\big\{\mathscr{A}_{p}\mathscr{A}_{q}\mathscr{A}_{r}\,\delta_{\omega_{m},\omega_{p}+\omega_{q}+\omega_{r}}+3​𝒜p​𝒜q​𝒜r∗​δωm,ωp+ωq−ωr\displaystyle\hphantom{\frac{1}{2}\big(\partial_{z}^{2}\mathscr{A}_{m}-\gamma_{m}^{*2}\mathscr{A}_{m}\big)\times\sum_{p,q,r}\big\{}+3\mathscr{A}_{p}\mathscr{A}_{q}\mathscr{A}_{r}^{*}\,\delta_{\omega_{m},\omega_{p}+\omega_{q}-\omega_{r}}+3𝒜p∗𝒜q∗𝒜rδωm,−ωp−ωq+ωr}.\displaystyle\hphantom{\frac{1}{2}\big(\partial_{z}^{2}\mathscr{A}_{m}-\gamma_{m}^{*2}\mathscr{A}_{m}\big)\times\sum_{p,q,r}\big\{}+3\mathscr{A}_{p}^{*}\mathscr{A}_{q}^{*}\mathscr{A}_{r}\,\delta_{\omega_{m},-\omega_{p}-\omega_{q}+\omega_{r}}\big\}.

For practical use of this expression, we observe that−ωm​(ωm​Cm​L0,m−j​Gm​L0,m)=j​γmZCm​Im⁡(γm​ZCm)≡bm,-\omega_{m}(\omega_{m}C_{m}L_{0,m}-jG_{m}L_{0,m})=j\frac{\gamma_{m}}{Z_{C_{m}}}\operatorname{Im}(\gamma_{m}Z_{C_{m}})\equiv b_{m},

allowing to express it in terms of the characteristic impedance and propagation constant since they are directly accessible either experimentally or by simulations. Finally, we go back to the original variable for the amplitude, leading to𝔄m\displaystyle\mathfrak{A}_{m}=124​bm​eγm​z\displaystyle=\frac{1}{24}b_{m}e^{\gamma_{m}z}(4)×∑p,q,r=1N{ApAqAre−(γp+γq+γr)​zδωm,ωp+ωq+ωr\displaystyle\times\sum_{p,q,r=1}^{N}\Bigg\{A_{p}A_{q}A_{r}\,e^{-(\gamma_{p}+\gamma_{q}+\gamma_{r})z}\,\delta_{\omega_{m},\omega_{p}+\omega_{q}+\omega_{r}}+3​Ar∗​Ap​Aq​e−(γp+γq+γr∗)​z​δωm,ωp+ωq−ωr\displaystyle\qquad+3A_{r}^{*}A_{p}A_{q}\,e^{-(\gamma_{p}+\gamma_{q}+\gamma_{r}^{*})z}\,\delta_{\omega_{m},\omega_{p}+\omega_{q}-\omega_{r}}+3Ap∗Aq∗Are−(γp∗+γq∗+γr)​zδωm,−ωp−ωq+ωr},\displaystyle\qquad+3A_{p}^{*}A_{q}^{*}A_{r}\,e^{-(\gamma_{p}^{*}+\gamma_{q}^{*}+\gamma_{r})z}\,\delta_{\omega_{m},-\omega_{p}-\omega_{q}+\omega_{r}}\Bigg\},

wherem=1,…,Nm=1,\ldots,N, and𝔄m≡12​Am′′−γm​Am′.\mathfrak{A}_{m}\equiv\frac{1}{2}A_{m}^{\prime\prime}-\gamma_{m}A_{m}^{\prime}.

Equation (4) represents a system ofNNequations describing the spatial evolution of theNNmodes assumed to be traveling in the superconducting transmission line. The Kronecker deltas serve to select the allowed combinations of the parametric process being studied, given the restrictions imposed by the modes allowed to travel. Therefore, this equation can easily be automatized to study any parametric process given a quadratic nonlinearity in the inductance, as in Eq. (1). An important aspect to consider is that the evolution of the amplitudes is only predicted as a fraction ofI∗′I^{\prime}_{*}, making its (experimental) determination crucial for practical applications.

Another important aspect of this equation is that it is more general than those presented in[6]and[22]. On the one hand, Carrascoet al.[6]did not apply the projection over𝒩​I\mathcal{N}Ibut over an approximation obtained by applying the method of multiple scales. On the other hand, Longdenet al.[22]did apply the projection over𝒩​I\mathcal{N}Ibut applied only to a specific parametric process. Even more, they limited their study to cases with low losses whereγ≈i​ω​L​C​[1−i2​(Rω​L+Gω​C)]\gamma\approx i\omega\sqrt{LC}\left[1-\frac{i}{2}\left(\frac{R}{\omega L}+\frac{G}{\omega C}\right)\right].

## II.3Some Limiting Cases

Before presenting examples on the use of Eq. (4), we discuss a few limiting cases:

## Slowly-varying envelope approximation (SVEA):

This is the usual assumption of a slowly varying wave resulting effectively in neglectingAm′′A_{m}^{\prime\prime}in𝔄m\mathfrak{A}_{m}.

## Purely real impedance (xC​m=0x_{Cm}=0):

It results inbm=j​βm​γmb_{m}=j\beta_{m}\gamma_{m}, implying that, in this case, the CMEs do not depend on the impedance of the line.

## No losses (αm=0\alpha_{m}=0&xC​m=0x_{Cm}=0):

This case leads toγm=j​βm\gamma_{m}=j\beta_{m}, andbm=−βm2b_{m}=-\beta_{m}^{2}. Under these circumstances, and using the SVEA, the CMEs reduce to the traditional form usually described in literature.

## Traditional lossy case (αm≠0\alpha_{m}\neq 0&xC​m=0x_{Cm}=0):

This limit givesbm=j​βm​γmb_{m}=j\beta_{m}\gamma_{m}. In the SVEA, this result shows that the lossy case can be obtained from the traditional CMEs by substitutingj​β→α+j​βj\beta\to\alpha+j\betabut only in the exponents. This is indeed the usual assumption made in nonlinear optics[31].

## IIIExamples

## III.1One Tone

## N=1N=1(ω1\omega_{1}):\begin{overpic}[scale={0.4},trim=0.0pt 50.18748pt 0.0pt 0.0pt,clip]{Figures/N=1_phase}
\put(-2.0,55.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 48.18pt,clip]{Figures/N=1_amplitude}
\put(-2.0,58.0){\footnotesize(b)}
\end{overpic}Figure 2:Simulation results for one traveling mode,N=1N=1. (a) Phase and (b) amplitude. Three cases are considered, a lossless line (α=xC=0\alpha=x_{C}=0) and two with losses, one coming from a complex impedance (xc=2​rcx_{c}=2r_{c}) and one from an attenuation constant (α=0.01​β1\alpha=0.01\beta_{1}). The simulations were performed within the SVEA for all the cases and without it for the latter case. Adding losses causes an attenuation of the mode and not using the SVEA gives a small spatial oscillation.

Direct use of (4) gives𝔄1=124b1eγ1​z{\displaystyle\mathfrak{A}_{1}=\,\,\frac{1}{24}b_{1}e^{\gamma_{1}z}\Big\{A13​δω1,3​ω1​e−3​γ1​z\displaystyle A_{1}^{3}\delta_{\omega_{1},3\omega_{1}}e^{-3\gamma_{1}z}+3​A1∗​A12​δω1,ω1​e−(γ1∗+2​γ1)​z\displaystyle+3A_{1}^{*}A_{1}^{2}\delta_{\omega_{1},\omega_{1}}e^{-(\gamma_{1}^{*}+2\gamma_{1})z}+3A1∗2A1δ−ω1,ω1e−(2​γ1∗+γ1)​z}.\displaystyle+3A_{1}^{*2}A_{1}\delta_{-\omega_{1},\omega_{1}}e^{-(2\gamma_{1}^{*}+\gamma_{1})z}\Big\}.

Since we are considering one propagating tone and positive frequencies, only one summand is left giving12​A1′′−γ1​A1′=18​b1​A1∗​A12​e−2​α1​z,\frac{1}{2}A_{1}^{\prime\prime}-\gamma_{1}A_{1}^{\prime}=\frac{1}{8}b_{1}A_{1}^{*}A_{1}^{2}e^{-2\alpha_{1}z},

where we have also used the definition for𝔄1\mathfrak{A}_{1}. In the lossless case within the SVEA this equation has a simple analytic solution. By usingA1=a1​eϕ1A_{1}=a_{1}e^{\phi_{1}}, one obtains thata1=ctea_{1}=\mathrm{cte}andϕ1=−18​β1​a12​z+cte\phi_{1}=-\frac{1}{8}\beta_{1}a_{1}^{2}z+\mathrm{cte}. In other words, only the phase changes linearly with position. Figure2compares this case with three numerical simulations for specific lossy cases. We can see that the introduction of losses, either asα≠0\alpha\neq 0orxC≠0x_{C}\neq 0, produces a reduction of the amplitude of the mode. Furthermore, the full solution, includingA1′′A_{1}^{\prime\prime}, predicts a small spatial oscillation.

## III.2Harmonic Generation

## N=3N=3(ω1\omega_{1},ω2=2​ω1\omega_{2}=2\omega_{1},ω3=3​ω1\omega_{3}=3\omega_{1}):

Application of Eq. (4) and some rewriting gives𝔄1\displaystyle\mathfrak{A}_{1}=b18{(eΔ​γ1​z​|A1|2+2​eΔ​γ2​z​|A2|2+2​eΔ​γ3​z​|A3|2)​A1⏟SPM/XPM∝A1\displaystyle=\frac{b_{1}}{8}\Bigl\{\underbrace{\bigl(e^{\Delta\gamma_{1}z}|A_{1}|^{2}+2\,e^{\Delta\gamma_{2}z}|A_{2}|^{2}+2\,e^{\Delta\gamma_{3}z}|A_{3}|^{2}\bigr)A_{1}}_{\text{SPM/XPM $\propto A_{1}$}}+eΔ​γ1|201​z​A1∗2​A3⏟THG back action+eΔ​γ1|021​z​A22​A3∗⏟Source forA1}\displaystyle\quad+\underbrace{e^{\Delta\gamma_{1|201}z}A_{1}^{*2}\,A_{3}}_{\text{THG back action}}+\underbrace{e^{\Delta\gamma_{1|021}z}A_{2}^{2}\,A_{3}^{*}}_{\text{Source for $A_{1}$}}\Bigr\}𝔄2\displaystyle\mathfrak{A}_{2}=b28{(2​eΔ​γ1​z​|A1|2+eΔ​γ2​z​|A2|2+2​eΔ​γ3​z​|A3|2)​A2⏟SPM/XPM∝A2\displaystyle=\frac{b_{2}}{8}\Bigl\{\underbrace{\bigl(2\,e^{\Delta\gamma_{1}z}|A_{1}|^{2}+e^{\Delta\gamma_{2}z}|A_{2}|^{2}+2\,e^{\Delta\gamma_{3}z}|A_{3}|^{2}\bigr)A_{2}}_{\text{SPM/XPM $\propto A_{2}$}}+2​eΔ​γ2|111​z​A1​A2∗​A3⏟SPM/XPM∝A2∗}\displaystyle\quad+\underbrace{2\,e^{\Delta\gamma_{2|111}z}A_{1}\,A_{2}^{*}\,A_{3}}_{\text{SPM/XPM $\propto A^{*}_{2}$}}\Bigr\}𝔄3\displaystyle\mathfrak{A}_{3}=b324{eΔ​γ3|300​z​A13+3​eΔ​γ3|120​z​A1∗​A22⏟THG\displaystyle=\frac{b_{3}}{24}\Bigl\{\underbrace{e^{\Delta\gamma_{3|300}z}A_{1}^{3}+3\,e^{\Delta\gamma_{3|120}z}A_{1}^{*}\,A_{2}^{2}}_{\text{THG}}+3​(2​eΔ​γ1​z​|A1|2+2​eΔ​γ2​z​|A2|2+eΔ​γ3​z​|A3|2)​A3⏟SPM/XPM∝A3}\displaystyle\quad+\underbrace{3\bigl(2\,e^{\Delta\gamma_{1}z}|A_{1}|^{2}+2\,e^{\Delta\gamma_{2}z}|A_{2}|^{2}+e^{\Delta\gamma_{3}z}|A_{3}|^{2}\bigr)A_{3}}_{\text{SPM/XPM $\propto A_{3}$}}\Bigr\}

whereΔ​γm=−2​Re​(γm)\Delta\gamma_{m}=-2\,\mathrm{Re}(\gamma_{m}),Δ​γ1|201=γ1−2​γ1∗−γ3\Delta\gamma_{1|201}=\gamma_{1}-2\gamma_{1}^{*}-\gamma_{3},Δ​γ1|021=γ1−2​γ2−γ3∗\Delta\gamma_{1|021}=\gamma_{1}-2\gamma_{2}-\gamma_{3}^{*},Δ​γ2|111=γ2−γ2∗−γ1−γ3\Delta\gamma_{2|111}=\gamma_{2}-\gamma_{2}^{*}-\gamma_{1}-\gamma_{3},Δ​γ3|300=γ3−3​γ1\Delta\gamma_{3|300}=\gamma_{3}-3\gamma_{1},Δ​γ3|120=γ3−γ1∗−2​γ2\Delta\gamma_{3|120}=\gamma_{3}-\gamma_{1}^{*}-2\gamma_{2}. As usually discussed in nonlinear optics[1,5,24], we can distinguish several contributions in these equations. First, we have self-phase and cross-phase modulations (SPM & XPM) that are proportional to the same mode being described by𝔄m\mathfrak{A}_{m}. Therefore, they do not contribute to spontaneous generation. Since𝔄2\mathfrak{A}_{2}only contains SPM and XPM, the second harmonic remains zero if it was not present atz=0z=0. It should also be noted that all of the SPM/XPM terms are affected by losses since they are proportional toeΔ​γme^{\Delta\gamma_{m}}.
The third equation also contains a third-harmonic generation (THG) term that is not proportional toA3A_{3}, allowing its spontaneous generation. Finally, the first equation contains two terms proportional toA3A_{3}. One is the THG back action that represents the energy exchange between the source and the spontaneously-generated third harmonic. The other term is not proportional toA1A_{1}representing, then, a source that is only present ifA2A_{2}is injected atz=0z=0.

## N=7N=7(ωn=n​ω1\omega_{n}=n\omega_{1}withn=1,…,Nn=1,\ldots,N):\begin{overpic}[scale={0.4},trim=0.0pt 46.67436pt 0.0pt 0.0pt,clip]{Figures/N=7_a}
\put(-2.0,52.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 47.17624pt 0.0pt 54.2025pt,clip]{Figures/N=7_b}
\put(-2.0,50.0){\footnotesize(b)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 54.2025pt,clip]{Figures/N=7_c}
\put(-2.0,60.0){\footnotesize(c)}
\end{overpic}Figure 3:Simulation results for harmonic generation withN=7N=7(ωn=n​ω1\omega_{n}=n\omega_{1}). For the simulations we setA1​(0)=0.15A_{1}(0)=0.15, and assumed linear dispersion,βn=n​β1\beta_{n}=n\beta_{1}, except when they are suppressed, in which case we setβi≈0\beta_{i}\approx 0. (a) All tones are allowed to travel. Only odd harmonics are spontaneously excited. (b) Fifth harmonic is suppressed resulting in increased THG, although the seventh harmonic still propagates. (c) Third harmonic is suppressed resulting in none of the other harmonics being excited.

In order to better illustrate the use of (4), we have performed three simulations where one tone and six harmonics are included in the model. For the sake of clarity, we have taken the lossless case within the SVEA and the results are presented in Fig.3. First, panel (a), we considered a transmission line with linear dispersion, i.e.βn=n​β1\beta_{n}=n\beta_{1}. It can be seen that, as expected, only odd harmonics are generated. Second, panel (b), we simulated the suppression of the fifth harmonic by settingβ5≈0\beta_{5}\approx 0. We can see that it increases the generation of the third harmonic but it does not suppress higher-order modes. The last simulation, panel (c), represents the suppression of the third harmonic (β3≈0\beta_{3}\approx 0), which leads to the suppression of all other harmonics. In principle, this result suggests that in parametric amplifiers, the third harmonic is the most important one to be suppressed.

Additionally, we have studied Eq. (4) withN=4N=4(ω1\omega_{1},ω2=3​ω1\omega_{2}=3\omega_{1},ω3=5​ω1\omega_{3}=5\omega_{1},ω4=7​ω1\omega_{4}=7\omega_{1}). We have verified that this situation is equivalent to the case studied above when the initial amplitudes of the even harmonics are kept equal to zero.

## III.3Degenerate Four-Wave Mixing (FWM) with & without Higher-Order Effects

## N=3N=3(ω1\omega_{1},ω2\omega_{2},ω3=2​ω1−ω2\omega_{3}=2\omega_{1}-\omega_{2}):

This is the traditional FWM case whereω1→pump\omega_{1}\to\mathrm{pump},ω2→signal\omega_{2}\to\mathrm{signal}, andω3→idler\omega_{3}\to\mathrm{idler}. The resulting system of equations is𝔄1=18b1[\displaystyle\mathfrak{A}_{1}=\frac{1}{8}b_{1}\Big[(eΔ​γ1​z​|A1|2+2​eΔ​γ2​z​|A2|2+2​eΔ​γ3​z​|A3|2)​A1\displaystyle\big(e^{\Delta\gamma_{1}z}|A_{1}|^{2}+2e^{\Delta\gamma_{2}z}|A_{2}|^{2}+2e^{\Delta\gamma_{3}z}|A_{3}|^{2}\big)A_{1}+2e(Δ​γ1−Δ​γ)​zA1∗A2A3]\displaystyle+2e^{(\Delta\gamma_{1}-\Delta\gamma)z}A_{1}^{*}A_{2}A_{3}\Big]𝔄2=18b2[\displaystyle\mathfrak{A}_{2}=\frac{1}{8}b_{2}\Big[(2​eΔ​γ1​z​|A1|2+eΔ​γ2​z​|A2|2+2​eΔ​γ3​z​|A3|2)​A2\displaystyle\big(2e^{\Delta\gamma_{1}z}|A_{1}|^{2}+e^{\Delta\gamma_{2}z}|A_{2}|^{2}+2e^{\Delta\gamma_{3}z}|A_{3}|^{2}\big)A_{2}+e(Δ​γ3+Δ​γ)​zA12A3∗]\displaystyle+e^{(\Delta\gamma_{3}+\Delta\gamma)z}A_{1}^{2}A_{3}^{*}\Big]𝔄3=18b3[\displaystyle\mathfrak{A}_{3}=\frac{1}{8}b_{3}\Big[(2​eΔ​γ1​z​|A1|2+2​eΔ​γ2​z​|A2|2+eΔ​γ3​z​|A3|2)​A3\displaystyle\big(2e^{\Delta\gamma_{1}z}|A_{1}|^{2}+2e^{\Delta\gamma_{2}z}|A_{2}|^{2}+e^{\Delta\gamma_{3}z}|A_{3}|^{2}\big)A_{3}+e(Δ​γ2+Δ​γ)​zA12A2∗],\displaystyle+e^{(\Delta\gamma_{2}+\Delta\gamma)z}A_{1}^{2}A_{2}^{*}\Big],

whereΔ​γm=−2​Re⁡(γm)\Delta\gamma_{m}=-2\operatorname{Re}(\gamma_{m})andΔ​γ=γ3+γ2−2​γ1\Delta\gamma=\gamma_{3}+\gamma_{2}-2\gamma_{1}. Here we can note that all terms containeΔ​γme^{\Delta\gamma_{m}}and, consequently, are affected by losses. It can also be demonstrated that the system reduces to the traditional one in the lossless case.

## N=9N=9:Figure 4:Cartoon of the degenerate FWM with higher-order effects. Specifically, two harmonics and their idlers are allowed to propagate. Nine modes are produced in this process.

This case corresponds to the one depicted in Fig.4where we consider pump and two harmonics (ω1\omega_{1},ω4\omega_{4},ω7\omega_{7}), signal (ω2\omega_{2}), and idlers (ω3\omega_{3},ω5\omega_{5},ω6\omega_{6},ω8\omega_{8},ω9\omega_{9}). To illustrate the effect of harmonics and high-order idlers in the parametric gain of the signal, we have performed various simulations presented in Fig.5. Again, in order to simplify the discussion, we have considered the lossless case within the SVEA. Furthermore, we have performed the simulations with perfect matching between the pump, signal and first idler, i.e.,Δ​β=−|A1​(0)|2​Δ​β¯\Delta\beta=-|A_{1}(0)|^{2}\Delta\overline{\beta}, whereΔ​β=β3+β2−2​β1\Delta\beta=\beta_{3}+\beta_{2}-2\beta_{1}andΔ​β¯=14​(β3+β2−β1)\Delta\overline{\beta}=\frac{1}{4}\left(\beta_{3}+\beta_{2}-\beta_{1}\right). Notice that this condition is more general and reduces to the standard form usually presented in the literature where it is assumed thatβ1≈β2\beta_{1}\approx\beta_{2}[11,15]. For the rest of the waves we have considered linear dispersion unless specified otherwise.\begin{overpic}[scale={0.4},trim=0.0pt 51.19124pt 0.0pt 0.0pt,clip]{Figures/N=9_a}
\put(-2.0,52.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 52.19499pt 0.0pt 52.19499pt,clip]{Figures/N=9_b}
\put(-2.0,50.0){\footnotesize(b)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 52.19499pt,clip]{Figures/N=9_c}
\put(-2.0,60.0){\footnotesize(c)}
\end{overpic}Figure 5:Simulation results for FWM (pump,ω1\omega_{1}, signal,ω2\omega_{2}, idler,ω3\omega_{3}) with two harmonics (ω4\omega_{4},ω7\omega_{7}) and high-order idlers (ω5\omega_{5},ω6\omega_{6},ω8\omega_{8},ω9\omega_{9}),N=9N=9, corresponding to the situation depicted in Fig.4. For the simulations we setA1​(0)=0.18A_{1}(0)=0.18,β2=0.9​β1\beta_{2}=0.9\beta_{1},β3=1.092​β1\beta_{3}=1.092\beta_{1}, ensuring perfect matching as described in the text. For the rest of the modes we assumed a linear dispersion, except when they are suppressed, in which case we setβi≈0\beta_{i}\approx 0. (a) Ideal FWM case obtained by suppressing all harmonics and high-order idlers. Notice the exponential gain achieved by perfect matching. (b) All nine modes are allowed to propagate. (c) The third harmonic (ω4=3​ω1\omega_{4}=3\omega_{1}) is suppressed.

Panel (a) considers the ideal degenerate FWM, meaning that only pump, signal and first idler are allowed to propagate. We achieve this situation by setting all other propagation constants close to zero. The perfect-matching condition is revealed by the exponential gain of the signal until saturation occurs.

In the simulation depicted in panel (b), all modes are allowed to propagate. We can see that, despite the fact that all of them interact, a signal gain still occurs.

In panel (c), the simulation allows all the waves but the third harmonic to propagate (ω4=3​ω1\omega_{4}=3\omega_{1},β4≈0\beta_{4}\approx 0). As anticipated in the previous subsection, the fifth harmonic is initially suppressed, but eventually excited. Its excitation and that of the high-order idlers limit the signal gain resulting in the need of a longer line to obtain a similar gain to that shown in panel (a). The signal gain aboveβ1​z≈3000\beta_{1}z\approx 3000can be improved if the matching condition is changed slightly or if the fifth harmonic is also suppressed. However, more importantly, the ideal situation of panel (a) is recovered if the idlers around the third harmonic (ω5\omega_{5}andω6\omega_{6}) are not allowed to propagate either. These simulations confirm that neglecting harmonics and high-order idlers can affect the achievable gain[19].

## IVExperiment & Methodology

In order to demonstrate the validity of the CMEs and the approach presented here, we have studied multiple harmonic generation in a superconducting transmission line. To achieve a parameter-free validation we have also determinedI∗′I^{\prime}_{*}independently by studying the dependence of the transmission of the sample,S21S_{21}, on applied DC current. The value found forI∗′I^{\prime}_{*}justifies our selection of harmonic generation over FWM for validation since it requires lower pump currents. Moreover, we complement these measurements with a determination of the critical current from resistance-current measurements using a sense resistor.

## IV.1SampleTable 1:Material PropertiesSiNbTiNϵr\epsilon_{r}ttTcT_{c}ρn\rho_{n}–nm\mathrm{nm}K\mathrm{K}µ​Ωcm\mathrm{\SIUnitSymbolMicro\SIUnitSymbolOhm}\text{\,}\mathrm{cm}11.86014.7132Figure 6:Schematics of the unit cell of the CPW DE line used in this work. Three loads,nin_{i}, are intercalated along a central line. The characteristics of the resulting sections are given in Table2. The CPW uses a NbTiN layer deposited over a Si substrate. The nominal material properties are given in Table1.Table 2:Parameters of Each Section of the Unit Cell.N1N_{1}N2N_{2}N3N_{3}N4N_{4}n1n_{1}n2n_{2}n3n_{3}# Stubs54798927402020w​(μ​m)w\,(\mu\mathrm{m})2338Z0​(Ω)Z_{0}\,(\Omega)6655v/cv/c0.0920.073αK\alpha_{K}0.620.58\begin{overpic}[scale={0.40},trim=0.0pt 50.18748pt 0.0pt 0.0pt,clip]{Figures/1b_gamma}
\put(0.0,52.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 0.0pt,clip]{Figures/1b_Zc}
\put(0.0,60.0){\footnotesize(b)}
\end{overpic}Figure 7:Simulated properties of the sample used in this work. (a) Propagation constant of the sample,γ\gamma, minus the propagation constant of the central line,γTL\gamma_{\mathrm{TL}}. This difference is normalized byd=1974µ​md=$1974\text{\,}\mathrm{\SIUnitSymbolMicro m}$, the length of the unit cell. (b) Characteristic impedance. Notice the strong frequency dependence, especially around the stopbands.

The sample used in this study is a CPW capacitively-loaded artificial superconducting transmission line from the same batch used in[25]and packaged in the same way. The superconductor is NbTiN deposited over a Si substrate, whose nominal properties are given in Table1. It has an engineered dispersion obtained by repeating 48 times the unit cell depicted in Fig.6with the number of capacitive stubs given in Table2. The central strip width and the gap to the ground plane are the same and equal to1.5µ​m1.5\text{\,}\mathrm{\SIUnitSymbolMicro m}. The characteristic impedance and phase velocity of each section, presented also in Table2, were obtained by simulation, using the methods described in[25]. Those values were used in turn to determine the properties of the entire DE transmission line (Fig.7).

## IV.2Experimental Setups\begin{overpic}[scale={0.4}]{Figures/Exp_setup_dc.pdf}
\put(48.0,-10.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4}]{Figures/Exp_setup_harm.pdf}
\put(48.0,-10.0){\footnotesize(b)}
\end{overpic}Figure 8:Experimental setups. (a) Measurement of the dependence ofS21S_{21}on applied DC current. The sample is kept in a cryostat, and it is connected to a VNA and a current source simultaneously using external bias tees. (b) A similar configuration is used to measure harmonic generation. The sample is connected at points A and B, via coaxial cables, to a signal generator, G, and a spectrum analyzer, S. No additional amplifiers were used to avoid their saturation or own harmonic generation. The maximum operating frequency of the VNA and spectrum analyzer is20GHz20\text{\,}\mathrm{GHz}.

As described in Fig.8, with the sample inside a cryostat, we measuredS21S_{21}under different DC currents, panel (a), and harmonic generation, panel (b). For the latter, in order to determine the actual incident and exiting powers,PAP_{A}andPBP_{B}, we performed an additional measurement. We removed the sample, terminated points A and B with shorts, and measured at cryogenic temperatures the resulting reflections. Assuming perfect matching of the cabling to the VNA, the reflections give two times the losses of each path. With the sample remaining in the cryostat, we also obtained a resistance-current plot using a two-point measurement with a sense resistor.

## IV.3Model forI∗I_{*}Determination

For modeling this experiment, following panel (a) of Fig.8, we start by constructing a transmission-matrix model of the signal path,Tc​1.TD​E.Tc​2T_{c1}.T_{DE}.T_{c2}, i.e., the DE sample between two lossy cables. We consider the case where we are well away from the stopbands so the sample is lossless resulting inγ=j​β\gamma=j\betaandZ=rZ=r. Then, the resulting ABCD matrix is converted to anSSmatrix assuming that the cables are perfectly matched to the VNA. The transmission term of such a matrix is calculated to beS21=2​j​e−(lc​1+lc​2)​γc​Z​Zc2​j​Z​Zc​cos⁡(β​l)−(Z2+Zc2)​sin⁡(β​l),S_{21}=\frac{2j\,e^{-(l_{c1}+l_{c2})\gamma_{c}}\,ZZ_{c}}{2jZZ_{c}\cos(\beta l)-(Z^{2}+Z_{c}^{2})\sin(\beta l)},(5)

whereZcZ_{c},γc\gamma_{c}, andlc​il_{ci}are the impedance, propagation constant, and lengths of the cables, andllis the total length of the sample. Now, when we apply a DC current to the system, due to the nonlinear inductance Eq. (1) and the fact that we are away from the stopbands, the impedance and propagation constant of the sample change, respectively, according toZi=g​ZoZ_{i}=gZ_{o}andβi=g​βo\beta_{i}=g\beta_{o}, whereg=[1+(ID​C/I∗′)2]1/2.g=\big[1+(I_{DC}/I^{\prime}_{*})^{2}\big]^{1/2}.

In these expressions,ZoZ_{o}andβo\beta_{o}are the values whenID​C=0I_{DC}=0. Finally, using Eq. (5), we calculate the ratio ofS21S_{21}with and without an applied current givingS21​(ID​C)S21​(0)=ZiZo​2​j​Zo​Zc​cos⁡(βo​l)−(Zo2+Zc2)​sin⁡(βo​l)2​j​Zi​Zc​cos⁡(βi​l)−(Zi2+Zc2)​sin⁡(βi​l),\frac{S_{21}(I_{DC})}{S_{21}(0)}=\frac{Z_{i}}{Z_{o}}\frac{2jZ_{o}Z_{c}\cos(\beta_{o}l)-(Z_{o}^{2}+Z_{c}^{2})\sin(\beta_{o}l)}{2jZ_{i}Z_{c}\cos(\beta_{i}l)-(Z_{i}^{2}+Z_{c}^{2})\sin(\beta_{i}l)},(6)

which removes the need for an independent characterization of the cables.

Equation (6) can be used to fit experimental data. Sinceβo\beta_{o}andZoZ_{o}can be taken from Fig.7, andZc=50ΩZ_{c}=$50\text{\,}\mathrm{\SIUnitSymbolOhm}$,I∗′I^{\prime}_{*}becomes the only free parameter of the model.

## IV.4Model for Harmonic GenerationFigure 9:Model for the study of harmonic generation. A fraction of the arriving input power,PAP_{A}, enters the sample,PaP_{a}, via the transmission coefficientT=4​Re⁡(Zc​Z∗)/|Zc+Z|2T=4\operatorname{Re}(Z_{c}Z^{*})/|Z_{c}+Z|^{2}and generates the rms currentIaI_{a}. This current is expressed as a normalized amplitude,A1​(0)A_{1}(0), usingI∗′I^{\prime}_{*}. Through the CMEs, the resulting normalized amplitudesAm​(l)A_{m}(l)at the end of the transmission line are calculated. They are converted back to current,IbI_{b}, and power inside the sample,PbP_{b}. Finally, the output powers generated in the coaxial output,PBP_{B}, are calculated. The impedance of the coaxial feeds was taken asZc=50ΩZ_{c}=$50\text{\,}\mathrm{\SIUnitSymbolOhm}$while the impedanceZZof the sample corresponds to that of the different harmonics as given by Fig.7.

To analyze the harmonic-generation experiment, we prepared the model detailed in Fig.9. Its input is the transmitted power of the injected tone into the sample,PaP_{a}. The power is converted to rms current and normalized byI∗′I^{\prime}_{*}, giving the initial condition for use in the CMEs. The reversed process gives the output powersPBP_{B}of the different harmonics.

For the CMEs, we took the lossless case withN=4N=4(ω1\omega_{1},ω2=3​ω1\omega_{2}=3\omega_{1},ω3=5​ω1\omega_{3}=5\omega_{1},ω4=7​ω1\omega_{4}=7\omega_{1}) within the SVEA approximation. We neglected losses for two reasons. First, the measurements were performed away from the stopbands where material losses are small and, second, within the experimental uncertainty of our measurements, their effect on harmonic generation could not be distinguished from the lossless case. The complex propagation constants and impedances required by the model were those given in Fig.7. In this manner, as with the previous model, the only free parameter isI∗′I^{\prime}_{*}.

## VResults and Discussion

## V.1Resistance-Current MeasurementsFigure 10:Normalized resistance-current measurement at different temperatures. Several steps, attributed to the presence of dissipative regions, and their evolution with temperature are clearly seen. The resistance is normalized byR1=40ΩR_{1}=$40\text{\,}\mathrm{\SIUnitSymbolOhm}$, the resistance reached by the first step at10K10\text{\,}\mathrm{K}. This temperature corresponds to the highest temperature with a well defined non-resistive region. At4K4\text{\,}\mathrm{K}, the onset of the first step is located atIC​1=1.8mAI_{C1}=$1.8\text{\,}\mathrm{mA}$, whileIC=2mAI_{C}=$2\text{\,}\mathrm{mA}$.

In Fig.10, we present the results of the resistance-current measurements, in normalized form, at different temperatures. The main common feature for all the curves is the presence of steps whose resistance values are independent of temperature. In contrast, the current onset of each step has a strong temperature dependence. Relevant for the measurement presented in the next sections is the first plateau with an onsetIC​1=0.9​ICI_{C1}=0.9I_{C}at4K4\text{\,}\mathrm{K}.

We notice that the steps reach a resistance that is only a small fraction of the resistance in the normal state,Rn≈1.5M​ΩR_{n}\approx$1.5\text{\,}\mathrm{M\SIUnitSymbolOhm}$, with a valueR1=40ΩR_{1}=$40\text{\,}\mathrm{\SIUnitSymbolOhm}$for the first step at10K10\text{\,}\mathrm{K}. These steps collapse to discrete multiples ofR1R_{1}indicating highly localized dissipation. The systematic shift of the plateaus towards higher currents as the temperature is lowered indicates that they are more difficult to form as the superconducting state becomes more robust. Furthermore, the nearly temperature-independent resistance values suggest that these states correspond to a small number of preferred dissipative configurations associated with the device geometry[28].

We also observe that the transition from one step to the other is not a well defined process but accompanied by fluctuations, signaling metastable states between successive dissipative configurations. This situation is further supported by the fact that the exactRR-IIcharacteristics depend on the current sweep protocol both in direction and current step.

## V.2Independent Determination ofI∗I_{*}Figure 11:Normalized transmission at4K4\text{\,}\mathrm{K}without applied DC current. Measured (gray) and simulated (blue). No fit was attempted.

We start by showing the measured transmission without applied current at4K4\text{\,}\mathrm{K}in Fig.11. The figure also shows the simulated transmission using the properties of the line presented in Fig.7. An excellent agreement between measurement and simulation is evident, with the stopbands differing only by a few hundredMHz\mathrm{MHz}. The small difference can easily be explained by reasonable deviations from the nominal values of the material properties given in Table1. Moreover, we also notice that the actual stopbands are broadened with respect to the simulation, likely due to either the finite number of unit cells or unmodeled losses in the line.\begin{overpic}[scale={0.4},trim=0.0pt 53.19875pt 0.0pt 0.0pt,clip]{Figures/S21_1GHz}
\put(91.0,45.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 52.19499pt 0.0pt 0.0pt,clip]{Figures/S21_4GHz}
\put(91.0,45.0){\footnotesize(b)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 0.0pt,clip]{Figures/S21_6GHz}
\put(91.0,56.0){\footnotesize(c)}
\end{overpic}Figure 12:Examples of the relative phase variation ofS21S_{21}with applied DC current. (a)1GHz1\text{\,}\mathrm{GHz}. (b)4GHz4\text{\,}\mathrm{GHz}. (c)6GHz6\text{\,}\mathrm{GHz}. Empty squares are measured data. Lines are plots of Eq. (6) usingI∗′=27mAI^{\prime}_{*}=$27\text{\,}\mathrm{mA}$, the global best-fit parameter at 551 frequency points, as described in the text.

Next, Fig.12shows the variation ofS21S_{21}with applied DC current. We performed a nonlinear least-squares fit of Eq. (6) to the measuredS21S_{21}variation using 551 frequency points from0.5GHzto6GHz0.5\text{\,}\mathrm{GHz}6\text{\,}\mathrm{GHz}. As the best-fit parameter we obtainedI∗′=27.116±0.007mAI^{\prime}_{*}=$27.116\pm 0.007\text{\,}\mathrm{mA}$. SinceαK≈0.6\alpha_{K}\approx 0.6(see Table2), we obtainI∗≈21mAI_{*}\approx$21\text{\,}\mathrm{mA}$. Surprisingly, this nonlinear parameter does not scale with the measuredICI_{C}but with the much larger depairing current as calculated from the Ginzburg-Landau theory[33].

From the measured values of the NbTiN film used to fabricate the sample (Table1), we obtain that its penetration depth isλ≈315nm\lambda\approx$315\text{\,}\mathrm{nm}$[37]. Moreover, as reported for similar films[36,20], we can take the coherence length asξ≈4nm\xi\approx$4\text{\,}\mathrm{nm}$. These two values allow us to calculate the depairing density current givingJdep≈2.54×1011Am−2J_{\mathrm{dep}}\approx$2.54\text{\times}{10}^{11}\text{\,}\mathrm{A}\text{\,}{\mathrm{m}}^{-2}$. Now, if we consider the central strip of the DE transmission line, which has a cross section of1.5µ​m×60nm$1.5\text{\,}\mathrm{\SIUnitSymbolMicro m}$\times$60\text{\,}\mathrm{nm}$, the depairing current for this specific sample becomesIdep≈23mAI_{\mathrm{dep}}\approx$23\text{\,}\mathrm{mA}$. We have obtained, thus, thatI∗∼Idep≫ICI_{*}\sim I_{\mathrm{dep}}\gg I_{C}, showing thatI∗I_{*}is governed by the intrinsic depairing mechanism and not by extrinsic defects in this sample.

## V.3Harmonic Generation\begin{overpic}[scale={0.4},trim=0.0pt 51.19124pt 0.0pt 0.0pt,clip]{Figures/PBn_2.3GHz.pdf}
\put(0.0,50.0){\footnotesize(a)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 52.19499pt 0.0pt 47.17624pt,clip]{Figures/PBn_3.5GHz.pdf}
\put(0.0,50.0){\footnotesize(b)}
\end{overpic}\begin{overpic}[scale={0.4},trim=0.0pt 0.0pt 0.0pt 47.17624pt,clip]{Figures/PBn_5.3GHz.pdf}
\put(0.0,60.0){\footnotesize(c)}
\end{overpic}Figure 13:Harmonic generation at three different fundamental tones. (a)2.3GHz2.3\text{\,}\mathrm{GHz}. (b)3.5GHz3.5\text{\,}\mathrm{GHz}. (c)5.3GHz5.3\text{\,}\mathrm{GHz}. Empty circles are measured data. Where not shown, the harmonics fell outside of the measuring window. Dashed lines are plots of the output powers predicted by the CMEs usingI∗′=27mAI^{\prime}_{*}=$27\text{\,}\mathrm{mA}$, as obtained from the fit presented in Fig.12. No fitting was attempted in this case. Within our resolution limit,−120dBm-120\text{\,}\mathrm{dBm}, we did not see the presence of even harmonics. The gray vertical line representsPA=−7dBmP_{A}=$-7\text{\,}\mathrm{dBm}$that marks the onset of the first resistive step identified in Fig.10. The breaking points do not necessarily coincide since every curve was obtained in different sweeps.

Fig.13gives three examples of the harmonic generation at different frequencies of the fundamental tone. Every curve was obtained in separate sweeps. Following Fig.9, we present the output powers at B,PB​nP_{Bn}, as a function of the incident powers of the fundamental tone at A,PAP_{A}. For the model presented in §IV.4, we have usedI∗′=27mAI^{\prime}_{*}=$27\text{\,}\mathrm{mA}$as obtained independently from theS21S_{21}vs.ID​CI_{DC}measurements. Notice that we did not attempt any fitting of the model to the experimental data. Up to an incident power of∼−7dB\sim$-7\text{\,}\mathrm{dB}$, a remarkable agreement between experimental data and model is obtained, confirming the validity of the CMEs and the methods used for describing the DE transmission line.

The results presented in Fig.13also show the presence of dissipative regions where superconductivity is disrupted. They manifest as a sudden decrease in the transmitted power. The entrance to the first step is clearly seen at an incident power of around−7dB-7\text{\,}\mathrm{dB}. As part of the model presented in §IV.4, this value can be converted to a normalized input amplitude, givingA1​(0)=0.07A_{1}(0)=0.07which coincides very well with the value ofIC​1/I∗′I_{C1}/I^{\prime}_{*}, further validating our methods.

## V.4Implications for Design

The fact thatI∗′>I∗∼Idep≫ICI^{\prime}_{*}>I_{*}\sim I_{\mathrm{dep}}\gg I_{C}has an important practical consequence, it limits the normalized amplitude with which a traveling-wave parametric device can be fed. This situation is further worsened by the appearance of the dissipative regions whose onset, fortunately, approachesICI_{C}at temperatures much lower thanTCT_{C}. In our sample, at4K4\text{\,}\mathrm{K}, the input amplitude is limited to only 7% ofI∗′I^{\prime}_{*}, preventing it from being used as a parametric amplifier when combined with its short length. Besides increasing the length of the transmission line, one practical solution is to increase its kinetic inductance fraction by using thinner superconducting films and decreasing its internal dimensions. In this way, one could achieveαK∼1\alpha_{K}\sim 1which, for our sample, maintaining everything else equal and taking into account thatI∗′=I∗/αKI^{\prime}_{*}=I_{*}/\sqrt{\alpha_{K}}, would translate into being able to achieveA1​(0)∼0.09A_{1}(0)\sim 0.09, nearly a 30% increase. Moreover, decreasing the film thickness, while maintaining the same fabrication quality, may have the advantage of increasingICI_{C}with respect toIdepI_{\mathrm{dep}}[30], allowing further increase ofA1​(0)A_{1}(0). Other groups have demonstrated gain[11,13,23]with designs consistent with these considerations.

Another important aspect to consider comes from the fact that kinetic-inductance traveling wave devices usually use capacitive stubs to compensate for the high inductance of the line. This geometry is prone to current crowding[17]further limiting the achievableICI_{C}. Rounding properly the intersections between the stubs and the central line may help to increaseICI_{C}. For our sample at least, we do not know if the critical current is limited by the presence of the stubs or by the central conductor of the CPW line.

## VIConclusions

We have presented a general and compact expression for obtaining the coupled mode equations for any parametric process in the presence of a quadratic nonlinearity in the inductance of a superconducting transmission line. Furthermore, the expression includes losses which can come not only from material properties but also from the presence of stopbands. We then presented several examples of the use of the equation to illustrate its versatility in representing any combination of traveling waves allowed by the mixing process.

The presented formulation was validated experimentally by studying harmonic generation in a dispersion-engineered superconducting transmission line. Importantly, we performed a parameter-free validation by combining simulations and measurements of the variation of the RF transmission of the line with applied DC current. On the one hand, the simulations allowed us to obtain the parameters of the studied transmission line, its propagation constant and characteristic impedance. On the other hand, the transmission vs.ID​CI_{DC}measurements permitted us to determine independently the nonlinear parameterI∗′I^{\prime}_{*}which normalizes the coupled mode equations. When using the obtained value forI∗′I^{\prime}_{*}and the simulated properties of the line, a remarkable agreement between theory and experiment was found. Furthermore, we found thatI∗′I^{\prime}_{*}does not scale with the critical current of the sample but with the more fundamental depairing current. This finding has profound implications for the design of traveling-wave parametric devices.

Our findings rigorously confirm the design choices made by other groups when fabricating kinetic-inductance traveling-wave devices, namely using thin superconducting films and long transmission lines. We also underscore the importance of increasing the achievable critical current so as to increase the normalized pump amplitude driving the parametric process inside the device.

## Acknowledgements.We thank Jochem Baselmans (Delft University of Technology and SRON, The Netherlands) for his invaluable support in the fabrication of the samples.
R. Finger and R. O. Berriel gratefully acknowledge support of ANID funds Basal FB210003 and ALMA 31240042.
The National Radio Astronomy Observatory and Green Bank Observatory are facilities of the U.S. National Science Foundation operated under cooperative agreement by Associated Universities, Inc.

## References
- [1]G. P. Agrawal(2019)Nonlinear fiber optics.6th edition,Academic Press,Cambridge, MA, USA.Cited by:§I,§III.2.
- [2]S.M. Anlage, H.J. Snortland, and M.R. Beasley(1989)A current controlled variable delay superconducting transmission line.IEEE Transactions on Magnetics25(2),pp. 1388–1391.External Links:DocumentCited by:§II.
- [3]J. Aumentado(2020)Superconducting parametric amplifiers: the state of the art in josephson parametric amplifiers.IEEE Microwave Magazine21(8),pp. 45–59.External Links:DocumentCited by:§I.
- [4]F. Aziz, K. Lin, P. Wen, Samina, Y. Lin, E. Weigand, C. Lee, Y. Cheng, Y. Lu, C. Chen, C. Chien, K. Hsieh, Y. Huang, H. Huang, H. Ian, J. Chen, Y. Lin, A. F. Kockum, G. Lin, and I. Hoi(2025)Nearly quantum-limited microwave amplification via interfering degenerate stimulated emission in a single artificial atom.npj Quantum Information11(1),pp. 45.External Links:Document,Link,ISSN 2056-6387Cited by:§I.
- [5]R. W. Boyd(2008)Nonlinear optics.3rd edition,Academic Press,Burlington, MA, USA.Cited by:§I,§III.2.
- [6]J. Carrasco, D. Valenzuela, C. Falcón, R. Finger, and F. P. Mena(2023)The effect of complex dispersion and characteristic impedance on the gain of superconducting traveling-wave kinetic inductance parametric amplifiers.IEEE Transactions on Applied Superconductivity33(3),pp. 1–9.External Links:DocumentCited by:§II.2,§II.
- [7]S. Chaudhuri, J. Gao, and K. Irwin(2015)Simulation and analysis of superconducting traveling-wave parametric amplifiers.IEEE Transactions on Applied Superconductivity25(3),pp. 1–5.External Links:DocumentCited by:§I.
- [8]S. Cho(1997)Temperature and current dependence of inductance in a superconducting meander line.J. Korean Phys. Soc.31(2),pp. 337.External Links:LinkCited by:§II.
- [9]A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf(2010-04)Introduction to quantum noise, measurement, and amplification.Rev. Mod. Phys.82,pp. 1155–1208.External Links:Document,LinkCited by:§I.
- [10]D. Cunnane, H. G. Leduc, N. Klimovich, F. Faramarzi, A. Beyer, and P. Day(2024-01)High-efficiency ka-band frequency multiplier based on the nonlinear kinetic inductance in a superconducting microstrip.Applied Physics Letters124(2),pp. 022601.External Links:ISSN 0003-6951,Document,LinkCited by:§I.
- [11]B. H. Eomet al.(2012)A wideband, low-noise superconducting amplifier with high dynamic range.Nature Phys8,pp. 623–627.Cited by:§I,§I,§I,§III.3,§V.4.
- [12]M. Esposito, A. Ranadive, L. Planat, and N. Roch(2021-09)Perspective on traveling wave microwave parametric amplifiers.Applied Physics Letters119(12),pp. 120501.External Links:ISSN 0003-6951,Document,LinkCited by:§I.
- [13]F. Faramarzi, R. Stephenson, S. Sypkens, B. H. Eom, H. LeDuc, and P. Day(2024-07)A 4–8 GHz kinetic inductance traveling-wave parametric amplifier using four-wave mixing with near quantum-limited noise performance.APL Quantum1(3),pp. 036107.External Links:ISSN 2835-0103,Document,LinkCited by:§I,§V.4.
- [14]L. Fasolo, A. Greco, and E. Enrico(2019)Superconducting josephson-based metamaterials for quantum-limited parametric amplification: a review.InAdvances in Condensed-Matter and Materials Physics - Rudimentary Research to Topical Technology,J. Thirumalai and S. I. Pokutnyi (Eds.),External Links:Document,LinkCited by:§I,§I.
- [15]J. Hansryd, P.A. Andrekson, M. Westlund, J. Li, and P.-O. Hedekvist(2002)Fiber-based optical parametric amplifiers and their applications.IEEE Journal of Selected Topics in Quantum Electronics8(3),pp. 506–520.External Links:DocumentCited by:§III.3.
- [16]Z. Hao, J. Cochran, Y.-C. Chang, H. M. Cole, and S. Shankar(2026-01)Wireless Josephson parametric amplifier above 20 GHz.Applied Physics Letters128(1),pp. 014004.External Links:ISSN 0003-6951,Document,LinkCited by:§I.
- [17]H. L. Hortensius, E. F. C. Driessen, T. M. Klapwijk, K. K. Berggren, and J. R. Clem(2012-05)Critical-current reduction in thin superconducting wires due to current crowding.Applied Physics Letters100(18),pp. 182602.External Links:ISSN 0003-6951,Document,LinkCited by:§V.4.
- [18]W. Huang(1994-03)Coupled-mode theory for optical waveguides: an overview.J. Opt. Soc. Am. A11(3),pp. 963–983.External Links:Link,DocumentCited by:§I.
- [19]N. Klimovich, S. Wood, P. K. Day, and B. Tan(2024-03)Investigating the effects of sum-frequency conversions and surface impedance uniformity in traveling wave superconducting parametric amplifiers.Journal of Applied Physics135(12),pp. 124402.External Links:ISSN 0021-8979,Document,LinkCited by:§I,§III.3.
- [20]Y. Lee, J. Yun, C. Lee,et al.(2024)Penetration depth in dirty superconducting NbTiN thin films grown at room temperature.Applied Physics A130,pp. 504.External Links:DocumentCited by:§V.2.
- [21]H. Li, M. Scigliuzzo, E. Guzovskii, S. Han, K. Han, and T. J. Kippenberg(2026)Quantum-limited traveling-wave parametric amplifier based on DUV lithography-defined planar structures.External Links:2603.14455,LinkCited by:§I.
- [22]J. C. Longden and B.-K. Tan(2024)Non-degenerate-pump four-wave mixing kinetic inductance travelling-wave parametric amplifiers.Eng. Res. Express6(1),pp. 015068.External Links:DocumentCited by:§II.2,§II.
- [23]M. Malnou, M.R. Vissers, J.D. Wheeler, J. Aumentado, J. Hubmayr, J.N. Ullom, and J. Gao(2021-01)Three-wave mixing kinetic inductance traveling-wave amplifier with near-quantum-limited noise performance.PRX Quantum2,pp. 010302.External Links:Document,LinkCited by:§V.4.
- [24]M. E. Marhic(2007)Fiber optical parametric amplifiers, oscillators and related devices.Cambridge Univ. Press,Cambridge, U.K..Cited by:§I,§III.2.
- [25]F. P. Mena, D. Valenzuela, C. Espinoza, F. Pizarro, B.-K. Tan, D. J. Thoen, J. J. A. Baselmans, and R. Finger(2024)Modeling and testing superconducting artificial CPW lines suitable for parametric amplification.IEEE Transactions on Applied Superconductivity34(6),pp. 1–8.External Links:DocumentCited by:§IV.1.
- [26]S. Pagano, C. Barone, M. Borghesi, W. Chung, G. Carapella, A. P. Caricato, I. Carusotto, A. Cian, D. D. Gioacchino, E. Enrico, P. Falferi, L. Fasolo, M. Faverzani, E. Ferri, G. Filatrella, C. Gatti, A. Giachero, D. Giubertoni, A. Greco, C. Kutlu, A. Leo, C. Ligi, G. Maccarrone, B. Margesin, G. Maruccio, A. Matlashov, C. Mauro, R. Mezzena, A. G. Monteduro, A. Nucciotti, L. Oberto, V. Pierro, L. Piersanti, M. Rajteri, A. Rettaroli, S. Rizzato, Y. K. Semertzidis, S. Uchaikin, and A. Vinante(2022)Development of quantum limited superconducting amplifiers for advanced detection.IEEE Transactions on Applied Superconductivity32(4),pp. 1–5.External Links:DocumentCited by:§I.
- [27]A. Roy and M. Devoret(2016)Introduction to parametric amplification of quantum signals with josephson circuits.Comptes Rendus Physique17(7),pp. 740–755.Note:Quantum microwaves / Micro-ondes quantiquesExternal Links:ISSN 1631-0705,Document,LinkCited by:§I.
- [28]W. J. Skocpol, M. R. Beasley, and M. Tinkham(1974-09)Self‐heating hotspots in superconducting thin‐film microbridges.Journal of Applied Physics45(9),pp. 4054–4066.External Links:ISSN 0021-8979,Document,LinkCited by:§V.1.
- [29]L. J. Splitthoff, J. J. Wesdorp, M. Pita-Vidal, A. Bargerbos, Y. Liu, and C. K. Andersen(2024-01)Gate-tunable kinetic inductance parametric amplifier.Phys. Rev. Appl.21,pp. 014052.External Links:Document,LinkCited by:§I.
- [30]G. Stejic, A. Gurevich, E. Kadyrov, D. Christen, R. Joynt, and D. C. Larbalestier(1994-01)Effect of geometry on the critical currents of thin films.Phys. Rev. B49,pp. 1274–1288.External Links:Document,LinkCited by:§V.4.
- [31]R. Stolen and J. Bjorkholm(1982)Parametric amplification and frequency conversion in optical fibers.IEEE Journal of Quantum Electronics18(7),pp. 1062–1072.External Links:DocumentCited by:§II.3.
- [32]Y. Sun, X. Li, Q. Wang, T. Bai, X. Liao, D. Lan, J. Zhao, and Y. Yu(2025-06)Broadband merged-element josephson parametric amplifier.Applied Physics Letters126(24),pp. 244005.External Links:ISSN 0003-6951,Document,LinkCited by:§I.
- [33]M. Tinkham(1996)Introduction to superconductivity.2nd edition,Dover Publications,Mineola, New York.External Links:ISBN 978-0-486-43503-9Cited by:§V.2.
- [34]A. Yariv(1973)Coupled-mode theory for guided-wave optics.IEEE Journal of Quantum Electronics9(9),pp. 919–933.External Links:DocumentCited by:§I.
- [35]Cited by:Coupled-Mode Equations with Arbitrary Mode Combinations for Kinetic-Inductance Superconducting Traveling-Wave Parametric Devices: Theory and Experimental Validation.
- [36]L. Yu, N. Newman, and J. M. Rowell(2002)Measurement of the coherence length of sputtered Nb0.62Ti0.38N thin films.IEEE Transactions on Applied Superconductivity12(2),pp. 1795–1798.External Links:DocumentCited by:§V.2.
- [37]J. Zmuidzinas(2012)Superconducting microresonators: physics and applications.Annual Review of Condensed Matter Physics3(Volume 3, 2012),pp. 169–214.External Links:Document,Link,ISSN 1947-5462Cited by:§I,§II,§V.2.


## 


- 


Major funding support from
